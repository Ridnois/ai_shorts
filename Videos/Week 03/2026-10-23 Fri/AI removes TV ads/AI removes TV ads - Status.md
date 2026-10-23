---
type: process
created: 2026-10-23
updated: 2026-10-23
status: v1 · rendered r1, waiting for the user (P7)
tags: [status, week-03]
---

# AI removes TV ads · Status

← [[Script - AI removes TV ads]] · [[YouTube Channel]] · [[Workflow]]

**Delegation (user, 23 Oct 2026):** *"Chose a trending ai topic and generate a new video"*. The agent picks the topic, runs P1 to P7 and stops at the render. First video with the hook, connection and look v2 rules.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | done (agent) | delegated 23 Oct 2026 | Trend: "vibe coding the ads out of smart TVs" (Decrypt, 20 Oct 2026; cleanyourtv 27k stars). Series Agent at work. Hook type: stakes. Theme line: *the developer door*. Street-lamp: pass. **Demand check not run** (YouTube token HTTP 400). Compact, 114 words, 5 scenes, 7 plates (2 in 3D) |
| 4 Prompts, stock, budget | approved by delegation | 23 Oct 2026 | base about $0.03 (voice about 600 characters, timings), cap about $0.04; 0 generated media, 0 photos |
| 6 Generation | done | within the cap | Voice take v1 (Dennis, rate 0.95, 1 break 0.2 s; id in `voice/_log.txt`): 42.6 s, whisper heard the script; **two silences over the 0.9 s ceiling** (1.02 s after "Here is how.", 0.94 s before "The catch"), kept rather than retaken. Spend about $0.015 + $0.01 = **about $0.025**. 5 motion plates, 2 3D plates (10.7 s of 3D); every sheet looked at; tile bevels and TV framing fixed |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 03/2026-10-23 Fri/TV-ads/render/tv-44s-9x16-r1.mp4` (44.3 s). MOTION SHARE 100 %, no REPEAT, no LONG PLATE, CHECK all voices complete. Mix **-14.1 LUFS, true peak -3.0 dBTP**, no music. First render had the TV behind the captions and a stale picture from a `mix_audio.py` bug (fixed); final frames looked at |
| 8 Publish · 9 Measure | not started | | |

*Recorded run:* none; the agent cannot record a TV session here, so the run is drawn as a terminal with the real commands (`adb connect`, `pm disable-user`) and illustrative addresses, not as any product's interface.

*Not verified:* the voice, caption timing, pace in motion, sound on a phone. Seen risks: the home-screen plate lasts 1.8 s; the lower half of the door and catch plates is empty until their last word; the 1 s pause after the hook.

## P7 listening rubric (answer in chat; words go under Feedback)

1. Voice natural? 2. Pace right? 3. Pauses misplaced or missing (scene, word)? 4. Sound mix right? 5. Any screen empty (scene)? 6. Did any picture fail to show what was said, or arrive late (scene, word)? 7. After the first sentence, did you know what the video is about and want the explanation? 8. Could you follow each sentence from the one before? 9. Does look v2 (ink ground, semantic colours) read better than the last video? 10. Build the thumbnail and publish pack?
