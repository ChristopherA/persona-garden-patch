---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Pruned Stage: a garden node no longer current but preserved rather than deleted. Pruning replaces deletion so that link chains and reasoning history remain traceable. Uses superseded_by:: predicates to point to replacements. Lowest retrieval priority among all growth stages."
tagline: "No longer current but preserved — the garden's way of retiring without deleting"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Pruned Stage

A pruned node is no longer current but is preserved rather than deleted. The garden metaphor is deliberate: pruning removes what no longer serves growth while keeping the plant (the knowledge graph) healthy. Pruned nodes maintain their links and predicates so the reasoning chain that led through them remains traceable.

Pruning replaces deletion. A node that was once useful contributed to the graph's development — removing it breaks link chains and erases the record of how understanding evolved. Instead, pruning marks the node as superseded and points to its replacement.

## Characteristics

- Content intact but no longer maintained or updated
- `superseded_by::[[Replacement Form]]↑` predicate present when a specific successor exists
- Existing inbound links preserved (other nodes may still reference the pruned node for historical context)
- Lowest retrieval priority — agents should not cite pruned nodes when a current alternative exists
- May retain value as historical record of how a decision was first framed or how understanding changed

## When to Prune

- A newer node covers the same topic with better structure or more current information
- Domain changes make the node's claims no longer applicable
- Extraction produced a duplicate that a better node now covers
- A seed node never developed and is not worth growing

## Sources

Originally `status/archived` in the architecture document; renamed to "Pruned Stage" in the garden-foundation workstream to match the garden metaphor and the two-word minimum naming convention. Growth stage definitions from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Growth Stages as Lifecycle Metadata" section.

## Relations

- relates_to::[\[\[Seed Stage\]\]](Seed%20Stage.html) — seeds may be pruned before ever growing
- relates_to::[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html) — evergreen nodes transition to pruned when superseded
- relates_to::[[Structural Retrieval Hierarchy]]↑ — pruned nodes rank below all active stages
