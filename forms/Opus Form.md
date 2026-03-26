---
created: 2026-03-15
author: Christopher Allen
brief_summary: "Defines the Opus form type: a compound garden node for the author's own substantial intellectual works. Lead file contains the work itself (living document), supported by analysis.md, insights.md, and sub-folders for Expressions (published venues), Renditions (drafts and derived versions), and Archives (binary artifacts). Opuses nest recursively. Attribution uses role-specific predicates grounded in the principal-agent framework."
tagline: "What am I saying here, and how does it connect? -- the structural contract for authored works"
---

is_a::[\[\[Form Type\]\]](Form%20Type.html)
has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Opus Form

**Core question**: "What am I saying here, how does it connect, and can I prove I said it?"

A compound garden node for the author's own substantial intellectual works. The lead file contains the work itself -- a living document in the author's voice. Companion files provide self-reflexive analysis, extractable garden insights, and tracking of the work's various published forms. Grounded in three traditions: FRBR's Work-Expression-Manifestation hierarchy from library science, IndieWeb's identity-consolidation patterns, and the principal-agent framework from agency law and Self-Sovereign Identity.

The name "opus" (Latin: work product, plural: opera) connects etymologically to cooperation (from *operari*, to produce from *opus*) -- the same root that organizes the cooperation-collaboration distinction in the Synpraxis domain.

## When to Use Opus Form

An Opus is reserved for substantial intellectual works that merit compound treatment: works you develop, publish, and maintain over time. The test: does this work have its own name, purpose, and ongoing development?

**Is an Opus**: A book. A substantial essay or article. A presentation with original argument. A pattern language. A specification you authored. A course curriculum.

**Is not an Opus**: A quick social post. An email reply. A meeting note. A clipping of someone else's work (use Citation Form). A single pattern within a pattern language (use Pattern Form).

**Graduating to Opus**: Authored content in Authored/ can graduate to Garden/opuses/ when it warrants compound treatment (analysis, insights, expression tracking). Lighter authored content stays in Authored/.

## Recursive Nesting

Opuses nest: a parent Opus can contain child Opuses. A trilogy is an Opus whose children are individual book-Opuses. A blog series may be a parent Opus containing individual article-Opuses. The parent lead file describes the arc and purpose; child Opuses are self-contained compounds within it.

```
Garden/opuses/[Parent Title]/
  [Parent Title].md                          -- parent lead file
  [Child Opus A]/                            -- child compound
    [Child Opus A].md
    [Child Opus A] — Analysis.md
    [Child Opus A] — Insights.md
    Expressions/
  [Child Opus B]/                            -- child compound
```

The nesting depth is not limited. A book-Opus within a trilogy-Opus might itself contain chapter-Opuses if they warrant independent treatment.

## Compound Structure

```
[Opus Title]/
  [Opus Title].md                            -- lead file (the work itself)
  [Opus Title] — Analysis.md                 -- self-reflexive analysis
  [Opus Title] — Insights.md                 -- extractable garden nodes
  [Opus Title] — Salience.md                 -- context-specific relevance bridges
  Expressions/                               -- published venues and forms
    [venue-sidecar].md                       -- metadata pointer per publication
  Renditions/                                -- drafts and derived versions
    [draft-or-derivative].md                 -- historical or lossy versions
  Archives/                                  -- binary source artifacts
    [file].key, .pdf, .pptx                  -- gitignored binaries
```

Sub-files use the lead file's full name with an em-dash suffix (` — Analysis.md`, ` — Insights.md`, ` — Salience.md`), making all analytical depth wikilink-accessible. See [[Proper Obsidian Names for Garden Compound Sub-Files]]↑ for the decision and rationale.

**Lead file**: The work itself, in the author's voice. Free-form structure -- the work determines its own sections. Living document: updated, revised, extended over time.

**Analysis**: Self-reflexive analysis of the work's arguments, framework, lineage, limitations. Garden-connected (wikilinks to related nodes). Can be revised when the work evolves substantially (unlike Citation Form's append-only analysis).

**Insights**: Extractable takeaways -- concepts, patterns, models, inquiries that could become standalone garden nodes. Maps connections to existing garden domains.

**Salience**: Context-specific relevance bridges -- compressed arguments for why this opus matters to specific audiences, lenses, or collaborative contexts. Each entry is a bridge. Append-only as the work serves new contexts.

