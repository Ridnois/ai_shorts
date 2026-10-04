---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v3 · more reference images, realism and faster change (Superconductors feedback, 4 Oct 2026); v2 scientific fidelity and no bare backdrops; v1 replaced the plasticine style
tags: [research, youtube, illustration, images, stock-photos, pipeline]
---

# Illustration pipeline

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Fast workflow]] · [[Prompt - per-scene generation guide]] · [[On-screen text style]] · [[Blender editing]]

> **Why this note exists.** Feedback on [[Twisted carbon - Status]]: *"the images feel not to be representing the content, nor describing the scenes, those shapes and styles are not helping… too little focus on the prompt quality… less approach on scene description, it is not a theatre show, it is modern content… use illustrations where they are useful: describe machines and explain processes… use free stock photos… use the model on the style it performs best, not a custom illustration style… generate images with transparent background and apply background gradients and styles in Blender."* The plasticine miniature style (videos 6 to 8) is **retired**: it made every object look like a toy and carried no information. This note is the source of truth for every image in every video.

## 1. Principles

1. **An image earns its place.** Every plate passes the **usefulness test**: write one sentence, *"this plate lets the viewer see ___ so they understand ___"*. If the sentence cannot be written (or reads "it looks nice"), the plate is replaced or cut.
2. **Show the thing, or explain the thing.** Real-world subjects (a place, a machine, an experiment, a material) → **a real photo** (free stock). Hidden things (insides, processes, structures, scales) → **a generated explainer** (cutaway, cross-section, exploded view, schematic). Never a decorative stand-in.
3. **Modern, not theatrical.** Describe the **subject and what must be understood**, not a mood, a scene or a "story". No "dramatic", "moody", "cinematic", "whimsical", "toy", "miniature".
4. **Use the model in the style it does best.** No custom style block. Let the model default to a clean, generic, modern look (photoreal or clean technical render, depending on the subject) and put the effort into **content-accurate prompts and good references** instead.
5. **Style is added in the edit, not in the prompt.** Backgrounds, gradients, shadows, framing and text are applied in Blender ([[Blender editing]]); images are generated as **full frames or as transparent cutouts**.
6. **Scientific fidelity beats creativity** (Magnetar feedback, 4 Oct 2026: *"illustrations are too creative and unscientific"*). An explainer shows only what the research note supports, in the form of a **textbook or agency schematic** of the established model; real counts, real arrangement, real relative scale. **Decorative structure that looks like data is a defect**: the Magnetar starquake plate's glowing arcs read as field lines but were invented. The prompt lists what must **not** be invented ("no glow, no light rays, no decorative particles"); after generation, **every element is checked against the research note** and the Status note records what is schematic ("pair size not to scale"). If an element cannot be sourced, regenerate once without it or use a photo.
7. **No bare backdrops.** A number card, callout or quote never sits on an empty gradient (feedback: *"blue empty background with added text is strange, illustrations could go there"*). It sits **on a real photo or a faithful explainer of the thing the number describes**. A gradient is only the surface behind a `contain` photo or a cutout; `build_video.py` refuses blank placeholder plates.

## 2. The visual plan (stage 3, one row per plate)

Before any prompt, the script note gets a **visual plan**: one row per plate with its type, source and usefulness sentence ([[Production process]], gate P4a).

| Type | Use it for | Source | Cost |
| --- | --- | --- | --- |
| **S · Stock photo** | real subjects: places, equipment, materials, historical objects | free sources, §5 | $0 |
| **G · Generated explainer** | insides and processes: cutaways, cross-sections, exploded views, schematics, scale comparisons | `openai/gpt-image-1.5` with a descriptive prompt and references, §3 | ≈ $0.05 |
| **C · Cutout** | a single object or part, placed on a Blender gradient with a soft shadow and callouts | transparent PNG: generated with `background: transparent`, or a stock photo cut out with `bria/remove-background` | ≈ $0.05, or $0 + the cut-out |
| **E · Edit of a real photo** | change one thing in a real photo (remove text, extend, recolour a part) | `black-forest-labs/flux-kontext-pro` (as an editor, never a restyler) | ≈ $0.04 |
| **N · Number or text plate** | a single figure or a fact that needs no image | built in Blender ([[On-screen text style]]) | $0 |

**Mix by default (a Short of 16 to 20 plates, a new image every ≈ 3 to 4 s, none over 5 s; Superconductors feedback: *"add more reference images, so it changes faster"*):** at least **half real photos or real scientific figures (free)**, at least **a third generated explainers or cutouts**; **no two consecutive plates of the same type** (a stock `full` photo next to a stock `full` photo is the same type; alternate with an explainer, or change both the treatment and the subject); a plate is held about **3 to 4 s**, so a Short has roughly one plate per 3 to 4 s of voice. **The same photo may appear twice if the crop shows a different detail** (`focus` and `zoom` in the plan).

**Plan example (one row):** `7 · S+callouts · "a helium dewar in a lab" · lets the viewer see how large and plain the tank is so they understand that helium is stored as a cold liquid in unglamorous steel · source: Wikimedia (CC BY-SA) · callouts: valve, wheeled base`.

## 3. Generated images: prompts that carry the content

Full recipe and templates in [[Prompt - per-scene generation guide]]. The rules:

