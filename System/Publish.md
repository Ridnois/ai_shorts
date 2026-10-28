---
type: process
updated: 2026-10-28
status: v2 · 27 Oct 2026: trimmed; the thumbnail is a prebuilt page snapshot; the hypotheses the analytics loop judges live here
---

# Publish and measure (P8 and after)

Five Shorts a week (Mon to Fri) at one fixed time of day, never two on one day; "New Shorts every day." in every description. **Confirm title, description, thumbnail and visibility with the user before any upload.**

## Policy that can sink the channel (YouTube Help; re-read quarterly)

- **Inauthentic content** (since 15 July 2025) is not monetizable: content that is "mass-produced, generic, repetitive", that "feels interchangeable from video to video", or "AI-generated content made with generic or unoriginal templates". AI scripts and visuals are allowed when every video is materially varied and educational. Safe: distinct threads, real captures with credit, faithful schematics, sourced facts, one original synthesis per video, a consistent look that is **not** a reskinned template ([[Playbook]] §1 *Spread and variety*).
- **Disclosure:** realistic depictions of things that did not happen must be disclosed; clearly non-realistic schematics and a synthetic narrator need not be, but the uploader sets `containsSyntheticMedia: true` and the description carries an AI line. TikTok: turn **AI-generated content ON**.
- **No malicious clickbait:** a hook promises only what the video shows.
- **Money:** YPP Shorts route = 1,000 subscribers + 10 M qualified Shorts views in 90 days; long-form route = 1,000 subscribers + 4,000 public watch hours in 12 months. Since 31 March 2025 a Shorts view is any start or replay; **engaged views** is what monetization uses. TikTok Creator Rewards needs videos over 1 minute: do not stretch Shorts for it.
- **AI shelf life:** a render older than 30 days, or any claim about a model, price, plan or product feature, is re-checked at its source before upload; a changed claim means a re-voice or a dated card.

## P8 in one command

Write **one** `upload/publish.json` (keys in the header of `System/scripts/publish.py`: title, claim, sources, caveats, hashtags, hook type, pinned comment, the user's words, optional claims and TikTok caption) and run `python3 System/scripts/publish.py <that file>` with `run_in_background` (processing can pass 10 minutes). It needs `upload/thumb.jpg` (`v.thumb`, [[Workflow]] §Thumbnail), writes the description (credits from `_credits.jsonl`), uploads **private** unless `privacy` says otherwise, waits for processing, sets the thumbnail again and checks by pixel compare that the served one is ours, writes the `videos.csv` row, the Upload note, Status stage 8 and the index row, pulls analytics and runs `check_vault`. Report its ten lines. `--dry-run` stops after the description and the pack; `--resume <id>` skips the upload after a crash. Never write the Upload note, the description or the csv row by hand.

## Publish pack

**Every video gets `upload/<prefix>-publish-pack.md` before the user is asked to approve:** the thumbnail embedded, the title with alternatives, the description, the pinned comment and the TikTok caption, each in its own plain ASCII ```` ```text ```` block. `publish.py` writes it on every run (`--dry-run` included); never edit it by hand: change `publish.json` and rerun.

**Copy-paste text:** plain ASCII, `-` bullets, `|` separators, no `>`, `•`, curly quotes or angle brackets (YouTube rejects them).

**Titles:** 100 characters or fewer, a searchable statement with the keyword first (the AI term a beginner types, or the product name), no all caps or emoji. **Description:** claim and search words in the first two lines, "New Shorts every day.", SOURCES as real links with cut-off date, credits for CC BY and CC BY-SA, the AI line, 3 to 5 hashtags last. **Pinned comment:** one question plus an invitation to correct a figure.

## YouTube route

`youtube_upload.py` (called by `publish.py`) sets `containsSyntheticMedia`; default private. `auth` needs the user once (client id and secret in `.env`; the consent link opened in the browser profile on the test-user list). **The app is in Testing, so refresh tokens expire every 7 days:** on HTTP 400 at `oauth2` or `invalid_grant`, the user runs `python3 System/scripts/youtube_analytics.py auth` and the upload consent again. Run the YouTube scripts from `~/Documents/youtube` (the only `.env` with the keys) with the script's absolute path. Quota: 1,600 of 10,000 units per upload. A private video's thumbnail is read from its signed `snippet.thumbnails.maxres.url`, never from `i.ytimg.com`. Not automated: the caption file, playlists, the pinned comment. Never print or note a token.

## TikTok route (manual)

The same master, uploaded from TikTok Studio on the web; no watermark, no TikTok library sound; the agent prepares the pack, the user posts and types the 48 h and 7 d numbers into `Analytics/`.

## Analytics loop

- `Analytics/videos.csv` (what each video is; filled at P8) and `Analytics/snapshots.csv` (video × platform × age). `Analytics/Report.md` is generated: never edit it by hand.
- **Pull** at about 24 h, 7 d, 28 d: `youtube_analytics.py pull`, then `analytics.py report`; typed numbers: `analytics.py add "<Video>" youtube 24h views=… viewed_pct=…`.
- **Decision metrics and the first lever when low:** `viewed_pct` → first sentence and frame 1 · `avg_pct_viewed` → length, pace, middle scenes · `engaged_views` → ending and loop · `shares` → payoff and stakes · `subs_gained` → channel page, consistency. **Under about 100 views read counts only; change nothing.**
- **One change per video**, so the next snapshot can attribute it; one *Learnings* line in Status per pull. Every 10 videos run the [[Feedback loop]] on the data and replace third-party benchmarks with the channel's medians. Kill criterion: 20 Shorts averaging under a third viewed means changing the idea gate and hook before the visuals.
- **Baseline:** YouTube's diagnostic on the channel's earlier niche (9 Oct 2026): 39.7 % viewed vs swiped away; the first 1 to 2 s are the first lever.

## Hypotheses

Rules marked [H] in the notes, judged here at 10 uploads; each is kept, changed or deleted in the owning note.

| Hypothesis | Owner | Judged by |
| --- | --- | --- |
| A named real case carries the concept | [[Playbook]] §1 | `viewed_pct`, shares vs videos without one |
| Short test block (90 to 140 words; compact 60 to 85) | [[Playbook]] §2 | `avg_pct_viewed` and `engaged_views` by length |
| Structure by series | [[Playbook]] §2 | `avg_pct_viewed` by series |
| Phrase captions (1 to 3 words) | [[Playbook]] §4 | `viewed_pct` vs the earlier word-by-word cuts |
| Camera and transitions (look v3, 27 Oct 2026) | [[Design system]] | `avg_pct_viewed` vs the v2 renders |
| Thumbnail: one focal image, 3 to 4 words | [[Workflow]] §Thumbnail | impressions click-through between videos |

## Narrative sources (28 Oct 2026)

Basis of [[Playbook]] §2a. Most are creator-tool blogs with unverified numbers: treated as hypotheses [H] until the channel's own curves say otherwise. YouTube publishes no viewed-versus-swiped threshold. Vendor claims: the hook decides in 1 to 3 s; 30 to 50 % leave in seconds 1 to 3 on a weak open; change the picture every 1.5 to 2 s; payoff in the first half; end on a frame that matches the opening for rewatches (aibrify.com, opus.pro, vidiq.com, 2026). Academic: a 2020 study of 306 popular YouTube science videos found popularity tied to emotional arousal, a dramatic question, moments of change and story (*Frontiers in Communication*, 2020, doi 10.3389/fcomm.2020.581349). Theory: the curiosity gap (Loewenstein).
