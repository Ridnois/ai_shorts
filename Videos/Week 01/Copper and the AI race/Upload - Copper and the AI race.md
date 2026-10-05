---
type: research
created: 2026-10-05
updated: 2026-10-05
status: UPLOADED (video id YRX0VfpPMtU, sent as private; Studio showed it Public when last looked, changed by the user); thumbnail added via the API; pinned comment is the user's
tags: [youtube, upload, week-01, copper, ai, shorts]
---

# Upload · Copper and the AI race (Week 01)

← [[Copper and the AI race - Status]] · [[Script - Copper and the AI race]] · [[YouTube upload]] · [[Upload - Battery and lithium]]

User request (5 Oct 2026): *"Upload the last video to youtube, you have credentials on .env now"*. The last video is **Copper and the AI race**. Same rules as [[Upload - Battery and lithium]]: the claim and search words first, sources as links, photo credits, the AI line, 5 relevant hashtags last. **Visibility: private** until the user chooses to publish (an unaudited API project is locked to private anyway, [[YouTube upload]] §3).

## Upload result (5 Oct 2026)

Uploaded with `System/scripts/youtube_upload.py` (the first real run): video id **YRX0VfpPMtU**, Studio link https://studio.youtube.com/video/YRX0VfpPMtU/edit, share link https://youtu.be/YRX0VfpPMtU. **Sent as private**, category Science & Technology, not made for kids, `containsSyntheticMedia: true`. Studio showed the title and the full description as written; **the file was still processing** (checks pending) when the agent looked, so visibility, the HD version and the copyright checks were not confirmed. No thumbnail was sent. **To do by the user:** wait for processing, choose the visibility or a schedule, post the pinned comment, decide the synthetic-content answer, upload `render/cu.srt` if wanted.

## Video

![[cu-61s-9x16-r1.mp4|320]]

`Media/Week 01/Copper-AI/render/cu-61s-9x16-r1.mp4` · 60.8 s · 1080×1920 · 160 words · Austin · captions centred (new layout). Subtitles: `render/cu.srt`.

## Title (34 characters)

**Why Copper Could Limit the AI Race**

Keyword first, hedged like the script ("may be geology" → "could limit"), no banned word. Alternatives: "Copper Takes 17 Years to Open a Mine. Can AI Wait?" (49); "One AI Rack Holds 2 Miles of Copper Cable" (41, the hook).

## Description (1932 characters)

> One AI server rack can hold over two miles of copper cable, yet AI is only a small slice of the world's copper. Why a new mine takes about 17 years, and why that could limit the AI race.
>
> New Shorts every day.
>
> SOURCES
> • S&P Global, copper supply gap study, 8 January 2026 (17 years from discovery to production; a 25% shortfall by 2040 is a forecast): https://press.spglobal.com/2026-01-08-Substantial-Shortfall-in-Copper-Supply-Widens-as-the-Race-for-AI-and-Growing-Defense-Spending-Add-to-Accelerating-Demand,-New-S-P-Global-Study-Finds
> • USGS, Mineral Commodity Summaries 2026, Copper: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-copper.pdf
> • IEA, Global Critical Minerals Outlook 2025: https://www.iea.org/reports/global-critical-minerals-outlook-2025/overview-of-outlook-for-key-minerals
> • Nvidia GB200 NVL72, about 5,000 copper cables and over 2 miles per rack (Nvidia's figures, as reported by LightCounting): https://www.lightcounting.com/research-note/april-2024-all-eyes-on-nvidia-352
> • Copper in electric cars, 83 kg against 23 kg (ICSG 2018, cited in this study): https://www.sciencedirect.com/science/article/abs/pii/S0921344920305152
> • How porphyry copper deposits form (Nature Reviews Earth & Environment, 2021): https://www.nature.com/articles/s43017-021-00182-8
> Figures checked on 5 October 2026.
>
> PHOTO CREDITS (Wikimedia Commons)
> Server rack cables: Derrick Coetzee from Berkeley, CA, USA, CC0 · Native copper: Flipin,OG, CC0 · Transformer busbars: Wtshymanski, CC BY-SA 3.0 · Transmission line: Eduardo Sanchez, CC0 · Electric car charging: Julian Herzog (Website), CC BY 4.0 · Copper pipes: Achim Hering, CC BY 3.0 · Chalcopyrite: Didier Descouens, CC BY-SA 3.0 · Chuquicamata mine: Diego Delso, CC BY-SA 4.0 · Bingham Canyon Mine: David Ratledge, CC BY 4.0, and Farragutful, CC BY-SA 4.0
>
> The narration and the schematic are AI-generated; the photos are real.
>
> #copper #AI #datacenters #mining #science

## Hashtags

`#copper #AI #datacenters #mining #science` (inside the description).

## Thumbnail (added 5 Oct 2026)

User: *"I uploaded the lithium video manually and added the thmbnail with no problem, check if you can generate and add one for the las video (copper)"*. Made: hero image with `openai/gpt-image-2` (high, one prediction, [47tndpt7…](https://replicate.com/p/47tndpt73srmy0d11n9r6cd6a4), ≈ $0.25 unconfirmed, a terraced open pit in copper-orange light) plus the text **"17 YEARS TO OPEN A MINE"** composed by `System/scripts/make_thumbnail.py` (entry `thumb-cu`), 1080×1920, 378 KB, text inside the 3:2 band: `Media/Week 01/Copper-AI/upload/thumb-cu.jpg`.

![[thumb-cu.jpg|230]]

**Added through the API** (`thumbnails.set`, the `youtube.upload` scope is enough): YouTube answered `youtube#thumbnailSetResponse`. When the agent looked at Studio afterwards the preview panel was still dark (processing), so **the user should confirm the thumbnail shows**. The channel clearly can use custom thumbnails (the user added one by hand on the lithium video), so the earlier "Partner Program only" assumption does not hold here.

## Pinned comment (post by hand after publishing)

> Which surprised you more: two miles of copper in one rack, or that a new mine takes about 17 years? If I got a number wrong, tell me and I will pin the correction.

## Studio settings

Not made for kids (the script sets it). **Altered or synthetic content: the script sends "yes"** (`containsSyntheticMedia: true`, the guide's choice for an AI-assisted channel); my reading of the policy for the Battery video was "No" (stock narration voice, non-photorealistic schematic): **the user decides which**. Category Science & Technology. Upload `render/cu.srt` by hand if wanted.

## Not verified

Same as the Status note: the rack's 2 miles (Nvidia's claim), the 83 kg per car, the data-center share (my arithmetic), the 17 years as an average. The agent did not watch or hear the video. The CC BY-SA photos sit inside a video that is not CC BY-SA (not legal advice).
