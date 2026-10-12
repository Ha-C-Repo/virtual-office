# Local Render and Hybrid Assembly

1. Read the detected mode (hybrid, local-only or cloud-only). If cloud-only, skip local generation and use the local engine only for assembly if it can run.
2. Convert the script JSON into composition files (`../skills/local-render-engine/SKILL.md`).
3. Import generated B-roll, voiceover, music and brand assets. Check each file exists and its rights status.
4. Add captions, lower thirds, logos (per brand tokens) and transitions.
5. Low-resolution preview render. Fix layout, timing and caption problems. Gate: producer approves the preview.
6. Final render at platform spec. Measure duration, resolution and loudness; log.
7. Play the full file once end to end to confirm it opens and syncs.
8. Hand to frame review.

Backup the composition files before each major change; version, never overwrite.
