---
name: service-we-owe-generator
description: Generates due bills, repair authorizations and goodwill repair records with client and internal copies and an overdue check.
---
## Document types
- DUE BILL: one line per promise (item, who owes, promise date, status).
- REPAIR AUTHORIZATION: defect reference, repair, authorizer, internal cost.
- GOODWILL REPAIR: post-sale, no implied legal obligation.

## Steps
1. Number `WO-<unit>-<NNN>`.
2. Pull promises from the delivery conversation, recon work order and sales notes.
3. Client copy (`../../templates/service-we-owe.md`): no cost.
4. Internal copy (`../../templates/service-we-owe-int.md`): cost, markup, total.
5. Status: DRAFT, APPROVED, OPEN, FULFILLED, CANCELED.
6. Daily overdue check. Same-day escalation for any past promise date.

## Gates
A promise not on the we-owe is a defect (copy Sales). Closing a recon item and fulfilling its we-owe is one action.
