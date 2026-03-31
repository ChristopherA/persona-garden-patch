---
title: "How to finally trust Claude's advice (using Karpathy's LLM Council method)"
canonical: "https://x.com/itsolelehmann/status/2038661433626333649"
author_name: "Ole Lehmann"
published: 2026-03-30
created: 2026-03-30
reviewed: 2026-03-30
brief_summary: "Ole Lehmann reimplements Karpathy's LLM Council entirely inside Claude Code using five sub-agents (Contrarian, First Principles, Expansionist, Outsider, Executor), anonymous cross-review, and a chairman synthesis step. The peer review round reliably surfaces blind spots no single advisor catches alone."
tagline: "Five adversarial AI advisors plus anonymous peer review produce decisions you can trust."
content_type: x-article
rendition_of: "[itsolelehmann (2026) LLM Council for Decision Quality](../itsolelehmann%20%282026%29%20LLM%20Council%20for%20Decision%20Quality.html)"
tweet_id: "2038661433626333649"
triaged: 2026-03-30
metrics:
  views: 198263
  likes: 505
  retweets: 41
  replies: 18
  bookmarks: 2053
  quotes: 10
---

# How to finally trust Claude's advice (using Karpathy's LLM Council method)

**authored_by::[[@itsolelehmann]]↑**

