---
type: research
created: 2026-10-03
updated: 2026-10-03
status: stages 0–4 done · generation in progress · all gates delegated by the user ("go for all steps by yourself")
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
| 5 Test | ⏳ | delegated | plate 1 + scene 1 voice |
| 6 Generation | ⏳ | delegated | |
| 7 Editing | ⏳ P7 | — | |
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

*(filled in below as the run goes)*
