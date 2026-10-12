#!/usr/bin/env python3
"""Job costing, margin and workers compensation helpers (stdlib, Decimal).

All figures in selftests are illustrative. Real rates, burdens and targets come
from {{PLACEHOLDERS}} supplied by the owner. Numbers from this tool win over
model arithmetic.

Usage:
  python job_cost.py --selftest
  python job_cost.py rollup --file job.json [--overhead-hours H --overhead-rate R]
  python job_cost.py convert --margin 30
  python job_cost.py convert --markup 42.857
  python job_cost.py price --cost 10000 --margin 32
  python job_cost.py overhead --annual-overhead 240000 --billable-hours 6000
  python job_cost.py wc --payroll 50000 --rate 12.5
job.json: {"revenue": 0, "costs": {"labor": 0, "labor_taxes": 0, "materials": 0}}
"""
import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")
DIRECT_KEYS = ["labor", "labor_taxes", "materials", "subcontractors", "disposal",
               "permits", "commissions", "transportation", "warranty_reserve",
               "workers_comp", "other"]


def D(x):
    return Decimal(str(x))


def q(x, places=CENT):
    return D(x).quantize(places, rounding=ROUND_HALF_UP)


def workers_comp_premium(payroll, rate_per_100):
    """payroll / 100 x rate, per class code. The rate comes from the carrier (VERIFY)."""
    if D(payroll) < 0 or D(rate_per_100) < 0:
        raise ValueError("payroll and rate must be >= 0")
    return D(payroll) / 100 * D(rate_per_100)


def overhead_per_hour(annual_overhead, billable_hours):
    if D(billable_hours) <= 0:
        raise ValueError("billable_hours must be > 0")
    if D(annual_overhead) < 0:
        raise ValueError("annual_overhead must be >= 0")
    return D(annual_overhead) / D(billable_hours)


def margin_to_markup(margin_pct):
    m = D(margin_pct) / 100
    if not (0 <= m < 1):
        raise ValueError("margin must be >= 0 and < 100")
    return m / (1 - m) * 100


def markup_to_margin(markup_pct):
    k = D(markup_pct) / 100
    if k < 0:
        raise ValueError("markup must be >= 0")
    return k / (1 + k) * 100


def price_for_margin(cost, margin_pct):
    m = D(margin_pct) / 100
    if not (0 <= m < 1):
        raise ValueError("margin must be >= 0 and < 100")
    return D(cost) / (1 - m)


def rollup(revenue, costs, overhead_hours=0, overhead_rate=0):
    """Roll up direct costs; optionally absorb overhead by labor hours."""
    unknown = set(costs) - set(DIRECT_KEYS)
    if unknown:
        raise ValueError("unknown cost keys: " + ", ".join(sorted(unknown)))
    if any(D(v) < 0 for v in costs.values()):
        raise ValueError("costs must be >= 0")
    rev = D(revenue)
    direct = sum((D(v) for v in costs.values()), Decimal(0))
    gp = rev - direct
    oh = D(overhead_hours) * D(overhead_rate)
    net = gp - oh
    return {
        "revenue": q(rev),
        "direct_costs": q(direct),
        "gross_profit": q(gp),
        "gross_margin_pct": q(gp / rev * 100) if rev else None,
        "markup_on_cost_pct": q(gp / direct * 100) if direct else None,
        "overhead_absorbed": q(oh),
        "net_profit_after_overhead": q(net),
        "net_margin_pct": q(net / rev * 100) if rev else None,
        "cost_breakdown": {k: q(costs[k]) for k in DIRECT_KEYS if k in costs},
    }


def selftest():
    # margin / markup conversions: 30 percent margin = 42.857 percent markup
    assert q(margin_to_markup(30), Decimal("0.001")) == D("42.857")
    assert q(markup_to_margin(50), Decimal("0.001")) == D("33.333")
    assert q(markup_to_margin(margin_to_markup(25))) == D("25.00")
    assert q(price_for_margin(10000, 30)) == D("14285.71")
    # a 30 percent markup is NOT a 30 percent margin
    assert q(markup_to_margin(30)) == D("23.08")
    # overhead per billable hour
    assert q(overhead_per_hour(240000, 6000)) == D("40.00")
    # workers comp: payroll / 100 x rate
    assert q(workers_comp_premium(50000, "12.5")) == D("6250.00")
    # rollup (illustrative job)
    costs = {"labor": 4000, "labor_taxes": 400, "materials": 5000, "disposal": 300,
             "permits": 150, "workers_comp": 500, "warranty_reserve": 200}
    r = rollup(16000, costs, overhead_hours=80, overhead_rate=40)
    assert r["direct_costs"] == D("10550.00")
    assert r["gross_profit"] == D("5450.00")
    assert r["gross_margin_pct"] == D("34.06")
    assert r["overhead_absorbed"] == D("3200.00")
    assert r["net_profit_after_overhead"] == D("2250.00")
    assert r["net_margin_pct"] == D("14.06")
    # zero revenue is safe
    assert rollup(0, {"labor": 10})["gross_margin_pct"] is None
    for bad in (lambda: rollup(1, {"bogus": 1}), lambda: margin_to_markup(100),
                lambda: overhead_per_hour(1, 0), lambda: rollup(1, {"labor": -1})):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("job_cost selftest OK")


def main(argv=None):
    p = argparse.ArgumentParser(description="Job cost helpers")
    p.add_argument("--selftest", action="store_true")
    sub = p.add_subparsers(dest="cmd")
    r = sub.add_parser("rollup")
    r.add_argument("--file", required=True)
    r.add_argument("--overhead-hours", type=float, default=0)
    r.add_argument("--overhead-rate", type=float, default=0)
    c = sub.add_parser("convert")
    c.add_argument("--margin", type=float)
    c.add_argument("--markup", type=float)
    pr = sub.add_parser("price")
    pr.add_argument("--cost", type=float, required=True)
    pr.add_argument("--margin", type=float, required=True)
    o = sub.add_parser("overhead")
    o.add_argument("--annual-overhead", type=float, required=True)
    o.add_argument("--billable-hours", type=float, required=True)
    w = sub.add_parser("wc")
    w.add_argument("--payroll", type=float, required=True)
    w.add_argument("--rate", type=float, required=True)
    a = p.parse_args(argv)
    if a.selftest:
        selftest()
        return 0
    try:
        if a.cmd == "rollup":
            with open(a.file, encoding="utf-8") as f:
                job = json.load(f)
            print(json.dumps(rollup(job["revenue"], job["costs"], a.overhead_hours,
                                    a.overhead_rate), indent=2, default=str))
        elif a.cmd == "convert":
            if (a.margin is None) == (a.markup is None):
                p.error("give exactly one of --margin or --markup")
            if a.margin is not None:
                print("markup_pct:", q(margin_to_markup(a.margin), Decimal("0.001")))
            else:
                print("margin_pct:", q(markup_to_margin(a.markup), Decimal("0.001")))
        elif a.cmd == "price":
            print("price:", q(price_for_margin(a.cost, a.margin)))
        elif a.cmd == "overhead":
            print("overhead_per_billable_hour:", q(overhead_per_hour(a.annual_overhead, a.billable_hours)))
        elif a.cmd == "wc":
            print("premium:", q(workers_comp_premium(a.payroll, a.rate)))
        else:
            p.print_help()
            return 2
    except (ValueError, KeyError, OSError) as e:
        print("error:", e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
