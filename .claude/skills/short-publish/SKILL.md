---
name: short-publish
description: Ship a reviewed Next Token Short - build the YouTube 4K and TikTok masters, write publish.json and the publish pack, upload privately or scheduled after the user confirms, and pull analytics at 24 h, 7 d and 28 d. Use when the user says ship, upload, publish, schedule, post, or asks for numbers on uploaded videos.
---

# /short-publish: masters, pack, upload, numbers

Rules: `System/Growth.md` (§Package, §Publish, §Policy, §Analytics). Run from the vault root unless a step says otherwise.

## 1. Pack (no upload yet)

1. Masters: `python3 System/scripts/master.py "Media/…/render/<v>-r<n>.mp4"` (writes `upload/<stem>-yt.mp4` 2160x3840 and `-tt.mp4` 1080x1920). Never upload the raw render.
2. `upload/publish.json` (keys in the header of `System/scripts/publish.py`): `media`, `render`, `video_name`, `title` (search words first), `alt_titles`, `claim` (first line of the description, with the search words), `sources`, `caveats`, `hashtags` (2 to 3: `#AI` plus a topic tag), `tags` (5 to 10 search phrases), `hook_type`, `pinned` (one question), `tiktok` (caption with the keyword), `synthetic` (true only for realistic generated media), `privacy` ("private"), optional `publish_at` (Mon to Fri, the channel's fixed hour, never two on one day).
3. `python3 System/scripts/publish.py "<publish.json>" --dry-run` → `upload/<v>-publish-pack.md`. Show the user the title, the description's first two lines, the thumbnail path, the visibility and the date. **Wait for a clear yes.**

## 2. Upload (after the yes)

- Run `publish.py "<publish.json>"` from the vault root (its `.env` must hold the `YT_*` keys; if they are missing, stop and ask the user to add them, see [[Growth]] §Publish), in the background: processing can take over 10 minutes.
- On HTTP 400 or `invalid_grant`: the refresh token expired (weekly); ask the user to run `python3 System/scripts/youtube_auth.py` and pick the NextToken brand channel, then `--resume <id>` if the video was already uploaded. "Wrong YouTube channel" means the wrong pick at consent: same fix, nothing was uploaded.
- Report its lines: the id, the master's probe line, the thumbnail result, `check_vault`.
- TikTok: hand the user `upload/*-tt.mp4` and the pack's caption (posted by hand from TikTok Studio on the web, no library sound).
- First 4K upload only: ask the user to open "Stats for nerds" on the private video and read the codec (`vp09`/`av01` good, `avc1` not); write it in `System/Growth.md` §Publish.

## 3. Numbers

- At about 24 h, 7 d and 28 d: `python3 System/scripts/youtube_analytics.py pull` then `python3 System/scripts/analytics.py report`; TikTok numbers the user reads out go in with `analytics.py add`.
- Read `Analytics/Report.md` against [[Growth]] §Algorithm: viewed vs swiped (hook), average percentage viewed (middle and length), replays (loop). Under 100 views, change nothing.
- Write one *Numbers* line in the video's Status. Every 10 uploads run the [[Feedback loop]] on the data.
