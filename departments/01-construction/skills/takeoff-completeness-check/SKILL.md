---
name: takeoff-completeness-check
description: Checks the takeoff against the required specification sections and scope checklist for the building type. Deck sections are never optional.
---
## When to use
After takeoff, before pricing.

## Inputs
Takeoff table, specifications, scope checklist (base plus building-type additions), building type.

## Steps
1. Load the base scope checklist and the additions for the building type.
2. Map each checklist item to takeoff rows or to the specification section that governs it (CSI MasterFormat divisions; steel deck 05 31 and composite deck 05 36 are never optional).
3. For each item mark: PRESENT, MISSING, EXCLUDED_BY_SCOPE (cite the scope statement) or NOT_APPLICABLE (give a reason).
4. Flag low-confidence gross area and carry contingency.
5. Report the missing list to the estimator and draft RFIs for anything the documents do not settle.

## Outputs
Completeness table, missing-item list, RFI candidates.

## Gates
Pricing does not proceed with a MISSING item that has no RFI or explicit exclusion.
