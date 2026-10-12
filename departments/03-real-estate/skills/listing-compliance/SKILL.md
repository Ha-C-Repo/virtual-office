---
name: listing-compliance
description: Scan client documents, captions, ads and scripts against the immutable Tier 1 rules (fair housing, MLS terms, disclosure, AI labeling). Fails closed.
---
# Listing Compliance

## When to use
Before any client document, caption, flyer, ad, tour text or video script moves to the approval queue.

## Inputs
The text or document; the surface it will appear on (MLS, social, print, web, video); `../../knowledge/rules.md`; `../../templates/fair-housing-rewrite-table.md`.

## Steps
1. Fair housing: scan for protected-class references, steering language, and descriptions of who a home or area is "perfect for". Replace with facts about the property.
2. Facts: every feature claim traces to a source document; remove unsourced claims.
3. Disclosure: required broker identification present on ads; absent from the MLS tour field.
4. AI labeling: generated imagery or staging labeled "AI-generated, illustrative, not a survey or measurement."
5. Commission secrecy: no commission, fee or split in any public or client text.
6. Guarantees: no promise of price, speed of sale or appreciation.
7. Write the gate report.

## Outputs
Report: line, rule, pass/fail, suggested compliant alternative (advisory). Blocked items are logged to the refusal ledger and never queued.

## Gates
The rewrite table is advisory, not exhaustive. A human decides ambiguous cases. Any Tier 1 hit is a refusal, not a warning.
