# 02 Sales: Outbound Message (one door)

Applies to every outward message from any function: lead replies, retention touches, review requests, stip requests, check-ins. Nothing auto-sends, auto-replies or auto-dials. Phone is not a messaging channel; AI voice never dials, leaves voicemail or answers.

## Order
1. **Recorded owner decisions.** Confirm the owner's current preferences (Tier 2) that apply to this message type.
2. **Consent ledger.** Check the contact's channel state: GRANTED, DENIED or UNKNOWN, with basis and date. UNKNOWN or DENIED = REFUSED. No bypass argument.
3. **Registry and relationship checks.**
   - Text or call: internal do-not-call list, national registry scrub with freshness and evidence, consent or established business relationship record (TCPA).
   - Email: accurate subject, ad disclosure if promotional, physical address, working opt-out honored within the statutory window (CAN-SPAM). The validator refuses rather than warns.
   - Direct mail: no consent rules apply. It is the home for the equity letter, with no cost or gross reachable.
4. **Channel content gate.** Blocklist, specificity, disclosure block if any payment or rate, grade-adjective gate, placeholders resolved, no internal money.
5. **AI disclosure.** If the surface is conversational AI, the fixed Tier 1 template is in the first message.
6. **Owner voice check** (`../skills/marketing-owner-voice-check/SKILL.md`).
7. **Approval queue.** Risk class: internal, customer-facing, money, legal. Money and legal items are approved individually. Low-risk batches may be approved together. A human sends.
8. **Log.** Record every message and every refusal. A refusal is logged as REFUSED with the reason.

## Opt-outs
Record an opt-out the moment it arrives, from any channel, and add it to the internal list. Never message a contact who opted out.

## Escalation
Any message touching financing terms, an allegation or a promise goes to {{OWNER}} first.
