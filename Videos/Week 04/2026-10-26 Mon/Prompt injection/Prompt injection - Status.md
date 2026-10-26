---
type: process
created: 2026-10-26
updated: 2026-10-26
status: v1 · rendered r1, waiting for the user (P7)
tags: [status, week-04]
---

# Prompt injection · Status

← [[Script - Prompt injection]] · [[YouTube Channel]] · [[Workflow]]

**Delegation (user, 26 Oct 2026):** *"New short: Prompt inyection and protection for your ai chatbot explained with smooth, rythmical 3d like animations. faster voice and more words allowed on the sime timeframe."* Read as a request to run P1 to P7 (Workflow: the normal run is delegated); cap $0.25 as on the ThinkPad video; stop at the render. The voice and length direction became edits of [[Playbook]] §2 and §5 and `CLAUDE.md` (speaking_rate 1.25, 180 to 235 words, aim 200 to 225).

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 26 Oct 2026 | Series How it works. Hook type: stakes. Theme line: *it can't tell your words from a stranger's*. Street-lamp: pass. Demand check: `youtube_search.py` still HTTP 400 (not re-run); indirect only (OWASP LLM01, vendor attack rates). 226 words, 9 scenes. Deep-first search not run (`youtube_search.py` down) |
| 4 Prompts, stock, budget | approved by delegation | 26 Oct 2026 | base about $0.05 (one take of about 1,370 characters, one timing call), cap $0.25; 0 generated media, 0 photos |
| 6 Generation | done | within the cap | Three takes (ids in `voice/_log.txt`): **v1** rate 1.15, 62.7 s, whisper heard "Remove anyone" for "Remove any one" (reworded) and a hitch after "is"; **v2** reworded, 67.7 s at the same rate (too long for the user's timeframe); **v3 used**: rate 1.25, **58.3 s, 226 words, about 232 wpm**, whisper heard the script, silences 0.26 to 0.56 s. Two retakes: one for the misheard word, one for the duration. Spend about 3 × $0.034 + 3 × $0.01 = **about $0.13** |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 04/2026-10-26 Mon/Prompt injection/render/pi-60s-9x16-r1.mp4` (59.7 s, 1080×1920, 30 fps; HyperFrames 0.8.200, render 2 m 50 s). CSS 3D: 7 worlds, each a perspective camera with a slow drift and a dolly hand-off; 100 BPM grid for the token stream steps, model pulses and packet hops; 142 tweens. `hyperframes check`: 0 errors. Mix **−14.0 LUFS, true peak −3.0 dBTP**, no music. `pi.srt` written. Final mp4 frames looked at |
| 8 Publish · 9 Measure | not started | | |

*Schematics:* the token stream, the model box, the glass box and the trifecta plate are drawn models, not any product's interface; the refund bot, the email and order 4471 are illustrative.

*Not verified:* how 232 wpm sounds and whether it is too fast (P7 question 2); caption timing against speech; pace in motion. Seen risks: first caption word at 0.15 s, not frame 1; the stream tiles enter the model in reverse reading order (a moving row, read left to right when still); the lower lane is empty in the first seconds of the stream scene.
