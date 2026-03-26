---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Transcript vault type: a cleaned speech-to-text record derived from a meeting recording via derived_from:: predicate. Speaker-normalized (full name first, then first name) with three cleanup levels and configurable filler calibration. Always a sidecar to its meeting note, never standalone."
tagline: "Cleaned speech record with speaker normalization — always derived from a meeting"
formatted: "2026-03-14"
---

- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Transcript

A transcript is a cleaned speech-to-text record derived from a meeting recording. Transcripts are always sidecars to their meeting note — they do not exist standalone. The `derived_from::` predicate links back to the parent meeting.

```
- is_a::[\[\[Transcript\]\]](Transcript.html)
- derived_from::[[Meeting Note Name]]↑
```

## Conventions

- **Speaker normalization**: Full name on first occurrence (`**Peter Kaminski**:`), first name only thereafter (`**Peter**:`).
- **Cleanup levels**: Light (minimal edits), Medium (filler calibration ~10-20% retained for natural rhythm), Heavy (near-zero filler). Medium is the default.
- **Frontmatter**: `created`, `reviewed`, `brief_summary`, `tagline`, `ai-transcription` (source format), `ai-processing` (cleanup tool and model).
- **Naming**: `YYYY-MM-DD Name - Transcript (Cleaned).md` within the compound meeting folder.

## Sources

Transcript conventions from the transcript-cleanup and meeting-capture skills. Processing pipeline: raw VTT/SRT → speaker normalization → filler calibration → cleaned markdown.

## Relations

- derived_from::[\[\[Meeting Note\]\]](Meeting%20Note.html) — every transcript belongs to a meeting
- relates_to::[\[\[Sidecar\]\]](Sidecar.html) — transcripts are companions to meeting notes, similar to how sidecars are companions to binary artifacts
