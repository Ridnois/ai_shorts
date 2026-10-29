---
type: process
created: 2026-10-26
updated: 2026-10-26
status: v3 · rendered r3 (HyperFrames + three.js, overlap-checked), waiting for the user (P7)
tags: [status, week-04]
---

# Prompt injection · Status

← [[Script - Prompt injection]] · [[YouTube Channel]] · [[Production]]

**Delegation (user, 26 Oct 2026):** *"New short: Prompt inyection and protection for your ai chatbot explained with smooth, rythmical 3d like animations. faster voice and more words allowed on the sime timeframe."* Read as a request to run P1 to P7 (Workflow: the normal run is delegated); cap $0.25 as on the ThinkPad video; stop at the render. The voice and length direction became edits of [[Format]] (old Playbook §2) and §5 and `CLAUDE.md` (speaking_rate 1.25, 180 to 235 words, aim 200 to 225).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Series How it works. Hook type: stakes. Theme line: *it can't tell your words from a stranger's*. Street-lamp: pass. Demand check: `youtube_search.py` still HTTP 400 (not re-run); indirect only (OWASP LLM01, vendor attack rates). 226 words, 9 scenes. Deep-first search not run (`youtube_search.py` down) |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | base about $0.05 (one take of about 1,370 characters, one timing call), cap $0.25; 0 generated media, 0 photos |
| 6 Generation | done | within the cap | Three takes (ids in `voice/_log.txt`): **v1** rate 1.15, 62.7 s, whisper heard "Remove anyone" for "Remove any one" (reworded) and a hitch after "is"; **v2** reworded, 67.7 s at the same rate (too long for the user's timeframe); **v3 used**: rate 1.25, **58.3 s, 226 words, about 232 wpm**, whisper heard the script, silences 0.26 to 0.56 s. Two retakes: one for the misheard word, one for the duration. Spend about 3 × $0.034 + 3 × $0.01 = **about $0.13** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-26 Mon/Prompt injection/render/pi-60s-9x16-r1.mp4` (59.7 s, 1080×1920, 30 fps; HyperFrames 0.8.200, render 2 m 50 s). CSS 3D: 7 worlds, each a perspective camera with a slow drift and a dolly hand-off; 100 BPM grid for the token stream steps, model pulses and packet hops; 142 tweens. `hyperframes check`: 0 errors. Mix **−14.0 LUFS, true peak −3.0 dBTP**, no music. `pi.srt` written. Final mp4 frames looked at |
| 7b Edit r2 (three.js) | done, **waiting for the user (P7)** | | User on r1 (26 Oct 2026): *"Theres no point on using the tiles that way, no 3d movement on text element. lets test remaking it with threejs"* (rule now in [[Look]] 3D plates). `render/pi-60s-9x16-r2.mp4` (59.7 s, same take v3 and captions): one three.js canvas (three 0.181.2, one `render(t)` from GSAP `onUpdate` and `hf-seek`); word capsules from three sources fold into one lane into a layered model on the 100 BPM beat clock, ember capsules glow on "ignore", all turn grey on "same"; glass box with a blocked rose ray and a mint draft; trifecta spheres on a disc with a hopping packet and a sinking node. All text is flat HTML; labels follow objects by 2D projection only. Render 3 m 12 s; `check` 0 errors; mix −14.0 LUFS, true peak −3.0 dBTP. r1 (CSS 3D) kept for comparison |
| 7c Edit r3 (HyperFrames + a little three.js) | done, **waiting for the user (P7)** | | User on r2 (26 Oct 2026): *"Content overlaps. consider using both hyperframes and a little bit of threejs. Improve the logic behing the generation of 3d animations, and redo the render. also new rule: when presenting solution, make it more attractive and colorful"* (rule in [[Look]] *Solution scenes*). `render/pi-60s-9x16-r3.mp4` (59.7 s, take v3): three.js only for the stream into the model (scenes 4 to 6) and the glass box (7); hook, definition, origin, trifecta and close are HyperFrames 2D. Generation logic: regions (stage, caption band, lower lane), auto-framing of each 3D world into its stage rect, labels placed off projected object boxes, keyframe tracks; `hf/check3d.mjs` samples every 0.25 s for 3D vs text, 3D vs caption band and text vs text: **OVERLAPS 0** (it found 11 kinds on the first r3 build). Solution scenes 7 to 9: mint and signal ground flood, mint hero cube and cards, springy entrances, colour sparks. `check` 0 errors; render 3 m 05 s; mix −14.0 LUFS, true peak −3.0 dBTP |
| 8 Publish · 9 Measure | **pack ready, waiting for approval** | | `upload/pi-publish-pack.md` (title, two alternatives, description 914 characters, pinned comment, TikTok caption) and thumbnail `upload/pi-thumb-a.jpg` (drawn: the email with one ember line lifting out into a rose reply, words ONE HIDDEN LINE; no warnings, checked at 168 px and in the 3:2 crop) from `publish.py --dry-run`. Not uploaded: private upload needs the user's yes on title, description, thumbnail, visibility. No next-in-series titles or previous-video link yet (none uploaded) |

## Feedback

P7 on r3 (user, 26 Oct 2026): *"No overlap, balance work, solution could be more colorful and meaingful but ok for now.go for the upload pack"*. Next time: the solution scenes need more colour and more meaning (a stronger picture of why the fix works), on top of the Style rule.

*Schematics:* the token stream, the model box, the glass box and the trifecta plate are drawn models, not any product's interface; the refund bot, the email and order 4471 are illustrative.

*Not verified:* how 232 wpm sounds and whether it is too fast (P7 question 2); caption timing against speech; pace in motion. Seen risks: first caption word at 0.15 s, not frame 1; the stream tiles enter the model in reverse reading order (a moving row, read left to right when still); the lower lane is empty in the first seconds of the stream scene.

*Before upload (26 Oct 2026):* the shared `System/scripts/check3d.mjs` finds r3 cards, the approve button and the email in the right interface strip (x > 950) from 31.25 to 56.5 s, under the app's like and comment buttons; r3 predates that check. Fix the card CSS to x 56 to 950 as on *Chatbot vs agent* and re-render (no spend) before P8.
