---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v2 · FMHY pages and the audio licenses read on each site 4 Oct 2026 · image/data sources still unverified · rules applied across the vault 4 Oct 2026
tags: [research, youtube, sources, sound, images, ideas]
---

# Free resource directories (FMHY) and what the vault can use

← [[YouTube Channel]] · [[Illustration pipeline]] · [[Guidelines for new scripts]]

FMHY (fmhy.net) is a link directory, not a source: it **lists** sites and says nothing reliable about their licenses. Its piracy sections (streaming, torrenting, downloading) are out of scope for a monetized channel. Only the audio, image and educational pages matter. **Audio licenses below were read on each site on 4 Oct 2026; image and data sources were not.**

## Gaps in the vault it can fill

| Gap (where it hurts today)                                                                                                     | Candidates from FMHY                                                                                                                                                                            | Fit and caveat                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Sound** ("no blender sound", `audiogen` 16 kHz, "quality could improve and add dynamism", [[Guidelines for new scripts]] §3) | See "Audio sources" below | Real recordings replace generated 16 kHz audio at **$0**. Credit CC BY in the description, like photos. |
| **Labeled schematics for reference plates** (`input_images` in generated explainers)                                           | **Wikimedia Commons** diagrams (already wired), **Smithsonian Open Access** (CC0, has an API with a free key), **Flickr Commons**, **PhyloPic** (animal silhouettes), **NASA 3D Resources**     | Smithsonian and Flickr Commons are not in `stock_photos.py` yet; they suit history and museum objects.                    |
| **Facts bank (≥ 15 facts) and figures with source and date**                                                                   | **NIST Chemistry WebBook**, **PubChem**, **NASA Exoplanet Archive**, **UniProt**, **Our World in Data**                                                                                         | Primary data beats a blog; each gives a citable number and a date.                                                        |
| **Idea queue** ([[Idea and hook quality]])                                                                                     | **The Pudding**, **Information Is Beautiful**, **Ciechanowski's blog**, **PhET**                                                                                                                | Use to see how a mechanism is explained, then rebuild it; never copy their visuals or text.                               |

## Audio sources (licenses read on each site, 4 Oct 2026)

| Source | Type | License as stated | Credit needed | Content ID risk | Use for |
| --- | --- | --- | --- | --- | --- |
| **BigSoundBank** | effects, ambience | CC0 / public domain; commercial allowed | No (suggested "Joseph SARDIN - BigSoundBank.com") | Low | first choice: rooms, machines, nature |
| **Freesound** | effects, foley, field recordings | per file: CC0, CC BY, CC BY-NC | CC BY: yes, with title, user and URL | Its FAQ admits Content ID can flag files; dispute with the upload date | the biggest catalog; **filter to CC0** by default |
| **Sonniss GDC bundles** | effects, large packs | royalty-free, monetized video allowed, no AI/ML training | No | Low | designed hits, risers, impacts; large downloads (GB) |
| **YouTube Audio Library** | effects and music | YouTube license; tracks "won't be claimed" via Content ID for Partner Program | Only on tracks marked CC | None for YouTube | safest music; **YouTube only**, not stated for other platforms ([[Channel strategy]] multi-platform plan) |
| **Pixabay Music / SFX** | music, effects | Pixabay license: commercial, no attribution; not as standalone files | No | Not addressed on the license page; check per track | quick music beds |
| **Incompetech** (Kevin MacLeod) | music | CC BY 4.0; monetized YouTube allowed | **Yes**: "Title Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 4.0" | Known to be claimed sometimes; keep the page as proof | ambient/dark underscore |

**Decision (user, 4 Oct 2026): BigSoundBank and Freesound are kept for later**; no helper, not in the workflow. **Order of use now:** YouTube Audio Library → Sonniss → Pixabay → Incompetech. The rules live in [[Guidelines for new scripts]] §3; this note is the evidence. Credits go into `Media/<video>/sound/_credits.jsonl` like photos and into the Status attribution table.

## Examples on a real script ([[Script - Superconductors]])

These are proposals; search terms are queries to try, not files found. Rules that already hold stay: sounds sit **under** the voice (volume 0.18 to 0.22, 0.3 s in, 0.4 s out, [[Transitions and effects]]), and sound is **opt-in** because of the earlier "no blender sound" feedback.

| Scene | Sound idea | Query | What it adds | Faithful? |
| --- | --- | --- | --- | --- |
| 1 · "Not low. Zero." | Low room hum under the first line that **cuts to silence** on "Zero." | `lab hum`, `refrigeration compressor` (BigSoundBank) | The silence lands as the claim, the way the Helium video cuts its plant hum | Yes, a hum is no claim about physics |
| 4 · magnet floats | Soft airy sustain while it hovers | `ambient drone low` | Holds attention during a still plate | Yes, if kept abstract |
| 5 · "28 years" | One slow clock tick that stops after the number card appears | `clock tick single` | Makes "does not fade" felt | Yes |
| 6 · LHC tunnel | Cavernous reverb and a faint cryogenic hiss | `tunnel ambience`, `gas hiss` | A real place sounds like a place; matches the photo | Yes; do not imply the LHC sounds like this |
| 7 · diamond anvil | One creaking low pressure sound building across the line | `metal creak pressure` (Sonniss) | Turns "1.5 million atmospheres" into tension | Yes, as a mood cue |
| 8 · close | A short, clean tail on the last word, no music bed | none | Ends on voice | n/a |
| Number cards (28 years, 1.9 K, 250 K, 5 %) | A soft tick as each figure appears, same one every time | `ui tick soft` | A consistent audio cue for "this is the number" | n/a |

**Music:** still none by default. If a Short wants a bed, one ambient track at volume 0.10 to 0.12 from YouTube Audio Library or Incompetech, under the same ducking as sounds. A bed hides abrupt voice starts less than silence does, so [[Blender editing]]'s voice-padding check still applies.

**Cost of the pilot:** $0 in downloads, and a few minutes of selection per video. The agent cannot hear: the user judges at P7 and the volumes stay estimates.

## Do not use

- **BBC Sound Effects**: its RemArc license is non-commercial. Unsuitable for monetization.
- **NCS, BenSound, Free Music Archive**: terms not checked (FMA's CC page returned 404); skip until read.
- **Freesound CC BY-NC files**: non-commercial, filter them out.
- **unDraw, StorySet, Vecteezy, "free" icon packs**: generic decorative art fails the usefulness test ([[Illustration pipeline]]).
- **Game-rip sites** (The Sounds Resource, Spriters Resource): copyrighted.
- Any FMHY item from the piracy sections.

## Proposed next steps 

1. Pilot on one video: 2 to 3 sounds from Sonniss or YouTube Audio Library (manual download, license noted); add a `sound` field to `plan.json` and `build_video.py`. Judge by ear (the agent cannot hear it).
2. Later: Freesound (API key; terms not read) and BigSoundBank, plus Smithsonian Open Access for images, in `stock_photos.py` or a sibling helper.

Applied on 4 Oct 2026: rules in [[Guidelines for new scripts]] §3, [[Shorts quality bar]], [[Channel playbook]], [[Fast workflow]], [[Channel models]], [[Production process]], [[Media convention]], [[Transitions and effects]], [[Prompt - per-scene generation guide]], [[Feedback loop]], `CLAUDE.md`, and an invariant in `check_vault.py`.

## Not verified

Image/data-source licenses; Freesound API terms and key cost; Pixabay's Content ID behavior on audio; YouTube Audio Library use outside YouTube; whether any query above returns a usable sound; whether Freesound/Smithsonian keys are free today; the 404 on FMHY's `/educational-index` (the `/educational` page was used instead).
