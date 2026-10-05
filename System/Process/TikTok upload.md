---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v1 · written from TikTok's public docs and secondary guides; nothing uploaded yet
tags: [tiktok, upload, process, multi-platform]
---

# TikTok upload (same master, native upload)

← [[YouTube Channel]] · [[YouTube upload]] · [[Channel strategy]] §5 · [[Fast workflow]] · [[Shorts quality bar]]

**Rule:** TikTok gets the **same 9:16 master** as YouTube (burned-in word captions, no watermark, no in-video branding), **uploaded natively**; never re-upload a download carrying another platform's mark. **Route today: manual upload by the user** (TikTok Studio on the web, or the app). The agent prepares the package; the user posts.

## 1. Why not the API (deferred, YAGNI)

The Content Posting API's Direct Post from an **unaudited client is limited to private (`SELF_ONLY`) posts and five users per 24 h**; lifting it needs a TikTok audit of the app ([TikTok docs](https://developers.tiktok.com/docs/en/content-sharing-guidelines)). It also needs a developer app and an approved product. One Short a week is cheaper by hand. Revisit if the cadence passes ≈ 5 a week or a scheduler is wanted. Not verified: audit lead time.

## 2. The package (agent, per video, after the YouTube package)

Add a `## TikTok` section to the video's `Upload - <Topic>` note ([[Upload - Copper and the AI race]] is the model):

| Field | Rule |
| --- | --- |
| **File** | the same `render/*.mp4` (1080×1920); check it opens and is under the app's size limit (**unverified**, a ≈ 65 to 80 MB render has not been tried) |
| **Caption** | the claim in plain words + 3 to 5 hashtags (1 broad such as `#science`, 2 to 3 on the topic); **no sources wall**: TikTok captions are short, put the 1 to 2 key sources as `Source: <name, date>` and the full list in the pinned comment |
| **Cover** | a frame with the hook readable inside the safe zone (pick in the upload screen) |
| **Pinned comment** | the sources and corrections, same text as YouTube's |
| **On-screen text check** | see §3 |
| **Settings** | see §4 |

## 3. Safe-zone test (once, then record the result)

TikTok's interface covers the **right edge and the bottom ≈ 20 %** (caption, buttons) ([guide](https://zeely.ai/blog/tiktok-safe-zones/), a secondary source). Our captions sit **16.5 % from the bottom** (`CAP_Y`), tuned for Shorts. **First video only:** upload privately, open it in the app, check captions, plates' key labels and number cards are not covered. If they are, raise `CAP_Y` for a TikTok export (`plan.json`) and record the value in [[Channel strategy]] §5; do not change the YouTube master for it.

## 4. Settings at upload (user)

1. **AI-generated content: turn the disclosure ON.** The channel uses AI voice and generated plates; TikTok requires labeling realistic AI media and detects it through C2PA metadata anyway ([TikTok support](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)). Honest labeling costs nothing and avoids a removal.
2. **Visibility:** private first for the first video (§3), then public; **schedule** from TikTok Studio if wanted.
3. Allow comments; allow Duet/Stitch as the user prefers (**decision pending**, record it here).
4. **Music:** the video carries its own synthesized sound design; do not add TikTok library sounds.

## 5. After posting

Record in the video's Status note: link, date, 48 h and 7 d views, average watch time, shares, followers gained (TikTok Studio / Analytics). Use it in the [[Channel strategy]] §6 loop **next to YouTube's**: same hook, different audience, so compare per video. Creator Rewards eligibility: not verified.

## 6. Not verified

No video has been uploaded to TikTok. After the first one, fix this note with what differs (size limit, cover picker, safe zone, label wording) and add the account handle.
