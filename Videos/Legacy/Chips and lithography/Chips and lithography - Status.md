---
type: research
created: 2026-10-03
updated: 2026-10-03
status: stages 0–6 done · render r1 · awaiting P7 · narrated in Spanish (made before the English-only decision)
tags: [research, youtube, status, chips, canon, shorts]
---

# Chips and lithography · status

← [[YouTube Channel]] · [[Fast workflow]]

Sixth video of the channel, **vertical Short (9:16)**. Idea: [[Chips - countries and brands, Canon and 2 nm]]. **Narration and on-screen text are in Spanish**: the video was made before the channel switched to English (3 Oct 2026). An English version would mean rewriting the script, re-recording 7 voice takes (≈ $0.12) and re-rendering; not done, offered to the user.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | 3 Oct 2026 · "Perfect go for the next" | Request: how countries and brands compete in making microchips, and how Canon advances on the 2 nm scale |
| 1 Research | ✅ P2 | 3 Oct 2026 · "I approve, go for package B" | [[Research - Chips and lithography]]: 15 claims; 4 left out as weak or outdated |
| 2 Script | ✅ P3 | 3 Oct 2026 · same | [[Script - Chips and lithography (85 seconds)]]: 211 words, 7 scenes |
| 3 Direction | ✅ P4a | 3 Oct 2026 · same | 8 plates, in the script |
| 4 Prompts and budget | ✅ P4 | 3 Oct 2026 · "I approve, go ahead" | ≈ $0.44, cap ≈ $0.50 |
| 5 Test | ✅ P5 | 3 Oct 2026 · "Everything ok, go ahead" | Image 1 and scene 1 voice accepted |
| 6 Generation | ✅ P6 | 3 Oct 2026 · same phrase (understood as carrying on to the render, within the cap) | 7 voices, 8 plates + 1 retry |
| 7 Editing | ⏳ P7 | — | `Media/Legacy/Chips - 85 segundos/render/chips-93s-9x16-r1.mp4` |

## Reference photos (one per plate; Kontext accepts a single `input_image`)

Downloaded to `Media/Legacy/Chips - 85 segundos/ilustraciones/_referencias/`. Licenses checked on Wikimedia Commons on 3 Oct 2026:

