---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · P1 to P4a done by delegation; What's coming; HyperFrames + three.js with the overlap check
tags: [research, youtube, script, ai, economics, week-04]
---

# Script · Model economics (Week 04, Mon 26 Oct)

← [[Model economics - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (26 Oct 2026): *"Using all the tools you got now for 3d animation and make a new short: explaining anthropic model tiers, billing and economics, intelligence of each model, destillation and profitability of all the model vs openai. build a narrative containing all of them and use vivid animations"*. Series: **What's coming** (the last series video was How it works). Not compact.

**Y:** know what you pay for when you pick a model, and whether the labs make money on it. **X:** price per token by tier, with writing at five times reading; intelligence does not scale with price; cheap tiers come from distillation; both labs still lose money. **Theme line:** *you buy intelligence by the word.* **Running example:** one contract summarized by each tier (50,000 tokens in, 2,000 out; illustrative).

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Output / input $ per MTok: Fable 5.1 50 / 10, Opus 5.5 20 / 4, Sonnet 5.5 10 / 2, Haiku 5.5 0.50 / 0.10 (prompts up to 100K) | platform.claude.com pricing page (**read**) and the claude-api reference, cached 6 Oct 2026 |
| 2 | Output costs 5x input on every current tier | same (derived) |
| 3 | Cache hits: Opus 5.5 $0.20 per MTok (1/20 of input); Fable 5.1 $0.25 | pricing page (**read**) |
| 4 | Batch API runs at 50 % of cost | claude-api reference, Oct 2026 |
| 5 | Contract cost (derived): Haiku $0.006, Sonnet $0.12, Opus $0.24, Fable $0.60 | facts 1, our arithmetic |
| 6 | Artificial Analysis Intelligence Index v4.3.2, max effort: Opus 5.5 58, Sonnet 5.5 56; Fable 5.1 and Haiku 5.5 not listed | artificialanalysis.ai (**read**, no date on page) |
| 7 | Fable 5.1 is Anthropic's most capable widely released model | claude-api reference, Oct 2026 |
| 8 | Distillation: "training a less capable model on the outputs of a stronger one"; "frontier AI labs routinely distill their own models to create smaller, cheaper versions" | Anthropic, 23 Feb 2026 (**read**) |
| 9 | Three labs, 16M+ exchanges, about 24,000 fraudulent accounts: DeepSeek 150k+, Moonshot 3.4M+, MiniMax 13M+ | Anthropic, 23 Feb 2026 (**read**) |
| 10 | Anthropic run rate $65B at end of July 2026 | CNBC, 17 Aug 2026 (search excerpt; page 403; not used) |
| 11 | Draft S-1: H1 2026 revenue $16.3B; net loss $80.7B, about $72B non-cash (convertible bonds); compute about $9B in H1 | WSJ review via Dealroom, 21 Oct 2026 (**read**) |
| 12 | Quarterly revenue 2026: Q1 $4.73B (Bloomberg, preliminary), Q2 $11.6B (Reuters), Q3 $16.8B (told investors) | Dealroom 21 Oct 2026 (**read**) and search excerpts |
| 13 | Compute commitments: at least $518B over a decade (Reuters); up to $750B (WSJ) | Business Today 21 Oct 2026 (**read**), Dealroom |
| 14 | OpenAI 2026: Q1 revenue about $5.7B, operating loss $9.3B; Q2 $6.7B, operating loss $12.3B | The Information, WSJ (search excerpts; one outlet says Q2 loss unconfirmed) |
| 15 | OpenAI projections: losses about $14B in 2026, first profit in 2029 | The Information (search excerpt) |
| 16 | A later leaked deck: negative free cash flow of $278B over 2026 to 2030 | FT via secondary (not used) |
| 17 | OpenAI GPT-5.5 about $5 / $30 per MTok | third-party price pages (not used, conflicting) |
| 18 | Anthropic 2025: operating loss about $8.1B on $4.6B revenue (excluding a charge) | Reuters via search excerpt (not used) |
| 19 | Distillation origin: Hinton, Vinyals, Dean, "Distilling the Knowledge in a Neural Network", 2015 | arXiv 1503.02531 (known; not opened; not used) |

## 1. Idea gate

**Scores:** surprise 4 (a hundredfold price gap for one question) · scale 5 · depth 4 · evidence 4 (pricing primary; finances from a draft filing and press) · showable 5 · plain 4. **Street-lamp:** pass: a price list does not say why the gap exists, how cheap tiers are made, or that neither lab profits. **Expert test:** output at 5x input; two index points for twice the price; the $72B non-cash share of the loss. **Against:** (1) "finance is boring" → the running example is the viewer's own question; (2) "biased channel about Claude" → OpenAI shown with the same yardstick, losses for both; (3) "numbers change" → every figure dated on screen. **Demand check:** `youtube_search.py` still HTTP 400; not run.
**Five hooks:** number "Asking Claude to summarize one contract can cost under a cent, or sixty cents. Same question, four models. Here is where that money goes." (**used**) · contradiction "The smartest Claude isn't the best deal." · fact "Every word an AI writes costs five times a word it reads." · stakes "Neither Anthropic nor OpenAI makes a profit on your questions yet." · question "Why does one AI cost a hundred times another?"

## 2. Package

- **Promise:** what each Claude tier costs and buys, how cheap tiers are made, and why neither lab is profitable yet.
- **Titles:** *One Question to Claude: Under a Cent or 60 Cents. Here's Why* (recommended) · *Claude's Model Tiers and the Money Behind AI* · *Why Neither Anthropic Nor OpenAI Makes a Profit Yet*.
- **Thumbnail (at P8):** the four 3D price pillars, Fable towering, Haiku a sliver; words "100x PRICE GAP".
- **Opening map:** scene 1 promise · scene 2 proof (the price list) and plan.

## 3. Script: 223 words, 9 scenes (take v1, rate 1.25: 62.8 s)

| Sc | Question it answers | Voice (exact text) | Delivery · pause |
| --- | --- | --- | --- |
| 1 | (hook) | Asking Claude to summarize one contract can cost under a cent, or sixty cents. Same question, four models. Here is where that money goes. | plain, curious |
| 2 | what are you paying for? | Anthropic sells four tiers: Haiku, Sonnet, Opus and Fable. You pay per token, a piece of a word, and writing costs five times reading. | steady |
| 3 | does more money buy more? | Does paying more buy more brains? Yes, but not in a straight line. On one independent index, Opus beats Sonnet by two points, for twice the price. | wry |
| 4 | how are cheap tiers made? | The cheaper tiers are possible because of distillation. A big model teaches a small one by example, and the student keeps much of the skill for a fraction of the compute. | explaining |
| 5 | what's the catch? | That is also why it gets stolen. In February, Anthropic said three Chinese labs ran millions of chats through fake accounts to copy Claude. | grave |
| 6 | do they make money? | And the business? Anthropic's draft filing shows billions in revenue each quarter, hundreds of billions promised for computing, and still a loss. | even |
| 7 | and OpenAI? | OpenAI runs the same race: revenue up every quarter, losses deeper, and its own forecasts put profit years away. | even |
| 8 | so what do I do? (solution) | So spend like a lab. Pick the smallest tier that does the job, and reuse what the model already read: cached input costs a twentieth. | brighter; break 0.2 after "lab" |
| 9 | so what? | So here is the point: you buy intelligence by the word, and neither lab has turned that into profit yet. Which tier do you use? Tell me. | slower; break 0.2 after "yet" |

**Honesty:** "cost under a cent, or sixty cents": the illustrative contract at list prices, on screen. "The cheaper tiers are possible because of distillation": Anthropic says labs routinely distill their own models; it has not said how each tier was trained (said generally, not per model). "still a loss": net loss $80.7B, most of it non-cash, on screen. OpenAI quarter figures are press reports (one unconfirmed), labelled. "a twentieth": Opus 5.5 cache hits, on screen. Facts used: 5.

## 4. Beat sheet, prefix `me`

3D pillars (height = output price) are the anchor: hook (Haiku and Fable rising from frame 1, middle two on "four", contract cost tags), solution (Fable and Opus dim on "smallest", mint arrows to Sonnet, cache ring on "reuse", sparks on "cached", mint flood) and close. 2D: read and write coins (1 vs 5) on "writing"; honest index chart (0 to 60) with two dots nearly level and far apart; Anthropic revenue bars on "billions" and the $518B+ compute tower on "hundreds"; OpenAI revenue up and loss bars down. 3D: teacher and student icosahedrons with lessons flowing on the beat; a ring of fake accounts siphoning into a rose copy on "copy".

## 5. Not verified

OpenAI's 2026 quarter figures and 2029 profit forecast (press reports, not opened); the S-1 is a confidential draft and can change; Artificial Analysis gives no date on the page; demand. How the voice sounds. P7 is the user's.
