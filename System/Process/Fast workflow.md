---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · English-only since 3 Oct 2026; each video's lessons live in the guidelines
tags: [research, youtube, process, costs, replicate]
---

# Fast workflow

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Production process]] · [[Channel models]]

**To produce a video you read two notes: this one (how and with what it is produced) and [[Guidelines for new scripts]] (which quality rules apply).** Everything else is reference.

## 1. Saving tokens

- **Sonnet 5.5, no subagents**: the work is sequential and short.
- **Minimum reading at the start:** these two notes + `<Topic> - Status` + the current script.
- **Only if needed:** [[Narration guide]] (when writing), [[Illustration pipeline]], [[Channel models]] (if the model changes), [[Blender editing]] and [[Transitions and effects]] (when editing).
- **A single note per video** (`<Topic> - Status`), with stages, budget, prompts and prediction log. No separate prompt notes.
- **Replicate results are not read whole:** keep the URL or the file and a one-line log entry.
- **Images are looked at in batches**, when the category is finished.
- **Everything is written in English** (notes, scripts, prompts, descriptions).

## 2. Flow in 5 packages

The stages are those of [[Production process]]; they are reviewed together:

| Package | Includes | Gate |
| --- | --- | --- |
| **A · Text** | Idea with ranked angles and five hooks, **facts bank and scoring** ([[Idea and hook quality]]), research with sources, script (sized in words) and the **visual plan** (one row per plate: type, source, usefulness sentence, [[Illustration pipeline]] §2) | **P1–P3 + P4a**, one review |
| **B · Budget** | **Stock photos picked and downloaded (free, credits logged)**, prompts for the generated plates (content-first, [[Prompt - per-scene generation guide]]), voice prompts, `plan.json`, and the cost in dollars (§5) | **P4**: spending is authorized here |
| **C · Test** | Voice of scene 1, **one generated cutout and one stock photo composed in Blender** (≈ $0.10 max.) | **P5** |
| **D · Generation** | **By category, in order: voice → image** (sound only if the script requires it) | P6, one approval per category |
| **E · Editing and publishing** | Render, description | **P7–P8** |

**Master rule: Replicate is not called before P4.** If the user delegates ("carry on until the render"), note it in the Status and continue without stopping within the cap.

## 3. Models by task

| Task | Model | Price | Notes |
| --- | --- | --- | --- |
| **Image · generated explainers and cutouts (default, 4 Oct 2026)** | `openai/gpt-image-1.5` (medium quality; 1:1, 3:2 or 2:3) with a descriptive prompt and up to 4 references; `background: transparent` for cutouts; `input_fidelity: high` to keep a reference's shape | ≈ $0.05 (**unconfirmed on Replicate**) | The model's own style; no style block ([[Illustration pipeline]]) |
| **Image · stock photos** | free sources (Openverse, NASA, Wikimedia) via `System/scripts/stock_photos.py` | $0 | Credits logged; ask the user for Pexels, Pixabay or Unsplash keys if needed |
| Image · background removal | `bria/remove-background` (alternatives `lucataco/remove-bg`, `cjwbw/rembg`) | **to measure** (test on one image) | Turns a stock photo into a cutout |
| Image · photo edit | `black-forest-labs/flux-kontext-pro` | ≈ $0.04 (unconfirmed) | **Edits** a real photo (remove text, extend, recolour a part); one `input_image`; not used to restyle |
| Image · hard edit | `google/nano-banana-2` (1K, `image_search` for real objects) | ≈ $0.067 | Can write words |
| Image · other | `wan-video/wan-2.7-image` ≈ $0.02 (unconfirmed, up to 3 references, tends to draw objects from memory) | | Fallback |
| Image · draft | `black-forest-labs/flux-2-klein-4b` | ≈ $0.015 | Fails at counts and copies references |
| Image · hard scene | `bytedance/seedream-5-lite` | $0.035 | That scene only |
| **Voice (English)** | `elevenlabs/v3`, `Roger`, `language_code: en` | ≈ $0.10 per 1,000 characters | Chosen by the user for the channel. Parameters in [[Channel voice]] and [[Guidelines for new scripts]] §3 |
| Voice · cheap alternative | `qwen/qwen3-tts` | ≈ $0.02 per 1,000 | No `speed`, ≈ 122 words per minute; English quality untested |
| Sound | `sepal/audiogen` | ≈ $0.011 | **Only if the script asks for it**; 16 kHz. `mmaudio` fails with text only |
| Animation and music | None | $0 | Editing cross-fades plates in Blender |

