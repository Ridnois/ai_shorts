---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · rewritten for flux-kontext-pro + real photo and an English elevenlabs voice
tags: [research, youtube, illustration, audio, prompt, replicate]
---

# Prompt guide: per-scene generation

← [[YouTube Channel]] · [[Fast workflow]] · [[Narration guide]] · [[Visual style - plasticine miniatures]] · [[Channel models]] · [[Media convention]]

> **No prompt is run before P4** (prompts and budget approved, in dollars). Models and prices: [[Fast workflow]] §3. Here only how each prompt is written from the script's scene row ([[Narration guide]] §4).

Every prompt ends in a Replicate *prediction* (`System/scripts/replicate_helper.py`). Parameters change by model: they are read from the schema (`GET /v1/models/<owner>/<name>`, free), not from this note.

## 1. Image: `flux-kontext-pro` + real photo

One image per scene. Input: **a cropped real photo** (`input_image`), in the orientation of the result. The prompt is an **editing instruction**; the full method and style are in [[Visual style - plasticine miniatures]].

Every prompt carries, in this order:

1. **What the narration says at that moment** (the script sentence, in English since the scripts are English): it avoids the generic prompt that forgets the research.
2. **The real object and the parts that must be kept** (from the object sheet).
3. **Which state the image shows** (one image = one state).
4. **The single copper-orange accent**: which element.
5. **Composition**: vertical 9:16, subject in the top two thirds.
6. **Style block** from [[Visual style - plasticine miniatures]].

Rules: prompts in the positive; no text, figures or faces in the image; counts and parts are checked by eye; one retry with the corrected prompt, in series. A scene with no object that has a photo is redesigned around one.

## 2. Voice: `elevenlabs/v3`

One take per scene, **with the exact script text** (a sentence is never cut). Current parameters (voice `Roger`, `language_code: en`, `speed`, `previous_text` / `next_text`) in [[Channel voice]]. Figures and acronyms are written as spoken if the model misreads them, and the change is noted.

## 3. Sound and music

None by default. Only if the script requires it, and with approval at P4 ([[Guidelines for new scripts]] §3). There is no animation: the editing cross-fades the images ([[Blender editing]]).

## 4. Log

For each prediction, one line: `scene · category · model · seed · ✅ used / ❌ discarded · https://replicate.com/p/<id>`. Files are saved per [[Media convention]]; discards go in `_descartes/`.
