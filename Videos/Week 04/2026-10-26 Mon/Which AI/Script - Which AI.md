---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · from scratch at the user's request (replaces Model economics); What's coming; HyperFrames + three.js, overlap-checked
tags: [research, youtube, script, ai, economics, week-04]
---

# Script · Which AI (Week 04, Mon 26 Oct)

← [[Which AI - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (26 Oct 2026, on [[Model economics - Status]] r2): *"The goal got diluted. remake a new one explaining the difference across different plan and models. comparatives between open ai, chinese models and anthropic, and suggestions about usage. remake it from scratch"*. Series: **What's coming**. One goal: **which AI to pay for**.

**Y:** pay for the right AI and nothing more. **X:** plans cost the same, models differ in intelligence and price per token, Chinese models are far cheaper but score lower and DeepSeek's app keeps data in China. **Theme line:** *pay for the top model where it earns its price.*

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Claude: Free $0 (Sonnet, Haiku); Pro $20/mo ($17 annual) adds Opus, Claude Code, Research; Max from $100 (5x or 20x Pro); Team $20 to $25/seat; Enterprise $20/seat plus API usage | claude.com/pricing (**read**) |
| 2 | ChatGPT: Free $0; Go about $8 (priced locally, may show ads); Plus $20/mo with Codex and deep research; Pro tiers from $100 (guides list $100, $200, $500); Business $20 to $25/seat | Oct 2026 guides (search excerpts; chatgpt.com and openai.com returned 403) |
| 3 | Output / input $ per MTok: Opus 5.5 20 / 4, Sonnet 5.5 10 / 2, Haiku 5.5 0.50 / 0.10, Fable 5.1 50 / 10 | Anthropic pricing page (**read**) |
| 4 | GPT-6.1 Sol $2 / $10 per MTok; Index v4.3.2 score 52 (max); released 29 Sep 2026 | artificialanalysis.ai model page (**read**) |
| 5 | Intelligence Index v4.3.2: Claude Opus 5.5 58, Sonnet 5.5 56, Kimi K3.1 Pro 55, MiMo-V2.6-Pro 46, DeepSeek V4.1 Flash 45, GLM-5.3 45 (DeepSeek, GLM, MiMo open weights) | artificialanalysis.ai/models (**read**, no page date) |
| 6 | DeepSeek V4.1 Flash (deepseek-flash since 10 Sep 2026): $0.30 / $1.20 per MTok at peak, half off-peak | benchlm.ai and DeepSeek docs (search excerpt; DeepSeek models page **read**, prices page not reached) |
| 7 | Opus $20 / DeepSeek $1.20 = 16.7, "a seventeenth" | facts 3, 6 (derived) |
| 8 | DeepSeek: "we directly collect, process and store your Personal Data in People's Republic of China" | DeepSeek privacy policy, last update 10 Feb 2026 (**read**) |
| 9 | Kimi K3 (Jul 2026): open weights under a modified MIT licence, $3 / $15 per MTok | search excerpts (not used: K3.1 Pro price not found) |
| 10 | GPT-6 Astra $10 / $50 per MTok, index about 52.7 (third-party) | search excerpts (not used) |
| 11 | Anthropic does not sell Claude in China | Anthropic, 23 Feb 2026 (**read**; not used) |
| 12 | Claude and GPT-6.1 Sol both price output at 5x input | facts 3, 4 |
| 13 | DeepSeek cache hits about 98 % below the cache-miss price | search excerpt (not used) |
| 14 | Claude Opus 5.5 cache hits $0.20 per MTok (1/20 of input) | pricing page (**read**; not used) |
| 15 | Index costs fall fast: reaching index 30 costs 86x less per task than when first reached | Artificial Analysis on X (search excerpt; not used) |

## 1. Idea gate

**Scores:** surprise 4 (seventeen times cheaper) · scale 5 · depth 4 · evidence 4 · showable 5 · plain 5. **Street-lamp:** pass: price lists do not set price against an independent score, nor add the data-location catch. **Expert test:** writing at 5x reading at both US labs; Kimi within 3 points of Opus; DeepSeek's privacy policy wording. **Against:** (1) "biased toward Claude" → the same index for all, OpenAI and Chinese prices beside Claude's, and the advice names both $20 plans; (2) "numbers move monthly" → every figure dated on screen; (3) "I just chat" → the first suggestion is a free plan. **Demand check:** not run (`youtube_search.py` HTTP 400).
**Five hooks:** number "A Chinese AI model now costs a seventeenth of Claude Opus, per word. So why do people still pay for Claude and ChatGPT? Here is the honest comparison." (**used**) · question "Claude, ChatGPT or a Chinese model: which should you pay for?" · contradiction "The best AI isn't the best deal." · stakes "You might be paying twenty dollars a month for an AI you barely use." · fact "Claude Pro and ChatGPT Plus cost exactly the same."

## 2. Package

- **Promise:** an honest side-by-side of Claude, ChatGPT and the Chinese models, and which to pay for.
- **Titles:** *Claude vs ChatGPT vs Chinese AI: Which Should You Pay For?* (recommended) · *A Chinese AI Costs 1/17 of Claude. Here's the Catch* · *Free, $20 or Open Weights? Picking an AI in 2026*.
- **Thumbnail (at P8):** the three price pillars (Opus towering, DeepSeek a sliver); words "1/17 THE PRICE".

## 3. Script: 219 words, 8 scenes (take v2, rate 1.25: 64.9 s)

| Sc | Question it answers | Voice (exact text) | Delivery · pause |
| --- | --- | --- | --- |
| 1 | (hook) | A Chinese AI model now costs a seventeenth of Claude Opus, per word. So why do people still pay for Claude and ChatGPT? Here is the honest comparison. | curious |
| 2 | what do the plans give? | Start with the plans. Claude Pro and ChatGPT Plus both cost twenty dollars a month, and both add stronger models, coding agents and research. The pricier tiers mostly raise your limits. | brisk |
| 3 | how are models billed? | Under every plan sit the models, charged per token, a piece of a word. At Anthropic and OpenAI, writing a token costs five times reading one. | steady |
| 4 | who is smartest? | So who is smartest? On one independent index, Claude Opus leads. China's Kimi is close behind, and OpenAI's Sol model comes next. | even |
| 5 | and the price? | Price flips that order. DeepSeek's fast model scores lower, but costs a fraction per word, and Chinese labs publish open weights anyone can run. | brighter |
| 6 | what's the catch? | The catch: DeepSeek's own app stores your data in China, and the cheap models still score well below the leaders. | grave |
| 7 | so which? (solution) | So here is how to choose. Everyday questions: any free plan. Serious work and coding: a single twenty-dollar plan, Claude Pro or ChatGPT Plus. Bulk tasks in an app: a cheap model, or open weights on your own servers, so the data stays with you. | brighter; break 0.2 after "choose" |
| 8 | so what? | So here is the point: pay for the top model where it earns its price. Which one do you pay for? Tell me. | slower; break 0.2 after "price" |

**Honesty:** "a seventeenth of Claude Opus": list output prices (Opus 5.5 $20, DeepSeek V4.1 Flash $1.20 peak), on screen; Fable is Claude's priciest. "Claude Opus leads": on the Index v4.3.2 page as read; Fable 5.1 not scored there. ChatGPT plan prices come from Oct 2026 guides (the official page refused the fetch); only the $20 Plus price is spoken. "stores your data in China": DeepSeek's own app and API per its privacy policy; open weights run elsewhere do not.

## 4. Beat sheet, prefix `wa`

3D price pillars of the three labs (Opus orange, Sol blue, DeepSeek cream; DeepSeek and Opus from frame 1, Sol on "ChatGPT") return at the close. 2D: Claude and ChatGPT plan columns with "same price" on "twenty"; a word split into tokens, then 1 read coin against 5 write coins; index bars growing on each name (honest 0 to 60); price against score with DeepSeek ringed and an "open weights" badge. 3D globe turning toward China with the data arc drawn on "stores". Solution lanes in colour (mint flood): daily questions to any free plan, work and coding to one $20 plan, bulk app tasks to cheap or open.

## 5. Not verified

ChatGPT plan details (official page blocked); DeepSeek's price page itself (figures from an aggregator matching the docs' model names); Artificial Analysis page date; demand. How the voice sounds. P7 is the user's.
