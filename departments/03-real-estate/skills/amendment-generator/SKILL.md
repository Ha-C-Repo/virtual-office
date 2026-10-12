---
name: amendment-generator
description: Draft price, repair and extension amendments and repair-request packages from approved terms.
---
# Amendment Generator

## When to use
A client or counterpart asks to change price, repairs, closing date or other terms of an executed contract.

## Inputs
Executed contract, the requested change in the principal's words, inspection report items (for repairs), jurisdiction form set {{STATE_FORMS}}.

## Steps
1. Restate the change and confirm the numbers with the principal.
2. Pick the correct form or addendum type for {{STATE_RULES}}.
3. Fill the form from the contract; compute any dollar or day changes with a script.
4. For repairs: list each item from the inspection report with location, issue, requested remedy and source page. Do not add items not in the report.
5. Produce the package using `../../templates/amendment-and-repair-request.md`.
6. Update the timeline if dates move.

## Outputs
Draft amendment or repair request package and a change summary for the principal.

## Gates
Money-risk item: never bulk approved. Principal reviews and approves before anything is sent. No legal advice; contract interpretation goes to the principal or an attorney.
