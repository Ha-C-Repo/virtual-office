---
name: comp-modeling
description: Internal-only earnings projection, recruiting economics, AEP production scenarios and override math, with VERIFIED or ESTIMATED tags on every number.
---
# Comp modeling

## When to use
Planning, recruiting economics, AEP production scenarios, override margin review. Internal only.

## Inputs
Comp grid rows, assumptions (production per agent, persistency, lead cost per vendor, target cost per issued policy), margin targets.

## Steps
1. List assumptions with owner and source. Anything not read from the comp grid or a statement is ESTIMATED.
2. Compute earnings projection per agent, recruiting economics (cost to onboard versus expected first-year and renewal commission), AEP production scenario (low, base, high), and override math.
3. Show arithmetic. Cross-check by a second independent path.
4. Tag each figure VERIFIED (read from a source of record, cited) or ESTIMATED.

## Outputs
Internal model with tags, and an `-INT` memo. Nothing from the model goes to an outward document.

## Gates
Number ownership: VERIFIED versus labeled ESTIMATED. Recruiting material uses qualitative income statements only. {{PRINCIPAL_ROLE}} reviews before the model is used for a decision.
