---
created: 2026-03-04
author: Christopher Allen
brief_summary: "Defines the vocabulary for treating plain markdown as a typed graph: documents are nodes, predicate wikilinks are edges. Covers seven structural terms and a full semantic predicate catalog across provenance, structural, lifecycle, and generative categories. Any markdown editor can read and write the graph."
tagline: "Plain markdown as a typed graph — nodes, edges, and predicates defined."
formatted: "2026-03-14"
---

- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Deep Context Graph Vocabulary

Deep context is a typed graph stored in plain markdown. Every document that carries predicate wikilinks is a node; every predicate wikilink is a directed, named edge. The graph emerges from the files — no database, no external index, no tooling required. An agent or human navigating the vault follows edges between nodes to build understanding.

This gloss consolidates the graph vocabulary: structural terms from the compound document decisions, new terms from compound node research, and the full semantic predicate catalog.

## New Terms

**Note**: Any markdown document in a knowledge vault. Not source code documentation (READMEs, API docs), which has its own conventions. A note becomes a node when it participates in the typed graph.

**Context node**: A note that participates in the typed graph through predicate edges. Atomic or compound, garden or vault. A note with `is_a::` and `relates_to::` edges is a context node; a note with only YAML frontmatter and no predicates is not.

**Form type**: The category a node belongs to (Pattern Form, Decision Form), declared by its `is_a::` edge. "Node" and "form type" are distinct: there is one Pattern Form type but many pattern nodes. When discussing individual documents, say "node" or "instance of [Form Type]"; reserve "form" for the type itself.

**Typed edge**: A predicate wikilink — a named, directional connection between context nodes. Written as `predicate::[[Target]]↑`. The predicate names the relationship type; the wikilink identifies the target. Examples: `relates_to::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`, `is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)`, `derived_from::"https://example.com"`.

**Compound node**: A folder-based context node containing a lead file, optional sibling files, and optional `Renditions/` and `Archives/` subfolders. Generalizes "compound document" from the garden decisions to vault-wide use.

**Lead file**: The primary access point of a compound node — the file that gives an LLM or human the most useful context first. A single lead file serves both audiences; LLM-specific context lives in a YAML frontmatter field rather than a separate file. See [[Lead File Selection Guidance]]↑.

## Terms from Compound Document Decisions

**Rendition**: A format-transformed markdown copy of an external source. Searchable. Lives in `Renditions/`. Created by conversion tools. Carries `derived_from::` pointing to the canonical source. Defined by [[Renditions and Archives Replace Sources]]↑ and [[Renditions and Archives as Distinct Artifact Types]]↑.

**Archive**: A preserved original binary. Lives in `Archives/` within a compound node folder. Named with [[Descriptive Slugs for Archive Binaries|descriptive slugs]]↑. Most don't need sidecars. Distinct from `Attachments/`, which is Obsidian's paste/drag subfolder for embedded media. Defined by [[Renditions and Archives Replace Sources]]↑ and [[Renditions and Archives as Distinct Artifact Types]]↑.

**Sidecar** (`.sidecar.md`): A metadata envelope for a binary that cannot carry its own frontmatter. Links to its binary via `artifact::` (per [[Artifact Predicate for Binary Metadata]]↑) and to the canonical source via `derived_from::`. Only created when the binary is actively cited or needs agent discoverability. Defined by [[Sidecar Files as Metadata Envelopes]]↑.

## Classification Predicates

Four predicates classify every context node in the graph:

- **`is_a::`** — the node's form type or vault type (`is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)`, `is_a::[\[\[Meeting Note\]\]](../forms/Meeting%20Note.html)`)
- **`has_status::`** — lifecycle stage (`has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)`, `has_status::[[Curated]]↑`)
- **`in_precinct::`** — organizational unit (`in_precinct::[\[\[Garden Precinct\]\]](Garden%20Precinct.html)`, `in_precinct::[\[\[Household Precinct\]\]](Household%20Precinct.html)`). Garden precinct node types carry structural contracts; household precinct types serve operational capture. See [[Precinct as Organizational Unit]]↑.
- **`in_domain::`** — knowledge area (`in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`). Links a node to the domain it belongs to. A node may belong to multiple domains.

The first two are required on every classified note. The latter two appear on garden nodes and are optional on vault types.

## Semantic Predicate Catalog

Beyond classification predicates, the graph uses semantic predicates to express relationships between nodes. These are organized into four categories by the kind of relationship they describe.

### Provenance Predicates (where did this come from?)

- `derived_from::` — this gloss synthesizes that source
- `motivated_by::` — this pattern arose from that case
- `informed_by::` — this skill drew on that reference
- `abstracted_from::` — this principle compressed that pattern
- `grounded_in::` — this principle derives from that value
- `established_by::` — this conviction emerged from that experience
- `extracted_from::` — this node was extracted from that source document. Construction predicate: when the source is archived or reincarnated as a living node, upgrade to `implements::` or `relates_to::`

### Structural Predicates (how does this relate?)

- `implements::` — this skill enacts that pattern
- `embodies::` — this protocol expresses that principle
- `composes_with::` — these nodes interoperate
- `extends::` — this node builds on that one
- `contradicts::` — these nodes are in tension
- `constrains::` — this boundary limits that agent's authority
- `relates_to::` — general-purpose connection (use a more specific predicate when one fits)

### Lifecycle Predicates (what happened over time?)

- `supersedes::` — this replaced that
- `evolved_into::` — this became that
- `validated_by::` — this case confirms that pattern
- `invalidated_by::` — this case broke that assumption

### Generative Predicates (what does this produce or require?)

- `proposes::` — this inquiry puts forward that hypothesis
- `directed_at::` — this question requires that person's or group's judgment (a boundary marker)
- `resolved_by::` — this inquiry was answered by that case, pattern, or reference
- `generates::` — this node produced that node through investigation or use
- `anticipates::` — this scenario imagines consequences of those forces or drivers
- `signaled_by::` — this scenario would be confirmed by that observable development
- `prepares_for::` — this scenario informs that decision or strategy

Predicates are freeform strings. Consistency depends on ongoing vocabulary curation — awareness of what exists, periodic review for drift, consolidation of redundant terms, and clarification of ambiguous ones. The vocabulary above has stabilized through use but is not enforced by the system. See [[Predicate Vocabulary Stabilization]]↑ for the open question on when to formalize, and [[Informal Edges Poison the Graph]]↑ for the failure mode that curation prevents.

## Sources

Extracted from the Graph Vocabulary gloss section of the compound nodes research note. Semantic predicate catalog from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "The Predicate Grammar" section.

## Relations

- extracted_from::[[Compound Nodes for Knowledge Management]]↑
  - The vocabulary gloss section, lines 91-115.

- extends::[[Typed Relations as Simple Graphs in Plain Markdown]]↑
  - The typed edge concept builds on the predicate::[[target]]↑ convention defined in the typed relations specification.

- defines_vocabulary_from::[[Renditions and Archives as Distinct Artifact Types]]↑
  - The rendition, archive, and sidecar terms originate from these decisions.

- defines_vocabulary_from::[[Artifact Predicate for Binary Metadata]]↑
  - The artifact:: predicate is defined as graph vocabulary here.

- relates_to::[[Knowledge Compounds Through Typed Edges Not Filing]]↑
  - The graph vocabulary enables knowledge compounding — typed edges create semantic compounds that filing into folders cannot.
