---
type: research
created: 2026-10-05
updated: 2026-10-05
status: decided (thumbnail B, title 1, the rest as recommended); the upload itself is blocked on how to send the 65 MB file (see §0)
tags: [youtube, upload, week-01, battery, lithium, shorts]
---

# Upload · Battery and lithium (Week 01)

← [[Battery and lithium - Status]] · [[Script - Battery and lithium]] · [[Channel playbook]] · [[Shorts quality bar]]

User request (5 Oct 2026): *"Its perfect, now i want it to prepare for upload, reorganize the media files, organize the videos by week, this one is week 1 and the rest is legacy. then prepare note to show me the video, description, hashtags, and thumbnail… remember to research on how to build all of this in order to be captivating and improve metrics"*. **Nothing has been uploaded, scheduled or published: that is a manual step in YouTube Studio** (the API route discussed earlier is not built).

## 0. Decisions (5 Oct 2026)

User: *"Thmbnail b is the winner, tittle recomendation is good, follow your recomendations on the rest. then proceed to upload my video"*.

| Item                                                   | Decision                                                                                                                                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Thumbnail                                              | **B** ("NOT RARE. STILL A FIGHT.", `Media/Week 01/Battery-lithium/upload/thumb-b.jpg`); A and C are archived as ideas (their files stay in `upload/` and can be deleted) |
| Title                                                  | **Lithium Isn't Rare, So Why Do Countries Fight Over It?** (54 characters)                                                                                               |
| Description, hashtags, pinned comment, Studio settings | as in §3, §4, §6, §7                                                                                                                                                     |

*Heads-up recorded:* thumbnail B's text says the same thing as the title (not rare, a fight); I had paired the title with A so they would complement each other. It still works; if the repetition bothers you, title 2 ("Your Battery Runs on a Metal That Floats") pairs better with B.

**Upload status (5 Oct 2026): not uploaded.** The channel is `UCCZX7-YPNPntwPKI1hdv2hQ` (REDTAIL, 0 videos), Studio is signed in and the Upload dialog is open in a Chrome tab. Claude in Chrome's `file_upload` accepts at most **10 MB** and the render is **65 MB**; a workaround that served the file from a temporary localhost server and attached it from the page was **denied by the permission check and was not pursued** (the server was shut down). Ways forward, the user decides: (a) the user attaches the file in the open dialog and the agent fills the rest; (b) the user explicitly approves the localhost route; (c) a one-time YouTube Data API setup (OAuth client created by the user), which also serves the weekly cadence. Visibility: **Private until the user chooses a schedule** (the weekly slot is not decided).

## 1. The video

![[bt-72s-9x16-r1.mp4|320]]

`Media/Week 01/Battery-lithium/render/bt-72s-9x16-r1.mp4` · 71.9 s · 1080×1920 · 200 words · Austin, speed 1.0 · captions burned in. Subtitle file for Studio: `render/bt.srt` (the narration with timings; the burned-in captions are for sound-off viewers, the SRT is for accessibility and search).

## 2. Title (pick one; the first ≈ 40 characters are what the feed shows)

| #   | Title                                                      | Characters | Why                                                                                                                                                  |
| --- | ---------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Lithium Isn't Rare, So Why Do Countries Fight Over It?** | 54         | the keyword first, the video's own question, no hype word; pairs with thumbnail A (the thumbnail shows the "floats" curiosity, the title the stakes) |
| 2   | Your Battery Runs on a Metal That Floats                   | 40         | the video's first line: a click lands on a payoff in 3 seconds; short, fits whole in the feed                                                        |
| 3   | The Lightest Metal Is a Political Pressure Point           | 48         | plain and accurate; the weakest on curiosity                                                                                                         |

**Recommendation: title 1 with thumbnail A.** Rules used: YouTube allows 100 characters; the keyword goes first because only the first ≈ 40 to 50 show in the feed (third-party sources, below); no banned words ([[Channel identity]]); the title promises only what the video delivers (it explains why countries compete: processing, not scarcity).

## 3. Description (paste as it is; 1980 characters, the limit is 5,000)

