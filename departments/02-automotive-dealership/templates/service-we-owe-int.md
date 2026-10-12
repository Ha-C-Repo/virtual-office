# We-Owe -INT (internal only): {{WO_NUMBER}}

Twin of `service-we-owe.md`. Never shown to the customer.

Unit: {{STOCK_NUMBER}}   Deal: {{DEAL_REF}}   Promise date: {{PROMISE_DATE}}   Status: DRAFT / APPROVED / OPEN / FULFILLED / CANCELED
Approved by: {{OWNER}} on {{DATE}}   Responsible: {{RECON_LEAD}}

| Line item | Direct cost | Markup percent | Total cost | Vendor (category) | Linked recon item |
|---|---|---|---|---|---|
| {{ITEM}} | {{DIRECT_COST}} | {{MARKUP_PCT}} | {{TOTAL_COST}} | {{VENDOR}} | {{RECON_ITEM_REF}} |

Total direct cost: {{DIRECT_COST_TOTAL}}   Total cost: {{TOTAL_COST_TOTAL}}   (calculator output; audit ref {{CALC_AUDIT_REF}})
Charged to: unit recon budget / deal gross / goodwill {{ACCOUNT}}

## Overdue check
Run daily. Any item past its promise date escalates to {{OWNER}} the same day. This is the single most damaging failure class.
Days overdue: {{DAYS_OVERDUE}}   Escalated: {{YES_NO}} on {{DATE}}   New promise date agreed with buyer (written): {{DATE_OR_NONE}}

Fulfilled date: {{FULFILLED_DATE}}   Customer sign-off on file: {{YES_NO}}   Notes: {{NOTES}}