| Ref. | Photo | Author · license | Used in plates |
| --- | --- | --- | --- |
| R1 | [Wafer with Pentium chips](https://commons.wikimedia.org/wiki/File:Wafer_with_Pentium_chips.jpg) (1200×1600) | Naotake Murayama · **CC BY 2.0** | 1, 3, 5, 6, 7, 8 |
| R2 | [Extreme ultraviolet lithography tool](https://commons.wikimedia.org/wiki/File:Extreme_ultraviolet_lithography_tool.jpg) (713×605) | Lawrence Livermore National Laboratory · **public domain** | 2 |
| R3 | [Padlock with chain](https://commons.wikimedia.org/wiki/File:Padlock_with_chain.jpg) (3264×2448, resized to 1600×1200) | Lacz02 · **CC BY-SA 4.0** | 4 |

- **Attribution** in the description: R1 and R3 (CC BY and CC BY-SA 4.0: check the terms before publishing).
- **Honest limitation:** **R2 is a 1990s EUV prototype (Livermore), not an ASML machine** nor a current one. In plasticine it only reads as "a big machine"; it is not claimed to be ASML's. **I found no free photo of Canon's FPA-1200NZ2C or of a nanoimprint mold**: those plates (1, 5, 6, 7) are drawn from the R1 wafer with the mold described in the prompt, **without verifying that Kontext does it well** (hence the P5 test).
- All three photos are horizontal or 3:4: `match_input_image` is used and the edit fills the 9:16 frame with the `max` scale.

## Image prompts (approved at P4)

**Model:** `black-forest-labs/flux-kontext-pro`, `aspect_ratio` `match_input_image`, PNG, one `input_image` (see above). Each prompt carries the narration sentence, the object, the state, the copper-orange accent and the style block.

**Style block (at the end of each prompt):**

```
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

| # | Ref. | Prompt (before the style block) |
| --- | --- | --- |
| 1 | R1 | Narration: "Canon shipped to Texas a machine that does not project chips with light: it stamps them, like a seal." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of small rectangular chips. Replace the background with a plain warm tabletop. A large grey clay rubber stamp with a round handle presses down onto the wafer from above. The stamp's handle is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 2 | R2 | Narration: "The most advanced chips are drawn with extreme ultraviolet light, and only one company builds those machines." Redraw this exact large lithography machine as a handmade plasticine clay miniature. Keep its large boxy body and its tall cylindrical column. Replace the background with a plain warm tabletop. A tiny clay figure stands next to it to show how big it is, back turned to the viewer. The machine's top light source is in bright copper-orange clay. The machine fills the frame, vertical composition. Remove all lettering and logos. |
| 3 | R1 | Narration: "Whoever does not have these machines cannot reach the smallest chips; one foundry makes almost three of every four dollars." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of small rectangular chips. Replace the background with a plain warm tabletop. All chips are matte grey clay and exactly one cluster of chips in the center is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 4 | R3 | Narration: "Countries fight over these machines: one bans their sale, another keeps advancing with older light." Redraw this exact padlock as a handmade plasticine clay miniature. Keep the rounded body, the curved shackle and the chain. Replace the background with a plain warm tabletop. The padlock is locked through the chain around a large grey clay machine crate behind it. The padlock body is in bright copper-orange clay. The padlock fills the frame, vertical composition. Remove all lettering and logos. (v2 adds: "sculpted entirely from soft clay… completely smooth and blank, with a plain unmarked surface and no engraving".) |
| 5 | R1 | Narration: "Canon proposes another path: pressing a mold onto resin." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape. Replace the background with a plain warm tabletop. A flat square glass-like clay mold plate hovers just above a thin shiny layer of clay resin on the wafer, about to touch it. The hovering mold plate is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 6 | R1 | Narration: "With better molds, it would reach two nanometers." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape. Replace the background with a plain warm tabletop. A flat square clay mold plate is pressed into the thin resin layer on the wafer and a neat pattern of tiny lines is copied into the resin around its edge. The copied pattern is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 7 | R1 | Narration: "When the mold touches the wafer it sheds particles, and a single defect ruins the chip." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of chips. Replace the background with a plain warm tabletop. A clay mold plate lifts away from the wafer and a single small speck of dust sits trapped on one chip. The speck of dust is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 8 | R1 | Narration: "The one that repeats the same chip, without failures, millions of times." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of identical small chips. Replace the background with a plain warm tabletop. Every chip is perfectly clean and identical, and a grey clay stamp is lifted high above the wafer. The stamp's handle is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |

**No text in the image:** labels and figures are added in editing ([[On-screen text style]]).

## Voice: `elevenlabs/v3` (Spanish, before the English switch)

7 takes, one per scene, with the **exact text** of the script (1,201 characters in total), voice `Roger`, language `es`, `speed` 0.95, `previous_text` and `next_text` of the neighbouring scenes ([[Guidelines for new scripts]] §3). **Sound and music:** none. For English videos the voice settings are in [[Channel voice]].

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Image | `flux-kontext-pro` | **8** (one per plate, each with its scene) | ≈ $0.04 (**from memory, unconfirmed**) | **≈ $0.32** | 9 images (≈ $0.36) |
| Voice | `elevenlabs/v3` | 7 takes (1,201 characters) | ≈ $0.10 per 1,000 characters | **≈ $0.12** | 8 predictions (≈ $0.14) |
| Sound | — | 0 | — | $0 | 0 |
| P5 test | plate 1 + scene 1 voice | 2 | — | (inside the total; ≈ $0.05) | |
| **Total and cap** | | | | **≈ $0.44** | **≈ $0.50** |

- Retries: one per image, in series; going over 9 images needs approval.
- References: Brazil ≈ $0.46; Lemon cake ≈ $1.57; this video is an 8-plate Short.

## Prediction log

Format: `scene · category · model · status · prediction`.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | image #1 | `flux-kontext-pro` (R1) | ✅ used (P5) | [6dmnbnytdsrmr0d10hb8vgw5aw](https://replicate.com/p/6dmnbnytdsrmr0d10hb8vgw5aw) |
| 1 | voice | `elevenlabs/v3` (`Roger`, `es`, 0.95) | ✅ used (P5) | [g1raw87q3nrmw0d10hbbag3s9g](https://replicate.com/p/g1raw87q3nrmw0d10hbbag3s9g) |
| 2 | voice | `elevenlabs/v3` | ✅ used | [tfh30nbmk5rmr0d10hcvrx82a4](https://replicate.com/p/tfh30nbmk5rmr0d10hcvrx82a4) |
| 3 | voice | `elevenlabs/v3` | ✅ used | [f3rwnycah9rmt0d10hcrqb5nf4](https://replicate.com/p/f3rwnycah9rmt0d10hcrqb5nf4) |
| 4 | voice | `elevenlabs/v3` | ✅ used | [t66h2254ahrmw0d10hcsn3fsn0](https://replicate.com/p/t66h2254ahrmw0d10hcsn3fsn0) |
| 5 | voice | `elevenlabs/v3` | ✅ used | [dymj9zdwy9rmw0d10hcv8sy5c0](https://replicate.com/p/dymj9zdwy9rmw0d10hcv8sy5c0) |
| 6 | voice | `elevenlabs/v3` | ✅ used | [xg06hypdd5rmt0d10hcrdpaxww](https://replicate.com/p/xg06hypdd5rmt0d10hcrdpaxww) |
| 7 | voice | `elevenlabs/v3` | ✅ used | [frbqg7f4w9rmt0d10hcvbbgb2w](https://replicate.com/p/frbqg7f4w9rmt0d10hcvbbgb2w) |
| 2 | image #2 | `flux-kontext-pro` (R2) | ✅ used | [ztd0ecrtd5rmt0d10hd9kpsqc0](https://replicate.com/p/ztd0ecrtd5rmt0d10hd9kpsqc0) |
| 3 | image #3 | `flux-kontext-pro` (R1) | ✅ used | [bwp75q256nrmw0d10hda761n2w](https://replicate.com/p/bwp75q256nrmw0d10hda761n2w) |
| 4 | image #4 v1 | `flux-kontext-pro` (R3) | ❌ discarded (legible "PRADO BRAZIL" brand) | [bzc7vmvk8srmw0d10hda94gay0](https://replicate.com/p/bzc7vmvk8srmw0d10hda94gay0) |
| 4 | image #4 v2 | `flux-kontext-pro` (R3) | ✅ used (the retry) | [q3va1exj31rmt0d10hdthftcmw](https://replicate.com/p/q3va1exj31rmt0d10hdthftcmw) |
| 5 | image #5 | `flux-kontext-pro` (R1) | ✅ used | [vacpvecrpnrmw0d10hdbq2gysm](https://replicate.com/p/vacpvecrpnrmw0d10hdbq2gysm) |
| 5 | image #6 | `flux-kontext-pro` (R1) | ✅ used (with reservations) | [jpnrzqe2w1rmt0d10hd8gt4vyg](https://replicate.com/p/jpnrzqe2w1rmt0d10hd8gt4vyg) |
| 6 | image #7 | `flux-kontext-pro` (R1) | ✅ used (with reservations) | [cqx72f7s0srmr0d10hdbxd4cnw](https://replicate.com/p/cqx72f7s0srmr0d10hdbxd4cnw) |
| 7 | image #8 | `flux-kontext-pro` (R1) | ✅ used (with reservations) | [ny8cbghb1nrmr0d10hdrqbyrxw](https://replicate.com/p/ny8cbghb1nrmr0d10hdrqbyrxw) |

**Predictions: 16 in total** (7 voices + 9 images: 8 used and 1 discarded, including the P5 test and the retry) against a cap of 8 voices and 9 images: **within the cap**. Estimated cost: voice ≈ $0.12 · images 9 × ≈ $0.04 = ≈ $0.36 · **≈ $0.48** (Kontext price unconfirmed), cap ≈ $0.50. *(An earlier version of this note said 15 predictions: it was a counting slip.)*

## P5 test result (3 Oct 2026)

Files in `Media/Legacy/Chips - 85 segundos/` (`ilustraciones/chips-i01-v1.png`, `voz/chips-e1-voz-v1.mp3`).

| Test | Result | What I could not check |
| --- | --- | --- |
| **Image #1** (880×1184, 3:4) | **Works:** a grey plasticine wafer with grids of chips and a grey stamp with a copper-orange handle above it, plasticine style and warm background. **Reservations:** the stamp floats above the wafer (it does not touch it), the wafer looks more like a manhole cover than a disc of chips (squares of uneven size), and the image is 3:4, not 9:16: the edit fills the frame with the `max` scale | Whether you like the look |
| **Voice** (`chips-e1-voz-v1.mp3`) | 141 KB at 128 kbps ≈ **8.8 s for 20 words** (≈ 136 words per minute with pauses), computed from file size | **How it sounds, the accent and whether it reads "Canon" and "Texas" well** |

## Generation and editing (3 Oct 2026)

- **Voice:** 7 takes (`chips-e1` to `e7`), exact script text, `Roger`, `es`, 0.95, with `previous_text` and `next_text`. They add up to ≈ 88 s of voice (≈ 144 words per minute).
- **Plates:** 8 (`chips-i01` to `i08`), one per scene and two in scene 5. All 8 were looked at on a contact sheet. Reservations below.
- **Editing:** `System/scripts/build_chips.py` (based on `build_queque.py`): voices without cut sentences (0.25 s tail), 0.45 s between scenes and 1.2 s before the close, "page turn" between scenes, slow 5 % push, label cards on scenes 1 to 6, vignette and grain. No sound or music.
- **Render r1:** `render/chips-93s-9x16-r1.mp4`, **≈ 93 s**, 1080×1920 (the duration comes from the voices; longer than the 85 s in the script title).

### Reservations

- **Duration ≈ 93 s** (voice 88 s + intro and tail): longer than planned. If it is too much, cut Rapidus (scene 4) and the energy claim (scene 5) and regenerate only those two voices (≈ $0.03).
- **One plate every ≈ 10 s** (the rule asks for ≈ 4 s): only 8 images were approved.
- **#2:** the photo is of the Livermore prototype, not ASML's; the image looks almost like a model photo (little plasticine) and the figure is cropped at the side when filling 9:16.
- **#4 v2** (padlock): clean; the side crop cuts part of the chains.
- **#6, #7, #8:** they do not clearly show the mold (#6 has no mold, only the pattern; #7 has two plates instead of one lifting off; #8 has round chips and a small stamp). Accepted as "almost right" (rule 2.7): no retry is left in the cap.
- **On-screen text:** scene 5 does not show "energy ≈ ÷10 (Canon)" (one card at a time); only `5 nm today · 2 nm goal` (in Spanish on screen). Scene 7 has no card.
- ✅ **Checked:** the render finished (64 MB, 1080×1920, 92.95 s per the edit) and seven frames (seconds 3, 15, 28, 44, 60, 76 and 88): legible cards, not covering the subject, no symbols missing from the typeface.
- ❌ **I did not hear the audio or watch the whole video:** voice, pace, fades and whether plate changes land where they should. The mp4's duration was not read from its header (there is no `ffprobe` on this machine); it is the edit's.

### Awaiting your decision (P7)

1. **Watch and listen** to the mp4: voice, pace and whether the plates land where they should.
2. Do I shorten the duration (voice of scenes 4 and 5) or do you leave it at ≈ 93 s?
3. Do I redo #6, #7 or #8 (≈ $0.04 each, over the 9-image cap) or do you leave them?
4. To publish: title, description with sources (attribution for R1 and R3, "data as of 3 Oct 2026", TSMC figure as an **estimate**) and AI disclosure.
5. **New:** do you want an English version of this video (new script, ≈ $0.12 of voice, same plates, new render)?
