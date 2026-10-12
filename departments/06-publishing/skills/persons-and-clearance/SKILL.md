---
name: persons-and-clearance
description: Track every person in a life story, decide disposition, collect permissions, run the outside legal read, and clear the work for release.
---
# Persons and Clearance

## When to use
Pipeline step 15 (gates G6 to G8), and whenever a draft names or describes a person.

## Steps
1. Populate `../../templates/persons-clearance-register.md` from the manuscript: every person, relationship, whether living, where they appear.
2. Assign a disposition: real name, pseudonym, omit, or existence without detail. Higher-risk categories (health, criminal, sexual, financial, minors) default to the more protective disposition.
3. Where a real name is kept for a living person in a sensitive context, seek written consent; log in `../../templates/permissions-log.md`.
4. Permissions clearance for quoted letters, photos, artwork, lyrics (do not quote lyrics) and any third-party text.
5. Risk scan: defamation, privacy, biometric or health data, minors, business disparagement. Tag items "counsel-required".
6. **Outside legal read** by a qualified reviewer for any T3 or T4 release that names living third parties. Required before release.
7. Record cleared_by and date for each person.

## Gates
- No release naming a living third party without a populated register and an outside legal read.
- Withdrawn consent returns the item to open status.
- Rights-compliance manager signs; {{OWNER}} approves.
