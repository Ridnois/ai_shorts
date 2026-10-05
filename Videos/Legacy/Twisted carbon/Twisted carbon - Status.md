---
type: research
created: 2026-10-04
updated: 2026-10-04
status: stages 0–6 done · render r1 · post-render feedback received (4 Oct 2026): narrative approved, illustrations failed · closed by the user on 4 Oct 2026: no rework, the learning stays in the vault · all gates delegated by the user ("follow all the steps for yourself until the render")
tags: [research, youtube, status, carbon, superconductors, metamaterials, shorts]
---

# Twisted carbon · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]]

Eighth video of the channel and the **second in English**. Idea: [[Twisted carbon]]. Media in `Media/Legacy/Twisted carbon - 85 seconds/` (files prefixed `tc-`).

> **Delegation (4 Oct 2026):** *"lets build a new video, this one is about carbon, metamaterial, superconductors and such. read this [CORDIS article], could be interesting. and follow all the steps for yourself until the render."* I take this as approval at every gate, **with the cap below**, and stop at the render (P7). This is the first video built with the new idea-quality rules ([[Idea and hook quality]]): facts bank, scoring, five hooks, size in words.

## Stage log

| Stage                | Status | Approved                    | Note                                                                                                |
| -------------------- | ------ | --------------------------- | --------------------------------------------------------------------------------------------------- |
| 0 Idea               | ✅ P1   | delegated                   | Angle chosen by scoring: geometry as a material (twisted graphene + metamaterials); 5 hooks written |
| 1 Research           | ✅ P2   | delegated                   | [[Research - Twisted carbon]]: 17 facts, 7 scored angles                                            |
| 2 Script             | ✅ P3   | delegated                   | [[Script - Twisted carbon]]: 185 words, 7 scenes                                                    |
| 3 Direction          | ✅ P4a  | delegated                   | 13 plates, in the script                                                                            |
| 4 Prompts and budget | ✅ P4   | delegated · **cap ≈ $0.76** | below                                                                                               |
| 5 Test               | ⏳      | delegated                   | plate 1 + scene 1 voice                                                                             |
| 6 Generation         | ⏳      | delegated                   |                                                                                                     |
| 7 Editing            | ⏳ P7   | —                           |                                                                                                     |
| 8 Publishing         | ⏳      | —                           |                                                                                                     |

## What was applied from the last iteration

Facts bank and scoring first; hook that gives a reason before the reaction; script sized in **words** (185) with no planned duration; no `Narration:` line in the image prompts, plus "no words, no letters, no captions" in every one; still states only; wide plates composed on a feathered 9:16 canvas; one **three-line card per plate**; references downloaded from `upload.wikimedia.org` directly (the thumbnail API throttled: 429 and timeouts).

## Reference photos (one per plate; Kontext accepts a single `input_image`)

Downloaded to `Media/Legacy/Twisted carbon - 85 seconds/plates/_refs/` (resized to ≤ 1,920 px). Licenses read from Wikimedia Commons on 4 Oct 2026.

