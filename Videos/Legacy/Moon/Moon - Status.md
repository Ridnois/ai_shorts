---
type: research
created: 2026-10-04
updated: 2026-10-04
status: render r1 built, awaiting P7 · delegated by the user ("I like C, do the video", 4 Oct 2026): P4 to P6 run by the agent within the cap
tags: [research, youtube, status, moon, shorts]
---

# Moon · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]] · [[Script - Moon]] · [[The Moon is leaving us]]

Short 9:16, English, 137 words. Theme: the Moon was born about twenty times closer, and its leaving keeps stretching Earth's day. Media in `Media/Legacy/Moon/` (prefix `mn-`). **Second video built with the rules of the Superconductors feedback:** plain-words hook, one theme line with bridges, ≤ 5 facts, concrete ending, a new image every ≈ 3 to 4 s, captions at 88 px, no in-video branding, synthesized sound design.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | user chose theme and angle C ("I like C") after the mirror angle was rejected as boring | [[The Moon is leaving us]] |
| 1 Research | ✅ | agent | 19-fact bank, sources fetched 4 Oct 2026 |
| 2 Script | ✅ | agent | 137 words, 7 scenes, cut test done |
| 3 Direction | ✅ | agent | visual plan below: 18 plates, 3 generated + 1 drawn to scale |
| 4 Prompts and budget | ✅ | **delegated by the user** (4 Oct 2026), cap ≈ $0.37 | below |
| 5 Test | ⏭ folded into 6 | delegation | scene 1 voice twice (default and the expressive variant) |
| 6 Generation | ✅ | delegation | 8 voice takes, 3 plates (one diagram drawn instead of generated), 7 word-timing runs |
| 7 Editing | ⏳ **P7 is yours** | | `Media/Legacy/Moon/render/mn-55s-9x16-r1.mp4` |
| 8 Publishing | ⏳ | — | description below |

## Budget in dollars (cap = base × 1.2)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` Roger `en`, speed 0.95 | 7 takes + 1 alternative take of scene 1, ≈ 840 + 50 characters | ≈ $0.10 per 1,000 characters | ≈ $0.09 | ≈ $0.11 |
| Image (generated) | `gpt-image-1.5` medium 2:3 | 3 plates | ≈ $0.05 (**unconfirmed**) | ≈ $0.15 | ≈ $0.18 |
| Word timings | `incredibly-fast-whisper` | 8 takes | cents (measured: negligible) | ≈ $0.02 | ≈ $0.03 |
| Image (stock) and the scale diagram | free sources, drawn locally | 15 plates | $0 | $0 | — |
| Sound | synthesized by the builder | — | $0 | $0 | — |
| **Total and cap** | | | | **≈ $0.26** | **≈ $0.31** (the 0.37 above allows one retry image) |

Voice note: the default take of scene 1 goes in the video; the alternative (`stability` 0.35, `style` 0.35, a `[curious]` tag) is saved as `voice/mn-s1-voice-alt.mp3` for the user's A/B at P7 ([[Channel voice]]). The agent cannot hear either.

## Prediction log

