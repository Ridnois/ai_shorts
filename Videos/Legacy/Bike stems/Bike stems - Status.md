---
type: research
created: 2026-10-03
updated: 2026-10-03
status: render r2 done (63.4 s) · awaiting P7 · generation delegated and complete · narrated in Spanish
tags: [research, youtube, status, stems, shorts]
---

# Bike stems · status

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]]

Fifth video of the channel, **third vertical Short (9:16)**, requested at 40 s and **extended to 60 s** (3 Oct 2026). Made with [[Fast workflow]] and [[Guidelines for new scripts]]. Media in `Media/Legacy/Potencias - 60 segundos/`. **Narration and on-screen text are in Spanish** (made before the English-only decision of 3 Oct 2026; "potencia" is Spanish for "stem"); quoted on-screen strings below are translations.

> **Request (3 Oct 2026):** "the history of *bike tees* in 40 seconds, from the oldest designs to the modern ones; show the evolution of the handlebar and, in each evolution, the fitting, the measurements and the improvements over the previous generation".

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | **3 Oct 2026** · "Correct, it is about stems, potencias, tees" | "Tees" = stems. Question: how did it change and what did each generation gain and lose? |
| 1 Research | ✅ P2 | 3 Oct 2026 · implicit on asking to move to the next stage | [[Research - Bike stems]]: 24 claims and a map of 10 mount types; **no dated source before 1946** (the script starts at the quill stem) |
| 2 Script | ✅ P3 | 3 Oct 2026 · "make it 60 seconds" | [[Script - Bike stems (40 seconds)]] (v2, **60 s**): 159 words, 5 scenes |
| 3 Direction | ✅ P4a | 3 Oct 2026 · "the 8 sheets" | 8 plates, below |
| 4 Prompts and budget | ✅ P4 | **3 Oct 2026** · "i approve the budget" | ≈ $0.23 with cap ≈ $0.28 |
| 5 Tests | ⏭️ skipped | 3 Oct 2026 · "skip image test, go direct with the illustrations for the render" | The voice was not tested separately either: all 5 takes were generated |
| 6 Generation | ✅ P6 | 3 Oct 2026 · **delegated** up to the render | 5 voices and 8 plates (9 image predictions). See *Generation and editing* |
| 7 Editing | ✅ render r2 · ⏳ P7 | ⏳ | `render/potencias-60s-9x16-r2.mp4`, **63.38 s**, 1080×1920 |
| 8 Publishing | ⏳ not started | — | Title, description with sources and AI disclosure are missing |

## Direction (vertical 9:16 · 1080×1920)

Rules from [[Guidelines for new scripts]] §2: **one large plate per image showing the mechanism**, no text, figures or faces inside the drawing; focus between 15 and 60 % of the height; copper-orange accent on what changed. Figures go on screen ([[On-screen text style]]).

| # | Scene | What the plate explains | Accent |
| --- | --- | --- | --- |
| 1 | 1 Hook (0–5 s) | **Where the stem is**: side view of a bike's front end, with the stem joining fork and handlebar | The stem |
| 2 | 2 Quill (5–14 s) | **Two quill-stem cutaways, side by side**: on the left with a wedge and on the right with an expander cone, a long bolt in both | The wedge and the cone |
| 3 | 2 Quill | **Raising the handlebar**: bolt loosened, stem rising up the fork, with the minimum-insertion mark | The rising arrow |
| 4 | 3 Threadless (14–23 s) | **Exploded view of the Aheadset**: fork, spacers, stem clamping on the outside, cap and bolt | The outer clamp |
| 5 | 3 Threadless | **Height with spacers**: two fronts side by side, one with spacers under the stem and another above it | The spacers |
| 6 | 4 Measures (23–32 s) | **Clamp diameter**: three handlebar centres in a row, each thicker, with the stem's face plate | The thickest |
| 7 | 4 Measures | **Length moves the handlebar**: two silhouettes of a bike front end, long stem and short stem, with a reach arrow | The short stem |
| 8 | 5 Close (32–40 s) | **Integrated piece**: carbon handlebar and stem in one piece, with a cut showing the cables inside | The junction |

