---
name: confidence-tagging
description: HIGH / MEDIUM / LOW confidence tags on every extracted fact and check, with source-order rules. LOW is routed to a human. Use on every extraction, valuation, reconciliation and review.
---

# Confidence tagging

## When to use
Whenever a fact is extracted from a document, measured, matched, or inferred.

## Tag definitions
- HIGH: stated by a controlling primary document or measured by a deterministic tool and confirmed (for example an executed contract date, a title, a calculator result from sourced inputs).
- MEDIUM: from a credible secondary document or a single-source reading (for example a third-party report, a machine transcript, a fuzzy match).
- LOW: seller or client statement without documents, photo inference, scaled estimate, anything fetched from the open web, anything a human edited after machine extraction without re-check.

## Steps
1. Rank the sources for the domain (see the department rules file for the source order).
2. Tag each fact at extraction time with the tag, the source and the date.
3. Force LOW when: the model flags uncertainty; a verifier returned unverifiable; a human edited the extraction; evidence conflicts.
4. Route LOW items to a human check with the specific question. Do not pass them silently.
5. Carry the lowest tag upward: a deliverable is only as confident as its weakest controlling input.

## Outputs
Tags on fields; a LOW list for the human; the deliverable's overall confidence.

## Gates
Misclassifying hearsay as an inspection is forbidden. A LOW item may not set a price, a quantity, a valuation, a status or a regulatory claim.

## Anti-patterns
Tagging everything HIGH. Dropping tags at the summary stage. Averaging tags.
