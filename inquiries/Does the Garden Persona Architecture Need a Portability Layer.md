---
created: 2026-03-26
author: Christopher Allen
brief_summary: "The garden's persona architecture is Claude Code-specific. SoulSpec proposes a portable cross-framework identity standard; AGENTS.md has become the Linux Foundation cross-tool standard. Six open questions about discovery, versioning, SOUL/IDENTITY separation, cross-framework rendering, conditional knowledge activation, and training vs runtime implications."
tagline: "Should garden personas be portable across frameworks, and at what cost?"
---

- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Does the Garden Persona Architecture Need a Portability Layer

## Research Question

The garden's persona architecture is Claude Code-specific. Persona nodes live as Obsidian markdown files; agent files render them into Claude Code system prompts; the whole mechanism assumes Claude Code as the execution environment. [\[\[SoulSpec Portable Agent Identity Standard\]\]](../models/SoulSpec%20Portable%20Agent%20Identity%20Standard.html) proposes a portable, cross-framework identity standard. AGENTS.md has become the cross-tool standard for project-level context (now under the Linux Foundation). As multi-framework agent deployment becomes more common, does the garden need a portability layer?

## What Is Being Determined

Whether persona portability is a current operational need or a speculative future concern; what the cost of portability indirection would be for a system currently optimized for a single framework; and whether the garden's two-layer design (persona node + agent file) can absorb a portability requirement without structural change.

The underlying question: does the garden serve one agent runtime, or should it aspire to serve any runtime that can consume its persona definitions?

## Open Questions

**1. Discovery**: SoulSpec includes `soul.json` — a package manifest enabling persona discovery across projects and frameworks. The garden has no equivalent. Discovery currently happens through the typed graph (wikilinks, `is_a::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)` traversal). Is the absence of a machine-readable manifest a gap, or is discovery through the typed graph sufficient for the garden's scale and deployment context?

**2. Versioning**: SoulSpec treats personas as versioned artifacts, with explicit version identifiers in the manifest. The garden's personas use git for versioning but carry no version metadata in the persona node itself. If a garden persona is consumed by multiple frameworks over time, which version of the persona is each framework using? Should persona nodes carry version predicates, or is git history sufficient?

**3. Separation of SOUL from IDENTITY**: SoulSpec distinguishes behavioral guidelines (SOUL.md) from identity specification (IDENTITY.md) — the former defines how the agent thinks; the latter defines what it looks like and what it's called. The garden collapses both into one persona node. The psychometric research reinforces the distinction: measurable personality traits (what a persona is) differ from behavioral decision rules (how it acts). Is the garden's collapse a useful simplification, or a conflation that will require retroactive decomposition?

**4. Cross-Framework Rendering**: If the same persona definition needs to generate both a Claude Code agent file and an OpenClaw SOUL.md, where does the rendering logic live? Ollama 0.17 (February 2026) now natively consumes SOUL.md files. Does the garden persona form need a `renders_as::` predicate pointing to platform-specific renditions — a pattern parallel to how compound nodes use Renditions/ for source-specific copies?

**5. Conditional Knowledge Activation**: Character cards in the roleplay community provide lorebooks — keyword-activated context injection that enriches persona behavior in specific conversational domains. [\[\[SoulSpec Portable Agent Identity Standard\]\]](../models/SoulSpec%20Portable%20Agent%20Identity%20Standard.html) provides HEARTBEAT.md — periodic autonomous behavior specifications. Garden persona nodes have neither mechanism. As agents grow more sophisticated, does the persona form need provisions for context-conditional behavioral rules, or does the commission briefing system already cover this?

**6. Training-Time vs. Runtime Implications**: [\[\[Anthropic Soul Document as Training-Time Character Specification\]\]](../glosses/Anthropic%20Soul%20Document%20as%20Training-Time%20Character%20Specification.html) and [\[\[Persona Vectors and the Assistant Axis\]\]](../models/Persona%20Vectors%20and%20the%20Assistant%20Axis.html) operate at the training/weights level. Garden personas operate at runtime. The persona vectors research shows runtime prompts activate mechanistic directions in activation space — but also that extended interactions cause drift away from those directions. Portability to other frameworks raises the question: do those frameworks have equivalent training-time foundations that garden persona prompts can activate, or does a portable persona specification need to be more self-contained because it cannot assume a pre-trained character base?

## Sources

- [\[\[SoulSpec Portable Agent Identity Standard\]\]](../models/SoulSpec%20Portable%20Agent%20Identity%20Standard.html) — portable cross-framework identity standard with soul.json discovery, SOUL/IDENTITY separation, and HEARTBEAT.md provisions
- [\[\[Character Cards as Community-Evolved Persona Specification\]\]](../models/Character%20Cards%20as%20Community-Evolved%20Persona%20Specification.html) — lorebook mechanism for conditional knowledge activation
- [\[\[Anthropic Soul Document as Training-Time Character Specification\]\]](../glosses/Anthropic%20Soul%20Document%20as%20Training-Time%20Character%20Specification.html) — training-time vs. runtime distinction and its implications
- [\[\[Persona Vectors and the Assistant Axis\]\]](../models/Persona%20Vectors%20and%20the%20Assistant%20Axis.html) — mechanistic basis for runtime persona activation and drift
- Research note: [[Persona and Agent Personalities]]↑, lines 493-517

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑

- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
  - The inquiry directly concerns whether the Persona Form structural contract needs extension or decomposition to support portability.

- relates_to::[\[\[SoulSpec Portable Agent Identity Standard\]\]](../models/SoulSpec%20Portable%20Agent%20Identity%20Standard.html)
  - SoulSpec is the primary external candidate for a portability layer; its design decisions frame most of the open questions here.

- relates_to::[\[\[Character Cards as Community-Evolved Persona Specification\]\]](../models/Character%20Cards%20as%20Community-Evolved%20Persona%20Specification.html)
  - Character cards provide the lorebook mechanism; this inquiry asks whether the garden needs an equivalent.

- relates_to::[\[\[Anthropic Soul Document as Training-Time Character Specification\]\]](../glosses/Anthropic%20Soul%20Document%20as%20Training-Time%20Character%20Specification.html)
  - The training/runtime distinction is one of the open questions; the soul document gloss grounds that question in a specific example.

- relates_to::[\[\[The Persona Selection Model\]\]](../models/The%20Persona%20Selection%20Model.html)
  - Portability assumptions depend on whether target frameworks have equivalent persona selection mechanisms.

- relates_to::[\[\[Ephemeral vs Persistent Persona Identity\]\]](../patterns/Ephemeral%20vs%20Persistent%20Persona%20Identity.html)
  - Cross-framework portability raises questions about which identity properties persist across frameworks and which are framework-specific renditions.
