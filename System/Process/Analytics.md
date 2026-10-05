---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v1 · metric catalogue from YouTube's API docs (read 5 Oct 2026); the Studio export format and "viewed vs swiped away" in the API are NOT verified; automatic collection deferred by the user
tags: [analytics, metrics, process, youtube, tiktok, feedback]
---

# Analytics (how the channel learns from its numbers)

← [[YouTube Channel]] · [[Channel strategy]] §6 · [[Feedback loop]] · [[Shorts quality bar]] · [[Idea and hook quality]] · [[YouTube upload]] · [[TikTok upload]]

**Principle:** a number that is not in the vault cannot change the next video. The user reads Studio; the agent keeps the **data in two CSVs**, regenerates **[[Report]]**, and the idea gate, the hook and the feedback loop **read the report**. Collection is manual for now (user decision, 5 Oct 2026: *"Lets keep automatic upload for later"*, and the numbers are read by the user in Studio); the CSV is the stable interface, so an API collector can fill it later without touching anything else.

## 1. What can be measured (catalogue)

**YouTube Analytics API v2** (`yt-analytics.readonly` scope; the current upload token does not have it; [docs](https://developers.google.com/youtube/analytics/channel_reports), read 5 Oct 2026). Studio shows the same data in the UI, and its **Advanced mode** can export a view as CSV (**format not seen yet**).

| Family | Metrics and dimensions | Use for a Short |
| --- | --- | --- |
| **Core per video** | views, **engaged views**, estimated minutes watched, average view duration, **average view percentage**, likes, comments, shares, playlist adds, subscribers gained and lost, red views | the five decision metrics (§2) |
| **Over time** | any core metric by day or month | the 24 h / 7 d / 28 d curve of one video |
| **Audience retention** | by elapsed video time ratio: audience watch ratio, relative retention performance, started/stopped watching | **where inside the Short people leave** (scene-level fixes) |
| **Traffic sources** | by source type: views, engaged views, minutes | how much of the reach is the Shorts feed vs search, suggested, channel page |
| **Playback location, device, OS** | views, engaged views, minutes | low value for a vertical Short |
| **Geography** | by country (also US province, city, DMA): views, minutes | whether the English audience is where expected |
| **Demographics** | viewer percentage by age group and gender | who the topics reach |
| **Sharing service** | shares by service | where shares go |
| **Playlists** | views, starts, saves, average time in playlist | only if weekly playlists are used |
| **Top videos** | up to 200, sorted | the ranking behind the report |
| **Money** (needs the Partner Program) | revenue, CPM, ad impressions | not yet |

**Studio-only or unverified in the API:** *viewed vs swiped away* (the hook metric; I could not confirm it as an API metric), Reach impressions, "new vs returning viewers", the Shorts-feed share. Until verified, they are **typed in by the user** from Studio.

**TikTok** (Studio / Analytics, manual): views, average watch time, finish rate (full-video views %), likes, comments, shares, saves, new followers, traffic by source (For You, profile, search), audience territories. TikTok's API route for reading stats is not researched.

## 2. What the vault keeps per video (the core set)

`Analytics/snapshots.csv`, one row per **video × platform × age**, columns: `views, engaged_views, viewed_pct, avg_view_s, avg_pct_viewed, completion_pct, likes, comments, shares, saves, subs_gained, new_viewers_pct, feed_pct, notes`. Leave a cell blank when the platform does not show it. **The five that decide things:**

| Metric | Question it answers | If low, change (first) |
| --- | --- | --- |
| `viewed_pct` (viewed vs swiped away) | does the hook work? | the first sentence and first image ([[Idea and hook quality]]) |
| `avg_pct_viewed` | does the pace hold? | script length, pace, the middle scenes (use the retention curve) |
| `engaged_views` | what monetization and reach count | the ending and the loop seam |
| `shares` | is it worth passing on? | the payoff and the stakes ([[Narration guide]]) |
| `subs_gained` | does the brand convert? | channel page, series consistency |

`Analytics/videos.csv` says what each video **is** (`words, duration_s, hook_type, hook, series, plates, voice, published, youtube_id, tiktok_id`), so the report can group results by hook type and series. Fill it at P8 (publishing), from the Status and Upload notes. `hook_type` values (extend by need): *surprising fact, surprising number, question, contradiction, stakes*.

## 3. How to record (the rhythm)

1. **When:** **24 h**, **7 d** and **28 d** after publishing (the Status note says the date). With a daily cadence, do all videos of the day-batch in one Studio session; one snapshot per age per video is enough.
2. **How:** the user pastes the numbers in chat (any format) or exports the Studio view; the agent runs
   `python3 System/scripts/analytics.py add "<Video>" youtube 24h views=… engaged_views=… viewed_pct=… avg_pct_viewed=… shares=… subs_gained=…` (columns in §2) and then `python3 System/scripts/analytics.py report`.
3. **The retention curve** (second by second) is a picture in Studio, not a column: the user describes where it drops, or saves a screenshot to `Videos/Week NN/<Topic>/`, and the agent writes one line under *Learnings* in the video's Status note (e.g. "drops at scene 6, the 4 s card").
4. **Corrections:** a new row with the same key replaces the old one in the report (newest wins); never edit the Report by hand.

## 4. How the numbers change the next video (the loop)

| Moment | The agent reads | And changes |
| --- | --- | --- |
| **P1, idea** | [[Report]]: which `hook_type` and topics held `viewed_pct`, `shares`, `subs_gained` | the ranking in the idea scoring ([[Idea and hook quality]] §2): a hook type that held earns a bonus, one that lost is not repeated without a new angle |
| **P2, script** | the video's retention notes, the median `duration_s` of the best videos | length and pace targets |
| **P8, publish** | `videos.csv` row is created; schedule slot | the first row of the video's data |
| **After 24 h, 7 d** | the new snapshot | the video's Status note, *Learnings* (what held, what did not) |
| **Every 10 videos** | the whole report | run [[Feedback loop]] on the **data**: edit [[Shorts quality bar]], [[Idea and hook quality]], [[Narration guide]]; replace the third-party benchmarks below with the channel's own medians |

One change per video, written down ([[Feedback loop]]): otherwise the next snapshot cannot say which change worked.

## 5. Benchmarks (hypotheses until replaced)

From third-party blogs ([[Upload - Battery and lithium]] §8): hold above ≈ 80 % through the first 3 s, ≈ 70 % average viewed; below ≈ 30 % "viewed" the Short dies. **Treat as guesses.** At 10 videos with data, the **channel's median** per metric becomes the bar (a video below it is a candidate for a fix), and this section is rewritten with the numbers. Kill criterion from [[Channel strategy]] §6.4 stands until then.

## 6. Later (deferred, not built)

- **API collector:** add the `yt-analytics.readonly` scope to the OAuth app (re-run `auth`; the app is in Testing, [[YouTube upload]] §3), then a script that calls the Analytics API and appends rows to `snapshots.csv` (audience retention could be saved per video). Not worth it before the CSV rhythm is used for ≈ 10 videos.
- **Studio CSV importer:** write it from a real export; none has been seen.
- **TikTok stats via API:** not researched.

## 7. Not verified

The Studio export format; whether *viewed vs swiped away* is available in the API; the shares-per-view levels that count as good; every third-party benchmark. The script was tested only with a throwaway row (removed).
