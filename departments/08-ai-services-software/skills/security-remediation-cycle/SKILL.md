---
name: security-remediation-cycle
description: Audit, triage ledger, batched fixes, sibling triage, cross-tenant sweep, verification probe, security notice.
---
# Security Remediation Cycle

## When to use
After a security audit, a penetration test report, or a discovered flaw.

## Steps
1. **Audit** findings into a triage ledger: id, location, class, severity, status.
2. **Triage** by severity and exploitability. Credential and cross-tenant issues first.
3. **Batch** fixes into small prompts for the executor, grouped by area.
4. **Sibling triage.** For every flaw, search for the same pattern elsewhere.
5. **Cross-tenant sweep.** Check every route that reads by id for tenant scoping.
6. **Verification probe.** Re-test each fix in staging, then production, with written authorization for any live testing.
7. **Rotate** any exposed secret; record rotation without values.
8. **Security notice** to affected customers if warranted (`../../templates/security-notice.md`), approved by the principal and, where needed, an attorney.

## Gates
Written authorization before any live test. Nothing marked closed without a recorded verification.
