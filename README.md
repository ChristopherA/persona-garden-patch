# Persona Garden Patch

A [garden patch](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) exploring how AI agent personas are designed, activated, and governed — and what happens when the design document becomes a first-class knowledge node rather than a configuration file.

## Why a Persona Garden?

Agent systems need personas. Most approaches treat them as configuration: a system prompt, a YAML file, a role string. The persona is consumed by the runtime and invisible to everyone else.

This [garden patch](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) asks: what if the persona were a knowledge artifact? One that carries its own design rationale, declares its blind spots, references the research that shaped it, and participates in a typed knowledge graph alongside the models, patterns, and inquiries that inform it.

The eight personas here — from estate-level strategist to specialized garden worker — are not documentation *about* agents. They are the design authority *for* agents. Each persona node defines behavioral scope, declared blind spots, operational architecture, and relationships to peer personas. The agent configuration files are downstream artifacts that implement what the persona specifies.

This distinction matters because it makes persona design auditable, composable, and evolvable through the same mechanisms that govern any other knowledge node: [structural contracts](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html), status stages, typed predicates, and peer review.

## What's in This Patch

**8 persona design documents** (patch-native⊙) — the operational architecture for a multi-agent knowledge estate:
- Orchestrators: Seneschal, Groundskeeper, Chancellor
- Boundary guardian: Chatelaine
- General worker: Gardener
- Specialized workers: Cultivator, Forager, Pruner

**15 research-extracted nodes** (grafted from source garden) — the analytical framework:
- 6 models mapping the persona design landscape
- 5 patterns capturing what works and what fails
- 2 glosses defining key concepts
- 2 open inquiries about portability and evaluation

**11 infrastructure nodes** (grafted) — the garden system itself:
- How to read garden patches, nodes, and predicates
- What [precincts](glosses/Garden%20Precinct.html), [structural contracts](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html), and [ghost links](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html) are
- Why this architecture exists

**1 foundational decision** (grafted) — Deep Context as an Architecture for Captured Reasoning

**2 knowledge domains** — Agentic Architecture and Deep Context Architecture

**35 form type definitions** (grafted) — the structural contracts that govern every node

## Three Ways to Read This

**Start with the personas** — read [Seneschal Persona](personas/Seneschal%20Persona.md) for the most complete example, then [Groundskeeper Persona](personas/Groundskeeper%20Persona.md) to see how personas relate to each other.

**Start with the research** — read [The Persona Selection Model](models/The%20Persona%20Selection%20Model.md) to understand how LLMs activate persona patterns, then [Role Prompting Improves Style but Not Accuracy](patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.md) for what role prompting actually does.

**Start with the system** — read [Garden Patch as Composable Knowledge Fragment](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.md) to understand what you're looking at, then the [Node Directory](NODES.md) for the full inventory.

## How to Read Garden Nodes

### Six Kinds of Links

- **[Grafted nodes](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)** appear as clickable `[[Node Name]]` links — copied from the source garden and navigable here
- **[Patch-native⊙ nodes](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html)** are marked with ⊙ — born in this patch, this is their home
- **[Upstream↑ nodes](glosses/Upstream%20Node%20as%20Source%20Garden%20Reference.html)** are marked with ↑ — they exist in the source garden but aren't included here. See the [Upstream Nodes section](NODES.md#upstream-nodes↑) in the Node Directory for summaries
- **[Ghost links](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html)** appear as plain `[[Node Name]]` text (not clickable) — stakes marking possible future nodes
- **Regular links** use standard markdown `[text](url)` syntax

### Predicates

Every node carries typed predicates — labeled directed edges in the knowledge graph:

```
- is_a::[[Persona Form]]         ← what kind of node this is
- has_status::[[Growing Stage]]  ← maturity level
- in_domain::[[Agentic Architecture]]  ← knowledge area
- in_precinct::[[Garden Precinct]]     ← organizational zone
```

These aren't tags or metadata. They're structural relationships that make the graph navigable and queryable.

### Form Types

Each node is an instance of a form type with a [structural contract](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html). The contract defines what questions the form answers and how instances are organized. See [Form Type Definitions](forms/) for all contracts.

## Knowledge Domains

**[Agentic Architecture](domains/Agentic%20Architecture.md)** — How autonomous agents are designed, configured, coordinated, and governed. Most persona and research nodes live here.

**[Deep Context Architecture](domains/Deep%20Context%20Architecture.md)** — The knowledge system architecture itself: typed forms, predicates, precincts, and the design decisions that shaped them.

---

**Author**: Christopher Allen
**License**: [CC-BY 4.0](LICENSE)
**Status**: Seed Stage — first publication of persona garden content
**Source garden**: Private Obsidian vault with [deep context](glosses/Deep%20Context%20as%20Shared%20Language.html) architecture
