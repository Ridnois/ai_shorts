---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v1 · brief · pages read 4 Oct 2026 (fmhy.net/, /audio, /image-tools, /educational); licenses NOT verified per source
tags: [research, youtube, sources, sound, images, ideas]
---

# Free resource directories (FMHY) and what the vault can use

← [[YouTube Channel]] · [[Illustration pipeline]] · [[Guidelines for new scripts]]

FMHY (fmhy.net) is a link directory, not a source: it **lists** sites and says nothing reliable about their licenses. Its piracy sections (streaming, torrenting, downloading) are out of scope for a monetized channel. Only the audio, image and educational pages matter. **Every source below needs its license read on its own site before first use.**

## Gaps in the vault it can fill

| Gap (where it hurts today)                                                                                                     | Candidates from FMHY                                                                                                                                                                            | Fit and caveat                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Sound** ("no blender sound", `audiogen` 16 kHz, "quality could improve and add dynamism", [[Guidelines for new scripts]] §3) | **Freesound** (per-file CC0/CC BY; API needs a free key), **BigSoundBank**, **Sonniss GDC game audio** (royalty-free packs), **YouTube Audio Library** (cleared for YouTube), **Pixabay Music** | Real recordings at 44.1 kHz would replace generated 16 kHz audio at **$0**. Credit CC BY in the description, like photos. |
| **Labeled schematics for reference plates** (`input_images` in generated explainers)                                           | **Wikimedia Commons** diagrams (already wired), **Smithsonian Open Access** (CC0, has an API with a free key), **Flickr Commons**, **PhyloPic** (animal silhouettes), **NASA 3D Resources**     | Smithsonian and Flickr Commons are not in `stock_photos.py` yet; they suit history and museum objects.                    |
| **Facts bank (≥ 15 facts) and figures with source and date**                                                                   | **NIST Chemistry WebBook**, **PubChem**, **NASA Exoplanet Archive**, **UniProt**, **Our World in Data**                                                                                         | Primary data beats a blog; each gives a citable number and a date.                                                        |
| **Idea queue** ([[Idea and hook quality]])                                                                                     | **The Pudding**, **Information Is Beautiful**, **Ciechanowski's blog**, **PhET**                                                                                                                | Use to see how a mechanism is explained, then rebuild it; never copy their visuals or text.                               |

## Do not use

- **BBC Sound Effects**: its RemArc license is non-commercial. Unsuitable for monetization.
- **NCS, BenSound, Incompetech and similar**: music is off by default ([[Transitions and effects]]), and several need attribution or have per-track terms.
- **unDraw, StorySet, Vecteezy, "free" icon packs**: generic decorative art fails the usefulness test ([[Illustration pipeline]]).
- **Game-rip sites** (The Sounds Resource, Spriters Resource): copyrighted.
- Any FMHY item from the piracy sections.

## Proposed next steps (need approval; nothing applied yet)

1. Add Freesound (API key) and Smithsonian Open Access to `stock_photos.py`, or a sibling `sound_search.py`, with the same `_credits.jsonl` log. Needs the user's free keys.
2. Pilot on one video: replace `audiogen` with 2 to 3 Freesound CC0 sounds; judge by ear (the agent cannot hear it).
3. If the pilot works: add the sources to [[Illustration pipeline]] §5, replace the "Sound" lines in [[Guidelines for new scripts]] §3, and add an invariant to `check_vault.py`.

## Not verified

Per-site licenses and API terms; whether Freesound/Smithsonian keys are free today; the 404 on FMHY's `/educational-index` (the `/educational` page was used instead).
