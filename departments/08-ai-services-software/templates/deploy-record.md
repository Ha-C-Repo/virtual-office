---
type: deploy-record
date: {{DATE}}
environment: staging | beta | production
spec: {{SPEC_REF}}
---
# Deploy Record: {{CHANGE_NAME}}

## Answer
One paragraph: what shipped, current state (live, staged inert, rolled back).

## What changed
| Component | Change | Flag (default) |
|---|---|---|

## How it was verified
Specific checks and results, with dates. Production verification: {{VERIFICATION_RESULT}}

## Rollback
Exact steps and the expected time to complete.

## Approvals
- Technical owner: {{APPROVAL_DATE}}
- Principal (if customer-visible): {{APPROVAL_DATE}}

## What remains
