---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · three-line card, one per plate, context-specific text (3 Oct 2026) · designed for vertical 9:16 Shorts; English-only
tags: [research, youtube, style, typography, text]
---

# On-screen text style

← [[Visual style - plasticine miniatures]] · [[Blender editing]] · [[YouTube Channel]]

> **Commission (3 Oct 2026):** *"Design a style for text, it must be sober, professional and modern."*

**Principle:** the text is a **sober label**, not a subtitle or a headline. It says little, is read at a glance and does not compete with the image. It is a paper card, ink and the same copper-orange accent as the illustrations ([[Visual style - plasticine miniatures]]).

## Piece: label card (*lower third*)

**v2 (3 Oct 2026, user feedback on the Helium video: "a more useful and descriptive, context-related text"):** one card **per plate** (not per scene), left-aligned, with **three lines**: a small label that says *what we are looking at or which point of the story this is*, a title that states the **fact or the claim of that moment**, and a short detail line with the **context, figure or source** that backs it. v1 (two lines, one card per scene) was used up to the Chips video.

| Element | Specification |
| --- | --- |
| **Label** (line 1) | Capitals with wide spacing (hair spaces U+200A between letters), **Noto Sans Regular, 34 px**, copper `#C76B38`. Examples: `S T E P  1`, `6  S T E P S` |
| **Detail** (line 3, v2) | **Noto Sans Regular, 34 px**, dark grey ink `#4D4741`, sentence case, a single line, **max. 40 characters**: the context, the figure with its unit, or the source/attribution ("Philips' own figure", "US 43 % · Qatar 33 % · Russia 9.5 %") |
| **Title** (line 2) | **Noto Sans Display Bold, 58 px**, ink `#1C1A17`, **sentence case** (only the first letter capitalised), a single line, **max. 26 characters** |
| **Card** | Warm paper `#F9F6EE` at 94 % opacity, 16 px corners, 1 px graphite border at 25 %, **8 px copper bar on the left edge**. Width 894 px (56 px left margin and 130 px on the right, where Shorts puts its buttons), height ≈ 210 px (v1) or ≈ 280 px (v2, three lines) |
| **Position** | Between 22 % and 33 % of the height from the bottom (v2: card centred at 28.5 %, so it spans ≈ 21.5–35.5 %): **above the Shorts caption and button zone**; the top 6 % stays free |
| **Appears / leaves** | 0.25 s fade with a 24 px rise; leaves with a 0.2 s fade. Enters 0.5 s after the scene starts and leaves 0.15 s before it ends |
| **One at a time** | Never two cards or text over text |

## Writing rules

**v2 rule of thumb:** the card must add something the voice does not say (a number, a place, a source, a caveat), and it must match what is on screen at that moment; two plates in one scene get two different cards. Do not repeat the narration.

1. **Maximum four content words**; if the title does not fit on one line, shorten it, do not lower the size.
2. **No exclamation marks, no emojis, no sustained capitals** (only the label is in capitals).
3. **Figures with their unit and a thin space**: `180 °C`, `40 min`. Use English number formatting (decimal point, comma for thousands): `72.5 %`, `1,000`.
4. **The text names what the drawing cannot**: the step, the figure or the condition. It does not repeat the narration.
5. **The video's language: English.** Check that the typeface has every symbol (`→` and `≈` may be missing in Noto Sans Display Bold: use `·` or "to").

## Why this typeface

- **Noto Sans Display Bold:** neutral sans-serif, uniform stroke and legible on small screens; it is sober and has no personality of its own to compete with the drawings. It is installed on this machine (`/usr/share/fonts/truetype/noto/`), published under a free license (SIL OFL) and Blender reads it without conversion.
- **Spaced copper label:** it organises without shouting and reuses the channel's accent.
- **Paper card with accent bar:** gives contrast without a black caption box.
- **A single hierarchy:** a small label and a large title are enough; no shadows or outlines.

## How it is implemented (Blender 5.2)

- Card: RGBA image the size of the frame, generated with `numpy` (rounded rectangle and bar), as an image strip with `blend_alpha` and offset in `transform.offset_y`.
- Text: two `TEXT` strips with `font`, `font_size`, normalised `location`, `anchor_x = "LEFT"` and `align_x = "LEFT"`; the label spacing is achieved with hair spaces.
- Script: `System/scripts/build_queque.py` and `build_chips.py` (section *label card*).

## Copy per scene (examples; the videos were narrated in Spanish, copy translated here)

| Lemon cake scene | Label | Title |
| --- | --- | --- |
| 1 | 6 steps | Lemon cake |
| 2 | Step 1 | Room temperature |
| 3 | Step 2 | Beat until pale |
| 4 | Step 3 | Eggs, one at a time |
| 5 | Step 4 | Mix just enough |
| 6 | Step 5 | Oven at 180 °C |
| 7 | Step 6 | The toothpick comes out clean |
| 8 | (no card) | |

| Chips scene | Label | Title |
| --- | --- | --- |
| 1 | Canon · Texas | September 2024 |
| 2 | ASML | Sole EUV supplier |
| 3 | TSMC · est. Q2 2026 | 72.5 % of the market |
| 4 | US · China · Japan | A fight over machines |
| 5 | According to Canon | 5 nm today · 2 nm goal |
| 6 | 2 nm | A goal, not a fact |
| 7 | (no card) | |

## Open

- [ ] Try the style on a non-cooking video (for example, figures from a political topic): does a two-line card work for a figure and its source?
- [ ] Define the 16:9 version.

## Copy for the Helium video (v2, one card per plate)

| Plate | Label | Title | Detail |
| --- | --- | --- | --- |
| 1 | MRI scanner | Up to 1,500 liters | liquid helium in a conventional magnet |
| 2 | Liquid helium | Stored at -269 °C | in insulated dewars like this one |
| 3 | Where it comes from | Uranium and thorium decay | Each decay releases one helium nucleus |
| 4 | Where it is found | Trapped with natural gas | Only a few gas fields, e.g. Texas |
| 5 | Why not manufacture it | No way to speed it up | No known large-scale way to make it |
| 6 | Once released | Escapes Earth's gravity | Lost to space, never recovered |
| 7 | Why nothing else works | Boils at 4.2 K (-269 °C) | Hydrogen boils at 20 K, nitrogen at 77 K |
| 8 | Who needs that cold | MRI magnets and chip fabs | US use: MRI 15 %, chips and fibre 17 % |
| 9 | USGS 2025 estimate | 85 % from three countries | US 43 % · Qatar 33 % · Russia 9.5 % |
| 10 | Price | Spot price doubled | after Qatar's output stopped in March |
| 11 | Sealed magnet | 7 liters instead of 1,500 | Philips' own figure |
| 12 | Newer still | 0.7 liters, closed circuit | Siemens' own figure |
| 13 | The takeaway | Use less, lose less | The safest helium never escapes |
