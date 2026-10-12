---
name: environment-detection
description: Detect available hardware and tools at session start and choose hybrid, local-only or cloud-only generation mode.
---
# Environment Detection

## When to use
First action of every production session.

## Steps
1. Run the environment-detection script. It checks GPU presence, video memory, free disk, available render and encoding tools, and the browser automation connection.
2. Compare video memory to two thresholds: a floor ({{VRAM_FLOOR}}) for any local generation and a target ({{VRAM_TARGET}}) for comfortable local use.
3. Choose mode: **hybrid** (generated B-roll plus programmatic local assembly) when at or above target; **local-only** when between floor and target and cloud is unavailable; **cloud-only** when below floor.
4. Write the result to a routing cache file read by later steps.
5. Report the mode and any missing tool to the producer.

## Gates
If a required tool is missing, stop and ask before proceeding. Never install software without approval.
