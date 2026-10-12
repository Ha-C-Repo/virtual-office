#!/usr/bin/env python3
"""Commission statement reconciliation (stdlib, Decimal, csv).

Compares expected amounts to amounts paid by a reference id. Arithmetic only.
Expected amounts come from the contract grid or carrier schedule the office
holds (VERIFY). Do not put personal identifiers in the files; use opaque refs.
Numbers from this tool win over model arithmetic.

Usage:
  python commission_recon.py --selftest
  python commission_recon.py recon --expected expected.csv --paid paid.csv [--tolerance 0.01]
CSV columns: ref,amount   (duplicate refs are summed)
"""
import argparse
import csv
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def load(rows):
    out = {}
    for ref, amt in rows:
        out[ref] = out.get(ref, Decimal(0)) + D(amt)
    return out


def recon(expected, paid, tolerance="0.01"):
    tol = D(tolerance)
    if tol < 0:
        raise ValueError("tolerance must be >= 0")
    res = {"matched": [], "underpaid": [], "overpaid": [], "missing": [], "unexpected": []}
    for ref in sorted(set(expected) | set(paid)):
        e, p = expected.get(ref), paid.get(ref)
        if e is None:
            res["unexpected"].append({"ref": ref, "paid": q(p)})
        elif p is None:
            res["missing"].append({"ref": ref, "expected": q(e)})
        else:
            diff = p - e
            row = {"ref": ref, "expected": q(e), "paid": q(p), "variance": q(diff)}
            if abs(diff) <= tol:
                res["matched"].append(row)
            elif diff < 0:
                res["underpaid"].append(row)
            else:
                res["overpaid"].append(row)
    te, tp = sum(expected.values(), Decimal(0)), sum(paid.values(), Decimal(0))
    res["totals"] = {"expected": q(te), "paid": q(tp), "variance": q(tp - te)}
    return res


def read_csv(path):
    with open(path, newline="") as f:
        return load((r["ref"], r["amount"]) for r in csv.DictReader(f))


def selftest():
    e = load([("A", 100), ("B", 50), ("C", 75)])
    p = load([("A", 100), ("B", 40), ("D", 20)])
    r = recon(e, p)
    assert [x["ref"] for x in r["matched"]] == ["A"]
    assert r["underpaid"][0]["variance"] == D("-10.00")
    assert r["missing"] == [{"ref": "C", "expected": D("75.00")}]
    assert r["unexpected"] == [{"ref": "D", "paid": D("20.00")}]
    assert r["totals"] == {"expected": D("225.00"), "paid": D("160.00"), "variance": D("-65.00")}
    assert load([("A", 1), ("A", 2)]) == {"A": D(3)}
    assert recon({"A": D(10)}, {"A": D("10.005")}, "0.01")["matched"]
    assert recon({"A": D(10)}, {"A": D(12)})["overpaid"]
    try:
        recon({}, {}, "-1")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
    print("commission_recon selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("recon")
    r.add_argument("--expected", required=True); r.add_argument("--paid", required=True)
    r.add_argument("--tolerance", default="0.01")
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "recon":
        print(json.dumps(recon(read_csv(a.expected), read_csv(a.paid), a.tolerance), indent=2, default=str))
        return 0
    ap.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
