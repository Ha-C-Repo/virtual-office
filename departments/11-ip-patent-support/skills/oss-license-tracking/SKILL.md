---
name: oss-license-tracking
description: Build and refresh the third-party component and license inventory for software, firmware, models, data and media.
---
# Open-Source and Third-Party License Tracking

## When to use
Before a release, before shipping firmware or an app, before a pilot, before due diligence, and on each dependency change.

## Inputs
Dependency manifests and lockfiles, firmware build manifests, model and dataset cards, font and media sources, `../../templates/third-party-license-inventory.md`.

## Steps
1. List components from manifests, not from memory: direct and transitive for software, SDKs and RTOS for firmware, models and datasets, fonts, stock media.
2. For each, record name, version, source URL, license identifier (SPDX id when the project gives one), where it is used, and how it is distributed (server only, shipped in device, shipped in app, build tool only).
3. Triage category: permissive, copyleft, source-available, proprietary, unknown.
4. Flag for counsel: copyleft or source-available in anything distributed; any "unknown"; any model or dataset whose terms limit commercial use; any component with a notice or attribution duty.
5. Collect the notices and attributions the licenses require and place them in the product's notice file.
6. Date the inventory and name who checked it.

## Outputs
Completed inventory, notice file, flag list for counsel.

## Gates
No release with an unresolved "unknown" or an unreviewed flag. Counsel decides compatibility.
