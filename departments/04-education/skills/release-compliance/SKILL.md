---
name: release-compliance
description: Pre-release compliance audit: audience rules, permission audit, data-safety cross-check from measured behavior, content rating, integrity check, pass/fail evidence table.
---
# Release Compliance

## When to use
Before every internal-track or production release candidate.

## Inputs
Build artifact, manifest/permission list, store data-safety draft, privacy policy text, measured network and storage behavior, listing copy.

## Steps
1. Audience rules: declared age bands match behavior and copy.
2. Permission audit: each permission maps to a feature. Expected: network and camera only. Anything else is FAIL.
3. Data-safety cross-check: declarations are compared with measured behavior (what the app actually sends and stores), not with intentions.
4. Content rating questionnaire answers consistent with the product.
5. Integrity check: listing, screens and strings contain nothing that invites ghostwriting or cheating.
6. Privacy policy live and consistent with the map.
7. Fill `../../templates/release-compliance-table.md` with evidence for each row.

## Outputs
Pass/fail evidence table.

## Gates
Any FAIL blocks the release. Owner signs off.
