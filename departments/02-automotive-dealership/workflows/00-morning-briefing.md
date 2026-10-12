# 00 Morning Briefing (weekday)

Owner: Dealership Lead (`../agents/00-dealership-lead.md`). Runs each weekday before opening. Output is one page to {{OWNER}}. The briefing reports; it never acts, sends or posts. A routine ships only after its output passes owner review twice.

## Inputs
Unit records, pipeline, deadline timelines, temp tag log, lead log, review queue, compliance flags, we-owe queue.

## Steps
1. **Units front-line ready.** List units whose recon is closed and grade re-run. Flag units listed but not on the ground, or on the ground with no photos (Inventory sentinel).
2. **Deals pending funding.** For each: open stips, jacket gaps, covered-borrower check recorded, days since write-up. Deals idle 3 or more days are flagged.
3. **Today's deadlines.** From `../templates/title-deadline-timeline.md` and `../templates/title-temp-tag-log.md`: URGENT (3 days), THIS WEEK (7 days). Include license and continuing-education dates.
4. **Overnight leads.** Count, source, time received, time to first drafted reply, any past target.
5. **New reviews.** Count by surface and class. Any class 1 is shown first and already escalated.
6. **We-owe queue.** Items due today and anything overdue (escalate).
7. **Compliance flags.** Open gate blocks, expiring certificates, registers past re-verify date.
8. **The one thing to do first.** Pick one by this order: overdue we-owe, class 1 review, URGENT deadline, deal at risk of funding with gaps, aged unit, everything else.

## Output format
Numbers first, short lines, no adjectives. Close with: what is ready, what is blocked, the one thing to do first, confidence tier (HIGH / MED / LOW) and open flags.

## Gates
- Every figure traces to a record. If a record is missing, say "no record", not an estimate.
- Human sign-off: {{OWNER}} reads the briefing. Any action it suggests goes through the approval queue.
