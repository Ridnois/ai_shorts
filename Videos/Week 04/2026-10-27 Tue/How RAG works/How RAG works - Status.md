---
type: process
created: 2026-10-27
updated: 2026-10-27
status: v1 · rendered r1 (40.3 s); waiting for the user (P7)
tags: [status, week-04]
---

# How RAG works · Status

← [[Script - How RAG works]] · [[YouTube Channel]] · [[Workflow]]

**Request (user, 27 Oct 2026):** *"add https://github.com/lucasmarkes/hairline and modify the vault so it uses this new tool along with the rest. then generate a new short: how rag works."* **Clarifying questions** ([[Workflow]] *Clarify first*, a rule set in the same message): angle **"Deeper mechanism"** (one level below [[RAG explained - Status]]: passages, map of meaning, nearest match, pasted into the prompt); real case **"Stanford legal AI study"**; gate **"Delegated to render"** (overrides *Ship before you build*: about ten renders wait at P7, none uploaded); Hairline **"Mechanism worlds"**. P1 to P7, cap **$0.06** (one take about $0.02, one retake, whisper $0.01; no generated media). Short test block, standard slot (AI slop rule took the compact one).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 27 Oct 2026 | How it works · hook type: stakes · theme line *nearest is not always right* · real case Magesh et al. (Stanford RegLab and HAI, May 2024) · street-lamp: pass (see Script) · demand: not run (YouTube token HTTP 400 since 26 Oct 2026) |
| 4 Prompts, stock, budget | approved by delegation | 27 Oct 2026 | no generated media; Hairline figures (MIT, vendored 0.5.1), Fluent Emoji 3D (MIT), real pages shot with headless Chrome ($0) |
| 6 Generation | done | within the cap | Take v1 `00bz8tb3bxrmt0d1fyjb3mhgcg` (801 characters with direction): 38.9 s, whisper heard all 130 words; caption spellings fixed ("Lexus" to Lexis, "made -up", "catch?"); silences 0.20 to 0.57 s, none inside a clause. Timings `ptjwk9eg0hrmt0d1fyjak42j28`. Spend about **$0.03** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-27 Tue/How RAG works/render/hr-40s-9x16-r1.mp4` (40.3 s, HyperFrames 2D + Hairline, hfkit). Seven scenes, five worlds: the real "hallucination-free" line and the HAI headline, struck; look up / page / answer; **Hairline riffle** (cards, the anchor) shrinking into **terrain** (the map); the question drops on the terrain and pillars rise; **stack** (cards above the lit question); riffle with the rose card and the paper's own passage; riffle with the mint card and the comment prompt. `check3d.mjs`: OVERLAPS 0, no WARN. `hyperframes check` passed; snapshots and the contact sheet of the mixed mp4 looked at. Mix −14.0 LUFS, true peak −2.4 dBTP. **Slideshow-risk score 1** (repetition 1: the riffle on 3 tiles, each in a new state). `MOTION SHARE` not measured (no HyperFrames counter). Caption key colour: "wrong" in scene 1 is lit blue (the key colours the doctrine's words). Publish pack built (dry run; thumbnail WRONG CARD, checked at 168 px and 3:2) |
| 8 Publish · 9 Measure | | | |

**Known simplifications:** "map of meaning" = embedding vectors, nearness = similarity score (schematic); "the nearest cards rise" = top-k retrieval (the 2020 paper used k of 5 or 10); how Lexis+ AI builds its index is not public, so the video shows the general method the Stanford paper draws (its Figure 3).

*Not verified:* the exact query text Lexis+ AI received for doctrine-test-177 (the paper names the source it relied on, not the full answer).
