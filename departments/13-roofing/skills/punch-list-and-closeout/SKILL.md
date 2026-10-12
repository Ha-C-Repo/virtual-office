---
name: punch-list-and-closeout
description: Build and close the punch list, run the customer walk-through, issue the completion certificate and release the final invoice.
---
# Punch List and Closeout

## When to use
After the final QC checklist, for every job.

## Inputs
QC checklist fails, customer comments, photo log, permit final result, change orders, contract.

## Steps
1. Create the punch list from QC fails and the customer walk-through (`../../templates/punch-list.md`): item, location, owner, due date, photo before, photo after.
2. Fix and retest; the quality inspector closes each item with an after photo.
3. Customer walk-through: show before and after photos, explain warranty layers and maintenance, collect questions. Never ask the customer to waive claims.
4. Confirm: permit final passed, cleanup and magnet sweep done, change orders signed and billed, material leftovers reconciled, dumpster removed.
5. Issue the completion certificate (`../../templates/completion-certificate.md`) after owner approval.
6. Trigger billing: final invoice goes out promptly (`../lien-waiver-tracker/SKILL.md` for the waiver exchange).
7. For insured jobs assemble the recoverable-depreciation release package with `../insurance-claim-support/SKILL.md`.
8. Start warranty registration (`../warranty-registration-and-tracker/SKILL.md`) and the review request (`../review-and-referral-compliance/SKILL.md`) after the customer is satisfied.

## Outputs
Closed punch list, completion certificate, final invoice trigger, warranty and review tasks.

## Gates
- No final invoice with open punch items unless the owner approves a written exception.
- Sub final payments follow `../subcontractor-vetting-and-payments/SKILL.md`.
- Owner signs the completion certificate.

Workflow: `../../workflows/09-closeout-to-final-payment.md`.
