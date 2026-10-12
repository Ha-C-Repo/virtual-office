# Workflow: Incident Response

Template: `../templates/incident-report.md`.

1. **Detect and declare.** Assign severity: SEV1 (data exposure or full outage), SEV2 (major feature down), SEV3 (degraded), SEV4 (minor).
2. **Contain.** Stop the bleeding: disable the flag, block the route, rotate exposed secrets.
3. **Investigate read-only** (`../skills/evidence-discipline/SKILL.md`). Timeline with sources.
4. **Notify.** SEV1/SEV2: technical owner and principal immediately. **Gate:** principal approves any customer communication; counsel reviews anything involving personal data.
5. **Fix** via the normal lifecycle, shortened but not skipped; record the change.
6. **Verify in production.**
7. **Communicate.** Outage notice or `../templates/security-notice.md`.
8. **Postmortem** within {{POSTMORTEM_DAYS}} days: blameless, root cause, follow-ups with owners.
9. Update runbooks and the spec index.
