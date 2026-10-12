---
name: award-to-budget
description: Converts a signed award into a cost-baseline workbook with cost codes mirroring the bid lines, an explicit management reserve, frozen on approval.
---
## When to use
After contract signature, as step 4 of `../../workflows/05-award-to-project-controls.md`.

## Inputs
Signed contract value, bid estimate lines, target margin, locked cost codes.

## Steps
1. Baseline = contract value minus target margin. Compute with the calculator.
2. Create cost codes mirroring the bid lines.
3. Add a named management reserve line.
4. Fill `../../templates/project-budget-workbook.md`.
5. Show the baseline to the {{APPROVER_ROLE}}. On approval, freeze and version-suffix it.
6. Later changes are new versions, never edits.

## Outputs
Baseline workbook and version record.

## Gates
Frozen on approval. Variance against baseline feeds earned value and notice triggers.
