---
type: research
created: 2026-10-04
updated: 2026-10-04
status: stages 0–3 done · delegated by the user ("I like C, do the video", 4 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7) · generating
tags: [research, youtube, status, moon, shorts]
---

# Moon · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]] · [[Script - Moon]] · [[The Moon is leaving us]]

Short 9:16, English, 137 words. Theme: the Moon was born about twenty times closer, and its leaving keeps stretching Earth's day. Media in `Media/Moon/` (prefix `mn-`). **Second video built with the rules of the Superconductors feedback:** plain-words hook, one theme line with bridges, ≤ 5 facts, concrete ending, a new image every ≈ 3 to 4 s, captions at 88 px, no in-video branding, synthesized sound design.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | user chose theme and angle C ("I like C") after the mirror angle was rejected as boring | [[The Moon is leaving us]] |
| 1 Research | ✅ | agent | 19-fact bank, sources fetched 4 Oct 2026 |
| 2 Script | ✅ | agent | 137 words, 7 scenes, cut test done |
| 3 Direction | ✅ | agent | visual plan below: 18 plates, 3 generated + 1 drawn to scale |
| 4 Prompts and budget | ✅ | **delegated by the user** (4 Oct 2026), cap ≈ $0.37 | below |
| 5 Test | ⏭ folded into 6 | delegation | scene 1 voice twice (default and the expressive variant) |
| 6 Generation | ⏳ | delegation | voice, then plates, in series |
| 7 Editing | ⏳ **P7 is yours** | | `Media/Moon/render/` |
| 8 Publishing | ⏳ | — | description below |

## Budget in dollars (cap = base × 1.2)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` Roger `en`, speed 0.95 | 7 takes + 1 alternative take of scene 1, ≈ 840 + 50 characters | ≈ $0.10 per 1,000 characters | ≈ $0.09 | ≈ $0.11 |
| Image (generated) | `gpt-image-1.5` medium 2:3 | 3 plates | ≈ $0.05 (**unconfirmed**) | ≈ $0.15 | ≈ $0.18 |
| Word timings | `incredibly-fast-whisper` | 8 takes | cents (measured: negligible) | ≈ $0.02 | ≈ $0.03 |
| Image (stock) and the scale diagram | free sources, drawn locally | 15 plates | $0 | $0 | — |
| Sound | synthesized by the builder | — | $0 | $0 | — |
| **Total and cap** | | | | **≈ $0.26** | **≈ $0.31** (the 0.37 above allows one retry image) |

Voice note: the default take of scene 1 goes in the video; the alternative (`stability` 0.35, `style` 0.35, a `[curious]` tag) is saved as `voice/mn-s1-voice-alt.mp3` for the user's A/B at P7 ([[Channel voice]]). The agent cannot hear either.

## Prediction log

`scene · category · model · status · cost · URL`
