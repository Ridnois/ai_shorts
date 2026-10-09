---
type: research
created: 2026-10-09
updated: 2026-10-09
status: DRAFT for the user's approval; nothing uploaded; `publish.py` rewrites this note at upload
tags: [upload, youtube, week-01]
---

# Upload · Decimal error (draft)

← [[Decimal error - Status]] · [[Script - Decimal error]] · [[Publish]]

Render: `Media/Week 01/2026-10-09 Fri/Decimal-error/render/de-57s-9x16-r1.mp4` (56.8 s, 163 words). Visibility proposed: **private first**. Approval: **pending** (title, thumbnail, description, visibility). **Copy-ready pack** (thumbnail, titles, description, pinned comment, TikTok caption): `Media/Week 01/2026-10-09 Fri/Decimal-error/upload/de-publish-pack.md`, made by `publish.py --dry-run` from `upload/publish.json`. After your yes: `python3 System/scripts/publish.py "Media/Week 01/2026-10-09 Fri/Decimal-error/upload/publish.json"` (needs the YouTube keys in `.env`; this machine has none).

## Thumbnail

`upload/de-thumb-a.jpg` (v2, 9 Oct 2026, after the user asked for a research-led redesign): one focal image drawn in the video's look (`make_thumbnail.drawn`, [[Workflow]] §Thumbnail v2): the index line sliding for two years, then jumping straight up in orange, a CLOSED sign beside the jump and a big x2; 2 words, inside the safe band, checked at 168 px wide and in the 3:2 crop. No kicker, chips or logo. The chart is schematic (the decline's wobble is illustrative; the levels 1,000, 524.811 and 1,098.892 are to scale). Title recommended with it: *The Rounding Error That Halved a Stock Index*.

## Studio settings

Not made for kids; synthetic-content answer: yes (AI voice, drawn animations); captions: upload `render/de.srt` by hand. TikTok: AI label on, cover = the hook frame (board at 1,098.892).

## Claims

| Claim | Source | Strength |
| --- | --- | --- |
| Index set at 1,000 in January 1982, updated after each trade | Wikipedia VSE, citing WSJ 8 Nov 1983 | read (secondary) |
| Four decimals computed, three kept, the last discarded, not rounded | Parker, *Humble Pi* (2019), excerpt | read (excerpt) |
| About 3,000 updates a day; about 25 points lost a month | Wikipedia VSE; Parker | read (secondary) |
| Friday 25 Nov 1983 close 524.811; Monday 1,098.892 after recalculating with rounding | Wikipedia VSE and Rounding (Toronto Star 29 Nov 1983; Higham 2002) | read (secondary) |
| The market was rising (recalculated value 9.9 % above the start) | Wikipedia Rounding; agent arithmetic | read and run |
| About 1.4 million cuts, about 0.0004 points each | agent estimate (477 trading days) | run |

## Checklist

- [ ] You choose the title and confirm the thumbnail and visibility
- [ ] YouTube keys in `.env` (or upload from the other machine)
- [ ] `Analytics/videos.csv` row (the P8 script writes it)
- [ ] Pulls at 24 h, 7 d, 28 d; compare `viewed_pct` with Netflix screenshot (52.6 %) and the channel's 39.7 %