> Lithium isn't rare, but about 60% of it is refined in one country. How the lightest metal became a pressure point, and the battery that could walk away from it.
>
> New Shorts every week.
>
> SOURCES
> • USGS, Mineral Commodity Summaries 2026, Lithium: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-lithium.pdf
> • IEA, Global Critical Minerals Outlook 2025 (China's share of lithium refining): https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals
> • China's export licenses for high-end batteries, cathodes and graphite anodes (MOFCOM Decision 58, 9 Oct 2025) and their one-year suspension (Decision 70, 7 Nov 2025): https://www.ess-news.com/2025/10/13/china-imposes-new-export-controls-on-lithium-ion-battery-technology/ and https://www.cirs-group.com/en/chemicals/china-temporarily-suspends-export-controls-on-key-raw-materials-including-rare-earths-lithium-batteries-and-diamond
> • CATL's sodium-ion batteries (company claims): https://carnewschina.com/2025/12/28/catl-confirms-2026-large-scale-sodium-ion-battery-deployment-in-multiple-sectors/
> • Atacama evaporation ponds: sources give about 12 to 24 months; the video uses about 18, from Albemarle's description.
> Figures checked on 5 October 2026.
>
> PHOTO CREDITS (Wikimedia Commons)
> Lithium in mineral oil: Sea Moon, CC BY 2.0 · Lithium: W. Oelen, CC BY-SA 3.0 · Lithium-ion cells: Sevenethics, CC0 · Salar de Atacama: NASA Earth Observatory and NASA SVS (public domain), ESA (CC BY-SA 3.0 IGO) · Greenbushes mine: Calistemon, CC BY-SA 4.0 · CATL, Arnstadt: Giorno2, CC BY-SA 4.0 · CATL, IAA 2024: Matti Blume, CC BY-SA 4.0 · NYK Themis at the Port of Los Angeles: Downtowngal, CC BY-SA 4.0 · Container cranes: George Robinson, CC BY-SA 2.0 · Sodium-ion cell: Vladimir022009, CC BY-SA 4.0 · Faradion sodium-ion cell, Science Museum: The wub, CC BY-SA 4.0
>
> The narration and the schematics are AI-generated; the photos are real.
>
> #lithium #batteries #science #geopolitics #sodiumion

How it was built:

- **The first two lines carry the search words** (lithium, refined, pressure point, battery) and the claim; the rest is below the fold.
- **Sources are real links to what was read** (USGS and IEA were read directly; the Chinese notices through summaries; CATL's claims are labelled as the company's). The pond figure is stated as a range because the sources disagree.
- **Photo credits are mandatory** for the CC BY and CC BY-SA photos (author, license). They are listed in [[Battery and lithium - Status]] §Attribution. *Open point:* the CC BY-SA photos sit inside a video that is not itself CC BY-SA; the channel already did this on earlier videos and treats the video as a collection, but this is **not legal advice**: if you want zero doubt, swap those photos for CC0 or public-domain ones.
- **The AI line stays** (pillar "Honest about machines"): narration and schematics are AI-generated, photos are real.
- **Hashtags last, five, all relevant.** YouTube shows up to three of the description's hashtags above the title (it picks which), ignores them all above 60, and removes videos for unrelated ones (YouTube Help).

## 4. Hashtags

`#lithium #batteries #science #geopolitics #sodiumion`

Five, in the description (not the title, so the title stays clean). Third-party sources recommend 3 to 5; there is no evidence here that more help. `#Shorts` is not added: the video is vertical and under three minutes, which is what makes it a Short; add it only if you want to.

## 5. Thumbnail

Three candidates, 1080×1920 (9:16), JPEG under 300 KB each. The hero images were generated with `gpt-image-1.5` (medium, about $0.05 each, the rate is unconfirmed) and the **text is composed locally** (`System/scripts/make_thumbnail.py`), so the spelling is exact. The white band marks the centre **3:2 zone: the text and the subject sit inside it** because thumbnails render near 3:2 on channel pages, search and TV.

![[thumb-a.jpg|230]] ![[thumb-b.jpg|230]] ![[thumb-c.jpg|230]]

| | Text | Idea | Agent's view |
| --- | --- | --- | --- |
| **A** | THE METAL THAT FLOATS | lithium floating in oil, the video's hook | **recommended**: concrete, matches the first 3 seconds, the metal is the hero |
| **B** | NOT RARE. STILL A FIGHT. | a silver pebble floating on still water at sunset | the best-looking; states the paradox; the pebble is a stand-in for lithium |
| **C** | 60% IN ONE COUNTRY | white powder pouring from a bottle | the weakest: the "bottleneck" metaphor does not read; the number is the strongest part |

**Can you upload it?** YouTube announced custom Shorts thumbnails on 24 July 2026, **for YouTube Partner Program channels first, desktop**; wider access "over time" (YouTube Blog; third-party reports give the details: 9:16 image, important content inside a 3:2 safe zone, no A/B testing for Shorts). **If the channel is not in the Partner Program yet, the option is not there:** use the fallback, choose a frame in Studio or the app (the opening frame, the jar of lithium, is the strongest). Also: **99.9 % of Shorts views start in the Shorts feed, where no thumbnail is shown** (ppc.land, a trade site: treat the number as indicative), so the thumbnail matters on the channel page, search and TV, not for the main feed. The vault's old rule "no thumbnail on Shorts" is updated accordingly ([[Guidelines for new scripts]] §5).

**Disclosure:** a thumbnail made with AI is exempt from YouTube's synthetic-content label (YouTube Help lists "thumbnail, title, or infographic" among the productivity uses).

## 6. Pinned comment (post it right after publishing)

> Which part surprised you more: a metal that floats, or one country refining about 60% of it? If I got a number wrong, tell me and I will pin the correction.

A question that is easy to answer in one line, and it invites corrections (the channel's rigor promise).

## 7. Studio settings

| Field | Value |
| --- | --- |
| Visibility | schedule it, in a fixed weekly slot (the channel promises *new Shorts every week*); pick the hour from Analytics › Audience › *When your viewers are on YouTube* once there is data; before that any consistent slot is a guess |
| Audience | **Not made for kids** (required choice) |
| Altered or synthetic content | **No** is my reading of the policy: the narration is a stock synthetic voice, not a real person's, and the schematics are not photorealistic scenes; the policy asks for a label on realistic content that could be mistaken for real. **The decision is yours** (YouTube Help, *altered or synthetic content*) |
| Category | Science & Technology |
| Language | English; subtitles: upload `bt.srt` |
| Playlist | create **"Week 01"** only if you want weekly playlists; otherwise none |
| Comments | on, pinned comment above |
| Thumbnail | A (or B) if the channel is eligible; otherwise pick the opening frame |
| Description and hashtags | §3 and §4 |

## 8. Why these choices (research, with what is solid and what is not)

| Claim | Source | Strength |
| --- | --- | --- |
| Hashtags: up to 3 shown above the title; over 60 are all ignored; unrelated ones can get a video removed; allowed in title and description | [YouTube Help, Hashtags](https://support.google.com/youtube/answer/6390658) (read) | **official** |
| AI disclosure covers realistic altered content; thumbnails, scripts, titles and non-realistic content are exempt; AI narration depends on context | [YouTube Help, altered or synthetic content](https://support.google.com/youtube/answer/14328491) (read) | **official** |
| Custom Shorts thumbnails announced 24 July 2026, Partner Program first | [YouTube Blog](https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/) (read: it gives no sizes) | **official**, sizes not |
| 3:2 safe zone, desktop upload, no A/B test, 99.9 % of views in the feed | [PPC Land](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/) | trade press: indicative |
| Title limit 100; about 40 to 50 characters visible; keyword first; 60 to 80 characters perform best | search results from [hashtagtools.io](https://hashtagtools.io/blog/youtube-shorts-character-limits-title-description-hashtags-2026), [miraflow.ai](https://miraflow.ai/blog/youtube-shorts-titles-descriptions-2026-templates) | **third-party blogs: hypotheses** |
| Benchmarks: hold above 80 % through the first 3 seconds, above 70 % average viewed; below 30 % "viewed" the Short dies; most swipes happen in the first 2 seconds | search results from [prepublish.ai](https://prepublish.ai/blog/viewed-vs-swiped-away-youtube-shorts), [tubeanalytics.net](https://www.tubeanalytics.net/blog/youtube-shorts-retention-guide) | **third-party blogs: hypotheses** |
| Engaged views (not raw views) drive promotion and monetization | [[Shorts quality bar]] §7 (YouTube Help, 4 Oct 2026) | official |

**What the video already does for the metrics** (from [[Shorts quality bar]]): a need-to-know claim in the first 8 words, speech from 0.15 s, the strongest real image from frame 1, a new image every ≈ 3 s, captions from the first word, a concrete ending, and **the last plate is the first plate** so the Short loops without a seam.

## 9. After publishing: what to measure and what to change

Fill this in at 24 hours and at 7 days (Studio › Analytics › Content › the Short). **These are the first data points the channel has: the benchmarks above are hypotheses until they are replaced by your own numbers** ([[Channel strategy]] §6).

| Metric | What it tells | 24 h | 7 days | If it is low, change |
| --- | --- | --- | --- | --- |
| **Viewed vs swiped away** | whether the hook works | | | the first sentence and the first image (hypothesis: hook of the next video) |
| **Average percentage viewed** | whether the pace holds | | | the pace: Austin runs ≈ 187 words per minute, test `speed` 0.95 next |
| Engaged views | what the algorithm rewards | | | the ending and the pinned comment |
| Shares and comments | whether it is worth passing on | | | the stakes in scene 2 and the ending |
| Subscribers gained | whether the brand converts | | | the channel page (banner, description) |

One change at a time, written in the next Status note ([[Feedback loop]]).

## 10. Checklist before pressing publish

- [x] Watched and approved by the user ("Its perfect", 5 Oct 2026); the scene 1 A/B was not mentioned, so the default take stays.
- [ ] Facts to recheck from [[Battery and lithium - Status]] (the 18-month figure, IEA's 60 %, CATL's claims, the two Chinese notices).
- [ ] Title, description, hashtags and pinned comment pasted; photo credits intact.
- [ ] Thumbnail uploaded or the opening frame chosen; audience set to *not made for kids*; the synthetic-content question answered.
- [ ] Scheduled in the weekly slot; after publishing: pin the comment, then log the 24 h numbers in §9.
