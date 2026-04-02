---
created: 2026-04-02
author: Christopher Allen
citation_slug: miller-donnelley-karp-2007-horton
publication_year: 2007
canonical: https://www.usenix.org/legacy/events/hotsec07/tech/full_papers/miller/miller_html/index.html
brief_summary: "Miller, Donnelley, and Karp propose Horton (Higher-Order Responsibility Tracking of Objects in Networks), a protocol that adds identity-based accountability to object-capability systems without sacrificing their proactive safety properties. Horton refutes the longstanding criticism that capability systems cannot support reactive security — who to blame when things go wrong."
tagline: "The protocol that adds accountability to capabilities without sacrificing safety"
---

- is_a::[[Citation Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Agentic Architecture]]
- in_precinct::[[Garden Precinct]]
- cites_work_by::[[Mark S. Miller]]

# Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems

## Bibliographic Entry

* _**Delegating Responsibility in Digital Systems: Horton's "Who Done It?"**_ (2007). [Workshop paper]. _Miller, Mark S.; Donnelley, James E.; Karp, Alan H._ 2nd USENIX Workshop on Hot Topics in Security (HotSec '07), August 2007, Boston, Massachusetts. Retrieved from: <https://www.usenix.org/legacy/events/hotsec07/tech/full_papers/miller/miller_html/index.html> *(accessible via Wayback Machine; direct USENIX link returns 403)*

> "The protocol that adds accountability to capabilities without sacrificing safety"

## Summary

The paper addresses a longstanding criticism of object-capability (OCap) systems: that their anonymous, bearer-right model makes it impossible to determine who to blame when something goes wrong. ACL systems track identity but sacrifice proactive safety; capability systems provide proactive safety but lack reactive accountability. Miller, Donnelley, and Karp propose Horton — Higher-Order Responsibility Tracking of Objects in Networks — a protocol layer that can be interposed between existing OCap application objects to add identity-based tracking and accountability without modifying the objects or their underlying capability foundations.

## Key Points

**Proactive and reactive security are complementary, not competing.** The paper frames two approaches to protecting users from harmful programs: proactive control (preventing bad things or limiting damage) and reactive control (identifying who to blame and suspending their access). ACL systems support reactive control directly by tagging actions with user identity, but are weak at proactive control because programs inherit all of their user's privileges. Capability systems provide strong proactive control through least authority, but their anonymous bearer-right model appears to make reactive control impossible.

**Horton refutes the accountability criticism of capabilities.** Among historical criticisms of OCap systems, the inability to record who to blame for which action was the one remaining unrefuted objection. Horton demonstrates that identity-based tracking can be added to capability systems as a protocol layer — interposed between existing objects without modifying them — thereby combining proactive safety with reactive accountability.

**Responsibility delegation requires coupling authority with accountability.** The paper's central thesis: delegation is fundamental to human society, and digital systems must support not just delegation of authority (capability systems) and not just assignment of responsibility (identity systems), but delegation of responsibility — authority coupled with accountability for its use. Horton makes this coupling explicit at the protocol level.

**The protocol uses proxy/stub pairs to track identity across capability boundaries.** Horton introduces Carol (an intermediary) between Alice and Bob. When Alice delegates a capability to Bob through Carol, Horton wraps the capability in a proxy that records Bob's identity when exercised. The stub at the receiving end ensures the exercised capability carries accountability metadata. Neither Alice's nor Bob's existing code needs modification.

**Bootstrapping relies on inductive trust relationships.** Every secure protocol faces two cases: establishing an initial secure relationship between unconnected parties (base case) and bootstrapping new relationships from existing secure ones (inductive case). Horton handles the inductive case through sealed/unsealed gift-wrapping — new accountability relationships are established through existing trusted connections, extending the accountability chain without requiring a central authority.

**Identity is represented through sealer/unsealer pairs, not central registries.** Rather than relying on a certificate authority or identity provider, Horton uses the sealer/unsealer cryptographic pattern native to OCap systems. This preserves the decentralized character of capability-based authority while adding the identity layer needed for accountability.

**Horton is a layer, not a replacement.** The protocol sits on top of existing OCap foundations. This architectural choice is load-bearing: it means systems can gain accountability incrementally, adding Horton to specific delegation paths that need tracking without imposing it everywhere. The capability substrate retains its properties unchanged.

