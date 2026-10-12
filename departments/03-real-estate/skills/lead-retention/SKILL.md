---
name: lead-retention
description: The single outbound door: consent ledger, channel content gates, opt-outs, tax-calendar touches, annual equity letter, do-not-call handling.
---
# Lead Retention and Outbound Gate

## When to use
Any email, text, call script, or mail piece to a past client, sphere contact or lead.

## Inputs
Contact record, consent ledger, opt-out list, internal do-not-call list, retention calendar (data with a verified-on stamp), draft message.

## Steps
1. Check recorded owner decisions (for example "no outreach to this contact").
2. Check opt-outs. An opt-out on any channel is honored on all channels, permanently.
3. Check the consent ledger for the channel and basis (express consent, established business relationship with its dates).
4. Content gate by channel: email must meet CAN-SPAM (accurate sender, clear subject, physical address, working opt-out); SMS and similar need TCPA consent or EBR and an opt-out line; direct mail is open.
5. Tax-calendar touches: use only dated entries with a verified-on stamp for the current year. Stale or wrong-year data is refused.
6. Annual equity letter: use `../../templates/annual-equity-letter.md`; no net-to-seller math, no price promises.
7. Place the passing draft in the approval queue with the gate report.
8. Cold outbound requires a complete evidence pack (registry downloads with dates, scrub freshness, training records, violation log). If incomplete, write no list.

## Outputs
Gate report, queued drafts, updated ledger entries.

## Gates
Fail closed. The owner approves each item. Never use a purchased or scraped list without the evidence pack. Voice cloning and synthetic presenters are for media only, never telephony.
