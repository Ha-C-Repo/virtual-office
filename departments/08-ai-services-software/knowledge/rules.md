# Rules: AI Services and Software

## Engineering (constitution-style)
1. Tenant id on every query; zero cross-tenant tolerance.
2. Feature flags default OFF; staged inert, then one restart window.
3. No secrets in code, logs, records or chat. Rotate on exposure.
4. Model names come from configuration; max tokens always set; cost and tokens logged on every call.
5. Payments: signed webhooks, idempotency keys.
6. Staging uses production schema with synthetic data only.
7. Backups are proven by restore.
8. Prove fixes in production before closing.
9. Structural code requires a passed spec.
10. Amendments to the constitution require explicit owner approval and a decision record.

## Behavior
- Never invent customers, partners, testimonials, metrics, license numbers or guarantees.
- Confidential-prefixed files are never output.
- Surface confusion; minimum output; stay in lane; goal-driven with success criteria.
- Never run live tests without written authorization.
- Never replace licensed professionals.

## Approvals
- Principal: all external communications, pricing, notices, contracts.
- Technical owner: all shipped code.
- Material risk changes surfaced to both.

## Generic regulatory touchpoints (consult counsel)
Privacy laws (state and international), children's online privacy (COPPA), email and text marketing rules (CAN-SPAM, TCPA), biometric privacy statutes, payment card standards, SOC 2 criteria, accessibility standards.
