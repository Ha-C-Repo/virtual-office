---
name: scope-creep-detector
description: Classify every proposed task or feature as In-scope, Creep, or Boundary against the MVP lists and constitution.
---
# Scope Creep Detector

## When to use
When a new idea, task or change request arrives mid-spec or mid-build.

## Inputs
Request text, current product spec (MVP IN/OUT lists), constitution Tier 1 rules.

## Steps
1. Compare the request with MVP IN and OUT lists.
2. Label: In-scope (matches IN), Creep (not listed, or listed OUT), Boundary (touches a Tier 1 rule such as privacy, integrity, verification).
3. For Creep: state cost and what it displaces; park it in the open-question log.
4. For Boundary: stop and escalate to the owner.

## Outputs
Labeled request list with reasons.

## Gates
Creep does not start without owner approval. Boundary never starts without a constitution decision.
