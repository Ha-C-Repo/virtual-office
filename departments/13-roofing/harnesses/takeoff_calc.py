#!/usr/bin/env python3
"""Roof takeoff calculator (stdlib only).

Numbers from this tool win over model arithmetic: verify, do not generate.
All defaults below are planning defaults. VERIFY against the supplier and the
product data sheet before ordering.

Usage:
  python takeoff_calc.py --selftest
  python takeoff_calc.py --length 40 --width 30 --rise 6 --waste 10 \
      --bundles-per-square 3 --eave-lf 80 --rake-lf 33.54 --ridge-lf 40
  python takeoff_calc.py --area-sf 1500 --rise 8 --waste 12 --json
"""
import argparse
import json
import math
import sys

# Planning defaults (VERIFY with supplier / data sheet).
STARTER_LF_PER_BUNDLE = 105.0
RIDGE_LF_PER_BUNDLE = 20.0
DRIP_STICK_FT = 10.0
DRIP_LAP_ALLOWANCE = 0.10
DEFAULT_ROLL_SQUARES = 10.0  # coverage per roll in squares; take from the data sheet


def pitch_factor(rise, run=12.0):
    """sqrt(rise^2 + run^2) / run."""
    if run <= 0 or rise < 0:
        raise ValueError("run must be > 0 and rise >= 0")
    return math.sqrt(rise * rise + run * run) / run


def roof_area_sf(footprint_sf, rise, run=12.0):
    return footprint_sf * pitch_factor(rise, run)


def squares(area_sf):
    return area_sf / 100.0


def ordering_squares(area_sf, waste_pct):
    """Squares to order = area with waste. Keep separate from tear-off/labor squares."""
    if waste_pct < 0:
        raise ValueError("waste_pct must be >= 0")
    return squares(area_sf) * (1.0 + waste_pct / 100.0)


def bundles(order_squares, bundles_per_square):
    """Round UP to whole bundles (rounding to 9 places guards float noise)."""
    return math.ceil(round(order_squares * bundles_per_square, 9))


def ceil_div(value, per):
    return math.ceil(round(value / per, 9)) if value > 0 else 0


def takeoff(length=None, width=None, area_sf=None, rise=6.0, run=12.0,
            waste_pct=10.0, bundles_per_square=3.0, eave_lf=0.0, rake_lf=0.0,
            ridge_lf=0.0, hip_lf=0.0, roll_squares=DEFAULT_ROLL_SQUARES):
    if area_sf is not None:
        footprint = None
        actual_area = float(area_sf)  # treated as already sloped surface area
    elif length and width:
        footprint = length * width
        actual_area = roof_area_sf(footprint, rise, run)
    else:
        raise ValueError("give --length and --width, or --area-sf (sloped area)")
    factor = pitch_factor(rise, run)
    sq = squares(actual_area)
    order_sq = ordering_squares(actual_area, waste_pct)
    edge_lf = eave_lf + rake_lf
    cap_lf = ridge_lf + hip_lf
    return {
        "footprint_sf": footprint,
        "pitch_factor": factor,
        "roof_area_sf": actual_area,
        "roof_squares": sq,
        "waste_pct": waste_pct,
        "ordering_squares": order_sq,
        "bundles_per_square": bundles_per_square,
        "shingle_bundles": bundles(order_sq, bundles_per_square),
        "starter_bundles": ceil_div(edge_lf, STARTER_LF_PER_BUNDLE),
        "ridge_cap_bundles": ceil_div(cap_lf, RIDGE_LF_PER_BUNDLE),
        "drip_edge_sticks": ceil_div(edge_lf * (1 + DRIP_LAP_ALLOWANCE), DRIP_STICK_FT),
        "underlayment_rolls": ceil_div(sq, roll_squares),
        "assumptions": {
            "starter_lf_per_bundle": STARTER_LF_PER_BUNDLE,
            "ridge_lf_per_bundle": RIDGE_LF_PER_BUNDLE,
            "drip_stick_ft": DRIP_STICK_FT,
            "drip_lap_allowance": DRIP_LAP_ALLOWANCE,
            "roll_squares": roll_squares,
            "note": "VERIFY all coverage figures against the product data sheet and supplier.",
        },
    }


def selftest():
    # pitch factor
    assert abs(pitch_factor(6) - math.sqrt(180) / 12) < 1e-12
    assert abs(pitch_factor(12) - math.sqrt(2)) < 1e-12
    assert pitch_factor(0) == 1.0
    # worked example: 40x30 footprint, 6/12, 10% waste, 3 bundles/sq
    r = takeoff(length=40, width=30, rise=6, waste_pct=10, bundles_per_square=3,
                eave_lf=80, rake_lf=2 * 15 * pitch_factor(6), ridge_lf=40)
    assert r["footprint_sf"] == 1200
    assert abs(r["roof_area_sf"] - 1341.6408) < 1e-3, r["roof_area_sf"]
    assert abs(r["roof_squares"] - 13.416408) < 1e-5
    assert abs(r["ordering_squares"] - 14.758049) < 1e-5
    assert r["shingle_bundles"] == 45, r["shingle_bundles"]  # ceil(44.27)
    assert r["starter_bundles"] == 2      # 113.54 lf / 105
    assert r["ridge_cap_bundles"] == 2    # 40 / 20
    assert r["drip_edge_sticks"] == 13    # 113.54 * 1.1 / 10 = 12.49
    assert r["underlayment_rolls"] == 2   # 13.42 sq / 10
    # exact multiple does not round up spuriously
    assert bundles(10.0, 3) == 30
    assert bundles(10.01, 3) == 31
    # direct area mode
    r2 = takeoff(area_sf=2000, waste_pct=15, bundles_per_square=3)
    assert abs(r2["ordering_squares"] - 23.0) < 1e-9 and r2["shingle_bundles"] == 69
    # bad input
    for bad in (lambda: pitch_factor(6, 0), lambda: takeoff(), lambda: ordering_squares(1000, -1)):
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("takeoff_calc selftest OK")


def main(argv=None):
    p = argparse.ArgumentParser(description="Roof takeoff calculator")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--length", type=float)
    p.add_argument("--width", type=float)
    p.add_argument("--area-sf", type=float, help="sloped roof area (skips footprint math)")
    p.add_argument("--rise", type=float, default=6.0, help="rise per 12 run")
    p.add_argument("--waste", type=float, default=10.0, help="waste percent (VERIFY with supplier)")
    p.add_argument("--bundles-per-square", type=float, default=3.0)
    p.add_argument("--eave-lf", type=float, default=0.0)
    p.add_argument("--rake-lf", type=float, default=0.0)
    p.add_argument("--ridge-lf", type=float, default=0.0)
    p.add_argument("--hip-lf", type=float, default=0.0)
    p.add_argument("--roll-squares", type=float, default=DEFAULT_ROLL_SQUARES)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        selftest()
        return 0
    try:
        r = takeoff(a.length, a.width, a.area_sf, a.rise, 12.0, a.waste,
                    a.bundles_per_square, a.eave_lf, a.rake_lf, a.ridge_lf,
                    a.hip_lf, a.roll_squares)
    except ValueError as e:
        print("error:", e, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        for k, v in r.items():
            if k != "assumptions":
                print(f"{k}: {round(v, 3) if isinstance(v, float) else v}")
        print("VERIFY coverage assumptions:", json.dumps(r["assumptions"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
