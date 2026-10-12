---
name: ai-cost-telemetry
description: Log tokens and cost on every AI call and review spend weekly.
---
# AI Cost Telemetry

## When to use
Building or reviewing any feature that calls a language model; weekly cost review.

## Rules for code
- Model name comes from configuration, never hard-coded.
- Max tokens always set.
- Every call logs: timestamp, model, input tokens, output tokens, cached tokens, cost, feature, tenant id, department, latency.
- Use the cheapest adequate model for bulk work, a mid model for reasoning, the top model for novel problems.
- Long jobs run asynchronously (enqueue, then poll) to avoid gateway timeouts.

## Weekly review
1. Total cost and cost per tenant, per feature.
2. Outliers: calls with unusual token counts.
3. Cache hit rate.
4. Compare against the cost-per-revenue target {{AI_COST_TARGET}}.
5. Write a finding if a feature breaches target; propose model downgrade, caching or prompt trimming.

## Outputs
A short cost review record; list of changes proposed for owner approval.
