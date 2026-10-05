---
type: research
created: 2026-10-05
updated: 2026-10-05
status: stages 0–3 done · delegated by the user ("from start to end you're allowed to decide and execute", 5 Oct 2026): P4 to P6 run by the agent within the cap, stop at the render (P7)
tags: [research, youtube, status, asteroid-mining, shorts]
---

# Asteroid mining · status

← [[YouTube Channel]] · [[Script - Asteroid mining]] · [[Fast workflow]] · [[Guidelines for new scripts]]

Short 9:16, English, 162 words. Question: what are the steps of a real asteroid mine, and which are nobody close to solving? Media in `Media/Asteroid-mining/` (prefix `am-`). Brand: the channel is now **Cutaway** with the fox, the Short itself carries no branding ([[Channel playbook]] §4).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | agent, under delegation | 19-fact bank, scoring and five hooks in [[Script - Asteroid mining]] |
| 1 Research | ✅ | agent | sources fetched 5 Oct 2026, all secondary (Wikipedia, University of Arizona News) |
| 2 Script | ✅ | agent | 162 words, 7 scenes |
| 3 Direction | ✅ | agent | visual plan below: 19 plates, 2 generated |
| 4 Prompts and budget | ✅ | **delegated by the user** (5 Oct 2026), cap ≈ $0.33 | below |
| 5 Test | ⏭ folded into 6 | delegation | |
| 6 Generation | ⏳ | delegation | |
| 7 Editing | ⏳ **P7 is yours** | | |
| 8 Publishing | ⏳ | — | |

## Visual plan (S stock · G generated explainer)

| # | Scene | Type | Source | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- | --- |
| 1 | 1 | S | `am-vial.jpg` (NASA) | the actual Bennu sample in a vial with tweezers, so "127 grams" has a size |
| 2 | 2 | S | `am-return.jpg` (NASA) | the recovery team in the Utah desert, so "two missions" are real operations |
| 3 | 2 | S | `am-sample.jpg` (NASA) | the open sample canister, so the haul is a small box, not a mine |
| 4 | 3 | S | `am-eros.jpg` (NASA/JPL) | a near-Earth asteroid, so "step one, the flight" has a target |
| 5 | 3 | S | `am-moon.jpg` (Apollo 17) | the Moon's surface, so the fuel comparison has a second end |
| 6 | 3 | S | `am-itokawa.jpg` (JAXA) | a second asteroid, so Eros is not a one-off |
| 7 | 4 | S | `am-bennu.jpg` (NASA) | Bennu as a whole, so "you could jump off it" has a body (490 m) |
| 8 | 4 | S | `am-boulders.jpg` (NASA) | the loose boulder surface, so "no solid ground" is visible |
| 9 | 4 | G | prompt G2 | the inside of a rubble pile with its gaps, so "ball pit" has a cause |
| 10 | 4 | S | `am-landing.jpg` (NASA, Oct 2020) | the real sampler on Bennu's rocks, so the sinking is not an illustration |
| 11 | 5 | G | prompt G1 | a drill pushing down and the craft pushed up, so "you push yourself up" is a diagram |
| 12 | 5 | S | `am-smelter.jpg` (Palmer, 1941) | what refining looks like on Earth (a ladle of molten iron), so "no refining in zero gravity" has a reference |
| 13 | 5 | S | `am-boulders.jpg`, other crop | the same rock field closer, so "digging" has a surface |
| 14 | 6 | S | `am-platinum.jpg` | native platinum nuggets, so the product is real |
| 15 | 6 | S | `am-platinum.jpg`, other crop | the same, closer |
| 16 | 6 | S | `am-utah.jpg` (NASA, return training) | a capsule under a parachute, so "a big load from space" is a capsule |
| 17 | 7 | S | `am-tagsam.jpg` (NASA) | scientists opening the Bennu sample, so "water locked in the rock" comes from real lab work |
| 18 | 7 | S | `am-sample.jpg`, other crop | the canister again, closer |
| 19 | 7 | S | `am-vial.jpg`, other crop | the hook image again, so the Short loops |

Mix: 17 S, 2 G. Ten of the photos are NASA or JAXA originals; the Itokawa picture is JAXA's (credit required, license to confirm). Not used: a Hayabusa2 photo (the only free one was a 3D model), a presentation photo of the capsule (a crowd).

## Prompts (P4; `gpt-image-1.5`, 2:3, medium; specifications, not scenes; no style)

Every prompt ends with: *"Plain light-grey background. No glow, no light rays, no decorative particles, no text. The image contains no letters, no numbers and no labels."* (rule 2.13)

