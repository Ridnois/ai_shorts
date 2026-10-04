---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v1 · designed for vertical 9:16 Shorts; English-only since 3 Oct 2026
tags: [research, youtube, style, typography, text]
---

# On-screen text style

← [[Visual style - plasticine miniatures]] · [[Blender editing]] · [[YouTube Channel]]

> **Commission (3 Oct 2026):** *"Design a style for text, it must be sober, professional and modern."*

**Principle:** the text is a **sober label**, not a subtitle or a headline. It says little, is read at a glance and does not compete with the image. It is a paper card, ink and the same copper-orange accent as the illustrations ([[Visual style - plasticine miniatures]]).

## Piece: label card (*lower third*)

One card per scene, left-aligned, with **two lines**: a small label and a title.

| Element | Specification |
| --- | --- |
| **Label** (line 1) | Capitals with wide spacing (hair spaces U+200A between letters), **Noto Sans Regular, 34 px**, copper `#C76B38`. Examples: `S T E P  1`, `6  S T E P S` |
| **Title** (line 2) | **Noto Sans Display Bold, 58 px**, ink `#1C1A17`, **sentence case** (only the first letter capitalised), a single line, **max. 26 characters** |
| **Card** | Warm paper `#F9F6EE` at 94 % opacity, 16 px corners, 1 px graphite border at 25 %, **8 px copper bar on the left edge**. Width 894 px (56 px left margin and 130 px on the right, where Shorts puts its buttons), height ≈ 210 px |
| **Position** | Between 22 % and 33 % of the height from the bottom: **above the Shorts caption and button zone**; the top 6 % stays free |
| **Appears / leaves** | 0.25 s fade with a 24 px rise; leaves with a 0.2 s fade. Enters 0.5 s after the scene starts and leaves 0.15 s before it ends |
| **One at a time** | Never two cards or text over text |

## Writing rules

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
