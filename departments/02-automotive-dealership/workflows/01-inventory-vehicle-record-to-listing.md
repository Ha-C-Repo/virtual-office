# 01 Inventory: Vehicle Record to Listing (nine stages)

Owner: Inventory agent (`../agents/01-inventory-agent.md`). Allowed sources only: own dealer system, public VIN decode, purchased auction run list and condition report, title and odometer documents in hand, lot photos, own paid history-report account. Skills: `../skills/inventory-vehicle-record-intake/SKILL.md`, `inventory-document-classifier`, `inventory-condition-report-reading`, `inventory-condition-grading`, `inventory-pricing-appraisal`, `inventory-photo-standard`, `inventory-listing-completeness-check`.

1. **Unit intake.** Unique stock number. VIN decode fills year, make, model, trim as HIGH. A failed decode is a recorded gap, not a guess. Open `../templates/inventory-unit-record.md`.
2. **Document harvest.** Classify every document by type and confidence from the closed allowlist. Hearsay is never upgraded to an inspection.
3. **VIN resolve.** Reconcile decode vs documents vs photos. Mismatch is a gate failure; stop and ask.
4. **Condition audit.** Rank defects by category and severity, cross-check recalls, produce the disclosure set (`../templates/inventory-disclosure-set.md`) and recon work order (`../templates/inventory-recon-work-order.md`) in one pass. Assign grade from evidence on file: A Inspected, B Declared, C As-Is Unverified. Never copy the report's own summary grade. Open recon downgrades an otherwise-A unit.
5. **Pricing.** Comp grid with three or more sourced comps (`../templates/inventory-comp-grid.md`). Calculator only. The owner sets the price.
6. **Merchandise.** Listing copy from the structured record only. Every sentence traces to a tagged fact. Adjectives limited by grade.
7. **Photo QC.** `../templates/inventory-photo-manifest.md`. Eight photos minimum, a photo per defect, nothing generated.
8. **Syndicate.** Push to site, social catalog and portal feeds only after recon-closed gate (`05-service-recon-and-we-owe.md`). Reconcile live vs ground and record each channel.
9. **Output gate.** Blocked unless: VIN reconciles, title status stated, odometer stated with source, defects in copy and photographed, buyer's guide consistent, no banned phrase, financing figures carry the disclosure block, no generated imagery, no superlative. Then follow `00-unit-to-listing-gate-order.md`.

## Human sign-off
{{OWNER}} on price and on go-live of the listing. Escalate: VIN will not reconcile; defect found after front-line; unit live but not on the ground (pull from all channels).

## KPIs
Days-to-turn, aged count, first-pass gate rate, drift between live channels and the ground.
