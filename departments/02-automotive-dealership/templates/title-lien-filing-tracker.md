# Lien Filing Tracker: {{DEALERSHIP}}

Financed deals only. A lien is perfected when recorded on the title by the state, not when the paperwork is mailed. "Filed" and "recorded" are separate columns.

| Deal | Unit (stock / VIN) | Lienholder ({{LENDER}}) | Title application filed | Method | Filing deadline | Recorded by state | Lienholder confirmed | Title returned to | Status |
|---|---|---|---|---|---|---|---|---|---|
| {{DEAL_REF}} | {{STOCK_NUMBER}} / {{VIN}} | {{LENDER}} | {{DATE}} | {{WALK_IN / MAIL / ELECTRONIC}} | {{DATE}} | {{DATE_OR_PENDING}} | {{YES_NO}} | {{LENDER_OR_BUYER}} | NEEDS_INPUT / FILED / RECORDED / OVERDUE |

## Rules
1. Unknown filing day count is NEEDS_INPUT. Confirm with the state authority text and mark VERIFY.
2. Any row within 7 days of deadline and not FILED is THIS WEEK. Within 3 days is URGENT. Both go in the morning briefing.
3. A row OVERDUE is escalated to {{OWNER}} the same day.
4. Keep proof of filing in the jacket and the tracking reference here.
