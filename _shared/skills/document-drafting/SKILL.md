---
name: document-drafting
description: Drafts letters, memos, policies, SOPs, notices, summaries and agreements-in-plain-language from a template and verified facts, with an internal twin and review chain. Use for any written document that is not a proposal, report or marketing piece.
---

# Document drafting

## When to use
Letters, internal memos, decision memos, SOPs, policy skeletons, notices, plain-language summaries of contracts, instruction files, FAQs.

## Inputs
Purpose, audience, band, source documents, template from `../../templates/`, voice profile, department rules.

## Steps
1. Thinking protocol: goal, audience, band, sources, gates.
2. Choose the template. Copy it; never edit the master in place.
3. Fill every field from a source. Mark gaps as `NEEDS_INPUT: <what, from whom>`.
4. Put the answer first. Then support. Keep to the audience's reading level.
5. Number the document `{{DOC_NUMBER}}` with the department's convention; revisions increment the sequence.
6. Create the internal twin (`-INT`) with sources, confidence and open flags.
7. Run voice firewall, QA editor, compliance reviewer as the band requires.
8. Anonymization pass on any reusable copy.
9. Human sign-off for outward documents. Export to the final format.
10. File with a changelog line. Do not overwrite earlier versions.

## Outputs
Final document, internal twin, gate results, version record.

## Gates
- Legal text: draft only; mark "draft for counsel review" and never present as legal advice. Counsel flag for indemnity, termination, regulatory, insurance and liability clauses.
- Formal notices are draft-only; the human sends.
- Unfilled placeholders block outward release.

## Anti-patterns
Starting from a blank page when a template exists. Copying clauses from a prior client. Silent edits to an approved version.