**Not used:** `qwen-image-edit-plus` to generate (copies the references), `flux-2-pro` (expensive), `stable-audio-2.5` ($0.20 per file).

**How to call Replicate without overspending:** the schema is read with `GET /v1/models/<owner>/<name>` (free); community models go through `POST /v1/predictions` with `version`; with `urllib` a `User-Agent` is needed (otherwise 403). Reuse `System/scripts/replicate_helper.py`. A command with more than ≈ 15 calls exceeds the time limit: batches of ≤ 10, and check which files are missing.

## 4. Rules to avoid generating too much

1. **Only images that appear in the cut**; every budget row cites the script second where it is used.
2. **1 image per shot**; 2 only if the shot needs a before and an after.
3. **Cap per video = base images × 1.2.** Going over needs approval.
4. **Minimal test (P5):** one scene, one image, one model. Compare models only if the user asks.
5. **Stock first:** a plate that shows a real thing is a free stock photo; generate only what cannot be photographed (insides, processes, structures). Default **≤ 5 generated images per Short.**
6. **Prompts in the positive**; fix the prompt **before** retrying and retry **once**.
7. **Series, not parallel** (429).
8. **Discards go to `_descartes/`** and are not regenerated "to compare".
9. **No thumbnail on Shorts**; on long videos reuse an image from the video.
10. **A model research does not count as the video's cost** (see [[Guidelines for new scripts]] §5).

## 5. P4 budget (fixed format, in dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` | takes (per scene) | ≈ $0.10 per 1,000 characters | | |
| Image (generated) | `gpt-image-1.5` | generated plates only (≤ 5 by default, each with its second) | ≈ $0.05 (unconfirmed) | | |
| Image (stock) | free sources | plates | $0 | $0 | — |
| Background removal | `bria/remove-background` | stock photos that become cutouts | to measure | | |
| Sound | `audiogen` | only if the script asks | ≈ $0.011 | | |
| P5 test | one of each | | | (inside the total) | |
| **Total and cap** | | | | | |

**Real cost references:** Helium ≈ $2 (32 predictions); Brazil ≈ $0.46 (7 images); Lemon cake ≈ $1.57 (20 plates with `gpt-image-1.5`); Chips ≈ $0.48 (8 `flux-kontext-pro` images + 7 voice takes). With `flux-kontext-pro`, 20 plates ≈ $0.80 plus voice ≈ $0.11 (estimate).

**Log per video**, one line per prediction and without copying the input: `scene · category · model · seed · ✅ used / ❌ discarded · URL`. When closing each category, how many predictions against the cap; if over ×1.2, note why.

## 6. Shorts format (0 to 2 min): vertical 9:16

- **Image:** generated plates in 2:3 (the nearest to 9:16) or as transparent cutouts; stock photos as they are; everything is composed onto 1080×1920 in Blender (`full`, `contain`, `cutout`). Safe zone and image rules: [[Illustration pipeline]] and [[Guidelines for new scripts]] §2.
- **Render in Blender:** `System/scripts/build_video.py` from a `plan.json` (1080×1920, 24 fps, H.264 and AAC); see [[Blender editing]].
- **Length is planned in words (130 to 190 for a Short), never in seconds;** the duration is measured after the voice exists (≈ 144 words per minute in English).
- **Render name:** `<video>-<duration>-9x16-r<n>.mp4` ([[Media convention]]).
- Videos over 2 min stay 16:9.

## 7. Images: the pipeline in one page (4 Oct 2026)

> **User feedback (Twisted carbon):** use illustrations where they are useful, describe machines and explain processes; use free stock photos plus generated images with fully descriptive prompts and references; use the model in its own style, not a custom one; generate transparent backgrounds and apply gradients in Blender. Full method: [[Illustration pipeline]].

1. **Stage 3, visual plan:** one row per plate (type S, G, C, E or N, source, usefulness sentence).
2. **Package B:** download the stock photos (`stock_photos.py`, credits in `stock/_credits.jsonl`); write the content-first prompts for the generated plates ([[Prompt - per-scene generation guide]]).
3. **P5 test:** one generated cutout and one stock photo composed in Blender with a callout.
4. **Generation:** `gpt-image-1.5` in series, one retry per image, ≤ 5 images by default; background removal for stock cutouts.
5. **Edit:** `plan.json` + `build_video.py`: types `full`, `contain`, `cutout` over gradients, callouts, cards, padded voices, `CHECK=1`.
6. **Past method (retired):** Kontext + a real reference redrawn as plasticine (videos 6 to 8). Evidence and tests: [[Research - Flux Kontext Pro with references (power)]].
