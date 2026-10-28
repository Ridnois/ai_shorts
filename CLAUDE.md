# Agent guide: Inside the Model vault (`~/Documents/ai_shorts`)

English AI-assisted channel that **teaches AI** in three series: **How it works**, **Agent at work**, **What's coming** ([[Audience]]). Vertical Shorts for YouTube and TikTok, five a week at a fixed time, never two on one day. The vault is the single source of knowledge: read the notes, follow them, and turn **feedback into an edit of the owning rule** ([[Feedback loop]]). Everything is written in English.

## Read order (every task)

1. This file. 2. `System/Playbook.md` (every content rule; read it whole before writing). 3. `System/Workflow.md` (stages, budget, commands). 4. `Analytics/Report.md` before choosing an idea, hook or length. 5. The video's Status and Script (`Videos/Week NN/<Day>/<Topic>/`).
On demand: `System/Audience.md` (niche, cases, plain words, search, package) when choosing an idea; `System/Design system.md` (look, zones, camera, transitions, components, sound kit) before building; `System/Style.md` (brand, persona, banned words) when writing text; `System/Publish.md` at P8; `Pipeline/Pipeline.md` for the idea queue. Craft reference: the `hyperframes` skills in `.claude/skills/`.

## Hard rules

- **Clarify first:** a new-video request opens with one round of `AskUserQuestion` (angle, real case, gate and delegation, visual approach); answers verbatim in Status.
- **No paid call and no media before P4** (budget approved in dollars, cap base × 1.2). Under delegation, record it in Status and run to the render; **stop at P7**. Replicate calls in series, one retry per image, prediction id logged at once.
- **The idea is a gate:** Y and X named, a named real case, facts bank of 15 or more, scores, street-lamp and expert tests ("borderline" = fail), demand check, five hooks of different types, variety guard.
- **Script:** length in words (short test block: 90 to 140, every third 60 to 85); the twist is the first words and passes the hook test; one running example; connection and cut tests; concrete payoff and one social question. Package (title, thumbnail, promise) written in the Script note.
- **Visuals at the bar of the feed:** show the verb; real captures and recorded runs for real things, Hairline figures with callouts for mechanisms, 3D only where depth explains; the subject fills the frame; the camera moves inside worlds (3 or more shot sizes); transitions with a cause (3 to 5 kinds, at most a third hard cuts); an event every 1.5 to 2 s; no AI clichés; no branding inside the video.
- **Build only with HyperFrames + `System/scripts/hfkit.py`;** never fork a component in a video's builder. Render at `--crf 14`.
- **Voice:** `inworld/realtime-tts-2`, `Dennis`, one continuous take, never stitched or cut. **Sound:** effects from the kit with a cause on screen, one payoff riser and hit, music opt-in; every render mixed by `mix_audio.py` to −14 LUFS, true peak −1 dBTP or lower.
- **Rigor and honesty:** every figure has source and date; every AI claim names model, version and date; demos are real runs, speed-ups marked, no key or personal data; say what you could not check (you cannot hear audio or watch a whole video).
- **Ship discipline:** the user's P7 verdict is ship, fix or drop; at most two revisions after r1; at most two renders wait at P7/P8 before a new video. Upload private, only after the user confirms the publish pack.
- **Notes live in the vault** (Markdown), short (ceilings in [[Workflow]]); delete obsolete notes instead of archiving; one Status note per video.
- **Done = `python3 System/scripts/check_vault.py` passes.**

## Gotchas that already cost time

Replicate 429 under bursts (the helper retries, nothing is charged); a hung download is recovered, never regenerated; Wikimedia thumbnails throttle (fetch originals from `upload.wikimedia.org`); system Python has no numpy (Blender's does); `Media/` is local and gitignored; never `pkill -f` a pattern in your own command; Obsidian re-pads tables; in zsh never name a variable `path` and do not rely on word splitting of `$var`; ffmpeg's `adelay` only shifts timestamps (pad with `aresample=async=1:first_pts=0`). The YouTube scripts read `.env` from the working directory: run them from `~/Documents/youtube` with the script's absolute path; refresh tokens expire weekly (HTTP 400: the user re-runs `youtube_analytics.py auth`). You cannot watch a clip: look at `snapshot` contact sheets and frames of the final mp4, not only the page. Hairline animates on its own clock: always through `hfkit` (it rewrites the clock so frames are deterministic). `hfkit` copies GSAP, three.js and the fonts into `hf/assets`: no network at render. HyperFrames lint warns about nested structure and dense tracks: accepted (the vault does not edit in Studio). Kenney's site blocks scripted downloads: new sounds come from Openverse (CC0) or the HyperFrames media-use library.

## Map

```
CLAUDE.md · YouTube Channel.md (index, video table)
System/  Playbook · Workflow · Design system · Style · Audience · Publish · Feedback loop · Model script
         assets/sfx (sound kit) · Brand/Inside the Model · scripts/ (hfkit, captions, check3d, voice, word_timings, mix_audio,
         publish, youtube_*, analytics, stock_*, replicate_helper, scene3d, check_vault, vendor/: hairline, gsap, three, fonts)
Pipeline/ idea queue, Niche map    Analytics/ csvs · Report.md (generated) · Reports/
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/ Status · Script · Upload      Media/Week NN/<YYYY-MM-DD Day>/<Video>/ local media
```
