# 07 AI Video and Creative Production

> **Authored, not extracted:** the anti-AI-look laws, kids-animation style laws and example timing/word-count thresholds in this department were written to fill gaps, not taken from earlier projects. Their review status is in `knowledge/authored-rules-review.md`; read it before relying on them.

## Purpose
An AI-assisted video and marketing-creative studio for {{COMPANY}}. It produces:

1. **Commercial and brand video:** 15-second pre-rolls, 30-second commercials, 60-second brand films, explainers, product demos, vertical reels, short films.
2. **Children's animated video:** episodes, nursery rhymes, learning loops, livestream loops, vertical shorts (with the series bibles owned by `06-publishing`).
3. **Marketing web design:** a design-system-led website build pipeline and brand token upkeep.

Generative tools make footage and images. Humans approve scripts, review every frame, clear rights and sign off before anything public.

## When to use
- A client or internal department needs a video, reel, ad, explainer or site page.
- Setting up or resuming a generative-video run (browser-driven or local render).
- Checking a video for anti-AI artifacts, IP lookalikes, kids-platform compliance or music/voice rights.
- Building or revising a marketing web page or brand token set.

## Contents
**Agents** (`agents/`): `creative-director-producer.md` (lead), `prompt-engineer.md`, `scriptwriter-storyboarder.md`, `qa-compliance-reviewer.md`, `automation-operator.md`, `web-design-engineer.md`.

**Skills** (`skills/<name>/SKILL.md`): video-type-router, creative-brief, anti-ai-look-laws, cost-gate, design-loop-critic, environment-detection, generative-platform-automation, timing-memory-and-persistence, local-render-engine, rig-workflow, kids-animation-style, ip-safety-screen, kids-platform-compliance, music-and-voice-rights, cadence-and-volume, short-film, brand-style-systems, web-design-pipeline.

**Templates** (`templates/`): creative-brief, script-json, session-resume, run-state, preroll-15s, commercial-30s, brand-film-60s, explainer-60s, product-demo, vertical-reel, storytime-episode, nursery-rhyme-and-learning-loop, livestream-loop-and-shorts-funnel, short-film-archetypes, episode-bible, ip-blocklist, frame-review-checklist, pre-generation-qa, brand-tokens, master-website-prompt.

**Workflows** (`workflows/`): commercial-video-production, video-episode-pipeline, character-consistency-video, generative-platform-run, local-render-hybrid, website-build, session-resume, delivery-and-disclosure.

**Knowledge** (`knowledge/`): glossary, rules, schemas.

## Hard rules
1. No paid generation without a quoted plan and explicit human "go". One approval per stated batch.
2. Every frame of a finished piece is reviewed by a human. Blocking.
3. Nothing public (post, ad, upload, send to client) without logged executive/owner approval.
4. IP and lookalike screen before any character, music or brand element is used. Blocking.
5. One locked style system per production.
6. Never fabricate claims, testimonials, endorsements or results in video copy. Regulated industries require compliance review of scripts.
7. Production log entry and AI disclosure register row for every published asset.
8. Never read or store credentials; keys live in an environment file whose values are never opened.

## Harnesses (`harnesses/`)
Stdlib Python 3 with self-tests: `video_planner.py`. See `harnesses/README.md`. Run `python video_planner.py --selftest` after any change.

## Handoffs
- From `06-publishing`: episode scripts and series bibles; read-along and trailer requests.
- To `06-publishing`: finished read-along video and promo shorts.
- From `05-insurance-medicare-marketing` and `01-construction` (and other departments): briefs for ads, explainers and web pages. Regulated copy (for example insurance or health marketing) is compliance-reviewed in the originating department before generation.
- To `09-business-admin-finance-compliance`: vendor/subscription register, spend log.
- To `08-ai-services-software`: automation scripts, render tooling, browser-driver maintenance.
