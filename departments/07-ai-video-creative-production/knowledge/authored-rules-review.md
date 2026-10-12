---
name: authored-rules-review
description: Review status of the rules in this department that were written fresh rather than extracted from earlier work. Read before relying on any threshold or law in 07.
status: reviewed-2026-10-12
---
# Authored Rules Review (07 AI Video and Creative Production)

Conclusion: the authored rules are sound as working heuristics and house rules. None is a legal or platform requirement. Two had overclaims and were reworded. One external fact was checked against its source. Platform policy wording was not re-verified and stays on the open list.

Method (2026-10-12): each rule was read, classified, and checked for claims stronger than its basis. Only WCAG 2.3.1 was fetched from its primary source. Everything else is reasoned review and is marked so. No rule was removed.

## Classification key
- House rule: a choice the studio makes to reduce risk or quality problems. Not a requirement of any outside party.
- Heuristic: a planning number. Calibrate with real measurements.
- Legal pointer: names a body of law. Counsel decides application.
- Platform pointer: names a platform policy. Policy text changes; verify and log source and date.

## Findings
| # | Rule | Where | Class | Basis | Status | Action taken |
|---|---|---|---|---|---|---|
| 1 | One locked style system per production | anti-ai-look-laws 1, rules 4 | House rule | Consistency practice | OK | none |
| 2 | Image-to-video for any shot with a person; never text-to-video for faces | anti-ai-look-laws 2, rules 5 | House rule | Reduces face drift | Overclaim ("never") | Reworded to a house rule with an owner-approved exception path |
| 3 | One reference per subject; never chain outputs as references | laws 3, 4 | House rule | Prevents drift accumulation | OK | none |
| 4 | Avoid quality adjectives; describe what the camera sees | law 5 | Heuristic | Prompting practice | OK | none |
| 5 | Avoid hands, teeth, crowds, text in frame | law 8 | Heuristic | Common generative artifacts at time of writing | May age as tools improve | Revisit each time the tool or model changes |
| 6 | No generated text or logos in footage | law 9 | House rule | Garbled text; trademark risk | OK | none |
| 7 | About 2.5 words per second of narration | rules 7, preroll template (about 35 words in 15 s) | Heuristic | Typical conversational narration pace; real pace varies by talent and language | Plausible, uncalibrated | Labeled as heuristic; `{{WORDS_PER_SECOND}}` added; `harnesses/video_planner.py` added. 35 words in 15 s equals about 2.3 per second, consistent |
| 8 | No flashing or strobing in kids content | kids-animation-style 3, rules | Safety rule | WCAG 2.3.1: no more than three flashes in any one-second period, or below the general and red flash thresholds. Fetched 2026-10-12 | Verified (web accessibility standard, used here as a conservative proxy) | Test criterion added. The standard is for web pages; the studio's target is stricter (none) |
| 9 | Wide stable staging, gentle pacing, calm sound | kids-animation-style 1, 2, 6 | House rule | Child-directed content practice | OK | none |
| 10 | Cadence cap on uploads per week | cadence-and-volume | House rule | Platforms publish no numeric cap known to this review; cap is the owner's setting | OK as a placeholder | none; `{{MAX_UPLOADS_PER_WEEK}}` stays owner-set |
| 11 | Made-for-kids designation, children's privacy | kids-platform-compliance | Legal and platform pointer | COPPA (US) and platform kids policies exist | Not re-verified | Stays blocking; log source and date at each use |
| 12 | Mass-produced or inauthentic content policy | kids-platform-compliance 3, cadence | Platform pointer | Major video platforms have such policies; wording changes | Not re-verified | Stays on the open list |
| 13 | AI disclosure toggle | kids-platform-compliance 5 | Platform pointer | Platforms have disclosure features for realistic synthetic content | Not re-verified | Stays on the open list |
| 14 | Generated output may not be copyright-protectable | rules IP section | Legal pointer | US Copyright Office human-authorship position | Stated too generally | Reworded with jurisdiction, VERIFY note and counsel reference |
| 15 | Voice cloning needs written consent | rules, music-and-voice-rights 2 | House rule and legal pointer | Likeness and voice statutes exist in some places | Incomplete | Added counsel note |
| 16 | Six-point IP screen; unsure means no | ip-safety-screen | House rule | Conservative by design | OK | none |
| 17 | Cost gate: quote, go, one approval per batch | cost-gate, rules 1 | House rule | Spend control | OK | `harnesses/video_planner.py quote` computes the quote |
| 18 | Example timings in templates (for example 0-3 s hook, 3-6 s promise) | preroll-15s, commercial-30s, others | Heuristic | Common ad structures; not a standard | Plausible | Treat as starting points; adjust per brief |

## Open list (verify at point of use, log source and date)
- Current platform wording on made-for-kids, inauthentic content and AI disclosure.
- Current Copyright Office guidance on AI-generated material and registration.
- Any state or national voice and likeness law that applies to the target market.
- Tool pricing used in cost quotes.
