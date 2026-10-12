---
name: fi-client-doc-scrubber
description: Final scrub of client documents. Strips internal money, verifies AI-image labels and catches unfilled placeholders. Confirms the -INT twin exists.
---
## Scan for
- Internal economics: cost, pack, recon spend, floorplan interest, reserve, front or back gross, lender names where policy forbids.
- Unfilled placeholder tokens (the registered token list has one home).
- Em-dashes, emojis, banned phrases.
- Staff or vendor names (role only; owner as single contact and signatory).
- AI-image labels present where an image was touched; any generated vehicle, building or person.
- Buyer's guide consistency with the contract.

## Steps
1. Scan, list hits with location.
2. Block on hit. Do not auto-fix silently.
3. Confirm the pair: client PDF and `-INT` PDF (`<stock>_<type>_v<NN>.pdf` and `...-INT.pdf`).
4. PDF only for external deliverables.

## Outputs
PASS or blocking hit list.

## Gates
Exit code contract applies: 0 clean, 1 blocked, 2 usage or input error (not a pass).
