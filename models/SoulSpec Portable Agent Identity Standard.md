---
created: 2026-03-26
author: Christopher Allen
brief_summary: "SoulSpec is an open standard treating agent identity as source code: a structured file set (soul.json, SOUL.md, IDENTITY.md, AGENTS.md) for portable, versionable, shareable AI persona definitions. Created by the OpenClaw project and now supported by Ollama's local model runtime."
tagline: "Agent personality as source code: portable, versionable, shareable"
---

- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# SoulSpec Portable Agent Identity Standard

SoulSpec (soulspec.org) is an open standard for AI agent identity. Its core claim: agent personality should be treated as source code — structured, versionable, shareable — not runtime configuration. Peter Steinberger, creator of OpenClaw (the fastest-growing repository in GitHub history with over 175,000 stars in 2025), pioneered the SOUL.md pattern, inspired by Anthropic's constitutional AI work.

## Structure

**The file set**:

| File | Purpose |
|------|---------|
| `soul.json` | Package manifest: metadata, versioning, compatibility, discovery |
| `SOUL.md` | Personality: values, communication style, opinions, behavioral guidelines |
| `IDENTITY.md` | Who the agent is: name, role, backstory, contextual positioning |
| `AGENTS.md` | Operational workflows: task handling, tool usage, autonomous behaviors |
| `STYLE.md` (optional) | Communication patterns |
| `HEARTBEAT.md` (optional) | Autonomous check-in behavior — periodic execution configuration |

OpenClaw's "Workspace-First" design philosophy treats these configuration files as the source of truth for agent identity and behavior. Multi-agent support is achieved through "one gateway with many brains" — each agent has isolated state, separate tools, different personalities. Not different models; different people.

**Relationship to the AGENTS.md cross-tool standard**: AGENTS.md emerged separately as a cross-tool standard for providing agent-specific project context. It originated in mid-2025 from collaboration between Sourcegraph, OpenAI, Google, Cursor, and others, and is now maintained by the Agentic AI Foundation under the Linux Foundation. As of March 2026, AGENTS.md is supported by Claude Code, Cursor, GitHub Copilot, Gemini CLI, Windsurf, Aider, Zed, Warp, and others. AGENTS.md provides project-level task instruction (what to build, what conventions to follow). SoulSpec's SOUL.md provides agent-level behavioral specification (who the agent is, how it decides). These are complementary layers — the same distinction captured in [Task Instruction and Role Specialization as Agent Configuration Layers](../models/Task%20Instruction%20and%20Role%20Specialization%20as%20Agent%20Configuration%20Layers.html).

**Portability**: Ollama 0.17 (February 2026) shipped with native OpenClaw integration, meaning local models can now consume SOUL.md files directly. The garden's persona architecture is single-framework (Claude Code). As multi-framework agent deployment grows, the portability question will reach the garden.

## Relationship to the Garden Model

The garden's two-layer design (garden persona node + `.claude/agents/` operational file) parallels SoulSpec's structure. The garden persona node corresponds to SOUL.md + IDENTITY.md. The agent file corresponds to the operational deployment.

Three gaps in the garden model relative to SoulSpec:

1. **No package manifest** — the garden has no equivalent to `soul.json`, no mechanism for discovering, versioning, or sharing personas across projects
2. **Collapsed SOUL and IDENTITY** — SoulSpec separates behavioral guidelines (SOUL.md, who the agent decides) from identity specification (IDENTITY.md, who the agent presents as). The garden collapses these into one persona node
3. **Single-framework scope** — SoulSpec targets cross-framework portability; the garden targets Claude Code specifically

## Boundaries

SoulSpec addresses portable identity across frameworks; it does not address how models mechanistically adopt personas (see [\[\[The Persona Selection Model\]\]](The%20Persona%20Selection%20Model.html)) or where persona traits live in activation space (see [\[\[Persona Vectors and the Assistant Axis\]\]](Persona%20Vectors%20and%20the%20Assistant%20Axis.html)). Portability at the file level does not guarantee behavioral consistency across different model families.

The standard also does not address the coordination limits that apply when multiple specialized agents share a workspace. Research on multi-agent scaling found coordination gains plateau beyond approximately 4 agents — file-format portability does not solve this ceiling.

## Sources

- [SoulSpec — Open Standard for AI Agent Personas](https://soulspec.org/)
- [Anthropic Publishes Official Skills Guide — How It Compares to Soul Spec — ClawSouls Blog](https://blog.clawsouls.ai/posts/anthropic-skills-guide-soul-spec/)
- [OpenClaw and the Programmable Soul — Duncan Anderson, Medium](https://duncsand.medium.com/openclaw-and-the-programmable-soul-2546c9c1782c)
- [AGENTS.md: One File to Guide Them All — Layer5](https://layer5.io/blog/ai/agentsmd-one-file-to-guide-them-all/)
- [AGENTS.md Cross-Tool Unified Management Guide — SmartScope](https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-agents-md-guide/)
- [Ollama 0.17 Makes Local AI Agents Real — ClawSouls Blog](https://blog.clawsouls.ai/en/posts/ollama-017-openclaw-soul/)

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑
- relates_to::[\[\[The Persona Spectrum from Role Label to Soul Document\]\]](The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)
- relates_to::[Task Instruction and Role Specialization as Agent Configuration Layers](../models/Task%20Instruction%20and%20Role%20Specialization%20as%20Agent%20Configuration%20Layers.html)
- relates_to::[\[\[The Persona Selection Model\]\]](The%20Persona%20Selection%20Model.html)
- relates_to::[\[\[Persona Vectors and the Assistant Axis\]\]](Persona%20Vectors%20and%20the%20Assistant%20Axis.html)
- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
- relates_to::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- relates_to::[[Agent Persona Portability]]↑
