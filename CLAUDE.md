# Agent guide: the Next Token vault (`~/Documents/bussiness/ai_shorts`)

**Next Token** is an English, AI-assisted channel that teaches AI in 45 to 60 s vertical Shorts (YouTube, TikTok and Instagram Reels), Mon to Fri, in three series: **How AI works**, **Agent at work**, **What's coming**. The vault is the single source of knowledge: each rule has one owner note, and feedback (the user's or the retention curves') becomes an edit of that note ([[Data]] §Feedback loop). Everything is written in English.

## Read order

1. This file.
2. `System/Strategy.md` (audience, series, hook patterns, ideas, package, policy).
3. `System/Story.md` (the words).
4. `System/Picture.md` (medium, bar, pace).
5. `Analytics/Report.md` and `System/Data.md` §Review (what our numbers say).
6. The video's Status and Script.

On demand: `System/Build.md` (look, kit, budget, commands, checks, upload) before building; `Research/` (Channels, Instagram, Radar, Signals, Shots) when choosing an idea and before a beat sheet; `Pipeline/` for the idea queue.

## Skills (`.claude/skills/`)

- `/short <topic or idea>`: one video, end to end (ask once, idea, script and pre-flight, build, `qa.py`, master, pack, stop for review).
- `/short-idea`: ideas from the radar, signals and outliers; writes `Pipeline/Ideas/`.
- `/short-script`: the script, beat sheet and pre-flight card ([[Story]]).
- `/short-qa <video>`: `qa.py` plus one read of every frame, scored against [[Picture]] §Bar.
- `/short-publish <video>`: masters, the publish pack, upload after the user confirms, the numbers at 24 h and 7 d.
- Craft: `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `anatomy`, `hairline-create`, `hairline-adopt`.

## Hard rules

- **Ask once, then run:** a new video opens with one round of `AskUserQuestion`; the answers go verbatim into Status. Then the agent runs to the audited render and the publish pack, and **stops for the user's verdict** (ship, fix or drop; at most two revisions).
- **Money:** cap $2.00 a video (user, 3 Nov 2026), written in Status; voice and timings cost about $0.03. Generated stills and clips are for metaphor only ([[Picture]] §Medium). Replicate calls run in series and each prediction id is logged at once.
- **Build only with HyperFrames + `System/scripts/hfkit.py`** (the paper look, tokens, captions, camera, sound, the ML primitives), driven by the video's `hf/beats.json` through `System/scripts/beats.py`. Never fork a component in a video's builder; never bring back gradients, grain or thin lines.
- **Every upload uses the master** made by `System/scripts/master.py` (2160x3840 for YouTube, 1080x1920 for TikTok and Instagram). Never upload the raw render.
- **Voice:** `inworld/realtime-tts-2`, `Dennis`, one continuous take, never stitched. Mix to −14 LUFS, true peak −1 dBTP.
- **Honesty:** every number has a source and date; every AI claim names model, version and date; recorded runs are real, speed-ups marked, no keys or personal data. Say what you could not check: you cannot watch or hear a video; you read frames and numbers.
- **Upload private, only after the user confirms the publish pack.**
- **Done = `python3 System/scripts/check_vault.py` passes.**

## Gotchas that already cost time

- **Replicate:** 429 under bursts (the helper retries, nothing is charged). A hung download is recovered, never regenerated.
- **Downloads and scraping:**
  - Wikimedia thumbnails throttle: fetch originals from `upload.wikimedia.org`.
  - Kenney's site blocks scripted downloads: new sounds come from Openverse (CC0) or the `media-use` skill.
  - Reddit answers its JSON API with 403 and rate-limits its RSS feeds with 429 (`signals.py` waits and skips).
  - YouTube auto captions also rate-limit (`shots.py` keeps the storyboard and retries captions later).
  - ffmpeg garbles YouTube's WebP storyboard sprites: Pillow reads them.
- **Python:** system Python has no numpy (Blender's does). Manim lives in `System/.venv` (Python 3.12 via `uv`) and needs the cairo and pango headers (`manim.py` header).
- **Files:** `Media/` is local and gitignored. Obsidian re-pads tables.
- **Shell:**
  - Never `pkill -f` a pattern in your own command.
  - In zsh never name a variable `path`, do not rely on word splitting of `$var`, and quote globs (`--include='*.md'`).
  - ffmpeg's `adelay` only shifts timestamps (pad with `aresample=async=1:first_pts=0`).
- **YouTube scripts and auth:**
  - Run them from the vault root: they read `.env` from the working directory.
  - That `.env` needs `YT_CLIENT_ID`, `YT_CLIENT_SECRET` (OAuth client "Redtail Uploader", Google Cloud project `redtail-upload`) and one `YT_REFRESH_TOKEN`.
  - Every token goes through `youtube_auth.py`, which refuses any channel but NextToken (the Redtail channel renamed).
  - At consent the user picks the brand account **REDTAIL** (the picker's old name for NextToken), not the personal one.
  - The token expires weekly (HTTP 400: the user re-runs `python3 System/scripts/youtube_auth.py`; `daily.py` writes a banner in the Report).
- **Analytics API:** the retention query returns no rows if `startedWatching` or `stoppedWatching` is added.
- **The repo is public:** keys live only in `.env`. `secret_scan.py` (in `check_vault`, and as the pre-commit hook in `System/scripts/githooks`) blocks any key from a commit.
- **HyperFrames:**
  - Hairline animates on its own clock: always mount it through `hfkit`.
  - `hfkit` vendors GSAP, three.js and the fonts into `hf/assets`: no network at render.
  - Lint warns about nested structure and dense tracks: accepted.

## Map

```
CLAUDE.md · YouTube Channel.md (index, video table) · User insights.md (the user's research notes)
System/  Strategy · Story · Picture · Build · Data
         Brand/Next Token (brand.py, avatar, banner, mascot) · anatomy/ (figures) · assets/sfx (sound kit)
         scripts/ hfkit (+ ML primitives), beats, captions, master, voice, word_timings, mix_audio, listen, pace, check3d, qa,
                  capture, manim, shots, radar, signals, daily, publish, youtube_*, analytics, stock_*, replicate_helper,
                  scene3d, check_vault, secret_scan, githooks/, vendor/ (hairline, gsap, three, fonts)
Research/ Channels (watchlist) · Instagram (Reels watchlist) · Radar, Signals (generated) · Shots/ (reference shots) · radar.csv, signals.csv
Pipeline/ idea queue, Ideas/    Analytics/ csvs · exports/ · Report.md (generated)
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/   Status · Script · Upload        Media/… (local media, renders, masters, _research)
```
