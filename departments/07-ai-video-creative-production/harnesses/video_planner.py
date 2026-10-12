#!/usr/bin/env python3
"""Narration timing check and generation cost quote (stdlib, Decimal).

The words-per-second figure is a PLANNING HEURISTIC (default 2.5), not a
standard. Set {{WORDS_PER_SECOND}} from your own voice talent's measured pace.
Unit costs come from the platform's current published pricing (VERIFY, log
source and date). A quote is not an approval; the human "go" comes from {{OWNER}}.

Usage:
  python video_planner.py --selftest
  python video_planner.py timing --seconds 15 --script-file vo.txt [--wps 2.5]
  python video_planner.py quote --clips 10 --unit-cost 2.00 --retry-pct 30 --budget 25
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


def timing(seconds, text, wps="2.5"):
    if D(seconds) <= 0 or D(wps) <= 0:
        raise ValueError("seconds and wps must be > 0")
    words = len(text.split())
    allowed = int(math.floor(D(seconds) * D(wps)))
    return {"words": words, "allowed_words": allowed, "fits": words <= allowed,
            "estimated_seconds": q(D(words) / D(wps))}


def quote(clips, unit_cost, retry_pct=0, budget=None):
    if int(clips) < 0 or D(unit_cost) < 0 or D(retry_pct) < 0:
        raise ValueError("inputs must be >= 0")
    total = D(clips) * D(unit_cost) * (1 + D(retry_pct) / 100)
    out = {"clips": int(clips), "expected_total": q(total)}
    if budget is not None:
        out["budget"] = q(budget)
        out["within_budget"] = total <= D(budget)
    return out


def selftest():
    t = timing(15, "one two three")
    assert t["words"] == 3 and t["allowed_words"] == 37 and t["fits"]
    long_text = " ".join(["w"] * 38)
    assert not timing(15, long_text)["fits"]
    assert timing(60, " ".join(["w"] * 150))["estimated_seconds"] == D("60.00")
    assert timing(10, "a b", "2")["allowed_words"] == 20
    qt = quote(10, 2.00, 30, 25)
    assert qt["expected_total"] == D("26.00") and qt["within_budget"] is False
    assert quote(10, 2.00, 30, 26)["within_budget"] is True
    assert quote(0, 5)["expected_total"] == D("0.00")
    for bad in (lambda: timing(0, "x"), lambda: quote(-1, 1)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("video_planner selftest OK")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    t = sub.add_parser("timing")
    t.add_argument("--seconds", required=True); t.add_argument("--script-file", required=True)
    t.add_argument("--wps", default="2.5")
    qq = sub.add_parser("quote")
    qq.add_argument("--clips", required=True, type=int); qq.add_argument("--unit-cost", required=True)
    qq.add_argument("--retry-pct", default="0"); qq.add_argument("--budget")
    a = ap.parse_args(argv)
    if a.selftest:
        selftest(); return 0
    if a.cmd == "timing":
        with open(a.script_file) as f:
            print(timing(a.seconds, f.read(), a.wps))
    elif a.cmd == "quote":
        print(quote(a.clips, a.unit_cost, a.retry_pct, a.budget))
    else:
        ap.print_help(); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
