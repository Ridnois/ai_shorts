---
type: research
created: 2026-10-04
updated: 2026-10-04
status: stages 0–3 done (user: "idea gate is good and scripting going well, continue") · stock downloaded · P4 approved by the user 4 Oct 2026 (prompts + budget, cap ≈ $0.29) · P5 test done, awaiting the user's ear
tags: [research, youtube, status, magnetar, neutron-star, shorts]
---

# Magnetar · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]] · [[Script - Magnetar]]

Short 9:16, English, 151 words. Question: *how can a star the size of a city be heard across the galaxy?* Media in `Media/Magnetar/` (files prefixed `mg-`).

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | user, 4 Oct 2026 | Thread: the 2004 SGR 1806-20 starquake. Alternative kept: SGR 1935+2154 and fast radio bursts (2020) |
| 1 Research | ✅ P2 | user | Sources in [[Script - Magnetar]]; NASA/JPL numbers replaced the Wikipedia ones |
| 2 Script | ✅ P3 | user | 151 words, 7 scenes |
| 3 Direction | ✅ P4a | pending glance | Visual plan below: 11 plates, 3 generated |
| 4 Prompts and budget | ✅ P4 | user: "I approve" (4 Oct 2026), cap ≈ $0.29 | below |
| 5 Test | ⏳ **P5** | **awaiting you** | scene-1 voice + plate 2 done; listen and look, then say go |
| 6 Generation, 7 Editing, 8 Publishing | ⏳ | — | not started |

## Visual plan (type: S stock · G generated explainer · N number plate built in Blender)

| # | Scene | Type | Source | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- | --- |
| 1 | 1 | S | `mg-magnetar-concept.jpg` (NASA/JPL) | a magnetar wrapped in field lines, so they know what "the star" is |
| 2 | 1 | G | prompt G1 | a 20 km sphere over a city street grid, so "the size of a city" is literal |
| 3 | 2 | N | built | **4 billion tons** per teaspoon (NASA/JPL), so the density is a number, not an adjective |
| 4 | 3 | S | `mg-sun-sdo.jpg` (NASA/SDO) | an ordinary star's surface, as the baseline for the field comparison |
| 5 | 3 | N | built | **≈ 1 trillion × Earth's field · 100 million × lab magnets** (NASA/JPL) |
| 6 | 4 | G | prompt G2 | field lines twisting inside, a thin solid crust cracking, so "starquake" has a cause |
| 7 | 5 | N | built | **0.1 s = 100,000 years of Sun** (Astronomy, Sept 2015; check vs arXiv) |
| 8 | 5 | G | prompt G3 | a burst expanding from a tiny star to a tiny Earth, so the scale of the trip is visible |
| 9 | 6 | S | `mg-earth-moon.jpg` (NASA/JPL) | Earth, the receiver; callout names "satellites" and "0.2 s" |
| 10 | 7 | N | built over `mg-milky-way.jpg` | **50,000 years** of travel, so the close lands on the scale |
| 11 | 7 | S | `mg-magnetar-concept.jpg` (reuse) | the thread returns to the object from the hook |

Mix: 5 S, 3 G, 3 N; no two consecutive plates of the same type. Not used as a plate: NASA's *Different Neutron Star Types* infographic (`mg-neutron-star-types.jpg`) carries text and a logo (rule 2.10); it is the **source** for scenes 2 and 3.

## Prompts (P4; `gpt-image-1.5`, 2:3, medium; paraphrased, never the narration)

- **G1 · scale.** A top-down aerial view of a dense city street grid with a large perfect sphere resting over it, the sphere's diameter spanning the whole city from edge to edge. The sphere has a pale cracked surface and faint glowing blue arcs leaving it near its two poles. Flat, clear, diagram-like framing. The image contains no letters, no numbers and no labels.
- **G2 · starquake cutaway.** A cross-section cutaway of a neutron star: a thin pale solid crust on the outside, a dense fluid interior below it, thick blue magnetic field lines twisted into coils inside, pressing outward against the crust; at one spot the crust has a clean crack with bright light escaping. Schematic, symmetrical, readable. The image contains no letters, no numbers and no labels.
- **G3 · burst crossing space.** A schematic of a very small bright star at the left edge emitting a thin expanding spherical shell of light across a dark empty field toward a tiny blue Earth at the right edge; the shell widens along the way and nothing else is between them. The image contains no letters, no numbers and no labels.

