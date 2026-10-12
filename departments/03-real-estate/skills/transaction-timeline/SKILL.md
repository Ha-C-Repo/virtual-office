---
name: transaction-timeline
description: Contract-to-close engine: extract dates from the executed contract, compute days-until, publish the calendar, checklists by transaction type.
---
# Transaction Timeline

## When to use
Within 24 hours of an executed contract for {{TRANSACTION_ID}}.

## Inputs
Executed contract and addenda, transaction type, parties' roles, lender and title contacts (as placeholders until supplied).

## Steps
1. Extract: effective date, option period end, financing deadline, appraisal deadline, title and survey deadlines, HOA document deadline, closing date. Cite the clause for each.
2. Compute days-until for each with a script.
3. Publish the calendar to {{CALENDAR_LOCATION}}.
4. Build the document checklist for the transaction type (cash, financed, new construction, HOA property).
5. Daily: re-pull deadlines and pass them to `../deadline-risk-detector/SKILL.md`.
6. Near closing: build the closing checklist (final walkthrough, funds, keys, utilities, post-closing follow-up).

## Outputs
Dated deadline table, calendar entries, checklists, daily pull.

## Gates
Dates are read, never inferred. If a clause is ambiguous, ask the principal. Amendments that change dates go through `../amendment-generator/SKILL.md` and owner approval.
