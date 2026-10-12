# 01 End-to-End Bid Pipeline

Owner: estimator-takeoff (lead: construction-lead). Sign-off: {{APPROVER_ROLE}}.

1. **Intake gate.** Confirm drawing set, GC, deadline, drawing version and scale, drawing stage, scope (fab only, fab and erection, full package). If anything is missing, ask. Never assume. GATE: no takeoff until complete.
2. **Screen the building type** (conventional, tilt-up, pre-engineered, bearing wall). Decide the deck question; default is deck in scope.
3. **Pre-takeoff protocol** (`../skills/drawing-reading/SKILL.md`): list every structural sheet; rasterize and view plan sheets; read general notes first; scale from dimension lines; count members; only then price.
4. **Classify drawing stage** (`../skills/drawing-stage-classifier/SKILL.md`); apply stage adder and contingency from the locked table.
5. **Takeoff** (`../skills/takeoff/SKILL.md`): schedules first, plan counts as fallback, weights from the reference shape database only.
6. **Completeness check** (`../skills/takeoff-completeness-check/SKILL.md`). GATE: no MISSING item without RFI or exclusion.
7. **Price** (`../skills/bid-pricing/SKILL.md`) with locked rates; fold engineering into rates; small-project override if triggered; validate payment structure against cash flow.
8. **Sanity gates** (`../skills/bid-sanity-check/SKILL.md`): two paths agree, benchmark band, rate divergence, completeness, low-confidence area carried with contingency. GATE: over 10 percent divergence stops the bid.
9. **Generate RFIs** from gate flags (`../templates/rfi-form.md`); draft a verification email to the approver.
10. **Render two documents:** client proposal and internal margin report (`-GP`).
11. **Output scrub** (`../skills/bid-output-scrubber/SKILL.md`): forbidden-item scan, voice check, visual QC of every page.
12. **Pair check** (`../skills/two-document-pair-check/SKILL.md`).
13. **HUMAN SIGN-OFF:** {{APPROVER_ROLE}} reviews the pair and the pre-flight checklist (`../templates/pre-flight-checklist.md`).
14. **Send** (by the approver), log in the correspondence register, schedule follow-up (`../templates/bid-follow-up-email.md`).

Escalate: building type changes the scope; area confidence LOW with no RFI answer; Critical contract risk.
