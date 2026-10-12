---
name: cma-sanity-check
description: Pre-delivery sanity pass on a CMA: price versus comp corridor, GLA sourced, photos present, disclosure checklist complete.
---
# CMA Sanity Check

## When to use
After a CMA draft exists and before the compliance review or any delivery.

## Inputs
Draft CMA report, comp grid, scenarios, document checklist.

## Steps
1. Corridor: each scenario price divided by subject GLA (use a script) must fall inside the comp corridor, or the report explains the outlier in a labeled note.
2. GLA: a source and confidence tag exist for the subject and every comp.
3. Comps: count meets {{MIN_COMPS}}; sale dates inside {{COMP_MAX_AGE_MONTHS}} months unless justified; no duplicate comps.
4. Scenarios: aggressive > recommended > floor, each with a stated basis.
5. Photos present for the subject; disclosure checklist complete (seller disclosure, HOA, inspection, survey where applicable).
6. Internal data (net sheet, commission, strategy notes) is absent from the client document.
7. Placeholders: no unfilled `{{TOKENS}}` remain.

## Outputs
Pass/fail table with one line of evidence per check. Exit semantics: 0 clean, 1 blocked.

## Gates
Any failure blocks the report. Do not soften a failure into a warning.
