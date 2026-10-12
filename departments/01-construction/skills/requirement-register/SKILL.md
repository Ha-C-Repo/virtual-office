---
name: requirement-register
description: Extracts every tender requirement into a four-bucket register with source references, and checks the human's clarification register against it.
---
## When to use
After tender-ingest. Also used to check the estimator's hand-written clarification register for omissions.

## Inputs
Tender index, specifications, scope of works, conditions of contract.

## Steps
1. Extract each requirement as one row: req_id, category, discipline, text, expected_unit, source references.
2. Sort into four buckets: scope of work, commercial and contract, submittal and quality, exclusions and assumptions.
3. State the recall target (for example "aim to capture all shall/must/provide statements") and the method used.
4. Link each row later to a priced line (`priced_line_ref`) or an explicit exclusion.
5. Compare against the estimator's clarification register and returnable pricing schedule. List what the human missed. The human owns the thinking; you cross-check.

## Outputs
Requirement register and a missed-items report.

## Gates
Final reconciliation runs in a fresh, memoryless session against this register.
