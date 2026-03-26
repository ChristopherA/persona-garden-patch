# Persona Garden Patch

A [garden patch](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) exploring how AI agent personas are designed, activated, and governed — and what happens when the design document becomes a first-class knowledge node rather than a configuration file.

## Why a Persona Garden Patch?

Agent systems need personas. Most approaches treat them as configuration: a system prompt, a YAML file, a role string. The persona is consumed by the runtime and invisible to everyone else.

This [garden patch](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) asks: what if the persona were a knowledge artifact? One that carries its own design rationale, declares its blind spots, references the research that shaped it, and participates in a typed knowledge graph alongside the models, patterns, and inquiries that inform it.

The eight personas here — from estate-level strategist to specialized garden worker — are not documentation *about* agents. They are the design authority *for* agents. Each persona node defines behavioral scope, declared blind spots, operational architecture, and relationships to peer personas. The agent configuration files are downstream artifacts that implement what the persona specifies.

This distinction matters because it makes persona design auditable, composable, and evolvable through the same mechanisms that govern any other knowledge node: [structural contracts](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html), status stages, typed predicates, and peer review.

## Garden Patches as Conversation

A garden patch is not just a portable fork of a source garden — it is a record of intellectual conversation. This patch grew from an ongoing dialogue between Christopher Allen and Peter Kaminski about how AI agent personas should work.

Peter brought 27 reflection personas he designed for his course — diverse cultural perspectives, deliberately not "a cheap pastiche thing." Victoria Gracia, one of Peter's course stewards, independently built compound personas with full cultural context documents. Christopher brought a decade of work on identity, trust, and typed knowledge systems. The conversation produced a shared conviction: persona should become a first-class knowledge form, not remain a configuration file.

