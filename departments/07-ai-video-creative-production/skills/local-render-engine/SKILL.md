---
name: local-render-engine
description: Code-driven local video rendering from a storyboard JSON using composition data attributes, with sub-skills for captions, transitions, audio, layers, effects and export.
---
# Local Render Engine

## When to use
Programmatic assembly: titles, captions, layouts, charts, transitions, voiceover sync, and combining generated B-roll in hybrid mode.

## Inputs
Storyboard JSON (`../../templates/script-json.md`), generated assets, audio files, brand tokens, detected mode.

## Sub-skills (six areas)
1. **Composition:** scenes as markup with data attributes for start time, duration, layer and track.
2. **Captions:** timed text from the voiceover script; safe areas; contrast.
3. **Transitions:** limited set, consistent across the piece.
4. **Audio:** voiceover, music ducking, level targets, no clipping.
5. **Layers and effects:** lower thirds, logos per brand rules, subtle motion.
6. **Export:** codec, resolution, frame rate, aspect ratio per platform; verify by playing the file.

## Steps
1. Convert storyboard to composition files.
2. Preview a low-resolution render; fix layout problems.
3. Render final. Measure duration and loudness; record in the production log.
4. Hand to frame review.

## Gates
Render the final only after preview approval. Human reviews every frame of the final.
