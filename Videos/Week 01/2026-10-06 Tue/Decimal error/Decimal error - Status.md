---
type: process
created: 2026-10-06
updated: 2026-10-06
status: P1 to P3 done; waiting for the user's P4 (budget and voice test)
tags: [status, week-01]
---

# Decimal error · Status

← [[Script - Decimal error]] · [[YouTube Channel]] · [[Workflow]]

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research | done | 6 Oct 2026 (user chose the idea) | Y: correct money code. X: cut-off error that grows with running time. Hook type: surprising fact. Demand: medium (200k best). Street-lamp: pass with the accumulation mechanism. Scale scored 3: carried by the consequence and the 7 m to 687 m growth ([[Script - Decimal error]] §1) |
| 2 Script · 3 Visual plan | done (agent) | pending the user's read | 164 words, 7 scenes, 18 plates (5 S, 10 D, 3 G); package (titles, thumbnail, promise) in the Script note §2. Schematic: "cut-off at every tick" simplifies the 24-bit conversion |
| 5 Test (voice) | done, **waiting for the user's ear** | 6 Oct 2026 (user: "lets go for the test first") | `elevenlabs/turbo-v2.5`, Austin, stability 0.45, similarity 0.75, style 0, speed 1.0, previous and next text accepted (no error). Files `Media/Week 01/2026-10-06 Tue/Decimal error/voice/de-e1-voice-v1.mp3` (6.5 s, 15 words, 138 wpm) and `de-e2-voice-v1.mp3` (9.7 s, 29 words, 179 wpm); 238 characters, about $0.02 (price unconfirmed). Predictions s6ehfb0behrmy0d12eave7z854, dxe1t5t1h9rmr0d12ear6y4v10. Not heard by the agent |
| 6 Generation | done | within the cap | voice 7 takes on turbo-v2.5 (838 characters, about $0.08), word timings 7 x about $0.01, 4 gpt-image-2 `high` predictions (3 plates + the one retry; price not in the API, budget about $0.25 each = about $1.00). Prediction ids: `Media/.../plates/_log.jsonl` and `voice/_log.jsonl`. **Plate 4 (register):** the generated row had 21 cells, then 23 cells but the wrong bit pattern; after the one retry I kept the generated cut line and faded cells and **repainted the 23 cells exactly** (bits 0.0001100110011001100110) with Pillow; marked *schematic, cells drawn*. Plates 14 and 16 (range gate, incident) passed the check by eye. 17 plates: 6 S, 8 D, 3 G. Plate 12 dropped (scene 5 would have had 2.1 s plates); its 3,600,000 card sits on plate 10 |
| 7 Edit | done, **waiting for the user (P7)** | | `Media/Week 01/2026-10-06 Tue/Decimal error/render/de-60s-9x16-r1.mp4` (60.1 s, 17 plates, longest 4.4 s, captions 162 words timed by whisper, `render/de.srt`); `CHECK` all voices complete; no `EMPTY PLATE`. Checked by eye in stills: plates 2, 3, 4, 14 fixed after the first render (soldiers in the wreck photo removed, register strip cropped and labelled, Scud inset moved off the gate diagram). **Not verified:** how it sounds in the mix, caption timing in motion, sound levels, pace. Cut-off "at every tick" is a schematic of the 24-bit conversion |
| 4 Prompts, stock, budget | **approved** | 6 Oct 2026 (user: "Audio is good and good pace. i approve P4"; voice test passed) | cap about $1.09 (base $0.91 x 1.2), gpt-image-2 at `high`; run stops at the render (P7);  base about $0.91, cap about $1.09 (voice and gpt-image-2 prices unconfirmed); no media, no Replicate call yet; voice test of scenes 1 and 2 on turbo-v2.5 first |

*Not verified:* see the Script note §3. *Feedback:* none yet.

## Prompts for the 3 generated plates (`openai/gpt-image-2`, content first, no style words; not run)

Output line for all: "plain white background, no letters, numbers, labels or logos, flat diagram, no glow, no shadows". Text and numbers are added by the builder.

1. **Plate 4, register (no references).** Subject: a binary register shown as one horizontal row of 23 equal square cells, then a vertical cut line, then 5 more cells to its right drawn faded and cut off by the line. Fill (dark) or leave empty the 23 cells left to right as: empty empty empty filled filled empty empty filled filled empty empty filled filled empty empty filled filled empty empty filled filled empty empty. View: straight on, 2:3 portrait, the row in the upper half.
2. **Plate 14, range gate (references: GAO figures 4 and 5, rendered from the PDF).** Subject: two stacked panels. Each has a radar dish at the left, a thin beam going right, a rectangular gate drawn across the beam, and a simple missile outline. Panel 1: the missile is in the centre of the gate. Panel 2: the same gate sits further left and the missile is outside it, to the right. View: top-down, same scale in both panels.
3. **Plate 16, incident (no references).** Subject: a top-down schematic of open flat ground. At left a missile launcher and a radar dish (one battery); at right a rectangular low building. A dashed arc descends from the top right to the building (the Scud's path). A short beam from the radar ends in a small gate placed short of the arc, with no missile inside it. No people, no fire, no explosion, no other vehicles.

Checks after generation: count the cells and compare the pattern (plate 1), missile outside the gate only in panel 2 (plate 2), nothing added that the GAO report does not state (plate 3). One retry per image; a failed plate becomes a drawn plate.

## Voice test: listening rubric (answer in chat, words go here under Feedback)

1. Natural? 2. Pace (too fast, right, too slow)? 3. Pauses: any that come where they should not (scene, word)? 4. Does scene 2 continue scene 1's tone (the point of previous and next text)? 5. Better or worse than the old v3 Austin?

## P7 listening rubric (answer in chat; words go under Feedback)

1. Voice natural? 2. Pace right? 3. Pauses: any that come where they should not, or are missing (scene, word)? 4. Sound mix right (effects and bed against voice)? 5. Does any screen feel empty (scene)? 6. Do you want the thumbnail built now (package in the Script note §2)?
