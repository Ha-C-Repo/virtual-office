# Workflow: Environment Promotion

Skill: `../skills/environment-promotion/SKILL.md`.

1. Confirm approved spec, reviewed diff, passing tests.
2. Local to dev: automated tests, smoke test.
3. Dev to staging: production schema, synthetic data only. Deploy flag OFF. Verify no behavior change.
4. Migration rehearsal on a restored copy. Write a staging record.
5. **Gate (sign-off):** technical owner approves activation window.
6. Beta: opt-in customers only; principal approves who is included.
7. Production: activate in one restart window; monitor errors, latency, AI cost for {{WATCH_HOURS}} hours.
8. Verify with the specific production check. Record in `../templates/deploy-record.md`.
9. If verification fails: roll back using the recorded steps; open a finding.
