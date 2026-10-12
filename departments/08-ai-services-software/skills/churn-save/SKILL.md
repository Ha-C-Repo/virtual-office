---
name: churn-save
description: Reason-coded, offer-matrix approach to saving a customer who signals cancellation.
---
# Churn Save

## When to use
Cancellation request, red health band, failed-payment pattern, or a negative reply.

## Steps
1. First touch within one business hour. Human tone, no discount in the first message.
2. Listen with open-ended questions. Capture the reason.
3. Assign a reason code (C1..Cn) from the rubric: price, missing feature, poor results, switching tool, business closed, bad support, other. Each code has a save-likelihood.
4. Pick from the offer matrix for that code (pause, downgrade, extended trial of a module, training session, roadmap commitment). Anything outside the matrix needs principal approval.
5. Track the economics: cost of offer versus remaining customer lifetime value.
6. If lost, run a clean exit: export data, confirm retention and deletion terms, ask permission for a short win/loss conversation.
7. Log everything in the customer config and the churn log.

## Outputs
Reason code, outcome, economics, lessons for product.
