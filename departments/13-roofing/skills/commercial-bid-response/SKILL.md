---
name: commercial-bid-response
description: Respond to commercial roofing bid documents with a requirements matrix, pre-bid walk, system selection, scope and compliant submission.
---
# Commercial Bid Response

## When to use
Invitations to bid, requests for proposal and negotiated commercial work on low-slope or steep-slope roofs.

## Inputs
Bid documents, drawings and specs, addenda, building access, moisture survey if any, manufacturer requirements, company qualifications.

## Steps
1. Build a requirements matrix: required years of experience, certifications, manufacturer-approved applicator status, insurance limits, bonding if any, substitution controls, warranty term and type, schedule, safety submittals, addenda received.
2. Decide bid / no bid with the owner by {{BID_DECISION_DEADLINE}} using capacity, qualifications and margin.
3. Pre-bid walk: photograph, measure, note access, parapets, drains, scuppers, curbs, penetrations, roof loads, existing system and layers, wet insulation signs, power and utility lines, safety edges and openings. Use `../roof-moisture-survey-planner/SKILL.md` where moisture is suspected.
4. System selection: compare TPO, PVC, EPDM, modified bitumen and coating options for the building using illustrative lifespan ranges and manufacturer constraints (VERIFY). Check wind uplift, insulation and energy code requirements with a design professional where required.
5. Quantities: measure and run `../../harnesses/takeoff_calc.py` for sloped steep-slope areas; flat-roof areas are measured directly. Include insulation, cover board, flashing lengths, accessories and disposal.
6. Price from {{PRICE_BOOK}} with `../../harnesses/job_cost.py price` for margin checks. State alternates, unit prices for wet insulation replacement and exclusions.
7. Complete `../../templates/commercial-bid-response.md`; reconcile every requirement; confirm addenda.
8. Review safety plan and warranty form with `safety-officer` and `service-warranty-coordinator`.
9. On award: kickoff, submittals, pre-installation meeting, permit, schedule.

## Outputs
Requirements matrix, bid package, exclusions and clarifications list.

## Gates
- Owner signs every bid.
- Do not bid a warranty the company is not approved to install.
- Substitutions only as the documents allow.
- Estimating and QC overlap with `../../../01-construction/README.md`; use its practices where they are stricter.

Workflow: `../../workflows/11-commercial-bid-to-award.md`.
