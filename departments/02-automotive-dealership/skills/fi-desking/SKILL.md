---
name: fi-desking
description: Deal structure, payment scenarios by credit tier, lender submission, stipulations and the covered-borrower check. Calculator only.
---
## Inputs
Unit price and disclosure requirements, credit application, locked deal economics, lender responses.

## Steps
1. Pull price from the unit record.
2. Calculator: payment scenarios at list, mid and floor tiers; out-the-door; negative-equity rollover; LTV; payment-to-income. Audit log kept.
3. Covered-borrower check (`../fi-military-lending/SKILL.md`).
4. Flag exclusion-voiding structures before submission.
5. Submit packet (`../../templates/fi-lender-packet-checklist.md`) and track stips (`../../templates/fi-stipulation-tracker.md`).
6. Product menu with transparent pricing (`../../templates/fi-product-menu.md`).
7. Decline: adverse-action notice.
8. Build the client recap and `-INT` sheet together.

## Outputs
Structure, scenarios, packet, recap and twin.

## Gates
Any payment shown to a customer carries the full disclosure block (down payment, repayment terms with payment amount and months, APR, possible rate increase after approval). Credit data never goes through unpaid AI APIs.