Some nodes in a garden patch belong to the source garden — they existed before the conversation and will persist after it. Others belong to the conversation itself. The eight persona nodes here started as patch-native explorations and were adopted by the source garden. But in the [\[\[IFP garden patch\]\]](https://christophera.github.io/ifp/garden/) — the first garden patch, placed alongside Peter's Inter-Face Protocol specifications — patch-native nodes like "Gossip as Social Sensing Filter" and "Conversation Temperature as Protocol Cadence Spectrum" belong to neither garden alone. They emerged from dialogue and the patch is their home.

This raises an [\[\[open question\]\]](inquiries/Where%20Do%20Patch-Native%20Nodes%20Live%20After%20They%20Grow.html): when a node is born in a patch, does it stay there or get adopted upstream? And what about nodes that belong to the conversation between gardeners rather than to any single garden?

## What's in This Patch

**8 persona design documents** (patch-native⊙) — the operational architecture for a multi-agent knowledge estate:
- Orchestrators: [\[\[Seneschal Persona|Seneschal\]\]](personas/Seneschal%20Persona.html), [\[\[Groundskeeper Persona|Groundskeeper\]\]](personas/Groundskeeper%20Persona.html), [\[\[Chancellor Persona|Chancellor\]\]](personas/Chancellor%20Persona.html)
- Boundary guardian: [\[\[Chatelaine Persona|Chatelaine\]\]](personas/Chatelaine%20Persona.html)
- General worker: [\[\[Gardener Persona|Gardener\]\]](personas/Gardener%20Persona.html)
- Specialized workers: [\[\[Cultivator Persona|Cultivator\]\]](personas/Cultivator%20Persona.html), [\[\[Forager Persona|Forager\]\]](personas/Forager%20Persona.html), [\[\[Pruner Persona|Pruner\]\]](personas/Pruner%20Persona.html)

**16 research-extracted nodes** (grafted from source garden) — the analytical framework:
- 6 models mapping the persona design landscape
- 5 patterns capturing what works and what fails
- 2 glosses defining key concepts
- 4 open inquiries about portability, evaluation, persona-to-agent sync, and patch-native node lifecycle

**11 infrastructure nodes** (grafted) — the garden system itself:
- How to read garden patches, nodes, and predicates
- What [precincts](glosses/Garden%20Precinct.html), [structural contracts](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html), and [ghost links](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html) are
- Why this architecture exists

**2 decisions** (grafted) — [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), and [\[\[Persona Nodes as Design Authority for Agent Configuration\]\]](decisions/Persona%20Nodes%20as%20Design%20Authority%20for%20Agent%20Configuration.html)

**1 scenario** (grafted) — [\[\[Thousand Gardens with Autonomous Trust\]\]](scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html)

**2 knowledge domains** — Agentic Architecture and Deep Context Architecture

**35 form type definitions** (grafted) — the structural contracts that govern every node

## Three Ways to Read This

**Start with the personas** — read [Seneschal Persona](personas/Seneschal%20Persona.md) for the most complete example, then [Groundskeeper Persona](personas/Groundskeeper%20Persona.md) to see how personas relate to each other.

**Start with the research** — read [The Persona Selection Model](models/The%20Persona%20Selection%20Model.md) to understand how LLMs activate persona patterns, then [Role Prompting Improves Style but Not Accuracy](patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.md) for what role prompting actually does.

**Start with the system** — read [Garden Patch as Composable Knowledge Fragment](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.md) to understand what you're looking at, then the [Node Directory](NODES.md) for the full inventory.

## How to Read Garden Nodes

### Six Kinds of Links

| What You See | What It Means |
|---|---|
| [\[\[Node Name\]\]](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html) | [\[\[**Grafted node**\]\]](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html) — copied from the source garden into this patch. Click to navigate. |
| [\[\[Node Name\]\]⊙](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html) | [\[\[**Patch-native node**\]\]](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html) — born in this garden patch, not grafted from upstream. This patch is its garden home. |
| [\[\[Node Name\]\]↑](NODES.html) | [\[\[**Upstream node**\]\]](glosses/Upstream%20Node%20as%20Source%20Garden%20Reference.html) — exists in the source garden but was not grafted into this patch. Click for its summary on the [Node Directory](NODES.html) page. |
| \[\[Node Name\]\] | [\[\[**Ghost link**\]\]](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html) — a reference to a node that does not exist yet. A stake in the ground marking where a node could grow. |
| \[\[Node Name\]\]↗ *(planned)* | A reference to a node in **somebody else's published garden** — a different gardener's version of the same or related concept. |
| [Link text](https://example.com) | **Regular link** — a standard web link to an external website, document, or resource. No brackets. |

### Form Types

Each node belongs to a **form type** that determines its [structural contract](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html) — what question it answers and how it is organized.

| Form Type | Core Question | Example |
|-----------|--------------|---------|
| [\[\[**Persona**\]\]](forms/Persona%20Form.html) | "What is this agent's behavioral identity?" | [\[\[Seneschal Persona\]\]](personas/Seneschal%20Persona.html) |
| [\[\[**Model**\]\]](forms/Model%20Form.html) | "How do these elements relate?" | [\[\[The Persona Selection Model\]\]](models/The%20Persona%20Selection%20Model.html) |
| [\[\[**Pattern**\]\]](forms/Pattern%20Form.html) | "What resolves this recurring tension?" | [\[\[Role Prompting Improves Style but Not Accuracy\]\]](patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.html) |
| [\[\[**Gloss**\]\]](forms/Gloss%20Form.html) | "What does this concept mean?" | [\[\[Behavioral Questions vs Identity Assertions in Persona Design\]\]](glosses/Behavioral%20Questions%20vs%20Identity%20Assertions%20in%20Persona%20Design.html) |
| [\[\[**Inquiry**\]\]](forms/Inquiry%20Form.html) | "What should we think about X?" | [\[\[Does the Garden Persona Architecture Need a Portability Layer\]\]](inquiries/Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html) |
| [\[\[**Decision**\]\]](forms/Decision%20Form.html) | "Why did we choose this over alternatives?" | [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) |
| [\[\[**Domain**\]\]](forms/Domain%20Form.html) | "What knowledge area is this?" | [\[\[Agentic Architecture\]\]](domains/Agentic%20Architecture.html) |

All [\[\[form type definitions\]\]](forms/index.html), [\[\[personas\]\]](personas/index.html), [\[\[models\]\]](models/index.html), [\[\[glosses\]\]](glosses/index.html), [\[\[patterns\]\]](patterns/index.html), [\[\[inquiries\]\]](inquiries/index.html), [\[\[decisions\]\]](decisions/index.html), and [\[\[scenarios\]\]](scenarios/index.html) are browsable by section.

### Predicate Links

Lines like `relates_to::[[Target]]` are **labeled directed edges** in the knowledge graph. The predicate name (before `::`) says *how* two nodes relate; the wikilink (after `::`) identifies the target node. These typed edges are the structure that makes a garden more than a folder of documents. See [\[\[Deep Context Graph Vocabulary\]\]](glosses/Deep%20Context%20Graph%20Vocabulary.html) for the full predicate catalog.

### Patches as Forks

Grafted nodes in a patch are **forks** of their source garden originals. As the patch grows — new connections to persona design content, refined explanations, additional context — the forked nodes diverge from their upstream versions. These changes can be **merged back** to the source garden, carrying insights discovered through the patch context. The patch is not a static copy; it is a living branch of the knowledge graph.

## Knowledge Domains

**[Agentic Architecture](domains/Agentic%20Architecture.md)** — How autonomous agents are designed, configured, coordinated, and governed. Most persona and research nodes live here.

**[Deep Context Architecture](domains/Deep%20Context%20Architecture.md)** — The knowledge system architecture itself: typed forms, predicates, precincts, and the design decisions that shaped them.

---

**Author**: Christopher Allen
**Context**: Ongoing dialogue with Peter Kaminski about agency, AI personas, and structured knowledge — building toward a working group with Victoria Gracia and others.
**Source garden**: [\[\[Deep Context Architecture\]\]](domains/Deep%20Context%20Architecture.html) — the source for grafted nodes and upstream↑ references. The full garden is in progress and will be published at [DeepContext.com](https://deepcontext.com).
**Status**: This entire garden patch is at [\[\[Seed Stage\]\]](forms/Seed%20Stage.html) — initial creation with low confidence, intended to grow through dialogue and use.
**License**: Content is available under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted. By contributing, you agree to license your contributions under the same license. © Christopher Allen and contributors.

> "These personas — I tried not to be just a cheap pastiche thing. It wasn't just a parlor trick." — Peter Kaminski, on designing 27 reflection personas for his course — the conversation that sparked this garden patch (March 2026)

> "This should be a first-class form, a garden form, and integrate some of the agent stuff as well." — Christopher Allen, on making persona a knowledge artifact rather than a configuration file (March 2026)

### About This Implementation

This garden patch was hand-assembled with the help of scripts that convert Obsidian wikilinks to GitHub Pages-compatible markdown. The output is close to what we want as an exemplar, but the process is not yet automated.

**Near-term goal**: A Claude Code skill — similar in spirit to [MassiveWiki](https://massivewiki.org) — where a gardener identifies a root node and the skill traverses the graph to determine which nodes to include, then generates a self-contained static website like this one. Changes made through GitHub's interface would auto-deploy, and the gardener could selectively merge edits back into their personal garden. Attribution and provenance would follow [Open Integrity](https://github.com/OpenIntegrityProject) conventions — signed commits, verifiable authorship, transparent history.

**Longer-term vision**: Thousands of gardens flourishing independently, each a personal knowledge system whose nodes are content-addressable — identified by what they contain, not where they are stored. Garden patches become portable, self-contained objects that carry their own permissions and provenance. Gardeners share nodes peer-to-peer with full attribution, make assertions about each other's content, and use [elision](https://developer.blockchaincommons.com/envelope/elision/) to selectively redact sensitive material while cryptographic proofs verify the whole remains intact. [Progressive trust](https://developer.blockchaincommons.com/progressive-trust/) governs how gardens deepen relationships — from anonymous exchange through verified collaboration. [Gordian Envelope](https://developer.blockchaincommons.com/envelope/) provides the infrastructure: autonomous cryptographic objects that work offline, across time, without central servers — infrastructure you control rather than infrastructure that controls you. The result is not a platform but an ecosystem where independent thinkers can cooperate, collaborate, fork, merge, attribute, and build on each other's reasoning while preserving human agency, dignity, and the right to exit.

That ecosystem does not exist yet. This patch is a proof of concept for what it would produce. For the full scenario, see [\[\[Thousand Gardens with Autonomous Trust\]\]](scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html).
