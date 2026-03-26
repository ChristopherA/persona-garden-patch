---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Skill form type: a compound node bundling trigger, procedure, quality criteria, and rationale — with graph dependencies declaring which garden nodes the skill reads and follows. Skills bridge the garden's knowledge layer and the agent's execution layer."
tagline: "How does an agent execute this reliably? — the structural contract for skill forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Skill Form

**Core question**: "How does an agent execute this reliably?"

A compound node bundling trigger logic (when), procedure (how), quality criteria (what counts as success), and rationale (why these decisions). What distinguishes a garden skill from a standalone script or checklist is graph integration: skills declare which garden nodes they read, which patterns they implement, and which principles constrain them. The procedure section references other nodes via labeled edges, making the skill's knowledge dependencies explicit and traversable.

## Two Layers, One Form

Claude Code skills live in `.claude/skills/` as operational artifacts following the Agent Skills spec (SKILL.md, scripts/, references/). Garden skills live in `Garden/skills/` as knowledge nodes participating in the typed graph. The two layers can be the same artifact: a skill in `Garden/skills/` symlinked to `.claude/skills/` is simultaneously a deployable package and a graph-connected knowledge node.

The garden layer adds what the operational layer lacks: typed edges to the principles the skill follows, the patterns it implements, the form types it reads, and the models that inform its design. An operational skill without graph connections works but cannot be discovered, composed, or audited through the garden's predicate vocabulary.

## Structural Contract

A skill form requires:

- **Trigger** — When this skill activates. Explicit conditions and exclusions.
- **Graph dependencies** — Which garden nodes the skill reads, follows, or implements. Declared as predicates: `reads::`, `follows::`, `implements::`. These are the skill's knowledge inputs — the garden context it needs to execute correctly.
- **Procedure** — Step-by-step process the agent follows. Steps may reference garden nodes by wikilink, loading them on demand per [[Progressive Disclosure Over Eager Loading]]↑.
- **Quality criteria** — What counts as success. Measurable where possible.
- **Rationale** — Why these steps, in this order, with these constraints.
- **Sources** — Prior art, standards, or experience the skill draws from.
- **Relations** — Connections to patterns it implements, protocols it follows, decisions that shaped it.

Naming heuristic: action-oriented compound noun describing the capability. "Annotated Citation Creation" not "Citation Skill." Name what the skill does, not what it is.

## Typical Predicates

- `is_a::[\[\[Skill Form\]\]](Skill%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)`
- `in_domain::[[Domain Name]]↑`
- `implements::[\[\[Pattern Form\]\]](Pattern%20Form.html)` — patterns the skill operationalizes
- `follows::[\[\[Principle Form\]\]](Principle%20Form.html)` — principles that constrain execution
- `reads::[\[\[Form Type\]\]](Form%20Type.html)` — form types the skill needs to load during execution
- `follows::[\[\[Protocol Form\]\]](Protocol%20Form.html)` — protocols the skill adheres to

## Exemplars

No garden-native instances yet. Two operational skills are candidates for garden promotion:

- `.claude/skills/annotated-citation/` — creates Citation Form nodes from URLs or clippings; reads Citation Form structural contract, follows bibliographic format rules, implements the citation-to-node pipeline
- `.claude/skills/node-research/` — researches topics and produces garden-form-typed sections; reads multiple Form Type definitions to classify extracted content

## Category

Action form — captures *what to do* and *what happened*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 100-101.

## Relations

- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — skills operationalize patterns into executable procedures
- relates_to::[\[\[Protocol Form\]\]](Protocol%20Form.html) — skills may implement protocols for single-agent execution
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — skill design involves decisions about approach and trade-offs
- relates_to::[[Progressive Disclosure Over Eager Loading]]↑ — skills load graph dependencies on demand, not eagerly
- relates_to::[[Context Conservation Hierarchy]]↑ — graph dependencies declare the minimum context a skill needs
