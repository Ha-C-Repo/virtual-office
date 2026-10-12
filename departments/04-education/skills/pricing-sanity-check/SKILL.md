---
name: pricing-sanity-check
description: Unit-economics gate: cost per problem, free exposure, paid margin, evaluated against heavy users.
---
# Pricing Sanity Check

## When to use
Before adopting or changing any tier, price, or free allowance.

## Inputs
Measured or owner-approved values, each with a named source: photo share, vision cost, explain cost, retry share, free users, free allowance, price, store fee share, usage per paying user, owner budget ceiling.

## Steps
1. Cost per problem = photo share x vision cost + explain cost x (1 + retry share). Use a script.
2. Free exposure = free users x allowance x cost per problem.
3. Paid margin = price x (1 - store fee share) - usage x cost per problem.
4. Evaluate against the tail (heavy users), not the mean.
5. Mark any unmeasured input UNMEASURED and carry it forward visibly.

## Outputs
Table of inputs, formulas, results, verdict.

## Gates
FAIL on negative margin. FAIL when free exposure exceeds the owner's budget ceiling. If the ceiling is unset the result is BLOCKED-ON-CEILING. Never invent an input.
