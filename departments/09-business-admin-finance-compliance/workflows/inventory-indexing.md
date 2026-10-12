# Inventory Indexing

Agent: records keeper.

## Steps
1. Define the address scheme: unit . tier . zone . cell.
2. Create the per-unit context folder: spec, readings log, occupancy grid, lineage, human-only standing notes; plus logs folders (incidents, watch, work sessions) and photos.
3. Photo intake: each photo is keyed to an address and date.
4. Update the occupancy map (`../templates/occupancy-map.md`) from register rows.
5. Quarterly physical count; tag the count VERIFIED with date.
6. Variance against mix targets goes to {{OWNER_ROLE}}.

## Gates
Standing notes are read, never edited. Missing address means flag it.
