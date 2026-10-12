---
name: store-listing-format
description: Structure and write the app store listing: what it does, who it serves, how it respects learning, privacy posture.
---
# Store Listing Format

## When to use
Creating or revising the store listing for {{APP_NAME}}.

## Inputs
Product spec, privacy map, brand voice, approved screenshots.

## Steps
1. What it does: one plain sentence, then three concrete capabilities.
2. Who it serves: grade bands and parents, stated without outcome promises.
3. How it respects learning: explains steps, checks answers with a solver, offers practice, never writes assignments for submission.
4. Privacy posture: offline-first, no account, camera used only for photo intake, no ads. Must match the compliance table.
5. Keywords via `../aso-listing/SKILL.md`.
6. Scrub via `../public-copy-scrubber/SKILL.md`.

## Outputs
Listing text in `../../templates/store-listing.md`.

## Gates
Every claim is true of the shipped build. Owner approves.