Each generated plate is checked for leaked text and against the facts; one retry per image (rule 2.7).

## Budget in dollars (cap = base × 1.2)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` Roger `en`, speed 0.95 | 7 takes, ≈ 850 characters | ≈ $0.10 per 1,000 characters | ≈ $0.09 | ≈ $0.11 |
| Image (generated) | `gpt-image-1.5` | 3 plates | ≈ $0.05 (**unconfirmed on Replicate**) | ≈ $0.15 | ≈ $0.18 |
| Image (stock) | free sources | 5 plates | $0 | $0 | — |
| Background removal, sound | none | 0 | — | $0 | — |
| P5 test | scene-1 voice + G1 | inside the totals | | | |
| **Total and cap** | | | | **≈ $0.24** | **≈ $0.29** |

Estimated duration (derived, not planned): 151 words ≈ 63 s at ≈ 144 wpm.

## Stock credits (`Media/Magnetar/stock/_credits.jsonl`)

| File | Title | Author | License | Page |
| --- | --- | --- | --- | --- |
| `mg-magnetar-concept.jpg` | A Magnetar Loses Mass (Artist's Concept) | NASA/JPL-Caltech | NASA media (public domain) | [PIA26274](https://images.nasa.gov/details/PIA26274) |
| `mg-sun-sdo.jpg` | Image of Sun From NASA's Solar Dynamics Observatory | NASA/SDO | NASA media (public domain) | [PIA26681](https://images.nasa.gov/details/PIA26681) |
| `mg-earth-moon.jpg` | The Earth & Moon | NASA/JPL | NASA media (public domain) | [PIA00342](https://images.nasa.gov/details/PIA00342) |
| `mg-milky-way.jpg` | View of Milky Way Galaxy from Earth | Image Catalog (Flickr) | CC0 1.0 | Flickr; **page URL not recorded, fill it in** |

## Not verified

- I looked at two of the five stock files (the magnetar concept and the neutron-star infographic), not the Sun, Earth–Moon or Milky Way files: check them for text and brands before P5.
- The "0.1 s = 100,000 years of Sun" figure still has one secondary source; confirm in arXiv astro-ph/0609595 before it goes on a card.
- `gpt-image-1.5` price on Replicate is unconfirmed; the cap assumes $0.05.
- Gate P7 (the full video, the voice) stays with you.

## Prediction log

`scene · category · model · status · cost · URL`

- s1 · voice · `elevenlabs/v3` Roger `en` 0.95 (`next_text` = scene 2) · ✅ `voice/mg-s1-voice-v1.mp3` · 99 characters ≈ $0.01 · [bv2wqj01…](https://replicate.com/p/bv2wqj017nrmt0d10zmrydab5r)
- p2 · image G1 · `gpt-image-1.5` medium 2:3 png · ✅ `plates/mg-p02-scale-v1.png` · ≈ $0.05 · [g9dqjvvc…](https://replicate.com/p/g9dqjvvcw9rmw0d10zms7avx58)
- One HTTP 429 on the first image call (rate limit, no prediction created, no cost); retried once after 15 s.
- Used so far: 2 predictions, ≈ $0.06 of the ≈ $0.29 cap.

## P5 result

- **Plate 2:** I looked at it. No letters, no numbers, no labels; a pale cracked sphere with blue arcs at its poles spans the city grid. It reads as "a sphere the size of a city". The sphere is perfectly smooth and the grid is photoreal, so the blue arcs are decorative rather than field lines; fine for scale, not a data claim.
- **Voice:** generated but **not heard** (I cannot hear audio). 99 characters returned a 120 KB file. The voice is your decision at P5 and is not changed afterwards.
- Next, if you say go: voice scenes 2 to 7, then plates G2 and G3, in series (≈ $0.23 more), then the Blender build with `CHECK=1`.
