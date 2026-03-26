---
created: 2026-03-10
author: Christopher Allen
brief_summary: "Defines the Captured Stage, the entry point for meeting processing: a raw recording or notes exist but no transcript has been produced. The meeting happened and was preserved, but the content is locked in audio/video format or unstructured shorthand. Lowest utility for retrieval until transcription unlocks the content."
tagline: "Raw recording or notes exist — where meeting processing begins"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Captured Stage

A captured meeting has a record — audio, video, or rough notes taken during the session — but no transcript. The content is preserved but not yet accessible as text. This is the entry point for the meeting processing track.

Capture is the minimum bar for a meeting to enter the vault. Without it, the meeting exists only in memory. A meeting note at captured stage has metadata (date, attendees, topic) and a pointer to the recording or notes, but the substance of the conversation remains locked in its original format.

## Characteristics

- Recording file (audio/video) or rough handwritten/typed notes exist
- Meeting note file created with frontmatter metadata (date, attendees, topic)
- No machine-readable transcript available
- Content not searchable or linkable — locked in non-text format
- Lowest utility for retrieval among processing stages

## Transitions

**Captured → Transcribed**: When a transcript is produced from the recording, either via automated tool (Whisper, Fathom, Otter) or manual effort. The transcript may be rough but represents the spoken content as text.

## Sources

Processing track design from [[Linear Processing Stages for Meetings]]↑. Track placement within the three-track status system from [[Status Lifecycle Tracks]]↑.

## Relations

- relates_to::[\[\[Transcribed Stage\]\]](Transcribed%20Stage.html) — the next stage in the processing track
- relates_to::[[Status Lifecycle Tracks]]↑ — this stage belongs to the processing track
- relates_to::[[Linear Processing Stages for Meetings]]↑ — the decision that defined this stage
