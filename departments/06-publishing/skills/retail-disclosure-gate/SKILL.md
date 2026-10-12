---
name: retail-disclosure-gate
description: Decide and record AI disclosure at every publish or republish: AI-generated versus AI-assisted, decision tree, tripwires.
---
# Retail Disclosure Gate

## When to use
Pipeline step 13 and every time a title is published, republished or materially edited. Also for video platform toggles (see `../../../07-ai-video-creative-production/skills/kids-platform-compliance/SKILL.md`).

## Definitions (confirm against the current platform wording and log the source)
- **AI-generated:** the AI produced the content (text, image, translation, narration) and the human did not create it, even if the human then edited it.
- **AI-assisted:** the human created the content and used AI to edit, refine, brainstorm or fix it.

## Decision tree (per component: text, illustration, cover, narration, music, translation)
1. Who produced the first expression of this component? If the AI did, it is AI-generated.
2. If the human produced it and AI only polished, it is AI-assisted.
3. If unsure, treat as AI-generated and escalate.
4. Fill the platform's questionnaire from these answers. Do not describe AI-generated work as assisted.

## Steps
1. Fill `../../templates/ai-disclosure-record.md` for the title.
2. Answer the retailer questionnaire consistently with the record.
3. Add a row to the root AI disclosure register (see `../../knowledge/schemas.md`).
4. Check tripwires: policies that bar AI content from certain distribution channels or audiobook channels; route private editions versus public listings accordingly.
5. Re-run at every republish.

## Gates
- Human sign-off before any answer is submitted.
- Policy facts need a logged source and date. Unverified means open list.
