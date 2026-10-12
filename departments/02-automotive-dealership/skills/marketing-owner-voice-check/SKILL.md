---
name: marketing-owner-voice-check
description: Final voice pass for owner-signed text: em-dashes, three-adjective lists, hedging, placeholders, padding and layout kill list.
---
## Rules
- Short sentences, figures not words, plain verbs, sentence case.
- No em or en dashes. No emojis in client documents.
- No filler openers, no hedging, no vague intensifiers without a fact.
- No three-adjective lists. No "not just X, it's Y".
- No unfilled placeholder tokens.
- Prose over bullets in reports; no bullets when declining.
- Email: subject 5 to 8 words, first-name salutation, three short paragraphs maximum, signature block with {{DEALERSHIP}}, {{ADDRESS}}, {{PHONE}}.
- Owner voice: short, direct, numbers first, decisions not options. Builder voice: fuller sentences, one line on why, never hedge numbers.

## Steps
Scan, return violations only, pass silently if clean. Severity: block (dashes, placeholders, emoji in client docs), warn (the rest).
