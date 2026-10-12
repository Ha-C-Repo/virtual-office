# Stipulation Tracker: {{DEAL_REF}}

Lender: {{LENDER}}   Unit: {{STOCK_NUMBER}}   Owner of tracker: {{FI_MANAGER}}
A deal is not reported funded while a lender stipulation is open.

| # | Stipulation (as written by lender) | Requested | Due | Customer contacted (date, channel) | Received | Verified by | Status |
|---|---|---|---|---|---|---|---|
| 1 | {{STIP_1}} | {{DATE}} | {{DATE}} | {{CONTACT_LOG}} | {{DATE_OR_OPEN}} | {{VERIFIER}} | OPEN / RECEIVED / SUBMITTED / CLEARED |
| 2 | {{STIP_2}} | {{DATE}} | {{DATE}} | {{CONTACT_LOG}} | {{DATE_OR_OPEN}} | {{VERIFIER}} | OPEN |
| 3 | {{STIP_3}} | {{DATE}} | {{DATE}} | {{CONTACT_LOG}} | {{DATE_OR_OPEN}} | {{VERIFIER}} | OPEN |

Common stips: proof of income, proof of residence, references, insurance binder, down payment verification, signed contract.

## Rules
1. Any contact with the customer is drafted and sent through `../workflows/02-sales-outbound-message.md`.
2. Documents received go in the jacket and the data processing register.
3. Open past due date: tell {{FI_MANAGER}} and {{OWNER}} the same day.
4. All stips CLEARED is a precondition to marking the deal FUNDED in the pipeline.
