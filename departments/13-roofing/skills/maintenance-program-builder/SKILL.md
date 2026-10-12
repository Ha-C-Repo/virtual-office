---
name: maintenance-program-builder
description: Design and run a preventive roof maintenance agreement with seasonal inspections, photo-documented findings and owner-authorized repairs.
---
# Maintenance Program Builder

## When to use
For commercial building owners, property managers, and residential customers who want a recurring inspection plan; also after a new roof to protect the warranty.

## Inputs
Roof inventory and age, warranty terms and maintenance conditions, building access rules, owner contacts, emergency expectations, pricing from {{PRICE_BOOK}}.

## Steps
1. Inventory each roof: area, system, age, drains, penetrations, previous repairs, warranty status.
2. Define visit cadence: spring and fall inspections at minimum, plus after major storms (cadence {{VISIT_CADENCE}}).
3. Inspection scope: drains and scuppers cleared, seams, flashing, penetrations, membrane condition, ponding, sealants, rooftop equipment curbs, debris, signs of foot-traffic damage, gutters, interior leak sign checks.
4. Output per visit: findings with location, photo reference and severity (`../../templates/maintenance-inspection-report.md`).
5. Repairs: small repairs allowed under a pre-authorized limit ({{PREAUTH_LIMIT}}) in the agreement; others need owner authorization before work.
6. Emergency response: response windows and tarp terms stated in the agreement.
7. Agreement draft: `../../templates/annual-maintenance-agreement.md`. Include term, scope, exclusions, access, fee structure placeholders, renewal, and records handling.
8. Feed the visit records into the warranty log (`../warranty-registration-and-tracker/SKILL.md`).
9. Annual review: condition trend, remaining life estimate (illustrative, VERIFY), recommendations (repair, restore with coating, replace).

## Outputs
Program plan, visit schedule, inspection reports, authorization log, annual summary.

## Gates
- Owner signs agreements; the customer's authorization is recorded for repairs.
- Photo-documented deficiencies are mandatory; no photo, no finding.
- Fall protection and permits apply on every visit.
- No promise of leak-free performance.

Workflow: `../../workflows/12-maintenance-program-cycle.md`.
