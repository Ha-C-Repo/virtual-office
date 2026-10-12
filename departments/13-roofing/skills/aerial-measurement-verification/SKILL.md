---
name: aerial-measurement-verification
description: Ingest an aerial measurement report, check it against a manual or on-site measurement, and log variance before any quantity is used.
---
# Aerial Measurement Verification

## When to use
When a remote measurement report is ordered or received from an aerial measurement provider. Always for complex roofs.

## Inputs
The report (areas by plane, pitches, linear measures, waste table), site photos, a footprint tape measure or manual measurements.

## Steps
1. Extract fields into `../../templates/measurement-verification-sheet.md`: footprint, roof area, squares, pitch per plane, eave, rake, ridge, hip, valley, wall flashing lengths, penetrations.
2. Compute a manual cross-check with `../../harnesses/takeoff_calc.py` from footprint and dominant pitch. Expect small differences; large ones need an explanation.
3. Check each plane against photos: missing dormers, additions, trees hiding edges, recent changes, wrong pitch, flat sections, second structures.
4. For complex roofs (many valleys, hips, dormers, steep sections, multiple layers) do an on-site check of key dimensions and pitch.
5. Compute variance percent between aerial and manual; record it in `variance_pct`. Use {{VARIANCE_TOLERANCE}} as the office tolerance. Above it, re-measure on site.
6. Choose the quantity source (aerial, manual, or reconciled) and record why.
7. Hand verified numbers to `../roof-takeoff-calculator/SKILL.md`.

## Outputs
Verification sheet with the source of record, variance, reconciliation note.

## Gates
- No material order or estimate uses an unverified report on a complex roof.
- The waste table in a report is a suggestion; the waste percent is set per `../estimate-builder-tiered/SKILL.md` and checked with the supplier (VERIFY).
- Variance history is kept to measure the provider's accuracy over time; accuracy figures are not assumed.