**Expressions/**: Metadata sidecars tracking where the work is published and in what form. Each sidecar has frontmatter: `expresses:`, `published_at:`, `published_on:`, `form:` (manifestation, variant), `verified:`. When an expression has multiple files that must work together (a website with HTML/CSS/JS, a slide deck), place them in a named sub-folder (e.g., `Expressions/web/`) so the expression is self-contained and functional — you should be able to open index.html and have the site work. The sidecar sits alongside the sub-folder and serves as the manifest (listing which files are published vs. development-only).

**Renditions/**: Early drafts, abbreviated versions, lossy transformations, archived snapshots of the work at specific points in time. Preserves historical states.

**Archives/**: Binary artifacts (Keynote files, PDFs, images). Typically gitignored. Referenced by Expression or Rendition sidecars.

## Attribution Predicates

Attribution uses role-specific predicates grounded in the principal-agent framework. Predicates capture the CURRENT state of attribution; git history preserves the full record. Roles evolve over time -- when a co-author becomes lead author, update the predicates and document the change in the Attribution section.

### Required

- `authored_by::[[Person]]↑` -- who wrote the content
- `principal::[[Person]]↑` -- who directed the work and bears ultimate responsibility (from agency law; see [\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html))

### Recommended

- `copyright_held_by::[[Person]]↑` -- legal ownership (distinct from authorship)
- `produced_by::[[Person]]↑` -- who made the work happen as a creative project (from film/game industry usage; often the same as principal but carries different connotation)

### As Needed

- `foreword_by::[[Person]]↑` -- foreword contributor
- `illustrated_by::[[Person]]↑` -- illustrator
- `contributed_by::[[Person]]↑` -- catch-all for other roles
- `edited_by::[[Person]]↑` -- editor
- `translated_by::[[Person]]↑` -- translator

The distinction between authorship and responsibility matters for AI-assisted works: a human may not author a single word yet bears full responsibility as principal. "The augmentation is the method, not the author."

## Other Predicates

- `is_a::[\[\[Opus Form\]\]](Opus%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` (or Growing, Evergreen)
- `in_domain::[[Domain Name]]↑`
- `in_series::[[Series Title]]↑` -- membership in a thematic collection
- `inspired_by::[[Source]]↑` -- intellectual lineage
- `extends::[[Other Opus]]↑` -- when one work builds on another
- `develops_from::[[Other Opus]]↑` -- earlier work this one grew out of
- `presents::[[Garden Node]]↑` -- references garden Pattern, Model, or other nodes the work discusses
- `same_work_as::URL` -- identity consolidation: "this work also exists here" (the IndieWeb rel-me concept applied to works)

## Frontmatter

- `created:` -- when the Work was first conceived
- `published:` -- when first publicly released
- `author:` -- vault author (standard garden field)
- `brief_summary:`, `tagline:` -- standard garden fields
- `signing_key:` -- optional SSI provenance pointer

## Relationship to Other Forms

**Opus presents Patterns**: A pattern book (Opus) references garden Pattern Form nodes via `presents::`. The garden Pattern nodes are the living truth; the Opus captures how the pattern appeared in a specific published Expression.

**Opus presents Models**: An article that introduces a framework references its garden Model Form node. Multiple Opuses can reference the same Model.

**Opus is not Citation**: Citation Form captures a dossier ABOUT someone else's work. Opus Form contains YOUR work itself. The attribution predicates differ: Citation uses `cites_work_by::` (third-person); Opus uses `authored_by::` and `principal::` (first-person).

**Opus may contain Cases**: A book with case studies can reference garden Case Form nodes. Cases are immutable historical records; the Opus provides narrative context.

## SSI and Provenance Layer

Opus Form acknowledges that works can carry verifiable authorship credentials without specifying the mechanism. The principal-agent framework from agency law provides the conceptual foundation. Practical verification may use:

- Signed git commits (existing infrastructure)
- DID-linked authorship (person note contains DID)
- Verifiable Credentials asserting authorship
- Gordian Envelope endorsements

The form definition remains mechanism-agnostic. The SSI layer sits alongside the garden, not inside it.

## Open Areas

- **Series formalization**: Currently using `in_series::` predicate + lightweight index page. May warrant its own form type if series develop consistent internal structure.
- **Expression sidecar format**: Needs concrete exemplars to stabilize. Current proposal: frontmatter with expresses/published_at/published_on/form/verified fields.
- **RAA Framework integration**: Peter Kaminski's Role-Authority-Attribution framework (raa-framework.peterkaminski.wiki) proposes six relationship types. Not yet integrated into garden predicates.
- **Temporal attribution**: Roles evolve (editor becomes co-author becomes lead author). Currently handled by updating predicates + git history. May need more structured approach.

## Exemplars

- [[Sociosocratic Learning & Seminars]]↑ -- Seed stage, compound. Solo-authored essay on collaborative learning, published as GitHub Gist. Develops from the Hybrid Flipped Learning presentation.
- [[My Hybrid Flipped Learning Environment]]↑ -- Seed stage, compound (lead article + Expressions/ with SlideShare sidecar). ~5,000-word article expanding a 2013 faculty presentation on game-design-informed pedagogy. Published on SlideShare (abbreviated).
- [[Field Notes on Handpan Sound Models & Instruments]]↑ -- Seed stage, dual-format compound (interactive HTML + portable markdown per instrument). Web-publishable reference work with code assets, requirements docs, and a 2014 precursor article as Rendition. Demonstrates Opus Form handling of hybrid web/vault content.

## Category

Structural form -- captures *what I am saying* and *how it connects*.

## Sources

- FRBR/LRM Work-Expression-Manifestation-Item hierarchy (IFLA)
- IndieWeb rel-me and rel-author identity consolidation patterns
- [\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html) -- principal-agent framework
- [[Cooperation vs Collaboration as Distinct Concepts]]↑ -- etymological grounding (opus = work product)
- "Wikis, Publishers, Communities, Community Stewards" email thread (Jan 2026) -- producer/principal distinction
- [[The Gardening Problem Returns]]↑ -- "authorship is not performance but responsibility"

## Relations

- relates_to::[\[\[Citation Form\]\]](Citation%20Form.html) -- citations capture others' works; opuses capture your own
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) -- opuses may present patterns as garden nodes
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) -- opuses may present models as garden nodes
- relates_to::[\[\[Case Form\]\]](Case%20Form.html) -- opuses may contain case studies
- relates_to::[\[\[Reference Form\]\]](Reference%20Form.html) -- references synthesize knowledge; opuses are original contributions
- relates_to::[\[\[Research Form\]\]](Research%20Form.html) -- research investigates; opuses articulate
- relates_to::[\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html) -- attribution framework
- relates_to::[[Principal-Agent Relationship in Augmented Knowledge Work]]↑ -- implementation model
- implements::[[Proper Obsidian Names for Garden Compound Sub-Files]]↑ -- em-dash suffix naming convention for compound sub-files
