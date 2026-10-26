---
type: process
updated: 2026-10-26
status: v5 · 3D plates (`scene3d.py`) and recorded runs for the AI channel (23 Oct 2026); v4 · one-take voice and mix-and-master stage (9 Oct 2026); footage and motion plates; delegated flow is the default; listening rubric; note size ceilings
---

# Workflow: stages, budget, models, files

Rules for the content: [[Playbook]]. One run per video, five Shorts a week at a fixed time; **Sonnet-class model, no subagents** (the work is sequential).

**Note size ceilings** (words, enforced by `check_vault.py`): Script 2,700 · Upload 2,300 · Status 1,500 (ceilings set from today's notes; lower them as notes shrink). Leave out: scoring rows of rejected threads (one line each), prompts once generated (the prediction log keeps the id), attribution tables (credits live in `stock/_credits.jsonl` and the Upload description), research prose that repeats the facts bank.

## Token discipline

Read `CLAUDE.md`, [[Playbook]], this note, `Analytics/Report.md`, then only the video's Status and script. Open [[Style]] when writing on-screen text, [[Publish]] at P8. Never read Replicate results whole (keep URL and a one-line log). Look at images in batches. One Status note per video holds stages, budget, prompts and the prediction log.

## Stages and gates

**The normal run is delegated:** the user asks for a video, the agent records the delegation and the cap in Status and runs A to E without stopping; **the render (P7) is where it stops.** Without delegation the user approves each gate and the agent never approves for them.

| Package                     | Stages                                                                                                                                                                  | Gate                                                                                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **A · Text**                | idea (deep-first search, Y and X, facts bank, scores, against-the-idea pass, demand check, five hooks) → research (claims with source and date) → script in words **with its Package (title, thumbnail, promise)** → visual plan (one row per plate) | P1 to P3 + P4a; the street-lamp test cannot be "borderline"                                                                                |
| **B · Budget**              | stock photos downloaded (free, credits), content-first prompts, voice prompts, `plan.json`, dollar budget with cap                                                      | **P4: spending allowed from here; no Replicate call and no file in `Media/` before it** (delegation counts as approval, written in Status) |
| **C · Generation** | voice (`voice.py`: one take, check its words and silences) → word timings → build with `SOLO_PROYECTO=1` (writes `render/_timeline.json`) → motion plates (`motion.py --sheet`) and 3D plates (`scene3d.py --preview --sheet`, then without `--preview`; look at every sheet) → recorded runs and footage cut (`stock_videos.py cut`) → generated images or clips (in series) | within the cap |
| **D · Edit** | `build_video.py`, `CHECK=1`, render in the background, then `mix_audio.py` (mix and master to −14 LUFS) | **P7 (the user)**, with the listening rubric below |
| **E · Publish and measure** | Upload note, `Analytics/videos.csv` row, pulls ([[Publish]])                                                                                                            | P8                                                                                                                                         |

A **test stage** (voice of scene 1, one cutout and one stock photo composed, ≈ $0.10) is run only when a new technique, voice setting or model is tried; routine videos skip it. A change in an approved stage reopens the later ones. A new video request without delegation ends at P4 as text: Status note, research, script with visual plan, prompts, `plan.json`, budget.

**Listening rubric at P7:** the agent cannot hear, so the user answers eight short questions and the answers are written in Status under *Feedback*: (1) does the voice sound natural? (2) is the pace right (too fast, right, too slow)? (3) **do the pauses feel human: any that comes where it should not, or is missing where it should be?** (write the scene and the word) (4) is the sound mix right (effects and bed against the voice)? (5) **does any screen feel empty?** (write the scene) (6) **did any picture fail to show what was being said, or arrive late?** (write the scene and the word) (7) **after the first sentence, did you know what the video is about and want the explanation?** (8) **could you follow each sentence from the one before?** These are the only evidence the vault has; each "no" becomes a change to the pause plan or the plate before the next video.

## Budget (show in dollars with cap = base × 1.2 before spending)

| Category               | Model                                                                                                                               | Unit price                                                                                                                                                                                                          |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Voice | `inworld/realtime-tts-2`, voice `Dennis`, one take per video (`voice.py`; ≤ 2,000 characters, `<break>` tags, bracketed direction, WAV 48 kHz; no timestamps) | $0.025 per 1,000 characters (model page, 9 Oct 2026): a 750-character script ≈ $0.02 a take |
| Generated plates (≤ 3) | `openai/gpt-image-2` (`quality` medium/high, `aspect_ratio` 2:3 or 9:16, `output_format: png`, `input_images`; no `input_fidelity`) | **unconfirmed**: the API shows no price; budget ≈ $0.25 at `high` until the user reads the Replicate dashboard once and the real figure replaces this line (fallback `gpt-image-1.5` ≈ $0.05) |
| Stock photos and footage | `stock_photos.py`, `stock_videos.py` (Commons keyless; Pexels and Pixabay need the user's free `PEXELS_API_KEY`, `PIXABAY_API_KEY` in `.env`) | $0 |
| Motion plates | `motion.py` (cairo, local) | $0 |
| 3D plates | `scene3d.py` (Blender 5.2 EEVEE, local; measured 23 Oct 2026 on this laptop: 0.75 to 1.7 s a frame at 1080×1920 (a landscape with a 96-cell grid is the slow end), 0.3 to 0.4 s with `--preview`; 30 s of 3D took about 18 minutes) | $0 |
| Recorded runs | the real AI tool, screen-recorded by hand (GNOME recorder `Ctrl+Shift+Alt+R` or OBS) or by the agent in the terminal | the run's own API or subscription cost, logged in Status as a line like any prediction |
| AI image-to-video (opt-in, ≤ 3 generated media per Short in all) | `lightricks/ltx-2.5-fast` (`image` start frame cropped to 720×1280, `resolution` 720p, `aspect_ratio` 9:16, `duration` 4, `generate_audio` false); fallback `bytedance/seedance-1.5-pro` (`camera_fixed`, `generate_audio` false) | **unconfirmed**: ≈ $0.12 and ≈ $0.10 per 4 s clip (model pages, 9 Oct 2026); a test of 2 photos on 3 models (≈ $0.70, the user's approval) comes before any clip enters a Short |
| Background removal     | `bria/remove-background`                                                                                                            | **unconfirmed**: test one and write the price                                                                                                                                                                       |
| Photo edit             | `black-forest-labs/flux-kontext-pro` (edits a real photo, never restyles)                                                           | ≈ $0.04                                                                                                                                                                                                             |
| Hard edit              | `google/nano-banana-2`                                                                                                              | ≈ $0.067                                                                                                                                                                                                            |
| Word timings | `vaibhavs10/incredibly-fast-whisper` via `word_timings.py` (a WAV take is sent as a 32 kbps Opus copy) | ≈ $0.01 per take (one per video) |
| Sound design and master | the builder's opening hit and scene whooshes; `mix_audio.py` (ffmpeg) mixes and masters; music opt-in, Pixabay by hand (shield-free) | $0 |

Typical Short since 9 Oct 2026: ≈ $0.05 without generated media (one voice take + one timing call; a retake ≈ $0.02), ≈ $0.30 with one generated plate. Retries are what cost: fix the prompt first, **one retry per image**, calls **in series** (the helper waits on HTTP 429, nothing is charged), batches ≤ 10. Over the cap needs approval; model research is not video cost. Discards go to `_descartes/`. Log one line per prediction: `scene · category · model · seed · used/discarded · URL`; the prediction id is logged at once; a hung download is `recover(id, dest)`, never regenerate. Read a model's schema free with `GET /v1/models/<owner>/<name>`; urllib needs a `User-Agent`.

Not used: `qwen-image-edit-plus` to generate, `flux-2-pro`, `stable-audio-2.5` ($0.20 per file), `qwen3-tts` (no speed control), ElevenLabs turbo-v2.5 per-scene takes (retired 9 Oct 2026: stitched takes sounded broken); Eleven v4 needs an ElevenLabs key ($6 a month, not chosen); **Manim** (tried 23 Oct 2026: needs `libcairo2-dev` and `libpango1.0-dev`, which need sudo on this machine; ask the user to install them only if a video needs equations or 3Blue1Brown-style math, `scene3d.py` and `motion.py` cover the rest).

## Thumbnail

**Designed at the script phase** (Package section of the Script note, [[Playbook]] §2b, rules in [[Audience]]); built here once the plates exist. Redesigned 9 Oct 2026 (user: *"rethink how do you do the thumbnail, forget about what i told you and make a fast and efficient research about youtube thumbnails, and the redo it"*). **Evidence** (secondary sources, read 9 Oct 2026): Shorts thumbnails never show in the swipe feed, only in search, the channel page, home shelves, subscriptions and TV, small (a phone tile is about 168 px wide) and near 3:2 (ppc.land, July 2026); Shorts have no A/B test; breakout thumbnails use one focal subject, high contrast and a median of five words or fewer (vidIQ 2026, 500 videos; faces in 69 %, but tech viewers look for the thing, not a presenter); title and thumbnail come first and set the expectation the video must meet (MrBeast production guide, 2024); educational thumbnails win on clarity: show the subject and the viewer's question, not a hidden answer. **Rules [H]:**

- **One focal image: the anchor in its surprising state** (the hook frame redrawn big: the chart jumping, the bar dropping), drawn with `motion.py` elements in the video's own look so the click matches the video; a real photo only when it shows the subject doing the surprising thing.
- **At most 3 to 4 words** (a number counts as a word), 110 px or more, high contrast. **Thumbnail and title complement each other:** the picture carries the surprise, the title the cause and the search words; never the same sentence twice.
- **Safe band:** everything that matters inside x 40 to 1040, y 600 to 1320; the rest is ground (mobile shelves lay the title over the bottom of the tile).
- **No kicker, chips, logo or brand mark** (the channel avatar sits beside it; small text is unreadable at tile size). Retired 9 Oct 2026: hero photo + two-line title + kicker + three chips + Redtail mark.
- **Look at it at 168 px wide and in the 3:2 crop** before the pack is made; `make_thumbnail.drawn` warns on words, size and band.
- Built by `publish.py` from `publish.json` `thumb: {"bg": "ink", "els": [...]}` (`--dry-run` makes it and the pack); custom thumbnails are set through the API after processing. No A/B test exists for Shorts: compare impressions click-through between videos in the analytics loop ([[Publish]]).

## Files

```
Videos/Week NN/<Day>/<Topic>/   Status · Script · Upload (+ Research if long)   (Week = calendar week Mon to Sun, Week 01 = 5 to 11 Oct 2026; **Day folder** = the day the video was made, named `YYYY-MM-DD Day`, e.g. `2026-10-05 Mon`; user, 6 Oct 2026)
Media/Week NN/<Day>/<Video>/    local, gitignored (same Day folder as the video's note): voice/ plates/ (+_refs, _descartes) stock/ (+_credits.jsonl) clips/ (+_src/ sources, _credits.jsonl) motion/ (clips and `.sheet.png` from `motion.py` and `scene3d.py`) sound/ upload/ (+ `<prefix>-publish-pack.md`: thumbnail, title, description, pinned comment, TikTok caption to copy, [[Publish]] §Publish pack) plan.json render/
Media/_canal/             shared (brand drafts, tests)
```

Every media file carries its video prefix (Obsidian resolves embeds by file name): `<v>-p<nn>-v<n>.png`, `<v>-s<nn>-<slug>.jpg`, `<v>-e<scene>-voice-v<n>.mp3`; render `<v>-<duration>s-9x16-r<n>.mp4` (the builder names it). New week = new `Week NN`, new day = new `<Day>` folder, in both trees. A `.blend` keeps absolute paths.

## Commands

| Need               | Command                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stock photos       | `python3 System/scripts/stock_photos.py search "<q>" --source openverse\|nasa\|commons`, then `get …` (Commons: fetch originals from `upload.wikimedia.org`, the thumbnail API throttles) |
| Replicate          | `System/scripts/replicate_helper.py` (`run`, `download`, `recover`), token in `.env`                                                                                                      |
| Voice | `python3 System/scripts/voice.py "Media/Week NN/<Day>/<Video>" --dry` (prints the request, $0), then without `--dry` |
| Word timings       | `python3 System/scripts/word_timings.py "Media/Week NN/<Day>/<Video>"` |
| Footage | `python3 System/scripts/stock_videos.py search "<q>" --source commons\|pexels\|pixabay\|nasa\|archive [--vertical]`, then `get …`, `look <src>` (frames with timestamps), `cut <src> <clips/…mp4> --start s --dur s --focus x` |
| 3D plates | `python3 System/scripts/scene3d.py "Media/Week NN/<Day>/<Video>" --preview --sheet` (after a `SOLO_PROYECTO=1` build; drafts at half size), then without `--preview` for the final clips; `--only <name>` for one plate |
| Recorded run | record the real tool in a tall window at a large font into `clips/_src/<v>-run-<slug>.mp4`, then `stock_videos.py look` and `cut … --focus` like footage; mark speed-ups with a `card` or callout |
| Motion plates | `python3 System/scripts/motion.py "Media/Week NN/<Day>/<Video>" --sheet` (after a `SOLO_PROYECTO=1` build; `--only <name>` for one plate) |
| Assemble and check | `VIDEO="Media/Week NN/<Day>/<Video>" SOLO_PROYECTO=1 CHECK=1 blender -b --factory-startup --python System/scripts/build_video.py`                                                               |
| Render             | same without `SOLO_PROYECTO`, in the background (1.5 to 5 min) |
| HyperFrames (trial since 26 Oct 2026, instead of Blender) | HTML + GSAP rendered by headless Chrome (`npx hyperframes`, Node 22+, Apache 2.0); first used on [[ThinkPad TrackPoint - Status]]. `hf/build.py` writes `index.html` from the take's words; `HYPERFRAMES_NO_TELEMETRY=1 npx hyperframes check`, `snapshot --at …`, `render hf -o render/<v>-<s>s-9x16-r<n>.mp4 -q delivery` (about 3 min for 62 s here); `render/_timeline.json` is written by hand so `mix_audio.py` works unchanged. Its defaults ban dark grounds and glow; [[Style]] wins |
| Mix and master     | `python3 System/scripts/mix_audio.py "Media/Week NN/<Day>/<Video>"` (replaces the render's sound; `--report` measures only) |
| Upload (P8) / metrics | `python3 System/scripts/publish.py "Media/Week NN/<Day>/<Video>/upload/publish.json"` ([[Publish]]) |
| New colour         | `node <dataviz skill>/scripts/validate_palette.js "#hex,..." --mode dark --surface "#0B0D17" --pairs all` (the dataviz skill; every check must pass before a colour enters [[Style]]) |
| Coherence          | `python3 System/scripts/check_vault.py`                                                                                                                                                   |

Never `pkill -f` a pattern that appears in your own command (match with `ps` and `awk`). Obsidian re-pads Markdown tables on save: parse tolerantly. **Pipeline runner** (`~/Documents/youtube-pipeline/pipeline.py`, user service): its prompts name `CLAUDE.md`, [[Playbook]], this note and [[Style]]; state machine in [[Pipeline]].

## Status note template (`<Topic> - Status.md`, updated at every gate)

| Stage                                           | Status | Approved (date) | Note                                                                            |
| ----------------------------------------------- | ------ | --------------- | ------------------------------------------------------------------------------- |
| 0 Idea · 1 Research · 2 Script · 3 Visual plan  |        |                 | angle, hook type, theme line, demand check, street-lamp result (pass or reason) |
| 4 Prompts, stock, budget                        |        |                 | budget table, cap, delegation if any                                            |
| 5 Test (only if a new technique) · 6 Generation |        |                 | prediction log                                                                  |
| 7 Edit                                          |        |                 | render names, what was not verified                                             |
| 8 Publish · 9 Measure                           |        |                 | upload id; *Learnings* per pull                                                 |

Plus: known simplifications of schematics, *Not verified*, *Feedback* (user's words verbatim, with the listening-rubric answers). No attribution table: credits are in `stock/_credits.jsonl` and the Upload description.
