---
name: ota-update-plan
description: Plan over-the-air firmware and app updates with signing, staged rollout, rollback and records.
---
# OTA Update Plan

## When to use
Designing the update path before pilot, and before each release after.

## Inputs
Firmware architecture design lock, `../../templates/ota-release-checklist.md`, fleet inventory.

## Steps
1. Confirm the design lock covers signed images, version checks, secure boot or equivalent, and a recovery path.
2. Define release stages: internal devices, small canary group, wider groups, full fleet. Set hold times and stop criteria.
3. Define rollback: how a device returns to the last good image, and what happens if power fails mid-update.
4. Define monitoring: update success rate, failure reasons, device health after update.
5. Define communication: user notice, support script, incident path.
6. Keep a release record: version, hash, test evidence, approver, stage dates, issues.

## Outputs
Completed OTA release checklist per release.

## Gates
Principal approves each production release. A failed canary stops the rollout until a finding is closed.
