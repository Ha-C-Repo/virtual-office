# 10 Shop QC Three-Gate Fabrication

Owner: shop-qc-inspector. Sign-offs: shop director, welding inspector, executive co-sign where required.

## Gate 1: Receiving
1. Import bill of lading lines.
2. Verify test reports against the physical checklist (`../templates/receiving-inspection-report.md`).
3. Record actual yield, tensile and carbon equivalent against specified minimums. Shortfall: warn and record, do not block.
4. Assign piece IDs. Print labels with piece, project, heat and received date.

## Gate 2: Fabrication
5. Open the traveler (`../templates/shop-traveler.md`, 18 fields; joist variant). Sequence is locked: only the lowest unsigned step is signable.
6. Pre-weld inspection is a HARD BLOCK. Record welder and procedure.
7. Post-weld visual, nondestructive testing, dimensional, camber and coating checks.
8. Fastener lot records and weld records maintained.

## Gate 3: Release
9. All required fields signed. Zero open NCRs, re-verified at sign time.
10. Executive co-sign for large tonnage or special-inspection projects.
11. Release certificate (`../templates/release-certificate.md`), manifest, load reference.

## NCR handling
An open NCR freezes the traveler (`../templates/ncr.md`). Unauthorized field modification NCRs need an engineer-of-record reference to close.

## Data
Sync to the shared backend with an append-only audit log. Nightly backups go to cloud storage only, never a copy of the live multi-station database.
