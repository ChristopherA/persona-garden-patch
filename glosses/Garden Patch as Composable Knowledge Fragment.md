---
created: 2026-03-19
author: Christopher Allen
brief_summary: "A garden patch is a portable, self-contained subset of a garden placed alongside external content to reveal connections through typed knowledge forms. It carries grafted nodes (copied from the source garden), patch-native nodes⊙ (born in the patch), form definitions, and a node directory. Patches function as forks — they diverge from the source garden as they grow, and changes can merge back upstream."
tagline: "A portable garden fork that reveals connections in external content through typed knowledge forms"
---

- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Garden Patch as Composable Knowledge Fragment

A garden patch is a **self-contained collection of garden nodes** placed alongside external content — a specification, a codebase, a document set — to reveal connections through the garden lens without modifying the original content. The patch does not critique or replace what it sits alongside; it offers a **dialogue** — showing how the same ideas look through typed knowledge forms.

## What a Patch Contains

A patch carries everything needed to read it:

- **Form type definitions** — [structural contracts](Structural%20Contract%20as%20Form%20Type%20Agreement.html) for every form type used
- **Domain pages** — knowledge areas that cross-cut the nodes
- **[Grafted nodes](Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)** — copies from the source garden, adapted for the patch context
- **[Patch-native nodes](Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html)⊙** — new nodes seeded from the external content, marked with ⊙
- **Citations** — with canonical URLs pointing to source works
- **A node directory** — complete listing of every node by provenance (grafted, patch-native⊙, upstream↑)

## Six Kinds of Links

A patch uses six link types to distinguish provenance and availability:

| Link | Meaning |
|---|---|
| `[[Node Name]]↑` | **Grafted** — present in patch, copied from source garden |
| `[[Node Name]]↑⊙` | **Patch-native** — present in patch, born here |
| `[[Node Name]]↑` | **Upstream** — in source garden, not in patch |
| `[[Node Name]]↑` (plain text) | **Ghost link** — does not exist yet |
| `[[Node Name]]↗` | **Cross-garden** — in another gardener's published garden |
| `[text](url)` | **Regular link** — external web resource |

These markers encode provenance at the point of reference, so a reader always knows where a concept lives and whether they can navigate to it.

## Patches as Forks

A garden patch functions like a **git fork** of the source garden. Grafted nodes start as copies but diverge as the patch grows — new connections to the target content, refined explanations, additional context. These changes can be **merged back** to the source garden, carrying insights discovered through application.

Patch-native nodes⊙ may also flow upstream. A gloss or model created to interpret external content may prove valuable beyond the patch context. The patch is not a static excerpt; it is a living branch of the knowledge graph.

## Composability

Patches are composable fragments. Two patches from different source gardens can coexist in the same repository. The form type system ensures structural compatibility — a [\[\[Model Form\]\]](../forms/Model%20Form.html) in one patch follows the same [structural contract](Structural%20Contract%20as%20Form%20Type%20Agreement.html) as a Model Form in any other garden. A patch author's interpretation is distinct from the source garden's authority, and the markers make this visible.

## Sources

- The Inter-Face Protocol garden patch — the first instance of a garden patch applied to external specifications
- Dialogue between Christopher Allen and Peter Kaminski (March 2026) on garden scale, patch mechanics, and collaborative knowledge work

## Relations

- relates_to::[[Content Over Container]]↑
  - A patch carries content (nodes and edges) without depending on a specific container (the source vault).

- relates_to::[[Progressive Disclosure Over Eager Loading]]↑
  - A patch loads only the nodes needed for its context, not the entire source garden.

- relates_to::[[Knowledge Compounds Through Typed Edges Not Filing]]↑
  - A patch's value comes from the typed edges between nodes, not from the folder structure.

- relates_to::[\[\[Neobooks as Composable Knowledge Objects\]\]](Neobooks%20as%20Composable%20Knowledge%20Objects.html)
  - Garden patches are one implementation of the neobooks concept — portable, composable, shareable knowledge fragments.

- relates_to::[[Thousand Gardens with Autonomous Trust]]↑
  - The scenario for where garden patches lead when combined with content-addressable nodes and progressive trust.
