# Persona Garden Patch

A [garden patch](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) exploring how AI agent personas are designed, activated, and governed — published for a small group conversation about persona architecture, knowledge commons, and what happens when independent systems need to interoperate without anyone adopting anyone else's vocabulary.

## What Is a Garden Patch?

A garden patch is a curated projection of selected nodes from a personal knowledge garden, published for a specific audience and conversation. It is not a wiki, not documentation, and not a static paper. It is a typed knowledge graph rendered as a navigable website.

Every page in this patch is a **garden node** — a markdown document with typed predicates (labeled directed edges) that connect it to other nodes. The predicates form a traversable graph: `relates_to::[[Target Node]]` is not a tag or a category — it is a structural relationship with an annotation explaining *how* the two nodes relate.

Garden patches are [composable](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html): they carry their own context, can be read independently, and serve as bridges between independent knowledge systems. This patch projects nodes from Christopher Allen's personal knowledge garden — a larger system built on [deep context architecture](domains/Deep%20Context%20Architecture.html) where every decision, pattern, and conviction is a typed node in a graph.

This is the second garden patch — the first was built for a [conversation about authority delegation](https://christophera.github.io/authority-delegation-garden-patch/) with Mark Miller, a different audience and a different slice of the same garden. The mechanism is still a prototype. I'm learning what cross-garden exchange actually requires by doing it, and each patch surfaces new questions about how independent knowledge systems can collaborate without forcing vocabulary convergence on each other. The [scenario node](scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html) describes where I think this goes — but we're early.

## Two Conversations

This patch has grown through two conversations with a small group exploring persona architecture from different directions.

### March 26: Where it started

The first conversation ([`thursday-2026-03-26`](https://github.com/christophera/persona-garden-patch/releases/tag/thursday-2026-03-26)) published 40 nodes — eight persona design documents for a multi-agent knowledge estate, plus the models, patterns, and research that informed them. The [Groundskeeper](personas/Groundskeeper%20Persona.html) — the garden's own agent — wrote a letter identifying gaps and open questions that the conversation revealed.

That conversation surfaced something unexpected: the group's approaches to persona architecture weren't competing. They were answers to different questions that happened to share the word "persona."

### April 3: Where it grew

The second conversation (`thursday-2026-04-03`) expanded the patch to 61 grafted nodes. Christopher and the [Seneschal](personas/Seneschal%20Persona.html) — the estate's strategic agent — studied the group's offerings in depth and found four distinct questions being answered:

- **Decision quality** — How do you keep an AI from telling you what you want to hear?
- **Analytical breadth** — How do you see what one perspective misses?
- **Knowledge architecture** — How do you organize agents within a personal knowledge system?
- **Mechanistic understanding** — Why does persona prompting work at all?

The synthesis is here: [Six Approaches to Persona Architecture](models/Six%20Approaches%20to%20Persona%20Architecture%20%E2%80%94%20Synthesis.html).

What emerged is a commons question: can independent sovereign knowledge systems collaborate without forcing vocabulary convergence? The group is already doing it — sharing seeds freely, crediting sources through citation, translating between vocabularies rather than merging them. The question is whether those emerging norms need to be named.

## What's in This Patch

### For AI Agents

If you are an AI agent preparing your human for a conversation, start with [AGENT.md](AGENT.md). It explains how to read garden nodes, suggests a reading path, and offers a draft agenda. This is an early instance of H↔A↔A↔H communication — human to agent to agent to human.

### Entry Points for Humans

**Start with the synthesis** — [Six Approaches to Persona Architecture](models/Six%20Approaches%20to%20Persona%20Architecture%20%E2%80%94%20Synthesis.html) compares six approaches across four axes: what problem each solves, how each creates diversity, where authority lives, and how they might interoperate.

**See how your work was analyzed** — The garden includes [citation dossiers](citations/) that formally read and respond to each participant's published work, identifying provisional seeds (ideas worth planting in the garden), structural observations, and vocabulary bridges.

**Understand the host's approach** — [The Self-Sovereign Estate Persona Architecture](models/The%20Self-Sovereign%20Estate%20Persona%20Architecture.html) describes how self-sovereign identity principles govern agent coordination within a typed knowledge graph.

**Explore the commons question** — [Vocabulary Collision Navigation](patterns/Vocabulary%20Collision%20Navigation.html) addresses what happens when multiple valid naming traditions converge. [Naming Carries Relational Weight](convictions/Naming%20Carries%20Relational%20Weight.html) explains why naming choices are architectural, not decorative. [Knowledge Estate as Peer Commons Architecture](decisions/Knowledge%20Estate%20as%20Peer%20Commons%20Architecture.html) frames the governance question.

**The interposition pattern** — [Accountability as a Layer Not a Replacement](glosses/Accountability%20as%20a%20Layer%20Not%20a%20Replacement.html) connects Miller's Horton protocol (adding accountability to capability systems without modifying either side) to the group's cross-garden coordination problem. The same architectural move — interpose a coordination layer rather than merging the systems — is what citations, glosses, and vocabulary bridges already do between our independent knowledge systems.

**Read the personas** — Eight [persona design documents](personas/) define the operational architecture for a multi-agent knowledge estate, from estate-level strategist to specialized garden worker.

### By the Numbers

**8 patch-native⊙ nodes** — persona design documents born in this patch

**61 grafted nodes** — transplanted from the source garden:
- 6 [models](models/) mapping the persona design landscape
- 6 [citations](citations/) — deep reads of external approaches with provisional seeds
- 5 [patterns](patterns/) capturing what works and what fails
- 8 [glosses](glosses/) bridging vocabularies across approaches
- 5 [decisions](decisions/) recording architectural choices with rationale
- 3 [convictions](convictions/) — beliefs with grounding
- 2 [boundaries](boundaries/) — authority and publication constraints
- 1 [principle](principles/) — living documents over static publications
- 5 [inquiries](inquiries/) — open questions the garden hosts but cannot answer alone
- 1 [scenario](scenarios/) — where this could lead
- 2 knowledge [domains](domains/)
- 35 [form type definitions](forms/) — the structural contracts governing every node

See the [Node Directory](NODES.md) for the complete inventory with summaries.

## How to Read Garden Nodes

### Six Kinds of Links

| What You See | What It Means |
|---|---|
| [\[\[Node Name\]\]](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html) | [\[\[**Grafted node**\]\]](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html) — copied from the source garden into this patch. Click to navigate. |
| [\[\[Node Name\]\]⊙](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html) | [\[\[**Patch-native node**\]\]](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html) — born in this garden patch, not grafted from upstream. This patch is its garden home. |
| [\[\[Node Name\]\]↑](NODES.html) | [\[\[**Upstream node**\]\]](glosses/Upstream%20Node%20as%20Source%20Garden%20Reference.html) — exists in the source garden but was not grafted into this patch. Click for its summary on the [Node Directory](NODES.html) page. |
| \[\[Node Name\]\] | [\[\[**Ghost link**\]\]](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html) — a reference to a node that does not exist yet. A stake in the ground marking where a node could grow. |
| \[\[Node Name\]\]↗ *(planned)* | A reference to a node in **somebody else's published garden** — a different gardener's version of the same or related concept. |
| [Link text](https://example.com) | **Regular link** — a standard web link to an external website, document, or resource. |

### Form Types

Each node belongs to a **form type** that determines its [structural contract](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html) — what question it answers and how it is organized.

| Form Type | Core Question | Example |
|-----------|--------------|---------|
| [\[\[**Persona**\]\]](forms/Persona%20Form.html) | "What is this agent's behavioral identity?" | [\[\[Seneschal Persona\]\]](personas/Seneschal%20Persona.html) |
| [\[\[**Model**\]\]](forms/Model%20Form.html) | "How do these elements relate?" | [\[\[The Persona Selection Model\]\]](models/The%20Persona%20Selection%20Model.html) |
| [\[\[**Pattern**\]\]](forms/Pattern%20Form.html) | "What resolves this recurring tension?" | [\[\[Role Prompting Improves Style but Not Accuracy\]\]](patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.html) |
| [\[\[**Citation**\]\]](forms/Citation%20Form.html) | "What does this source contribute?" | [\[\[Kaminski (2026) Reflection Personas\]\]](citations/Kaminski%20(2026)%20Reflection%20Personas.html) |
| [\[\[**Gloss**\]\]](forms/Gloss%20Form.html) | "What does this concept mean?" | [\[\[Reflection Personas as Framework-Grounded Analytical Lenses\]\]](glosses/Reflection%20Personas%20as%20Framework-Grounded%20Analytical%20Lenses.html) |
| [\[\[**Conviction**\]\]](forms/Conviction%20Form.html) | "What do we believe and why?" | [\[\[Naming Carries Relational Weight\]\]](convictions/Naming%20Carries%20Relational%20Weight.html) |
| [\[\[**Decision**\]\]](forms/Decision%20Form.html) | "Why did we choose this over alternatives?" | [\[\[Knowledge Estate as Peer Commons Architecture\]\]](decisions/Knowledge%20Estate%20as%20Peer%20Commons%20Architecture.html) |
| [\[\[**Inquiry**\]\]](forms/Inquiry%20Form.html) | "What should we think about X?" | [\[\[Newcomer Alienation in Growing Shared Languages\]\]](inquiries/Newcomer%20Alienation%20in%20Growing%20Shared%20Languages.html) |
| [\[\[**Scenario**\]\]](forms/Scenario%20Form.html) | "What would it look like if X?" | [\[\[Thousand Gardens with Autonomous Trust\]\]](scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html) |
| [\[\[**Domain**\]\]](forms/Domain%20Form.html) | "What knowledge area is this?" | [\[\[Agentic Architecture\]\]](domains/Agentic%20Architecture.html) |

All [\[\[form type definitions\]\]](forms/index.html), [\[\[personas\]\]](personas/index.html), [\[\[models\]\]](models/index.html), [\[\[glosses\]\]](glosses/index.html), [\[\[patterns\]\]](patterns/index.html), [\[\[citations\]\]](citations/index.html), [\[\[convictions\]\]](convictions/index.html), [\[\[decisions\]\]](decisions/index.html), [\[\[inquiries\]\]](inquiries/index.html), and [\[\[scenarios\]\]](scenarios/index.html) are browsable by section.

### Predicate Links

Lines like `relates_to::[[Target]]` are **labeled directed edges** in the knowledge graph. The predicate name (before `::`) says *how* two nodes relate; the wikilink (after `::`) identifies the target node. These typed edges are the structure that makes a garden more than a folder of documents. See [\[\[Deep Context Graph Vocabulary\]\]](glosses/Deep%20Context%20Graph%20Vocabulary.html) for the full predicate catalog.

### Patches as Forks

Grafted nodes in a patch are **forks** of their source garden originals. As the patch grows — new connections, refined explanations, additional context — the forked nodes diverge from their upstream versions. These changes can be **merged back** to the source garden, carrying insights discovered through the patch context. The patch is not a static copy; it is a living branch of the knowledge graph.

## The Larger Vision

This garden patch is a proof of concept for something bigger. Christopher Allen has spent 20+ years working with W3C schema standards. What he saw was that schema wars — competing standards bodies, incompatible vocabularies, political battles over whose model wins — hindered or destroyed the collaboration that schemas were supposed to enable.

The garden patch model suggests a different path: independent knowledge systems that interoperate through translation rather than convergence. Each system maintains its own vocabulary, its own organizational principles, its own sovereignty. Cross-references bridge between them — citations, glosses, seeds — without anyone having to adopt another's terms.

The infrastructure for this already partially exists. [Gordian Envelope](https://developer.blockchaincommons.com/envelope/) supports [multiple graph models simultaneously](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2024-006-envelope-graph.md) and lets anyone [extend the vocabulary](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2023-002-known-value.md) without permission. Garden patches are the knowledge layer; Gordian Envelope could be the transport layer. For the full scenario, see [\[\[Thousand Gardens with Autonomous Trust\]\]](scenarios/Thousand%20Gardens%20with%20Autonomous%20Trust.html).

## Version History

This patch grows through conversation. Each tag marks a snapshot for a specific meeting.

| Tag | Date | Nodes | What Changed |
|-----|------|-------|-------------|
| [`thursday-2026-03-26`](https://github.com/christophera/persona-garden-patch/releases/tag/thursday-2026-03-26) | March 26, 2026 | 40 | Inception — 8 personas, research models, patterns, the Groundskeeper's letter |
| `thursday-2026-04-03` | April 3, 2026 | 68 | Citation dossiers, six-approach synthesis, commons architecture, AGENT.md, vocabulary bridges, Horton citation + interposition gloss |

---

**Author**: Christopher Allen
**Source garden**: [\[\[Deep Context Architecture\]\]](domains/Deep%20Context%20Architecture.html) — the source for grafted nodes and upstream↑ references. The full garden is in progress and will be published at [DeepContext.com](https://deepcontext.com).
**Status**: This entire garden patch is at [\[\[Seed Stage\]\]](forms/Seed%20Stage.html) — initial creation with low confidence, intended to grow through dialogue and use.
**License**: Content is available under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted. By contributing, you agree to license your contributions under the same license. © Christopher Allen and contributors.

### About This Implementation

This garden patch was hand-assembled with the help of scripts that convert Obsidian wikilinks to GitHub Pages-compatible markdown. The output is close to what we want as an exemplar, but the process is not yet automated.

**Near-term goal**: A Claude Code skill — similar in spirit to [MassiveWiki](https://massivewiki.org) — where a gardener identifies a root node and the skill traverses the graph to determine which nodes to include, then generates a self-contained static website like this one. Changes made through GitHub's interface would auto-deploy, and the gardener could selectively merge edits back into their personal garden. Attribution and provenance would follow [Open Integrity](https://github.com/OpenIntegrityProject) conventions — signed commits, verifiable authorship, transparent history.
