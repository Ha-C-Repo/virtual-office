---
name: ar-milestone-billing
description: Milestone invoicing, overdue reminders at 7, 14 and 21 days, and receivables status tracking. Drafts only.
---
# Accounts receivable and milestone billing

## When to use
At each contract milestone and weekly for the overdue sweep.

## Inputs
Project record (contract sum, signed date, milestones paid, material arrived, percent complete), invoice register.

## Steps
1. Milestone pattern: fixed deposit; percentage at signing; percentage on material arrival; percentage on progress against the schedule of values.
2. Draft the invoice: number, project, client, date, due date, milestone, amount, status.
3. Statuses: draft, sent, paid, overdue. Only {{OWNER_ROLE}} moves a draft to sent.
4. Overdue sweep: reminders drafted at 7, 14 and 21 days; each increments the reminder count.
5. Quote validity: track the expiry window on each quote.
6. Report aging by client.

## Outputs
Invoice drafts (`../../templates/invoice.md`), reminder drafts, aging table.

## Gates
Amounts come from the contract or schedule; if unclear, flag. After approval, never edit an amount; issue an adjustment.
