---
created: 2026-03-10
author: Christopher Allen
brief_summary: "Defines the Cleaned Stage: the transcript has been processed for readability — speaker names normalized, filler words calibrated, formatting standardized. The content reads as a reliable record of what was said but has not been synthesized into structured meeting notes with topics, action items, or key takeaways."
tagline: "Transcript cleaned and readable — a reliable record but not yet synthesized"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Cleaned Stage

A cleaned meeting has a transcript that reads well. Speaker names follow the full-name-first convention (full name on first occurrence, first name thereafter), filler words are calibrated to the chosen cleanup level, and formatting is consistent. The transcript is a reliable record of what was said.

Cleaning is editorial work, not synthesis. The goal is a transcript that someone can read and follow without guessing who said what or wading through verbal tics. The content structure still mirrors the conversation's chronological flow — topical organization and insight extraction happen at the next stage.

## Characteristics

- Speaker names normalized (full name on first occurrence, first name thereafter)
- Filler words calibrated to cleanup level (light keeps ~30%, medium keeps ~10-20%, heavy removes nearly all)
- Formatting standardized — consistent speaker labels, paragraph breaks at topic shifts
- Timestamps preserved or normalized
- Reads as a coherent conversation record
- No topical reorganization or synthesis applied

## Transitions

**Cleaned → Summarized**: When the transcript has been synthesized into structured meeting notes — organized by topic rather than chronology, with action items extracted, key takeaways identified, and an inverted pyramid structure (summary above the divider, detail below). The `/meeting-notes` skill handles this step.

## Sources

Processing track design from [[Linear Processing Stages for Meetings]]↑. Cleanup conventions from the `/transcript-cleanup` skill, which defines light/medium/heavy cleanup levels. Track placement within the three-track status system from [[Status Lifecycle Tracks]]↑.

## Relations

- relates_to::[\[\[Transcribed Stage\]\]](Transcribed%20Stage.html) — the previous stage in the processing track
- relates_to::[\[\[Summarized Stage\]\]](Summarized%20Stage.html) — the next stage in the processing track
- relates_to::[[Status Lifecycle Tracks]]↑ — this stage belongs to the processing track
