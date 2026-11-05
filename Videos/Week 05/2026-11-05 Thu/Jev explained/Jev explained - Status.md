---
type: status
updated: 2026-11-05
---

# Jev explained: Status

**Ask once (user, 5 Nov 2026, verbatim):** angle "use 1 + use cases" · real output "Docs capture + primitives (Recommended)" · audio "Quiet music bed". Request: *"improve audio effects and sound, and new short explaining jev"*.

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video What's coming). `name-it`. Real thing: TypeSafe AI's Jev (early access 15 Sep 2026), a System One model that returns typed answers with probabilities; docs' real `jev-1.13.0` response on a support ticket. Demand: IBM "What Is Jev?" 1.27 M, 29.9x. Idea note [[Jev answers with odds, not words]], score 16. |
| **Pre-flight** | 1. `name-it`; IBM 29.9x, IBM 3.1x, Two Minute Papers 2.3x. 2. Field in [[Script - Jev explained]]: ours shows the real answer and the confidence turn in 52 s. 3. Hook "Jev is the AI that never writes a single word back."; stake "Ask ChatGPT to sort a support ticket…"; 0 s bars + "NEVER WRITES A WORD", 3 s a chatbot paragraph typing, 6 s it is struck, Jev's numbers land at 8.7 s. 4. Weakest beat: scene 3 (a typed ticket in a dark panel, 9.5 s of setup). 5. Prediction: at median (≈590 engaged at 7 d): strong outside demand, but `name-it` (195, n=1) and How AI works trail ours. |
| **Script** | 159 words, 7 scenes, turn at 55 %; sources checked 5 Nov 2026. |
| **Spend** | cap $2.00. Voice take `88ebvb2yq9rmy0d1n8ab9cydwg` (1,006 chars, about $0.025); incredibly-fast-whisper `3bdm8j67f5rmw0d1n8aaah2fwg` (about $0.01). Music bed CC0, $0. Total about $0.04. |
| **Build** | main medium primitive (`probs` with the docs' real numbers, `tokens`), 4 docs phrase crops, the real JSON in a labelled `code` panel. First video with the default music bed (`aesthetic-lofi`, 20.3 LU under the voice after ducking). `render/jev-53s-9x16-r1.mp4` 52.5 s, −14.0 LUFS, −1.4 dBTP; `qa.py` 8 of 8 PASS (composition warnings: 3 stretches of 6.1 to 7.0 s; stills of 2.8 and 2.3 s in w2, w3). Masters `-yt` 2160x3840, `-tt` 1080x1920; thumbnail; pack `upload/jev-publish-pack.md` (dry run, private). |
| **Review** | shipped (user, 5 Nov 2026: "Ship it as public") |
| **Publish** | public 5 Nov 2026, [`1-bpUdFHmdY`](https://youtu.be/1-bpUdFHmdY), 4K master, thumbnail confirmed |

## Not verified

No API call (no TypeSafe key): the numbers are the docs' published example, labelled on screen. The 88 % is TypeSafe's own case study. Not checked: how the voice, effects and bed sound together; the motion in playback.

## Feedback
