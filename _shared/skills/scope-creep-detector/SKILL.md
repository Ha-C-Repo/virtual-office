---
name: scope-creep-detector
description: Scans inbound requests, emails and change notes for work outside the signed scope, classifies each as in scope, creep or boundary, and drafts a numbered change for the owner. Use on any client communication during delivery.
---

# Scope-creep detector

## When to use
Client emails, requests for information, meeting notes, change requests, specification updates, any message after scope is signed.

## Inputs
The signed scope or agreement, the always-out-of-scope list, the message.

## Trigger phrases (examples)
"can you also", "not in the drawings", "while you are at it", "client now wants", "additional work", "design change", "small tweak", "just one more", "quick revision".

## Steps
1. Quote the trigger text.
2. Classify: In scope / Creep / Boundary (needs a judgment) / Clarification (not a change).
3. If unclear, ask the client one question before pricing.
4. For Creep: estimate effort from verified rates; do not start work.
5. Draft a numbered change (amendment) with the template `../../templates/proposal.md` (change section): number, original contract reference, description, scope basis, hours and cost (internal twin only for margin), schedule effect, signature blocks.
6. Route to the owner. No work proceeds unsigned.
7. Log in the correspondence register and obligations register. If client-caused delay, flag a formal notice candidate.

## Status flow
draft, pending approval, submitted, approved or rejected.

## Outputs
Classification, change draft, register entries.

## Gates
Draft only; the human approves and sends. Items on the always-out-of-scope list always require a change.

## Anti-patterns
Absorbing creep to be nice. Pricing before confirming it is creep. Verbal approvals with no record.
