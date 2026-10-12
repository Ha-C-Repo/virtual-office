---
name: anti-ai-look-laws
description: Sixteen laws applied to every image and video prompt to avoid the generic AI look and common artifacts.
---
# Anti-AI Look Laws (16)

## When to use
Every prompt, every production. Also in the pre-generation QA checklist.

## The laws
1. One locked style system per production: color, grade, grain, lens language.
2. Use image-to-video for any shot with a person. House rule: text-to-video for faces is not used unless {{OWNER}} approves an exception and the frame review passes.
3. One reference per subject; the same reference every time.
4. Never chain output N as the reference for output N+1.
5. Describe what the camera sees, not adjectives of quality ("stunning", "epic", "cinematic masterpiece").
6. Specify a real lens and camera height; keep them consistent across a sequence.
7. Motion is slow and motivated: one camera move per shot, one subject action per shot.
8. Avoid hands doing detailed tasks, close-up teeth, crowds in focus, reading text in frame.
9. No generated text or logos inside footage; add type in post as a layer.
10. Natural imperfection: asymmetry, uneven light, real surfaces. No plastic skin, no glow on everything.
11. Lighting direction and time of day stay fixed within a scene.
12. Keep clips short and cut on action; do not stretch a clip past what the model holds well.
13. No morphing transitions, no warped background geometry; reject and regenerate those clips.
14. Backgrounds must obey real geometry (perspective, scale, structural logic) for the industry shown.
15. Color grade and sound mix applied uniformly in assembly to unify clips.
16. A human reviews every frame; artifacts found are repaired or cut, not excused.

## Steps
1. Check each prompt against the laws before submission.
2. Record violations and fixes in `../../templates/pre-generation-qa.md`.

## Gates
A prompt with an unresolved law violation does not run.
