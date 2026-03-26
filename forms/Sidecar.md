---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Sidecar vault type: a markdown metadata envelope for binary or non-local artifacts (video, audio, slides, PDFs) that cannot be represented directly in the knowledge graph. Uses artifact:: predicates to point to canonical sources in local Archives/ folders or remote repositories."
tagline: "Metadata envelopes for binaries and non-local artifacts — the markdown proxy pattern"
formatted: "2026-03-14"
---

- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Sidecar

A sidecar is a markdown file that serves as a metadata envelope for an artifact that cannot be represented directly in markdown — typically a video recording, audio file, slide deck, or PDF. The sidecar makes the artifact discoverable in the knowledge graph without embedding binary content.

```
- is_a::[\[\[Sidecar\]\]](Sidecar.html)
- derived_from::[[Parent Note]]↑
```

## Conventions

- **Naming**: Descriptive slug matching the artifact type (e.g., `recording.sidecar.md`, `slides.sidecar.md`). The `.sidecar.md` suffix distinguishes these from content files.
- **Location**: At the root of the compound document folder, alongside the lead file.
- **Canonical source**: The sidecar documents where the artifact lives — a URL, a repository path, or a local `Archives/` subfolder.
- **Predicates**: `artifact::` predicates for each binary (e.g., `artifact::Archives/recording.mp4`). Non-local artifacts use the Source Repository + Public URLs pattern instead.
- **Archives/**: Binary files live in a gitignored `Archives/` subfolder within the compound folder. The sidecar is the committed, searchable proxy.

## When to Use

- Meeting recordings (video, audio) — private meetings where the recording is canonical
- Slide decks shared during a meeting
- PDFs or other binaries attached to a note
- Non-local artifacts where the canonical version lives in another repository

For non-local artifacts, the sidecar records the source repository and public URLs rather than storing a local copy. This avoids duplicating large files while keeping the reference in the graph.

## Sources

Sidecar conventions from D8-D13 decisions and [[Non-Local Artifact References in Sidecars]]↑. Binary archival pattern from [[Descriptive Slugs for Archive Binaries]]↑.

## Relations

- relates_to::[\[\[Meeting Note\]\]](Meeting%20Note.html) — sidecars are companions within compound meeting folders
- relates_to::[\[\[Transcript\]\]](Transcript.html) — another type of meeting companion file
