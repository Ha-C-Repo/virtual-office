---
name: commission-reconciliation
description: Reconcile a carrier commission statement against the comp grid line by line, with fair-market-value cap check and human review list.
---
# Commission reconciliation

## When to use
Each time a carrier commission statement arrives (spreadsheet, CSV or PDF).

## Inputs
Statement, comp grid (carrier, product, level, basis, rate), book export for matching, current-year FMV cap table from the regulator.

## Steps
1. Read the statement itself; record row count and period.
2. Normalize columns to the standard statement schema; log every mapping decision.
3. Match each line to a grid row on carrier x product x level. Exact match = high confidence; fuzzy = medium.
4. Expected = grid rate x basis (per application or percent of premium). Grid only.
5. Variance = paid minus expected, signed.
6. Classify MATCH, VARIANCE or UNMATCHED with confidence and a one-sentence reason.
7. FMV cap check on Medicare Advantage and Part D lines. Renewal cap is half of initial. Flag FMV-EXCEEDS-CAP. Re-verify caps yearly; never guess.
8. Aggregate by carrier and by writing agent; verify the sum of line variances equals the total variance.
9. Send every variance, unmatched, low-confidence and cap flag to the human review list.

## Outputs
Reconciliation report (`../../templates/commission-reconciliation-report.md`) plus `-INT` memo. PHI masked as initials plus last four of a record ID.

## Gates
Verify, do not generate. No commission data in any outward document. Disputes go through `../contract-notice/SKILL.md` (commission variance notice), draft only.
