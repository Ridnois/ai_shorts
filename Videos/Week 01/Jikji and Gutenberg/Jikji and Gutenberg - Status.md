---
type: research
created: 2026-10-05
updated: 2026-10-05
status: P4 approved, delegated to the render (cap about $0.18) · media stage in progress
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
| 6 Generation · 7 Edit | ⏳ | delegation | |
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

## Decisions and open points

1. Budget approved (5 Oct 2026).
2. Hook #2 chosen by the user: "The first book printed with metal type is not the Gutenberg Bible." Scenes 1 and 2 rewritten to fit it ([[Script - Jikji and Gutenberg]] §3).
3. Demand check is incomplete (no search autocomplete or Shorts view counts here). Tell me if you want a different topic.
4. Plates: 3 of 17 are explainers, below the Playbook's third; accepted because the hidden idea is one diagram. Say if you want more.

## Not verified by the agent

The mistakes (upside-down, omitted, tilted characters) come from a Wikipedia and UNESCO summary; I could not open the UNESCO PDF. The 73 to 78 year gap depends on which Gutenberg date a source uses. "His method worked much faster" is one article's judgement. I have heard and watched nothing: P7 belongs to you.

## Feedback

(empty: your words verbatim)
