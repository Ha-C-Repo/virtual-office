---
name: two-pdf-pair-check
description: Enforce that every listing document ships as a client PDF plus an internal twin, and that the pair agrees.
---
# Two-PDF Pair Check

## When to use
At export of any listing presentation or CMA.

## Inputs
Client PDF, internal twin (file name ends with `-INT`), source data.

## Steps
1. Confirm both files exist with matching base names and version.
2. Confirm the client file contains no internal-only content (see `../client-doc-scrubber/SKILL.md`).
3. Confirm the internal twin contains the net sheet, strategy and confidence tags.
4. Compare the prices, GLA, comps and dates between the two; they must match exactly.
5. Confirm section order for presentations matches the locked order in `../../templates/listing-presentation-client.md`.
6. Record the result with exit code: 0 clean, 1 blocked, 2 usage error.

## Outputs
Pair report. Hash both files and log in the document log.

## Gates
Missing twin, mismatch or internal leak blocks export. Owner sign-off required before delivery.
