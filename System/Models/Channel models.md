---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · cost re-evaluation without running models · prices read on Replicate's pages on 3 Oct 2026; English voice added
tags: [research, youtube, models, replicate, costs]
---

# Channel models

> **Current selection: [[Fast workflow]]** (§3: `flux-kontext-pro` + real photo, `elevenlabs/v3`). This note only keeps the price tables; where they differ, [[Fast workflow]] rules.

← [[YouTube Channel]] · [[Production process]] · [[Prompt - per-scene generation guide]] · [[Channel voice]] · [[Illustration pipeline]]

Which model is used in each case, **with its real price on Replicate**. This version comes from a user complaint: *"it's getting expensive, too much test"*. It was re-evaluated **without running any model**: only the price pages and input schemas were read.

**Used** = it already generated files for a video. **Candidate** = not tested. Models are fixed at stage 5 of the [[Production process]]; nothing runs before gate P4.

## Prices (Replicate, 3 Oct 2026)

Read in each model's *Pricing* section. Per-megapixel prices count **input and output**: a reference image is also charged.

### Image

| Model | Price | Input references | Notes |
| --- | --- | --- | --- |
| `black-forest-labs/flux-kontext-pro` **(current)** | ≈ $0.04 per image (**from memory, unconfirmed**) | a single `input_image` | Edits a real photo; see [[Fast workflow]] §7 |
| `black-forest-labs/flux-2-pro` (used before) | $0.015 per run + $0.015 per input megapixel + $0.015 per output megapixel → **≈ $0.045 with one reference** | up to 8 | **Does not understand negative prompts**: "no text" may add text |
| `black-forest-labs/flux-2-flex` | $0.06 per input and output megapixel | up to 10 | More expensive; meant for typography |
| `black-forest-labs/flux-2-max` | $0.04 per run + $0.03 per input and output megapixel | up to 8 | The most expensive of the family |
| `bytedance/seedream-5-lite` | **$0.035 per output image**, flat | up to 14 | Built-in reasoning (space and physics), sequential batches; no extra charge for the references |
| `ideogram-ai/ideogram-v3-turbo` | **$0.03 per image** (balanced $0.06; quality $0.09) | up to 3 style | Style presets; strong at text, which we do not want here |
| `recraft-ai/recraft-v4.1` | $0.04 per image | **none** (prompt, size and aspect only) | Design focus; not useful for generating the final from the initial |
| `google/imagen-4-ultra` | $0.06 per image | — | Text to image only |
| `google/nano-banana-2` | $0.067 (1K), $0.101 (2K), $0.151 (4K) per image | up to 14 | Conversational editing and image blending; the most expensive useful one for editing |
| `openai/gpt-image-2` | no readable price on the page | — | Not evaluated |

### Voice

| Model | Price | Cost of a ≈ 1,000-character script |
| --- | --- | --- |
| `qwen/qwen3-tts` **(used)** | $0.02 per 1,000 characters | **≈ $0.02** |
| `resemble-ai/chatterbox-turbo` | $0.025 per 1,000 characters | ≈ $0.025 |
| `minimax/speech-2.8-turbo` | $0.06 per 1,000 tokens (≈ 1 token per character) | ≈ $0.06 |
| `minimax/speech-2.8-hd` | $0.10 per 1,000 tokens | ≈ $0.10 |
| `elevenlabs/v3` **(current, English `Roger`)** | $0.10 per 1,000 characters | ≈ $0.10 |
| `google/gemini-3.1-flash-tts` | $2 per million input tokens + $0.04 per 1,000 output | ≈ $0.015 per 15 s take; ≈ $0.07 per 70 s |

`elevenlabs/v3` voices on Replicate (26): Rachel, Drew, Clyde, Paul, Aria, Domi, Dave, Roger, Fin, Sarah, James, Jane, Juniper, Arabella, Hope, Bradford, Reginald, Gaming, Austin, Kuon, Blondie, Priyanka, Alexandra, Monika, Mark, Grimblewood. English choice and alternative: [[Channel voice]].

### Sound

| Model | Price | Notes |
| --- | --- | --- |
| `stability-ai/stable-audio-2.5` **(used)** | **$0.20 per file** | The most expensive per unit in the whole channel |
| `zsxkib/mmaudio` | ≈ $0.005 per run | **≈ 38 times cheaper**; generates sound from text or for a video. Untested |
| `sepal/audiogen` | ≈ $0.011 per run | Text to sound. Rejected once ("no blender sound"); 16 kHz |
| `declare-lab/tango` | ≈ $0.054 per run | Text to sound. Untested |
| `tencent/hunyuanvideo-foley` | ≈ $0.057 per run | Needs an already animated video; does not apply today |

## How much has been spent (estimate)

What Replicate's prediction list shows since the channel's work began (up to the first four videos), at list prices. **It is not your bill**: the real consumption is in Replicate's dashboard.

| Item | Predictions | Estimated cost |
| --- | --- | --- |
| `flux-2-pro` | 55 | **≈ $2.5 to $3.3** (with one reference each) |
| `stable-audio-2.5` | 3 | $0.60 |
| `qwen3-tts` | 18 (≈ 1,000 characters in the most recent) | **cents** |
| `gemini-3.1-flash-tts` | 6 | ≈ $0.1 |
| **Total** | 82 | **≈ $3.3 to $4.1** |

Later videos (Lemon cake ≈ $1.57, Bike stems ≈ $0.26, Chips ≈ $0.48) are recorded in their Status notes.

**What the numbers say:**

- **Voice hardly costs anything.** A whole script at $0.02 with qwen; even the most expensive voice (elevenlabs/v3 or minimax HD) costs ≈ $0.10. Testing voices is not what makes the channel expensive.
- **What costs is the image**, and above all **retries and experiments**: 55 image predictions for about 37 useful images. Changing model saves little (≈ $0.045 → $0.035 per image, ≈ 22 %); **avoiding retries saves a lot more**.
- **Sound at $0.20 per file is the most expensive per unit** and has an alternative ≈ 38 times cheaper.

## Usage notes

- **Replicate rate limit:** do not launch more than a few requests at once; the extra ones get a 429. Send in series with retries.
- Input parameters change by model: copy them from each one's *API* tab.
- Price sources: the *Pricing* section of each model page on Replicate, read on 3 Oct 2026. Prices may change.
