#!/usr/bin/env python3
"""Small-business unit economics helpers (stdlib, Decimal).

Breakeven, CAC payback and retention math. Inputs are the owner's own figures;
label each as actual, estimate or target. Selftest figures are illustrative.
Numbers from this tool win over model arithmetic.

Usage:
  python unit_economics.py --selftest
  python unit_economics.py breakeven --fixed 12000 --price 50 --variable 20
  python unit_economics.py payback --cac 600 --monthly-revenue 100 --gross-margin-pct 60
  python unit_economics.py retention --start 100000 --expansion 12000 --contraction 3000 --churn 5000
"""
import argparse
import math
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def breakeven(fixed, price, variable):
    cm = D(price) - D(variable)
    if cm <= 0:
        raise ValueError("price must exceed variable cost per unit")
    if D(fixed) < 0:
        raise ValueError("fixed must be >= 0")
    units = D(fixed) / cm
    return {"contribution_per_unit": q(cm), "units": int(math.ceil(units)),
            "contribution_margin_pct": q(cm / D(price) * 100)}


def payback(cac, monthly_revenue, gross_margin_pct):
    gp = D(monthly_revenue) * D(gross_margin_pct) / 100
    if gp <= 0:
        raise ValueError("monthly gross profit must be > 0")
    if D(cac) < 0:
        raise ValueError("cac must be >= 0")
    return {"monthly_gross_profit": q(gp), "payback_months": q(D(cac) / gp)}


def retention(start, expansion, contraction, churn):
    s = D(start)
    if s <= 0:
        raise ValueError("start must be > 0")
    if min(D(expansion), D(contraction), D(churn)) < 0:
        raise ValueError("inputs must be >= 0")
    nrr = (s + D(expansion) - D(contraction) - D(churn)) / s * 100
    grr = (s - D(contraction) - D(churn)) / s * 100
    return {"nrr_pct": q(nrr), "grr_pct": q(grr)}


def selftest():
    b = breakeven(12000, 50, 20)
    assert b["units"] == 400 and b["contribution_margin_pct"] == D("60.00")
    assert breakeven(12001, 50, 20)["units"] == 401
    assert payback(600, 100, 60)["payback_months"] == D("10.00")
    r = retention(100000, 12000, 3000, 5000)
    assert r["nrr_pct"] == D("104.00") and r["grr_pct"] == D("92.00")
    for bad in (lambda: breakeven(1, 10, 10), lambda: payback(1, 0, 50), lambda: retention(0, 0, 0, 0)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("unit_economics selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    b = sub.add_parser("breakeven")
    for k in ("fixed", "price", "variable"):
        b.add_argument("--" + k, required=True)
    p = sub.add_parser("payback")
    for k in ("cac", "monthly-revenue", "gross-margin-pct"):
        p.add_argument("--" + k, required=True)
    r = sub.add_parser("retention")
    for k in ("start", "expansion", "contraction", "churn"):
        r.add_argument("--" + k, required=True)
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "breakeven":
        print(breakeven(a.fixed, a.price, a.variable))
    elif a.cmd == "payback":
        print(payback(a.cac, a.monthly_revenue, a.gross_margin_pct))
    elif a.cmd == "retention":
        print(retention(a.start, a.expansion, a.contraction, a.churn))
    else:
        ap.print_help(); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
