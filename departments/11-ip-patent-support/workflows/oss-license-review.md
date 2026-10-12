# Workflow: Third-Party License Review

Run before each release, before shipping firmware, and before diligence.

1. Generate the component list from manifests and build files (`../skills/oss-license-tracking/SKILL.md`).
2. Fill `../templates/third-party-license-inventory.md`. Every row needs a license file path or an "unknown" flag.
3. Triage categories. List flags: distributed copyleft or source-available, unknown, restricted-use models or data, attribution duties.
4. Build the notice file from the licenses' own required texts.
5. **Gate (sign-off):** counsel reviews the flag list. Coordinator and principal approve release only when no unknown and no unreviewed flag remains.
6. Archive the inventory with the release record.
