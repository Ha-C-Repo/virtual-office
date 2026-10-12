# Book Pipeline (15 steps, fixed order)

Numbered working files per title (01 to 09). Back up before overwrite. Log every stage in `../templates/production-log.md`. BLOCKING = a logged human PASS is required to continue.

| # | Step | Owner | Output file | Gate |
|---|---|---|---|---|
| 1 | Concept: age band, theme, spread count, series fit (`../templates/concept-record.md`) | book-editor | 01 | Owner approves |
| 2 | Manuscript as numbered spreads with right-page hooks (`../skills/manuscript-drafting/SKILL.md`) | book-editor | 02 | |
| 3 | Readability gate, story text only, per spread and whole book (`../skills/readability-gate/SKILL.md`) | book-editor | 03 | In band |
| 3b | Meter scan if rhyming (`../skills/rhyme-meter-gate/SKILL.md`) | human scanner | 03 | Human PASS |
| 4 | Read-aloud at performance pace, then to a child in the age band | human | log | **BLOCKING** |
| 5 | Art direction: character bible, location bible, palette of 5 to 7 colors, one style family (`../skills/character-bible/SKILL.md`) | art-director | 04 | IP screen |
| 6 | Model sheets perfected before scenes | art-director | 04 | Human approval |
| 7 | Prompts: one per spread, typed references, final dimensions with bleed (`../skills/illustration-prompts/SKILL.md`) | art-director | 05 | |
| 8 | Generate 4 to 8 variations per beat, select, inpaint drift | art-director | 05 | |
| 9 | Flip-through QC of all spreads in order | human | 07 | **BLOCKING** |
| 10 | Layout: text as type, fixed-layout ebook (`../skills/layout-and-print-spec/SKILL.md`) | production-manager | 06 | |
| 11 | Cover (print only): calculator, spine math, CMYK | production-manager | 06 | |
| 12 | Physical proof checked by a human (print only) | human | log | **BLOCKING** |
| 13 | AI disclosure questionnaire; record in title record and root register (`../skills/retail-disclosure-gate/SKILL.md`) | rights-compliance-manager | 08 | Owner sign-off |
| 14 | Copyright registration with claim text; disclaim AI material (`../skills/copyright-filing/SKILL.md`) | rights-compliance-manager | 08 | Human files |
| 15 | Publish; log all human work | production-manager | 09 | Owner sign-off |

## Rules
- Never skip or reorder steps. If a gate fails, return to the step that caused it.
- Do not change a threshold to pass a gate.
- Quality bar (`../skills/quality-bar/SKILL.md`) runs after step 3 and before step 15.
- Publishing also follows `release-and-disclosure.md`.
