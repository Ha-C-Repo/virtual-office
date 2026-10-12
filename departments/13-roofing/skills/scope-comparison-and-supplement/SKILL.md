---
name: scope-comparison-and-supplement
description: Compare the carrier scope with the contractor line-item estimate and prepare evidence-based supplement requests for owner approval.
---
# Scope Comparison and Supplement

## When to use
After the carrier issues a scope or estimate, and again when hidden conditions appear during tear-off.

## Inputs
Carrier scope (line items with quantities and prices), contractor line-item estimate, measurement verification sheet, photo log, code requirements, manufacturer instructions, policy provisions as provided by the homeowner.

## Steps
1. Align both documents line by line in a table: item, carrier qty, our qty, unit, difference, evidence.
2. Classify each difference: quantity (measurement), missing line (e.g. drip edge, ice barrier, starter, ridge, vents, flashing, steep or high charges, haul-off, permit), material mismatch (product type), code-required item, hidden condition (decking), matching issue, overhead and profit, depreciation dispute.
3. For each candidate supplement attach evidence: photo ids, measurement, code section reference, manufacturer instruction, or invoice. Items without evidence are removed.
4. Use `../../templates/supplement-request-letter.md`. Number supplements (typically one to three). Price totals through `../../harnesses/claim_math.py` where payment effects are shown.
5. Hidden decking: document at tear-off with photos before replacement, then submit. Pricing per the contract's unit price.
6. Matching and appraisal: record the disagreement and the policy's process; the homeowner and qualified representatives decide.
7. Track status, response and date in the tracker (`../../templates/acv-rcv-tracker.md`).

## Outputs
Comparison table, supplement letter draft, evidence index.

## Gates
- No padding. Every line has evidence and a basis.
- No coverage arguments or legal interpretations; present facts and requirements.
- Homeowner authorizes the submission; owner signs off before it goes to the carrier.
- Respect policy deadlines (VERIFY).
- Run `../deductible-and-inducement-gate/SKILL.md` on the letter.
