---
created: 2026-03-10
author: Christopher Allen
brief_summary: "Defines the Transcribed Stage: a raw transcript exists but has not been cleaned. Speaker labels may be wrong or missing, filler words are present, timestamps may be inconsistent. The content is now text-searchable but reads poorly and requires cleanup before synthesis."
tagline: "Raw transcript exists but unclean — searchable but not yet readable"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Transcribed Stage

A transcribed meeting has a text transcript produced from the recording. The spoken content is now machine-readable and searchable, but the transcript is raw — speaker labels may be wrong, filler words clutter the text, and formatting is whatever the transcription tool produced.

Transcription is the step that unlocks meeting content from audio/video into text. The quality varies by tool: Whisper produces bare text with timestamps, Fathom adds speaker labels and AI summaries, Otter provides real-time transcription with varying accuracy. Regardless of source, the raw transcript needs editorial attention before it can serve as a reliable reference.

## Characteristics

- Full or partial transcript exists as text
- Speaker labels present but may be incorrect or inconsistent (first name vs full name, "Speaker 1" placeholders)
- Filler words present (um, uh, you know, like, so)
- Formatting reflects transcription tool output, not editorial structure
- Content is searchable — a significant step up from captured stage
- May include AI-generated summary from the transcription tool (Fathom, Otter)

## Transitions

**Transcribed → Cleaned**: When the transcript has been processed through cleanup — speaker names normalized, filler words calibrated (removed or reduced to natural rhythm), formatting standardized. The `/transcript-cleanup` skill handles this step.

## Sources

Processing track design from [[Linear Processing Stages for Meetings]]↑. Track placement within the three-track status system from [[Status Lifecycle Tracks]]↑.

## Relations

- relates_to::[\[\[Captured Stage\]\]](Captured%20Stage.html) — the previous stage in the processing track
- relates_to::[\[\[Cleaned Stage\]\]](Cleaned%20Stage.html) — the next stage in the processing track
- relates_to::[[Status Lifecycle Tracks]]↑ — this stage belongs to the processing track
