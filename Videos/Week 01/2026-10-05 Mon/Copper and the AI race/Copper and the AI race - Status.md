---
type: research
created: 2026-10-05
updated: 2026-10-05
status: rendered r1 (61 s) · delegated by the user ("do it all for yourself", 5 Oct 2026) · P7 is the user's
tags: [research, youtube, status, copper, ai, shorts, week-01]
---

# Copper and the AI race · status (Week 01)

← [[YouTube Channel]] · [[Script - Copper and the AI race]] · [[Workflow]] · [[Playbook]]

Short 9:16, English, **160 words**, Austin at `speed` 1.0, **Week 01** (the same calendar week as [[Battery and lithium - Status]]: both were made on Monday 5 Oct 2026; [[Workflow]]). Question: why can't the AI race just make more copper? Media in `Media/Week 01/2026-10-05 Mon/Copper-AI/` (prefix `cu-`). First video with **the new caption layout** (captions centred, cards below) and **the new image model** (`gpt-image-2`, one plate).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | agent, under delegation | 20-fact bank, scoring of six threads, five hooks in [[Script - Copper and the AI race]]; street-lamp test **borderline** (swap candidate: China mines 8 % and refines 48 %) |
| 1 Research | ✅ | agent | USGS MCS 2026, S&P Global (8 Jan 2026) and the IEA overview read; the rest from search summaries |
| 2 Script | ✅ | agent | 160 words, 7 scenes, 5 facts, 3 spoken figures |
| 3 Direction | ✅ | agent | 18 plates, 17 stock and 1 generated |
| 4 Prompts and budget | ✅ | **delegated by the user** (*"do it all for yourself"*), cap ≈ $0.49 | below |
| 5 Test | ⏭ folded into 6 | delegation | |
| 6 Generation | ✅ | delegation | 7 voice takes, 1 plate (no retry), 7 word-timing runs |
| 7 Editing | ✅ rendered · ⏳ **P7 is yours** | | `Media/Week 01/2026-10-05 Mon/Copper-AI/render/cu-61s-9x16-r1.mp4` (81 MB, 60.8 s, 1080×1920, 24 fps; + `cu.srt`) |
| 8 Publishing | ⏳ uploaded **private** (id YRX0VfpPMtU, 5 Oct 2026) | the user's delegation (*"Upload the last video to youtube"*) | [[Upload - Copper and the AI race]]; publishing, thumbnail and pinned comment pending |

## P4 budget (dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0 | 7 takes, 847 characters | ≈ $0.10 per 1,000 characters | ≈ $0.085 | ≈ $0.10 |
| Image (generated) | **`openai/gpt-image-2`**, 2:3, **high** | 1 plate | **not shown by Replicate; assumed ≈ $0.25** (conservative) | ≈ $0.25 | ≈ $0.30 |
| Image (stock) | free sources | 17 plates | $0 | $0 | n/a |
| Word timings | `incredibly-fast-whisper` | 7 takes | ≈ $0.01 (unconfirmed) | ≈ $0.07 | ≈ $0.08 |
| Sound | built by `build_video.py` | | $0 | $0 | n/a |
| **Total and cap** | | | | **≈ $0.41** | **≈ $0.49** |

## Prediction log

- Voice · `elevenlabs/v3` Austin `en` 1.0 (`previous_text`/`next_text`), 7 takes, 847 characters · ✅ `voice/cu-s1…s7-voice-v1.mp3` · ids in `voice/_log.jsonl`
- G1 porphyry · `openai/gpt-image-2` 2:3 **high** · ✅ `plates/cu-p04-porphyry-v1.png` · [6n6db2yp…](https://replicate.com/p/6n6db2yps1rmy0d11mrsdpqv94) · predict time 75 s
- Word timings · `incredibly-fast-whisper` word, 7 runs · ✅ `voice/*.words.json`

**Total: 15 predictions (7 voice, 1 image, 7 timings), no retries, ≈ $0.41 of the ≈ $0.49 cap if `gpt-image-2` high is ≈ $0.25.** Replicate's `metrics` carry no cost: the real charge is for you to read on the dashboard, and **it also settles the price of `gpt-image-2`** that the vault still lists as unmeasured.

## Checks done by the agent (stills and numbers)

`PLATES 18`, durations 3.0 to 3.8 s, `LONG PLATE: none`; `CAPTIONS 156 words, timed by whisper`; all 7 voices complete (lead-in, tail, order ok); 60.8 s with the gaps (about 54 s of speech: ≈ 178 words per minute while speaking, ≈ 161 with the gaps). Stills looked at on 25 frames: captions sit in the middle of the frame, cards below them, callouts above. **Fixed during the build:** the first card's title ran off the card (shortened); the "Magma" label moved closer to its target.

## Not verified by the agent (said out loud, for your P7)

- **I did not hear the audio or watch the whole video:** how Austin sounds on this script, the pace, the sound mix, the motion.
- **Facts to recheck before publishing:** the rack's 2 miles and 20 kW (Nvidia's claims, secondary sources), the 83 kg per electric car, the data-center share of demand (my arithmetic), and that the 17 years is an average.
- **Weak images:** only 10 photos, five reused with a new crop; the refining step has no photo; the generated plate is a simplified schematic.
- **`gpt-image-2`:** one plate is not a comparison. Look at plate 8 against the earlier `gpt-image-1.5` schematics and tell me if the new model earned its price.
