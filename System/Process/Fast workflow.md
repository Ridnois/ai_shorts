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
- **Only if needed:** [[Narration guide]] (when writing), [[Visual style - plasticine miniatures]], [[Channel models]] (if the model changes), [[Blender editing]] and [[Transitions and effects]] (when editing).
- **A single note per video** (`<Topic> - Status`), with stages, budget, prompts and prediction log. No separate prompt notes.
- **Replicate results are not read whole:** keep the URL or the file and a one-line log entry.
- **Images are looked at in batches**, when the category is finished.
- **Everything is written in English** (notes, scripts, prompts, descriptions).

## 2. Flow in 5 packages

The stages are those of [[Production process]]; they are reviewed together:

| Package | Includes | Gate |
| --- | --- | --- |
| **A · Text** | Idea, research with sources, script and direction (text only) | **P1–P3 + P4a**, one review |
| **B · Budget** | Image and voice prompts, and the cost in dollars (§5) | **P4**: spending is authorized here |
| **C · Test** | Voice of scene 1 and one image (≈ $0.10 max.) | **P5** |
| **D · Generation** | **By category, in order: voice → image** (sound only if the script requires it) | P6, one approval per category |
| **E · Editing and publishing** | Render, description | **P7–P8** |

**Master rule: Replicate is not called before P4.** If the user delegates ("carry on until the render"), note it in the Status and continue without stopping within the cap.

## 3. Models by task

| Task | Model | Price | Notes |
| --- | --- | --- | --- |
| **Image · default (user decision, 3 Oct 2026)** | `black-forest-labs/flux-kontext-pro` **with a real reference** (photo of the object) | ≈ $0.04 (**from memory; confirm in the dashboard**) | 4 to 7 s. It is an **editing** model: a single `input_image`. Config and limits in §7 |
| Image · alternative | `wan-video/wan-2.7-image` | ≈ $0.02 (third party; **unconfirmed**) | Understands long prompts and 3 references, but draws real objects from memory. Used if Kontext does not solve the image |
| Image · alternative | `openai/gpt-image-1.5` (medium quality, **2:3 only**) | ≈ $0.05 | If Kontext does not solve the image; extended to 9:16 in editing |
| Image · hard edit | `google/nano-banana-2` (1K, 9:16, `image_search` for real objects) | ≈ $0.067 | Can write words |
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
5. **One real reference per shot** (Kontext accepts a single `input_image`).
6. **Prompts in the positive**; fix the prompt **before** retrying and retry **once**.
7. **Series, not parallel** (429).
8. **Discards go to `_descartes/`** and are not regenerated "to compare".
9. **No thumbnail on Shorts**; on long videos reuse an image from the video.
10. **A model research does not count as the video's cost** (see [[Guidelines for new scripts]] §5).

## 5. P4 budget (fixed format, in dollars)

| Category | Model | Quantity | Unit price | Subtotal | Cap (×1.2) |
| --- | --- | --- | --- | --- | --- |
| Voice | `elevenlabs/v3` | takes (per scene) | ≈ $0.10 per 1,000 characters | | |
| Image | `flux-kontext-pro` | plates (each with its second) | ≈ $0.04 (unconfirmed) | | |
| Sound | `audiogen` | only if the script asks | ≈ $0.011 | | |
| P5 test | one of each | | | (inside the total) | |
| **Total and cap** | | | | | |

**Real cost references:** Helium ≈ $2 (32 predictions); Brazil ≈ $0.46 (7 images); Lemon cake ≈ $1.57 (20 plates with `gpt-image-1.5`); Chips ≈ $0.48 (8 `flux-kontext-pro` images + 7 voice takes). With `flux-kontext-pro`, 20 plates ≈ $0.80 plus voice ≈ $0.11 (estimate).

**Log per video**, one line per prediction and without copying the input: `scene · category · model · seed · ✅ used / ❌ discarded · URL`. When closing each category, how many predictions against the cap; if over ×1.2, note why.

## 6. Shorts format (0 to 2 min): vertical 9:16

- **Image:** `aspect_ratio` 9:16 (or `match_input_image` with Kontext, see §7); a single subject, tall composition. Safe zone and image rules: [[Visual style - plasticine miniatures]] and [[Guidelines for new scripts]] §2.
- **Render in Blender:** `W, H = 1080, 1920`, 24 or 30 fps, H.264 and AAC; scale `max(...)` to fill the frame.
- **Duration:** ≈ 150 words for 60 s; longer is fine if needed.
- **Render name:** `<video>-<duration>-9x16-r<n>.mp4` ([[Media convention]]).
- Videos over 2 min stay 16:9.

## 7. Default image: `flux-kontext-pro` + real reference (3 Oct 2026)

> **User decision:** *"From now on we're using flux-kontext pro plus real references."* Evidence and tests: [[Research - Flux Kontext Pro with references (power)]].

- **Model:** `black-forest-labs/flux-kontext-pro`. Inputs: `prompt`, **`input_image` (a single one)**, `aspect_ratio` (accepts `match_input_image` and 9:16), `output_format`, `seed`. ≈ 4 to 7 s per image.
- **Real reference:** a **photo of the object** (Wikimedia Commons or another licensed source, **cropped to the object**, without a distracting background). Note each photo's license and attribution; with CC BY-SA, check it before publishing.
- **A single image:** the model does not accept several. **A collage of two references does not work** (the photo lost strength and only rings came out).
- **Prompt as an editing instruction:** *"Redraw this exact <object>… Keep the exact shape and proportions… Replace the background… Remove all lettering and logos…"* + a style line. State the parts that must be kept.
- **Orientation:** the model respects the input's composition; **a horizontal photo with a 9:16 canvas is rotated and distorted**. Try `match_input_image` or an already vertical input (Chips used `match_input_image` with 3:4 and 4:3 photos and filled the frame in editing).
- **Style:** plasticine miniature, the only one Kontext recognized as a style ("flat vector" and "screen print" came out as renders). Definition and prompt template: [[Visual style - plasticine miniatures]].
- **Cost and retries:** same as §4 (one retry per image, in series, cap ×1.2). One test image before a batch.
- **Fallback:** `wan-2.7-image` (earlier call: `prompt` with scene context, `images` = up to 3 real reference photos, `size` `1152*2048`).
