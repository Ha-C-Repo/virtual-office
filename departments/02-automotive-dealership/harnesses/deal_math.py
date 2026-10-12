#!/usr/bin/env python3
"""Dealership deal arithmetic (stdlib, Decimal).

Arithmetic only. Advertised payments, APR and finance disclosures must follow
dealer ad law and the lender's terms ({{STATE}} rules, VERIFY). Tax rules and
which fees are taxable come from {{PLACEHOLDERS}} supplied by the dealer.
Numbers from this tool win over model arithmetic. Selftest figures are illustrative.

Usage:
  python deal_math.py --selftest
  python deal_math.py payment --principal 20000 --apr 6 --months 60
  python deal_math.py financed --price 15000 --tax-pct 6.25 --fees 200 --down 1000 \
      --trade-allowance 3000 --trade-payoff 1000 [--trade-reduces-tax]
  python deal_math.py ltv --financed 13137.5 --value 12000
  python deal_math.py gross --price 15000 --acquisition 11000 --recon 800 [--other 150]
  python deal_math.py aging --acquired 2026-07-01 --today 2026-10-12
"""
import argparse
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def payment(principal, apr_pct, months):
    p, n = D(principal), int(months)
    if p < 0 or n <= 0 or D(apr_pct) < 0:
        raise ValueError("principal >= 0, months > 0, apr >= 0 required")
    if D(apr_pct) == 0:
        return p / n
    r = D(apr_pct) / 1200
    return p * r / (1 - (1 + r) ** (-n))


def financed(price, tax_pct, fees, down, trade_allowance=0, trade_payoff=0,
             trade_reduces_tax=False):
    price, allowance = D(price), D(trade_allowance)
    base = price - allowance if trade_reduces_tax else price
    if base < 0:
        raise ValueError("taxable base is negative")
    tax = base * D(tax_pct) / 100
    total = price + tax + D(fees) - D(down) - allowance + D(trade_payoff)
    return {"tax": q(tax), "amount_financed": q(total)}


def ltv(financed_amt, value):
    if D(value) <= 0:
        raise ValueError("value must be > 0")
    return D(financed_amt) / D(value) * 100


def gross(price, acquisition, recon=0, other=0):
    g = D(price) - D(acquisition) - D(recon) - D(other)
    return {"gross": q(g), "gross_pct_of_price": q(g / D(price) * 100) if D(price) else None}


def aging(acquired, today):
    days = (date.fromisoformat(today) - date.fromisoformat(acquired)).days
    if days < 0:
        raise ValueError("acquired date is after today")
    bucket = "0-30" if days <= 30 else "31-60" if days <= 60 else "61-90" if days <= 90 else "90+"
    return {"days": days, "bucket": bucket}


def selftest():
    assert q(payment(20000, 6, 60)) == D("386.66")
    assert q(payment(12000, 0, 48)) == D("250.00")
    f = financed(15000, "6.25", 200, 1000, 3000, 1000)
    assert f["tax"] == D("937.50") and f["amount_financed"] == D("13137.50")
    f2 = financed(15000, "6.25", 200, 1000, 3000, 1000, trade_reduces_tax=True)
    assert f2["tax"] == D("750.00") and f2["amount_financed"] == D("12950.00")
    assert q(ltv("13137.5", 12000)) == D("109.48")
    g = gross(15000, 11000, 800, 150)
    assert g["gross"] == D("3050.00") and g["gross_pct_of_price"] == D("20.33")
    assert aging("2026-07-01", "2026-10-12") == {"days": 103, "bucket": "90+"}
    assert aging("2026-09-20", "2026-10-12")["bucket"] == "0-30"
    for bad in (lambda: payment(1, 5, 0), lambda: ltv(1, 0), lambda: aging("2026-12-01", "2026-10-12"),
                lambda: payment(-1, 5, 12)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("deal_math selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("payment")
    p.add_argument("--principal", required=True); p.add_argument("--apr", required=True)
    p.add_argument("--months", required=True, type=int)
    f = sub.add_parser("financed")
    f.add_argument("--price", required=True); f.add_argument("--tax-pct", required=True)
    f.add_argument("--fees", default="0"); f.add_argument("--down", default="0")
    f.add_argument("--trade-allowance", default="0"); f.add_argument("--trade-payoff", default="0")
    f.add_argument("--trade-reduces-tax", action="store_true")
    l = sub.add_parser("ltv")
    l.add_argument("--financed", required=True); l.add_argument("--value", required=True)
    g = sub.add_parser("gross")
    g.add_argument("--price", required=True); g.add_argument("--acquisition", required=True)
    g.add_argument("--recon", default="0"); g.add_argument("--other", default="0")
    ag = sub.add_parser("aging")
    ag.add_argument("--acquired", required=True); ag.add_argument("--today", required=True)
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "payment":
        print(q(payment(a.principal, a.apr, a.months)))
    elif a.cmd == "financed":
        print(financed(a.price, a.tax_pct, a.fees, a.down, a.trade_allowance, a.trade_payoff, a.trade_reduces_tax))
    elif a.cmd == "ltv":
        print(q(ltv(a.financed, a.value)))
    elif a.cmd == "gross":
        print(gross(a.price, a.acquisition, a.recon, a.other))
    elif a.cmd == "aging":
        print(aging(a.acquired, a.today))
    else:
        ap.print_help(); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