| Ref. | Photo                                                                                                                                                                         | Author · license                    | Plates |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------ |
| R01  | [Graphite-crystal-structure](https://commons.wikimedia.org/wiki/File:Graphite-crystal-structure.jpg) (stacked layers of black spheres, a physical model)                      | MartinThoma · **CC0**               | 1, 6   |
| R03  | [Adhesive tapes clear](https://commons.wikimedia.org/wiki/File:Adhesive_tapes_clear.JPG)                                                                                      | BarberJP · **public domain**        | 3      |
| R04  | [Pencils, DM, 12](https://commons.wikimedia.org/wiki/File:Pencils,_DM,_12.jpg)                                                                                                | Kent Madsen · **CC BY-SA 2.0**      | 4, 13  |
| R05  | [Atomic scale moire patterns](https://commons.wikimedia.org/wiki/File:Atomic_scale_moire_patterns_(5940480205).jpg) (907×900)                                                 | NIST · **public domain**            | 2, 5   |
| R06  | [Liquid helium dewar](https://commons.wikimedia.org/wiki/File:Liquid_helium_dewar.jpg) (reused from the helium video)                                                         | Alkamid · **CC BY-SA 3.0**          | 7      |
| R07  | [Mercury escaped](https://commons.wikimedia.org/wiki/File:Mercury_escaped.jpg)                                                                                                | Tavo Romann · **CC BY 4.0**         | 8      |
| R08  | [Split-ring resonator array](https://commons.wikimedia.org/wiki/File:Split-ring_resonator_array_10K_sq_nm.jpg) (350×263, low resolution)                                      | NASA Glenn · **public domain**      | 9      |
| R09  | [Refraction of light at a prism (Wellcome)](https://commons.wikimedia.org/wiki/File:Refraction_of_light_at_a_prism._Wellcome_M0010893.jpg) (an engraved diagram with letters) | Wellcome Collection · **CC BY 4.0** | 10     |
| R10  | [1886VE10-Si-HD](https://commons.wikimedia.org/wiki/File:1886VE10-Si-HD.jpg) (a microchip die)                                                                                | ZeptoBars · **CC BY 3.0**           | 11     |
| R11  | [Optical Table with doubled Nd-YAG Laser (1)](https://commons.wikimedia.org/wiki/File:Optical_Table_with_doubled_Nd-YAG_Laser_-_(1).jpg)                                      | Giorgio Brida · **CC BY 2.0**       | 12     |

(A moiré-circles file, CC0, was dropped: at plate size it is nearly a flat grey.)

- **Attribution** goes in the description (CC BY and CC BY-SA need author and license; check the terms before publishing).
- **Risks:** R09 has letters (A to G) that may leak; R08 is low resolution; R11 is dark; R05 is a diagram, not a physical object. Every plate is checked for text and distortion.
- All references are horizontal or near-square: `match_input_image`; plates are composed onto 9:16 in editing.

## Prompts (P4)

**Model:** `black-forest-labs/flux-kontext-pro`, `aspect_ratio` `match_input_image`, PNG, one `input_image`. **Style block (appended to each prompt):**

```
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

The narration is **not** in the prompts (rule 2.11); every prompt ends with the "no words, no letters, no captions" line.

| #   | Ref. | Prompt (before the style block)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | R01  | Redraw this exact stack of three flat layers of black spheres joined by thin rods as a handmade plasticine clay miniature. Keep the three horizontal layers, each a flat grid of round spheres, one above another. Replace the background with a plain warm tabletop. The middle layer of spheres is in bright copper-orange clay. The stack fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                          |
| 2   | R05  | Redraw this exact pattern of two overlapping lattices of tiny dots turned slightly against each other, with large circular swirl patterns as a handmade plasticine clay miniature. Keep the two dot lattices and the swirl patterns they make. Replace the background with a plain warm tabletop. One lattice is matte grey clay. The other lattice is in bright copper-orange clay. The pattern fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                      |
| 3   | R03  | Redraw this exact transparent tape dispenser holding a roll of clear tape as a handmade plasticine clay miniature. Keep the clear dispenser body and the round roll of tape with a short strip pulled out. Replace the background with a plain warm tabletop. The roll of tape is in bright copper-orange clay. The dispenser fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                                         |
| 4   | R04  | Redraw this exact row of seven sharpened wooden pencils lying side by side as a handmade plasticine clay miniature. Keep the seven pencils, their round bodies and their sharpened cone tips. Replace the background with a plain warm tabletop. The graphite tips is in bright copper-orange clay. The pencils fill the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                                                        |
| 5   | R05  | Redraw this exact pattern of two overlapping lattices of tiny dots turned slightly against each other, with large circular swirl patterns as a handmade plasticine clay miniature. Keep the two dot lattices and the swirl patterns they make. Replace the background with a plain warm tabletop. All dots are matte grey clay except one large circular swirl cell in the centre, which is in bright copper-orange clay. The pattern fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos. |
| 6   | R01  | Redraw this exact stack of three flat layers of black spheres joined by thin rods as a handmade plasticine clay miniature. Keep the three layers of round spheres, with the top layer turned slightly so its grid is not aligned with the layers below. Replace the background with a plain warm tabletop. The top layer of spheres is in bright copper-orange clay. The stack fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                        |
| 7   | R06  | Redraw this exact tall insulated liquid helium dewar as a handmade plasticine clay miniature. Keep the tall cylindrical body, the rounded dome top with its neck and the wheeled base. Replace the background with a plain warm tabletop. The valve on top is in bright copper-orange clay. The dewar fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                                                                 |
| 8   | R07  | Redraw this exact group of shiny round mercury droplets spilled from two glass tubes as a handmade plasticine clay miniature. Keep the round droplets of different sizes and the two small glass tubes. Replace the background with a plain warm tabletop. All droplets are matte grey clay except the largest droplet, which is in bright copper-orange clay. The droplets fill the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                            |
| 9   | R08  | Redraw this exact array of tiny square split-ring resonators on thin upright boards as a handmade plasticine clay miniature. Keep the rows of thin upright boards with their small square ring patterns,, seen at an angle. Replace the background with a plain warm tabletop. One row of rings is in bright copper-orange clay. The array fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                            |
| 10  | R09  | Redraw this exact triangular glass prism with a thin ray of light entering one side and bending as it passes through as a handmade plasticine clay miniature. Keep a small clay triangular prism standing on the tabletop with a thin ray of clay bending through it. Replace the background with a plain warm tabletop. The bent ray is in bright copper-orange clay. The prism fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                      |
| 11  | R10  | Redraw this exact microchip die with a ring of small bond pads and large rectangular blocks as a handmade plasticine clay miniature. Keep the rectangular die, the ring of pads and the large dark blocks. Replace the background with a plain warm tabletop. The large block at the top is in bright copper-orange clay. The die fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                                     |
| 12  | R11  | Redraw this exact laboratory optical table with a green laser beam crossing small mirrors and lenses as a handmade plasticine clay miniature. Keep the table, the small mirrors and lenses and the beam crossing between them. Replace the background with a plain warm tabletop. The laser beam is in bright copper-orange clay. The table fills the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                           |
| 13  | R04  | Redraw this exact row of seven sharpened wooden pencils as a handmade plasticine clay miniature. Keep the seven pencils arranged in a tidy fan with the tips pointing the same way. Replace the background with a plain warm tabletop. The pencil in the middle is in bright copper-orange clay. The pencils fill the frame, vertical composition. The image contains no words, no letters and no captions of any kind. Remove all lettering and logos.                                                                                                                           |

**Voice:** `elevenlabs/v3`, `Roger`, `language_code: en`, `speed` 0.95, `previous_text` / `next_text`, 7 takes, exact script text (1,164 characters). "Kamerlingh Onnes" and "moiré" are written as is; if misread, a phonetic spelling is used and noted. **Sound and music:** none.

## On-screen cards (three lines per plate, see [[On-screen text style]])

| Plate | Label | Title | Detail |
| --- | --- | --- | --- |
| 1 | Carbon | One element, flat sheets | Graphite is a stack of graphene layers |
| 2 | Magic angle | Twist one sheet by 1.1° | Two graphene layers, MIT, 2018 |
| 3 | 2004, Manchester | Graphene peeled with tape | Geim and Novoselov, Nobel Prize 2010 |
| 4 | Same material | Pencil lead is graphite | Graphene is a single layer of it |
| 5 | Moiré pattern | Twist makes a big pattern | Electrons slow into nearly flat bands |
| 6 | Flat bands | Electrons act together | Insulating states, then zero resistance |
| 7 | 1911, Leiden | Mercury cooled in helium | Resistance vanishes near 4.2 K |
| 8 | Superconductor | Zero electrical resistance | Twisted graphene: up to 1.7 K |
| 9 | Metamaterial | Shape beats chemistry | Structures smaller than the wavelength |
| 10 | Proposed | Negative refraction | Veselago, 1960s · cloaks: Pendry, 2006 |
| 11 | GRAB-A-META | Graphene on a metamaterial | University of Birmingham, EU funded |
| 12 | Terahertz light | A voltage tunes the speed | EU project, 2015 to 2017 |
| 13 | The takeaway | Same carbon, new layout | Design instead of discovery |

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Image | `flux-kontext-pro` | **13** (one per plate) | ≈ $0.04 (**unconfirmed**) | **≈ $0.52** | 15 images (≈ $0.60) |
| Voice | `elevenlabs/v3` | 7 takes (1,164 characters) | ≈ $0.10 per 1,000 characters | **≈ $0.12** | 9 predictions (≈ $0.16) |
| Sound | — | 0 | — | $0 | — |
| P5 test | plate 1 + scene 1 voice | 2 | — | (inside the total) | |
| **Total and cap** | | | | **≈ $0.64** | **≈ $0.76** |

- Retries: one per image, in series; going over 15 images or 9 voice predictions stops the run.

## Prediction log

Format: `scene · category · model · status · prediction`.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | voice | `elevenlabs/v3` (`Roger`, `en`, 0.95) | ✅ (P5) | [fqq4tpaajsrmt0d10yjt26zavr](https://replicate.com/p/fqq4tpaajsrmt0d10yjt26zavr) |
| 2 | voice | same | ✅ | [pqw7vqkszhrmt0d10yjs9p2cdm](https://replicate.com/p/pqw7vqkszhrmt0d10yjs9p2cdm) |
| 3 | voice | same | ✅ | [4hr4y4cmz1rmt0d10yjvs7tyd0](https://replicate.com/p/4hr4y4cmz1rmt0d10yjvs7tyd0) |
| 4 | voice | same | ✅ | [c6b8pnnc6srmy0d10yjr56c664](https://replicate.com/p/c6b8pnnc6srmy0d10yjr56c664) |
| 5 | voice | same | ✅ | [jaa06ay62xrmw0d10yjrjzfgkc](https://replicate.com/p/jaa06ay62xrmw0d10yjrjzfgkc) |
| 6 | voice | same | ✅ | [n0kz5jf6m1rmy0d10yjs6zyprm](https://replicate.com/p/n0kz5jf6m1rmy0d10yjs6zyprm) |
| 7 | voice | same | ✅ | [59w870rk71rmr0d10yk81k174c](https://replicate.com/p/59w870rk71rmr0d10yk81k174c) |
| 1 | plate 1 | `flux-kontext-pro` (R01) | ✅ (P5; recovered after a hung download) | [wj644vg7h9rmt0d10yfvh251b4](https://replicate.com/p/wj644vg7h9rmt0d10yfvh251b4) |
| 1 | plate 2 | (R05) | ✅ | [51shbvmsrhrmw0d10yk9bajrv4](https://replicate.com/p/51shbvmsrhrmw0d10yk9bajrv4) |
| 2 | plate 3 | (R03) | ✅ | [b8dajxe2thrmt0d10ykbytm7e0](https://replicate.com/p/b8dajxe2thrmt0d10ykbytm7e0) |
| 2 | plate 4 | (R04) | ✅ | [1htcte7xgxrmt0d10yk9hkd75m](https://replicate.com/p/1htcte7xgxrmt0d10yk9hkd75m) |
| 3 | plate 5 | (R05) | ✅ | [qzwzee16pdrmt0d10ykt7ww240](https://replicate.com/p/qzwzee16pdrmt0d10ykt7ww240) |
| 3 | plate 6 | (R01) | ✅ | [q9smayanx1rmw0d10ykrd22dac](https://replicate.com/p/q9smayanx1rmw0d10ykrd22dac) |
| 4 | plate 7 | (R06) | ✅ | [392nhfcc81rmt0d10ykspfvtjc](https://replicate.com/p/392nhfcc81rmt0d10ykspfvtjc) |
| 4 | plate 8 | (R07) | ✅ | [x0mn3yxqndrmr0d10ykvx6c2yw](https://replicate.com/p/x0mn3yxqndrmr0d10ykvx6c2yw) |
| 5 | plate 9 | (R08) | ✅ | [5q8w2gf3ddrmt0d10yksk6hrwr](https://replicate.com/p/5q8w2gf3ddrmt0d10yksk6hrwr) |
| 5 | plate 10 | (R09) | ✅ | [57n2r589qdrmy0d10ymbsvv8a8](https://replicate.com/p/57n2r589qdrmy0d10ymbsvv8a8) |
| 6 | plate 11 | (R10) | ✅ | [padjs0hx2nrmt0d10ymbzbmkr0](https://replicate.com/p/padjs0hx2nrmt0d10ymbzbmkr0) |
| 6 | plate 12 | (R11) | ✅ | [3vzxwxkbesrmw0d10ymazgh0tc](https://replicate.com/p/3vzxwxkbesrmw0d10ymazgh0tc) |
| 7 | plate 13 | (R04) | ✅ | [8bvse1wzxsrmt0d10ym91sbn6w](https://replicate.com/p/8bvse1wzxsrmt0d10ym91sbn6w) |

**Predictions: 20** (7 voices + 13 images, all used; 2 images of cap left). Estimated cost: voice ≈ $0.12 + images 13 × ≈ $0.04 = ≈ $0.52 → **≈ $0.64**, inside the approved cap ≈ $0.76 (Kontext price unconfirmed).

## Findings from this run

- **No narration line in the prompts + "no words, no letters, no captions" in all 13: zero text leaks** (the helium video leaked one plate). Confirms rule 2.11. R09 (a diagram with letters A to G) was the risk; the prism plate came out clean.
- **Pace in words:** 185 words generated **83.0 s of voice** (from file sizes at 128 kbps) = **134 words per minute with pauses**, slower than the 144 of the helium video; per scene 120 to 156. Edited length **85.27 s**. The word range (130 to 190) held; the length (≈ 85 s) is a result, as the new rule says. Plan English at **135 to 145 wpm**.
- **Source photos can be abstract:** the NIST moiré diagram (R05) became two clay swirl shapes; it reads as "a pattern" but not as a lattice. The graphite-layers model (R01) and the prism diagram worked well because they are simple solids.
- **Infrastructure:** (1) the Wikimedia thumbnail/API endpoint throttled (429, timeouts): fetching originals from `upload.wikimedia.org/wikipedia/commons/<h0>/<h0h1>/<name>` (md5 path) worked instantly. (2) A download hung after the prediction succeeded and left a 0-byte file: `replicate_helper.py` now has timeouts, retries, prints the prediction id as soon as it exists and has `recover(id, dest)` to fetch a finished prediction without paying again. (3) Obsidian re-padded the Status table columns on save, which broke a strict regex that read prompts from the note: the parser must tolerate spaces. (4) Never `pkill -f` a pattern that appears in the shell command itself.

## Editing

- **Script:** `System/scripts/build_twisted_carbon.py` (from `build_helium2.py`): 7 voices (0.45 s between scenes, 1.2 s before the close, 0.25 s tail), 13 plates composed onto 1080×1920 with a feathered blurred background, a cross-fade within the scene and a page turn between scenes, slow 5 % push, **one three-line card per plate** (label, title, detail), vignette and grain. No sound or music.
- **Render r1:** `Media/Legacy/Twisted carbon - 85 seconds/render/tc-85s-9x16-r1.mp4`, **85.27 s**, 1080×1920.

![[tc-85s-9x16-r1.mp4]]


### What I checked and what I did not

- ✅ All 13 plates looked at together; no text or brand leaks, no retries. Twelve frames of the render (seconds 4 to 84): three-line cards legible, subjects clear, seams feathered. The render finished (57 MB, 1080×1920, 85.27 s per the edit).
- ❌ **I did not hear the audio or watch the whole video:** how `Roger` sounds in English, the pace (scenes 2, 4 and 5 are slow at 120 to 127 words per minute, scene 1 fast at 156), the fades, and whether plate changes land where they should.
- **Reservations:** plates 2 and 5 turned the NIST moiré diagram into clay swirls (they read as "a pattern", not as a lattice); plate 9 shows generic clay blocks instead of split rings; plate 12 is a small table with an orange stripe for the laser; plate 4 has five pencils, not seven. The card on the last plate is repeated across two plates (12 and 13 share the style, not the text).
- **Claims to confirm before publishing:** the 1.1° and 1.7 K figures (consistent across search summaries, arXiv and Physics World, but the *Nature* page itself was not opened); Veselago's date and Pendry's 2006 cloak proposal; the CORDIS "10-year retention" claim is not used.

### Awaiting your decision (P7)

1. **Watch and listen** to `tc-85s-9x16-r1.mp4`: is the hook now worth the reaction? Is `Roger` right in English?
2. Do any plates need redoing (≈ $0.04 each; 2 of the 15-image cap left)?
3. For publishing (P8): title, a description with the sources in [[Research - Twisted carbon]], the CC attributions for R01 to R11, "data as of 4 Oct 2026", the caveat that the 1.7 K superconductivity is at very low temperature (so "can" in the hook), and the AI disclosure, all in English.

## Post-render feedback (4 Oct 2026) and what changed

User feedback: [[Post-render feedback - Twisted carbon]]. **The narrative, the data and the voice are approved** (no change to the voice pipeline). **The illustrations failed**: they did not represent or describe the content. The whole illustration method was redesigned and the vault now applies it by default ([[Illustration pipeline]], [[Prompt - per-scene generation guide]], [[On-screen text style]], [[Channel identity]], [[Blender editing]], [[Feedback loop]], `CLAUDE.md`); the response table is at the end of the feedback note.

### Rework plan with the new pipeline (not executed: needs your OK, ≈ $0.27 + the voice is reused)

Visual plan for the same script (types: S stock, G generated explainer, C cutout, N number or text plate). Mix: 5 stock, 5 generated, 1 cutout, 2 number plates; no two consecutive plates of the same type.

| # | Scene | Type | What it lets the viewer see | So they understand | Source | Callouts and text |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | **G** | three stacked graphene lattices, the top one rotated 1.1° | what "twisting a sheet" physically means | `gpt-image-1.5`, reference: a moiré of twisted bilayer graphene (Openverse/Wikimedia, CC BY-SA) | "Top layer: 1.1°", "Bottom layer" |
| 2 | 1 | **S** | two identical grids overlapping with a small rotation | a small twist makes a large new pattern | Openverse: a moiré photo or diagram | "Moiré pattern" |
| 3 | 2 | **C** | a roll of sticky tape (cut out) on a gradient | how graphene was first peeled off graphite (Manchester, 2004) | stock photo + `bria/remove-background` | "Sticky tape", number or context card with Geim and Novoselov |
| 4 | 2 | **S** | pencils and graphite | the pencil lead is the same element (and layers) | Openverse | margin note: "Yes, the same carbon as your pencil lead." |
| 5 | 3 | **G** | a chart: a curved energy band (normal) next to a flat band | why a flat band means electrons barely move and start to interact | `gpt-image-1.5`, clean technical chart, no text | "Normal band", "Flat band" |
| 6 | 3 | **N** | the number 1.1° on a gradient | the single figure the whole effect depends on | built in Blender | number card: **1.1°**, "twist between two graphene layers", "Cao et al., Nature, 2018" |
| 7 | 4 | **S** | a liquid-helium dewar in a lab | the cold that discovered superconductivity (Leiden, 1911) | Wikimedia (CC BY-SA), already in the vault as R06 | "Liquid helium, 4.2 K", "Vacuum jacket" |
| 8 | 4 | **G** | a resistance-versus-temperature curve dropping to zero | what "zero resistance" looks like | `gpt-image-1.5`, simple chart, no text | "Mercury, 4.2 K", "Resistance = 0" |
| 9 | 5 | **S** | a split-ring metamaterial array | metamaterials are structures smaller than the wavelength | NASA Glenn (public domain), already in the vault as R08 | "Split ring", "Smaller than the wavelength" |
| 10 | 5 | **G** | light bending the "wrong" way into a negative-index material, next to glass | what negative refraction is | `gpt-image-1.5`, top-down diagram, no text | "Glass", "Negative index" |
| 11 | 6 | **S** | a terahertz or graphene device photo | that this is real hardware | Openverse (to find) | "Graphene device" |
| 12 | 6 | **G** | an exploded view of the device: gate electrode, one graphene layer, split-ring metamaterial, substrate | how a voltage on a single atomic layer tunes the light | `gpt-image-1.5`, exploded view, no text | "Gate electrode", "One layer of graphene", "Metamaterial", "Substrate" |
| 13 | 7 | **N** | a text plate on a gradient | the thesis in a line | built in Blender | context card: `What the 1.1° buys · One element, three behaviours · Insulator, conductor, superconductor` |

**Cost:** 5 generated plates ≈ $0.25 + one background removal (unmeasured) ≈ $0.27 in total; stock photos $0; the voice is reused. **Also free:** re-render with the padded and checked voices (the voice-start fix) from a `plan.json`, with or without the new plates. Tell me which you want: (a) only the voice-start fix, (b) the full rework, (c) neither.

**Decision (4 Oct 2026):** the user chose **neither** option (no voice-start re-render, no rework): *"C, lets keep the learning and move on on the next script."* This video stays as rendered (plasticine plates, v2 cards, the voice-start defect). Its value is the knowledge now in the vault ([[Illustration pipeline]], [[Channel identity]], [[Blender editing]], [[Feedback loop]]). The rework plan above is kept only as a worked example of the visual plan.

