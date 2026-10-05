---
type: process
updated: 2026-10-05
status: v1 · stages, gates, budget, models, files, commands in one note
---

# Workflow: stages, budget, models, files

Rules for the content: [[Playbook]]. One run per video, one Short a day; **Sonnet-class model, no subagents** (the work is sequential).

## Token discipline

Read `CLAUDE.md`, [[Playbook]], this note, `Analytics/Report.md`, then only the video's Status and script. Open [[Style]] when writing on-screen text, [[Publish]] at P8. Never read Replicate results whole (keep URL and a one-line log). Look at images in batches. One Status note per video holds stages, budget, prompts and the prediction log.

## Stages and gates

The user approves each gate; the agent proposes and never approves for them. If the user **delegates** ("carry on until the render"), write the delegation and the cap in Status and continue without stopping, within the cap; stop at the render (P7).

| Package | Stages | Gate |
| --- | --- | --- |
| **A · Text** | idea (facts bank, scores, five hooks) → research (claims with source and date) → script in words → visual plan (one row per plate) | P1 to P3 + P4a, one review |
| **B · Budget** | stock photos downloaded (free, credits), content-first prompts, voice prompts, `plan.json`, dollar budget with cap | **P4: spending allowed from here; no Replicate call and no file in `Media/` before it** |
| **C · Test** | voice of scene 1, one cutout and one stock photo composed in Blender (≈ $0.10 max) | P5 |
| **D · Generation** | by category: voice → word timings → images (in series) | P6 |
| **E · Edit** | `build_video.py`, `CHECK=1`, render in the background | **P7 (the user)** |
| **F · Publish and measure** | Upload note, `Analytics/videos.csv` row, pulls at 24 h, 7 d, 28 d ([[Publish]]) | P8 |

Every approval is written in the Status note (date, what). A change in an approved stage reopens the later ones. A new video request ends at P4 as text: Status note, research, script with visual plan, prompts, `plan.json`, budget.

## Budget (show in dollars with cap = base × 1.2 before spending)

| Category | Model | Unit price |
| --- | --- | --- |
| Voice | `elevenlabs/v3` | ≈ $0.10 per 1,000 characters |
| Generated plates (≤ 3) | `openai/gpt-image-2` (`quality` medium/high, `aspect_ratio` 2:3 or 9:16, `output_format: png`, `input_images`; no `input_fidelity`) | no price shown by the API: budget ≈ $0.10 each until measured (fallback `gpt-image-1.5` ≈ $0.05) |
| Stock photos | `System/scripts/stock_photos.py` | $0 |
| Background removal | `bria/remove-background` | unmeasured: test one |
| Photo edit | `black-forest-labs/flux-kontext-pro` (edits a real photo, never restyles) | ≈ $0.04 |
| Hard edit | `google/nano-banana-2` | ≈ $0.067 |
| Word timings | `vaibhavs10/incredibly-fast-whisper` via `word_timings.py` | ≈ $0.01 per take |
| Sound design | synthesized by the builder | $0 |

Typical Short: ≈ $0.40 to $0.50 (7 voice takes + 1 generated plate + 7 timings). Real references: Copper ≈ $0.41, Battery ≈ $0.35. Retries are what cost: fix the prompt first, **one retry per image**, calls **in series** (the helper waits on HTTP 429, nothing is charged), batches ≤ 10. Over the cap needs approval; model research is not video cost. Discards go to `_descartes/`. Log one line per prediction: `scene · category · model · seed · used/discarded · URL`; the prediction id is logged at once; a hung download is `recover(id, dest)`, never regenerate. Read a model's schema free with `GET /v1/models/<owner>/<name>`; urllib needs a `User-Agent`.

Not used: `qwen-image-edit-plus` to generate, `flux-2-pro`, `stable-audio-2.5` ($0.20 per file), `qwen3-tts` (no speed control).

## Thumbnail

Custom thumbnails work on this channel (API `thumbnails.set` or Studio). Hero image from `gpt-image-1.5` (≈ $0.05, no text in the prompt) plus text from `System/scripts/make_thumbnail.py` (1080×1920, content in the centre 3:2 band); three candidates, budgeted as a plate. The feed shows none: polish, not the lever.

## Files

```
Videos/Week NN/<Topic>/   Status · Script · Upload (+ Research if long)   (Week = calendar week Mon to Sun, Week 01 = 5 to 11 Oct 2026)
Media/Week NN/<Video>/    local, gitignored: voice/ plates/ (+_refs, _descartes) stock/ (+_credits.jsonl) sound/ upload/ plan.json render/
Media/_canal/             shared (brand drafts, tests)
```

Every media file carries its video prefix (Obsidian resolves embeds by file name): `<v>-p<nn>-v<n>.png`, `<v>-s<nn>-<slug>.jpg`, `<v>-e<scene>-voice-v<n>.mp3`; render `<v>-<duration>s-9x16-r<n>.mp4` (the builder names it). New week = new `Week NN` in both trees. A `.blend` keeps absolute paths.

## Commands

| Need | Command |
| --- | --- |
| Stock photos | `python3 System/scripts/stock_photos.py search "<q>" --source openverse\|nasa\|commons`, then `get …` (Commons: fetch originals from `upload.wikimedia.org`, the thumbnail API throttles) |
| Replicate | `System/scripts/replicate_helper.py` (`run`, `download`, `recover`), token in `.env` |
| Word timings | `python3 System/scripts/word_timings.py "Media/Week NN/<Video>"` |
| Assemble and check | `VIDEO="Media/Week NN/<Video>" SOLO_PROYECTO=1 CHECK=1 blender -b --factory-startup --python System/scripts/build_video.py` |
| Render | same without `SOLO_PROYECTO`, in the background (3 to 5 min) |
| Upload / metrics | [[Publish]] |
| Coherence | `python3 System/scripts/check_vault.py` |

Never `pkill -f` a pattern that appears in your own command (match with `ps` and `awk`). Obsidian re-pads Markdown tables on save: parse tolerantly. **Pipeline runner** (`~/Documents/youtube-pipeline/pipeline.py`, user service): its prompts name `CLAUDE.md`, [[Playbook]], this note and [[Style]]; state machine in [[Pipeline]].

## Status note template (`<Topic> - Status.md`, updated at every gate)

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan | | | angle, five hooks, hook type, theme line |
| 4 Prompts, stock, budget | | | budget table, cap, delegation if any |
| 5 Test · 6 Generation | | | prediction log |
| 7 Edit | | | render names, what was not verified |
| 8 Publish · 9 Measure | | | upload id; *Learnings* per pull |

Plus: attribution table (from `stock/_credits.jsonl`), known simplifications of schematics, *Feedback* (user's words verbatim).
