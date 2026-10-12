#!/usr/bin/env python3
"""BOM unit-cost rollup by volume tier (stdlib, Decimal).

Selftest figures are illustrative. Real prices come from dated supplier quotes.
Numbers from this tool win over model arithmetic.

Usage:
  python bom_rollup.py --selftest
  python bom_rollup.py rollup --file bom.json --volume 1000 [--as-of 2026-10-12]
bom.json:
  {"lines": [{"item": "A", "qty": 2, "tiers": [[1, 5.00], [1000, 4.00]],
              "quote_expiry": "2026-12-31"}],
   "non_part": {"assembly": 3, "test": 1, "freight": 0, "packaging": 0},
   "scrap_pct": 2, "warranty_pct": 3, "target_price": 40}
Tier rule: the tier with the largest min_qty <= volume applies. Below the
smallest tier the smallest tier price is used and a warning is returned.
"""
import argparse
import json
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def q(x):
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)


def tier_price(tiers, volume):
    if not tiers:
        raise ValueError("line has no price tiers")
    ordered = sorted(((D(m), D(p)) for m, p in tiers), key=lambda t: t[0])
    if any(p < 0 for _, p in ordered):
        raise ValueError("prices must be >= 0")
    chosen, below = ordered[0][1], D(volume) < ordered[0][0]
    for m, p in ordered:
        if D(volume) >= m:
            chosen = p
    return chosen, below


def rollup(bom, volume, as_of=None):
    if D(volume) <= 0:
        raise ValueError("volume must be > 0")
    parts, warnings, stale = Decimal(0), [], []
    detail = []
    for ln in bom["lines"]:
        if D(ln["qty"]) < 0:
            raise ValueError("qty must be >= 0")
        price, below = tier_price(ln["tiers"], volume)
        ext = D(ln["qty"]) * price
        parts += ext
        detail.append({"item": ln["item"], "unit_price": q(price), "extended": q(ext)})
        if below:
            warnings.append("%s: volume below smallest tier" % ln["item"])
        exp = ln.get("quote_expiry")
        if exp and as_of and date.fromisoformat(exp) < date.fromisoformat(as_of):
            stale.append(ln["item"])
    non_part = sum((D(v) for v in bom.get("non_part", {}).values()), Decimal(0))
    if non_part < 0:
        raise ValueError("non_part costs must be >= 0")
    scrap = parts * D(bom.get("scrap_pct", 0)) / 100
    subtotal = parts + scrap + non_part
    warranty = subtotal * D(bom.get("warranty_pct", 0)) / 100
    unit = subtotal + warranty
    out = {"volume": int(D(volume)), "parts": q(parts), "scrap": q(scrap),
           "non_part": q(non_part), "warranty_reserve": q(warranty),
           "unit_cost": q(unit), "stale_quotes": stale, "warnings": warnings,
           "lines": detail}
    t = bom.get("target_price")
    if t is not None and D(t) > 0:
        out["margin_vs_target_pct"] = q((D(t) - unit) / D(t) * 100)
    return out


def selftest():
    bom = {"lines": [{"item": "A", "qty": 2, "tiers": [[1, 5.00], [1000, 4.00]],
                      "quote_expiry": "2026-09-01"},
                     {"item": "B", "qty": 1, "tiers": [[1, 10.00]]}],
           "non_part": {"assembly": 3, "test": 1}, "scrap_pct": 2,
           "warranty_pct": 3, "target_price": 40}
    r = rollup(bom, 1000, "2026-10-12")
    assert r["parts"] == D("18.00") and r["scrap"] == D("0.36")
    assert r["warranty_reserve"] == D("0.67") and r["unit_cost"] == D("23.03")
    assert r["margin_vs_target_pct"] == D("42.42")
    assert r["stale_quotes"] == ["A"]
    assert rollup(bom, 10)["unit_cost"] == D("25.13")
    assert rollup(bom, 10)["parts"] == D("20.00")
    # volume below smallest tier warns
    b2 = {"lines": [{"item": "C", "qty": 1, "tiers": [[100, 2.00]]}]}
    assert rollup(b2, 10)["warnings"]
    for bad in (lambda: rollup(bom, 0), lambda: rollup({"lines": [{"item": "x", "qty": 1, "tiers": []}]}, 1),
                lambda: rollup({"lines": [{"item": "x", "qty": -1, "tiers": [[1, 1]]}]}, 1)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("bom_rollup selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("rollup")
    r.add_argument("--file", required=True)
    r.add_argument("--volume", required=True, type=int)
    r.add_argument("--as-of")
    a = ap.parse_args(argv)
    if a.selftest:
        selftest()
        return 0
    if a.cmd == "rollup":
        with open(a.file) as f:
            bom = json.load(f)
        print(json.dumps(rollup(bom, a.volume, a.as_of), indent=2, default=str))
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
