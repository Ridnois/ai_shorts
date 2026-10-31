---
type: process
created: 2026-10-26
updated: 2026-10-30
status: v1 · shipped (user, 30 Oct 2026), not uploaded
tags: [status, week-04]
---

# ThinkPad TrackPoint · Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

← [[Script - ThinkPad TrackPoint]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 26 Oct 2026):** *"Make a new short with hyperframes ... topic: Why thinkpads are so special"*; at the agent's questions the user chose **"One-off, mechanism angle"** (off-niche, How it works structure, no series) and **"Delegate to render"** (cap $0.25, no generated images, install HyperFrames with npx). The agent runs P1 to P7 and stops at the render.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Angle: the TrackPoint's force-to-speed zones (IBM patent US5764219). Off-niche one-off (user). Hook type: contradiction. Theme line: *how hard you push*. Street-lamp: pass. Demand: `youtube_search.py` HTTP 400; autocomplete shows "why are thinkpads so good", "thinkpad trackpoint how to use". 170 words, 8 scenes |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | base about $0.04 (voice 1,034 characters about $0.026, timings about $0.01), cap $0.25; 0 generated media; 4 Commons photos (credits in `stock/_credits.jsonl`) |
| 5 Test · 6 Generation | done | within the cap | New engine: **HyperFrames 0.8.200** (no separate test stage; the snapshots served as the test). Voice take v1 `96r0g8vxc9rmt0d1esfa5gm87w` (Dennis, rate 0.95, 2 breaks of 0.2 s): 60.6 s, about 168 wpm; whisper `gk9cj3e67srmr0d1esfbhdjyvc` heard the script; silences 0.28 to 0.67 s, none over 0.9. Spend about **$0.04** |
| 7 Edit | done, **shipped (user, 30 Oct 2026)** | | `Media/Week 04/2026-10-26 Mon/ThinkPad/render/tp-62s-9x16-r1.mp4` (62.3 s, 1080×1920, 30 fps; HyperFrames render 3 min). `hyperframes check`: 0 errors. Mix **−14.0 LUFS, true peak −3.0 dBTP**, no music; sound stem synthesized by hand (thump at 0, 7 whooshes in the scene pauses). Final mp4 frames looked at. 6 worlds, every one moving (about 100 tweens); `tp.srt` written. Seen risks: first caption word lands at 0.15 s, not frame 1; lower lane of scene 7 is empty until "tests" |
| 8 Publish · 9 Measure | not started | | |

*Schematics:* the push-to-speed curve follows the zones in Rutledge and Selker's patent, not a measured firmware curve; the negative-inertia trace is marked "schematic" on screen; the doc window and typo are illustrative. The token was read from `~/Documents/youtube/.env` at run time (this clone has no `.env`).

*Not verified:* the voice, caption timing, pace in motion, sound on a phone; the sensor photo's elements read as strain gauges without a datasheet.
