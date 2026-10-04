---
type: research
created: 2026-10-04
updated: 2026-10-04
status: stages 0–3 done · delegated by the user ("build a youtube short all by yourself", 4 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7) · generating
tags: [research, youtube, status, superconductors, shorts]
---

# Superconductors · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]] · [[Script - Superconductors]]

Short 9:16, English, 162 words. Question: why can a superconductor carry current with zero resistance, and what would change without the freezer? Media in `Media/Superconductors/` (prefix `sc-`). First video built with the Magnetar-feedback rules: need-to-know opener, scientific explainers, no bare backdrops, word-by-word captions ([[Shorts quality bar]]).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | agent, under delegation | thread and rejected angles in [[Script - Superconductors]] |
| 1 Research | ✅ | agent | 17-fact bank, sources fetched 4 Oct 2026 (secondary: Wikipedia, EIA) |
| 2 Script | ✅ | agent | 162 words, 8 scenes |
| 3 Direction | ✅ | agent | visual plan below: 9 plates, 4 generated |
| 4 Prompts and budget | ✅ | **delegated by the user** (4 Oct 2026), cap ≈ $0.47 | below |
| 5 Test | ⏭ folded into 6 | delegation | a failed first plate is the test |
| 6 Generation | ⏳ | delegation | voice, then plates, in series |
| 7 Editing | ⏳ **P7 is yours** | | `Media/Superconductors/render/` |
| 8 Publishing | ⏳ | — | description below |

## Visual plan (S stock · G generated explainer)

| # | Scene | Type | Source | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- | --- |
| 1 | 1 | S | `sc-levitation.jpg` (Bobroff, CC BY-SA 3.0) | a magnet hovering over a cooled disc, so they know the thing the video is about is real |
| 2 | 2 | G | prompt G1 | electrons scattering in an ordinary wire next to pairs passing straight in a superconductor, so "resistance vanishes" has a picture |
| 3 | 2 | S | `sc-onnes.jpg` (public domain, 1923) | the man who found it, so the date and place have a face |
| 4 | 3 | G | prompt G2 | two electrons bound through a dent in the atom lattice, so "pairing" is concrete |
| 5 | 4 | S | `sc-levitation2.jpg` (Bobroff, CC BY-SA 3.0) | the magnet and the disc under it, so "expels magnetic fields" is seen as floating |
| 6 | 5 | G | prompt G3 | a closed ring with nothing connected to it, so "a current with no battery" is literal |
| 7 | 6 | S | `sc-lhc.jpg` (alpinethread, CC BY-SA 2.0) | the real LHC tunnel with its cryostats, so the scale of "cooled magnets" is clear |
| 8 | 7 | G | prompt G4 | two diamonds squeezing a tiny sample, so "a million atmospheres" is a device, not a number |
| 9 | 8 | S | `sc-pylon.jpg` (Novoklimov, CC0) | the grid that loses part of its power in the wires |

Mix: 5 S, 4 G; S and G alternate. 9 plates for ≈ 65 s: plates are held longer than the 4 to 6 s default because two photos (the Meissner and LHC scenes) have no honest second image; callouts, cards and the word-by-word captions carry the motion. Not used: SCMaglev photo, MRI photo (a visible brand), diamond-anvil photo (an identifiable person).

## Prompts (P4; `gpt-image-1.5`, 2:3, medium; specifications, not scenes; no style)

Every prompt ends with: *"Plain light-grey background. No glow, no light rays, no decorative particles, no text. The image contains no letters, no numbers and no labels."* (rule 2.13)

- **G1 · resistance.** A clean technical schematic, two long horizontal wires stacked one above the other, each drawn as a cut-open cylinder showing a regular grid of identical atoms inside. In the upper wire, single electrons (small spheres, much smaller than the atoms) travel left to right and several are deflected at an angle where they pass close to an atom. In the lower wire, the same atom grid, but the electrons travel in pairs (two small spheres side by side) in straight parallel lines left to right, none deflected. Same scale in both wires.
- **G2 · pairing.** A side view of a crystal lattice: a regular grid of identical positively charged ions as grey spheres. One electron (a small blue sphere) has just passed through the middle and the ions nearest to its path are drawn slightly pulled toward it, a visible dent in the grid. A second small blue sphere sits a few ion spacings behind, drawn toward the dent. Electrons are much smaller than ions. Nothing else.
- **G3 · persistent current.** A simple closed circular ring of thick metal wire shown lying flat inside the cutaway of an open-top insulated vessel filled with pale liquid; three small arrowheads on the ring, all pointing the same way around it, show the current direction. Nothing is connected to the ring: no battery, no cables, no components.
- **G4 · diamond anvil cell.** A cross-section schematic of a diamond anvil cell: two cut diamonds facing each other, their flat tips almost touching; between the tips a thin metal gasket sheet with a tiny round hole, and a microscopic sample in the hole. A large arrow above and a large arrow below press the diamonds together. A plain metal body holds the diamonds. Nothing else.

Each generated plate is checked for leaked text and against the research note; one retry per image (rules 2.7 and 2.13).

## Budget in dollars (cap = base × 1.2)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` Roger `en`, speed 0.95 | 8 takes, ≈ 990 characters | ≈ $0.10 per 1,000 characters | ≈ $0.10 | ≈ $0.12 |
| Image (generated) | `gpt-image-1.5` medium 2:3 | 4 plates | ≈ $0.05 (**unconfirmed on Replicate**) | ≈ $0.20 | ≈ $0.24 |
| Word timings | `vaibhavs10/incredibly-fast-whisper` | 8 takes of 4 to 12 s | ≈ $0.01 (**unconfirmed**) | ≈ $0.08 | ≈ $0.10 |
| Image (stock) | free sources | 5 plates | $0 | $0 | — |
| Sound, background removal | none | 0 | — | $0 | — |
| **Total and cap** | | | | **≈ $0.38** | **≈ $0.46** |

Planned duration is not set: 162 words ≈ 67 s at ≈ 144 wpm (derived, not planned).

## Stock credits (`Media/Superconductors/stock/_credits.jsonl`)

| File | Title | Author | License | Page |
| --- | --- | --- | --- | --- |
| `sc-levitation.jpg` | Levitation of a magnet on a superconductor | Julien Bobroff and Frederic Bouquet | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Levitation_of_a_magnet_on_a_superconductor.jpg) |
| `sc-levitation2.jpg` | Levitation of a magnet on top of a superconductor 2 | Julien Bobroff and Frederic Bouquet | CC BY-SA 3.0 | [Commons](https://commons.wikimedia.org/wiki/File:Levitation_of_a_magnet_on_top_of_a_superconductor_2.jpg) |
| `sc-onnes.jpg` | Heike Kamerlingh Onnes, 1923 | unknown | public domain | [Commons](https://commons.wikimedia.org/wiki/File:Heike_Kamerlingh_Onnes,_1923.jpg) |
| `sc-lhc.jpg` | LHC dipole magnets | alpinethread | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:LHC_dipole_magnets.jpg) |
| `sc-pylon.jpg` | Anchor pylon of high-voltage overhead power line 750 kV | Novoklimov | CC0 | [Commons](https://commons.wikimedia.org/wiki/File:Anchor_pylon_of_high-voltage_overhead_power_line_750_kV.jpg) |

Looked at all five: no text or brand, except the LHC photo, which shows a "MEYER" label on a box at its right edge: the plate focus keeps it out of the 9:16 crop (checked on the render stills).

## Prediction log

`scene · category · model · status · cost · URL`
