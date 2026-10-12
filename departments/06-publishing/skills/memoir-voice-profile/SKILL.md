---
name: memoir-voice-profile
description: Build a stratified voice profile from the subject's own writing and run Stage 0 calibration before drafting; measure voice fidelity afterwards.
---
# Memoir Voice Profile

## When to use
Pipeline step 9 (gate G5a) before drafting, and step 14 (gate G5c) for the fidelity report.

## Steps
1. Build a style corpus from the subject's own writing only (messages, posts, letters, emails they authored). Exclude other people's words.
2. **Stratify by register** (for example casual messages, public posts, formal writing). Never average across registers.
3. Hold out part of the corpus with a hash-based split for testing.
4. Measure with scripts: function-word frequencies, lexical diversity measures, punctuation and contraction profiles, sentence-length distribution, distinctive words, character n-gram profiles.
5. **Stage 0 calibration.** Test whether the profile can distinguish the subject's held-out text from a control corpus. Result is PASS or CORPUS-INADEQUATE. If inadequate, do not draft in the subject's voice; fall back to a neutral register and tell the subject why.
6. Record in the voice profile register: subject, profile_version, registers_measured, corpus_words_per_register, stage0_result, control_corpus_version, consent_on_file, date, permitted_use.
7. After drafting, produce a voice-fidelity report comparing draft passages to the profile with thresholds fixed beforehand.

## Gates
- Thresholds are set before measuring and not moved after a failure.
- Voice profile use requires recorded consent and a permitted_use statement.
- A human listens to or reads passages aloud with the subject (see `../memoir-interview-protocol/SKILL.md`).
