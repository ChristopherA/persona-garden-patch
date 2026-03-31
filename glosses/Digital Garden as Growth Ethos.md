---
created: 2026-03-04
author: Christopher Allen
brief_summary: "Interprets the digital garden movement (Caufield's stream-vs-garden distinction, Appleton's six patterns) as a growth ethos — organic, imperfect, associative knowledge development. Our deep context garden adopts the philosophy but adds formal structure: typed nodes, typed predicates, and structural contracts that most digital gardens lack."
tagline: "The garden metaphor — growth, imperfection, association — informs our philosophy, but we add typed nodes and structural contracts"
---

- is_a::[[Gloss Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]

# Digital Garden as Growth Ethos

**Source**: Maggie Appleton, [A Brief History & Ethos of the Digital Garden](https://maggieappleton.com/garden-history); Mike Caufield, "The Garden and the Stream" (2015)

## Core Distinction

Caufield's 2015 keynote distinguishes two modes of web interaction:

- **The Stream**: Chronological, social, ephemeral (Twitter, blogs, feeds)
- **The Garden**: Topographical, accumulated, evolving (wikis, personal knowledge bases)

A garden organizes by *contextual association*, not by publication date. Notes grow through stages — seedlings, budding, evergreen — and are never "finished."

## Six Patterns (Appleton)

1. Topography over timelines — spatial, associative navigation
2. Continuous growth — ideas evolve over time
3. Imperfection and learning in public — transparent development stages
4. Playfulness and experimentation
5. Content diversity — beyond text
6. Independent ownership — self-hosted, long-term control

## Relationship to Our Architecture

Our deep context garden adopts the garden metaphor directly but adds formal structure that most digital gardens lack:

| Digital Garden Norm | Our Extension |
|--------------------|---------------|
| Growth stages (seedling/budding/evergreen) | `has_status::` predicate (Seed/Growing/Evergreen/Archived) |
| Associative links | Typed predicates with five predicate categories |
| Organic organization | 15 form types with structural contracts |
| Public imperfection | Private vault with agent-assisted maintenance |

Where most digital gardens are loosely structured personal wikis, our garden is a *typed knowledge graph* with formal relationships. The garden ethos informs our philosophy (growth, imperfection, association), but our architecture specifies *what kinds of knowledge exist* and *how they relate*.

## Sources

- [Maggie Appleton: A Brief History & Ethos of the Digital Garden](https://maggieappleton.com/garden-history)
- Mike Caufield, "The Garden and the Stream" (2015)

## Relations

- extracted_from::[[PARA and Variants for PKM Organization]]
  - The Digital Garden Ethos gloss section, lines 282-319.

- relates_to::[[Personal Knowledge Management Organizing Principle Spectrum]]
  - Digital gardens sit at the meaning end of the spectrum, emphasizing associative growth over actionability.

- relates_to::[[Deep Context as an Architecture for Captured Reasoning]]
  - Our architecture extends the garden ethos with formal typed forms and structural contracts.
