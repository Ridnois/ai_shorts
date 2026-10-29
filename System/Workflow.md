---
type: process
updated: 2026-10-28
status: v8 · 28 Oct 2026: frame audit from `_beats.txt`, stricter `check3d`; v7 · 28 Oct 2026: Anatomy figures (build, checks, budget); v6 · 27 Oct 2026: HyperFrames only (the Blender builder, motion.py and make_thumbnail.py were deleted), render at CRF 14, local sound kit and libraries, thumbnail as a page, ship discipline
---

# Workflow: stages, budget, files, commands

Rules for the content: [[Playbook]]. One run per video; the work is sequential.

**Note size ceilings** (words, enforced by `check_vault.py`): Script 2,700 · Upload 2,300 · Status 1,500. Leave out rejected-thread scoring (one line each), prompts once generated (the prediction log keeps the id), attribution tables (credits live in `_credits.jsonl` and the description), research prose that repeats the facts bank.

**Token discipline:** read `CLAUDE.md`, [[Playbook]], this note, `Analytics/Report.md`, then only the video's Status and Script; [[Design system]] before building, [[Style]] when writing text, [[Publish]] at P8. Never read Replicate results whole. Look at images in contact sheets.

## Stages and gates

**Clarify first:** a new-video request opens with one round of interactive multiple-choice questions (`AskUserQuestion`, 1 to 4, the agent's recommendation first), after reading the vault and before any spend: **angle** (always when an earlier video shares the topic), **real case**, **gate and delegation**, **visual approach**, the **length slot** only when unclear. The answers go verbatim into Status as its first line. A rerun or fix skips it.

**The normal run is delegated:** the agent records the delegation and the cap in Status and runs A to D without stopping; **it stops at the render (P7)**. Without delegation the user approves each gate. **Ship before you build:** at most two renders wait at P7 or P8 ([[Playbook]] §8).

| Package | Stages | Gate |
| --- | --- | --- |
| **A · Text** | idea (deep-first search, Y and X, real case, facts bank, scores, against-the-idea pass, demand check, five hooks) → research → script in words with its Package → beat sheet (one row per beat, camera and transition columns) | P1 to P3 + P4a; the street-lamp test cannot be "borderline" |
| **B · Budget** | captures and stock downloaded (free, credits), prompts, `plan.json`, dollar budget with cap (base × 1.2) | **P4: no paid call and no file in `Media/` before it** (delegation counts, written in Status) |
| **C · Generation** | voice (one take; check its words and silences) → word timings → recorded runs and captures → generated media (in series, if any) | within the cap |
| **D · Build** | `hf/build.py` → `hyperframes check` → `check3d.mjs` → snapshots → render (CRF 14) → `mix_audio.py` → contact sheet and slideshow-risk score → thumbnail → publish pack (`publish.py --dry-run`) | **P7: the user** (ship, fix or drop) |
| **E · Publish and measure** | `publish.py` (private by default), pulls at 24 h, 7 d, 28 d ([[Publish]]) | P8 |

A **test stage** (one scene's voice and one composed beat, about $0.10) runs only for a new technique, voice setting or model.

**Listening rubric at P7** (the agent cannot hear; answers go in Status under *Feedback*): (1) does the voice sound natural? (2) is the pace right? (3) do the pauses feel human: any wrong or missing? (scene and word) (4) are the effects and their levels right? (5) does any screen feel empty or static? (scene) (6) did any picture fail to show what was said, or arrive late? (scene and word) (7) after the first sentence, did you know what the video is about and want the explanation? (8) could you follow each sentence from the one before? (9) did the last line make you want to watch again, and did any stretch lose you (scene)? Each "no" becomes one change to the owning rule.

## Budget (in dollars, cap = base × 1.2, shown before spending)

| Category | Model or tool | Unit price |
| --- | --- | --- |
| Voice | `inworld/realtime-tts-2`, voice `Dennis`, one take (`voice.py`; 2,000 characters or fewer, `<break>` tags, bracketed direction, WAV 48 kHz) | $0.025 per 1,000 characters: a 750-character script is about $0.02 a take |
| Word timings | `vaibhavs10/incredibly-fast-whisper` via `word_timings.py` | about $0.01 per take |
| Generated stills (opt-in, 3 or fewer) | `openai/gpt-image-2` (`aspect_ratio` 2:3 or 9:16, png); fallback `gpt-image-1.5` | unconfirmed, budget about $0.25 at `high` |
| AI image-to-video (opt-in, on a real photo) | `lightricks/ltx-2.5-fast` (720p, 9:16, 4 s, no audio) | unconfirmed, about $0.12 a clip |
| Photo edit | `black-forest-labs/flux-kontext-pro` (edits a real photo, never restyles) | about $0.04 |
| Recorded runs | the real AI tool, recorded by hand (GNOME `Ctrl+Shift+Alt+R` or OBS) or as real terminal output | the run's own cost, logged in Status |
| Anatomy figure (the `anatomy` skill) | `System/anatomy/<name>/build.mjs`, local Node and Chrome | $0, agent time: a Figure (40 to 80 parts) is built within the P4 to P6 stretch; a Hero (2 to 4 hours) needs the user's yes at P4a |
| Stock, captures, Hairline, 3D, sound kit, render, mix | `stock_photos.py`, `stock_videos.py`, headless Chrome, Blender, HyperFrames, ffmpeg (local) | $0 |

Typical Short: about $0.05 (one take and one timing call). Retries are what cost: fix the prompt first, **one retry per image**, calls **in series** (the helper waits on HTTP 429), the prediction id logged at once (`scene · category · model · seed · used/discarded · id`); a hung download is `recover(id, dest)`, never regenerate. Read a model's schema free with `GET /v1/models/<owner>/<name>`.

Not used: ElevenLabs per-scene takes (stitched takes sounded broken), `qwen3-tts`, `stable-audio-2.5`, Manim (needs sudo for cairo and pango), the Blender video builder (retired 27 Oct 2026).

## Anatomy

For a physical machine ([[Playbook]] §3): invent the object whose working is the concept, list 40 to 80 parts, build with the skill's kit, then give it the pose contract (parameters in, part transforms out, pure of the page clock) so frames are deterministic. Gates before it is placed: the line check at 0, the preview read at 1x and zoomed in each pose the video uses, no part floating (every line ends on something), the figure's numbers equal the video's numbers. Say in Status that it is a schematic. The skill's own community-gallery publish step is never run for the channel. Update with `npx skills add wheresryan22/anatomy -a claude-code -y` and re-run each figure's `build.mjs`.

## Thumbnail

Shorts thumbnails show in search, the channel page, shelves and TV (a phone tile is about 168 px wide, cropped near 3:2), never in the swipe feed; there is no A/B test for Shorts. Rules [H]:

- **One focal image:** the real case or the anchor in its surprising state, drawn in the video's own look, so the click matches the video.
- **3 to 4 words** at 110 px or more (a number counts as a word), high contrast; picture and title complement each other, never the same sentence twice.
- **Safe band:** everything that matters inside x 40 to 1040, y 600 to 1320; no kicker, chips or logo.
- Built by `v.thumb(inner)` in `hf/build.py` (`hf/thumb.html` → `upload/thumb.jpg`); look at it at 168 px wide before the pack is made.

## Files

```
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/   Status · Script · Upload
Media/Week NN/<YYYY-MM-DD Day>/<Video>/    local, gitignored: plan.json · voice/ · hf/ (build.py, index.html, thumb.html, assets/) ·
                                           stock/ clips/ (+ _credits.jsonl) · render/ (+ _fx, _timeline.json, _sheet.jpg) · upload/
```

Week = calendar week Mon to Sun (Week 01 = 5 to 11 Oct 2026); the Day folder is the day the video was made. Every media file carries the video prefix: `<v>-take-v<n>.wav`, `<v>-s<nn>-<slug>.jpg`; renders `<v>-<seconds>s-9x16-r<n>.mp4`.

## Commands

| Need | Command |
| --- | --- |
| Voice | `python3 System/scripts/voice.py "Media/…/<Video>" --dry` (prints the request, $0), then without `--dry` |
| Word timings | `python3 System/scripts/word_timings.py "Media/…/<Video>"` |
| Stock photos, footage | `stock_photos.py search "<q>" --source openverse\|nasa\|commons`, `get …`; `stock_videos.py search … [--vertical]`, `get`, `look`, `cut` |
| Replicate | `System/scripts/replicate_helper.py` (`run`, `download`, `recover`), token in `.env` |
| New project | copy `hf/hyperframes.json`, `meta.json` and `package.json` from the last video's `hf/`, then write `hf/build.py` |
| Build | `python3 hf/build.py` (writes `index.html`, the effects stem, `_timeline.json`; prints transition warnings) |
| Check | `HYPERFRAMES_NO_TELEMETRY=1 npx --yes hyperframes@0.8.209 check --json` (in `hf/`), then `node System/scripts/check3d.mjs hf/index.html` (every 0.125 s: overlaps, `CLIPPED`, `OVERFLOW`, `TEXT OVER PICTURE`, small text, sparse frames) and the `WARN` lines of `build.py` |
| Look (frame audit) | `npx --yes hyperframes@0.8.209 snapshot --at "$(cat ../render/_beats.txt)"` (in `hf/`): `hfkit` writes `_beats.txt` with a time for every event and 0.45 s after it; read every contact sheet under `.hyperframes/artifacts/snapshots/`; a fault found on one frame is searched for on all the others, then added to `check3d` if it is a class |
| Render | `npx --yes hyperframes@0.8.209 render . -o ../render/<v>-<s>s-9x16-r<n>.mp4 -q delivery --crf 14` (in `hf/`, in the background; about 3 to 5 min for 40 s) |
| Mix and master | `python3 System/scripts/mix_audio.py "Media/…/<Video>"` (`--report` measures only) |
| Listen (numbers for the sound) | `python3 System/scripts/listen.py "Media/…/render/<v>.mp4"`: LUFS, true peak, silences, clipping; exit 1 on a failed target |
| Deeper listening (optional) | `earshot` (github.com/Leonxlnx/earshot, MIT, CPU, about 1.1 GB of models): `earshot describe <wav>`, `earshot critique <mp4>`. The user runs its README install; the agent never installs it unattended |
| Contact sheet | `ffmpeg -i render/<v>.mp4 -vf "fps=1/3,scale=270:-1,tile=8x3" -frames:v 1 render/_sheet.jpg` |
| Bitrate | `ffprobe -v error -select_streams v -show_entries stream=bit_rate -of csv=p=0 render/<v>.mp4` |
| Design system self-check | `python3 System/scripts/hfkit.py`; demo page: `python3 System/scripts/hfkit.py --demo <scratch dir>` |
| Anatomy figure | new: `/anatomy <the machine whose working is the concept>` (skill in `.claude/skills/anatomy`; read its `SKILL.md` and `references/craft.md` first), then keep the result in `System/anatomy/<name>/` with the pose contract of [[Design system]] *Anatomy figures*; look: `node System/anatomy/<name>/build.mjs --preview <t> --state='{"he":1}'` and a headless-Chrome screenshot of `preview.html` (read it at 1x and zoomed); line check: `CHROME_PATH=<chrome-headless-shell> node .claude/skills/anatomy/scripts/lines.mjs System/anatomy/<name>/preview.html` must print `line ends: 0` (and `node build.mjs --audit` where the figure has pipes or round parts); place: `K.anatomy` and `v.pose` |
| Hairline figure | `/hairline-create <idea>` (or `/hairline-adopt <svg>`), then move it into `vendor/hairline/custom/` and add its row in [[Design system]] |
| 3D | `hfkit.blender3d(spec, "assets/x.glb", dur, "glb")` inside `build.py` ([[Design system]] *3D routes*) |
| New colour | `node <dataviz skill>/scripts/validate_palette.js "#hex,…" --mode dark --surface "#0B0D17" --pairs all` |
| Upload (P8) and metrics | `python3 System/scripts/publish.py "Media/…/upload/publish.json"` ([[Publish]]) |
| Coherence | `python3 System/scripts/check_vault.py` |

Never `pkill -f` a pattern that appears in your own command. Obsidian re-pads Markdown tables on save: parse tolerantly.

## Status note template (`<Topic> - Status.md`, updated at every gate)

First line: the clarify answers, verbatim. Then:

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Beat sheet | | | angle, real case, hook type, theme line, demand check, street-lamp result, figure set |
| 4 Captures, budget | | | budget, cap, delegation |
| 5 Generation | | | prediction log |
| 6 Build | | | check results, transitions, shot sizes, slideshow-risk score, bitrate, `MIX` line |
| 7 Verdict · 8 Publish · 9 Measure | | | ship, fix or drop; upload id; *Learnings* per pull |

Plus *Not verified* and *Feedback* (the user's words verbatim, with the rubric answers).
