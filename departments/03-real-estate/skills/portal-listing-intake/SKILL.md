---
name: portal-listing-intake
description: Compliant intake of a listing from a portal, the MLS or an address, pulling only what licensing allows.
---
# Portal Listing Intake

## When to use
You have an address or listing reference and need a starting record for the CMA or tour.

## Inputs
{{PROPERTY_ADDRESS}} or listing reference; the data access the brokerage is licensed for.

## Steps
1. Pull only what the license and terms of use allow. If a source does not allow it, ask the agent to export or upload instead.
2. Store each field with source, date and confidence. Public web data is LOW.
3. Feed the tour engine and CMA only with fields at MEDIUM or higher, or with a human-confirmed LOW field marked as such.
4. Create the folder structure and run `../listing-doc-classifier/SKILL.md`.

## Outputs
Intake record with per-field source and confidence; gap list.

## Gates
LOW data can never set a property fact, comp or valuation. Respect MLS terms (see `../../knowledge/rules.md`).
