---
name: generative-platform-automation
description: Drive a node-based generative video platform through the browser: reference images, clip nodes, mode toggles, run order, stitch, text-to-speech and audio.
---
# Generative Platform Automation

## When to use
When a production uses a browser-based node-graph generative video platform.

## Pipeline (full)
1. Create or open the project canvas. Record project metadata in the session resume file.
2. Upload reference images (one per subject).
3. Create image nodes, then clip nodes. Wire each clip node to its prompt and first-frame input.
4. **Mode check:** verify the unlimited (or credit) mode toggle on every node. This is a standing rule; do not assume.
5. Confirm the cost-gate go (`../cost-gate/SKILL.md`).
6. Run nodes in the stated order. Never "run all" on a canvas with cached results.
7. Wait using timing memory (`../timing-memory-and-persistence/SKILL.md`).
8. Download or stitch clips, add text-to-speech and audio nodes, assemble.
9. Update the build-progress table and edge ledger in `../../templates/session-resume.md`.

## Helpers
Small scripts: find node by type, get handle coordinates, inspect canvas, run node, wire handles.

## Failure handling
- On an error, log node, error text and time. Retry once. On a second failure, trip the circuit breaker and ask a human.
- If the page layout changed, stop and re-inspect rather than guessing coordinates.

## Gates
Never exceed the approved batch. Never read or paste credentials. Human reviews all output before use.
