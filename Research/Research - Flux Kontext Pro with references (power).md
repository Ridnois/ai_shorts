---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · 4 test images · the style half works and the shape is not preserved
tags: [research, youtube, models, image, flux-kontext]
---

# Flux Kontext Pro with references: exploded view of a stem

← [[YouTube Channel]] · [[Visual style - plasticine miniatures]] · [[Fast workflow]]

General channel research, **independent of any script**: useful for any video with real parts. The test subject is the same plate that `wan-2.7-image` drew as a hub: the **exploded view of a threadless stem** (Aheadset). (A "stem" here is the bicycle part joining the fork to the handlebar.)

> **Commission (3 Oct 2026):** *"Generate a stem image with flux-kontext-pro, use image references and show it on the research."*

## How it was done

- **Model:** `black-forest-labs/flux-kontext-pro`. Schema inputs (read for free): `prompt`, **`input_image` (a single image)**, `aspect_ratio` (9:16), `output_format`, `seed`, `safety_tolerance` and `prompt_upsampling`.
- **A single input image, so I made a collage** of two references, joined side by side in one file: on the left a **real photo** of a threadless stem, for the shape; on the right a **simple exploded view** from the library, for the layout.
- **Prompt:** *"Use the LEFT photo only as the exact shape reference… use the RIGHT image only as a guide for how an exploded view is laid out"* + a description of the exploded view from bottom to top (fork, **three** spacers, stem with rear and front clamp, cap with a bolt) + flat vector style with a copper-orange accent. Full text in `Media/_canal/investigacion/potencia-kontext/prompt-A.txt`.
- **Cost:** **1 prediction**, [`h43qrsc3q5rmt0d10ecvy2j5cg`](https://replicate.com/p/h43qrsc3q5rmt0d10ecvy2j5cg), ≈ 5 s. This model's usual rate ≈ $0.04 per image (**from memory, unconfirmed on Replicate's page**). It does not count as any video's cost.

## References

| Reference | What it provides | License |
| --- | --- | --- |
| ![[ref-stem-foto-a.jpg]] | Real photo of a threadless stem with cap, rear clamp and front plate | CC BY-SA 3.0 (Wikimedia Commons: [Threadless stem with hole for front brake cable](https://commons.wikimedia.org/wiki/File:Threadless_stem_with_hole_for_front_brake_cable.JPG)) |
| `ref-explosionada-bloques.jpg` (exploded-view illustration) | Layout of an exploded view | Public domain |

Other photos downloaded and unused: `ref-stem-foto-b.jpg` (stem with a steerer adapter, CC BY-SA 4.0, Troy Sankey) and `ref-stem-foto-c.jpg` (adjustable stem, CC BY-SA 3.0). If a plate derived from a CC BY-SA photo is ever published, check the attribution.

## Result

![[potencia-kontext-A-v1.png]]

**What went well**
- **The style:** flat vector, cream paper, warm greys and **a single copper-orange accent** (the arrow). It is the half that was asked for and it comes out clean, with no text or figures.
- **The layout:** a vertical column with dashed guide lines, as in the reference exploded view.
- **Speed:** ≈ 5 s, versus 14 to 21 s for `wan-2.7-image`.

**What went wrong**
- **There is no stem.** They are rings and cups: a cap, a ring, three spacers, a dotted ring and a headset cup with windows. **The stem body, the handlebar clamp and the fork's steerer tube are missing**, exactly what the reference photo showed.
- **The model copied the "exploded rings" idea from the collage** and followed the spacers text, but ignored the real shape. The photo, with a brick-and-railing background, did not translate into geometry.
- **The copper-orange accent** is on the arrow and not on the clamp, as requested (the clamp does not exist).

## Reading

- **The style is not the problem.** `flux-kontext-pro` delivers the flat style first time and fast, but **it does not extract an object's shape from a photo with a background when it is inside a collage**. The collage probably took strength away from the photo (the second image was much wider and took almost the whole frame).
- **Kontext is designed to edit one image**, not to generate from two. With a single input image, the natural thing is to pass **the photo alone** and ask *"redraw this exact stem as a flat vector illustration"*, and explode it afterwards.

## Round 2 · photo alone and three styles (3 Oct 2026)

> **Commission:** *"Remember on the vault that from now on we're using flux-kontext pro plus real references; generate a test image with three different illustration styles optimized for this model."*

**How it was done (changes from round 1):**
- **The photo alone, cropped** to the stem (`ref-stem-foto-a-recorte.jpg`, no brick or railing), no collage.
- **Prompts written as editing instructions**, which is how Kontext works: *"Redraw this exact bicycle stem… Keep the exact shape and proportions… Replace the background… Remove all lettering and logos…"* + a style line. Texts in `_canal/investigacion/potencia-kontext/prompt-solo-A/B/C.txt`.
- `aspect_ratio` 9:16, one image per style. **3 predictions**: A [`d49bwxdjwxrmt0d10edsegamkc`](https://replicate.com/p/d49bwxdjwxrmt0d10edsegamkc), B [`x8ppqqek01rmt0d10edvymqw5g`](https://replicate.com/p/x8ppqqek01rmt0d10edvymqw5g), C [`59vxwgxdg1rmr0d10eg9wyhk3g`](https://replicate.com/p/59vxwgxdg1rmr0d10eg9wyhk3g). With round 1 that is **4 Kontext predictions** (≈ $0.16 if the rate is ≈ $0.04; unconfirmed). The connection dropped halfway through the series: I recovered the already finished prediction B instead of repeating it, so it was not paid twice.

| Style | Result |
| --- | --- |
| **A · flat vector** ![[potencia-kontext-A-solo-v1.png]] | **It is not flat vector:** it is a grey matte 3D piece with an orange screw mark. **It does not look like a stem**: it is a bracket with two ears. The photo was barely preserved |
| **B · plasticine** ![[potencia-kontext-B-solo-v1.png]] | **The style does work:** grey clay with cracks and fingerprints, tabletop background, copper-orange cap. The shape is the closest: a T-shaped piece with a cap and two side bolts, **but with extra rings** and without the arm toward the handlebar |
| **C · screen print** ![[potencia-kontext-C-solo-v1.png]] | **It is not screen print:** it is a photographic render with flat colours, with no halftone or layer misregistration. The **shape is recognisable** (body, round front clamp with four bolts, cap with a bolt), but **standing up** and with a deformed cap |

### Reading

- **Kontext respects the input image's composition.** The photo has the stem **horizontal** and I asked for a **vertical** canvas (9:16): the model rotated and recomposed it, and that broke the shape. In all three cases the arm toward the handlebar and the relation to the fork were lost.
- **Of the three styles, only B is recognised as a style.** A and C ended up as renders: "flat vector" and "screenprint" are not enough as an editing instruction, and the model keeps the photo's 3D-object look.
- **All three removed the text and the background**, as requested (the "ITM" brand disappeared).
- **Speed and cost:** 4 to 7 s per image, much faster than `wan-2.7-image` (14 to 21 s).
- **None of the three is usable yet as a video plate.** Orientation needs solving, not style.

### Update (3 Oct 2026, Chips Short)

`match_input_image` with real photos of the objects worked: the wafer, the padlock and the lithography machine kept their shape and the clay look. See [[Chips and lithography - Status]] and [[Visual style - plasticine miniatures]].

### What I would try next (each ≈ $0.04; **I did not do it**, needs your OK)

1. **`aspect_ratio: match_input_image`** (the horizontal photo, without forcing 9:16) and frame vertically in editing, as was done with `gpt-image-1.5`. *(Done later with the Chips video.)*
2. **Prepare the vertical input:** place the cropped stem photo, without rotating it, on a blank or cream 9:16 canvas, so Kontext completes the rest.
3. **A style instruction closer to the image,** in steps: first *"turn this photo into a clay miniature"* (B, which already works) and then editing the framing or the colour.
4. **Round-trip editing template:** first "redraw as a flat illustration" with a real style example as a second image, **but Kontext only accepts one image**, so the style sheet would have to be used as text.

## Open

- [x] Channel style: **B (plasticine)**, defined in [[Visual style - plasticine miniatures]] (the user can veto it).
- [x] Try the input with `match_input_image` (worked in the Chips video).
- [ ] Prepared vertical canvas input.
- [ ] Compare with `wan-2.7-image` on the same plate and with the same style.
- [ ] Confirm `flux-kontext-pro`'s price on Replicate.
