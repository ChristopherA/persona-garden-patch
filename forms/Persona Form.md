---
created: 2026-03-21
author: Christopher Allen
brief_summary: "Defines the Persona form type: an agent identity specification declaring perspective, objectives, operating principles, behavioral patterns, and blind spots. Personas define WHO an agent is; skills define HOW it executes. Operational deployment via .claude/agents/ files."
tagline: "Who is this agent and how does it behave? — the structural contract for persona forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Persona Form

**Core question**: "Who is this agent and how does it behave?"

An agent identity specification that declares perspective, objectives, operating principles, behavioral patterns, and acknowledged blind spots. What distinguishes a persona from a skill is the separation of identity from execution: a Gardener persona defines who the agent is and what it prioritizes; a `/citation-creator` skill defines how it performs a specific task. Personas compose with skills — the same skill executes differently depending on the persona wielding it.

## Two Layers, One Design

Claude Code agents live in `.claude/agents/` as operational artifacts (markdown files with YAML frontmatter where the body is the system prompt). Garden personas live in `Garden/personas/` as knowledge nodes in the typed graph. Unlike skills, the two layers cannot be the same artifact — the operational format (YAML frontmatter for tool restrictions, model selection, isolation mode) and garden format (body predicates, structural sections, relations) have incompatible contracts. The garden form is the canonical design document; the agent file is derived from it.

The garden layer adds what the operational layer lacks: typed edges to the principles the persona follows, the patterns it implements, the domains it operates in, and the other personas it coordinates with. An operational agent without graph connections works but cannot be discovered, composed, or audited through the garden's predicate vocabulary.

## Structural Contract

A persona form requires:

- **Core identity** — What the agent is and what distinguishes it. One paragraph.
- **Primary objectives** — What the agent works toward. Ordered by priority.
- **Non-goals** — What the agent explicitly does not do. Prevents scope creep.
- **Operating principles** — How the agent approaches its work. Behavioral constraints.
- **Behavioral patterns** — Concrete responses to common situations. "When X, do Y."
- **Declared blind spots** — What the agent tends to miss or deprioritize. Required across all persona approaches. Each blind spot should be specific enough to trigger behavioral refusal when the pattern is recognized — "may over-architect" is disclosure; "creating structure for things that already have precedent" is a brake. Vague blind spots don't activate; specific ones function as active constraints during decision-making.
- **Failure modes** — How the agent fails when operating poorly.
- **Positioning** — What role analogies help understand this agent's function.
- **Session obligations** — Close-out steps (mandatory, ordered) and context recovery instructions (what to read on startup or after /clear). Derived from the agent's operational close-out documentation in `.claude/agents/`.
- **Sources** — Prior art, frameworks, or experience the persona draws from.
- **Relations** — Connections to other personas it coordinates with, principles it follows, domains it operates in.

Optional for compound personas:
- **Composition model** — How this persona relates to others (polarity pairs, orchestrator-worker, peer coordination).
- **Consumer context** — Who or what uses this persona and how (deliberation, task execution, reflection, orchestration).

Naming heuristic: role noun with "Persona" suffix — `[Role] Persona`. "Groundskeeper Persona" not "Garden Orchestration Persona." Name who the agent is, not what the form type is. Use the full name in wikilinks: `[\[\[Groundskeeper Persona\]\]](../personas/Groundskeeper%20Persona.html)`.

## Typical Predicates

- `is_a::[\[\[Persona Form\]\]](Persona%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)`
- `in_domain::[[Domain Name]]↑`
- `in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)` or `[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)`
- `coordinates_with::[\[\[Persona Form\]\]](Persona%20Form.html)` — other personas in the same system
- `follows::[\[\[Principle Form\]\]](Principle%20Form.html)` — principles that constrain behavior
- `operates_in::[\[\[Domain Form\]\]](Domain%20Form.html)` — knowledge domains the persona works within

## Five Observed Approaches

The persona design space spans at least five axes (from [[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑ plus this workstream's contribution):

| Approach | Axis of Diversity | Example |
|----------|-------------------|---------|
| Historical thinker | Intellectual tradition | Socrates, Feynman |
| Cultural reflection | Culture, language | Toki Pona philosopher |
| Professional role | Functional domain | Engineering lead |
| Soul/identity | Persistent identity | OpenClaw SOUL.md |
| **Operational** | System function | Groundskeeper, Gardener |

All five share the structural requirement of declared perspective and declared blind spots. The operational approach adds coordination semantics (orchestrator-worker relationships, commission assignment, worktree isolation).

## Category

Action form — captures *who acts* and *how they behave*.

## Exemplars

- [\[\[Groundskeeper Persona\]\]](../personas/Groundskeeper%20Persona.html) — Garden Precinct orchestrator (first instance)
- [\[\[Gardener Persona\]\]](../personas/Gardener%20Persona.html) — Garden Precinct worker (first instance)

## Sources

- [[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑ — inquiry exploring the design space
- [[Structured Disagreement Through Persona Review]]↑ — pattern using personas for adversarial deliberation
- [[Principal-Agent Relationship in Augmented Knowledge Work]]↑ — authority model for agent personas
- Claude Code custom agents specification — operational deployment format

## Relations

- relates_to::[\[\[Skill Form\]\]](Skill%20Form.html)
  - Personas define WHO; skills define HOW. They compose: a persona uses skills but is not a skill.

- relates_to::[\[\[Protocol Form\]\]](Protocol%20Form.html)
  - Coordination between personas (Groundskeeper assigning commissions to Gardeners) is a protocol concern. The persona defines the participant; the protocol defines the interaction.

- relates_to::[\[\[Boundary Form\]\]](Boundary%20Form.html)
  - Persona non-goals and scope constraints define boundaries of agent authority.

- relates_to::[[Principal-Agent Relationship in Augmented Knowledge Work]]↑
  - Personas operate within the principal-agent authority model. The vault owner is the principal; personas are agents with delegated authority.
