---
type: rules
updated: 2026-11-03
status: v2 · 3 Nov 2026 vault rebuild. Owns who we make for, what we make, how ideas are found and scored, the package and the policy. Replaces Growth (audience, ideas, package, policy) and Format §1–2; built on the channel research of 3 Nov 2026 (Research/Channels)
---

# Strategy: who, what, which idea, which package

The words: [[Story]]. The picture: [[Picture]]. How it is built and shipped: [[Build]]. What the numbers say: [[Data]]. The user's own research notes: [[User insights]].

## Audience and promise

Curious adults who use ChatGPT, Claude or Gemini every week and feel they are missing how it works or how others use it so well. Also developers and knowledge workers who want agents to do real work. Plain words first; the expert gets one detail they did not know.

**Y and X** ([[User insights]]): Y is the result the viewer already wants (stop being fooled, get more done, see the change coming). X is the mechanism that blocks it. The title sells Y; the video teaches X. **News is the case, never the video:** a launch or incident opens a mechanism that is still true in a year.

**Where we stand** (Research, 3 Nov 2026): most AI-news channels post no Shorts at all (AI Explained, TheAIGrid, Wes Roth, AI Revolution, MattVidPro, per [[Radar]] §Shorts use). The animated "how AI works" Short is a thin slot; Coding with Lewis, ByteByteGo and 3Blue1Brown are the ones doing it well. That is our lane.

## Series (each video belongs to one; two in a row never share one)

| Series | Promise | Example title |
| --- | --- | --- |
| **How AI works** | the mechanism behind something people see AI do | "Why ChatGPT can't count the r's in strawberry" |
| **Agent at work** | a real recorded run of an AI tool doing a task, and the one trick that made it work | "I let Claude Code fix a bug while I watched" |
| **What's coming** | a change with evidence: compute, energy, jobs, rules | "Why AI companies are buying nuclear plants" |

Off-niche videos (no AI in the mechanism) are not made: the Antibiotics Short (29 Oct 2026) was the last.

## Hooks: the pattern library

Every video names one pattern in its Status and `publish.json` (`hook_pattern`). These are the patterns behind outliers on the watchlist ([[Channels]]). Ratios are views ÷ the channel's median, from vidIQ public stats or [[Radar]], read 3 Nov 2026. Our column: median engaged views and average % viewed at the newest snapshot, from the [[Data]] review of 3 Nov 2026 (our median: 368 engaged at 7 d). It beats the outside column once a pattern has 3 videos.

| id | Pattern | Outside evidence | Fits | Our results |
| --- | --- | --- | --- | --- |
| `limit-mystery` | a limit or failure nobody fully explains | Welch Labs "AI can't cross this line and we don't know why" 2.52 M, 30x | How AI works | 826 engaged, 59 % viewed (n=1) |
| `name-it` | give a name to a behaviour or a new term, at its spike | Coding with Lewis "There's a Name for People Who Paste AI Responses at You" 1.80 M, 37x; IBM "What Is Jev?" 1.27 M, 53x | How AI works, Agent at work | 195, 55 % (n=1) |
| `incident` | a named real case with a consequence | Zack D. Films "The Pepsi Contest That Killed 5 People" 12 M; our "Agent deleted a database" | Agent at work | 721, 51 % (n=3) |
| `cost-why` | why X costs, uses or needs so much | Computerphile "Why AI Tokens are so Expensive" 864 k, 11x | What's coming, How AI works | 658, 72 % (n=2) |
| `stakes` | a line crossed, now what | Kurzgesagt "AI Just Crossed the Terrifying Line, Now What?" 23.4 M, 12x | What's coming | 363, 56 % (n=2) |
| `stunt` | a physical or visual demonstration of an abstract idea | Art of the Problem "I Gave ChatGPT a Body" 5.48 M, about 440x | Agent at work | under 100 views (n=2) |
| `ranking` | an iceberg, tier list or three-way comparison | Coding with Lewis "The AI Model Iceberg" 1.70 M, 35x; ByteByteGo "gRPC, WebSocket and WebHook!" 362 k | How AI works | no readable data (n=1) |
| `surprising-result` | a true result that contradicts what the viewer assumes | our "Lottery ticket", "Quantization explained" | How AI works | 703, 60 % (n=4) |
| `news-why` | a real decision explained ("why X chose Y") | our "Rust checks AI code" | Agent at work | 706, 60 % (n=1) |

**What does not work outside:** a paper headline as a Short (bycloud's paper Shorts sit near 0.3x their median). A plain launch report competes with every AI channel on the same day (the "GPT-6 Astra" launch week, Sept 2026, topped Fireship, AI Explained, Two Minute Papers and Matt Wolfe at once). Spectacle beats model news in the feed (Matt Wolfe's flying-car Short, 1.9 M, against about 2.6 k for his model-news Shorts).

