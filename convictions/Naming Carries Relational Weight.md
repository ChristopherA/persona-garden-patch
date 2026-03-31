---
created: 2026-03-31
author: Christopher Allen
brief_summary: "Naming in typed-predicate architectures is an architectural choice that teaches the model what a thing is and how it relates. Choosing a term for a concept, role, or system encodes relational semantics that shape every downstream inference — name choices are load-bearing, not decorative."
tagline: "Every name teaches the model — naming is architecture, not labeling"
---

- is_a::[Conviction Form](../forms/Conviction%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Naming Carries Relational Weight

## The Conviction

Naming is an architectural choice, not a labeling act. When you name a role, a concept, or a system, you teach every agent and reader how to relate to it. The name activates a web of associations — prior use, etymology, cultural resonance, semantic neighbors — and those associations become the context through which every subsequent inference runs.

In a typed-predicate graph, names are nodes, and node names determine which edges can be drawn. Choosing "estate" over "workspace" or "vault" is not a style preference: it imports a semantic field (stewardship, generational continuity, selective permeability, sovereignty bounded by obligation) that shapes how the architecture is understood and extended. The wrong name imposes the wrong semantic field, and you spend the rest of the project fighting the connotations you chose.

This conviction holds even when — perhaps especially when — the name carries risk.

## Grounding

The 2016 naming of self-sovereign identity is the sharpest test case. Allen chose "self-sovereign" knowing it carried dangerous baggage from the sovereign citizen movement — a fringe legal ideology that claims individuals are exempt from government jurisdiction. The name was genuinely hazardous. Community members raised the risk immediately. The alternative was some more neutral phrase: "user-owned identity," "decentralized identity," "individual-controlled identity."

Allen chose "self-sovereign" anyway, because it was the only phrase that captured what the concept actually required: individuals as ultimate authorities over their identity, not merely as the center of a system someone else controls. The weaker names would have admitted a weaker concept. The SSI 10 Principles — Control, Portability, Protection — flow from the sovereign framing. A user-owned-identity framing would have produced different principles, less demanding of systems, more accommodating of institutional authority.

The naming risk was real and the naming choice was right. The dangerous connotation had to be carried because the concept required it.

The estate's own naming follows the same logic. The choice of feudal English — estate, steward, gardener, groundskeeper, chamberlain — imports a semantic field of stewardship and generational continuity that the architecture requires. "Vault" (Obsidian's default term) suggests a container to lock things in. "Workspace" suggests a tool. Neither captures the relationship of a person to their accumulated knowledge as something they tend and pass forward. The feudal vocabulary carries its own risks (hierarchy, inaccessibility), but those risks are worth taking because the semantic field is correct.

In typed-predicate systems specifically, this conviction has technical force. [The Persona Selection Model](../models/The%20Persona%20Selection%20Model.html) (Anthropic, 2026) shows that invented role names like "Groundskeeper" activate weaker pretrained patterns than established professional roles like "information architect." Naming maps directly to which behavioral patterns are activated. A poorly chosen name does not just mislead readers — it misroutes the model.

## Implications

- **For the deep context architecture**: Every form type name, every predicate name, every domain name is a semantic commitment. Before introducing a new term, ask: what relational field does this activate? What does this name teach the model about how this thing relates to everything else?
- **For persona design**: Role names activate pretraining patterns. Naming a role "Groundskeeper" imports the semantic field of a person who tends a living system — maintenance, growth, judgment about what to cultivate and what to prune. That field shapes behavioral inference whether or not the persona definition states it explicitly.
- **For the least authority principle**: [[Allen (2023) Least and Necessary Design Patterns]]↑ grounds least authority in the observation that privileges form a web of transitive authority. Names are the same: you cannot name something without inheriting a transitive web of associations. Naming with care is a form of architectural least-authority — take only the associations you need, accept the costs of the ones you can't avoid.
- **For vocabulary lifecycle**: A garden that uses precise names for its predicates and form types maintains a shared language community. Imprecise naming produces predicate drift — `related_to` proliferating because the more specific predicates were never clearly named.

## Sources

- Allen, C. (2016). [[Allen (2016) The Path to Self-Sovereign Identity]]↑ — naming SSI knowing the sovereign citizen risk
- Allen, C. (2023). [[Allen (2023) Origins of Self-Sovereign Identity]]↑ — retrospective on why "sovereign" was necessary despite the hazard
- Allen, C. (2023). [[Allen (2023) Least and Necessary Design Patterns]]↑ — transitive authority webs as analog for naming's semantic transitivity
- [The Persona Selection Model](../models/The%20Persona%20Selection%20Model.html) — empirical evidence that role names activate different pretraining patterns
- [Deep Context Graph Vocabulary](../glosses/Deep%20Context%20Graph%20Vocabulary.html) — the vocabulary that naming choices instantiate

## Relations

- relates_to::[[Values Precede Technical Decisions]]↑
  - Naming is a values-first technical decision — what a thing is called encodes what we believe it is
- relates_to::[[Allen (2023) Least and Necessary Design Patterns]]↑
  - Least authority's transitive authority principle has a direct analog in naming: every name imports a transitive web of associations
- relates_to::[The Persona Selection Model](../models/The%20Persona%20Selection%20Model.html)
  - The PSM demonstrates that role names activate different pretrained patterns, making naming an architectural choice with measurable downstream effects
- relates_to::[[Shared Language Community]]↑
  - Naming choices are the primary mechanism by which a shared language community coheres — or fragments
- relates_to::[[Vocabulary Lifecycle Through Tending]]↑
  - The conviction that names carry weight implies that vocabulary needs tending — precision maintained over time, not just at initial definition
- relates_to::[Feudal English Over Latin or Corporate Terms](../decisions/Feudal%20English%20Over%20Latin%20or%20Corporate%20Terms.html)
  - The decision that instantiates this conviction for the estate's own naming
- relates_to::[Vocabulary Collision Navigation](../patterns/Vocabulary%20Collision%20Navigation.html)
  - The pattern for when multiple naming traditions converge — this conviction explains why the collision is high-stakes
- relates_to::[[Subtitle Anchoring for Persona Activation]]↑
  - Subtitle anchoring applies this conviction to system prompt design: archetype names activate specific behavioral clusters
- relates_to::[[Scope-Encoded Naming as Authority Boundary]]↑
  - Scope-encoded prefixes carry structural information about authority boundaries — naming as architecture in practice
