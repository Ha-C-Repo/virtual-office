---
name: safety-questionnaire-responder
description: Drafts answers to contractor-qualification safety questionnaires from the company's written safety programs, flagging gaps instead of inventing policy.
---
## When to use
When a client or qualification platform sends a safety questionnaire.

## Inputs
Questionnaire items, written safety programs, master safety manual.

## Steps
1. Parse items.
2. Identify the written program each item references.
3. Required program set to check: fall protection, hot work, personal protective equipment, hazard communication, emergency action, lockout/tagout, electrical safety, scaffolding, ladders, rigging, powered industrial trucks, aerial lifts, respiratory, noise, first aid, incident reporting, crane operations, chemical safety.
4. Extract the policy text. If a standalone program is absent, fall back to the master manual and note it.
5. Answer: direct statement, program and section reference, procedures, responsible role, training frequency, confidence (HIGH, MEDIUM, LOW).
6. Injury rates come from the calculator (recordable and days-away) and the annual summary posting.
7. List FLAGged gaps for the safety coordinator.

## Outputs
Draft answers, gap list.

## Gates
Never invent policy. The {{APPROVER_ROLE}} reviews and submits.