- **G1 · reaction.** A clean technical schematic of a spacecraft body floating next to a small irregular rock, a drill on a short arm pressing its bit against the rock. One thick arrow points from the drill into the rock (the push), one thick arrow of the same length points from the spacecraft body away from the rock (the reaction). Nothing else: no ground, no gravity arrow.
- **G2 · rubble pile.** A cross-section schematic of a small roughly round asteroid cut in half: the inside is a loose heap of angular boulders of many sizes with visible empty gaps between them, about four tenths of the volume empty; the outer layer is the same heap, no solid core and no solid crust.

Each generated plate is checked for leaked text and against [[Script - Asteroid mining]]; one retry per image.

## Budget in dollars (cap = base × 1.2)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` Roger `en`, speed 0.95 | 7 takes, ≈ 930 characters | ≈ $0.10 per 1,000 characters | ≈ $0.10 | ≈ $0.12 |
| Image (generated) | `gpt-image-1.5` medium 2:3 | 2 plates | ≈ $0.05 (**unconfirmed on Replicate**) | ≈ $0.10 | ≈ $0.12 |
| Word timings | `incredibly-fast-whisper` | 7 takes | ≈ $0.01 (**unconfirmed**) | ≈ $0.07 | ≈ $0.09 |
| Image (stock) | free sources | 17 plates | $0 | $0 | — |
| Sound, background removal | none | 0 | — | $0 | — |
| **Total and cap** | | | | **≈ $0.27** | **≈ $0.33** |

## Stock credits (`Media/Asteroid-mining/stock/_credits.jsonl`)

| File | Title | Author | License | Page |
| --- | --- | --- | --- | --- |
| `am-vial.jpg` | Vial with Sample of Asteroid Bennu | NASA/GSFC | NASA media | [NASA](https://images.nasa.gov/details/Bennu_Sample2) |
| `am-return.jpg` | OSIRIS-REx Sample Return | NASA/Keegan Barber | NASA media | [NASA](https://images.nasa.gov/details/NHQ202309240020) |
| `am-sample.jpg` | OSIRIS-REx sample canister with lid open | Erika Blumenfeld and Joseph Aebersold / NASA | NASA media | [NASA](https://images.nasa.gov/details/jsc2024e023024) |
| `am-eros.jpg` | Eros - PIA02923 (color) | NASA/JPL/JHUAPL | public domain | [Commons](https://commons.wikimedia.org/wiki/File:Eros_-_PIA02923_(color).jpg) |
| `am-moon.jpg` | Astronaut Eugene Cernan beside lunar roving vehicle (Apollo 17) | NASA | NASA media | [NASA](https://images.nasa.gov/details/as17-134-20476) |
| `am-itokawa.jpg` | Itokawa | ISAS, JAXA | JAXA (**credit required, license to confirm**) | [Commons](https://commons.wikimedia.org/wiki/File:Itokawa06_hayabusa.jpg) |
| `am-bennu.jpg` | BennuAsteroid.jpg | NASA/Goddard/University of Arizona | public domain | [Commons](https://commons.wikimedia.org/wiki/File:BennuAsteroid.jpg) |
| `am-boulders.jpg` | A Region of Bennu's Northern Hemisphere Close Up | NASA/Goddard/University of Arizona | NASA media | [NASA](https://images.nasa.gov/details/2019-02-25_regolith_image_compilation) |
| `am-landing.jpg` | OSIRIS-REx landing (sampler touching Bennu) | NASA/Goddard/University of Arizona | public domain | [Commons](https://commons.wikimedia.org/wiki/File:OSIRIS-REx_landing.jpg) |
| `am-smelter.jpg` | Ladle of molten iron is poured into an open hearth furnace (1941) | Alfred T. Palmer, US OWI | public domain | [Commons](https://commons.wikimedia.org/wiki/File:Ladle_of_molten_iron_is_poured_into_an_open_hearth_furnace_for_conversion_into_steel1a35060v.jpg) |
| `am-platinum.jpg` | Platinum nuggets | Aram Dulyan | public domain | [Commons](https://commons.wikimedia.org/wiki/File:Platinum_nuggets.jpg) |
| `am-utah.jpg` | OSIRIS-REx Sample Return Training | NASA/Keegan Barber | NASA media | [NASA](https://images.nasa.gov/details/NHQ202308300001) |
| `am-tagsam.jpg` | OSIRIS Rex curation team pouring the sample from the TAGSAM | Robert Markowitz / NASA-JSC | NASA media | [NASA](https://images.nasa.gov/details/jsc2024e008542) |

Looked at all thirteen on one contact sheet: no brands or legible text except the NASA banner in the `am-return` crowd image, which was dropped; `am-return` is the two-person desert shot.

## Prediction log

`scene · category · model · status · cost · URL`
