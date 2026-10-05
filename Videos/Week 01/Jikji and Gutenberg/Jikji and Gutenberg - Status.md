---
type: research
created: 2026-10-05
updated: 2026-10-05
status: rendered r2 (62 s) · delegated by the user (5 Oct 2026) · P7 is the user's
tags: [research, youtube, status, jikji, printing, shorts, week-01]
---

# Jikji and Gutenberg · status (Week 01)

← [[YouTube Channel]] · [[Script - Jikji and Gutenberg]] · [[Workflow]] · [[Playbook]]

Short 9:16, English, **146 words** (about 52 s of speech), Austin at `speed` 1.0, **Week 01**. Question: how can anyone prove, 650 years later, that a page was printed with loose metal type? Source article: Open Culture, Sept 2026. Media will go in `Media/Week 01/Jikji/` (prefix `jk-`), created only after P4. Hook type: **contradiction**.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ text | not yet | 17-fact bank, thread scored 4 on surprise, scale and plain, street-lamp **pass** (reason in the script), against-the-idea pass, demand check partly done, five hooks |
| 1 Research | ✅ | not yet | BnF, Global Jikji, Utah project and Open Culture read; Wikipedia and UNESCO details through search summaries only |
| 2 Script | ✅ | not yet | 143 words, 7 scenes, 5 facts, 3 spoken figures |
| 3 Visual plan | ✅ | not yet | 17 plates: 14 stock, 3 drawn, 0 generated |
| 4 Prompts and budget | ✅ | **user, 5 Oct 2026**: *"Aprove budger, use hook #2 and go ahead"* | below; delegation: continue within the cap (about $0.18), **stop at the render (P7)** |
| 5 Test | skipped | | no new technique |
| 6 Generation | ✅ | delegation | 7 voice takes, 0 generated plates, 7 word-timing runs, 3 drawn diagrams |
| 7 Edit | ✅ rendered r2 · ⏳ **P7 is yours** | | `Media/Week 01/Jikji/render/jk-62s-9x16-r2.mp4` (+ `jk.srt`) |
| 8 Publish | not started | | upload only after you confirm title, description, thumbnail, visibility |

## P4 budget (dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3`, `Austin`, `en`, `speed` 1.0, `previous_text` / `next_text` | 7 takes, 784 characters | about $0.10 per 1,000 characters | about $0.08 | about $0.10 |
| Word timings | `incredibly-fast-whisper` | 7 takes | about $0.01 (unconfirmed) | about $0.07 | about $0.08 |
| Generated plates | none planned | 0 | | $0 | |
| Drawn diagrams (3) | Pillow, exact geometry | 3 | $0 | $0 | |
| Stock photos | `stock_photos.py` | about 12 | $0 | $0 | |
| Sound | built by `build_video.py` | | $0 | $0 | |
| **Total and cap** | | | | **about $0.15** | **about $0.18** |

No thumbnail image is budgeted. If you want a hero image for the upload: one `gpt-image-1.5` plate, about $0.05 (adds to base; cap recomputed).

## What P4 contains

- **Voice prompts:** the exact texts of scene 1 to 7 in [[Script - Jikji and Gutenberg]] §3, one take per scene, no tags (expressive A/B only if you ask).
- **Image prompts:** none (no generated plate). The three drawn plates are specified in the plan rows 4, 6 and 7.
- **`plan.json`:** built after approval from the visual plan (full plates for photos, `contain` for diagrams, captions spelled "1377", "1972"; the voice spells numbers as spoken).
- **After approval, in order:** search and download the photos with credits, check each against its usefulness sentence, draw the 3 diagrams, voice, timings, build with `CHECK=1`, render. The agent stops at the render (P7).

## Prediction log

