---
type: research
created: 2026-10-03
updated: 2026-10-03
status: stages 0–6 done · render r1 · awaiting P7 · all gates delegated by the user ("go for all steps by yourself")
tags: [research, youtube, status, helium, shorts]
---

# Helium - why it cannot be made · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]]

Seventh video of the channel and the **first made entirely in English**. Idea: [[Helium - why it cannot be made]]. Media in `Media/Helium - 70 seconds/` (files prefixed `he2-`; `helio-` belongs to the earlier helium video).

> **Delegation (3 Oct 2026):** *"Now go for another script, this one about the importance of helium again, learn from the last iteration and improve it, go for all steps by yourself this time."* I take the user's approval at P1–P4a, P4, P5 and P6 as given by this instruction, **with the cap below**, and stop at the render for P7.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | 3 Oct 2026 · delegated | Different angle from [[Helium and power - Status]]: why helium cannot be made |
| 1 Research | ✅ P2 | delegated | [[Research - Helium - why it cannot be made]]: 15 claims; 3 left out as vendor-sourced |
| 2 Script | ✅ P3 | delegated | [[Script - Helium - why it cannot be made (70 seconds)]]: 175 words, 7 scenes |
| 3 Direction | ✅ P4a | delegated | 13 plates, in the script |
| 4 Prompts and budget | ✅ P4 | delegated · **cap ≈ $0.74** | below |
| 5 Test | ✅ P5 | delegated | plate 1 (clean: clay look, no brand leak) + scene 1 voice; I could not judge the voice's sound |
| 6 Generation | ✅ P6 | delegated | 7 voices, 13 plates + 2 retries (15 images = cap), all in series |
| 7 Editing | ✅ render r1 · ⏳ P7 | — | `Media/Helium - 70 seconds/render/he2-76s-9x16-r1.mp4` |
| 8 Publishing | ⏳ | — | |

## What I applied from the last iteration

See the table in the script note. In short: shorter (≈ 70 s), 13 plates instead of 8, a real photo per plate, still states only, references checked for text, voice pace measured as soon as the takes exist.

## Reference photos (one per plate; Kontext accepts a single `input_image`)

Downloaded to `Media/Helium - 70 seconds/plates/_refs/` (resized to ≤ 1,920 px). Licenses checked on Wikimedia Commons on 3 Oct 2026.

