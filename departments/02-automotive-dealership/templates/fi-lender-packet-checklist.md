# Lender Packet Checklist: {{DEAL_REF}}

Lender: {{LENDER}}   Submitted by: {{FI_MANAGER}}   Date: {{DATE}}
Customer credit data stays in paid, approved systems only. Never paste it into an unpaid AI tool.

## Before submission
- [ ] Unit price pulled from the unit record (`inventory-unit-record.md`), not retyped.
- [ ] Payment scenarios run through the calculator (list, mid, floor tier); audit ref {{CALC_AUDIT_REF}}.
- [ ] Covered-borrower check recorded.
- [ ] Structure reviewed for exclusion-voiding items; owner informed of any flag.
- [ ] Minimum down for the credit tier met.

## Packet contents
- [ ] Credit application, complete and signed
- [ ] Proof of identity: {{ID_TYPE}}
- [ ] Proof of income: {{INCOME_DOCS}}
- [ ] Proof of residence: {{RESIDENCE_DOC}}
- [ ] Insurance information
- [ ] Vehicle information: VIN {{VIN}}, mileage, price, buyer's guide
- [ ] Trade-in payoff letter (if trade)
- [ ] Lender-specific forms: {{LENDER_FORMS}}

## Response
Decision: {{APPROVED / CONDITIONAL / DECLINED}}   Date received: {{DATE}}
Approved terms: rate {{APR}}, term {{TERM_MONTHS}}, advance {{ADVANCE}}
Stipulations: track in `fi-stipulation-tracker.md`
If declined: adverse-action notice (`fi-adverse-action-notice.md`) the same business day it is drafted for sign-off.
