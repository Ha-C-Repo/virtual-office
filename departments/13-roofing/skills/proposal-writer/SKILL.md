---
name: proposal-writer
description: Turn an approved estimate into a clear customer proposal with scope, materials, options, timeline, warranty and next steps.
---
# Proposal Writer

## When to use
After the estimate is approved internally.

## Inputs
Approved estimate, inspection report and selected photos, product data sheets, warranty descriptions, schedule outlook, license and insurance details ({{LICENSE_NUMBER}}, {{COI_REFERENCE}}).

## Steps
1. Open with what was found, in plain words, with two or three photos from the log. No fear language.
2. Present the three tiers side by side: what is included, product line, expected warranty (name the layers separately: installer workmanship, manufacturer material, extended/system), price, timeline.
3. State scope inclusions and exclusions, including decking allowance and unit price, ventilation work, permit responsibility, cleanup, color confirmation date.
4. State payment terms and the schedule from the contract template. Deposit terms follow state limits (VERIFY).
5. Weather and material delay language.
6. Insurance jobs: state that the homeowner is responsible for the deductible and non-covered work, and that the office does not negotiate coverage. No deductible promises.
7. Add a next-steps list and the proposal validity date ({{PROPOSAL_VALID_DAYS}}).
8. Use `../../templates/proposal.md`. Check against `../contract-compliance-check/SKILL.md` for consistency with the contract.

## Outputs
Customer-ready proposal draft.

## Gates
- Facts trace to the inspection and estimate. Numbers come from the harness outputs.
- Marketing claims need support; no unverified statistics.
- Owner sign-off before it is sent.
