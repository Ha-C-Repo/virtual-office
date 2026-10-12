---
name: drawing-reading
description: Mandatory protocol before any takeoff. Indexes the drawing set, reads general notes first, calibrates scale and counts tagged items from the vector text layer.
---
## When to use
Before every takeoff, and whenever a new drawing revision arrives.

## Inputs
Drawing PDF set, specifications, scope of works, GC name, deadline, drawing version and scale.

## Steps
1. Split the merged PDF into one file per sheet at high resolution and extract the text layer per sheet (see `../../workflows/04-drawing-indexing.md`).
2. List every structural sheet and classify each by discipline. Build a sheet cross-reference map.
3. Rasterize and view each plan sheet. Do not rely on one page-level glance.
4. Read general notes first. General notes govern over plan notes. Any conflict is escalated, never resolved silently.
5. Calibrate scale from dimension lines, not from the printed scale label alone. Record the check.
6. Count tagged items (columns, beams, joists, anchors) from the vector text, not from pixels. State the confidence of each count.
7. Record sheet and reliability on every extracted record.

## Outputs
Sheet index, cross-reference matrix, count table with confidence, conflict list, open-question list.

## Gates
- Never trust vision for a count or a measurement. Extract deterministically, tag confidence, verify.
- A human verifies every LOW count before it reaches pricing.
- If a sheet is unreadable or missing, stop and ask.
