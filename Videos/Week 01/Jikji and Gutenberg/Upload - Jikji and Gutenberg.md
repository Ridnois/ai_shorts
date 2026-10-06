---
type: research
created: 2026-10-05
updated: 2026-10-05
status: UPLOADED private (video id a3faPJ87qsk), short cut (39 s) with thumbnail set via the API; visibility, pinned comment and TikTok are the user's
tags: [youtube, upload, week-01, jikji, printing, shorts]
---

# Upload · Jikji and Gutenberg (Week 01)

← [[Jikji and Gutenberg - Status]] · [[Script - Jikji and Gutenberg (short)]] · [[Publish]] · [[Upload - Copper and the AI race]]

User request (5 Oct 2026): *"Upload the last video to youtube, make sure you upload the thumbnail too"*. "The last video" = the **short cut** (39 s, 91 words); the 62 s version is not uploaded. No visibility was named, so it went up **private** (the default in [[Publish]]).

## Upload result

`System/scripts/youtube_upload.py` (private, Science & Technology, not made for kids, `containsSyntheticMedia: true`): id **a3faPJ87qsk**, https://studio.youtube.com/video/a3faPJ87qsk/edit, https://youtu.be/a3faPJ87qsk. File `Media/Week 01/Jikji-short/render/jks-39s-9x16-r1.mp4`. The first attempt died on a dropped connection (`RemoteDisconnected`); the second worked. The Data API pull then listed 4 videos, so no duplicate exists. **Thumbnail set** (`thumbnails.set`, the API answered "thumbnail set"): `upload/thumb-jk.jpg`, text **BEFORE GUTENBERG** (second line orange) over a real page of the Jikji (public domain), made with `make_thumbnail.py`, no image generated ($0). **The user found no custom thumbnail in Studio** (set while the video was still processing); re-set with `youtube_upload.py thumb a3faPJ87qsk` (HTTP 200) and the served `maxresdefault.jpg` now shows the text (checked 5 Oct 2026).

## Title (52 characters)

```text
The First Metal-Type Book Is Not the Gutenberg Bible
```

Keyword first, no banned word. Alternatives: "A Printer's Mistake Proves Korea Beat Gutenberg" (47); "The Korean Book That Beat Gutenberg by 70 Years" (47).

## Description (1,660 characters, plain ASCII)

In `Media/Week 01/Jikji-short/upload/desc.txt`: the claim and search words first, "New Shorts every day.", five sources as links (BnF, Global Jikji, Open Culture, Wikipedia, Utah), the Gutenberg dating note (73 to 78 years), PHOTO CREDITS for the CC BY and CC BY-SA photos, the AI line, then `#Jikji #Gutenberg #printing #history #Korea`.

## Pinned comment (post by hand)

```text
Jikji printed first. Gutenberg's press changed Europe. Who gets the title "inventor of printing"? Vote Jikji or Gutenberg below. If I got a date wrong, tell me and I will pin the correction.
```

## Studio settings

Not made for kids. Altered or synthetic content: the script sent "yes" (the channel's choice); you decide. Upload `Media/Week 01/Jikji-short/render/jks.srt` by hand if you want captions as a track. TikTok: not prepared.

## Claims to recheck before making it public

| Claim | Source | Strength |
| --- | --- | --- |
| Printed 1377 at Heungdeok Temple near Cheongju; the postscript says cast metal type | BnF, Global Jikji (read) | solid |
| Upside-down, omitted and tilted characters are the evidence | Wikipedia and UNESCO summary (not opened) | **weakest**: open the UNESCO nomination before relying on it |
| "Over seventy years before Gutenberg" (73 to 78) | Gutenberg dated 1450 to 1455 by source | solid, range stated |
| Oldest known metal-type book; free on Gallica | BnF (read) | solid |

## Not verified

I have not heard or watched the video. The reused voice takes (scenes 1 and 3) may sit slightly differently beside the new ones; check "Jikji" and "Cheongju" by ear. The srt name above is the builder's usual `<prefix>.srt`.
