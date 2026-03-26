---
created: 2026-03-10
author: Christopher Allen
brief_summary: "Defines the Published Stage, the terminal stage for meeting processing: notes have been shared beyond the vault. Public meetings carry is_published::URL pointing to the web page. Private meetings carry is_shared::DATE marking when attendees received the notes. Processing is complete; further changes are content maturity (garden stages), not processing."
tagline: "Shared beyond the vault — the terminal stage of meeting processing"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Published Stage

A published meeting is the terminal stage of the processing track. The notes have been shared beyond the vault — either to a public URL or to meeting attendees. Processing is complete.

Publication is a distribution event, not a content transformation. The meeting notes don't change when published; they become available to an audience beyond the vault owner. After publication, any further development of the meeting's content is a maturity concern (the garden stage track), not a processing concern.

## Characteristics

- Meeting notes shared beyond the vault
- Fork predicates carry distribution details:
  - `is_published::URL` — for public meetings, the URL where notes are accessible
  - `is_shared::DATE` — for private meetings, the date notes were shared with attendees

- Both predicates can coexist (notes shared privately, then later published)
- Processing track complete — no further processing stages
- Content may still be at any garden maturity stage (a published meeting note can be a seed)

## When Published Does Not Apply

Some meetings are processed for personal reference only — captured, transcribed, cleaned, and summarized but never shared. These remain at summarized stage indefinitely. Published stage is not a required endpoint; it applies when distribution happens.

## Sources

Processing track design from [[Linear Processing Stages for Meetings]]↑, which defines fork predicates (`is_published::URL`, `is_shared::DATE`) as distinct from the linear processing stages. Track placement within the three-track status system from [[Status Lifecycle Tracks]]↑.

## Relations

- relates_to::[\[\[Summarized Stage\]\]](Summarized%20Stage.html) — the previous stage in the processing track
- relates_to::[[Status Lifecycle Tracks]]↑ — this stage belongs to the processing track
- relates_to::[[Linear Processing Stages for Meetings]]↑ — the decision that defined fork predicates for distribution tracking
