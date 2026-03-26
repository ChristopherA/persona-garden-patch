---
created: 2026-03-10
author: Christopher Allen
brief_summary: "Defines the Summarized Stage: meeting notes have been synthesized from the transcript into topical structure with action items, key takeaways, and inverted pyramid organization. The meeting record is complete as a standalone reference. Distribution (publishing or sharing) is the only remaining step."
tagline: "Synthesized into structured notes — complete as a reference, ready for distribution"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Summarized Stage

A summarized meeting has structured notes synthesized from the cleaned transcript. Content is organized by topic rather than chronologically, action items are extracted with owners, and key takeaways sit above the horizontal rule in inverted pyramid style. The meeting record is complete as a standalone reference.

Summarization transforms a conversation record into a knowledge artifact. The chronological transcript preserves what was said; the summary preserves what matters. Multiple AI summaries (from transcription tools, meeting participants, or dedicated synthesis) can be compared to catch gaps — one model's summary highlights what another missed.

## Characteristics

- Organized by topic, not chronologically
- Action items extracted with assignees
- Key takeaways and quotes above the horizontal rule (inverted pyramid)
- Supporting detail and full discussion below the rule
- Person notes suggested or created for attendees
- `brief_summary:` and `tagline:` frontmatter populated
- Standalone readable without the transcript

## Transitions

**Summarized → Published**: When the meeting notes are shared beyond the vault — either published to a URL (`is_published::URL` for public meetings) or shared with attendees (`is_shared::DATE` for private meetings). Publication is a distribution action, not a content transformation.

## Sources

Processing track design from [[Linear Processing Stages for Meetings]]↑. Summary conventions from the `/meeting-notes` skill, which defines topical organization, inverted pyramid structure, and multi-AI comparison. Track placement within the three-track status system from [[Status Lifecycle Tracks]]↑.

## Relations

- relates_to::[\[\[Cleaned Stage\]\]](Cleaned%20Stage.html) — the previous stage in the processing track
- relates_to::[\[\[Published Stage\]\]](Published%20Stage.html) — the next stage in the processing track
- relates_to::[[Status Lifecycle Tracks]]↑ — this stage belongs to the processing track
