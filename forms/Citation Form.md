---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Citation form type: a structured dossier on a single work containing bibliographic entry, summary, key points, key quotes, influence, sources, and relations. Named as Author (Year) Abbreviated Title. Atomic at Seed stage, graduating to compound (analysis.md, insights.md, Renditions/, Archives/) as analysis deepens. Append-only."
tagline: "What do I need to know about this source? — the structural contract for citation forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Citation Form

**Core question**: "What do I need to know about this source?"

A structured dossier on a single work: metadata, abstract, analysis, insights, connections to other works, bibliography, and archived source material. A compound object containing glosses, extracted principles, and typed relations to other citations. Append-only; new insights accumulate but analysis isn't rewritten.

## Naming Convention

Citations follow the pattern `Author (Year) Abbreviated Title`, with an optional venue suffix `, in/from Publication` when venue adds important context:

- `[[Roy (2026) Words Without Consequence, from The Atlantic]]↑`
- `[[Chatlatanagulchai (2025) Agent READMEs]]↑`

The `citation_slug:` frontmatter field provides a short cross-referencing key (e.g., `roy-2026-words-without-consequence`).

## Structural Contract

A citation lead file has 7 required sections:

1. **Bibliographic Entry** — Full inline citation: bold-italic title, year, [type], italic author(s), publication details, URL.
2. **Summary** — ~75 words. What the work covers and why it matters. Practitioner voice.
3. **Key Points** — Analytical summaries in our voice (not quotes). Bold subheading per point. 7-10 points for Growing/Evergreen; fewer acceptable at Seed.
4. **Key Quotes** — Verbatim quotes with section/page reference. 2-5 minimum.
5. **Influence** — Impact on field and methodology/significance. ~60-80 words.
6. **Sources** — Where this node's content comes from (the work itself, secondary sources consulted).
7. **Relations** — Typed predicate links to other garden nodes.

Frontmatter includes `citation_slug:` and `publication_year:` alongside standard fields.

## Compound Structure

Citations graduate from atomic (single file) to compound when analysis deepens:

```
Author (Year) Abbreviated Title/
├─ Author (Year) Abbreviated Title.md              ← lead file
├─ Author (Year) Abbreviated Title — Analysis.md   ← primary source analysis
├─ Author (Year) Abbreviated Title — Insights.md   ← extraction candidates
├─ Author (Year) Abbreviated Title — Salience.md   ← context-specific relevance bridges
├─ Renditions/
│  └─ source-title.md                              ← markdown copy of source
└─ Archives/
   └─ citation-slug.pdf                            ← original binary
```

Sub-files use the lead file's full name with an em-dash suffix (` — Analysis.md`, ` — Insights.md`, ` — Salience.md`). This makes all analytical depth wikilink-accessible and visible in Obsidian's graph — garden content is synpraxis (collaborative knowledge) and must be findable. See [[Proper Obsidian Names for Garden Compound Sub-Files]]↑ for the full decision.

Sidecar files (`.sidecar.md`) remain invisible by design — metadata envelopes, not knowledge nodes.

### Sub-file roles

| Sub-file | Role | Growth pattern |
|----------|------|----------------|
| Analysis | Analytical breakdown: named patterns, second-order analysis, structural insights about the source | Written once per source, may be supplemented |
| Insights | Extraction candidates: each tagged with target garden form type, inference level, ghost links | Append-only as new extraction targets emerge |
| Salience | Context-specific relevance bridges: compressed arguments for why this citation matters to specific lenses, articles, or arguments. Each entry is a **bridge** connecting the citation to a specific audience | Append-only as the citation serves new contexts |

When both primary and secondary analysis exist, use `— Analysis (Primary).md` and `— Analysis (Secondary).md`.

## Typical Predicates

- `is_a::[\[\[Citation Form\]\]](Citation%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)`
- `in_domain::[[Domain Name]]↑`
- `cites_work_by::[[Person Name]]↑` — who wrote the cited work (subject is the citation node: "this citation cites a work by...")
- `cited_by::[[Other Citation]]↑` — reverse citation links
- `cites::[[Other Citation]]↑` — forward citation links

## Exemplars

- [[Roy (2026) Words Without Consequence, from The Atlantic]]↑ — Seed stage, atomic. Philosophical argument grounding the [[Human Authority Over Augmentation Systems]]↑ principle.
- [[Chatlatanagulchai (2025) Agent READMEs]]↑ — Seed stage, atomic. Empirical study validating the architecture's treatment of context files as living documents.

## Category

Structural form — captures *how things relate* and *what we understand*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 68-69.

## Citation Form vs. Opus Form

Citation Form and [\[\[Opus Form\]\]](Opus%20Form.html) share compound structure (Analysis, Insights, Salience sub-files, Renditions/, Archives/) and the em-dash suffix naming convention, but serve opposite relationships to the work:

- **Citation Form**: a dossier ABOUT someone else's work. Key predicate: `cites_work_by::[[Person]]↑`. The lead file summarizes and analyzes. The source is fixed and external. Append-only (new analysis accumulates but doesn't rewrite).
- **Opus Form**: the author's OWN work. Key predicates: `authored_by::[[Person]]↑`, `principal::[[Person]]↑`. The lead file IS the work. The source is living and local. Revisable (the work evolves, analysis updates).

Both forms share the principal-agent attribution framework (see [[Role-Specific Attribution Predicates for Opus Form]]↑) but apply it differently: Citation uses `cites_work_by::` (third-person attribution); Opus uses `authored_by::` and `principal::` (first-person attribution).

## Relations

- relates_to::[\[\[Gloss Form\]\]](Gloss%20Form.html) — citations contain glosses as interpretive annotations
- relates_to::[\[\[Reference Form\]\]](Reference%20Form.html) — references synthesize multiple citations
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — citations may contain pattern instances
- relates_to::[\[\[Opus Form\]\]](Opus%20Form.html) — opuses capture the author's own works; citations capture others' works
- implements::[[Proper Obsidian Names for Garden Compound Sub-Files]]↑ — em-dash suffix naming convention for compound sub-files
