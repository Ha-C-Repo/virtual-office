---
name: environment-promotion
description: Move a change through local, dev, staging, beta and production with flags off by default and a rollback ready.
---
# Environment Promotion

## When to use
Whenever a change is going to a shared environment.

## Environments
local -> dev -> staging (production schema, synthetic data only) -> beta (opted-in customers) -> production.

## Steps
1. Confirm the change has a spec and an approved plan.
2. Deploy to staging with the feature flag OFF ("staged inert"). Verify nothing changed.
3. Run migrations on a restored copy of the production schema first; write the result into a staging record.
4. Activate in one restart window. Watch error rate and AI cost telemetry.
5. Verify in production with a specific, repeatable check. Prove the fix in production before declaring it closed.
6. Write the deploy record (`../../templates/deploy-record.md`), including rollback steps and the verification result.

## Gates
- Staging never holds real customer data.
- Backups are proven by restoring into a scratch database, not by assuming.
- Technical owner approves activation; principal approves customer-facing announcements.
- If drift is found between served code, repository and copies, stop and record it as a finding.
