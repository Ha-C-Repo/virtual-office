# Routine Rollout (build manual first, then schedule)

## Principle
Every routine is run by hand and verified before it is scheduled. A scheduled routine has an explicit "may never do" list.

## Core routines
1. Register logger.
2. Readings exception monitor.
3. Asset lifecycle clock (hold, release, markdown, liquidation flag).
4. Inventory reconciler.
5. Order intake and fulfillment check.
6. Weekly yield audit.
7. Quarantine clock.
8. Consumables reorder trigger.

Stretch routines: reserve sweep, growth velocity tracker, photo-to-listing draft, permit and trade-document calendar.

## Steps per routine
1. Write the manual procedure and output template.
2. Run it three times by hand with a human checking each output.
3. Define freshness windows and confidence tags.
4. Write the "may never do" list (never shorten a hold, never discount below schedule, never delete entries, never mark VERIFIED without a recent count).
5. GATE: {{OWNER_ROLE}} signs off before scheduling.
6. Schedule. Review output weekly for the first month.
7. Log the rollout in the changelog.

## Disposition when adopting from another domain
Triage each skill KEEP, ADAPT, RETIRE or BUILD (`../skills/document-governance/SKILL.md`).
