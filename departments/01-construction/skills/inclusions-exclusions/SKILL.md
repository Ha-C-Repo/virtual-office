---
name: inclusions-exclusions
description: Writes client-facing inclusion and exclusion sentences from the requirement register, enforcing mandatory inclusions and the standard exclusions list.
---
## When to use
When composing the proposal or letter of offer.

## Inputs
Requirement register, always-in-scope list, never-in-scope list, standard exclusions list, scope (fab only, fab and erection, full package).

## Steps
1. Draft one sentence per inclusion, linked via derived_from_req_ids.
2. Enforce mandatory inclusions (for example deck in scope by default).
3. Apply the standard exclusions and any out-of-scope by company position.
4. Convert each unpriced requirement into an explicit exclusion or a clarification.
5. Strip internal language, supplier names and rationale.

## Outputs
Inclusion and exclusion lists for `../../templates/client-proposal.md`.

## Gates
Every tender requirement is priced or explicitly excluded. Reconciliation checks it.
