# Workflow: Security Remediation

Skill: `../skills/security-remediation-cycle/SKILL.md`; checks: `../skills/tenant-isolation-review/SKILL.md`.

1. Collect audit or test output. Build the triage ledger (id, location, class, severity, status).
2. Triage. **Gate:** technical owner confirms severity ordering.
3. Batch fixes into executor prompts (`../templates/code-executor-prompt.md`).
4. Implement and review each batch.
5. Sibling triage: search for the same pattern in the rest of the code.
6. Cross-tenant access sweep of every route that reads by id.
7. Verification probe in staging, then production. **Gate:** written authorization for any live test.
8. Rotate secrets as needed; record without values.
9. **Gate (sign-off):** principal decides on a customer notice; counsel reviews.
10. Close the ledger entries only with recorded verification. Schedule the next external test.
