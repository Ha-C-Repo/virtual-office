---
name: shop-traveler-gates
description: Enforces the three-gate shop QC sequence: receiving, fabrication traveler with hard blocks, and release with zero open NCRs.
---
## When to use
Whenever material is received, a traveler step is signed, an NCR is raised, or a piece is released.

## Inputs
Bill of lading, material test reports, specified minimums, traveler record, NCR list.

## Steps
1. Receiving: record actual yield, tensile and carbon equivalent against specified minimums. Warn on shortfall; do not block. Assign piece IDs and label payload (piece, project, heat, received date).
2. Fabrication: the traveler has 18 fields in a locked sequence (see `../../templates/shop-traveler.md`). Only the lowest unsigned step can be signed. Pre-weld inspection is a hard block.
3. Open NCR freezes the traveler. Close only with disposition and authority. Unauthorized field modification needs an engineer-of-record reference.
4. Release: all required fields signed, zero open NCRs re-verified at sign time, co-sign if tonnage or special inspection requires it.
5. Produce release certificate and piece manifest.

## Outputs
Signed records, NCRs, release certificate, manifest, audit log lines.

## Gates
No back-dated or proxy signatures. Audit log is append-only.
