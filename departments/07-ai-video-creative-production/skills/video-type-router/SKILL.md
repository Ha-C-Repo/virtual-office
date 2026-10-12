---
name: video-type-router
description: Route a video request to the right type, template, duration and pipeline (pre-roll, commercial, brand film, explainer, demo, reel, short film, kids episode).
---
# Video Type Router

## When to use
At intake, right after environment detection.

## Routing table
| Request | Type | Template | Pipeline |
|---|---|---|---|
| Skippable ad opener | 15-second pre-roll | `../../templates/preroll-15s.md` | commercial |
| Broadcast or social ad | 30-second commercial (hook, problem, agitate, solution, proof, call to action) | `../../templates/commercial-30s.md` | commercial |
| Company story | 60-second brand film | `../../templates/brand-film-60s.md` | commercial |
| Teach one idea | Explainer (about 60 seconds, about 10 clips) | `../../templates/explainer-60s.md` | commercial |
| Show a product | Product demo | `../../templates/product-demo.md` | commercial |
| Vertical social | Vertical reel (9:16, 15 or 30 seconds) | `../../templates/vertical-reel.md` | commercial |
| Narrative piece | Short film (3-act, vignette, cinematic sequence) | `../../templates/short-film-archetypes.md` | commercial plus `../short-film/SKILL.md` |
| Children's story episode (5 to 10 minutes) | Storytime episode | `../../templates/storytime-episode.md` | episode |
| Song-led kids | Nursery rhyme | `../../templates/nursery-rhyme-and-learning-loop.md` | episode |
| Repeating lesson | Learning loop | same | episode |
| Always-on stream | Livestream loop | `../../templates/livestream-loop-and-shorts-funnel.md` | episode |
| Funnel to episodes | Shorts funnel | same | episode |

## Steps
1. Identify type; if ambiguous, ask one question.
2. Confirm aspect ratio and platform specs for the destination; record in the brief.
3. Open the matching workflow: `../../workflows/commercial-video-production.md` or `../../workflows/video-episode-pipeline.md`.
4. Estimate generation cost (clips x attempts) for the cost gate.

## Gates
Regulated-industry content (insurance, health, financial, real estate, education claims) needs the originating department's compliance clearance on the script before generation.