**On-screen text (in editing):** sc. 2 `Quill stem` and `Cinelli 1A · 26.4 mm clamp` · sc. 3 `1990 · Aheadset` · sc. 4 `25.4 → 31.8 mm` and `100+ → 35–60 mm` · sc. 5 `Integrated`.
**Sound:** none (default rule). **Editing:** `build_queque.py` as the base, 1080×1920, one plate every ≈ 4 s, "page turn" between scenes.

## Prompts (P4, approved)

**Model:** `wan-video/wan-2.7-image`, `size` `1152*2048`, `num_outputs` 1, **3 references** from the technical-sketch reference library (withdrawn): `ref-explosionada-colt`, `ref-explosionada-bloques` and `ref-corte-recipiente-color` (in #7, `ref-patente-mecanismo-flujo` instead of the last one).

**Template of each prompt:** *"Use the references only as a guide to technique (line, hatching, cutaway, arrows); do not copy their objects, labels or text."* + **context** + **subject** + **composition** + **accent** + style block.

**Common context (pasted at the start of all):** *This sheet belongs to a 40-second explainer on how the bicycle stem, the part joining the fork to the handlebar, evolved from the quill stem to the threadless Aheadset, to larger handlebar clamps, shorter stems and integrated cockpits. Every sheet explains one mechanism.*

**Real-object sheets** (checked against the research sources; look at a real photo before P5):
- **Quill stem:** a vertical shaft that enters the fork, an extension that comes out forward at an angle and ends in a round clamp for the handlebar; a long bolt crosses the shaft from the top to a wedge or cone at the lower tip.
- **Aheadset:** the fork protrudes above the bearing; on it go spacer rings, then the stem with a side clamp of two bolts around the fork and a four-bolt front plate for the handlebar, and on top a cap with a single central bolt.
- **Handlebar:** the centre is the thickest zone; it widens compared with the ends.

| # | Subject, composition and accent (in English, before the style block) |
| --- | --- |
| 1 | One single large drawing filling the sheet: a side view of the front end of a bicycle showing the head tube, the fork, a short stem and a flat handlebar, with a long arrow pointing along the stem from the fork to the handlebar. The stem is the copper-orange accent. |
| 2 | One single large drawing filling the sheet: two vertical cutaways of a quill stem inside a fork steerer tube, side by side; the left one with a long bolt pulling a diagonal wedge at the bottom of the shaft, the right one with a long bolt pulling a conical expander; short arrows on each show it pushing outward against the tube wall; exactly two cutaways. The wedge and the cone are the copper-orange accent. |
| 3 | One single large drawing filling the sheet: a loosened quill stem rising out of the steerer tube with a tall upward arrow, a thin horizontal line on the shaft marking the minimum insertion, and the handlebar raised with it. The upward arrow is the copper-orange accent. |
| 4 | One single large drawing filling the sheet: an exploded vertical view of a threadless stem assembly, from the bottom up: the fork steerer sticking out of the headset, three thin spacer rings, a stem clamping around the outside of the steerer with two side bolts, a top cap with one central bolt; dashed alignment lines between the parts. The outer clamp of the stem is the copper-orange accent. |
| 5 | One single large drawing filling the sheet: two fronts of a bicycle side by side, on the left three spacer rings below the stem and the handlebar high, on the right the same three spacer rings above the stem and the handlebar low, with a double-headed vertical arrow between them. The spacer rings are the copper-orange accent. |
| 6 | One single large drawing filling the sheet: three handlebar centre sections in a row, each thicker than the previous, each with its stem face plate and four bolts around it, and a thin dimension line across each; exactly three bars, no more. The thickest bar is the copper-orange accent. |
| 7 | One single large drawing filling the sheet: two side silhouettes of a bicycle front end stacked vertically, the upper with a long stem and the handlebar far forward, the lower with a short stem and the handlebar closer to the rider, with a horizontal arrow between the head tube and the handlebar on each. The short stem is the copper-orange accent. |
| 8 | One single large drawing filling the sheet: a one-piece carbon road handlebar and stem seen from above and slightly from the front, a cutaway along the stem showing two thin cables routed inside it, thin leader lines ending in small arrowheads. The junction between bar and stem is the copper-orange accent. |

**Style block (v3 of the technical-sketch visual style (withdrawn), pasted at the end):**

```
Hand-drawn industrial design concept sketch on warm off-white paper, vertical sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat marker colour in cool greys with natural metal and rubber tones where the object needs them, and a single copper-orange marker accent on the one element that matters. Technical-drawing language made of straight lines, thin leader lines ending in small arrowheads, blank dimension lines, cutaway views and angular shapes. Real, recognisable bicycle parts drawn accurately. Clean paper around the subject.
```

**Voice:** `elevenlabs/v3`, voice `Roger`, `language_code: es`, `speed` 0.95 (raised to ≈ 1.05 only if P5 allows), 5 takes, one per scene, with the script's exact text. The *API* tab's schema is copied before calling.

## Budget in dollars (cap = base × 1.2)

| Category | Model | Base quantity | Unit price | Subtotal | Cap |
| --- | --- | --- | --- | --- | --- |
| Image | `wan-2.7-image` | **8** (each with its second in the direction table) | ≈ $0.02 (**unconfirmed on Replicate**) | **≈ $0.16** | 9 images (≈ $0.18) |
| Voice | `elevenlabs/v3` | 5 takes (≈ 640 characters) | ≈ $0.10 per 1,000 characters | **≈ $0.07** | 6 predictions (≈ $0.08) |
| Sound | — | 0 | — | $0 | — |
| **Total** | | | | **≈ $0.23** | **≈ $0.28** |

- **P5 test (inside the total, later skipped):** voice of scene 1 (≈ $0.02) + image #4, the hardest for having more parts (≈ $0.02): **≈ $0.04**.
- Retries: **one per image**, only if the prompt changes; the ones most prone to fail by counting are **#6** (three handlebars) and **#5** (three spacers on each side).
- No thumbnail (Short).
- For comparison: Brazil ≈ $0.46 (7 images), Lemon cake ≈ $1.57 (20 plates).

## Generation and editing (3 Oct 2026)

**Changes over what was approved:** the script went to 60 s (159 words); the 8 plates and prompts are those above, with the context of each scene's narration and 3 references from the external library. Plate #2 asks for "two cutaways" (wedge and cone).

| Category | Predictions | Cost (estimated) |
| --- | --- | --- |
| Voice | 5 (`elevenlabs/v3`, 843 characters) | ≈ $0.08 |
| Image | **9** (8 plates + 1 retry of #5) = cap | ≈ $0.18 (`wan-2.7-image`, **price unconfirmed on Replicate**) |
| Sound | 0 | $0 |
| **Total** | **14** | **≈ $0.26**; approved cap ≈ $0.28 |

**The image cap (9 of 9) was reached.** No retries are left without approval.

| Scene | Category | Model | Status | Prediction |
| --- | --- | --- | --- | --- |
| 1 | voice | `elevenlabs/v3` | ✅ | [ta80qxe46srmr0d10dks711kcm](https://replicate.com/p/ta80qxe46srmr0d10dks711kcm) |
| 2 | voice | `elevenlabs/v3` | ✅ | [9erj836mz1rmw0d10dkv4mpkww](https://replicate.com/p/9erj836mz1rmw0d10dkv4mpkww) |
| 3 | voice | `elevenlabs/v3` | ✅ | [bxt5zcqcqxrmr0d10dkrzvvyhc](https://replicate.com/p/bxt5zcqcqxrmr0d10dkrzvvyhc) |
| 4 | voice | `elevenlabs/v3` | ✅ | [re77q486e1rmt0d10dmbh1za6c](https://replicate.com/p/re77q486e1rmt0d10dmbh1za6c) |
| 5 | voice | `elevenlabs/v3` | ✅ | [d1sc27ry21rmy0d10dm8amhvvr](https://replicate.com/p/d1sc27ry21rmy0d10dm8amhvvr) |
| 1 | image #1 | `wan-2.7-image` | ✅ | [rpb64wek49rmy0d10dmbefy4v4](https://replicate.com/p/rpb64wek49rmy0d10dmbefy4v4) |
| 2 | image #2 | `wan-2.7-image` | ✅ | [c846gcrx0nrmt0d10dmte8h6d4](https://replicate.com/p/c846gcrx0nrmt0d10dmte8h6d4) |
| 2 | image #3 | `wan-2.7-image` | ✅ | [2mr53vk8d5rmr0d10dmvn9shdw](https://replicate.com/p/2mr53vk8d5rmr0d10dmvn9shdw) |
| 3 | image #4 | `wan-2.7-image` | ✅ | [nfh6xnnhk1rmt0d10dmvvfhw1g](https://replicate.com/p/nfh6xnnhk1rmt0d10dmvvfhw1g) |
| 3 | image #5 v1 | `wan-2.7-image` | ❌ discarded (both fronts came out identical) | [yenrz99r15rmt0d10dn8ffe06w](https://replicate.com/p/yenrz99r15rmt0d10dn8ffe06w) |
| 3 | image #5 v2 | `wan-2.7-image` | ✅ | [ds7zb4r771rmt0d10dpaw9vfk0](https://replicate.com/p/ds7zb4r771rmt0d10dpaw9vfk0) |
| 4 | image #6 | `wan-2.7-image` | ✅ | [nmrbyech0nrmy0d10dnah4nwq8](https://replicate.com/p/nmrbyech0nrmy0d10dnah4nwq8) |
| 4 | image #7 | `wan-2.7-image` | ✅ | [809d2xz35hrmw0d10dn8j7q3yr](https://replicate.com/p/809d2xz35hrmw0d10dn8j7q3yr) |
| 5 | image #8 | `wan-2.7-image` | ✅ | [83gxeqtczhrmy0d10dntb4mbhm](https://replicate.com/p/83gxeqtczhrmy0d10dntb4mbhm) |

**Render r2:** `render/potencias-60s-9x16-r2.mp4`, **63.38 s**, 1080×1920, 24 fps. Script: `System/scripts/build_potencias.py` (based on `build_queque.py`). The useful voice adds up to ≈ 59 s; the rest are 0.35 s silences between scenes, 0.7 s before the close, 0.3 s of intro and 0.8 s of tail. Sentences are not cut (each strip covers its voice plus 0.25 s). Plates: 1, 2, 2, 2 and 1 per scene, with cross-fade and "page turn"; one label card per scene ([[On-screen text style]]); no sound or music. r1 was discarded: the arrow "→" does not exist in the typeface and came out as a box; now "·" is used.

### What I checked and what I did not

- ✅ Duration and tracks of the render; five key frames (plates, legible cards, no broken glyphs after the fix; the one for scene 4 I changed without looking again).
- ❌ **I did not hear the audio or watch the whole video:** timbre, pace, and whether the card covers anything.
- **Plates, looking at the eight together:** #1, #2, #3 and #7 explain well. **#4:** the exploded view looks more like a hub than a stem, with little numbers "(1) (2) (3)" inside the drawing. **#5 (v2):** the height difference shows; the position of the rings is doubtful. **#6:** the three clamps float with lots of empty paper and carry their dimensions written (`25.4mm`, `31.8mm`, `35mm`, correct). **#8:** has a frame.
- **Rigor:** "veinticinco" in the voice is 25.4 mm; "according to the brands" in the close. Still no source before 1946.

### What awaits your decision (P7)

1. **Watch and listen** to the mp4: pace and voice OK? Do plate changes land where they should?
2. Do I redo **#4** (exploded view) and **#6** (clamps)? We already reached the cap of 9 images: ≈ $0.02 each, it must be approved.
3. Are the 63 s fine, or do I trim ≈ 3 s of silences?
4. To publish (P8): title, description with sources (the ones in [[Research - Bike stems]]) and AI disclosure.
