---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v2 · deeper: the gap between chatbot use and advanced use, four paired use cases (r1 kept)
tags: [research, youtube, script, ai, week-04]
---

# Script · Free or paid (Week 04, Mon 26 Oct)

← [[Free or paid - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (26 Oct 2026, P7 on [[Which AI - Status]]): *"Goal not sharp enough, you just spit information. consider a conversation i had that started with. i do everything for free with top tier chatbots. why should i get a subscription, and focus between api connection, usage, context, rag and general serious work. consider openai, anthropic and deepseek, add reference images for the models and companies and close with a strong conclusion. ... comparison get lost between words and fast topic change, suggestion ok. pace right. redo it and go for the render"*. Series: **What's coming** (what AI costs and what it changes for the viewer).

**Y:** know whether a subscription is worth it. **X:** the free chatbots run the same models; plans buy the room around them (usage, context, file retrieval, agents, privacy), and connecting your own app is the API, not a plan. **Theme line:** *free gives you the model; paying gives you the workshop around it.*

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Claude Free $0 (Sonnet, Haiku; projects capped at 5); Pro $20/mo, at least 5x Free per 5-hour session, adds Opus, Claude Code, Research; Max adds $100 or $200/mo API credit; Team: no training on your content by default | claude.com/pricing (**read**) |
| 2 | Enhanced project knowledge with RAG only on paid plans; RAG mode expands capacity up to 10x | support.claude.com "What are projects?" (search excerpt of the help article) |
| 3 | ChatGPT Free: unlimited text chats, limited uploads, images, voice, deep research; Plus $20 with Codex, deep research, more uploads | OpenAI pricing page via Oct 2026 guides (search excerpts; page returned 403) |
| 4 | ChatGPT context: Free about 27K tokens, Plus about 54K on the everyday model | 2026 guides (search excerpts; unofficial, labelled "guides" on screen) |
| 5 | DeepSeek app: free, no subscription plans; file upload, search, deep-think | reviews (search excerpts) |
| 6 | Model context on the API: Claude models 1M; GPT-6 Sol 1M; DeepSeek V4 1M | claude-api reference; artificialanalysis.ai; DeepSeek V4 guide (excerpt) |
| 7 | Output $ per MTok: Claude Opus 5.5 $20, GPT-6.1 Sol $10, DeepSeek V4.1 Flash $1.20 (peak) | Anthropic pricing (**read**); artificialanalysis.ai (**read**); benchlm (excerpt) |
| 8 | DeepSeek stores personal data in the People's Republic of China | DeepSeek privacy policy, 10 Feb 2026 (**read**) |
| 9 | ChatGPT Business: no training on business data | Oct 2026 guides (search excerpts) |
| 10 | Logos: Anthropic (public domain), Claude symbol (CC0), OpenAI 2025 symbol and ChatGPT logo (public domain), DeepSeek icon and logo (MIT) | Wikimedia Commons (**read**; credits in `stock/_credits.jsonl`) |

## 1. Idea gate

**Scores:** surprise 4 (the free chatbots are the real models) · scale 5 · depth 4 · evidence 4 · showable 5 · plain 5. **Street-lamp:** pass: pricing pages list features, not which features a free user is missing for real work. **Expert test:** RAG only on paid Claude plans; Claude Max includes API credit; DeepSeek's data location. **Against:** (1) "biased" → three labs on one board, same rows; (2) "I just chat" → the first suggestion is stay free; (3) "numbers age" → dated on screen. **Demand check:** not run (`youtube_search.py` HTTP 400).
**Five hooks:** objection "Claude, ChatGPT and DeepSeek all give their chatbots away for free. So why would anyone pay twenty dollars a month? Five things free plans hold back." (**used**) · contradiction "The free chatbot is the same model you'd pay for." · stakes "You might be paying for a chatbot you could use free." · question "Why pay for AI when it's free?" · fact "Free AI plans hold back five things."

## 2. Package

- **Promise:** why pay for AI when the top chatbots are free, in five concrete things, and when not to pay.
- **Titles:** *Every Top AI Chatbot Is Free. So Why Pay $20?* (recommended) · *Free vs Paid AI: What You Actually Get (ChatGPT, Claude, DeepSeek)* · *You Don't Need an AI Subscription. Unless You Need These 5 Things*.
- **Thumbnail (at P8):** the three logos on $0 pedestals, one turning into the workshop ring; words "FREE vs $20".

## 3. Script r2: 216 words, 7 scenes (take v3, rate 1.25: 61.0 s)

User on r1 (26 Oct 2026): *"go deeper on advanced usage vs common chatbot and rerender. make it more dynamic, with example usecases for example reading a simple document vs designing a knowledge base and generating complex content (software, knowledge bases, coding). the goal of this video is to explain the breach between types of use of ai. keep mention different companies. make a new render and keep the old one"*. **New theme line:** *chatbots answer questions; agents do the work; the gap is the tools around the model.*

| Sc | Pair (chatbot vs advanced) | Voice (exact text) |
| --- | --- | --- |
| 1 | hook: search box vs building | Most people use AI like a search box. Others build software and whole knowledge bases with it, using the same models. Here is the gap between them. |
| 2 | one PDF vs a knowledge base | Take reading. Asking about one PDF works free on ChatGPT, Claude and DeepSeek. But turning hundreds of documents into a knowledge base needs retrieval, called RAG, and Claude keeps that for paid plans. |
| 3 | a few pages vs a codebase in view | Then memory. A chat holds a few pages at a time. Advanced work keeps a whole codebase or book in view: the models take a million tokens, but free chats get only a slice. |
| 4 | an email vs a coding agent | Then building. A free chat writes you an email. A coding agent, like Claude Code or OpenAI's Codex, reads your project, edits the files and runs the tests, and Claude Code needs at least Pro. |
| 5 | typing vs AI inside your tools | And connection. Chat is you typing. Advanced use puts AI inside your own tools through the API, paid per word, with DeepSeek the cheapest and Claude Opus the priciest. |
| 6 | which to pick (solution) | So match the tool to the job. Questions and one-off documents: stay free. Files, research and code every day: a single twenty-dollar plan. AI inside your product: the API. |
| 7 | conclusion | Here is the point: chatbots answer questions, agents do the work, and the gap is not the model, it's the tools around it. Which side are you on? Tell me. |

**Beat sheet r2:** a "chatbot | advanced" split stays on screen from scene 1 to 5 (one frame of reference). Left: a search box typing, one PDF with three free logos, a few pages in a rose window, a free-chat email, you typing. Right (3D clipped to the advanced half): modules stacking into software, about 100 documents flying into a knowledge base and three retrieved by beams into an answer, a mint window sliding over a 34-page codebase ribbon with a rose free slice inside it, the API pipes from your app to DeepSeek, OpenAI and Claude with logo price tags; scene 4 is a schematic agent loop (read, edit, test, fix) with a packet circling on the beat, "tests pass" and the agents' plans, not a drawn product UI. Colourful lanes, then the model core gaining its workshop.

**Honesty r2:** "Claude Code needs at least Pro": claude.com/pricing (Free has no Claude Code). Codex in Plus: Oct 2026 guides. Agent loop is a schematic. "hundreds of documents": the help article's RAG capacity claim (up to 10x), not a fixed count.

## 3b. Script r1 (kept, `render/fp-65s-9x16-r1.mp4`)

| Sc | Question it answers | Voice (exact text) | Delivery |
| --- | --- | --- | --- |
| 1 | (hook: the objection) | Claude, ChatGPT and DeepSeek all give their chatbots away for free. So why would anyone pay twenty dollars a month? Five things free plans hold back. | plain |
| 2 | reason 1 | First, usage. Free plans ration you. Claude Pro gives at least five times the free limit, and ChatGPT's free plan caps uploads. DeepSeek's app has no paid plan at all. | steady |
| 3 | reason 2 | Second, context: how much the model holds at once. The models fit huge documents, but free chats get less room. On ChatGPT, Plus roughly doubles it. | explaining |
| 4 | reason 3 | Third, your own files. Claude searches big project libraries with retrieval, called RAG, only on paid plans, and free accounts get five projects. | steady |
| 5 | reason 4 | Fourth, connection. Wiring a model into your own app needs the API, paid per word, not a plan. DeepSeek's is the cheapest, and Claude Max even includes API credit. | brisk |
| 6 | reason 5 | Fifth, serious work. Pro and Plus run coding agents, and team plans keep your data out of training. DeepSeek's app stores data in China. | firm |
| 7 | so which? (solution) | So: chatting and learning, stay free. Long documents, your own files or daily coding, pay for one plan. Building an app, skip the plans and use the API. | brighter |
| 8 | the conclusion | Here is the point: free gives you the model, paying gives you the workshop around it. Which part are you missing? Tell me. | slower; break 0.2 after "model" |

**Honesty:** ChatGPT limits come from Oct 2026 guides (the official page refused the fetch), labelled on screen; "free chats get less room" is said only for ChatGPT with its numbers. "1M model" cells are API context windows, not chat-plan limits. DeepSeek data location is from its own policy. Logos name the companies compared.

## 4. Beat sheet, prefix `fp`

3D hook: three pedestals with the logos and "$0" from frame 1; the paid-plans card on "twenty". One 2D board (scenes 2 to 6): logo column heads, five rows (usage, context, files, API, work); each row lights on its scene, cells land on the company's word, earlier rows dim and stay. Solution lanes in colour (mint flood). 3D close: the model core alone ("the model"), then the mint ring and five modules light around it ("the workshop") with sparks.

## 5. Not verified

ChatGPT plan limits and context (official page blocked); DeepSeek app limits; Claude Free context; demand. How the voice sounds. P7 is the user's.
