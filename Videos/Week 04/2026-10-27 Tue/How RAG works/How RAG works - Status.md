---
type: process
created: 2026-10-27
updated: 2026-10-27
status: v1 · in generation
tags: [status, week-04]
---

# How RAG works · Status

← [[Script - How RAG works]] · [[YouTube Channel]] · [[Workflow]]

**Request (user, 27 Oct 2026):** *"add https://github.com/lucasmarkes/hairline and modify the vault so it uses this new tool along with the rest. then generate a new short: how rag works."* **Clarifying questions** ([[Workflow]] *Clarify first*, a rule set in the same message): angle **"Deeper mechanism"** (one level below [[RAG explained - Status]]: passages, map of meaning, nearest match, pasted into the prompt); real case **"Stanford legal AI study"**; gate **"Delegated to render"** (overrides *Ship before you build*: about ten renders wait at P7, none uploaded); Hairline **"Mechanism worlds"**. P1 to P7, cap **$0.06** (one take about $0.02, one retake, whisper $0.01; no generated media). Short test block, standard slot (AI slop rule took the compact one).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 27 Oct 2026 | How it works · hook type: stakes · theme line *nearest is not always right* · real case Magesh et al. (Stanford RegLab and HAI, May 2024) · street-lamp: pass (see Script) · demand: not run (YouTube token HTTP 400 since 26 Oct 2026) |
| 4 Prompts, stock, budget | approved by delegation | 27 Oct 2026 | no generated media; Hairline figures (MIT, vendored 0.5.1), Fluent Emoji 3D (MIT), real pages shot with headless Chrome ($0) |
| 6 Generation | | | |
| 7 Edit | | | |
| 8 Publish · 9 Measure | | | |

**Known simplifications:** "map of meaning" = embedding vectors, nearness = similarity score (schematic); "the nearest cards rise" = top-k retrieval (the 2020 paper used k of 5 or 10); how Lexis+ AI builds its index is not public, so the video shows the general method the Stanford paper draws (its Figure 3).

*Not verified:* the exact query text Lexis+ AI received for doctrine-test-177 (the paper names the source it relied on, not the full answer).
