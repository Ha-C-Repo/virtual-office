# 09 Steel Procurement

Owner: contract-administrator.

1. Pull verified tonnage by shape family from the frozen takeoff.
2. Check long-lead items and delivery windows against the erection schedule.
3. For high-value anchors and items over the threshold, request three supplier quotes in parallel. Log all in the quote log (`../skills/supplier-quote-tracker/SKILL.md`). Quotes are internal only.
4. Compare price, lead time, terms, expiration.
5. Draft purchase orders (`../skills/steel-purchase-order/SKILL.md`, `../templates/purchase-order.md`) using the supplier rate card and calculator.
6. **HUMAN SIGN-OFF:** {{APPROVER_ROLE}} approves before sending.
7. Track status: draft, approved, sent, confirmed.
8. On delivery, hand to shop-qc-inspector for receiving (`10-shop-qc-three-gate.md`). Heat numbers must match test reports.
9. Check domestic-material requirement where the contract imposes one.
