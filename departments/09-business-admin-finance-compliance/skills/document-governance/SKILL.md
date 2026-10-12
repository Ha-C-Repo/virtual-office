---
name: document-governance
description: Rules for keeping policy and protocol documents consistent: source wins, additive revisions, append-only corrections, and skill disposition triage.
---
# Document governance

## When to use
Whenever documents conflict, are revised, or when migrating a template from another domain.

## Rules
- Source SOPs win on protocol conflicts. Flag; never silently pick.
- Revisions are additive with effective dates.
- Corrections append; never overwrite. Log in `../../templates/changelog.md`.
- Back up before overwriting any protected file.

## Skills disposition triage (when adopting a template from another domain)
Classify each inherited skill KEEP, ADAPT, RETIRE or BUILD. Absolute priorities: first anything that guards money or compliance; then anything that logs data; then convenience. Build new skills in priority order and test each before scheduling it.

## Outputs
Conflict list; disposition table; changelog line.

## Gates
{{OWNER_ROLE}} approves dispositions.
