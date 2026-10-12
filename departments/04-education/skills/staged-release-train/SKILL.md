---
name: staged-release-train
description: Dormant release train: preconditions, internal track, staged rollout, advance and rollback rules, postmortem.
---
# Staged Release Train

## When to use
Only after the owner lifts the store freeze.

## Preconditions (all required)
Owner lifts the freeze; store accounts ready; signing keys secured outside the repository; privacy policy live; compliance checklist passed (`../release-compliance/SKILL.md`); release pair passed (`../release-pair-check/SKILL.md`); human on-device QA done.

## Steps
1. Internal track release.
2. Staged rollout in steps of {{ROLLOUT_STEPS}}.
3. Advance a step only if crash-free rate and ANR rate hold at or above {{CRASH_FREE_FLOOR}} and below {{ANR_CEILING}}.
4. Roll back on any gate breach, any integrity or children's-data defect, or an owner stop.
5. File the release pair and a postmortem (`../../templates/postmortem-note.md`) for every run, including rollbacks.

## Outputs
Release log, postmortem.

## Gates
The owner is the only person who can lift the freeze or approve advancing past {{OWNER_APPROVAL_STEP}}.
