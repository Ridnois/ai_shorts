---
name: short-publish
description: Ship a reviewed Next Token Short - build the YouTube 4K and TikTok masters, write publish.json and the publish pack, upload privately or scheduled after the user confirms, and read the numbers at 24 h, 7 d and 28 d against the pre-flight prediction. Use when the user says ship, upload, publish, schedule, post, or asks for numbers on uploaded videos.
---

# /short-publish: masters, pack, upload, numbers

Rules: `System/Strategy.md` §Package and §Policy, `System/Build.md` §Upload, `System/Data.md`. Run from the vault root unless a step says otherwise.

## 1. Pack (no upload yet)

1. Masters: `python3 System/scripts/master.py "Media/…/render/<v>-r<n>.mp4"` (writes `upload/<stem>-yt.mp4` 2160x3840 and `-tt.mp4` 1080x1920). Never upload the raw render.
2. `upload/publish.json` (keys in the header of `System/scripts/publish.py`): `media`, `render`, `video_name`, `title`, `alt_titles`, `claim`, `sources`, `caveats`, `hashtags`, `tags`, **`series`, `hook_pattern`, `medium`**, `pinned`, `tiktok`, `synthetic` (true only for realistic generated media), `privacy` ("private"), optional `publish_at` (Mon to Fri, the channel's fixed hour, never two on one day).
3. `python3 System/scripts/publish.py "<publish.json>" --dry-run` writes `upload/<v>-publish-pack.md`. Show the user the title, the description's first two lines, the thumbnail path, the visibility and the date. **Wait for a clear yes.**

## 2. Upload (after the yes; one attempt, then hand over)

- Run `publish.py "<publish.json>"` from the vault root, in the background: processing can take over 10 minutes. If the `YT_*` keys are missing from `.env`, stop and ask.
- On HTTP 400 or `invalid_grant`, the weekly token has expired. Ask the user to run `python3 System/scripts/youtube_auth.py` and pick the brand account REDTAIL, then use `--resume <id>` if the video was already uploaded. "Wrong YouTube channel" means the wrong pick at consent: same fix, and nothing was uploaded.
- Report its lines: the id, the master's probe line, the thumbnail result, `check_vault`.
- TikTok: hand the user `upload/*-tt.mp4` and the pack's caption (posted by hand from TikTok Studio on the web, no library sound). TikTok numbers are not tracked.

## 3. Numbers

- The daily job ([[Build]] §Schedule) pulls everything. By hand: `youtube_analytics.py pull` then `analytics.py report`.
- **At 24 h and 7 d**, ask the user in one line for **viewed vs swiped** from Studio (Content › Shorts), and type it: `analytics.py add "<Video>" youtube 7d viewed_pct=<n>`.
- **At 7 d:** run `analytics.py beats "<Video>"`, look at the two drop frames, and write one *Numbers* line in Status: engaged views against the median, viewed vs swiped, hold at 3 s, the two drops (word and beat), and the pre-flight prediction marked hit or miss.
- Under 100 views, change nothing. Every 10 uploads, run the [[Data]] §Review.