_Clipped from [X](https://x.com/itsolelehmann/status/2038661433626333649) on 2026-03-30_

_is_a::[[web_clipping]]↑; has_status::[[curated]]↑_

---

Claude just tells you what you want to hear. Every time. You can't trust it.

So I built a skill that forces 5 AI advisors to argue about your question, anonymously review each other's work, and hand you a verdict you can actually trust.

In this article I'll show you exactly how to set it up.

Here's the method and the exact skill I built, so you can run it yourself:

P.S. If you want more AI workflows like this one delivered to your inbox every week, join 35k readers getting them free: [aisolo.beehiiv.com/subscribe](http://aisolo.beehiiv.com/subscribe)

## Why one answer is the problem

Claude is incredibly agreeable.

Ask it "should I launch this product?" and it'll find 5 reasons why you should.

Then ask it "is this product a bad idea?" and it'll find 5 reasons why it is.

Same product, different framing, completely opposite answers.

You've probably noticed this.

You ask a question, get an answer that sounds smart, feel good, and move on.

But that answer was shaped by how you asked it.

- Your assumptions
- Your framing
- Your emotional lean

Claude picked up on all of it and told you what you wanted to hear.

That's fine for writing emails.

It's dangerous for making decisions.

The council breaks this by forcing 5 different thinking styles onto the same question.

They can't all agree with you because they're not all looking at it from your angle.

## Where this comes from

Andrej Karpathy (co-founder of OpenAI + former head of AI at Tesla) built something called the LLM Council.

The idea: instead of asking one AI model a question and trusting whatever comes back…

1. You poll multiple models on the same question.
1. Then you have them peer-review each other's responses anonymously.
1. Then a chairman model reads everything and synthesizes the final answer.

His version polls GPT, Claude, Gemini, and others against each other.

I rebuilt it to work entirely inside Claude using sub-agents with different thinking styles instead of different models.

I say "council this" and 5 advisors spin up, argue, review each other's blind spots, and hand me a verdict. All inside one session.

## The 5 advisors

**The Contrarian**

Looks for what will fail. Assumes your idea has a fatal flaw and tries to find it. If everything looks solid, digs deeper. (catches the "this sounds great but have you thought about..." gaps you skip when you're excited about something)

**The First Principles Thinker**

Ignores your question and asks what you're actually trying to solve. Strips away assumptions. Rebuilds the problem from the ground up. (catches the "you're optimizing the wrong variable entirely" problem, which happens more often than you'd think)

**The Expansionist**

Hunts for upside you're missing. What could be bigger? What adjacent opportunity is sitting right next to your question that you haven't noticed? (catches the "you're thinking too small" blind spot)

**The Outsider**

Has zero context about you, your field, or your history. Responds purely to what's in front of them. (catches the curse of knowledge: things that are obvious to you but completely invisible to your customers)

**The Executor**

Only cares about one thing: what do you do Monday morning? If an idea sounds brilliant but has no clear first step, the Executor will say so. (catches brilliant plans with no path to actually doing them, which is most of them)

## Why the peer review matters

This is what separates the council from just asking Claude 5 times.

After all 5 advisors respond, the skill anonymizes everything. Shuffles which advisor maps to which letter. The reviewers don't know who said what.

Then 5 reviewers read all the responses and answer 3 questions:

1. Which response is strongest and why?
1. Which has the biggest blind spot?
1. What did all five miss?

That last question is the most valuable one.

Every time I've run the council, the peer review round catches something no individual advisor saw.

When you read 5 perspectives side by side, the gap between them reveals what nobody thought to mention.

## How to set it up

Step 1: Grab the skill [here](https://docs.google.com/document/d/e/2PACX-1vSvw_Mk4iq4DkeMM3YVcvHgkzY-bsmnkXBC2TaEVBUDMjU4RtwDrKdxenpc-x7Vnzw5THGA4wVJd-LX/pub).

Drop it into your Skills in Claude Code or Cowork (Customize > Skills > Add skill. Remember to paste the name + description separately).

Step 2: Type "council this" followed by your question. Give it as much context as you can. The richer the input, the sharper the output.

Step 3: The skill scans your workspace for relevant context, frames the question, spawns all 5 advisors in parallel, runs the anonymous peer review, and produces a chairman synthesis with a clear recommendation and one concrete next step.

Step 4: You get a visual HTML report you can scan in 60 seconds, plus a full markdown transcript if you want to dig into the reasoning later.

## What happened when I counciled a product decision

I was building a Claude Code product and had to pick a format.

The obvious move was a full self-paced course. Build it once, sell it forever. Passive income baby!

That's what everyone tells you to do (and what I'd done myself over the past 3 years).

If I'd asked Claude straight up, that's exactly what it would have said:

"Self-paced courses scale better, create passive income, let students learn at their own pace, and you've already proven you can sell them."

Helpful. Reasonable. But potentially far too agreeable.

So I counciled it.

Here's what came back:

1. The First Principles Thinker reframed the whole question. Said the real variable here is speed. AI tools change every few weeks. A self-paced course filmed in March could be outdated by May. A workshop lets you teach the latest version live, then the recording becomes a point-in-time snapshot instead of a promise you can't keep.
1. The Contrarian went after completion rates. Self-paced courses in this space average 3-5% completion. That means 95% of buyers never finish, which means bad reviews, refund requests, and a product that technically "scales" but leaves a trail of disappointed customers. A live workshop forces completion by design.
1. The Executor ran the timeline math. A polished self-paced course takes 8-12 weeks to produce (scripts, recording, editing, platform setup). A workshop takes 2-3 weeks to prep. Ship faster, get real feedback, iterate. You can always build the course from the recording later.
1. The Expansionist spotted something I'd been too binary to see. A live workshop with the recording included gives people both formats in one purchase. The live experience, the Q&A, the energy of doing it with a group, plus they can rewatch it whenever they want. One production effort, twice the perceived value.
1. The Outsider flagged that the course description assumed people already knew why they needed Claude Code. Someone outside the AI bubble wouldn't understand the value prop from the landing page alone. A live workshop solves this naturally because you demonstrate it in real time instead of explaining it in a sales page.

Then the peer review caught one more thing:

The Contrarian's completion rate argument and the First Principles Thinker's speed argument actually reinforce each other in a way neither advisor saw alone.

A live workshop solves both problems at once.

High completion because people show up live, AND always-up-to-date because you're teaching the current version.

That combination is the actual moat against self-paced competitors.

Final verdict: Live workshop with the recording included.

So I ran the workshop. 180 people signed up. 4.8 out of 5 stars.

1 question gave me 5 perspectives and a format decision I probably would've gotten wrong (because the "obvious" answer sounded so reasonable), caught in about 4 minutes.

Btw if you want to join my next workshop and learn how to leverage Claude Cowork to get the output of a $500k/year marketing team....

You can pre-register to reserve a spot here (no payment needed): https://tally.so/r/LZbxKl

## What else to council

The council works on any decision where being wrong is expensive and you keep going back and forth.

- Content and positioning. "Should I niche down further or broaden my audience?" The Contrarian will stress-test the risk of going too narrow. The Expansionist will find the bigger play hiding inside your niche.
- Hiring and operations. "Should I hire a VA or build an automation?" The Executor maps the fastest path. The First Principles Thinker asks if you even need either.
- Pricing. "Am I leaving money on the table or pricing myself out?" The Outsider will tell you whether your value prop actually makes sense to someone who's never heard of you.
- Any fork in the road where you keep going back and forth. If the cost of being wrong is high and you've been circling for more than a few days, council it.

If you already know the answer and just want validation, skip it.

The council will tell you things you might not want to hear. That's the point.

## Go council something

Think about the decision you've been going back and forth on. The one where you ask Claude, get a nice-sounding answer, and still don't feel sure.

Council it. Grab the skill [here](https://docs.google.com/document/d/e/2PACX-1vSvw_Mk4iq4DkeMM3YVcvHgkzY-bsmnkXBC2TaEVBUDMjU4RtwDrKdxenpc-x7Vnzw5THGA4wVJd-LX/pub). Say "council this" and give it the full context.

5 minutes from now you'll have 5 independent perspectives, a peer review that caught what they all missed, and a clear recommendation with one concrete next step.

P.S. If you want more AI workflows that help you get more customers, more attention, and more done (without working more hours)...

I send them to 35k readers every week for free.

Plus you get a free Claude Cowork masterclass when you join: aisolo.beehiiv.com/subscribe

---

## Relations

relates_to::[[Claude Code]]↑
relates_to::[[Agent Orchestration]]↑
relates_to::[[Decision Making]]↑
