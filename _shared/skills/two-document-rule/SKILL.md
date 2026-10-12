---
name: two-document-rule
description: Every outward deliverable ships with an internal twin (suffix -INT) that carries economics, compliance findings and verification status. The outward piece never carries internal data. Use whenever a document, quote, listing, report or message will leave the office.
---

# Two-document rule

## When to use
Any deliverable going to a client, buyer, investor, regulator, partner or the public.

## The pair
- Outward document: only what the audience may see. Numbered `{{DOC_NUMBER}}`.
- Internal twin: same number with `-INT`. Holds costs, margins, commission or fee data, internal notes, gate results, confidence tags, sources, open flags, and the approver line.

## Steps
1. Create the twin first or together with the outward piece, using `../../templates/internal-twin-memo.md`.
2. Draft the outward piece from verified facts only.
3. Run the leak scan on the outward piece against the forbidden-items list: supplier names, internal costs, margins, commission schedules, headcount, personal data, credentials, internal rationale, superseded terms.
4. Confirm both files exist and carry the same version.
5. Export outward documents in the approved final format only (PDF for anything leaving, unless the department says otherwise).
6. Send only the outward piece. The twin stays internal.

## Outputs
A matched pair, a leak-scan result, a pair-check line in the twin.

## Gates
A missing twin is a defect and blocks release. A leak in the outward piece is a BLOCK. A template that passed once does not pre-clear a filled copy.

## Anti-patterns
Putting margins in a comment or hidden field. Reusing the internal file as the outward file after deleting rows. Attaching the wrong file.
