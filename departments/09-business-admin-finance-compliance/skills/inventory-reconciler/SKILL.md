---
name: inventory-reconciler
description: Logs asset sessions to the register, assigns tags, runs the lifecycle clock (hold, release, markdown, liquidation flag), and reconciles register versus physical counts.
---
# Inventory reconciler

## When to use
After every production session, weekly with the yield audit, and when an order or listing refers to an asset.

## Inputs
Session notes from staff, the register, the occupancy map, the lifecycle schedule, physical count.

## Steps
1. Log each new asset: assign a unique global asset tag, record creation date, source lineage, address (unit . tier . zone . cell), hold-until date.
2. Lifecycle clock: hold period (no sale until the clock releases it), release day, markdown day, liquidation or bundle flag day. Only the clock releases a hold. Never shorten a hold.
3. Reconcile register versus physical count. Tag the count VERIFIED if a physical count occurred within the freshness window; otherwise ESTIMATED.
4. Compare mix ratios to targets by tier and flag variance.
5. Block listings when the hold is active, a photo is missing, or identification is unconfirmed.
6. Output exceptions to the human review list.

## Outputs
Updated register rows, occupancy summary by tier versus target share, exceptions list.

## Gates
Never delete an entry; corrections append. Never mark VERIFIED without a recent physical count (`../verify-dont-generate/SKILL.md`).
