---
type: research
created: 2026-10-05
updated: 2026-10-05
status: rendered r2 (61 s) · delegated by the user ("upload it to youtube", 5 Oct 2026) · P7 is the user's
tags: [research, youtube, status, battery, ev, shorts, week-01]
---

# EV battery tech · status (Week 01)

← [[YouTube Channel]] · [[Script - EV battery tech]] · [[Workflow]] · [[Playbook]]

Short 9:16, English, **155 words**, Austin at `speed` 1.0, **Week 01**. Question: how long does an EV battery really last, and what does it cost? Media in `Media/Week 01/2026-10-05 Mon/EV-battery/` (prefix `ev-`). Different angle from [[Battery and lithium - Status]] (that one: lithium, processing, politics).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | agent, under delegation | 18-fact bank, five threads scored, five hooks in [[Script - EV battery tech]]; street-lamp test **borderline** |
| 1 Research | ✅ | agent | Geotab (Jan 2026) and BloombergNEF (Dec 2025) read; AAA, plating papers, CATL, BYD, Tesla via search summaries |
| 2 Script | ✅ | agent | 155 words, 7 scenes, 5 facts, 3 spoken figures |
| 3 Direction | ✅ | agent | 18 plates, 17 stock and 1 generated |
| 4 Prompts and budget | ✅ | **delegated by the user** (*"upload it to youtube"*), cap ≈ $0.49 | below |
| 5 Test | ⏭ folded into 6 | delegation | |
| 6 Generation | ✅ | delegation | 7 voice takes, 1 plate (no retry), 7 word-timing runs |
| 7 Editing | ✅ rendered r2 · ⏳ **P7 is yours** | | `Media/Week 01/2026-10-05 Mon/EV-battery/render/ev-61s-9x16-r2.mp4` (+ `ev.srt`) |
| 8 Publishing | see [[Upload - EV battery tech]] | the user's delegation | |

## P4 budget (dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0 | 7 takes, 885 characters | ≈ $0.10 per 1,000 characters | ≈ $0.09 | ≈ $0.11 |
| Image (generated) | `openai/gpt-image-2`, 2:3, **high** | 1 plate | not shown by Replicate; assumed ≈ $0.25 | ≈ $0.25 | ≈ $0.30 |
| Image (stock) | free sources | 17 plates | $0 | $0 | n/a |
| Word timings | `incredibly-fast-whisper` | 7 takes | ≈ $0.01 (unconfirmed) | ≈ $0.07 | ≈ $0.08 |
| Sound | built by `build_video.py` | | $0 | $0 | n/a |
| **Total and cap** | | | | **≈ $0.41** | **≈ $0.49** |

No thumbnail image was generated (≈ $0.25 saved): see [[Upload - EV battery tech]].

## Prediction log

- Voice · `elevenlabs/v3` Austin `en` 1.0 (`previous_text`/`next_text`), 7 takes, 885 characters · ✅ `voice/ev-s1…s7-voice-v1.mp3` · ids in `voice/_log.jsonl`
- G1 anode schematic · `openai/gpt-image-2` 2:3 **high** · ✅ `plates/ev-p07-anode-v1.png` · [ftg3jawp…](https://replicate.com/p/ftg3jawp8hrmt0d11phbc1fpvw) · predict time 66 s; split into `ev-p07-gentle.png` and `ev-p07-fast.png` locally
- Word timings · `incredibly-fast-whisper` word, 7 runs · ✅ `voice/*.words.json`

**Total: 15 predictions (7 voice, 1 image, 7 timings), no retries, ≈ $0.41 of the ≈ $0.49 cap** if `gpt-image-2` high is ≈ $0.25 (still unconfirmed; the Replicate dashboard settles it).

## Checks done by the agent (stills and numbers)

`PLATES 18`, durations 2.9 to 4.2 s, `LONG PLATE: none`; `CAPTIONS 149 words, timed by whisper`; all 7 voices complete (lead-in, tail, order ok); 61.4 s with the gaps. Stills looked at on 14 frames of r1: captions sit mid-frame, cards below, callouts above. **Fixed after r1:** the two anode plates (gentle and fast) looked identical because the 2:3 image covers almost the whole frame; r2 shows each half as its own `contain` plate on a gradient.

## Not verified by the agent (said out loud, for your P7)

- **I did not hear the audio or watch the whole video:** how Austin sounds on this script, the pace, the sound mix, the motion, whether the captions land on the spoken words.
- **Facts to recheck before publishing:** the AAA 39% (a May 2026 test reported by secondary outlets; "most of that is the cabin heater" is the summaries' reading); Geotab's 2.3% is an average; "cheaper chemistry did the work" is BloombergNEF's framing (LFP shift offset higher metal prices).
- **Weak images:** the pack-line photo is a *motorcycle* battery line, the Tesla charger photo shows the Tesla name, the Leaf pack is an older design, four photos are reused with new crops, the winter-road photo is small (`contain`), the generated electrode plate is a simplified schematic (ion counts are illustrative).
- **`gpt-image-2`:** one more plate, still no price confirmation.
