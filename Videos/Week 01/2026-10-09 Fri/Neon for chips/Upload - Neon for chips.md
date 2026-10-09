---
type: research
created: 2026-10-09
updated: 2026-10-09
status: DRAFT for the user's approval; nothing uploaded; `publish.py` rewrites this note at upload
tags: [upload, youtube, week-01]
---

# Upload · Neon for chips (draft)

← [[Neon for chips - Status]] · [[Script - Neon for chips]] · [[Publish]]

Render: `Media/Week 01/2026-10-09 Fri/Neon-for-chips/render/ne-45s-9x16-r3.mp4` (44.7 s, 117 words). Visibility proposed: **private first**. Approval: **pending** (title, thumbnail, description, visibility). Draft `upload/publish.json` is ready; `python3 System/scripts/publish.py "Media/Week 01/2026-10-09 Fri/Neon-for-chips/upload/publish.json"` uploads it after your yes.

## Thumbnails

Variant A (recommended: it restates the title and the hook, "a gas from steel mills") is `upload/thumb.jpg`; variant B (the glowing neon tube, plainer promise, stronger in a feed) is `upload/thumb-b.jpg`. Both: kicker, two lines with the second in orange, three chips that are sourced figures or key terms. To use B, change `thumb` in `publish.json` to hero `stock/ne-s05-neon.jpg`, lines `THE GAS BEHIND` / `EVERY CHIP`, kicker `STEEL MILLS' LEFTOVER`.

## Titles (pick one)

```text
Every Chip Needs a Gas From Steel Mills
```

1. **Every Chip Needs a Gas From Steel Mills** (recommended, 39 characters; plain claim, same words as the hook).
2. Why Chips Depend on a Steel Mill Leftover (41).
3. Half the Neon for Chips Came From Two Companies (49; keeps the Ukraine stake, dated 2021 to 2022 in the description).

## YouTube description (paste as is)

```text
Chip lasers need neon, and neon is a leftover from the air plants of big steel mills. In 2021 two Ukrainian companies supplied about half of the neon used for chips, and both shut down in 2022.

New Shorts every day.

SOURCES
- Chip lasers: KrF and ArF excimer lasers give the 248 and 193 nm light used in lithography: https://en.wikipedia.org/wiki/Excimer_laser
- Neon is about 18 parts per million of air: https://en.wikipedia.org/wiki/Neon
- Neon is a by-product of steel plants' air separation, recovered only at very large plants: https://apac.gasworld.com/story/inox-air-products-tata-steel-sign-record-setting-industrial-gas-production-deal/
- Two Ukrainian firms supplied 45 to 54 percent of chip-grade neon (Reuters with Techcet data, March 2022): https://cyprus-mail.com/2022/03/12/russias-attack-on-ukraine-halts-half-of-worlds-neon-output-for-chips
- The largest chipmakers could cover two months or more from stock (Techcet): https://www.pcgamer.com/au/major-chipmakers-could-weather-neon-shortages-as-result-of-war-in-ukraine-for-two-months-or-more
The shares are 2021 estimates reported in 2022; the current split was not found. Apart from Wikipedia, sources were checked from search summaries only. Cut-off 9 October 2026. Figures checked on 9 October 2026.

PHOTO CREDITS (Wikimedia Commons)
Aciarium, CC BY-SA 4.0 | Peellden, CC BY-SA 3.0 | Jurii, CC BY 3.0 | Mister rf, CC BY-SA 4.0 | Public domain and CC0 photos: A ansems

The narration is AI-generated and the diagrams were drawn for this video; the photos are real.

#semiconductors #neon #chips #howitworks #tech
```

## Pinned comment

```text
Should the chips that run everything depend on a leftover gas? Tell me what you think, and correct me if the supply has changed since 2022. Sources are in the description.
```

## Studio settings

Not made for kids; synthetic-content answer: yes (AI voice, drawn and generated diagrams); captions: upload `render/ne.srt` by hand.

## TikTok (draft)

```text
Every chip is made with a gas from steel mills, and in 2021 about half of it came from two companies in Ukraine. Should chips depend on a leftover gas? #semiconductors #neon #chips #tech
```

## Claims

| Claim | Source | Strength |
| --- | --- | --- |
| KrF and ArF excimer lasers give 248 and 193 nm light for lithography | Wikipedia, Excimer laser | read 9 Oct 2026, secondary |
| Neon is about 18 ppm of air (so about 1 in 55,000 by volume, agent's arithmetic) | Wikipedia, Neon; patent US 5100446 | snippet |
| Neon is a by-product of steel plants' air separation; only very large plants recover it | gasworld, Springer | snippet |
| Ingas and Cryoin supplied 45 to 54 % of chip-grade neon in 2021 and shut after the invasion | Reuters with Techcet data, March 2022 | snippet; estimate |
| Largest fabs could cover two months or more from stock | Techcet via PC Gamer | snippet |
| Neon's exact role in the laser (buffer gas) and the scene 2 phrase "use it inside their lasers" | not read in a primary page | **open** |

## Checklist

- [ ] Open the Reuters, gasworld and PC Gamer pages and confirm the figures (only Wikipedia was opened)
- [ ] User chooses title and thumbnail A or B, confirms visibility
- [ ] `Analytics/videos.csv` row (the P8 script writes it)
- [ ] Pulls at 24 h, 7 d, 28 d
