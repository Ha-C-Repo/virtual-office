---
name: scheduling-and-routines
description: Defines deadline watches, recurring routines and calendars: what runs, when, with which inputs, what it may never do, and how it fails safe. Build the routine by hand first, then schedule it. Use for deadline tracking, sweeps, briefings and recurring checks.
---

# Scheduling and routines

## When to use
Any recurring task, deadline clock, expiry watch, weekly sweep, morning briefing, or calendar of dated milestones.

## Inputs
Task description, source registers, owner role, cadence, freshness windows, warning windows.

## Steps
1. Run the task by hand at least twice. Write down inputs, steps, outputs, defects.
2. Write the routine as a standalone prompt that reads governance first (constitution, bands), then its inputs.
3. Define the schedule: day, time, timezone. Define the data it reads. Routines can only read data they can reach (cloud-resident or exported); local-only files are invisible to them.
4. Stamp input age. Refuse to act on stale data; report it instead.
5. Define warning levels for deadlines: for example URGENT inside 3 days, THIS WEEK inside 7. "Filed" and "recorded" are different states. Flag dependency risk earlier when the anchor date is missing.
6. Write the "may never" list for the routine: never shorten a lock, never discount below schedule, never delete register entries, never mark VERIFIED without a recent physical check, never send, post or dial.
7. Output: a brief to the human with items sorted by urgency and one "do this first" line.
8. Failure mode: on error or missing input, stop and report. Do not guess. Circuit-break on repeated external errors.
9. Promote the routine only after its output passes owner review twice.

## Typical routines
Morning briefing; deadline sentinel; register sweep; consent expiry sweep; weekly report draft; aged-item review; inbox scan for leads or invitations; weekly audit; monthly context audit; quarterly policy re-check.

## Outputs
Routine definition, schedule, run log, brief.

## Gates
Unknown day counts are NEEDS_INPUT, never guessed. Rules and dates are re-verified at the stated interval.

## Anti-patterns
Scheduling before the manual version works. Routines with write access they do not need. Silent failures.
