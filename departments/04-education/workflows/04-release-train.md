# 04 Release Train

Owner: release-manager | Approver: {{OWNER}} (sole)

## Steps
1. GATE: the owner lifts the store freeze in writing.
2. Preconditions checked: accounts, signing keys outside the repo, privacy policy live, compliance table passed (`../skills/release-compliance/SKILL.md`), release pair passed (`05-two-artifact-release.md`), human on-device QA.
3. Internal track release.
4. Staged rollout in steps of {{ROLLOUT_STEPS}}.
5. Advance a step only if crash-free and ANR rates hold.
6. Rollback on any gate breach, any integrity or children's-data defect, or an owner stop.
7. File the release pair and a postmortem (`../templates/postmortem-note.md`) for every run.
8. Update the release context (`../templates/release-context-loader.md`).

## Outputs
Release log, postmortem, updated context.
