---
type: process
created: 2026-10-27
updated: 2026-10-30
status: v3 · shipped (user, 30 Oct 2026), not uploaded
tags: [status, week-04]
---

# How RAG works · Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

← [[Script - How RAG works]] · [[YouTube Channel]] · [[Production]]

**Request (user, 27 Oct 2026):** *"add https://github.com/lucasmarkes/hairline and modify the vault so it uses this new tool along with the rest. then generate a new short: how rag works."* **Clarifying questions** ([[Production]] *Clarify first*, a rule set in the same message): angle **"Deeper mechanism"** (one level below [[RAG explained - Status]]: passages, map of meaning, nearest match, pasted into the prompt); real case **"Stanford legal AI study"**; gate **"Delegated to render"** (overrides *Ship before you build*: about ten renders wait at P7, none uploaded); Hairline **"Mechanism worlds"**. P1 to P7, cap **$0.06** (one take about $0.02, one retake, whisper $0.01; no generated media). Short test block, standard slot (AI slop rule took the compact one).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 27 Oct 2026 | How it works · hook type: stakes · theme line *nearest is not always right* · real case Magesh et al. (Stanford RegLab and HAI, May 2024) · street-lamp: pass (see Script) · demand: not run (YouTube token HTTP 400 since 26 Oct 2026) |
| 4 Prompts, stock, budget | approved by delegation | 27 Oct 2026 | no generated media; Hairline figures (MIT, vendored 0.5.1), Fluent Emoji 3D (MIT), real pages shot with headless Chrome ($0) |
| 6 Generation | done | within the cap | Take v1 `00bz8tb3bxrmt0d1fyjb3mhgcg` (801 characters with direction): 38.9 s, whisper heard all 130 words; caption spellings fixed ("Lexus" to Lexis, "made -up", "catch?"); silences 0.20 to 0.57 s, none inside a clause. Timings `ptjwk9eg0hrmt0d1fyjak42j28`. Spend about **$0.03** |
| 7 Edit | done, **shipped (user, 30 Oct 2026)** | | `Media/Week 04/2026-10-27 Tue/How RAG works/render/hr-40s-9x16-r1.mp4` (40.3 s, HyperFrames 2D + Hairline, hfkit). Seven scenes, five worlds: the real "hallucination-free" line and the HAI headline, struck; look up / page / answer; **Hairline riffle** (cards, the anchor) shrinking into **terrain** (the map); the question drops on the terrain and pillars rise; **stack** (cards above the lit question); riffle with the rose card and the paper's own passage; riffle with the mint card and the comment prompt. `check3d.mjs`: OVERLAPS 0, no WARN. `hyperframes check` passed; snapshots and the contact sheet of the mixed mp4 looked at. Mix −14.0 LUFS, true peak −2.4 dBTP. **Slideshow-risk score 1** (repetition 1: the riffle on 3 tiles, each in a new state). `MOTION SHARE` not measured (no HyperFrames counter). Caption key colour: "wrong" in scene 1 is lit blue (the key colours the doctrine's words). Publish pack built (dry run; thumbnail WRONG CARD, checked at 168 px and 3:2) |
| 7 Edit r2 | done, **shipped (user, 30 Oct 2026)** | | `render/hr-40s-9x16-r2.mp4` (same take, $0). Every emoji replaced: hook = the riffle of citations under the real claim and the HAI headline (a card pulls rose on "wrong"); definition = Hairline `drawer` with callouts *look up* and *answer*; then riffle, terrain, stack, riffle rose, riffle mint as in r1, hosts enlarged so drawings span about 60 % of the width. New information layers ([[Look]] *Information on screen*): pipeline rail cut · map · fetch · paste from "here is how" (fetch turns rose on the catch, mint at the close); callouts with leaders replace floating labels; the question is a tag that drops onto the map; cards are line panels; the comment prompt's bubble is line-drawn. `check3d.mjs`: OVERLAPS 0, no WARN; mix −14.0 LUFS, true peak −2.4 dBTP; contact sheet of the mixed mp4 looked at. **Slideshow-risk score 1** (repetition 1: the riffle holds the last five tiles, the anchor returning in three states with a tag, a rose callout, a mint callout). Publish pack refreshed (r2) |
| 7 Edit r3 to r5 | done, **shipped (user, 30 Oct 2026)** | | User (27 Oct 2026): *"Use this new figure on the last video, and create 2 new ones"*. **r3:** the paste scene's stack replaced by the custom `window` figure (frame of 9 blocks glides over the prompt tape; callouts *cards* and *question*; panel detail "It reads only what is in its window"). **r4:** `hfkit` turns off Hairline's real-time stroke fades, which lagged behind the captured frames (rose and mint cards now light on their frame). **r5:** the hook's tray no longer pulls a card before "wrong", so the rose card lands on the word. `render/hr-40s-9x16-r5.mp4`; `check3d.mjs` OVERLAPS 0; mix −14.0 LUFS, true peak −2.4 dBTP; publish pack points to r5. Four more custom figures (balance, temperature, splitter, loop) were made for later Shorts, not used here ([[Look]] *Figure library*) |
| 8 Publish · 9 Measure | | | |

**Known simplifications:** "map of meaning" = embedding vectors, nearness = similarity score (schematic); "the nearest cards rise" = top-k retrieval (the 2020 paper used k of 5 or 10); how Lexis+ AI builds its index is not public, so the video shows the general method the Stanford paper draws (its Figure 3).

**Feedback** (user, 27 Oct 2026, on r1): *"Way better, i think those icon-like illustrations can be removed, use hairlines. redesign the way info is showed on the screen and improve the last short"*: written into [[Look]] Illustrations, [[Format]] (old Playbook §3), [[Look]], [[Growth]] *Plain-words map*; r2 answers it.

*Not verified:* the exact query text Lexis+ AI received for doctrine-test-177 (the paper names the source it relied on, not the full answer).