- **Fully descriptive and content-first.** Name the **exact object or process**, its **parts and their count and arrangement**, the **view** (side, cross-section, exploded, top-down), and **what must be readable** about it. If the real thing has a known structure (a superconducting MRI magnet, a graphene lattice, a split-ring resonator), describe that structure, not a vague likeness.
- **Explain, do not stage.** Prompts describe machines and processes ("a cross-section of a cylindrical cryostat: an outer steel shell, a vacuum gap, a liquid-helium vessel, and a coil of wire at the centre"), not scenes.
- **References do the heavy lifting.** Pass 1 to 4 real photos or diagrams (`input_images` in `gpt-image-1.5`) and **say what each one supplies** ("image 1: the real shape of the dewar; image 2: the layout of a cutaway view"). Prefer references from the stock sources in §5; keep their credits.
- **No style block.** Optionally one neutral line about the output: "clean, modern, high-detail technical illustration on a plain background". No clay, no sketch, no "hand-drawn".
- **Transparent background when the plate is a cutout:** `background: transparent`, `output_format: png`, subject centred with margin, no ground shadow, no floor (the shadow is added in Blender).
- **No text inside the image:** labels are added as callouts in Blender. State it ("no letters, no numbers, no labels"), and **check each plate for leaks** (rule 2.11 in [[Guidelines for new scripts]]).
- **Check against the facts:** counts and structures are verified against the research note; a pretty but wrong cutaway fails the usefulness test.

## 4. Models, each in its natural role

| Role | Model | Notes |
| --- | --- | --- |
| Explainers and cutouts with references | **`openai/gpt-image-1.5`** | follows detailed prompts and several references best; `background: transparent`; aspect ratios 1:1, 3:2, 2:3 only; `quality` medium; `input_fidelity: high` when the reference shape must be kept |
| Real-photo edits | `black-forest-labs/flux-kontext-pro` | one `input_image`; use it to **edit** a photo, not to convert it to a style; a prompt that carries narration text can leak it into the image |
| Hard edits and real-object grounding | `google/nano-banana-2` | with `image_search`; ≈ $0.067 |
| Background removal | `bria/remove-background` (alternatives `lucataco/remove-bg`, `cjwbw/rembg`) | for stock photos that become cutouts; **price and quality unconfirmed: test on one image** |

Prices and caps: [[Fast workflow]] §3 to §5. **Test before a batch:** one generated cutout and one stock cutout, composed in Blender, at P5.

## 5. Free stock photos

Helper: `System/scripts/stock_photos.py` (search, download, credits log).

| Source | Access | License | Good for |
| --- | --- | --- | --- |
| **Openverse** (aggregates Flickr, Wikimedia, museums) | API, no key | filter `commercial`; mixed CC and public domain | most subjects, including technical equipment |
| **NASA images** | API, no key | mostly public domain (check the guidelines) | space, labs, materials, engineering |
| **Wikimedia Commons** | search by API, **fetch originals directly** from `upload.wikimedia.org` (the thumbnail API throttles) | CC0, CC BY, CC BY-SA, public domain | diagrams, history, science |
| Pexels, Pixabay, Unsplash (API) | need a free API key | their own permissive licenses | generic photography; **ask the user for keys before relying on them** |

**Quota:** find **2 to 3 candidate photos or figures per scene** before writing the visual plan (Commons, NASA, Openverse; real diagrams from papers or Wikipedia as `contain` plates, credited). When a real photo exists, **photo plus callouts beats a generated schematic** (rule 2.15 in [[Guidelines for new scripts]]).

**Selection:** relevance first (does it show the exact thing the narration names?), then quality (≥ 1,080 px wide, sharp, no watermark, no visible brand unless it is the subject), then license. **License and attribution are recorded for every photo** in `Media/<video>/stock/_credits.jsonl` and copied into the Status note's attribution table; CC BY and CC BY-SA photos are credited in the description. No identifiable people unless the person is the subject and the license allows it.

## 6. Composition in Blender (plan file)

Each video has a `plan.json` consumed by `System/scripts/build_video.py` ([[Blender editing]]). Plate fields:

```json
{ "type": "full | contain | cutout",
  "file": "plates/he-p03.png",
  "focus": [0.5, 0.45],                       // full: the point that stays in frame
  "bg": ["#0b1a2b", "#27507a"], "bg_angle": 70, // contain/cutout: gradient colours and angle
  "pos": [0.5, 0.40], "size": 0.5, "width": 0.9, // placement (fractions of the frame)
  "callouts": [ {"text": "Vacuum gap", "target": [0.42, 0.33], "label": [0.7, 0.2]} ],
  "card": ["Where it is found", "Trapped with natural gas", "Only a few gas fields, e.g. Texas"] }
```

- **full**: a photo or generated image that fills the frame, with a slow push toward the focus point.
- **contain**: a photo or diagram fitted inside the frame with rounded corners and a soft shadow, on a gradient: for wide photos and diagrams that must not be cropped.
- **cutout**: a transparent PNG over a gradient with a soft shadow.
- **Gradients:** two colours and an angle, **one palette family per video** chosen from the topic (cold blue for cryogenics, warm copper for heat and energy, deep green for materials and biology), dark enough for white-paper cards and callouts to stand out; vary the angle between plates, not the family.
- **Callouts** name parts of the image (see [[On-screen text style]]); labels never sit over the card.

## 7. Budget and tests

Stock photos cost nothing; generated explainers and cutouts ≈ $0.05 each; background removal to be measured. A Short plans **≤ 5 generated images** by default, so a typical image budget is **under $0.40**, with the usual cap (base × 1.2) and a **P5 test** of the whole chain (one generated cutout, one stock photo, composed in Blender).

## 8. What this replaces

- A decorative, "creative" explainer (Magnetar plate with invented glowing arcs) and bare gradient plates for number cards (Magnetar plates 3, 5, 7). The plasticine miniature style and its prompt template (videos 6 to 8: Chips, Helium, Twisted carbon). Lessons that survive: still states beat "interaction" states; wide images need a composed 9:16 canvas; check plates for text leaks.
- `flux-kontext-pro` as the default generator ([[Research - Flux Kontext Pro with references (power)]] stays as model research).
- One reference photo per plate and "real object redrawn as clay".