`scene · category · model · status · cost · URL`
- Voice · `elevenlabs/v3` Roger `en` 0.95, 7 takes + 1 alternative of scene 1, 763 + 57 characters · ✅ `voice/mn-s1…s7-voice-v1.mp3`, `mn-s1-voice-alt.mp3` · ids: [prbwfp57…](https://replicate.com/p/prbwfp5785rmy0d1145snv5dd8), 88jxaqpt…, y62hdege…, znpqfdj0…, hvxpxz3r…, t0f9gnna…, ggbpzxyw…, hsr3zy0f… (alt)
- Images · `gpt-image-1.5` medium 2:3 png · ✅ `plates/mn-p01-looming-v1.png` ([z3kb48tg…](https://replicate.com/p/z3kb48tgrdrmw0d1146ryrdk3m); the poll timed out on a network error, so the prediction was **recovered, not regenerated**, and the helper's polling now survives such errors), ✅ `plates/mn-p02-impact-v1.png`, ❌ the first tidal-bulge plate (`mn-p08-bulge-v1`, generated: the bulge was not ahead of the Earth–Moon line and the Moon's arrow pointed outward, failing rule 2.13; **discarded, not retried**) replaced by a diagram drawn with exact geometry (`System/scripts/make_tide_diagram.py` → `plates/mn-p08-bulge-v2.png`, $0)
- Word timings · `incredibly-fast-whisper` word, 7 runs · ✅ `voice/*.words.json`
- Several HTTP 429s (no prediction created, no cost), retried by the helper.
- **Total: 18 predictions (8 voice, 3 images, 7 timings), ≈ $0.24 of the ≈ $0.31 cap** (voice ≈ $0.08, images ≈ $0.15 at the unconfirmed $0.05, timings negligible).

## Visual plan (S stock · G generated · D drawn to scale/geometry)

| # | Scene | Type | Source | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- | --- |
| 1 | 1 | G | `mn-p01-looming-v1` (illustration) | a Moon filling the sky over an ocean, so "twenty times closer" is a picture; card with the model figures |
| 2 | 2 | G | `mn-p02-impact-v1` (artist's impression) | a molten Earth, a debris ring and a clump, so "the debris gathered into the Moon" has a shape |
| 3 | 2 | S | `mn-mars-disc` (Hubble, public domain; cropped from a four-planet frame to remove its labels) | a Mars-sized body, so "Mars-sized" is concrete |
| 4 | 3 | S | `mn-moon-sea` (CC BY-SA 2.0) | the Moon as we see it today, tiny in the sky, for the comparison |
| 5 | 3 | S | `mn-supermoon` (NASA/Bill Ingalls) | a large Moon at the horizon, the nearest everyday thing to "filling the sky" |
| 6 | 3 | S | `mn-tide-in` (CC BY 2.0) | a harbour at high tide, so "pulled the oceans" is a tide |
| 7 | 4 | S | `mn-tide-out` (CC BY 2.0) | the same dock at low tide, so tides are the difference |
| 8 | 4 | D | `mn-p08-bulge-v2` | the ocean bulge carried ahead of the Moon, pulling it forward (callouts name every part) |
| 9 | 4 | S | `mn-earth-a17` (NASA Apollo 17) | the spinning Earth, for "Earth spins faster than the Moon orbits" |
| 10 | 5 | S | `mn-coral1` (CC BY 2.0), `contain` | a Devonian fossil coral, a real fossil from the record that shows longer-ago days; card: 22 hours |
| 11 | 5 | S | `mn-startrails` (NASA, Don Pettit) | a day as a trail of stars, so "day length" is something you can see |
| 12 | 5 | S | `mn-coral1`, `full` crop | the fossil's texture up close |
| 13 | 6 | S | `mn-reflector` (NASA Apollo 14) | the reflector with which the distance is measured |
| 14 | 6 | S | `mn-craters` (NASA Artemis II) | the Moon's edge, with the card 3.8 cm a year |
| 15 | 6 | S | `mn-galileo` (NASA), `contain` | Earth and Moon far apart, with the card 1.7 ms per century |
| 16 | 7 | S | `mn-earthset` (NASA Artemis II) | Earth over the lunar horizon |
| 17 | 7 | S | `mn-earth-a17`, crop | the Earth that has the 24-hour day |
| 18 | 7 | S | `mn-moon-sea`, crop | the Moon itself, leaving, to close the video |

Mix: 14 S, 2 G, 1 D, plus 2 reused photos (same photo, different crop); 18 plates in ≈ 55 s (2.4 to 3.8 s each, none over 5 s).

## Stock credits (`Media/Legacy/Moon/stock/_credits.jsonl`)

| File | Title | Author | License | Page |
| --- | --- | --- | --- | --- |
| `mn-reflector.jpg` | Laser Ranging Retro Reflector deployed by Apollo 14 | NASA/JSC | NASA media (public domain) | [as14-67-09386](https://images.nasa.gov/details/as14-67-09386) |
| `mn-earth-a17.jpg` | View of the Earth, Apollo 17 | NASA/JSC | NASA media | [as17-148-22727](https://images.nasa.gov/details/as17-148-22727) |
| `mn-earthset.jpg` | A Breathtaking Earthset from Orion | NASA | NASA media | [art002e021278](https://images.nasa.gov/details/art002e021278) |
| `mn-startrails.jpg` | ISS-30 Star trail composite | Don Pettit, NASA | NASA media | [jsc2012e051505_alt](https://images.nasa.gov/details/jsc2012e051505_alt) |
| `mn-supermoon.jpg` | Supermoon | NASA/Bill Ingalls | NASA media | [NHQ201712030001](https://images.nasa.gov/details/NHQ201712030001) |
| `mn-galileo.jpg` | Galileo view of Moon orbiting the Earth | NASA/JSC | NASA media | [S92-52043](https://images.nasa.gov/details/S92-52043) |
| `mn-craters.jpg` | Birkhoff Crater in Low-Light Detail | NASA | NASA media | [art002e012723](https://images.nasa.gov/details/art002e012723) |
| `mn-mars.jpg` (and `mn-mars-disc.jpg`) | Hubble Mars During 1999 | Steve Lee (Univ. of Colorado) et al., NASA/STScI | public domain | [Commons](https://commons.wikimedia.org/wiki/File:Hubble_Mars_During_1999.jpg) |
| `mn-tide-in.jpg` / `mn-tide-out.jpg` | Bay of Fundy, Tide In / Tide Out | Dylan Kereluk | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Bay_of_Fundy_-_Tide_In.jpg), [Tide Out](https://commons.wikimedia.org/wiki/File:Bay_of_Fundy_-_Tide_Out.jpg) |
| `mn-coral1.jpg` | Hexagonaria sp. (fossil coral), Devonian, Missouri | James St. John | CC BY 2.0 | [Commons](https://commons.wikimedia.org/wiki/Category:Hexagonaria) |
| `mn-moon-sea.jpg` | Full Moon rising over Brisbane River | Sheba_Also | CC BY-SA 2.0 | [Commons](https://commons.wikimedia.org/wiki/File:Full_Moon_rising_over_Brisbane_River-1_(14633318102).jpg) |

Looked at all 13: no legible text or brand (the four-planet Mars frame had labels: cropped to one disc). The Bay of Fundy photos show boat names too small to read.

## Editing (render r1)

`Media/Legacy/Moon/plan.json` → `System/scripts/build_video.py`: **55.1 s** (derived: 137 words ≈ 149 wpm with pauses), 1080×1920, 24 fps, 18 plates `[3.3, 3.8, 3.8, 2.4, 2.4, 2.4, 3.4 ×3, 3.0 ×3, 3.1 ×3, 2.7 ×3]`, `LONG PLATE: none`, `CHECK RESULT all voices complete`, `CAPTIONS 137 words, timed by whisper`, synthesized sound design (`sfx` peak 0.150, `bed` peak 0.024), captions 88 px, keywords in copper (twenty, closer, tides, tug, spin, day, leaving), no branding.

- **Looked at (stills at 19 times, 1.5 to 54 s):** cards and callouts sit on real images or faithful diagrams, captions readable, no leaked text, no overlaps. Fixes after the first build: the impact plate's focus, the reflector callout (the card moved to the next plate so it no longer hides the reflector).
- **Opener:** "Our newborn Moon was about twenty times closer." (8 words, plain).
- **Not verified:** the voice (not heard) and **the A/B of scene 1**: the default take is in the video; compare it with `voice/mn-s1-voice-alt.mp3` and tell the agent which wins; whether the image rhythm feels right; the sound mix.
- **Known simplifications and doubts:** "twenty times" is the model start (≈ 16,200 km vs 385,000 km, ratio ≈ 24), the looming Moon is an illustration (its size on screen is not exactly 20×); the 22 h day is the 620-million-year estimate (21.9 ± 0.4 h) from a secondary source, while the photographed fossil is a Devonian coral (≈ 380 million years old, a different time): the card names the 620-million-year figure and the callout names the coral separately; the impact plate is an artist's impression. **Check the primary papers before publishing.**

## Description draft (stage 8)

The Moon was born about twenty times closer than it is today, and its slow retreat keeps lengthening Earth's day. Sources: Wikipedia articles *Giant-impact hypothesis*, *Moon*, *Orbit of the Moon*, *Tidal acceleration*, *Lunar distance*; NASA, *Moon formation*; to be confirmed against primary papers. Photos: NASA (public domain), Hubble Mars (public domain), Dylan Kereluk (CC BY 2.0), James St. John (CC BY 2.0), Sheba_Also (CC BY-SA 2.0), via Wikimedia Commons and NASA. The looming Moon and the impact scene are AI-generated illustrations (gpt-image-1.5); the tide diagram is drawn to scale of geometry, not of size; voice generated with AI (ElevenLabs v3); sound design synthesized in Blender. Data as of 4 Oct 2026.
