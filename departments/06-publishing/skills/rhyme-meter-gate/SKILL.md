---
name: rhyme-meter-gate
description: Prepare rhyming text for human meter scansion and enforce rhyme rules. The system flags; a human certifies.
---
# Rhyme and Meter Gate

## When to use
Any manuscript or song lyric that rhymes or has a refrain meant to be read aloud or sung.

## Inputs
Draft spreads from `../manuscript-drafting/SKILL.md`.

## Steps
1. Mark the intended meter per stanza (for example, a steady four-beat line) and the rhyme scheme.
2. Prepare a scansion sheet: each line broken into syllables with stressed beats marked.
3. Flag likely problems: stress on a weak syllable, forced inversion, a rhyme that needs a mispronunciation, filler words added only to fill a beat, a line that is one beat short or long.
4. Check rhymes are true rhymes in the target dialect, not near-rhymes, unless chosen deliberately and noted.
5. Prefer natural word order. Reject a line whose word order is bent only to land the rhyme.
6. Hand the sheet to a human reader. The human scans aloud at performance pace and signs off line by line.

## Outputs
Scansion sheet with flags and the human's disposition (keep, fix, rewrite).

## Gates
- Meter is certified by a human scan only. Automated syllable counts are advisory.
- Any rewrite triggers a fresh readability measurement.
