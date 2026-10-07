---
type: research
created: 2026-10-06
updated: 2026-10-06
status: DRAFT for the user's approval; nothing uploaded; `publish.py` rewrites this note at upload
tags: [upload, youtube, week-01]
---

# Upload · Netflix screenshot (draft)

← [[Netflix screenshot - Status]] · [[Script - Netflix screenshot]] · [[Publish]]

Render: `Media/Week 01/2026-10-06 Tue/Netflix-screenshot/render/ns-63s-9x16-r1.mp4` (63.1 s). Visibility proposed: **private first**. Approval: **pending** (title, thumbnail, description, visibility).

## Thumbnails

Variant B (recommended: half the phone screen goes black) and variant A (plain screen):

![[ns-thumb-b.jpg]]

![[ns-thumb-a.jpg]]

## Titles (pick one)

```text
Why Your Phone Won't Screenshot Netflix
```

1. **Why Your Phone Won't Screenshot Netflix** (recommended, 39 characters).
2. The Black Screenshot: What Your Phone Is Really Doing.
3. Netflix Doesn't Catch Your Screenshot. Your Device Refuses to Copy It (only if a source says Netflix's own app does not set the flag).

## YouTube description (paste as is)

```text
A screenshot of a streamed movie comes out black because your device leaves protected video out of the copy: Android, iPhone and Windows each have a switch an app can set. The app is only told about a screenshot afterwards.

New Shorts every day.

SOURCES
- Android: FLAG_SECURE makes screenshots blank: https://developer.android.com/security/fraud-prevention/activities
- Apple: protected video is blacked out in recording, mirroring and AirPlay; sound is not: https://developer.apple.com/documentation/uikit/uiscreen/iscaptured
- Apple: the screenshot notification posts after the screenshot: https://developer.apple.com/documentation/uikit/uiapplication/userdidtakescreenshotnotification
- Windows: SetWindowDisplayAffinity and Microsoft's caveat: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowdisplayaffinity
Behaviour differs by device and app version. The video says apps can mark their video as protected; it does not claim how any one streaming app implements it. Figures checked on 6 October 2026.

PHOTO CREDITS (Wikimedia Commons)
Sage Ross, CC BY-SA 4.0 | Ajsm712, CC BY-SA 4.0 | Public domain and CC0 photos: Dave Pape, NeONBRAND, Oceanos y dados

The narration is AI-generated and the diagrams were drawn for this video; the photos are real.

#netflix #screenshot #howitworks #tech
```

First two lines are the claim and the search words; hashtags last (`#howitworks` is the weak one; `#drm` or `#streaming` would replace it).

## Pinned comment

```text
Should a device be allowed to refuse to copy what it shows you? Tell me what you think, and correct me if your phone or laptop behaves differently. Sources are in the description.
```

## Studio settings

Not made for kids; synthetic-content answer: yes (AI voice, drawn and generated diagrams); captions: upload `render/ns.srt` by hand.

## TikTok (draft)

```text
A Netflix screenshot comes out black because your device refuses to copy protected video. Android, iPhone and Windows each do it their own way. Should a device be allowed to refuse? #netflix #screenshot #tech #howitworks
```

## Claims

| Claim | Source | Strength |
| --- | --- | --- |
| Android `FLAG_SECURE` makes screenshots blank and keeps the window off non-secure displays | Android developers, Secure sensitive activities | primary, read 6 Oct 2026 |
| iPhone blacks out FairPlay-protected video in recording, mirroring and AirPlay; the sound is still included | Apple docs, `UIScreen.isCaptured` | primary |
| The iPhone screenshot notification posts after the screenshot | Apple docs | primary |
| Windows `WDA_MONITOR` shows the window only on a monitor; Microsoft says it is no guarantee | Microsoft Learn | primary |
| "Netflix does not have to notice": the blocking is done by the system | agent's reading of the four pages; **no Netflix source** | inference |

## Checklist

- [ ] User approves title, thumbnail, description, visibility
- [ ] `python3 System/scripts/publish.py "Media/Week 01/2026-10-06 Tue/Netflix-screenshot/upload/publish.json"` (set `approval` first)
- [ ] `render/ns.srt` uploaded by hand; pinned comment posted by hand
