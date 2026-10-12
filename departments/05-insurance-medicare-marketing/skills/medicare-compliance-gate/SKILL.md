---
name: medicare-compliance-gate
description: Judgment gate for every Medicare-touching artifact (flyer, mailer, event invite, script, web, social, email). Returns PASS, FIX-AND-RERUN or BLOCK plus a carrier routing note.
---
# Medicare compliance gate

## When to use
Any artifact that mentions Medicare, a plan, a benefit, an enrollment period, or targets Medicare-eligible people. Run it on every filled copy, even if the template already passed.

## Inputs
The artifact, its type (print, event, call script, email or mail, web or social), the plan year, and the service area. Rules come from `../../knowledge/rules.md`.

## Steps
1. Identify the artifact type and whether it is educational or plan-specific (marketing). Use the decision table in `../../knowledge/rules.md`.
2. Government-origin check: seals, eagle, card imagery, "official" framing, envelope teasers, "Medicare" in the sender, headline, URL or email suggesting origin, implied government endorsement.
3. Required disclaimer check: third-party marketing organization disclaimer, correct variant, with the real organization count and plan count for the service area. Unresolved placeholders mean BLOCK.
4. Claim check: no scare tactics; "free" is not used for a zero-dollar premium, cost-sharing reduction or subsidy; superlatives need current or prior-year substantiation with source; benefit, network and cost statements must not mislead; no carrier disparagement.
5. Timing check: no marketing of next plan year before October 1; concurrent-year pieces state which year.
6. Type-specific checks (print, event, call, email, web) from the rules file.
7. Carrier routing: plan-specific content must go through the carrier for federal material submission before use.
8. Tag each finding high, medium or low confidence. Low goes to {{PRINCIPAL_ROLE}}.

## Outputs
Verdict (PASS, FIX-AND-RERUN, BLOCK), failed checks with location, confidence tags, and a mandatory routing note recorded in the internal memo (`../../templates/internal-memo-int.md`).

## Gates
- A gate PASS never substitutes for carrier approval.
- Never pre-clear a filled copy because its template passed.
- Verify, do not generate: if a rule or date cannot be verified against the regulator, flag it and do not assume.
