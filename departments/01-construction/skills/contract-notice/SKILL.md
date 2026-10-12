---
name: contract-notice
description: Drafts contractual notices for delay, changed condition, constructive change or variation, citing the clause and notice period from the obligations register. Draft only.
---
## When to use
When a correspondence-register tag or a project-controls variance indicates a notice candidate.

## Inputs
Event description and date, obligations register, correspondence register.

## Steps
1. Identify the event type: delay, changed condition, constructive change, variation.
2. Pull the notice clause and period from the obligations register. If either is unknown, mark NEEDS_INPUT and stop.
3. Compute the last day to give notice and flag it on the calendar.
4. Fill `../../templates/contract-notice.md` with facts only: dates, what happened, who caused it, impact days, cost impact if known.
5. Attach references to evidence (diary entries, emails).

## Outputs
Draft notice and deadline entry.

## Gates
DRAFT ONLY. The {{APPROVER_ROLE}} sends and the send is logged. Do not characterize fault beyond facts. Counsel reviews anything that may become a claim.
