---
name: contract-compliance-check
description: Check a residential roofing contract package for required contents, state-specific notices and prohibited terms before it goes out for signature.
---
# Contract Compliance Check

## When to use
Before every contract, change order that alters price, and renewals of maintenance agreements.

## Inputs
Draft contract (`../../templates/residential-contract.md`), proposal, state rules file ({{STATE_RULES}}), license and insurance details.

## Checklist
1. Parties, address, dates, contact data.
2. {{LICENSE_NUMBER}} and insurance certificate available.
3. Scope of work and exclusions match the proposal.
4. Materials by product line and color, with the confirmation date.
5. Price, deposit, payment schedule; deposit within any state limit (VERIFY).
6. Start and completion windows with weather and material delay language.
7. Permit responsibility and who pays inspection fees.
8. Change-order clause (written, signed before work).
9. Warranty terms: workmanship term and exclusions; manufacturer and extended warranties described as separate documents.
10. Cancellation / rescission notice, including off-premises sales notice and any insurance-denial rescission right (VERIFY {{STATE}}). Record the date given.
11. Insurance clause: homeowner owns the claim, is responsible for the deductible and non-covered work. No deductible waiver, rebate, absorption or credit language.
12. Assignment of benefits or direction-to-pay language: removed unless counsel approved (VERIFY).
13. Lien language and waiver statements where required (VERIFY).
14. Dispute process and governing law ({{GOVERNING_LAW}}).
15. Signatures from every owner of record.

## Outputs
Pass/fail list with evidence and required fixes.

## Gates
- Any fail blocks sending. A warning is not a pass.
- `../deductible-and-inducement-gate/SKILL.md` must pass.
- Counsel reviews the template when state rules change; this skill does not give legal advice.
- Owner signs off before the contract is sent.

Workflow: `../../workflows/03-estimate-to-signed-contract.md`.
