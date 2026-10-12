---
name: build-phase-test-plan
description: Write and track test plans for engineering, design and production validation builds (EVT, DVT, PVT).
---
# Build Phase Test Plan

## When to use
Planning each build phase and reviewing results at the gate.

## Inputs
Requirements list, design locks, `../../templates/test-plan.md`, prior findings.

## Steps
1. Link each requirement to one or more tests. A requirement with no test is a gap.
2. For each test: id, method, equipment, sample size, pass criterion, owner.
3. EVT focus: does the design work. DVT focus: does it meet requirements across conditions and sample units. PVT focus: can the factory build it repeatedly at rate and quality. (General practice; adapt to the product.)
4. Record results with date, unit serial role, hardware revision and firmware version.
5. Failures become findings with owner and re-test plan.
6. Summarize pass rate, open findings and risks for the gate.

## Outputs
Test matrix, result log, gate summary.

## Gates
`../../workflows/build-phase-gate.md`. Principal approves moving to the next phase.