## Ideas (outliers and signals, not guesses)

1. **Radar** (weekly, about 100 quota units): `python3 System/scripts/radar.py pull && python3 System/scripts/radar.py report` scores every recent upload of the watchlist against its channel's same-format median, and writes [[Radar]]. A row at 3x or more is demand. Rows marked `early` are leads only.
2. **Signals** (weekly, free): `python3 System/scripts/signals.py` writes [[Signals]], covering Hacker News, Reddit, Hugging Face papers and GitHub trending. A rising term no watchlist video has explained is a `name-it` candidate, the IBM "What is Jev?" pattern. A signal is never demand by itself.
3. **Deep-first** ([[User insights]]): from the best outlier, open its channel's other outliers and the related questions. Stop when topics repeat. Write **why** people clicked (a result they want, faster than expected, an unfair-advantage feeling); never copy words or looks.
4. **One-off search** for a plain question: `youtube_search.py "<q>" --short --min-ratio 3` (100 units a query). New channels: `radar.py discover "<q>"`, then add the row to [[Channels]].
5. Also free: YouTube Studio's Research tab, autocomplete, the AI Incident Database, lab blogs and system cards.

## The idea passes 4 tests, then gets a score

**Tests** (5 minutes): (1) **real thing**: a named product, company, person or incident, dated; (2) **curiosity gap**: a stranger who uses ChatGPT says "wait, why?" to the one-line claim; (3) **demand**: 2 or more outliers at 3x or more on the same question (in [[Radar]] or `youtube_search.py`), or the question autocompletes; (4) **showable**: a medium in [[Picture]] §Medium shows the mechanism.

**Score** (out of 20, written in the idea note):

| Part | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Demand | autocomplete only | 2 outliers at 3x+ | 4+ outliers, or one at 20x+ |
| Own fit | the pattern and series are below our median engaged views | no own data yet | the pattern and series are above our median |
| Showable | only said, or a generic picture | a figure or capture shows part of it | a primitive or a real run shows the whole mechanism |
| Real thing | a vague trend | a named, dated case | a named case with a number and a consequence |

The next video is the top score whose series differs from the last one.

## Package

- **Title** (100 characters or fewer; 40 to 60 is best): the plain search words first, a named thing, the curiosity gap; no all caps, no emoji. "Why ChatGPT can't count letters", not "The hidden truth about tokens". Before the pack, put the title next to the 5 nearest [[Radar]] outlier titles: it must give the right viewer a clearer reason to choose it ([[User insights]]).
- **Frame 0 is the real thumbnail** in the Shorts feed: the hook's picture plus 3 to 5 words. A custom thumbnail (`v.thumb`) shows only on the channel page, search and home.
- **Description:** first line = the claim with the search words; sources with links; the channel line; 2 to 3 hashtags (`#AI` plus one topic tag). **Tags:** 5 to 10 search phrases.
- **Pinned comment:** one question the viewer can answer in a word.
- **Cadence:** Mon to Fri at one fixed hour (15:00 UTC unless [[Data]] says otherwise), never two on one day.
- **TikTok** (manual, not measured since 3 Nov 2026, the user's decision): upload `upload/*-tt.mp4` from TikTok Studio on the web, caption from the pack, no TikTok library sound; the keyword in the voice, the screen text and the caption.

## Policy

- **Inauthentic content** (YouTube, renamed 15 Jul 2025): videos that are "mass-produced, generic, repetitive" lose monetisation channel-wide. So do "templated storylines" and "AI-generated content made with generic or unoriginal templates". Defence: every video has a distinct real case, an original figure or capture, a real argument and a sourced number. The brand is consistent; the videos are not interchangeable ([[Picture]] §Bar, *Varied*).
- **Disclosure:** the "altered or synthetic" label is for realistic generated people, places or events. Drawn animation with a stock TTS narrator does not need it (`synthetic: false`). Set `synthetic: true` when a realistic generated still or clip appears ([[Picture]] §Medium). Never clone a real person's voice. The description carries an AI line either way.
- **Partner Program:** 1,000 subscribers plus 10 M engaged Shorts views in 90 days, or 4,000 public watch hours in 12 months.
- **No malicious clickbait:** the hook promises only what the video shows. Claims about a model, price or feature are re-checked if the render is over 30 days old.

## Sources

Channel research of 3 Nov 2026: vidIQ public stats pages (last 48 uploads) and the YouTube Data API (`channels.list`, [[Channels]]). YouTube inauthentic content policy (support.google.com/youtube/answer/1311392). Paddy Galloway and Chris Gileta's Shorts study (5,400 Shorts, 33 channels; before the 2025 view change). Third-party tool and retention blogs are treated as direction, never as numbers on screen.
