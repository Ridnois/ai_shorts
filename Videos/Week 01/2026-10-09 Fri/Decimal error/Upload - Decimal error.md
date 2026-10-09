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

`upload/de-thumb-a.jpg`: hero drawn in the render's style (`upload/hero-de.png`: Friday's board at 524.811 against Monday's at 1,098.892, bars to scale), kicker ROUNDING ERROR, lines IT DOUBLED. / NOTHING TRADED. (orange), chips ONE DIGIT DROPPED | 3,000 TIMES A DAY | VANCOUVER, 1982 TO 1983. The package's first draft said "doubled overnight": changed, because it happened over a weekend.

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
