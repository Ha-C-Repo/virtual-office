---
name: thinking-protocol
description: Short pre-draft reasoning routine for deliverables, routing decisions and external communications. Use before drafting anything non-trivial.
---

# Thinking protocol

## When to use
Before any deliverable, any routing decision, and any message to an outside party. Skip for one-line lookups.

## Inputs
The request, the audience, the band, the sources on file.

## Steps
1. Goal. What decision or action must the reader take? One sentence.
2. Audience. Internal, buyer or client, investor, regulator, counsel. This decides voice, content and which facts may appear.
3. Band. Which of AUTO / DRAFT / BRIEF / WAIT applies? When in doubt, go up.
4. Sources. List the documents and registers the facts will come from. Missing source means a flagged gap, not an assumption.
5. Risks. What could go wrong if this is wrong or leaks? Money, compliance, safety, reputation.
6. Gates. Which gates must pass (QA, compliance, scrub, sign-off)?
7. Shape. Answer first, then support. Choose the template.
8. Pre-mortem for structural changes (schema, folder layout, new skill, new integration): the textbook approach; how it fails six months later; the smaller approach using existing parts; the one judgment call that decides it. Use `../../templates/pre-mortem.md`.

## Outputs
A five-line plan kept in working notes: goal, audience, band, sources, gates. Not shown to the audience unless asked.

## Gates
If steps 4 or 6 cannot be completed, stop and ask one question.

## Anti-patterns
Starting to write before the sources are listed. Writing for the wrong audience. Skipping the pre-mortem for a structural change.
