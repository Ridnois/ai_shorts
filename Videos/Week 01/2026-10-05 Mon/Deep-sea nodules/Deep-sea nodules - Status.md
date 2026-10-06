---
type: research
created: 2026-10-05
updated: 2026-10-05
status: rendered r1 (62 s) · uploaded private (WtKTVljJR7A) on the user's word
tags: [research, youtube, status, deep-sea, mining, shorts, week-01]
---

# Deep-sea nodules · status (Week 01)

← [[YouTube Channel]] · [[Script - Deep-sea nodules]] · [[Workflow]] · [[Playbook]] · [[Youtube idea #2]]

Short 9:16, English, **148 words** (about 53 s of speech), Austin at `speed` 1.0, **Week 01**. Question: who decides whether the deep-sea rocks get mined? Media in `Media/Week 01/2026-10-05 Mon/Deep-sea/` (prefix `dn`). Hook type: **stakes**. Built with the 5 Oct 2026 vault changes: a **pause plan** (`gaps` and per-scene `pauses`) and **immersive plates** (`bg: blur`, `inset`, split layouts, no `EMPTY PLATE`).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | delegation | 17-fact bank; thread scored 4 or more on surprise, scale, plain; street-lamp **pass**; against-the-idea pass; the idea note's nickel claim not supported (left out) |
| 1 Research | ✅ | delegation | Wikipedia, Mongabay (July 2026) and NOAA read; USGS estimate through a summary |
| 2 Script | ✅ | delegation | 148 words, 7 scenes, 5 facts, 3 spoken figures, pause plan in the table |
| 3 Visual plan | ✅ | delegation | 18 plates: 13 stock, 3 drawn, 0 generated |
| 4 Prompts and budget | ✅ | **user, 5 Oct 2026**: *"make a video based on the idea described on Youtube idea #2"*; cap about $0.19 | below. Delegation: run to the render, **no upload** |
| 5 Test | skipped | | no new voice technique; the pause tool is checked by numbers |
| 6 Generation | ✅ | delegation | 7 voice takes, 0 generated plates, 7 word-timing runs, 4 drawn diagrams |
| 7 Edit | ✅ rendered r1 · ⏳ **P7 is yours** | | `Media/Week 01/2026-10-05 Mon/Deep-sea/render/dn-62s-9x16-r1.mp4` (+ `dn.srt`) |
| 8 Publish | ✅ uploaded private | **user, 5 Oct 2026**: *"Way better, upload the video"* | see [[Upload - Deep-sea nodules]]; `videos.csv` row added |

## P4 budget (dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0, `previous_text` / `next_text` | 7 takes, 876 characters | about $0.10 per 1,000 characters | about $0.09 | about $0.11 |
| Word timings | `incredibly-fast-whisper` | 7 takes | about $0.01 | about $0.07 | about $0.08 |
| Generated plates, drawn diagrams, stock, sound | none generated | | $0 | $0 | |
| **Total and cap** | | | | **about $0.16** | **about $0.19** |

## What was new in this build (5 Oct 2026 vault changes)

- **Pause plan:** `gaps` = [0.55, 0.30, 0.45, 0.80, 0.25, 1.00] and inner `pauses` on scenes 1, 3, 4, 5, 6, 7 (words "pacific", "grain", "years", "mexico", "it", "grow"), all written in the script table with their intention. The pauses made the video 62.2 s against about 53 s of speech.
- **Immersive plates:** every `contain` plate uses `bg: blur` (13 of 18 plates are photos, 4 are drawn splits with a real-photo inset below the captions); the build printed `EMPTY PLATE: none`. A cut from one picture and one note to a frame with a second layer was the user's "empty screen" feedback.

## Checks done by the agent

`PLATES 18`, durations 3.3 to 3.8 s, `LONG PLATE: none`, `EMPTY PLATE: none`; `CAPTIONS 148 words, timed by whisper`; all 7 voices complete; 62.2 s. Stills of the assembled project checked **before** the first full render (18 frames, then 2 after card fixes): the number card "3 to 50 million years" and the title "Application accepted for review" overflowed their cards and were shortened. One render only. Cost: voice about $0.09 + timings about $0.07 = **about $0.16** of the $0.19 cap.

## Not verified by the agent

**I did not hear the audio or watch the whole video: above all, whether the new pauses feel human** (the first test of the pause plan: say which scene and word if one sounds wrong; the listening rubric in [[Workflow]] has five questions), the pace, the sound mix, the motion, caption timing. **Facts:** "more cobalt than all known land reserves" is one USGS estimate seen only in a search summary (the voice says "by one estimate"); the 3 to 50 million years is my arithmetic and assumes the 1 to 15 mm per million years is radial growth; "45 of 193" uses the UN member count from general knowledge; the NOAA dates are from NOAA's August 2026 release; the idea note's nickel claim is not used. **Images:** the CCZ map is an old NOAA graphic (about 1991) of claim areas, not current; the collector tracks are from a 2021 Ifremer test (EDEN campaign) in another contract area; no photo of a collector at work; the ROV photo is from a 2015 research cruise.

## Feedback

(empty: your words verbatim, plus the five listening-rubric answers: voice natural? pace? pauses? mix? any empty screen?)
