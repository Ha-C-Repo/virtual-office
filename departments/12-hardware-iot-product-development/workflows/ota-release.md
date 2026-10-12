# Workflow: OTA Release

1. Complete `../templates/ota-release-checklist.md`.
2. **Gate (sign-off):** principal approves the production release.
3. Release to internal devices; hold; check metrics.
4. Release to canary group; hold; check success rate against stop criteria.
5. Widen in stages. At any stop criterion, halt and open a finding.
6. Failed update: use the rollback path; record device counts and causes.
7. Close the release record with stage log and issues.
