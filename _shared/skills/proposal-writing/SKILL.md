---
name: proposal-writing
description: Builds proposals, quotes and scope letters as a client version plus an internal margin version. Locked section order, inclusions and exclusions, assumptions, validity, payment schedule. Use for any priced offer to a client.
---

# Proposal writing

## When to use
Any document that offers work, a product or a service at a price.

## Inputs
Scope notes, verified quantities, priced lines from the approved rate source, risk and contingency notes, payment terms, validity period, template `../../templates/proposal.md`.

## Steps
1. Confirm scope in writing: what is in, what is out, what is assumed. Unknown scope is a clarification question, not an assumption.
2. Pull prices only from the approved rate source or owner-approved input. The model does not set rates. Run arithmetic in a calculator and cross-check by a second path.
3. Apply the stated markup or contingency rules from the internal rate file, in the internal version only.
4. Write the client version in the locked section order: header, summary of the offer, scope, inclusions, exclusions, assumptions, pricing table, payment schedule, schedule or timeline, validity, acceptance block.
5. Write the internal version (`-INT`): cost basis, margin, contingency, risks, comparable offers, confidence tags, open flags, approver line.
6. Leak scan the client version: no supplier names, internal costs, margins, headcount, internal rationale.
7. Four-pass review, then human sign-off. Send only the client version as the approved format.
8. Schedule a follow-up (see `../scheduling-and-routines/SKILL.md`) and log in the correspondence register.

## Outputs
Client proposal, internal twin, follow-up date.

## Gates
- Verify, do not generate: prices, quantities and dates have sources.
- Two independent calculation paths must agree within the stated tolerance.
- Payment schedule is validated against cash flow in the internal version.
- Never fabricate references, certifications or past results.
- Pricing exposure above the owner's threshold goes to WAIT.

## Anti-patterns
Burying exclusions. Footnoting a failed cross-check. Using a past proposal's numbers.
