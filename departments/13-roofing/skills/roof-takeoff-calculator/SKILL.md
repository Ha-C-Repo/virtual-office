---
name: roof-takeoff-calculator
description: Compute roof area, squares, waste, bundles and accessories through the takeoff harness, never by model arithmetic.
---
# Roof Takeoff Calculator

## When to use
Whenever a quantity of shingles, starter, ridge, drip edge or underlayment is needed for an estimate or an order.

## Inputs
Verified measurements (`../aerial-measurement-verification/SKILL.md`): footprint or sloped area, pitch, eave, rake, ridge and hip lengths, waste percent ({{WASTE_PERCENT}}), bundles per square from the product data sheet, underlayment roll coverage from the data sheet.

## Method (for review; run the harness)
- Pitch factor = sqrt(rise^2 + run^2) / run.
- Sloped area = footprint x pitch factor. Squares = area / 100.
- Ordering squares = squares x (1 + waste). Planning waste: about 10 percent simple gable, about 12 percent hip, 15 percent or more for complex, up to 25 percent for very complex (**VERIFY with supplier**).
- Bundles = ordering squares x bundles per square, rounded up. Typical bundles per square: 3 for 3-tab, 3 to 4 for architectural, 4 to 5 for premium (**VERIFY data sheet**).
- Starter: eave plus rake length / about 105 linear ft per bundle. Ridge cap: ridge plus hip length / about 20 linear ft per bundle. Drip edge: eave plus rake length plus about 10 percent lap, in 10 ft sticks. Underlayment: area / roll coverage from the data sheet. All VERIFY.
- Keep **ordering squares** separate from **tear-off and labor squares** (no waste on labor).

## Steps
1. Run: `python ../../harnesses/takeoff_calc.py --length L --width W --rise R --waste P --bundles-per-square B --eave-lf E --rake-lf K --ridge-lf G --json` (or `--area-sf` when only sloped area is known).
2. Paste the output and the command into `../../templates/takeoff-sheet.md`.
3. Have a second person re-run it with the same inputs.
4. Add penetration, flashing, vent and sealant items separately from the harness output.

## Outputs
Takeoff sheet with quantities, assumptions and the harness command.

## Gates
- Harness output wins over model arithmetic (`../../harnesses/README.md`).
- Waste and coverage assumptions are stated on the sheet and confirmed with the supplier before ordering (`../material-order-builder/SKILL.md`).
- Round up, never down.
