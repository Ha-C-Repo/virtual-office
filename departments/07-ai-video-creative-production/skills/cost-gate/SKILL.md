---
name: cost-gate
description: Quote any paid generation plan and wait for explicit human go before running; one approval per stated batch.
---
# Cost Gate

## When to use
Before any paid image, video, voice or music generation, and before any retry batch.

## Steps
1. Build the plan: clip list, attempts per clip, engine/mode, expected cost units (credits or equivalent), unlimited-mode status, contingency.
2. Present the quote in plain text: total, per-clip, what is included, what happens if clips fail.
3. Wait for an explicit "go" from {{OWNER}} or {{CLIENT_NAME}}'s authorized contact. Silence is not approval.
4. Record the go (who, when, batch scope) in the production log.
5. Run only the approved batch. If more is needed, quote again.
6. Compare actual to quoted at completion; log variance.

## Design loop variant
For design and web iteration, set a maximum number of loop iterations in the quote.

## Gates
Blocking. No paid generation without a logged go. Never loosen the batch scope after approval.
