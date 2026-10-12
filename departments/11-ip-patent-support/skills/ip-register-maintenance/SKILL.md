---
name: ip-register-maintenance
description: Keep the IP register complete, sourced and current. One row per asset, one source per fact.
---
# IP Register Maintenance

## When to use
A filing, grant, abandonment, assignment, license, new mark, new domain-neutral asset, or counsel update arrives. Also on the review cadence.

## Inputs
New document (receipt, certificate, counsel email), the current register (`../../templates/ip-register.md`), schema `IP register` in `../../knowledge/schemas.md`.

## Steps
1. Identify the asset. Match to an existing row by title or reference; create a row only if none matches.
2. Update only the fields the document supports. Cite the document in `source_doc`.
3. Copy any stated deadline into `next_deadline` and `deadline_type` exactly as written; add the date you recorded it.
4. Check `owner_entity` against the assignment record. Mismatch goes to `../assignment-gap-check/SKILL.md`.
5. Re-sort by `next_deadline`. Flag rows with no deadline and no "none" note.

## Outputs
Updated register and a change list (row, field, old, new, source).

## Gates
Counsel confirms any status the register shows as pending, granted or registered before it is used in an investor or partner statement.
