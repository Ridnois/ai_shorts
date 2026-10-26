---
type: process
created: 2026-10-26
updated: 2026-10-26
status: v2 · rendered r2 (holistic), waiting for the user (P7)
tags: [status, week-04]
---

# Model economics · Status

← [[Script - Model economics]] · [[YouTube Channel]] · [[Workflow]]

**Delegation (user, 26 Oct 2026):** *"Using all the tools you got now for 3d animation and make a new short ..."* (full words in the Script). Run P1 to P7 by the Workflow default, cap $0.25 as on the earlier videos today; stop at the render.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Series What's coming. Hook type: surprising number. Theme line: *you buy intelligence by the word*. Street-lamp: pass. Demand check not run (`youtube_search.py` HTTP 400). Prices from the live pricing page; finances from the draft S-1 press coverage. 223 words, 9 scenes |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | base about $0.045 (one take of 1,397 characters, one timing call), cap $0.25; 0 generated media, 0 photos |
| 6 Generation | done | within the cap | Take v1 (Dennis, rate 1.25; id in `voice/_log.txt`): 62.8 s, 223 words, about 213 wpm, silences 0.25 to 0.56 s. Whisper heard the co-articulated "Anthropic said" / "Anthropic's" as "Anthropix" (kept: the same word run together; captions use the script spelling). Spend about **$0.045** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-26 Mon/Model economics/render/me-64s-9x16-r1.mp4` (64.1 s, 1080×1920, 30 fps; HyperFrames 0.8.200 + three.js 0.181.2; render 4 m 02 s). 3D only for the price pillars (hook, solution, close) and teacher/student distillation; charts and coins in 2D. `check3d.mjs` **OVERLAPS 0** (first build found 23 kinds: a full-frame SVG tagged as text, pillar labels framed by the stage's short side, labels on bars, a label inside the accounts ring); `hyperframes check` ok. Mix **−14.0 LUFS, true peak −2.7 dBTP**, no music. Final mp4 frames looked at |
| 7b Edit r2 (holistic) | done, **waiting for the user (P7)** | | User on r1: *"Make it more holistic, like explaining plan tipes and it capabilities too, how profitable are the actual plans for anthropic and suggestions"*. Takes v2 ("Free is chat" heard as "Free as chat": reworded) and **v3 used**: 65.1 s, 230 words, silences 0.25 to 0.67 s. Spend so far about **$0.12** (3 takes, 3 timings). `render/me-66s-9x16-r2.mp4` (66.5 s; render 5 m 09 s). 3D: $200 coin against a stacking compute tower (hook), price pillars (models, close), teacher and cheap tier, a buffet of 12 user columns with agents towering until the mint weekly-limit lid clamps them. 2D: index chart, plan ladder (Free, Pro, Max, Team and Enterprise with capabilities on their words), revenue against compute shares (labelled unconfirmed), both labs' bars, colourful choice lanes (solution). `check3d.mjs` OVERLAPS 0 (4 kinds at the lid fixed by retiring two labels); `hyperframes check` ok. Mix −14.0 LUFS, true peak −3.1 dBTP. Final mp4 frames looked at |
| 8 Publish · 9 Measure | not started | | |

*Fixes found in frames, not by the checker:* the money bars were hidden by an id-prefix selector, the hook card was hidden on frame 1, theft accounts too small; all fixed before the render. `build.py` also got a guard: a scene start whisper spells differently made the matcher loop forever.

*Schematics:* pillar heights are list output prices; the contract and its costs are illustrative; teacher, student and the accounts ring are drawn models, not any lab's system.

*Not verified:* the voice; caption timing; pace in motion; OpenAI figures beyond press reports. Seen risks: first caption at 0.15 s; the lower lane is empty in a few stretches (theft before its card, OpenAI before its card).
