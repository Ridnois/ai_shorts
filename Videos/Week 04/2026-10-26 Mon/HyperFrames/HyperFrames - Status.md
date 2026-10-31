---
type: process
created: 2026-10-26
updated: 2026-10-30
status: v2 · shipped (user, 30 Oct 2026), public 27 Oct 2026
tags: [status, week-04]
---

# HyperFrames · Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**; public 27 Oct 2026 ([`4YuqDYQYGBg`](https://youtu.be/4YuqDYQYGBg)).

← [[Script - HyperFrames]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 26 Oct 2026):** *"New short: explain hyperframes to web and youtube short"* (read as: how HyperFrames turns a web page into a YouTube Short). P1 to P7, cap **$0.06** (one take, one retake, whisper). Uploads are paused by the user, so [[Production]] *Ship before you build* does not stop this video. Second video of the short test block.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Agent at work · hook type: contradiction · theme line *a page you can film* · real case: our own run (Claude Code wrote the HyperFrames page for *RAG explained*) · street-lamp: pass (the README says what, not the seek-per-frame mechanism shown on a real Short) · demand check: not run (token) |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | no generated media; real frames and real code from *RAG explained*, Fluent Emoji 3D (MIT) |
| 6 Generation | done | within the cap | Take v1 `nabak775ksrmw0d1fcxvxd0w8c` (832 characters): 43.3 s, whisper heard all 137 words ("one, two, thirty" as digits, "web pages" as "webpages"), silences up to 0.67 s. Spend about **$0.03** |
| 7 Edit | done, **shipped (user, 30 Oct 2026)** | | `Media/Week 04/2026-10-26 Mon/HyperFrames/render/hy-45s-9x16-r1.mp4` (44.7 s, HyperFrames 0.8.200, 2D). Real proof: 7 frames and 4 code lines of *RAG explained* r2; Fluent Emoji 3D (MIT) for page parts, hidden browser, camera, encoder, outputs. `check3d.mjs` OVERLAPS 0, no WARN (fixed before render: labels past x 950, a label overlapping the film strip, sparse openings of scenes 3 and 5). Re-rendered once: the crossed-out editor landed on the scene's last word (0.4 s on screen), now on "no". Mix −14.1 LUFS, true peak −2.0 dBTP; final mp4 frames looked at. **Slideshow-risk score 1:** weak motion 1 (the code panel holds about 5 s), all else 0 |
| 7b Edit r2 (comment prompt, spacing) | done, **shipped (user, 30 Oct 2026)** | | User on r1 (27 Oct 2026): *"Redesign margin notes and rerender, the rest is good, also improve spacing"*. The closing card became the **comment prompt** ([[Look]]): speech balloon, the question, three answer chips popping on "Tell me" (an explainer, an ad, a story), "reply in the comments". Spacing: every three-item row on one grid (centres x 210, 503, 796), labels 20 px under their pictures, the close moved down to the middle of the stage, encoder row symmetric. `check3d.mjs` OVERLAPS 0, no WARN. `render/hy-45s-9x16-r2.mp4` (44.7 s); mix −14.1 LUFS, true peak −2.0 dBTP; final mp4 frames looked at. Spend unchanged (**$0.03**) |
| 7c Builder on hfkit (27 Oct 2026) | done | | `hf/build.py` now imports `System/scripts/hfkit.py` ([[Look]]); 314 to 117 lines; snapshots at 15 moments identical to r2 pixel for pixel, same `_timeline.json`, `check3d.mjs` OVERLAPS 0. The r2 mp4 is unchanged |
| 8 Publish · 9 Measure | public 27 Oct 2026 ([`4YuqDYQYGBg`](https://youtu.be/4YuqDYQYGBg)); row in `Analytics/videos.csv` | | |

*Not verified:* the voice (how "HyperFrames" and "HTML" sound); phrase-caption timing in motion; the open-source date (third-party). Seen risks: scene 1's real frame is small inside the phone at phone size; each cut has a 0.4 s near-empty cross-fade.
