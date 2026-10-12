# 13 Roofing (Residential, Storm Restoration, Commercial and Service)

## Purpose
A virtual office for a roofing contractor run by an owner/operator ({{OWNER}}) with a small office team and crews. The AI layer drafts, checks, calculates and organizes. Humans own every contract, every dollar decision, every claim document and every outward message. Core rule: **verify, do not generate**. Quantities, claim payments and margins come from the scripts in `harnesses/`, not from model arithmetic.

Content comes from public-source research and is generic. Facts from general knowledge or conflicting sources carry a **VERIFY locally** tag. See `knowledge/research-notes.md`.

## Scope
1. Residential retail re-roof and repair
2. Insurance and storm restoration (documentation and claim support, not adjusting)
3. Commercial low-slope (TPO, PVC, EPDM, modified bitumen, coatings) and steep-slope
4. Maintenance and service programs
5. Optional gutter and siding add-ons (use the same estimate, contract and QC flow)
6. Lead intake and speed-to-lead; storm surge response
7. Safety, quality, closeout, warranty, finance, marketing and compliance

## When to use
Any task touching a roof lead, inspection, measurement, estimate, contract, claim, permit, material order, crew, safety plan, QC check, invoice, warranty or marketing item. Not for legal, coverage, engineering or tax advice; it produces organized drafts for licensed humans to decide.

## Hard rules
- Never waive, rebate or absorb a deductible (`skills/deductible-and-inducement-gate/SKILL.md`).
- No unlicensed adjusting or claim negotiation.
- Fall protection plan before any roof work.
- Written, compliant contract before work.
- Human sign-off before anything leaves the office.
- Clear VERIFY tags locally before a rule appears in a customer document.

## Agents (`agents/`)
- `roofing-operations-director.md` (lead): routing, gates, approval queue, weekly KPI view
- `sales-estimator.md`: inspection, measurement, estimates, proposals, contracts
- `insurance-claims-coordinator.md`: claim file, scope comparison, supplements, payment tracking
- `production-manager.md`: permits, materials, scheduling, crews, subcontractors
- `safety-officer.md`: fall protection, toolbox talks, incidents, training
- `quality-inspector.md`: staged QC, punch list, final walk-through
- `commercial-bid-manager.md`: commercial bids, moisture surveys, maintenance programs
- `service-warranty-coordinator.md`: warranty registration, service calls, emergency tarping
- `marketing-reputation-manager.md`: local marketing, reviews, compliant canvassing
- `finance-controller.md`: job costing, billing, lien waivers, margin review

## Skills (`skills/`)
lead-intake-triage, storm-surge-playbook, roof-inspection-protocol, damage-documentation-photo-log, aerial-measurement-verification, roof-takeoff-calculator, estimate-builder-tiered, proposal-writer, contract-compliance-check, deductible-and-inducement-gate, insurance-claim-support, scope-comparison-and-supplement, acv-rcv-depreciation-math, permit-and-code-check, material-order-builder, crew-scheduling-weather, subcontractor-vetting-and-payments, fall-protection-plan (includes toolbox talks), qc-checklists, punch-list-and-closeout, lien-waiver-tracker, warranty-registration-and-tracker, service-call-leak-triage, commercial-bid-response, roof-moisture-survey-planner, maintenance-program-builder, review-and-referral-compliance, job-costing-and-margin-review

## Templates (`templates/`)
inspection-report, photo-log, measurement-verification-sheet, takeoff-sheet, estimate-good-better-best, proposal, residential-contract, change-order, claim-file-cover-sheet, supplement-request-letter, adjuster-meeting-checklist, acv-rcv-tracker, material-order, permit-packet-checklist, job-kickoff-checklist, crew-work-order, sub-agreement, sub-payment-milestone-sheet, toolbox-talk, fall-protection-plan, incident-report, qc-checklist, punch-list, completion-certificate, lien-waiver-tracker, warranty-registration-record, workmanship-warranty-certificate, service-ticket, tarp-authorization, commercial-bid-response, maintenance-inspection-report, annual-maintenance-agreement, review-request-message, canvass-script, job-cost-report, weekly-kpi-dashboard, storm-response-lead-log

## Workflows (`workflows/`)
01-lead-to-appointment, 02-inspection-to-estimate, 03-estimate-to-signed-contract, 04-insurance-claim-support, 05-permit-to-dryin-to-final, 06-material-order-to-delivery, 07-production-day-and-weather, 08-safety-program-routine, 09-closeout-to-final-payment, 10-warranty-and-service-call, 11-commercial-bid-to-award, 12-maintenance-program-cycle, 13-storm-surge-response, 14-monthly-job-costing-review

## Knowledge (`knowledge/`)
glossary.md, rules.md, schemas.md, research-notes.md (sources, confidence, conflicting figures, open gaps)

## Harnesses (`harnesses/`)
Stdlib Python 3 tools with self-tests: `takeoff_calc.py`, `claim_math.py`, `job_cost.py`. See `harnesses/README.md`. Run `python <file> --selftest` after any change.

## Handoffs to other departments
- Finance, bookkeeping, tax, entity and compliance filings: `../09-business-admin-finance-compliance/README.md`.
- Video and advertising production (before/after stories, storm education): `../07-ai-video-creative-production/README.md`, after the script passes the compliance gate here.
- Insurance rules and disclosure practices where relevant to claim-related messaging: `../05-insurance-medicare-marketing/README.md` (for ideas on consent and advertising practice only; roofing contractors do not sell insurance).
- Commercial estimating and QC overlap, general construction practices: `../01-construction/README.md`.
- AI response automation, CRM integrations, photo-labeling and measurement ingestion tools: `../08-ai-services-software/README.md`.

## Open gaps
Retention data, product-specific install specifications, state-specific statutes and current rate benchmarks are not in this department; use placeholders and local verification (`knowledge/research-notes.md`).
