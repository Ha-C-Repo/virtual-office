# 09 Change Control

Owner: office-manager with the IT / executive assistant ({{IT_DIRECTOR}}) | Approver: {{OWNER}}

## Steps
1. Read the changelog.
2. Run the office health check.
3. Make the smallest edit that solves the problem.
4. Compile or validate.
5. Run the offline regression ("practice run"). Add a regression row for every defect fixed.
6. If any skill was edited, run the skills audit (skill prose matches the canonical rules list).
7. Back up before overwriting any FINAL or DELIVERED file; write protected files through the safe-write script with a timestamped backup.
8. Redact secrets from logs and handoffs.
9. Record the change in the changelog and the handoff note.
10. SIGN-OFF: owner approves any Tier 1 or Tier 2 rule change.

## Principles
Secrets live outside the repository. Nothing is deleted without approval; retire to an archive.
