---
type: process
created: 2026-10-27
updated: 2026-10-27
status: v3 · refocused on Agent Skills, rendered r4; waiting for the user (P7)
tags: [status, week-04]
---

# MCP vs skills · Status

← [[Script - MCP vs skills]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 27 Oct 2026):** *"New short: explain the diference between an mcp and skill and mention some examples. interesting less known usages, be creative"*. P1 to P7, cap **$0.06** (one take, one retake, whisper). Uploads are paused by the user (RAG explained, HyperFrames: "upload later"), so [[Production]] *Ship before you build* does not stop this video. Third video of the short test block; after the story rewrite it is a 110 to 130-word video, and the next video takes the compact slot.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 27 Oct 2026 | v2: How it works · hook type: stakes · message *can't reach it, or doesn't know how?* · running example: Claude posting a birthday GIF in Slack (illustrative), with the real `slack-gif-creator` skill and our real `claude mcp list` · street-lamp: pass · demand: autocomplete yes, outliers not run (token 400) |
| 4 Prompts, stock, budget | approved by delegation | 27 Oct 2026 | no generated media; Fluent Emoji 3D (MIT); real text from `claude mcp list` and two real SKILL.md files |
| 6 Generation | done | within the cap | Take v1 `4s5dbpd0r9rmr0d1fsftjnk7br` (555 characters): 30.0 s, whisper heard all 85 words; silences 0.25 to 0.61 s, none inside a clause. Whisper spellings fixed for captions in `ms-take-v1.words.json` (Gidra to Ghidra, know -how to know-how, slack gifs to Slack GIFs). Timings `jdkkkkpvndrmt0d1fsfrcv3mxw`. Spend about **$0.02** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-27 Tue/MCP vs skills/render/ms-32s-9x16-r2.mp4` (31.6 s, HyperFrames 0.8.200, 2D, hfkit). Four worlds: plug and scroll around the agent; real `claude mcp list` (shortened), Blender dragon on gold, Ghidra lens on a gear; real `slack-gif-creator` header with the description lit, counter 36 to 1,103 words, caveman with its real header; the agent between new app and new habit, comment prompt. `check3d.mjs` OVERLAPS 0, no WARN (fixed: caveman panel in the caption band, card ids). r1 deleted unseen: it showed 37 words, the real count is 36. Mix −14.0 LUFS, true peak −2.5 dBTP; contact sheet looked at. **Slideshow-risk score 1:** decoration 1 (the GIF frame alone for about 1.5 s), all else 0. Publish pack built (`upload/ms-publish-pack.md`, dry run) |
| 6b Generation v2 | done | within the cap | Take v2 `ymattz2w9hrmt0d1fsvv56xdp8` (648 characters): 38.9 s, whisper heard all 131 words; silences up to 0.62 s. Caption spellings fixed ("1." and "2." to one and two, "and MCP" to "An MCP", know-how). Total spend about **$0.05** of $0.06 |
| 7b Edit r3 (story) | done, **waiting for the user (P7)** | | `render/ms-41s-9x16-r3.mp4` (40.6 s). Five worlds: the stuck agent; the task (Claude, cake, GIF, Slack, message, stop); reach (wall to plug, real `claude mcp list`, check on post); know-how (GIF, ruler, Slack's real rule; folder, scroll; real header with the description lit and 36 to 1,103 words); the question (plug and scroll, comment prompt). `check3d.mjs`: OVERLAPS only `z-ask` at one sample (38.0 s, during its rise; kept), no WARN (fixed: sparse W2 start and W3, panel in the band). Mix −14.0 LUFS, true peak −1.9 dBTP; contact sheet and frames looked at. **Slideshow-risk score 1:** weak motion 1 (the close holds about 3 s), all else 0. Pack rebuilt (`upload/ms-publish-pack.md`, dry run) |
| 6c Generation v3 | done | over the cap, see note | Take v3 `9mbs8h2nr9rmw0d1ft4r9yphcr` (about 630 characters): 34.5 s, whisper heard all 117 words; silences up to 0.58 s. **Spend about $0.08 in all against the $0.06 cap**: the two redos the user asked for (v2, v3) each took a take and a timing call; no further spend without approval. A real run of the skill's code (to show a GIF it made) was blocked by the auto-mode classifier (downloaded code); the video makes no run claim |
| 7c Edit r4 (skills only, dynamic) | done, **waiting for the user (P7)** | | `render/ms-36s-9x16-r4.mp4` (36.2 s). Six worlds, each with a scale change: a text file flies into Claude (+1 job); zoom into the folder, real tree; real header, description lit, counter to 36, rest dim; 100 scrolls collapse beside 3 full files (card 100 x 36 = 3,600); ask, match, the rules panel springs open, each rule on its number; agent and manual, comment prompt. `check3d.mjs`: OVERLAPS only `z-ask` at one sample (33.5 s, during its rise), no WARN. Mix −14.0 LUFS, true peak −2.7 dBTP; sheets and frames looked at. **Slideshow-risk score 1:** text doing the picture's job 1 (the rules panel), all else 0. Pack rebuilt (title *AI Agent Skills Explained: How Claude Learns a New Job*, thumbnail +1 JOB) |
| 8 Publish · 9 Measure | | | |

*Not verified:* how the voice says "MCP"; caption timing in motion; outlier demand. Seen risks: frame 1 near empty for about 0.25 s; the lower stage is often empty in worlds 3 to 5.

## Feedback

User on r2 (27 Oct 2026): *"Narrative and structure is not well composed and pointless, just a plain comparison table. we need more narrative, storytelling and message. redo the script. you're making videos to people that is actually learning about that"*. Owning rule edited: [[Format]] (old Playbook §2) *A comparison is a story*. Script v2 (131 words), take v2, worlds rebuilt as one task.

User on r3 (27 Oct 2026): *"Refocus the video. ai agent skills explained. make it more dynamic. more engaging"*. Owning rules edited: [[Format]] (old Playbook §3) (an event every 1.5 to 2 s, one scale change per world), with [[Look]], [[Look]] and `CLAUDE.md`. Script v3 (117 words) on skills alone.
