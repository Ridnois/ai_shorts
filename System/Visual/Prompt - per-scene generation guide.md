---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v5 · scientific-explainer line added (Magnetar feedback); v4 · content-first prompts, no custom style, references and transparent cutouts (4 Oct 2026)
tags: [research, youtube, illustration, audio, prompt, replicate]
---

# Prompt guide: per-scene generation

← [[YouTube Channel]] · [[Fast workflow]] · [[Narration guide]] · [[Illustration pipeline]] · [[Channel models]] · [[Media convention]]

> **No prompt is run before P4** (prompts and budget approved, in dollars). Models and prices: [[Fast workflow]] §3. The strategy (which plates are stock, which are generated, why) is in [[Illustration pipeline]]; this note is only how each prompt is written.

Every prompt ends in a Replicate *prediction* (`System/scripts/replicate_helper.py`). Parameters change by model: read them from the schema (`GET /v1/models/<owner>/<name>`, free), not from this note.

## 1. Image prompts (type G, C and E in the visual plan)

**A prompt is a specification, not a scene.** Write it in this order:

| # | Part | What goes there | Example |
| --- | --- | --- | --- |
| 1 | **Subject** | the exact object or process, with its real name | "a cross-section of a cylindrical MRI magnet cryostat" |
| 2 | **Structure** | the **parts, how many, and how they are arranged** (from the research note) | "an outer steel shell, a vacuum gap, a liquid-helium vessel, and a coil of niobium-titanium wire wound around the central bore" |
| 3 | **View** | the angle that makes it readable | "side cutaway", "exploded view", "top-down", "scale comparison with a human hand" |
| 4 | **What must be readable** | what the viewer has to understand from it, in plain words (a paraphrase of the narration idea, **never the narration sentence in quotes**) | "it must be clear that the coil sits inside the helium vessel, which sits inside the vacuum jacket" |
| 5 | **References** | for each input image, **what it supplies** | "image 1: the real outer shape of a clinical MRI scanner; image 2: the layout of a technical cutaway" |
| 6 | **Output** | background and framing, plus the no-text line | "plain white background, subject centred with a margin, no shadow on the ground. The image contains no letters, no numbers and no labels." For cutouts: `background: transparent`. |

**Scientific explainers (rule 2.13):** describe the established model as a textbook schematic, and add what must **not** appear: *"Plain light-grey background. No glow, no light rays, no decorative particles, no text."* Anything not in the research note is not in the prompt. Check the result element by element.

**Do:** be literal about structure, name materials, give relative sizes, say what is inside and what is outside. **Do not:** describe a mood, a story or a camera ("dramatic", "cinematic", "moody", "whimsical", "magical glow"), add a style (clay, sketch, watercolour, "miniature"), or add decorative props. If a detail is not needed to understand the idea, it is not in the prompt.

**Style:** none. The default of the model is the style ([[Illustration pipeline]] §1.4). If the output must be neutral, one line: *"clean, modern technical illustration"* or *"realistic product-photo rendering"*, chosen by the subject.

**Model by role:** `openai/gpt-image-2` for explainers and cutouts (several references, `input_fidelity: high` when a shape must be kept, `background: transparent` for cutouts); `flux-kontext-pro` only to **edit** a real photo; other models in [[Fast workflow]] §3.

### Worked examples (to verify against the research note before use)

- **Cutaway (G):** *"A side cross-section of a clinical MRI scanner. A large horizontal cylinder with a central patient bore. Inside the housing, from outside to inside: an outer shell, a vacuum layer, a thermal shield, a vessel of liquid helium, and the superconducting coil wound around the bore. A patient table slides into the bore. It must be clear that the helium vessel surrounds the coil. Image 1 supplies the outer shape of the scanner. Plain white background, no text, no labels."*
- **Process (G):** *"A top-down diagram of two graphene layers stacked, the upper layer rotated by a small angle against the lower, producing a larger repeating pattern where the atoms line up. Hexagonal lattices drawn as thin lines, upper layer in one colour, lower layer in another. Image 1 supplies the real moiré pattern. No text."*
- **Cutout (C):** *"A single tall insulated liquid-helium dewar with a rounded dome top, a neck with one valve and a wheeled base. Realistic. Transparent background, subject centred with a margin."* (`background: transparent`)

## 2. Voice: `elevenlabs/v3`

One take per scene, **with the exact script text** (a sentence is never cut). Current parameters (voice `Austin`, `language_code: en`, `speed`, `previous_text` / `next_text`) in [[Channel voice]]. Figures and acronyms are written as spoken if the model misreads them, and the change is noted; **the captions keep the clean spelling** through `captions` in `plan.json` ([[Blender editing]]). The takes are padded and faded in the edit ([[Blender editing]]), because the files often start and end abruptly.

## 3. Sound and music

None by default. If the script asks for it, take it from a **free licensed library** (sources, credits and levels in [[Guidelines for new scripts]] §3), not from a generator, with approval at P4a; files go to `sound/` with `_credits.jsonl`. There is no animation: the editing cross-fades and pushes the plates ([[Blender editing]]).

## 4. Log

For each prediction, one line: `scene · category · model · seed · ✅ used / ❌ discarded · https://replicate.com/p/<id>`. Files are saved per [[Media convention]]; discards go in `_descartes/`. If a download hangs, recover the prediction (`recover(id, dest)` in `replicate_helper.py`); never regenerate.
