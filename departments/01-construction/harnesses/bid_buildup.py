#!/usr/bin/env python3
"""Steel tonnage and bid price build-up (stdlib, Decimal).

Weights per foot come from the published section tables the estimator uses
(VERIFY); this tool does not contain them. Rates, allowances and markups are
{{PLACEHOLDERS}} from the owner. Selftest figures are illustrative.
Numbers from this tool win over model arithmetic.

Usage:
  python bid_buildup.py --selftest
  python bid_buildup.py price --file bid.json
bid.json:
  {"members": [{"mark": "B1", "qty": 10, "length_ft": 20, "lb_per_ft": 30}],
   "waste_pct": 3, "connection_pct": 10, "material_per_ton": 1500,
   "labor_hr_per_ton": 20, "labor_rate": 60,
   "markups": [["overhead", 10], ["contingency", 5], ["profit", 8], ["bond", 1.5]]}
Markups apply in the listed order, each on the running total.
"""
import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")
LB_PER_TON = Decimal(2000)


def D(x):
    return Decimal(str(x))


def q(x, places=CENT):
    return D(x).quantize(places, rounding=ROUND_HALF_UP)


def tonnage(members, waste_pct=0, connection_pct=0):
    lb = Decimal(0)
    for m in members:
        if min(D(m["qty"]), D(m["length_ft"]), D(m["lb_per_ft"])) < 0:
            raise ValueError("member values must be >= 0")
        lb += D(m["qty"]) * D(m["length_ft"]) * D(m["lb_per_ft"])
    if D(waste_pct) < 0 or D(connection_pct) < 0:
        raise ValueError("percentages must be >= 0")
    base = lb / LB_PER_TON
    total = base * (1 + D(waste_pct) / 100) * (1 + D(connection_pct) / 100)
    return {"member_lb": q(lb), "base_tons": q(base, Decimal("0.001")), "total_tons": q(total, Decimal("0.001")), "_exact": total}


def price(bid):
    t = tonnage(bid["members"], bid.get("waste_pct", 0), bid.get("connection_pct", 0))
    tons = t["_exact"]
    material = tons * D(bid["material_per_ton"])
    hours = tons * D(bid["labor_hr_per_ton"])
    labor = hours * D(bid["labor_rate"])
    direct = material + labor
    running, steps = direct, []
    for name, pct in bid.get("markups", []):
        if D(pct) < 0:
            raise ValueError("markups must be >= 0")
        amt = running * D(pct) / 100
        running += amt
        steps.append({"markup": name, "pct": str(pct), "amount": q(amt), "running_total": q(running)})
    return {"total_tons": t["total_tons"], "material": q(material), "labor_hours": q(hours),
            "labor": q(labor), "direct_cost": q(direct), "steps": steps, "bid_price": q(running)}


def selftest():
    bid = {"members": [{"mark": "B1", "qty": 10, "length_ft": 20, "lb_per_ft": 30},
                       {"mark": "C1", "qty": 5, "length_ft": 40, "lb_per_ft": 50}],
           "waste_pct": 3, "connection_pct": 10, "material_per_ton": 1500,
           "labor_hr_per_ton": 20, "labor_rate": 60,
           "markups": [["overhead", 10], ["contingency", 5], ["profit", 8], ["bond", 1.5]]}
    t = tonnage(bid["members"], 3, 10)
    assert t["member_lb"] == D("16000.00") and t["base_tons"] == D("8.000")
    assert t["total_tons"] == D("9.064")
    r = price(bid)
    assert r["material"] == D("13596.00") and r["labor"] == D("10876.80")
    assert r["direct_cost"] == D("24472.80")
    assert r["steps"][0]["running_total"] == D("26920.08")
    assert r["bid_price"] == D("30985.28")
    assert price({"members": [], "material_per_ton": 1, "labor_hr_per_ton": 1, "labor_rate": 1})["bid_price"] == D("0.00")
    for bad in (lambda: tonnage([{"qty": -1, "length_ft": 1, "lb_per_ft": 1}]),
                lambda: tonnage([], waste_pct=-1)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("bid_buildup selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("price"); p.add_argument("--file", required=True)
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "price":
        with open(a.file) as f:
            print(json.dumps(price(json.load(f)), indent=2, default=str))
        return 0
    ap.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
