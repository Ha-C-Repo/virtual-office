---
name: photo-intake-rd
description: R&D pattern for photo and document intake: split, render, extract text layer first, label handwriting as lower confidence, human verify.
---
# Photo Intake R&D

## When to use
Prototyping how a photo or scanned worksheet becomes confirmed problem text.

## Inputs
Image or PDF of a worksheet.

## Steps
1. Split multi-page documents into one file per page.
2. Render each page at high DPI.
3. Extract the text layer deterministically first. If present, it outranks vision.
4. For scans and handwriting use vision transcription, labeled lower confidence.
5. Tag confidence (high, medium, low). An edited transcription is never high.
6. Show the transcription to the learner; require confirmation. Optionally crop to the problem first.
7. Only confirmed text proceeds to `../answer-verification/SKILL.md`.

## Outputs
Per-page text with confidence tags.

## Gates
Never certify from OCR alone. Never trust vision for a count or a measurement. Unconfirmed transcription has no path to a solve.
