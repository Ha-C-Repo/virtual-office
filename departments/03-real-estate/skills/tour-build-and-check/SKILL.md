---
name: tour-build-and-check
description: Build a graded virtual tour from listing assets and run the completeness check and publish gate.
---
# Tour Build and Completeness Check

## When to use
A listing needs a walkthrough tour or illustrative staging.

## Inputs
Listing intake, source-tagged assets, room graph from `../floorplan-reading/SKILL.md`.

## Steps
1. Assign grade: A measured, B reconstructed, C captured.
2. Harvest assets and tag each with its source.
3. Grade B only: infer layout; all dimensions LOW confidence.
4. Build model: room graph, coordinate model, 3D mesh. Computed area must reconcile to stated GLA.
5. Staging: generate imagery conditioned on real photos. Label "AI-generated, illustrative, not a survey or measurement."
6. Compose the tour: walkthrough, waypoints, hotspots, mini-map, fly-through video.
7. Completeness check: every room reachable, all labels present, grade shown, source list attached, no unfilled placeholders, broker identification correct for the surface.
8. Publish gate: owner sign-off.

## Outputs
Tour package in working folder, completeness report, publish decision.

## Gates
Incomplete or unreconciled tours do not publish. Output goes to a working folder first; the final folder is written only after sign-off.
