#!/usr/bin/env python3
"""Insurance claim payment math (stdlib, Decimal). Illustrative arithmetic only.

Not legal or adjusting advice. Policy language and state rules control (VERIFY).
Numbers from this tool win over model arithmetic.

Usage:
  python claim_math.py --selftest
  python claim_math.py --rcv 30000 --dep-amount 10000 --deductible 2000
  python claim_math.py --rcv 30000 --dep-pct 33 --deductible 2000 \
      --supplement 1500 --supplement 800 --op-pct 0 --json
"""
import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def money(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def claim(rcv, dep_amount=None, dep_pct=None, deductible=0, supplements=(),
          op_pct=0, recoverable=True, nonrecoverable_amount=0):
    """Compute the claim position.

    rcv: replacement cost value of the carrier scope (before O&P).
    dep_amount or dep_pct (percent of RCV): total depreciation withheld.
    supplements: approved supplement RCV amounts added after the initial scope.
        Depreciation on supplements is taken at the same percentage as the base.
    op_pct: overhead and profit percent applied to RCV when allowed (VERIFY).
    recoverable: whether withheld depreciation is paid on completion.
    nonrecoverable_amount: portion of depreciation never paid back (policy terms).
    """
    rcv = D(rcv)
    if rcv < 0:
        raise ValueError("rcv must be >= 0")
    if (dep_amount is None) == (dep_pct is None):
        raise ValueError("give exactly one of dep_amount or dep_pct")
    if dep_amount is not None:
        dep = D(dep_amount)
        pct = (dep / rcv * 100) if rcv else Decimal(0)
    else:
        pct = D(dep_pct)
        dep = rcv * pct / 100
    if dep < 0 or dep > rcv:
        raise ValueError("depreciation must be between 0 and RCV")
    ded = D(deductible)
    if ded < 0:
        raise ValueError("deductible must be >= 0")
    op = D(op_pct)
    sup = [D(s) for s in supplements]
    if any(s < 0 for s in sup):
        raise ValueError("supplements must be >= 0")

    base_total = rcv * (1 + op / 100)
    base_dep = dep * (1 + op / 100)
    sup_total = sum(sup, Decimal(0)) * (1 + op / 100)
    sup_dep = sup_total * pct / 100
    total_rcv = base_total + sup_total
    total_dep = base_dep + sup_dep
    acv = total_rcv - total_dep
    base_acv = base_total - base_dep
    initial_acv_payment = max(base_acv - ded, Decimal(0))
    nonrec = D(nonrecoverable_amount)
    recoverable_dep = (total_dep - nonrec) if recoverable else Decimal(0)
    if recoverable_dep < 0:
        recoverable_dep = Decimal(0)
    # Supplement ACV is paid as approved; depreciation on it is released at completion.
    supplement_acv = sup_total - sup_dep
    # If base ACV is smaller than the deductible, the remainder reduces later payments.
    deductible_unapplied = max(ded - base_acv, Decimal(0))
    supplement_payment = max(supplement_acv - deductible_unapplied, Decimal(0))
    total_expected = initial_acv_payment + supplement_payment + recoverable_dep
    out = {
        "rcv_scope": money(base_total),
        "supplements_rcv": money(sup_total),
        "total_rcv": money(total_rcv),
        "depreciation_pct": money(pct),
        "total_depreciation": money(total_dep),
        "acv_before_deductible": money(acv),
        "deductible": money(ded),
        "stages": [
            {"stage": "1 initial ACV payment (scope ACV minus deductible)", "amount": money(initial_acv_payment)},
            {"stage": "2 supplement ACV payments as approved", "amount": money(supplement_payment)},
            {"stage": "3 recoverable depreciation on completion", "amount": money(recoverable_dep)},
        ],
        "total_expected_payments": money(total_expected),
        "homeowner_responsibility_deductible": money(ded),
    }
    return out


def selftest():
    # Illustrative example: RCV 30,000; depreciation 10,000; ACV 20,000 before deductible.
    r = claim(30000, dep_amount=10000, deductible=2000)
    assert r["total_rcv"] == D("30000.00")
    assert r["total_depreciation"] == D("10000.00")
    assert r["acv_before_deductible"] == D("20000.00")
    assert r["depreciation_pct"] == D("33.33")
    assert r["stages"][0]["amount"] == D("18000.00")
    assert r["stages"][2]["amount"] == D("10000.00")
    assert r["total_expected_payments"] == D("28000.00")
    # exactly 33 percent is 9,900, not 10,000: do not round percents by hand
    r = claim(30000, dep_pct=33, deductible=0)
    assert r["total_depreciation"] == D("9900.00") and r["acv_before_deductible"] == D("20100.00")
    # supplements at the same depreciation percentage
    r = claim(30000, dep_amount=10000, deductible=2000, supplements=[1500, 900])
    assert r["supplements_rcv"] == D("2400.00")
    assert r["total_rcv"] == D("32400.00")
    assert r["total_depreciation"] == D("10800.00")
    assert r["total_expected_payments"] == D("30400.00"), r["total_expected_payments"]  # 32400 - 2000
    # non-recoverable policy
    r = claim(30000, dep_amount=10000, deductible=2000, recoverable=False)
    assert r["stages"][2]["amount"] == D("0.00") and r["total_expected_payments"] == D("18000.00")
    # deductible larger than base ACV carries into later payments
    r = claim(1000, dep_amount=500, deductible=800, supplements=[1000])
    assert r["stages"][0]["amount"] == D("0.00")
    assert r["stages"][1]["amount"] == D("200.00")  # supplement ACV 500 minus unapplied 300
    # O&P
    r = claim(10000, dep_pct=0, op_pct=20)
    assert r["total_rcv"] == D("12000.00")
    for bad in (lambda: claim(100, 10, 10), lambda: claim(100), lambda: claim(100, dep_amount=200),
                lambda: claim(100, dep_amount=10, deductible=-1)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("claim_math selftest OK")


def main(argv=None):
    p = argparse.ArgumentParser(description="Claim payment math")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--rcv", type=float)
    p.add_argument("--dep-amount", type=float)
    p.add_argument("--dep-pct", type=float)
    p.add_argument("--deductible", type=float, default=0.0)
    p.add_argument("--supplement", type=float, action="append", default=[])
    p.add_argument("--op-pct", type=float, default=0.0)
    p.add_argument("--non-recoverable", action="store_true")
    p.add_argument("--nonrecoverable-amount", type=float, default=0.0)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        selftest()
        return 0
    if a.rcv is None:
        p.error("--rcv is required")
    try:
        r = claim(a.rcv, a.dep_amount, a.dep_pct, a.deductible, a.supplement,
                  a.op_pct, not a.non_recoverable, a.nonrecoverable_amount)
    except ValueError as e:
        print("error:", e, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(r, indent=2, default=str))
    else:
        for k, v in r.items():
            if k == "stages":
                for s in v:
                    print(f"  {s['stage']}: {s['amount']}")
            else:
                print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
