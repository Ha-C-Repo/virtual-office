# Adverse Action Notice: {{DEALERSHIP}}

Send on every decline, counteroffer on different terms, or approval on terms the applicant did not request. {{FI_MANAGER}} drafts. {{OWNER}} signs. Nothing is sent without sign-off. The notice goes out within the legal window for the state; confirm that window in `../knowledge/rules.md` and with counsel.

Date: {{DATE}}
To: {{CUSTOMER_NAME}}
Address: {{CUSTOMER_ADDRESS}}
Deal reference: {{DEAL_REF}}   Unit: {{STOCK_NUMBER}}

Thank you for applying for credit with {{DEALERSHIP}}. We are not able to offer you credit on the terms you requested.

Action taken: {{DECLINED / COUNTEROFFER / DIFFERENT_TERMS}}

Principal reasons (use only reasons that are true and recorded on the lender response):
1. {{REASON_1}}
2. {{REASON_2}}
3. {{REASON_3}}

Credit reporting agency used (complete only if a consumer report was a factor):
Name: {{CREDIT_BUREAU_NAME}}
Address: {{CREDIT_BUREAU_ADDRESS}}
Phone: {{CREDIT_BUREAU_PHONE}}
The agency did not make this decision and cannot explain why it was made. You have the right to a free copy of your report if you ask within the period stated by law, and the right to dispute inaccurate information.

Equal credit opportunity statement: {{REQUIRED_ECOA_STATEMENT_TEXT}}

Creditor name and contact: {{LENDER}} / {{DEALERSHIP}}, {{ADDRESS}}, {{PHONE}}

Signed: {{OWNER_SIGNATURE}}

## Internal checklist (remove before sending)
- [ ] Lender response saved to the deal jacket.
- [ ] Reasons match the lender response word for word in substance.
- [ ] Covered-borrower check already recorded for this deal.
- [ ] Client-doc scrubber run (`../skills/fi-client-doc-scrubber/SKILL.md`): no cost, pack, reserve or gross.
- [ ] Copy of notice and date sent filed in the jacket (`title-deal-jacket-checklist.md`).
