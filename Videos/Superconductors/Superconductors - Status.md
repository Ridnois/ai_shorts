---
type: research
created: 2026-10-04
updated: 2026-10-04
status: stages 0–3 done · delegated by the user ("build a youtube short all by yourself", 4 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7) · render r2 built (brand layer, sound design), awaiting P7
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
| 6 Generation | ✅ | delegation | 8 voice takes, 4 plates (no retry needed), 8 word-timing runs |
| 7 Editing | ⏳ **P7 is yours** | | `Media/Superconductors/render/sc-72s-9x16-r2.mp4` (r1 deleted; r2 adds the brand layer, the sound design, copper key terms and `sc.srt`) |
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
- Voice · `elevenlabs/v3` Roger `en` 0.95 (`previous_text`/`next_text`), 8 takes, 997 characters · ✅ `voice/sc-s1…s8-voice-v1.mp3` · s2 to s8 ids: [8k5hhsvy…](https://replicate.com/p/8k5hhsvy29rmt0d11089j9xhrr), na678sxg…, aqx6ekf4…, 8y71qsrp…, harx1629…, ypv3r2m0…, y1s51fxj… (s1's id was lost when the first call failed on a 429 before the helper retried; one take, no regeneration)
- Images · `gpt-image-1.5` medium 2:3 png · ✅ `plates/sc-p02-wires-v1`, `sc-p04-pairing-v1`, `sc-p06-loop-v1`, `sc-p08-anvil-v1` · [j0b7rjth…](https://replicate.com/p/j0b7rjth0xrmy0d1109bz5vbmw), [f003ebwc…](https://replicate.com/p/f003ebwcbdrmw0d11099aypdpm), [1qwfaepa…](https://replicate.com/p/1qwfaepa6drmy0d1109b1gx6sr), [zt1ssdrh…](https://replicate.com/p/zt1ssdrhysrmt0d1109vqa1f28) · no retry
- Word timings · `incredibly-fast-whisper` word, 8 runs, ≈ 0.4 s of compute each (cost ≈ cents; **price not read from Replicate**) · ✅ `voice/*.words.json`
- Several HTTP 429s (no prediction created, no cost); the helper now waits and retries.
- **Total: 20 predictions, ≈ $0.30 of the ≈ $0.46 cap** (voice ≈ $0.10, images ≈ $0.20 at the unconfirmed $0.05, whisper negligible).

## Plate checks (looked at each generated plate; stock photos looked at before use)

| Plate | Checked against the research note | Known simplification |
| --- | --- | --- |
| G1 wires | upper wire: electrons deflected near atoms; lower: pairs, straight lines; no text | atoms are drawn touching, electrons almost atom-sized; a schematic, not to scale |
| G2 pairing | a dent of ions around one electron, a second one drawn toward it; no text | real Cooper pairs are far larger than the atom spacing (**size not verified here**); the first electron is drawn larger by perspective |
| G3 loop | a closed ring, current arrows, nothing connected; no text | the vessel is generic (not a real gravimeter); the liquid looks milky; one arrow is not exactly tangent |
| G4 anvil | two cut diamonds tip to tip, a gasket with a hole, a sample, force arrows; no text | the sample is drawn as a gold dot |

## Editing (render r1)

`Media/Superconductors/plan.json` → `System/scripts/build_video.py`: **71.9 s** (derived: 162 words ≈ 135 wpm with pauses), 1080×1920, 24 fps. `CHECK=1`: `all voices complete`. `CAPTIONS 162 words, timed by whisper`.

- **Looked at (stills at 1.5, 2, 3.5, 8, 10 to 70 s):** captions legible and on the figure; cards and callouts on real images; no leaked text in the four plates; the LHC "MEYER" label is out of the crop. Two fixes after the first build: the levitation plate moved to `contain` (the disc was hidden under the caption zone) and callouts moved to their own channels (the third callout ghosted the diamond-anvil number card); a long caption word now shrinks to fit.
- **Plate durations (derived):** 5.3, 3.8, 3.8, 7.1, 9.1, 8.0, 9.4, 11.9, 6.9, 6.9 s. **Three plates exceed the 8 s ceiling of [[Shorts quality bar]] §4 (levitation, LHC, diamond anvil at 11.9 s):** there is no honest second image for them; callouts arrive at +1.0, +1.6 and +2.2 s and a card at +0.45 s. If it drags at P7, rework with a second explainer (over the 5-image cap, needs approval) or a second photo.
- **Opener:** first clause "Some wires carry electricity with zero resistance" ends at 2.9 s (whisper timing).
- **Not verified:** how the voice sounds, whether the captions land on the spoken words in motion, the pace, the transitions; the full video was not watched. Gate P7 stays with the user.
- **Content to check before publishing:** the primary sources named in [[Script - Superconductors]] (Drozdov 2015 and 2019, the Dias retractions, the gravimeter record); the facts come from Wikipedia and EIA.

## Render r2: brand layer and sound design (user request, 4 Oct 2026)

- **Brand layer:** progress bar at the top filling over 71.9 s, ring-and-dot mark and the series tag "The mechanism" top-left (the tag got a dark outline after a still showed it unreadable on light plates). Looked at stills at 1, 9, 24, 36, 55 and 70 s.
- **Copper key terms in the captions:** `keywords` = zero, resistance, pairing, freezer, miracle (plus every figure).
- **Caption file:** `Media/Superconductors/render/sc.srt` (5 words per cue) to upload as a caption track.
- **Sound design:** synthesized by the builder; `SOUND sfx` peak 0.150 and rms 0.0055, `SOUND bed` peak 0.024 and rms 0.0088, against voice ≈ −22 dBFS; `sfx_gain` 0.7. **Not heard.** Check at P7: is the opening thump too hard, are the whooshes audible under the voice, does the drone bed disturb? Dials: `sound` in `plan.json`.
- **Not verified:** how the top bar and tag sit under YouTube's own top overlay; the mix.

## Description draft (stage 8)

Why superconductors carry current with zero resistance, and what a room-temperature one could change, in about 70 seconds. Sources: Wikipedia articles *Superconductivity*, *Meissner effect*, *Room-temperature superconductor*, *Large Hadron Collider*; EIA FAQ 105 (transmission losses 2018 to 2022); to be confirmed against Drozdov et al., *Nature* 2015 and 2019. Photos: J. Bobroff and F. Bouquet (CC BY-SA 3.0), alpinethread (CC BY-SA 2.0), Novoklimov (CC0), H. Kamerlingh Onnes portrait, 1923 (public domain), via Wikimedia Commons. Schematic plates generated with AI (gpt-image-1.5), not to scale; voice generated with AI (ElevenLabs v3); sound design synthesized in Blender. Data as of 4 Oct 2026.
