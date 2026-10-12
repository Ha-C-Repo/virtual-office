---
name: human-signoff-gate
description: The mandatory human approval point before anything leaves the office or commits money, law or safety. Defines what the approver sees, what counts as approval, and how it is logged. Use for every BRIEF-band deliverable.
---

# Human sign-off gate

## When to use
Before any outward email, document, post, reply, quote, filing, notice, payment instruction, publication, or release. Before any irreversible internal action (deletion, schema change, production change).

## Inputs
The deliverable, its internal twin, gate results (QA, compliance, scrub), open flags, the approver role.

## Steps
1. Assemble the approval package with `../../templates/approval-request.md`: what it is, who receives it, what it commits, headline number, confidence tier, gate results, open flags, recommended action.
2. Present the package to the named approver role ({{OWNER_ROLE}} or the role the department charter names). Money items are approved individually, never in bulk. Low-risk internal items may be batched.
3. Approval must be explicit and tied to a specific version (document number and revision).
4. Log the decision: date, approver role, version, decision (approve, approve with changes, reject), note. Use the decision log.
5. After approval, lock the version. Any edit voids the approval and returns to step 1.
6. Send or publish as a human-paced action. Record the permalink, message ID or filing reference in the register.

## Outputs
An approval record and, when approved, a release-ready file set.

## Gates
- No approval, no release. Silence is not approval.
- Drafts that failed a gate cannot be taken to approval; fix first.
- The approver may reject at any time; rejection is logged with the reason.
- AI never approves for the human, never auto-replies, auto-posts, auto-dials or auto-signs.
- Open owner decisions are escalated, not defaulted.

## Anti-patterns
Approval by "looks fine" without the twin. Approving a template instead of the filled copy. Bundling a money item inside a batch of routine items.
