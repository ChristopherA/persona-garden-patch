---
created: 2026-03-19
author: Christopher Allen
brief_summary: "An upstream node is a knowledge node that exists in the source garden but was not grafted into a garden patch. It is referenced through predicate links marked with ↑, and its summary is documented on the Node Directory page. The source garden is 'upstream' — the origin from which knowledge flows into the patch."
tagline: "A node that exists in the source garden but was not grafted into this patch"
---

- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Upstream Node as Source Garden Reference

A garden patch is a fragment of a larger garden. It cannot contain every node the source garden has — that would make it a full garden, not a patch. When a node references something that exists in the source garden but was not included in the patch, that reference is an **upstream node**.

The term borrows from version control: the source garden is "upstream" — the origin from which knowledge flows into the patch. An upstream node has known provenance (we know where it is and what it says) but is not present for direct navigation.

## How Upstream Nodes Appear

Links to upstream nodes are marked with **↑** and are clickable — they navigate to the upstream section of the Node Directory, which documents each upstream node's name, form type, and brief summary from the source garden. This gives readers enough context to understand the reference without needing access to the source garden.

The ↑ marker distinguishes upstream nodes from:
- **Grafted nodes** (clickable without a marker — copied from source garden, present in the patch)
- **[Patch-native nodes](Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html)⊙** (clickable with ⊙ — born in this patch)
- **[Ghost links](Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html)** (plain text, not clickable — the node does not exist yet)

## Why Not Include Everything

A garden patch is deliberately selective. Including every referenced node would cascade indefinitely — each included node references more nodes, and so on. The patch boundary is a design decision: graft the nodes needed for the patch to be self-contained and legible, document the rest as upstream references.

## Sources

- First articulated in the Inter-Face Protocol garden patch (March 2026). Marker changed from ⊙ to ↑ when ⊙ was reassigned to patch-native nodes.

## Relations

- relates_to::[\[\[Garden Patch as Composable Knowledge Fragment\]\]](Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)
  - Upstream nodes define the boundary of what a patch includes.

- relates_to::[\[\[Grafted Node as Transplanted Knowledge in a Garden Patch\]\]](Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)
  - The complement: grafted nodes are present, upstream nodes are referenced.

- relates_to::[\[\[Patch-Native Node as Original Knowledge in a Garden Patch\]\]](Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html)
  - Patch-native nodes exist in the patch but not in the source garden — the opposite direction from upstream.

- relates_to::[\[\[Ghost Link as Unplanted Garden Stake\]\]](Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html)
  - Ghost links are the fourth category — no node exists yet, unlike upstream nodes which exist but elsewhere.

- relates_to::[[Progressive Disclosure Over Eager Loading]]↑
  - The Node Directory is progressive disclosure — enough context to understand the reference, with the full node available when the source garden publishes.
