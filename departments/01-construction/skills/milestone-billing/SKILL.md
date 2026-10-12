---
name: milestone-billing
description: Issues milestone invoices, tracks receivables and overdue reminders, applies statutory late-payment interest logic, and seeds the pay application schedule of values.
---
## When to use
At every billing milestone and in the daily receivables review.

## Inputs
Project record, milestone schedule, contract terms, payments received.

## Steps
1. Milestone pattern: fixed submittal deposit, percentage at signing, percentage on material arrival, percentage on schedule-of-values progress.
2. Create invoice from `../../templates/milestone-invoice.md`. Status path: draft, sent, paid, overdue.
3. Quote validity window recorded on bids.
4. Overdue reminders at 7, 14 and 21 days. Draft each; the {{APPROVER_ROLE}} sends.
5. Late-payment interest: compute with the calculator per the statute or contract term.
6. Pay application: fill `../../templates/pay-application-seed.md` with percent complete per schedule-of-values line.
7. Maintain the lien calendar; surface preliminary notice and filing dates.

## Outputs
Invoice, reminders, receivable aging, pay application draft.

## Gates
Percent complete comes from verified field data (site diary), never estimated. Invoices are DRAFT until signed.