## Key Quotes

> "There are two approaches to protect users from the harm programs can cause, *proactive control* and *reactive control*. Proactive controls help prevent bad things from happening, or limit the damage when they do. But when repeated abuse occurs, we need some workable notion of 'who' to blame, so we can reactively suspend the responsible party's access."

> "Because ocaps operate on an anonymous 'bearer right' basis, they seem to make reactive control impossible. Indeed, although many historical criticisms of ocaps have since been refuted, a remaining unrefuted criticism is that they cannot record who to blame for which action. This lack has led some to forego the benefits of ocaps."

> "Horton can be interposed between existing ocap-based application objects, without modifying either these objects or their underlying ocap foundations. Horton supports identity-based tracking and control for delegating responsibility with authority. Horton thereby refutes this criticism of the ocap paradigm."

> "Delegation is fundamental to human society. If digital systems are to mediate ever more of our interactions, we must be able to delegate responsibility within them. While some systems support the controlled delegation of authority, and other systems support assignment of responsibility, today we have no means for delegating responsibility, that is, delegating authority coupled with assigning responsibility for using that authority."

> "Every protocol which builds secure relationships must face two issues: 1) the base case, building an initial secure relationship between players not yet connected by this protocol, and 2) the inductive case, in which a new secure relationship is bootstrapped from earlier assumed-secure relationships."

## Influence

Horton provided the missing accountability mechanism for the object-capability paradigm, resolving the most persistent criticism that had led some system designers to reject capabilities in favor of ACL-based approaches. The protocol influenced Miller's subsequent work on robust openness (the 2019 ActivityPub talk recapitulates Horton as the accountability layer enabling open social systems). The Horton architecture — accountability as a layer atop authorization — directly informs approaches to agent delegation where principals need to track how delegated authority is exercised without requiring agents to operate under ambient identity systems.

## Sources

- Primary: Miller, Mark S.; Donnelley, James E.; Karp, Alan H. "Delegating Responsibility in Digital Systems: Horton's 'Who Done It?'" 2nd USENIX Workshop on Hot Topics in Security (HotSec '07), August 2007. <https://www.usenix.org/legacy/events/hotsec07/tech/full_papers/miller/miller_html/index.html>
- Archived: Wayback Machine capture, October 2021. <https://web.archive.org/web/20211010010717/https://www.usenix.org/legacy/events/hotsec07/tech/full_papers/miller/miller_html/index.html>
- Google Research listing: <https://research.google/pubs/delegating-responsibility-in-digital-systems-hortons-who-done-it/>

## Relations

- relates_to::[[Miller (2006) Robust Composition]]
  - Horton builds directly on the object-capability foundations formalized in Miller's dissertation; the capability substrate that Horton layers accountability onto is the model defined in the thesis

- relates_to::[[Miller (2019) Architectures of Robust Openness]]
  - The 2019 talk recapitulates the Horton protocol as the key mechanism enabling accountability in open federated systems; Horton is the bridge between proactive safety (capabilities) and reactive security (identity-based blame)

- relates_to::[[Miller, Tulloh & Shapiro (2005) The Structure of Authority]]
  - Horton extends the authority structure framework: the 2005 paper defines how authority flows through capability graphs; Horton adds tracking of who exercises that authority

- relates_to::[[Saltzer & Schroeder (1975) The Protection of Information in Computer Systems]]
  - Horton addresses the accountability gap that ACL-based systems (Saltzer and Schroeder's design-principles context) fill with identity but at the cost of ambient authority

- relates_to::[[Allen (2021) Principal Authority]]
  - Principal authority's legal agency framework requires exactly what Horton provides: when a principal delegates authority to an agent, accountability for the agent's exercise of that authority must trace back through the delegation chain

- relates_to::[[Authority Flows from the Person]]
  - Horton makes delegation of responsibility concrete: authority flows from the person through capabilities, and accountability flows back through Horton's tracking layer

- relates_to::[[Human Authority Over Augmentation Systems]]
  - Horton provides a technical mechanism for the principle's requirement that humans retain meaningful oversight of agent actions — not just authority delegation but accountability for its exercise

- relates_to::[[Topology Determines Authority]]
  - Horton respects the topology principle: accountability relationships mirror the authority graph rather than imposing a separate identity hierarchy
