---
name: character-bible
description: Seven-step workflow to keep characters and locations visually consistent across every illustration in a title or series.
---
# Character Bible

## When to use
Before any scene illustration. Also when adding a character to an existing series.

## Inputs
Concept record, manuscript, style direction, IP blocklist.

## Steps
1. **IP screen first.** Compare the proposed character to protected characters; reject lookalikes. Log result.
2. **Text bible.** Complete `../../templates/character-bible.md`: name, age, hair, skin tone, eye color, face shape, distinctive features, signature outfit (items and colors), personality-to-expression mapping, art-style label.
3. **Model sheet.** Generate front, three-quarter, profile, three-quarter back, back, and an expression grid on a plain background. Perfect them before scenes.
4. **Style lock.** Choose one style family and a palette of 5 to 7 colors. Record it.
5. **Location bible.** Complete `../../templates/location-bible.md` for each recurring place: fixed features, palette, props, camera notes.
6. **Scene generation.** Attach canonical anchors (model sheet, location reference) on every call. Multi-character scenes use a three-clause prompt: identities, positions, actions.
7. **Repair, do not regenerate.** Inpaint drift. Then flip-through QC.

## Outputs
Approved character and location bibles, model sheets, style lock record.

## Gates
- Never chain output N into output N+1 as the reference.
- The bible is the sole source of character truth. Manuscript and prompts follow it.
- A human approves model sheets before scene work (logged).
