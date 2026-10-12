---
name: executive-voice-check
description: Silent final pass that checks drafts against the executive voice rules and surfaces only violations.
---
## When to use
Last pass on every outbound email, proposal text and notice, after the scrubber.

## Rules
Block: em-dashes and en-dashes, unfilled placeholder tokens, emojis, internal information in client text.
Warn: filler openers, hedging, marketing cliches, three-adjective lists, "not just X, it's Y", passive streaks, sentences over 25 words.
Style: short sentences, specific numbers, plain verbs, subject line, salutation, body, signature.

## Steps
1. Scan the draft.
2. If clean, pass silently.
3. If not, return only the violations with line references. Do not rewrite unless asked.

## Outputs
Violation list or nothing.

## Gates
Block hits stop delivery.
