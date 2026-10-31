# Agent guide: the Next Token vault (`~/Documents/bussiness/ai_shorts`)

**Next Token** is an English, AI-assisted channel that teaches AI in 45 to 60 s vertical Shorts (YouTube and TikTok), Mon to Fri, in three series: **How AI works**, **Agent at work**, **What's coming**. The vault is the single source of knowledge; feedback becomes an edit of the rule that owns it ([[Feedback loop]]). Everything is written in English.

## Read order

1. This file. 2. `System/Format.md` (what a Short is; read it whole before writing). 3. `System/Production.md` (stages, commands, checks). 4. `Analytics/Report.md` before choosing an idea. 5. The video's Status and Script.
On demand: `System/Look.md` (brand, design system, motion, sound) before building; `System/Growth.md` (audience, ideas, package, upload, policy, numbers) when choosing an idea and at upload; `Pipeline/` for the idea queue.

## Skills (`.claude/skills/`)

- `/short <topic or idea>`: one video, end to end (ask once, idea, script, build, checks, master, pack, stop for review).
- `/short-idea`: find and score ideas from outliers; writes `Pipeline/Ideas/`.
- `/short-script`: write or fix a script to [[Format]] §3.
- `/short-qa <video>`: audit a render (frames, layout, sound, encode) and score it against [[Format]] §4.
- `/short-publish <video>`: masters, the publish pack, upload after the user confirms, analytics pulls.
- Craft: `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `anatomy`, `hairline-create`, `hairline-adopt`.

## Hard rules

- **Ask once, then run:** a new video opens with one round of `AskUserQuestion`; the answers go verbatim into Status. Then the agent runs to the audited render and the publish pack, and **stops for the user's verdict** (ship, fix or drop; at most two revisions).
- **Money:** default cap $0.50 a video, written in Status; voice and timings cost about $0.03. Anything else paid is asked first. Replicate calls run in series and each prediction id is logged at once.
- **Build only with HyperFrames + `System/scripts/hfkit.py`** (the paper look, tokens, captions, camera, sound), driven by the video's `hf/beats.json` through `System/scripts/beats.py`. Never fork a component in a video's builder; never bring back gradients, grain or thin lines.
- **Every upload uses the master** made by `System/scripts/master.py` (2160x3840 for YouTube, 1080x1920 for TikTok). Never upload the raw render.
- **Voice:** `inworld/realtime-tts-2`, `Dennis`, one continuous take, never stitched. Mix to −14 LUFS, true peak −1 dBTP.
- **Honesty:** every number has a source and date; every AI claim names model, version and date; recorded runs are real, speed-ups marked, no keys or personal data. Say what you could not check: you cannot watch or hear a video; you read frames and numbers.
- **Upload private, only after the user confirms the publish pack.**
- **Done = `python3 System/scripts/check_vault.py` passes.**

## Gotchas that already cost time

Replicate 429 under bursts (the helper retries, nothing is charged); a hung download is recovered, never regenerated. Wikimedia thumbnails throttle (fetch originals from `upload.wikimedia.org`). System Python has no numpy (Blender's does). `Media/` is local and gitignored. Never `pkill -f` a pattern in your own command. Obsidian re-pads tables. In zsh never name a variable `path`, do not rely on word splitting of `$var`, and quote globs (`--include='*.md'`). ffmpeg's `adelay` only shifts timestamps (pad with `aresample=async=1:first_pts=0`). The YouTube scripts read `.env` from the working directory: run them from the vault root; that `.env` needs `YT_CLIENT_ID`, `YT_CLIENT_SECRET` (OAuth client "Redtail Uploader", Google Cloud project `redtail-upload`) and one `YT_REFRESH_TOKEN`. Every token goes through `youtube_auth.py`, which refuses any channel but NextToken (the Redtail channel renamed); at consent the user picks the brand account **REDTAIL** (the picker's old name for NextToken), not the personal one. The token expires weekly (HTTP 400: the user re-runs `python3 System/scripts/youtube_auth.py`). The repo is public: keys live only in `.env`; `secret_scan.py` (in `check_vault`, and as the pre-commit hook in `System/scripts/githooks`) blocks any key from a commit. Hairline animates on its own clock: always mount it through `hfkit`. `hfkit` vendors GSAP, three.js and the fonts into `hf/assets`: no network at render. HyperFrames lint warns about nested structure and dense tracks: accepted. Kenney's site blocks scripted downloads: new sounds come from Openverse (CC0) or the `media-use` skill.

## Map

```
CLAUDE.md · YouTube Channel.md (index, video table) · User insights.md (the user's research notes)
System/  Format · Look · Production · Growth · Feedback loop
         Brand/Next Token (brand.py, avatar, banner, mascot) · anatomy/ (figures) · assets/sfx (sound kit)
         scripts/ hfkit, beats, captions, master, voice, word_timings, mix_audio, listen, check3d, publish, youtube_*, analytics,
                  stock_*, replicate_helper, scene3d, check_vault, secret_scan, githooks/, vendor/ (hairline, gsap, three, fonts)
Pipeline/ idea queue, Niche map, Ideas/    Analytics/ csvs · Report.md (generated)
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/   Status · Script · Upload        Media/… (local media, renders, masters)
```
