---
type: process
created: 2026-10-26
updated: 2026-10-26
status: v2 · rendered r2 (slower, re-laid out), r1 kept; waiting for the user (P7)
tags: [status, week-04]
---

# Chatbot vs agent · Status

← [[Script - Chatbot vs agent]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 26 Oct 2026):** *"Horrible, unnecesary 3d models. unclear diferentiation. go simpler, ai chatbot vs ai agent"*. Replaces the superseded *Free or paid* (notes deleted 27 Oct 2026, in git history); P1 to P7, cap $0.25. The verdict on 3D became a [[Look]] rule (3D is the exception).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Series How it works. Hook type: contradiction. Theme line: *you are the loop; it is the loop*. 197 words, 7 scenes |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | base about $0.04; logos reused from Free or paid |
| 6 Generation | done | within the cap | Take v1 (id in `voice/_log.txt`): 51.0 s, whisper heard every word (one "Cloud Code"), silences 0.26 to 0.54 s. Spend about **$0.04** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-26 Mon/Chatbot vs agent/render/ca-52s-9x16-r1.mp4` (52.3 s; HyperFrames 0.8.200, **2D only, no three.js**; render 2 m 26 s). `check3d.mjs` OVERLAPS 0 (first build clean after three layout fixes found before building); `hyperframes check` ok. Mix −14.0 LUFS, true peak −2.7 dBTP. Final mp4 frames looked at |
| 7b Edit r2 (pace, layout) | done, **waiting for the user (P7)** | | User on r1: *"Timing is a little too fast, not enough spaces between phrases, longer it a little bit. also position of the elements is not quite right, improve that"*. Take v2: rate 1.1 (rule updated in [[Format]] (old Playbook §5) and `CLAUDE.md`), 70.0 s, 217 words, pauses mostly 0.5 to 0.72 s (r1: 0.26 to 0.54). Spend so far about **$0.08**. Layout: everything inside x 56 to 950 (r1 had the hook cards, plan columns, safe-copy box, closing rows and the **context card itself** past x 950, the platform's button strip; the card CSS was 93 to 987 in every HyperFrames video, now at the Style spec 56 to 950); larger ring and hub; goal chip moved to the lower lane until the card replaces it; no spring overshoot on full-width rows. `check3d.mjs` gained the right-strip (x > 950) and bottom-zone (y > 1440) checks: OVERLAPS 0. `render/ca-71s-9x16-r2.mp4` (71.4 s; render 3 m 13 s); mix −14.0 LUFS, true peak −2.1 dBTP. Final mp4 frames looked at |
| 8 Publish · 9 Measure | pack ready (`upload/ca-publish-pack.md`, thumb YOU vs AGENT), awaiting approval of title, description, thumbnail, private | | |

*Not verified:* the voice; caption timing. Seen risks: first caption at 0.15 s; the close's first second before "answer" shows only the flooded ground; 51 s is shorter than the other cuts.
