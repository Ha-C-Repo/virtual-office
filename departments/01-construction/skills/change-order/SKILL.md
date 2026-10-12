---
name: change-order
description: Prices and drafts a standard-form change order from a qualified scope-creep event, at locked rates plus a stated markup. Draft only.
---
## When to use
After scope-creep-detector confirms creep, per `../../workflows/06-scope-creep-to-change-order.md`.

## Inputs
Trigger text, original contract reference, locked rates, markup, schedule information.

## Steps
1. Number it `CO-{{DATE}}-{{SEQ}}` sequentially per project.
2. Describe the work, reason and scope basis (what in the contract it falls outside of).
3. Estimate: engineering hours, shop hours, tons times blended hours, overhead and profit multiplier. Arithmetic by calculator.
4. State schedule impact in days.
5. Fill `../../templates/change-order.md`.
6. Status path: DRAFT, PENDING_APPROVAL, SUBMITTED, ACCEPTED or REJECTED.
7. Track margin on change orders separately from base contract.

## Outputs
Change order draft and register entry.

## Gates
- The {{APPROVER_ROLE}} signs before submission.
- No work proceeds unsigned.
- Rates are locked; the markup is stated, not hidden.
