---
name: illustration-prompts
description: Write one illustration prompt per spread with typed references, final dimensions and bleed, then run variation selection and flip-through QC.
---
# Illustration Prompts

## When to use
Pipeline steps 7 to 9, after model sheets are approved.

## Inputs
Spread map, character and location bibles, style lock, final trim and bleed dimensions from `../layout-and-print-spec/SKILL.md`.

## Prompt formula
1. Style label and palette (from style lock).
2. Subject(s) by bible name and reference image type (character reference, location reference).
3. Composition: shot type, camera height, where empty space sits for the text layer.
4. Action and expression, tied to the spread text.
5. Lighting and time of day, matching the location bible.
6. Output size including bleed and aspect ratio.
7. Exclusions: no text in image, no extra fingers or limbs, no style drift.

## Steps
1. Write one prompt per spread into numbered working file 05.
2. Generate 4 to 8 variations per beat.
3. Select the best; note why in one line.
4. If a mostly right image has drift (clothing, face, hand), inpaint the region. Do not re-roll.
5. Flip-through QC across all spreads in order: continuity of outfit and setting, expression matches text, resolution meets spec, uniform aspect ratio. Record in file 07.

## Gates
- Flip-through QC is blocking with human sign-off.
- Text is typeset as a layer, never rendered in the image.
- Record AI role per image in the production log.