| Ref. | Photo | Author · license | Plates |
| --- | --- | --- | --- |
| R01 | [MRI-Philips](https://commons.wikimedia.org/wiki/File:MRI-Philips.JPG) | Jan Ainali · **CC BY 3.0** | 1, 11 |
| R02 | [Liquid helium dewar](https://commons.wikimedia.org/wiki/File:Liquid_helium_dewar.jpg) | Alkamid · **CC BY-SA 3.0** | 2, 13 |
| R03 | [Uraninite-3cm](https://commons.wikimedia.org/wiki/File:Uraninite-3cm.jpg) | 책읽는달팽 · **CC BY-SA 3.0** | 3 |
| R04 | [Aerial view of Kapuni Natural Gas Wellhead](https://commons.wikimedia.org/wiki/File:Aerial_view_of_Kapuni_Natural_Gas_Wellhead,_Kapuni,_Taranaki._(41487975151).jpg) (900×689, black and white) | Archives New Zealand · **CC BY 2.0** | 4 |
| R05 | [Mt. Fuji and Keiyo petrochemical complex](https://commons.wikimedia.org/wiki/File:Mt._Fuji_and_Keiyo_petrochemical_complex.JPG) | Nanashinodensyaku · **CC BY-SA 4.0** | 5 |
| R06 | [Πέτα (balloons)](https://commons.wikimedia.org/wiki/File:%CE%A0%CE%AD%CF%84%CE%B1_-_Flickr_-_philos_from_Athens.jpg) | Christos Loufopoulos · **CC BY 2.0** | 6 |
| R07 | [Liquid nitrogen ŚFN 2025 (2)](https://commons.wikimedia.org/wiki/File:Liquid_nitrogen_%C5%9AFN_2025_(2).jpg) | Adrian Tync · **CC BY-SA 4.0** | 7 |
| R08 | [Wafer with Pentium chips](https://commons.wikimedia.org/wiki/File:Wafer_with_Pentium_chips.jpg) | Naotake Murayama · **CC BY 2.0** | 8 |
| R09 | [Minerva Amorgos (LNG tanker)](https://commons.wikimedia.org/wiki/File:Minerva_Amorgos_(LNG-Tanker).jpg) | Rhetos · **CC0** | 9 |
| R10 | [Bundle of compressed gas bottles](https://commons.wikimedia.org/wiki/File:2008-07-24_Bundle_of_compressed_gas_bottles.jpg) | Ildar Sagdejev · **CC BY-SA 4.0** | 10 |
| R11 | [Community Diagnostics Centre Mobile MRI Scanner](https://commons.wikimedia.org/wiki/File:Community_Diagnostics_Centre_Mobile_MRI_Scanner,_Kingston_upon_Hull_Dec25.jpg) | Hullian111 · **CC BY-SA 4.0** | 12 |

- **Attribution** goes in the description (CC BY and CC BY-SA need author and license; check the terms before publishing).
- **Text in the references:** R01 (scanner brand), R02 (dewar label "LIQUID HELIUM"), R10 (cylinder markings), R11 (trailer lettering). Every prompt asks to remove lettering and logos; **each plate is checked for leaks** (rule 2.10).
- R04 is low resolution and old black and white: the least reliable reference.
- All references are horizontal or 3:4: `match_input_image`; the edit fills 9:16 with the `max` scale.

## Prompts (P4)

**Model:** `black-forest-labs/flux-kontext-pro`, `aspect_ratio` `match_input_image`, PNG, one `input_image`. **Style block (at the end of each prompt):**

```
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

Each prompt = narration sentence + "Redraw this exact … as a handmade plasticine clay miniature. Keep …" + still state + accent + "fills the frame, vertical composition. Remove all lettering and logos." + style block.

| # | Ref. | Prompt (before the style block) |
| --- | --- | --- |
| 1 | R01 | Narration: "An MRI scanner can hold fifteen hundred liters of liquid helium." Redraw this exact MRI scanner as a handmade plasticine clay miniature. Keep the large round scanner ring with its central tunnel and the long patient table in front of it. Replace the background with a plain warm tabletop. The tunnel ring is in bright copper-orange clay. The scanner fills the frame, vertical composition. Remove all lettering and logos. |
| 2 | R02 | Narration: "Every atom of it was made underground, by radioactive rock." Redraw this exact tall insulated liquid helium dewar as a handmade plasticine clay miniature. Keep the tall cylindrical body, the rounded dome top with its neck and the wheeled base. Replace the background with a plain warm tabletop. The valve on top is in bright copper-orange clay. The dewar fills the frame, vertical composition. Remove all lettering and logos. |
| 3 | R03 | Narration: "Uranium and thorium decay, and each decay fires out one helium nucleus." Redraw this exact dark rock as a handmade plasticine clay miniature. Keep its rough, angular, dark shape. Replace the background with a plain warm tabletop. A few tiny specks on the rock's surface are in bright copper-orange clay. The rock fills the frame, vertical composition. Remove all lettering and logos. |
| 4 | R04 | Narration: "Some gets trapped beneath rock, with natural gas." Redraw this exact aerial view of flat farmland with a small industrial gas pad as a handmade plasticine clay diorama. Keep the field patches, the road and the small industrial pad in the middle. The industrial pad is in bright copper-orange clay. The diorama fills the frame, vertical composition. Remove all lettering and logos. |
| 5 | R05 | Narration: "No factory speeds up radioactive rock." Redraw this exact petrochemical complex with tall chimneys as a handmade plasticine clay miniature. Keep the row of tall chimneys and the low industrial buildings. Replace the distant landscape with a plain warm tabletop backdrop. The top of the tallest chimney is in bright copper-orange clay. The complex fills the frame, vertical composition. Remove all lettering and logos. |
| 6 | R06 | Narration: "Helium is so light that once it escapes, it leaves the planet for good." Redraw this exact bunch of balloons tied to one string as a handmade plasticine clay miniature. Keep the round balloons and the string. Replace the background with a plain warm tabletop backdrop. One balloon is in bright copper-orange clay. The balloons fill the frame, vertical composition. Remove all lettering and logos. |
| 7 | R07 | Narration: "Helium boils at four degrees above absolute zero." Redraw this exact glass dish with cold fog spilling over its edge as a handmade plasticine clay miniature. Keep the round shallow dish and the curling fog. Replace the background with a plain warm tabletop. A small patch of frost in the dish is in bright copper-orange clay. The dish fills the frame, vertical composition. Remove all lettering and logos. |
| 8 | R08 | Narration: "MRI magnets need that cold, and chip factories use it too." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of small rectangular chips. Replace the background with a plain warm tabletop. All chips are matte grey clay and exactly one cluster of chips in the centre is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 9 | R09 | Narration: "This year a war cut off Qatar." Redraw this exact liquefied natural gas tanker at sea as a handmade plasticine clay miniature. Keep the long dark hull, the row of white round cargo domes and the ship's bridge. Replace the sea with a plain warm tabletop. The cargo domes are in bright copper-orange clay. The tanker fills the frame, vertical composition. Remove all lettering and logos. |
| 10 | R10 | Narration: "Only a few places supply it, and the price doubled." Redraw this exact group of tall gas cylinders chained to a wall as a handmade plasticine clay miniature. Keep the tall rounded cylinders, their caps and the chain. Replace the background with a plain warm tabletop backdrop. The middle cylinder is in bright copper-orange clay. The cylinders fill the frame, vertical composition. Remove all lettering and logos. |
| 11 | R01 | Narration: "One sealed magnet holds seven liters, not fifteen hundred." Redraw this exact MRI scanner as a handmade plasticine clay miniature. Keep the large round scanner ring with its central tunnel and the patient table. Replace the background with a plain warm tabletop. A tiny bottle stands on the table beside the scanner and is in bright copper-orange clay. The scanner fills the frame, vertical composition. Remove all lettering and logos. |
| 12 | R11 | Narration: "Another holds less than one." Redraw this exact white mobile MRI trailer as a handmade plasticine clay miniature. Keep the long white box shape on its wheels and the ventilation grille. Replace the street with a plain warm tabletop. A tiny bottle stands on the table beside the trailer and is in bright copper-orange clay. The trailer fills the frame, vertical composition. Remove all lettering and logos. |
| 13 | R02 | Narration: "The safest supply is the helium that never escapes." Redraw this exact tall insulated liquid helium dewar as a handmade plasticine clay miniature. Keep the tall cylindrical body, the rounded dome top with its neck and the wheeled base. Replace the background with a plain warm tabletop. A small closed padlock hangs on the valve on top and is in bright copper-orange clay. The dewar fills the frame, vertical composition. Remove all lettering and logos. |

**Voice:** `elevenlabs/v3`, voice `Roger`, `language_code: en`, `speed` 0.95, `previous_text` / `next_text`, 7 takes, exact script text (997 characters). Acronym "MRI" is written as is; if misread it is spelled "M R I". **Sound and music:** none.

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Image | `flux-kontext-pro` | **13** (one per plate, each with its second) | ≈ $0.04 (**unconfirmed**) | **≈ $0.52** | 15 images (≈ $0.60) |
| Voice | `elevenlabs/v3` | 7 takes (997 characters) | ≈ $0.10 per 1,000 characters | **≈ $0.10** | 9 predictions (≈ $0.12) |
| Sound | — | 0 | — | $0 | — |
| P5 test | plate 1 + scene 1 voice | 2 | — | (inside the total; ≈ $0.05) | |
| **Total and cap** | | | | **≈ $0.62** | **≈ $0.72** (approved cap ≈ $0.74) |

- Retries: one per image, in series; going over 15 images or 9 voice predictions stops the run and asks.
- For comparison: Chips ≈ $0.48 (8 plates), Lemon cake ≈ $1.57 (20 plates).

## Prediction log

Format: `scene · category · model · status · prediction`.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | voice | `elevenlabs/v3` (`Roger`, `en`, 0.95) | ✅ used (P5) | [edrn01w81srmr0d10j1tf7013m](https://replicate.com/p/edrn01w81srmr0d10j1tf7013m) |
| 2 | voice | same | ✅ | [npt5h467p9rmy0d10j1tnkmm54](https://replicate.com/p/npt5h467p9rmy0d10j1tnkmm54) |
| 3 | voice | same | ✅ | [byt6xw6ygsrmt0d10j1shtanf8](https://replicate.com/p/byt6xw6ygsrmt0d10j1shtanf8) |
| 4 | voice | same | ✅ | [q2qa38zcmxrmt0d10j1s8vfxyw](https://replicate.com/p/q2qa38zcmxrmt0d10j1s8vfxyw) |
| 5 | voice | same | ✅ | [xjm0kf088xrmw0d10j29zn0knr](https://replicate.com/p/xjm0kf088xrmw0d10j29zn0knr) |
| 6 | voice | same | ✅ | [xrv45m8zv9rmt0d10j2a5gcds0](https://replicate.com/p/xrv45m8zv9rmt0d10j2a5gcds0) |
| 7 | voice | same | ✅ | [bzwhvdsqqxrmr0d10j29z50x14](https://replicate.com/p/bzwhvdsqqxrmr0d10j29z50x14) |
| 1 | plate 1 | `flux-kontext-pro` (R01) | ✅ used (P5) | [4dmw0nv7zhrmy0d10j1v60mjmg](https://replicate.com/p/4dmw0nv7zhrmy0d10j1v60mjmg) |
| 1 | plate 2 | (R02) | ✅ | [p0rfaw32x5rmt0d10j2a0g5tar](https://replicate.com/p/p0rfaw32x5rmt0d10j2a0g5tar) |
| 2 | plate 3 | (R03) | ✅ | [q2ye19mbfhrmr0d10j29jmr18c](https://replicate.com/p/q2ye19mbfhrmr0d10j29jmr18c) |
| 2 | plate 4 | (R04) | ✅ | [ch5tpmxsphrmt0d10j2bj2rq7c](https://replicate.com/p/ch5tpmxsphrmt0d10j2bj2rq7c) |
| 3 | plate 5 | (R05) | ✅ | [8wmewxynw5rmw0d10j29nyqp7m](https://replicate.com/p/8wmewxynw5rmw0d10j29nyqp7m) |
| 3 | plate 6 | (R06) | ✅ | [rxrt1zgaj5rmr0d10j2v5d0550](https://replicate.com/p/rxrt1zgaj5rmr0d10j2v5d0550) |
| 4 | plate 7 | (R07) | ✅ | [7kpj7t1g89rmw0d10j2vtb3ywc](https://replicate.com/p/7kpj7t1g89rmw0d10j2vtb3ywc) |
| 4 | plate 8 | (R08) | ✅ | [2kkmgsax75rmy0d10j2ts4kajc](https://replicate.com/p/2kkmgsax75rmy0d10j2ts4kajc) |
| 5 | plate 9 v1 | (R09) | ❌ discarded: **the narration sentence leaked into the image as garbled text** | [pc1vkxcfvnrmt0d10j2rty99mc](https://replicate.com/p/pc1vkxcfvnrmt0d10j2rty99mc) |
| 5 | plate 9 v2 | (R09), no narration line, "no words" | ✅ (retry) | [8rjajqdwrxrmt0d10j39755bag](https://replicate.com/p/8rjajqdwrxrmt0d10j39755bag) |
| 5 | plate 10 | (R10) | ✅ | [s5hazne3hsrmt0d10j2vgt6rgm](https://replicate.com/p/s5hazne3hsrmt0d10j2vgt6rgm) |
| 6 | plate 11 | (R01) | ✅ | [sn8pdf7m89rmr0d10j2s8ae0e0](https://replicate.com/p/sn8pdf7m89rmr0d10j2s8ae0e0) |
| 6 | plate 12 | (R11) | ✅ | [vtdnmkrhfhrmy0d10j3ass3968](https://replicate.com/p/vtdnmkrhfhrmy0d10j3ass3968) |
| 7 | plate 13 v1 | (R02) | ❌ discarded: padlock barely visible | [cvabr19nv1rmr0d10j3a8brhk8](https://replicate.com/p/cvabr19nv1rmr0d10j3a8brhk8) |
| 7 | plate 13 v2 | (R02), larger padlock | ✅ (retry) | [nmg0mefa41rmy0d10j3avpjfr4](https://replicate.com/p/nmg0mefa41rmy0d10j3avpjfr4) |

**Predictions: 22** (7 voices + 15 images: 13 used + 2 discarded) against a cap of 9 voices and 15 images: **within the cap, with no images left over.** Estimated cost: voice ≈ $0.10 · images 15 × ≈ $0.04 = ≈ $0.60 · **≈ $0.70** (Kontext price unconfirmed), approved cap ≈ $0.74.

## Findings from this run

- **The narration line in the prompt can leak into the image.** Plate 9 printed "This year a war cut off/QCoUnr". The other 12 prompts, which carried the same kind of line, did not. Rule for next time: put the narration only in the notes, or keep it and add "The image contains no words, no letters and no captions of any kind"; check every plate for text.
- **Still states worked.** All 13 plates read clearly; the two "add a tiny bottle" plates (11, 12) and the padlock (13) worked because the added object is still and simple.
- **English pace measured:** 175 words in ≈ 72.9 s of voice (from file sizes at 128 kbps) = **≈ 144 words per minute with pauses**; individual scenes ran from 121 to 179. Update [[Channel voice]] and the guidelines with this figure.
- **Wide plates:** composing each plate onto a 1080×1920 canvas with a blurred background (instead of covering the height) kept the whole tanker, the dish and the gas field in frame. The first composite showed hard seams where the sharp plate met the blur; the final one feathers the edges (PIL gradient mask; this machine's system Python has no `numpy`, and the first attempt failed silently inside a chained command, so check that generated files actually changed).

## Editing (3 Oct 2026)

- **Script:** `System/scripts/build_helium2.py` (from `build_chips.py`). 7 voices (0.45 s between scenes, 1.2 s before the close, 0.25 s tail), 13 plates (2 per scene, 1 in the last; ≈ 5 s each, a cross-fade within the scene and a page turn between scenes), slow 5 % push, label cards on scenes 1 to 6 (English text), vignette and grain. No sound or music.
- **Render r1:** `Media/Helium - 70 seconds/render/he2-76s-9x16-r1.mp4`, **≈ 75.8 s**, 1080×1920.


**Spend (estimated):** voice ≈ $0.10 + images 15 × ≈ $0.04 = ≈ $0.60 → **≈ $0.70**, inside the approved cap ≈ $0.74 (Kontext price unconfirmed).

### What I checked and what I did not

- ✅ All 13 used plates looked at together on a contact sheet; the two discarded ones are in `plates/_descartes/`. No brand or text leaks in the final plates.
- ✅ Render finished (50 MB, 1080×1920, 75.84 s per the edit) and seven frames (seconds 3, 13, 27, 37, 50, 62, 72): cards legible, subjects clear, seams feathered.
- ❌ **I did not hear the audio or watch the whole video:** how `Roger` sounds in English, the pace (per scene it ran from 121 to 179 words per minute; scene 4 is the slowest, scene 7 the fastest), the fades, and whether plate changes land where they should.
- **Reservations:** plates 11 and 12 add a tiny orange bottle that reads as a bottle, not as "seven liters" (the card says it); plate 4 is a flat clay slab of a gas field, not a wellhead; plate 7's accent reads as a frost blob. The sealed-magnet figures (7 L, 0.7 L) are **manufacturer claims** (Philips, Siemens): say so in the description.

### Awaiting your decision (P7)

1. **Watch and listen** to `he2-76s-9x16-r1.mp4`: is the English voice (`Roger`) right, or should I test `Bradford`? Is the pace OK?
2. Do any plates need redoing (≈ $0.04 each, over the 15-image cap)?
3. For publishing (P8): title, a description with sources (the research note), the CC attributions for R01–R11, "data as of 3 Oct 2026", the manufacturer-figures caveat for the sealed magnets, and the AI disclosure, all in English.
