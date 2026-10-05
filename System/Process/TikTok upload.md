---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v2 · "not verified" items checked 5 Oct 2026 against secondary guides (TikTok's own pages would not load); nothing uploaded yet
tags: [tiktok, upload, process, multi-platform]
---

# TikTok upload (same master, native upload)

← [[YouTube Channel]] · [[YouTube upload]] · [[Channel strategy]] §5 · [[Fast workflow]] · [[Shorts quality bar]]

**Rule:** TikTok gets the **same 9:16 master** as YouTube (burned-in word captions, no watermark, no in-video branding), **uploaded natively**; never re-upload a download carrying another platform's mark. **Route today: manual upload by the user** (the API route is in §1) (TikTok Studio on the web, or the app). The agent prepares the package; the user posts.

## 1. The API route (researched 5 Oct 2026; not built)

**Two modes**, both under the Content Posting API ([docs](https://developers.tiktok.com/doc/content-posting-api-get-started)):

| | Direct Post | **Upload (inbox draft)** |
| --- | --- | --- |
| Endpoint | `/v2/post/publish/video/init/` | `/v2/post/publish/inbox/video/init/` ([docs](https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content)) |
| Scope | `video.publish` | `video.upload` |
| Result | posts straight away | the video lands in the user's TikTok **inbox as a draft**; the user taps the notification and finishes the post in the app (caption, cover, AI label, visibility) |
| Unaudited app | **private only** (`SELF_ONLY`), 5 users per 24 h, account must be private ([guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines)) | restriction not stated in the docs; a third-party guide mentions no audit for drafts (**unverified**) |
| Daily cap | about 15 posts per creator per day (guidelines) | not stated |

**Recommendation: Upload (draft) mode.** The user still taps once per video, but that tap is where the AI-generated label, the cover and the safe-zone check happen, which stay a human decision anyway. It avoids needing the Direct Post audit. The agent would do the 65 to 80 MB transfer (chunked `PUT` with `Content-Range`, `Content-Type: video/mp4`) and read the result from `/v2/post/publish/status/fetch/`.

**What the user must do once (≈ 30 min plus waiting):**

1. Register at [developers.tiktok.com](https://developers.tiktok.com/) (a guide says a business email is required and a personal account is not eligible: **unverified**; try the channel's Redtail email).
2. Create an app, add the **Content Posting API** product, request the scope **`video.upload`** (the docs say the app must be approved for it).
3. Redirect URI: `http://127.0.0.1:8765/` (same local listener as the YouTube `auth`); if TikTok refuses a loopback URI, say so and we adapt.
4. Submit the app for review: a demo video of the flow and a privacy policy page are typical requirements (**unverified**; a guide says 5 to 10 business days).
5. While waiting, use the **sandbox** (no review; up to 5 sandboxes, each shareable with 10 accounts): per the docs it cannot post public videos, so it tests the plumbing only.
6. Put `TT_CLIENT_KEY` and `TT_CLIENT_SECRET` in `.env` (never in a note). Access tokens last about 24 h and refresh tokens about 365 days (guide, unverified), so there is no weekly re-login like YouTube's Testing mode.

**What the agent builds once the app is approved:** `System/scripts/tiktok_upload.py` (stdlib only, like `youtube_upload.py`): `auth` (OAuth with PKCE, refresh token to `.env`), `upload <mp4>` (init, chunked PUT, poll status). **Not built yet on purpose:** it cannot be tested before approval, and the scope and review rules above may change what it needs.

**Until then:** the manual route in §2 to §5. At one Short a day, schedule several days at once in TikTok Studio to keep it cheap.

## 2. The package (agent, per video, after the YouTube package)

Add a `## TikTok` section (caption and pinned comment in a plain ```` ```text ```` block, ASCII only: [[Guidelines for new scripts]] "Copy-paste text") to the video's `Upload - <Topic>` note ([[Upload - Copper and the AI race]] is the model):

| Field | Rule |
| --- | --- |
| **File** | the same `render/*.mp4` (1080×1920); MP4 H.264 + AAC is the safe format. **Upload from the web (TikTok Studio, limit ≈ 4 GB), not the phone:** guides give the mobile limit as ≈ 72 MB on Android and ≈ 287 MB on iPhone, and our renders are ≈ 65 to 81 MB, so an Android upload could fail. Default max length is 3 min, no problem for a Short |
| **Caption** | the claim in plain words + 3 to 5 hashtags (1 broad such as `#science`, 2 to 3 on the topic); **no sources wall**: TikTok captions are short, put the 1 to 2 key sources as `Source: <name, date>` and the full list in the pinned comment |
| **Cover** | a frame with the hook readable inside the safe zone (pick in the upload screen) |
| **Pinned comment** | the sources and corrections, same text as YouTube's |
| **On-screen text check** | see §3 |
| **Settings** | see §4 |

## 3. Safe-zone test (once, then record the result)

TikTok's interface covers the **right edge and the bottom 15 to 20 %** (caption, action bar) ([Zeely](https://zeely.ai/blog/tiktok-safe-zones/) says 20 %, [Sendcove](https://www.sendcove.app/integrations/tiktok/video-specs) says 15 %; TikTok's own page gave no numbers). Our captions sit **16.5 % from the bottom** (`CAP_Y`), tuned for Shorts: **inside the risky band**, so the test below is likely to fail. **First video only:** upload privately, open it in the app, check captions, plates' key labels and number cards are not covered. If they are, raise `CAP_Y` for a TikTok export (`plan.json`) and record the value in [[Channel strategy]] §5; do not change the YouTube master for it.

## 4. Settings at upload (user)

1. **AI-generated content: turn the disclosure ON.** The channel uses AI voice and generated plates; TikTok requires labeling realistic AI media and detects it through C2PA metadata anyway ([TikTok support](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)). Honest labeling costs nothing and avoids a removal.
2. **Visibility:** private first for the first video (§3), then public; **schedule** from TikTok Studio if wanted.
3. Allow comments; allow Duet/Stitch as the user prefers (**decision pending**, record it here).
4. **Music:** the video carries its own synthesized sound design; do not add TikTok library sounds.

## 5. After posting

Record in the video's Status note: link, date, 48 h and 7 d views, average watch time, shares, followers gained (TikTok Studio / Analytics). Use it in the [[Channel strategy]] §6 loop **next to YouTube's**: same hook, different audience, so compare per video. 
**Creator Rewards (secondary guides, 5 Oct 2026):** 10,000 followers, 100,000 views in the last 30 days, age 18+, a personal account, and **original videos longer than 1 minute** (shorter ones earn nothing). **Consequence for scripts:** our 130 to 160 words land at ≈ 50 to 65 s (Copper: 60.8 s, **just under or at the line**). Do not stretch Shorts for TikTok; if the program becomes reachable, plan a few 65 to 75 s videos on purpose. Re-check on TikTok's page then.

## Account (set up 5 Oct 2026)

**@redtail_media** (https://www.tiktok.com/@redtail_media), created by the user. Avatar: `Media/_canal/brand-redtail/1.png` (the Redtail logo), set through Edit profile on the web; **it took a few minutes to show** after Save, so reload before retrying. TikTok has no banner. Bio: *Science at full speed. New Shorts every day. Sources in comments.* (changed from "every week" the same day) Display name still `redtail_media` (changeable once per 7 days). The browser tool uploads ≤ 10 MB, so the videos are uploaded by the user.

## 6. Still not verified

- TikTok's **own** pages (AI-label setting wording, safe-zone numbers, Creator Rewards rules) did not load; every number above is from third-party guides that sometimes disagree (mobile size limit, safe zone 15 vs 20 %).
- The exact label in the app, and whether C2PA metadata survives our Blender render (TikTok detects AI media this way, secondary sources).
- No video has been uploaded to TikTok. After the first one, fix this note with what differs and add the account handle.
