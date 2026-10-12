---
name: insurance-claim-support
description: Support a homeowner insurance claim end to end with documentation, adjuster meeting prep, payment tracking and deadlines, without adjusting or legal advice.
---
# Insurance Claim Support

## When to use
Storm or damage jobs where the homeowner has filed or intends to file a claim.

## Inputs
Inspection report and photo log, policy declarations page (from the homeowner), claim number placeholder ({{CLAIM_NUMBER}}), carrier ({{CARRIER}}), adjuster details ({{ADJUSTER_NAME}}), carrier scope and payment letters.

## Steps
1. Explain the roles in writing: the homeowner files and owns the claim; the office documents damage, provides an itemized estimate, and attends the adjuster meeting if the homeowner asks. The office does not negotiate coverage.
2. Open the claim file with `../../templates/claim-file-cover-sheet.md`. Record the date of loss, cause, deadlines (work completion, recoverable depreciation claim, proof of loss; **VERIFY** from the policy and state rules).
3. Prepare the adjuster meeting (`../../templates/adjuster-meeting-checklist.md`): photo set, test squares, measurements, line-item estimate, manufacturer requirements.
4. After the carrier scope arrives, run `../scope-comparison-and-supplement/SKILL.md`.
5. Track payments with `../acv-rcv-depreciation-math/SKILL.md` and `../../templates/acv-rcv-tracker.md`: initial ACV payment, supplements, recoverable depreciation after completion. Note mortgagee-endorsed checks, which can delay funds.
6. Contract and schedule only after the homeowner decides to proceed. Run `../contract-compliance-check/SKILL.md`; no deductible language beyond the homeowner's responsibility.
7. At completion, assemble the recoverable-depreciation release package: final invoice, completion certificate, photos, permit final, any carrier form.
8. Watch appraisal or matching disputes; refer the homeowner to the policy process and qualified representatives.

## Outputs
Claim file, meeting checklist, scope comparison, tracker, release package.

## Gates
- No legal advice, coverage opinions or adjusting (`../../knowledge/rules.md`, Tier 1).
- `../deductible-and-inducement-gate/SKILL.md` on every outward message.
- Written homeowner permission before communicating with the carrier on their behalf.
- Owner signs off on documents sent to the carrier.
- Assignment of benefits and direction-to-pay documents need counsel review (VERIFY).

Workflow: `../../workflows/04-insurance-claim-support.md`.
