---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Meeting Note vault type: a record of a synchronous conversation with attendees, topics, and outcomes. Uses body predicates for attendees and processing status. May contain compound documents with transcript, chat log, and recording sidecars."
tagline: "Synchronous conversation records with attendees, outcomes, and optional compound artifacts"
formatted: "2026-03-14"
---

- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Meeting Note

A meeting note records a synchronous conversation — who participated, what was discussed, what was decided, and what follows. Meeting notes belong to the [\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html): they have templates and conventions suited to capture-first workflows, not the formal structural contracts of [\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html) form types.

Meeting notes live in `Meetings/` and use body predicates for classification and attendees:

```
- is_a::[\[\[Meeting Note\]\]](Meeting%20Note.html)
- has_status::[\[\[Summarized Stage\]\]](Summarized%20Stage.html)
- attendee::[[Person Name]]↑
```

## Conventions

- **Attendees as predicates**: `attendee::[[Person Name]]↑` in the body, not YAML arrays. Full name on first reference; each attendee links to a person note in `People/Individuals/`.
- **Processing status**: Captured → Transcribed → Cleaned → Summarized → Published. Tracked via `has_status::` with the appropriate stage predicate.
- **Inverted pyramid**: Summary and key quotes above the `---` divider; detailed discussion topics below.
- **Frontmatter**: `created`, `reviewed`, `brief_summary`, `tagline`, `ground-rules`, `duration`.

## Compound Documents

Simple meetings are flat files. When a meeting has a transcript, chat log, slides, or recording, it becomes a compound document: a folder with the meeting note as the lead file and sidecars at the folder root.

```
Meetings/
  2026-03-05 Meeting Name/
    2026-03-05 Meeting Name.md          ← lead file (is_a::[\[\[Meeting Note\]\]](Meeting%20Note.html))
    2026-03-05 Meeting Name - Transcript (Cleaned).md
    2026-03-05 Meeting Name - Chat.md
    recording.sidecar.md
    Archives/                           ← gitignored binaries
      recording.mp4
      audio.m4a
```

## Cross-Precinct Extraction

Garden nodes are often extracted from meeting notes. Decisions made in meetings become `[\[\[Decision Form\]\]](Decision%20Form.html)` entries. Patterns observed become `[\[\[Pattern Form\]\]](Pattern%20Form.html)` entries. The meeting note remains the source record in the household precinct; extracted forms use `extracted_from::` to link back from the garden precinct.

## Sources

Conventions from [[Deep Context Garden Conventions]]↑, "Vault Types" section. Meeting predicate architecture from D8-D13 decisions in garden-foundation workstream.

## Relations

- relates_to::[\[\[Transcript\]\]](Transcript.html) — cleaned speech record derived from a meeting
- relates_to::[\[\[Chat Log\]\]](Chat%20Log.html) — text chat captured during a meeting
- relates_to::[\[\[Sidecar\]\]](Sidecar.html) — metadata envelope for binary artifacts
- relates_to::[\[\[Person Note\]\]](Person%20Note.html) — attendees link to person notes
