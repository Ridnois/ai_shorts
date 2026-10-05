---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v1 · first snapshot, taken 1 to 2 hours after publishing; counts only, nothing here is a conclusion
tags: [analytics, report, youtube, week-01, battery, copper]
---

# First numbers · 5 Oct 2026

← [[Publish]] · [[Report]] (generated tables) · [[Battery and lithium - Status]] · [[Copper and the AI race - Status]] · [[YouTube Channel]]

Pulled at **19:38 UTC** with `youtube_analytics.py pull` (read-only OAuth, YouTube Data API for public counts; raw JSON in `Analytics/exports/2026-10-05/`). Both videos are **public** and were published the same evening, one hour apart.

## 1. The data

| | Battery and lithium | Copper and the AI race |
| --- | --- | --- |
| YouTube id | zwNmTGoXPu0 | YRX0VfpPMtU |
| Published (UTC) | 17:31 | 18:29 |
| Length · words | 72 s · 200 | 61 s · 160 |
| Hook | "Your battery runs on a metal that floats" (surprising fact) | "One AI server rack can hold over two miles of copper cable" (surprising number) |
| Age at the pull | 2 h | 1 h |
| Views | 45 | 9 |
| Likes · comments | 1 · 2 | 0 · 0 |
| Views per hour of age | ≈ 21 | ≈ 8 |

Channel: **2 subscribers**, 2 videos (Data API). The **Analytics API returned no rows for either video** (see §3).

## 2. What this says, and what it does not

- **Nothing about retention, hook strength or pace.** Viewed vs swiped away, average percentage viewed, shares and subscribers gained are not available yet, and **45 and 9 views cannot support a rate** anyway. Battery got more early views than Copper; the videos were published an hour apart, to different moments of the evening, and the user's own views and shares are inside these counts. **Do not rank the hook types on this.**
- **Comments exist on Battery (2)**: the first reaction signal; read them for what people questioned (a free fact-check, [[Publish]] §3).
- Both are the channel's first two data points: **the baseline that every later video is compared with.**

## 3. Findings about the measuring itself (these are certain)

1. **The Analytics API had no rows for videos 1 to 2 hours old**, although the call and the permissions work (an empty table, not an error). Reporting lags; the Data API's public counts do not. So a **fast snapshot (views, likes, comments) is possible at any time; the full set (engaged views, average percentage viewed, shares, subscribers, traffic split, retention curve) needs waiting**. How long the lag lasts is not yet known: **the next pull is the test** (see §5).
2. **Ages must be compared like with like.** With one Short a day, videos are always at different ages; the report now groups snapshots by age (`1h`, `2h`, `3d`…) instead of fixed 24 h, 7 d, 28 d.
3. **A small-sample guard was missing:** the report now flags videos under 100 views and says to read counts only.
4. **Records were stale:** [[Upload - Battery and lithium]] still said "not uploaded". Fixed; `videos.csv` now has both ids and dates.
5. **The live YouTube description of Copper still says "New Shorts every week"** (the vault says every day). Change it in Studio; the pull saves the raw description in `data-api.json` so this kind of drift can be checked.

## 4. Changes applied to the vault

| Where | Change |
| --- | --- |
| [[Publish]] §3, §5, §6 | rhythm: instant counts at 1 to 24 h, full metrics from the first day the API answers (test), then 7 d and 28 d; the sample rule (< 100 views: counts only); the collector exists (`youtube_analytics.py`) and what it needs (API enabled, read-only consent) |
| `System/scripts/analytics.py` | report groups by real age; low-sample warning |
| `System/scripts/youtube_analytics.py` | built; falls back to Data API counts when the Analytics API is empty; saves raw JSON |
| [[Workflow]] stage 8 and 9 | P8 fills `youtube_id` and `published` in `videos.csv`; stage 9 says to run `pull` |
| `CLAUDE.md` | tooling table lists the puller |
| [[Upload - Battery and lithium]] | status: uploaded and public, with the id |

## 5. Questions for the next report (about 3 days after the first)

1. When does the Analytics API start returning rows (hours after publishing)? Record the answer in [[Publish]] §6.
2. Does `viewed_pct` exist in the API at all? (Not in the pull; if absent, the user types it from Studio.)
3. What are the retention drops of both videos (`retention-<id>.json`)? Map them to scenes in the Status notes.
4. Which topic family and hook type get more views per day after the first 48 h, once the user's own views are out of the noise? Needs ≥ 5 videos before any rule changes ([[Publish]] §5).
5. What did the Battery commenters ask or dispute?
