---
name: qc-checklists
description: Run staged quality checks (pre-start, deck, dry-in, flashing, final) with photo evidence and fail-closed results.
---
# QC Checklists

## When to use
At each production milestone and before closeout.

## Inputs
Contract scope, product instructions, permit requirements, photo log, crew work order.

## Steps
1. Pre-start: materials match order and color, safety plan on site, permit posted, protection of landscaping and property.
2. Deck: damaged sections replaced, fasteners secure, no soft spots left, ventilation openings correct. Photos before cover.
3. Dry-in: underlayment, ice barrier, drip edge, laps per spec, valleys, penetrations covered. Inspection photos, inspector result.
4. Flashing: step flashing at walls, kickouts, chimney and skylight, pipe boots, valley treatment.
5. Final: nail placement and pattern per manufacturer instructions, nails driven flush, shingle alignment and exposure, ridge and hip caps, vents, sealing, gutters clear, cleanup with magnet sweep of the yard, driveway and gutters.
6. Photos: before and after sets with date stamps.
7. Record each item pass or fail in `../../templates/qc-checklist.md`. Failed items go to the punch list (`../punch-list-and-closeout/SKILL.md`).
8. Piecework: increase spot checks; record the crew quality score.

## Outputs
Completed checklists with evidence ids, fail list, retest dates.

## Gates
- Fail closed: missing photo or unchecked item equals fail.
- A QC fail blocks sub milestone payments and the final invoice.
- Manufacturer instructions are the standard, not memory.
- Inspector independent of the crew that installed.
