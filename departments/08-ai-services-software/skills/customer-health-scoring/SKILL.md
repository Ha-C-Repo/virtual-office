---
name: customer-health-scoring
description: Signal-weighted weekly health score per customer with green, yellow, red routing.
---
# Customer Health Scoring

## When to use
Weekly, and before every renewal or QBR.

## Signal categories (weights set in {{HEALTH_WEIGHTS}})
- Product usage (logins, key actions, modules in use)
- Engagement (replies, meeting attendance, support tone)
- Business health (payment status, headcount change, news)
- Relationship (champion present, executive contact, NPS/CSAT)

## Steps
1. Pull the signals for each customer; mark missing data as missing, not zero.
2. Compute the weighted score and the delta from last week.
3. Apply trigger flags (usage drop, failed payment, champion left, angry ticket).
4. Band: green (healthy), yellow (watch, assign an action), red (churn-save workflow).
5. Write the weekly list: customer, band, delta, top reason, next action, owner.
6. Recalibrate the model quarterly against actual renewals and churn.

## Outputs
Weekly health report; red accounts routed to `../../workflows/churn-save.md`.
