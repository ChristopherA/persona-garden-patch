---
created: 2026-03-16
author: Christopher Allen
brief_summary: "Defines the Medical Visit vault type: a compound folder lead file documenting a healthcare appointment. Lives in Health/Visits/ with adaptive sections based on available materials (transcript, portal docs, exam findings). Relates to condition trackers and health overview via typed predicates. Processed by /health-appointment-post skill."
tagline: "Visit note type for health appointments with adaptive sections and multi-source synthesis"
---

- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Medical Visit

A medical visit note is the compound folder lead file documenting a healthcare appointment. Medical visit notes live in `Health/Visits/YYYY-MM-DD Dr. FirstName LastName - Facility/` and serve as the primary record of what happened during a visit, synthesized from available sources.

```
- is_a::[\[\[Medical Visit\]\]](Medical%20Visit.html)
- relates_to::[[Health Overview]]↑
- relates_to::[[Condition Name]]↑
```

## Conventions

- **Location**: `Health/Visits/` in a compound folder named `YYYY-MM-DD Dr. FirstName LastName - Facility/`
- **Lead file**: Same name as the folder with `.md` extension
- **Frontmatter**: `created`, `reviewed`, `brief_summary`, `tagline`, tags `type/reference` + `status/seed`
- **Body predicates**: `is_a::[\[\[Medical Visit\]\]](Medical%20Visit.html)`, `relates_to::` for Health Overview and each condition discussed

## Adaptive Sections

Visit notes include only sections with content. The template (`Templates/Health Visit Note.md`) has all sections as comments; the `/health-appointment-post` skill enables sections based on available materials.

**Always present**: Diagnosis, Treatment Plan, Follow-Up Plan, Action Items

**Conditional**:
- Key Findings (Physical Exam, Clinical Reasoning) — when exam performed
- Imaging — when imaging discussed or results available
- Symptom History — when transcript available
- Source Comparison — when multiple sources cross-referenced
- Activity Guidance — when activity/restrictions discussed
- Person Note Suggestions — when new or notable providers

## Distinct From Meeting Note

Medical visits share pipeline elements with meetings (transcript cleanup, notes synthesis) but have unique concerns: condition trackers, medication management, portal document processing, health overview updates, and provider-specific person notes. Medical visits use `is_a::[\[\[Medical Visit\]\]](Medical%20Visit.html)` (not `is_a::[\[\[Meeting Note\]\]](Meeting%20Note.html)`) and live in `Health/Visits/` (not `Meetings/`).

## Compound Folder Contents

Visit folders contain the lead file plus artifacts:
- Portal downloads (.pdf + .txt extracts)
- Pre-visit prep documents (.md + .docx)
- Recordings (.m4a) and raw transcripts (.txt)
- Cleaned transcripts (.md)

## Processing

The `/health-appointment-post` skill orchestrates visit processing with two paths:
- **Path A** (with transcript): transcript cleanup → meeting notes synthesis → visit note
- **Path B** (without transcript): portal documents + filled checklist → guided visit note creation

## Sources

Medical Visit type conventions from Health Intake Conventions and health-appointment-post skill (sessions 1-4 of maintain/personal-health workstream).

## Relations

- relates_to::[\[\[Person Note\]\]](Person%20Note.html) — provider person notes created from visit context
- relates_to::[[Health]]↑ — domain map of content
