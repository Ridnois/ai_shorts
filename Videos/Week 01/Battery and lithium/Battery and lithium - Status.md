---
type: research
created: 2026-10-05
updated: 2026-10-05
status: stages 0 to 3 done · delegated by the user (5 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7)
tags: [research, youtube, status, battery, lithium, shorts]
---

# Battery and lithium · status

← [[YouTube Channel]] · [[Script - Battery and lithium]] · [[Workflow]] · [[Playbook]]

Short 9:16, English, **200 words** (the user's number, above the 130 to 190 range), first video with the **Austin** voice at **`speed` 1.0** ("pace 1"). Question: why did a metal that is not rare become something countries compete for? Media in `Media/Week 01/Battery-lithium/` (prefix `bt-`); this is **Week 01**, the first video of the weekly schedule ([[Workflow]]). The Short itself carries no branding ([[Playbook]] §4).

## Stage log

| Stage                | Status                         | Approved                                                                                                                                 | Note                                                                                                                                                                 |                                                                                                            |
| -------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 0 Idea               | ✅                              | agent                                                                                                                                    | 19-fact bank, scoring of six threads, five hooks in [[Script - Battery and lithium]]; street-lamp test **borderline** (swap candidate: the Big Bang lithium problem) |                                                                                                            |
| 1 Research           | ✅                              | agent                                                                                                                                    | USGS MCS 2026 and IEA GCMO 2025 read; the rest from search summaries; see "not verified" in the script note                                                          |                                                                                                            |
| 2 Script             | ✅                              | agent                                                                                                                                    | 200 words, 8 scenes, 5 facts, 3 spoken figures                                                                                                                       |                                                                                                            |
| 3 Direction          | ✅                              | agent                                                                                                                                    | 21-plate visual plan, 18 stock and 3 generated; on-screen text plan                                                                                                  |                                                                                                            |
| 4 Prompts and budget | ✅                              | **delegated by the user** (5 Oct 2026: *"Follow the steps until the render, use the date atemporally, keep the 200 words"*), cap ≈ $0.41 | prompts in the script note §5, budget below                                                                                                                          |                                                                                                            |
| 5 Test               | ⏭ folded into 6                | delegation                                                                                                                               |                                                                                                                                                                      | scene 1 voice twice (default and the expressive variant), one generated plate and one stock photo composed |
| 6 Generation         | ✅                              | delegation                                                                                                                               | 9 voice takes (8 + the scene 1 alternative), 3 plates (no retry), 8 word-timing runs                                                                                 |                                                                                                            |
| 7 Editing            | ✅ rendered · ⏳ **P7 is yours** |                                                                                                                                          | `Media/Week 01/Battery-lithium/render/bt-72s-9x16-r2.mp4` (65 MB, 71.9 s, 1080×1920, 24 fps; + `bt.srt`)                                                             |                                                                                                            |
| 8 Publishing         | ⏳                              |                                                                                                                                          |                                                                                                                                                                      |                                                                                                            |

Stock photos (free) were downloaded **before** P4 as part of package B into `Media/Week 01/Battery-lithium/stock/` (credits in `_credits.jsonl`). **Weak points that remain:** five photos are small (345 to 722 px) and are shown as `contain` plates; no photo shows lithium clearly floating on water (the hook is carried by the voice and by the jar-of-oil photo); G1 was written from a specification, **not from a real cell diagram** (none was available in a fetchable format).

## P4 budget (dollars; Replicate is not called before your approval)

| Category          | Model                                        | Quantity                                                                      | Unit price                   | Subtotal     | Cap (×1.2)  |
| ----------------- | -------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------- | ------------ | ----------- |
| Voice             | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0 | 8 takes, 1,099 characters + a 41-character alternative of scene 1 for the A/B | ≈ $0.10 per 1,000 characters | ≈ $0.115     | ≈ $0.14     |
| Image (generated) | `gpt-image-1.5`, 2:3, medium                 | 3 plates (G1, G2, G3)                                                         | ≈ $0.05 (unconfirmed)        | ≈ $0.15      | ≈ $0.18     |
| Image (stock)     | free sources                                 | 18 plates                                                                     | $0                           | $0           | n/a         |
| Word timings      | `incredibly-fast-whisper`                    | 8 takes                                                                       | ≈ $0.01 (unconfirmed)        | ≈ $0.08      | ≈ $0.10     |
| Sound             | built by `build_video.py`                    |                                                                               | $0                           | $0           | n/a         |
| P5 test           | scene 1 voice twice, one plate               | (inside the lines above)                                                      |                              |              |             |
| **Total and cap** |                                              |                                                                               |                              | **≈ $0.345** | **≈ $0.41** |

One retry of one plate fits inside the total cap; going over needs your approval. Prices are rates read in [[Workflow]], not confirmed on Replicate's pages; the real charge is not in the API's `metrics`, so I will report the dashboard check as unverified.

**Decisions taken with the delegation:** the borderline thread stays (no answer given, so the agent keeps the chosen one); the pause sentence is **atemporal** (scene 6 now says "for one year… a pause is not a repeal", no end date); the 200 words are kept; Zimbabwe stays cut.

## Prediction log

- Voice · `elevenlabs/v3` Austin `en` 1.0 (`previous_text`/`next_text`), 8 takes, 1,099 characters · ✅ `voice/bt-s1…s8-voice-v1.mp3` · ids in `voice/_log.jsonl` (s1 [zzd7vrvw…](https://replicate.com/p/zzd7vrvwesrmr0d11kv9e9hrb4), s2 [qef70bdh…](https://replicate.com/p/qef70bdh5drmt0d11kv9a6zes4), s8 [6bvgp48w…](https://replicate.com/p/6bvgp48w39rmt0d11kwb40zknw))
- Voice alternative of scene 1 · `stability` 0.35, `style` 0.35, a `[curious]` tag · ✅ `voice/bt-s1-voice-alt.mp3` · [dkm353jf…](https://replicate.com/p/dkm353jfkdrmt0d11kw9jymq9r). **For your A/B at P7; the default take is in the video.**
- G1 cell · `gpt-image-1.5` 2:3 medium · ✅ `plates/bt-p04-cell-v1.png` (cropped to `…-crop.png`) · [rd5dmc5k…](https://replicate.com/p/rd5dmc5kthrmw0d11kw9weee74)
- G2 chain · ✅ `plates/bt-p10-chain-v1.png` · [kb3q9zfj…](https://replicate.com/p/kb3q9zfjwsrmr0d11kwb7n6pf4)
- G3 sodium · ✅ `plates/bt-p17-sodium-v1.png` · [andv36ss…](https://replicate.com/p/andv36ss5drmr0d11kwvm1y6vr)
- Word timings · `incredibly-fast-whisper` word, 8 runs · ✅ `voice/*.words.json`

**Total for the video: 20 predictions (9 voice, 3 images, 8 timings), ≈ $0.35 of the ≈ $0.41 cap**; **thumbnails (P8, requested separately): 3 `gpt-image-1.5` hero images, medium, ≈ $0.15 of a $0.18 cap** (`Media/Week 01/Battery-lithium/upload/_log.jsonl`) (voice ≈ $0.115, images ≈ $0.15 at the unconfirmed $0.05, timings ≈ $0.08 at the unconfirmed $0.01); no retries. Replicate's `metrics` carry no cost, so the dashboard check is yours.

## Checks done by the agent (stills and numbers)

`PLATES 21`, durations 3.0 to 4.2 s, `LONG PLATE: none`; `CAPTIONS 195 words, timed by whisper`; every voice complete (lead-in, tail, order ok); stills looked at on 24 frames: captions land on the spoken words (turning, 2025, plus, 1, sodium…), callouts sit on the parts they name, the cards render. **Fixed during the build:** the "≈" in the number card was a box (Noto Sans Display Bold lacks it, as the guidelines warn) and the caption overflowed the card; "≈" and "≥" are removed from the cards; the NASA date stamp was cropped; the Samsung phone photo was replaced by a logo-free cell photo.

## Not verified by the agent (said out loud, for your P7)

- **I did not hear the audio or watch the whole video**: how Austin sounds, whether the pace (≈ 187 words per minute while speaking) feels rushed, whether the sound design is balanced, and the motion of pushes and transitions. I looked at 24 stills and read the build numbers; the mp4's header shows the expected duration and an audio and a video track.
- **A/B of scene 1:** the default take is in the video; compare it with `voice/bt-s1-voice-alt.mp3` (`stability` 0.35, `style` 0.35, `[curious]`) and tell me which wins.
- **Facts to recheck before publishing:** the 18-month pond figure (sources say 12 to 24), IEA's "about 60 %" (a global 2024 refining share), CATL's sodium-ion claims (secondary sources), and the text of MOFCOM Notices 58 and 70 (read through law-firm and trade summaries). The pause is described atemporally ("for one year… a pause is not a repeal") so the video does not go stale.
- **Weak images:** five small photos shown as `contain`; G1 was not built from a real cell diagram; G3's "larger ions" is a schematic (the radius ratio is not sourced in the vault); the CATL plant photo is the German site.
- **Description to write at P8** with the credit lines for the CC BY and CC BY-SA photos, the sources, the AI disclosure (voice and schematics) and the cut-off date.

## Re-render r2 (5 Oct 2026): caption layout

User: *"i see an issue, the youtube shorts ui overlaps the captions, redesign the layout of the videos captions should go more on the center"*. r1 had the captions at 16.5 % from the bottom, under the Shorts channel name, title and sound ticker. **r2: captions centred at 50 % of the height, cards at 66 % (below the captions, above the Shorts bottom text), callout labels above the captions**; the video, voice, plates and plan are otherwise identical (71.86 s, same checks: `CHECK RESULT all voices complete`, no long plate). `render/bt-72s-9x16-r2.mp4` replaces r1 for the upload. **Not verified:** how it looks in the real Shorts player on a phone (the interface zones are estimates).
