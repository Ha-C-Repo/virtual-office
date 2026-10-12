---
name: web-design-pipeline
description: Build a marketing web page from a master website prompt, design system and brand tokens, with accessibility and performance checks.
---
# Web Design Pipeline

## When to use
Landing pages, service pages, microsites, demo pages.

## Inputs
Business ({{BUSINESS}}), audience ({{AUDIENCE}}), page job ({{PAGE_JOB}}), aesthetic direction ({{AESTHETIC_DIRECTION}}), references ({{REFERENCE}}), brand tokens.

## Steps
1. Fill `../../templates/master-website-prompt.md`: typography, motion, stack, sections, hero visual, accessibility, performance targets, output location.
2. Design the hero first: one message, one action.
3. Build sections in order; use real copy supplied or approved, no lorem ipsum in the final.
4. Generate hero visuals under `../anti-ai-look-laws/SKILL.md`.
5. Run the design loop and critic pass (`../design-loop-critic/SKILL.md`).
6. Check: color contrast, keyboard use, alt text, responsive layouts, image weight, load time, no layout shift. Record measurements.
7. Regulated content: required disclaimers appear prominently and verbatim from the approved source. A placeholder left in a required disclosure blocks publish.
8. Human approval, then publish via the build in `../../workflows/website-build.md`.

## Gates
No fabricated testimonials, ratings, licenses, awards or statistics. Forms collecting personal data need a privacy notice and the originating department's approval.
