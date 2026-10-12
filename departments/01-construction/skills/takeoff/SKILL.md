---
name: takeoff
description: Member-by-member quantity takeoff, schedule-first with plan-count fallback, with provenance and confidence on every row. Weights only from the reference shape database.
---
## When to use
After drawing-reading and stage classification, before pricing.

## Inputs
Sheet index, schedules, plans, reference shape database, building type.

## Steps
1. Screen the building type (conventional, tilt-up, pre-engineered, bearing wall). Decide the deck question; default is deck in scope.
2. Take off from schedules first: column, beam, joist, anchor. Where no schedule exists, count from plans using template matching and mark the row secondary-source.
3. Classify each row: COL, BEAM, JST, DECK, PLATE, ANCH, MISC. Mode: COUNT (each), LINEAR (feet) or AREA (square feet).
4. Look up weight per foot in the reference shape database. If a designation does not resolve, mark the row LOW and do not estimate a weight.
5. Compute weight and tons through the calculator. No arithmetic by the model.
6. Use note tokens where needed: CONFLICT, GROUP, OPENING, QTY_BASIS, REMOVED.
7. Calibrate scale and record formula references.

## Outputs
Takeoff table (JSON and workbook) using the fields in `../../knowledge/schemas.md`; summary by class; list of unresolved designations.

## Gates
- Every row has sheet, source and confidence.
- Unresolved designations block pricing until a human supplies or confirms them.
- Two independent paths (for example weight from takeoff, and intensity from area) are later compared by bid-sanity-check.
