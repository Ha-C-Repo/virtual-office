---
name: kids-platform-compliance
description: Compliance checks for children's video on public platforms: made-for-kids designation, inauthentic-content policy, quality principles and AI disclosure.
---
# Kids Platform Compliance (blocking)

## When to use
Pipeline step 9 for any children's video, and for any commercial video that may be seen by children.

## Checks (verify wording against the platform's current published policy; log source and date)
1. **Made-for-kids designation:** set correctly per the audience. Do not mark kids content as general audience to gain features.
2. **Children's privacy law (for example COPPA in the United States):** no personal data collection from child viewers; features that depend on it are disabled for kids content.
3. **Inauthentic or mass-produced content policy:** content must show original creative contribution; avoid repetitive, templated or low-effort uploads. See `../cadence-and-volume/SKILL.md`.
4. **Quality principles for kids content:** age-appropriate, educational or enriching value, no deceptive thumbnails or titles.
5. **AI disclosure toggle:** disclose realistic synthetic content as the platform requires; keep consistent with the AI disclosure register.
6. **Rights:** music and voice cleared (`../music-and-voice-rights/SKILL.md`).
7. **Metadata:** honest titles, descriptions and tags; no misleading claims.

## Outputs
Compliance checklist with PASS/FAIL per item, evidence and date.

## Gates
Blocking. Human sign-off by {{OWNER}} before publish. Unverified policy facts go on the open list, not acted on.
