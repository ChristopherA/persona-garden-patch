---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Chat Log vault type: a text chat record from a meeting sidebar or AI conversation, always derived from a parent note via derived_from:: predicate. Preserves original timestamps and speaker attribution without cleanup. Captures links shared, brief exchanges, and introductions alongside the spoken conversation."
tagline: "Text chat records from meetings or AI conversations — timestamped and attributed"
formatted: "2026-03-14"
---

- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Chat Log

A chat log is a text record of a synchronous chat — typically the Zoom chat sidebar during a meeting or an AI conversation archive. Chat logs are always sidecars to a parent note, linked via `derived_from::`.

```
- is_a::[\[\[Chat Log\]\]](Chat%20Log.html)
- derived_from::[[Parent Meeting or Conversation]]↑
```

## Conventions

- **Format preserved**: Timestamps and speaker names kept as captured (e.g., `2026-03-04 10:07:08 From Name to Everyone:`). No cleanup beyond basic formatting.
- **Frontmatter**: `created`, `reviewed`, `brief_summary`, `tagline`, `source-format` (e.g., `zoom-chat`).
- **Naming**: `YYYY-MM-DD Meeting Name - Chat.md` within the compound meeting folder.
- **Content**: Links shared, brief exchanges, introductions. Chat logs capture what was typed alongside the spoken conversation.

## Related Types

AI chat archives (`ai-chats-archive-vault/`) use `type/chat-archive` tags rather than `is_a::[\[\[Chat Log\]\]](Chat%20Log.html)`. Chat logs are meeting sidecars; chat archives are standalone conversation records from a different era of the vault.

## Sources

Chat log conventions from meeting-capture skill and D8-D13 decisions.

## Relations

- derived_from::[\[\[Meeting Note\]\]](Meeting%20Note.html) — chat logs belong to meetings
- relates_to::[\[\[Transcript\]\]](Transcript.html) — parallel artifact from the same meeting (speech vs text)
