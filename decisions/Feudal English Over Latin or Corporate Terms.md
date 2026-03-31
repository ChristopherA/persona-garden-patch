---
created: 2026-03-31
author: Christopher Allen
status: accepted
brief_summary: "This estate chose feudal English vocabulary (estate, steward, gardener, chamberlain, groundskeeper) over Victoria Gracia's Latin namespace (nos, agens, fidelis-est) and corporate hierarchy terms (manager, director, team lead). Four reasons: wiki gardening origins, stewardship metaphor alignment, common law heritage, and sovereignty-with-obligation awareness. The naming 'Self-Sovereign Estate' demonstrates its own thesis."
tagline: "Feudal English over Latin precision — stewardship and sovereignty over management and control"
---

- is_a::[Decision Form](../forms/Decision%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Feudal English Over Latin or Corporate Terms

## Context

Every multi-agent knowledge system needs vocabulary for its roles, structures, and relationships. The vocabulary choice is architectural: it activates semantic fields that shape how agents, designers, and human collaborators understand what everything is and how it relates.

Three vocabulary families were available:

**Feudal English** (estate, steward, gardener, groundskeeper, chamberlain, seneschal, precinct) — the vocabulary of medieval land management and governance, filtered through common law and wiki-gardening culture. Already present in the project's origins as a knowledge garden.

**Latin namespace** — Victoria Gracia's [Gracia (2026) Uni-Versum Personal Knowledge Architecture](../citations/Gracia%20%282026%29%20Uni-Versum%20Personal%20Knowledge%20Architecture/Gracia%20%282026%29%20Uni-Versum%20Personal%20Knowledge%20Architecture.html) deliberately chose Latin for its namespace-isolation properties: English words carry connotations from prior tool use ("workspace" means different things in Slack, VS Code, and Notion); Latin terms arrive without baggage. Her vocabulary includes nos (the human perspective center), agens (any agent), fidelis-est (loyalty/allegiance), autonomia (delegated trust contract), diploma (inter-system trust credential).

**Corporate hierarchy** (manager, director, team lead, report, task owner) — the vocabulary of organizational management software and agile methodology.

## Decision

Use feudal English for the estate's primary vocabulary. Keep Latin terms as a reference vocabulary where Gracia's precise trust semantics (fidelis-est, autonomia, diploma) add analytical depth, but do not adopt Latin as the estate's operating namespace. Reject corporate hierarchy terms entirely.

## Consequences

**Positive consequences:**

*Stewardship metaphor imports the right semantic field.* "Estate" implies something held in trust across time — managed for a purpose beyond the holder's immediate needs, capable of outlasting any single caretaker. "Vault" suggests secure containment. "Workspace" suggests a tool that serves the current task. "Estate" activates the idea of tending, growing, and passing forward — which is what a personal knowledge system actually is.

*Gardening origins honored.* The digital garden metaphor — wiki culture, growing nodes, tending knowledge — is already established in the project and in the broader PKM community. Feudal English extends that metaphor naturally: an estate has gardens; gardens have groundskeepers and cultivators; the whole is more than any single planting.

*Common law heritage captures sovereignty-with-obligation.* Feudal sovereignty was never absolute control — it was sovereignty within a web of mutual obligation (lord to vassal, vassal to serf, all to the common law). This maps to the estate's own design: sovereignty is selective permeability, not absolute control. The estate is a membrane that negotiates with its environment. "Sovereign" without "feudal" would suggest the wrong kind of sovereignty.

*"Self-Sovereign Estate" demonstrates its own naming thesis.* The compound name encodes both the sovereignty framework (self-sovereign, from Allen's 2016 SSI work) and the architectural scope (estate, with all its tending and stewardship connotations). Choosing this name was itself an architectural act — it prevents the system from being misread as either a mere tool (workspace) or an absolute authority (sovereign without obligation).

**Negative consequences:**

*Accessibility barrier.* "Seneschal" and "chamberlain" are unfamiliar words. New collaborators need to learn the vocabulary before they can participate in design conversations. The Latin alternative would have the same problem; corporate terms would not.

*Feudal eras were brutal.* The vocabulary imports a semantic field that includes serfdom, conquest, and class violence alongside stewardship. This is the naming risk parallel to "self-sovereign" carrying sovereign-citizen baggage: the right semantic field comes attached to a dangerous historical record. The decision accepts this cost.

*Apparent hierarchy.* Feudal vocabulary connotes rank and hierarchy. The estate is not a hierarchy in the corporate sense — it is a set of functional roles in one person's sovereignty — but the vocabulary does not prevent hierarchical misreading.

## Alternatives Considered

**Victoria Gracia's Latin namespace**: Gracia's vocabulary has significant advantages: formal precision (each term has one meaning, mapped to SKOS/RDFS/JSON-LD standards), namespace isolation (no prior-tool connotations), and a rich trust vocabulary (fidelis-est, autonomia, diploma) that the estate's own vocabulary lacks. The Latin terms are adopted as a reference vocabulary because this trust vocabulary is genuinely superior for its semantic domain. The decision against adopting Latin as the estate's primary namespace: the accessibility cost is higher (41 technical terms versus a dozen familiar feudal words), and the stewardship metaphor that feudal English imports is the right frame for a personal knowledge estate's human relationship to their accumulated knowledge. Gracia's vocabulary is optimized for machine-readable ontology; feudal English is optimized for human conceptual grounding.

**Corporate hierarchy terms**: Rejected on connotation grounds. "Manager" implies a principal-agent employment relationship — authority delegated downward, accountability flowing upward, roles defined by organizational position. The estate's roles are functional specializations in one person's sovereignty: a groundskeeper is not a manager of the garden, but a person with knowledge and judgment about what the garden needs. Corporate vocabulary would misframe every design conversation about role authority, escalation, and decision rights. The estate's agents are augmentations, not employees.

## Relations

- implements::[Naming Carries Relational Weight](../convictions/Naming%20Carries%20Relational%20Weight.html)
  - This decision is the instantiation of the conviction: choosing feudal English over available alternatives because the semantic field it imports is architecturally necessary
- relates_to::[Gracia (2026) Uni-Versum Personal Knowledge Architecture](../citations/Gracia%20%282026%29%20Uni-Versum%20Personal%20Knowledge%20Architecture/Gracia%20%282026%29%20Uni-Versum%20Personal%20Knowledge%20Architecture.html)
  - The Latin alternative considered and partially adopted for its trust vocabulary (fidelis-est, autonomia, diploma)
- relates_to::[[Sovereignty Is Selective Permeability Not Absolute Control]]↑
  - The feudal-sovereignty-with-obligation semantics ground this conviction's membrane model of sovereignty
- relates_to::[[Allen (2016) The Path to Self-Sovereign Identity]]↑
  - "Self-sovereign" in the estate name draws from Allen's 2016 framing — sovereignty as authority sufficient to negotiate as a peer, not absolute control
- relates_to::[[Shared Language Community]]↑
  - Vocabulary choice creates or fragments shared language communities — this decision defines which semantic community the estate belongs to
- relates_to::[[Digital Garden as Growth Ethos]]↑
  - The estate vocabulary extends the digital garden metaphor that this gloss establishes
- relates_to::[Vocabulary Collision Navigation](../patterns/Vocabulary%20Collision%20Navigation.html)
  - This decision is one strategy (semantically rich loaded tradition) within the broader collision navigation pattern
- extended_by::[[Subtitle Anchoring for Persona Activation]]↑
  - Medieval names require archetype subtitles because feudal English terms are thinner in pretraining data than professional archetypes
- extended_by::[[Scope-Encoded Naming as Authority Boundary]]↑
  - Scope prefixes (Estate, Garden, Household) extend feudal English naming with authority-boundary encoding
