---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · simplest version at the user's request (replaces Free or paid); 2D only, one difference
tags: [research, youtube, script, ai, agents, week-04]
---

# Script · Chatbot vs agent (Week 04, Mon 26 Oct)

← [[Chatbot vs agent - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (26 Oct 2026, P7 on [[Free or paid - Status]] r2): *"Horrible, unnecesary 3d models. unclear diferentiation. go simpler, ai chatbot vs ai agent"*. Series: **How it works** (what makes an agent an agent). One difference: **who runs the loop.**

**Y:** know when a chatbot is enough and when you need an agent. **X:** a chatbot answers and you run every step; an agent is a model with tools in a loop, so it runs the steps itself. **Theme line:** *you are the loop; it is the loop.* **Running example:** add a contact form to your website.

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Claude Free has no Claude Code; Pro ($20/mo) adds Claude Code | claude.com/pricing (**read**) |
| 2 | ChatGPT Plus ($20) includes the Codex agent | Oct 2026 guides (search excerpts; OpenAI page returned 403) |
| 3 | ChatGPT, Claude and DeepSeek chat apps have free tiers (DeepSeek: no paid plan) | claude.com/pricing (**read**); guides and reviews (excerpts) |
| 4 | Coding agents read and edit files, run commands and tests in a loop | Claude Code and Codex product descriptions (general knowledge of the tools; no figure claimed) |
| 5 | Logos: Anthropic, OpenAI, ChatGPT (public domain), Claude symbol (CC0), DeepSeek (MIT) | Wikimedia Commons (**read**; `stock/_credits.jsonl`) |

Facts 6 onward live in [[Script - Free or paid]] (plans, context, RAG, API prices); this video uses only the five above.

## 1. Idea gate

**Scores:** surprise 3 · scale 5 · depth 4 · evidence 4 · showable 5 · plain 5. **Street-lamp:** pass: "agent" is used everywhere, rarely shown as "who runs the loop". **Against:** (1) "agents are hype" → the catch scene; (2) "I don't code" → the loop applies to any multi-step task; (3) "brand ad" → both labs' agents named, chatbots from three labs. **Demand check:** not run (`youtube_search.py` HTTP 400).
**Five hooks:** contrast "A chatbot answers you. An agent does the work for you. Same AI models, completely different results. Here is the difference." (**used**) · question "What actually makes an AI an agent?" · stakes "You might be doing an AI agent's job by hand." · fact "An agent is just a chatbot that can run its own loop." · number "One goal, dozens of steps, zero copy-paste."

## 2. Package

- **Promise:** the one difference between an AI chatbot and an AI agent, shown on one example.
- **Titles:** *AI Chatbot vs AI Agent: The One Difference* (recommended) · *You Are the Loop: Chatbots vs Agents Explained* · *Why an AI Agent Does What a Chatbot Can't*.
- **Thumbnail (at P8):** the two rings side by side, "you" in one, "agent" in the other; words "WHO DOES IT?".

## 3. Script: 197 words, 7 scenes (take v1, rate 1.25: 51.0 s)

| Sc | Question it answers | Voice (exact text) |
| --- | --- | --- |
| 1 | (hook) | A chatbot answers you. An agent does the work for you. Same AI models, completely different results. Here is the difference. |
| 2 | what does a chatbot do? | Say you want a contact form on your website. Ask a chatbot like ChatGPT, Claude or DeepSeek, and it writes the code. Then you copy it, paste it, run it, and paste back every error. You are the loop. |
| 3 | and an agent? | Give the same goal to an agent, like Claude Code or OpenAI's Codex. It opens your files, writes the form, runs the site, reads the error, fixes it, and runs the tests again. It is the loop. |
| 4 | what makes that possible? | The difference is tools. An agent can read and change files, run commands and check its own work, so one goal becomes dozens of steps without you. |
| 5 | what does it cost? | That is why agents sit in paid plans. Claude Code needs Pro, Codex comes with ChatGPT Plus, and the chat stays free. |
| 6 | the catch | The catch: an agent acts on your real files. Give it a copy or a branch, and read what it changed. |
| 7 | so what? (solution) | So here is the point: ask a chatbot when you want an answer, use an agent when you want it done. Which would you trust with your files? Tell me. |

**Honesty:** "dozens of steps" is illustrative of a multi-step task, not a measured count. The diff lines and file names are illustrative. Codex in Plus from guides.

## 4. Beat sheet, prefix `ca`

2D only. Hook: two big cards, "chatbot · answers you" (blue, frame 1) and "agent · does the work" (orange, on "agent"). The same ring twice: chatbot scene with YOU in the centre and stations ask, code, copy, paste, run, error (a rose dot laps every two beats); agent scene with the AGENT in the centre and stations files, write, run, error, fix, tests (an orange dot laps every beat), ending in a mint "done" hub. Tools as three spokes. Plans in two columns (free chatbots, $20 agents). Catch: your files, a safe copy, a diff to read. Close: "want an answer? chatbot", "want it done? agent" in colour.

## 5. Not verified

Codex plan details (OpenAI page blocked); demand. How the voice sounds (one "Claude Code" heard by whisper as "Cloud Code"). P7 is the user's.