- Voice · `elevenlabs/v3` Austin `en` 1.0 (`previous_text`/`next_text`), 7 takes, 784 characters (scene 1 and 2 as rewritten for hook #2) · ✅ `voice/jk-s1…s7-voice-v1.mp3` · ids in `voice/_log.jsonl`
- Word timings · `incredibly-fast-whisper`, 7 runs (the run crashed twice on `_ssl handshake timed out`; finished takes were kept, nothing was re-charged for them) · ✅ `voice/*.words.json`
- Generated plates: none. Drawn diagrams: `plates/draw_diagrams.py` → `jk-p04-gap.png`, `jk-p06-block-vs-pieces.png`, `jk-p07-turned-piece.png`.

**Cost:** voice about $0.08 + timings about $0.07 = **about $0.15** of the $0.18 cap (Replicate prices not read from the dashboard).

## Checks done by the agent (numbers and stills)

`PLATES 20`, durations 2.9 to 4.0 s, `LONG PLATE: none`; `CAPTIONS 150 words, timed by whisper`; all 7 voices complete (lead-in, tail, order ok); 61.56 s. Stills looked at on 17 frames of r1 and 8 of r2. **Fixed after r1:** the timeline's "Gutenberg Bible" label and the two diagrams' lower text sat under the captions (diagrams now 78 % wide, higher); the blurry `jk-jikji.jpg` (the source photo is out of focus) no longer fills the frame, it is used once as a framed photo; the Paris card no longer overlaps the cover photo.

## Plan changes made on the way

- **No plate marks the upside-down character.** The free page photos are too small to find it with certainty, so plate 2 shows a real page without a callout on a specific letter (the voice says what scholars found).
- Replica metal plate and two more Gutenberg photos failed (Wikimedia 429); the Gutenberg photo is reused with two crops. 10 photos used; credits in `stock/_credits.jsonl` (Public domain, CC0, CC BY 2.0, CC BY-SA 3.0, CC BY-SA 4.0: the CC BY and BY-SA ones must be credited in the description).
- `jk-book.jpg` (the postscript page, 500 px) and `jk-jikji2.jpg` (the BnF cover with the handwritten French note, 350 px) are small and soft; both are framed (`contain`), not full-screen.

## Short version (user, 5 Oct 2026: *"try a shorter version, 90 words"*)

[[Script - Jikji and Gutenberg (short)]]: 91 words, 5 scenes, 12 plates, same images. Media in `Media/Week 01/Jikji-short/` (prefix `jks`). Scene 1 and 3 voice takes are **reused** from the long cut (same text; their `previous_text` / `next_text` context differed, so prosody may differ slightly); 3 new takes (scenes 2, 4, 5, about 330 characters) and 3 timing runs, about **$0.06** more (running total about $0.21 against the long cut's $0.18 cap; the request counted as approval for the variant).

## Decisions and open points

1. Budget approved (5 Oct 2026).
2. Hook #2 chosen by the user: "The first book printed with metal type is not the Gutenberg Bible." Scenes 1 and 2 rewritten to fit it ([[Script - Jikji and Gutenberg]] §3).
3. Demand check is incomplete (no search autocomplete or Shorts view counts here). Tell me if you want a different topic.
4. Plates: 3 of 17 are explainers, below the Playbook's third; accepted because the hidden idea is one diagram. Say if you want more.

## Not verified by the agent

The mistakes (upside-down, omitted, tilted characters) come from a Wikipedia and UNESCO summary; I could not open the UNESCO PDF. The 73 to 78 year gap depends on which Gutenberg date a source uses. "His method worked much faster" is one article's judgement. **I did not hear the audio or watch the whole video:** how Austin sounds; above all how he says **Jikji** and **Cheongju** (whisper heard "Jik -Jik" in scene 6, "Jikji" correctly in scene 2: listen to both); the pace (speech about 57 s for 146 words), the sound mix, the motion, whether captions land on the spoken words. **Image doubts:** the Heungdeoksa photo shows a hall I could not confirm is original or rebuilt (the callout names only the place); the metal pieces photo is a museum display of early Korean type, not shown to be the Jikji's own; the Gutenberg photo is the NYPL copy. P7 belongs to you.

## Feedback

(empty: your words verbatim, plus the three listening-rubric answers: voice natural? pace? sound mix?)
