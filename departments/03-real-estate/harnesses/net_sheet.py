#!/usr/bin/env python3
"""Seller net sheet and CMA adjustment math (stdlib, Decimal).

Arithmetic only. Commission rates, closing costs, prorations and payoff figures
come from the contract, the title company and the lender (VERIFY). Selftest
figures are illustrative. Numbers from this tool win over model arithmetic.

Usage:
  python net_sheet.py --selftest
  python net_sheet.py net --price 300000 --list-pct 3 --buyer-pct 3 --closing 2500 \
      --payoff 180000 --concessions 5000 --repairs 1500 --prorations 1200
  python net_sheet.py cma --file comps.json
comps.json: [{"price": 310000, "adjustments": [5000, -2000]}, ...]
"""
import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext
from statistics import median

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def net_sheet(price, list_pct, buyer_pct, closing, payoff, concessions=0, repairs=0, prorations=0):
    price = D(price)
    if price <= 0:
        raise ValueError("price must be > 0")
    for v in (list_pct, buyer_pct, closing, payoff, concessions, repairs, prorations):
        if D(v) < 0:
            raise ValueError("inputs must be >= 0")
    if D(list_pct) + D(buyer_pct) >= 100:
        raise ValueError("commission percentages must total < 100")
    comm = price * (D(list_pct) + D(buyer_pct)) / 100
    deductions = comm + D(closing) + D(payoff) + D(concessions) + D(repairs) + D(prorations)
    net = price - deductions
    return {"price": q(price), "commission": q(comm), "other_deductions": q(deductions - comm),
            "net_proceeds": q(net), "net_pct_of_price": q(net / price * 100)}


def cma(comps):
    if not comps:
        raise ValueError("no comps")
    adj = [D(c["price"]) + sum((D(a) for a in c.get("adjustments", [])), Decimal(0)) for c in comps]
    if any(a <= 0 for a in adj):
        raise ValueError("adjusted price must be > 0")
    mean = sum(adj, Decimal(0)) / len(adj)
    return {"adjusted": [q(a) for a in adj], "mean": q(mean), "median": q(median(adj)),
            "low": q(min(adj)), "high": q(max(adj))}


def selftest():
    r = net_sheet(300000, 3, 3, 2500, 180000, 5000, 1500, 1200)
    assert r["commission"] == D("18000.00") and r["net_proceeds"] == D("91800.00")
    assert r["net_pct_of_price"] == D("30.60")
    c = cma([{"price": 310000, "adjustments": [5000, -2000]}, {"price": 295000},
             {"price": 305000, "adjustments": [-3000]}])
    assert c["adjusted"] == [D("313000.00"), D("295000.00"), D("302000.00")]
    assert c["mean"] == D("303333.33") and c["median"] == D("302000.00")
    for bad in (lambda: net_sheet(0, 3, 3, 0, 0), lambda: net_sheet(100, 60, 40, 0, 0),
                lambda: cma([]), lambda: net_sheet(100, -1, 3, 0, 0)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("net_sheet selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("net")
    for k in ("price", "list-pct", "buyer-pct", "closing", "payoff"):
        n.add_argument("--" + k, required=True)
    for k in ("concessions", "repairs", "prorations"):
        n.add_argument("--" + k, default="0")
    c = sub.add_parser("cma"); c.add_argument("--file", required=True)
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "net":
        print(json.dumps(net_sheet(a.price, a.list_pct, a.buyer_pct, a.closing, a.payoff,
                                   a.concessions, a.repairs, a.prorations), indent=2, default=str))
    elif a.cmd == "cma":
        with open(a.file) as f:
            print(json.dumps(cma(json.load(f)), indent=2, default=str))
    else:
        ap.print_help(); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
