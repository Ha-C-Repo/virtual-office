# 02 Inspection to Estimate

Owner: sales-estimator | Approver: {{OWNER}}

## Steps
1. Decide access method and review weather and safety (`../skills/roof-inspection-protocol/SKILL.md`). No wet, icy or unsafe roof walking.
2. Inspect and photograph; fill `../templates/inspection-report.md` and `../templates/photo-log.md` (`../skills/damage-documentation-photo-log/SKILL.md`).
3. Order or prepare the measurement. Verify it (`../skills/aerial-measurement-verification/SKILL.md`, `../templates/measurement-verification-sheet.md`).
4. GATE: complex roofs get an on-site check; variance above {{VARIANCE_TOLERANCE}} stops the takeoff.
5. Run the takeoff with the harness (`../skills/roof-takeoff-calculator/SKILL.md`, `../templates/takeoff-sheet.md`).
6. Build the tiered estimate (`../skills/estimate-builder-tiered/SKILL.md`, `../templates/estimate-good-better-best.md`). Margin check with `../harnesses/job_cost.py`.
7. GATE (human): owner reviews estimates above {{ESTIMATE_APPROVAL_THRESHOLD}} or below {{MIN_MARGIN}}.
8. Write the proposal (`../skills/proposal-writer/SKILL.md`, `../templates/proposal.md`). Send within {{ESTIMATE_TURNAROUND}}.
9. Follow up on a set cadence. Insured jobs: confirm the homeowner has filed or decided to file; hand to `04-insurance-claim-support.md`.
10. Record `days_to_estimate`.

## Outputs
Inspection report, photo log, verified measurement, takeoff, estimate, proposal.
