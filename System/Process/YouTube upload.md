---
type: research
created: 2026-10-05
updated: 2026-10-05
status: v2 · first real upload done 5 Oct 2026 (Copper and the AI race, private); consent lessons added
tags: [youtube, upload, api, process, setup]
---

# YouTube upload (connecting the agent to the channel)

← [[YouTube Channel]] · [[Fast workflow]] · [[Production process]] · [[Channel strategy]]

**Why:** the browser route failed on [[Upload - Battery and lithium]] (Claude in Chrome's `file_upload` takes ≤ 10 MB; a render is ≈ 65 MB). The YouTube Data API has no such limit and also serves the weekly cadence. Tool: `System/scripts/youtube_upload.py` (stdlib, no install).

## 1. One-time setup (the user, ≈ 10 minutes)

1. [Google Cloud Console](https://console.cloud.google.com/) → new project `redtail-upload`.
2. **APIs & Services → Library → YouTube Data API v3 → Enable.**
3. **OAuth consent screen** (Google Auth Platform): user type **External**, app name `Redtail uploader`, your email. Add the scope `…/auth/youtube.upload`. **Add your own Google account as a test user.**
4. **Credentials → Create credentials → OAuth client ID → type "Desktop app".** Copy the client ID and secret.
5. Put them in `.env` (gitignored, next to `REPLICATE_API_TOKEN`):
   ```
   YT_CLIENT_ID=…
   YT_CLIENT_SECRET=…
   ```
6. `python3 System/scripts/youtube_upload.py auth` → a browser opens → sign in **with the account that owns the Redtail channel** (channel `UCCZX7-YPNPntwPKI1hdv2hQ`; if you have several channels, pick Redtail in the account chooser) → accept the "unverified app" warning (it is your own app) → paste the printed `YT_REFRESH_TOKEN=…` line into `.env`.
7. **Consent screen → Publish app (In production).** Do this *before relying on the token*: while the app is in **Testing**, Google expires the refresh token after **7 days**. An unverified production app only shows the warning screen and works for your own account.

## 2. Uploading (the agent)

```
python3 System/scripts/youtube_upload.py upload "Media/Week NN/<Video>/render/<file>.mp4" \
  --title "<title from the Upload note>" --desc-file <description.txt> \
  --thumb "Media/Week NN/<Video>/upload/thumb-b.jpg" [--privacy private] [--publish-at 2026-10-12T15:00:00Z]
```

- **Default is `private`** and the agent never passes `public` unless the user said so for that video; `--publish-at` (UTC, needs `private`) schedules it. Upload is an outward-facing step: **confirm title, description, thumbnail and visibility with the user first**, then record the video id and the Studio link in the `Upload - <Topic>` note.
- Description: the §3 block of the Upload note saved to a temp file (scratchpad), including `#Shorts` and credits. A vertical video ≤ 3 minutes is a Short automatically; there is no API flag.
- The script sets `containsSyntheticMedia: true` (AI-assisted channel; YouTube's altered/synthetic-content disclosure). Change it only on the user's say-so.
- Not in the script (YAGNI): captions upload (`render/*.srt` stays a manual Studio step), playlists, comments (the pinned comment is posted by hand), resuming a dropped upload.

## 3. Gotchas (from Google's documentation, not yet seen live)

| Gotcha | Consequence |
| --- | --- |
| **Unaudited API projects (created after 28 July 2020) have uploads locked to private.** | Every API upload lands private until the project passes the [YouTube API Services audit](https://support.google.com/youtube/contact/yt_api_form). Fine while the plan is "private until the user schedules"; to let the script publish, file the audit form or switch visibility by hand in Studio. |
| Quota: `videos.insert` costs 1,600 units of 10,000 per day | ≈ 6 uploads a day; plenty for weekly Shorts. A failed attempt still spends quota. |
| Testing-mode refresh tokens last 7 days | §1 step 7. If `invalid_grant` appears, run `auth` again. |
| Scope `youtube.upload` only | The token cannot read, edit or delete videos; changing a title later is done in Studio. |
| Thumbnails | `thumbnails.set` works only if the channel may use custom thumbnails; for a Short that needs the Partner Program ([[Fast workflow]] §4.9). The script reports the failure and keeps the upload. |
| Secrets | `.env` is gitignored; never print the token or paste it in a note. |

## 4. Not verified

The script and the steps above were written from API documentation and **have not been run**: no OAuth client exists yet, so nothing has touched the channel. First real upload = a private test of the Battery and lithium render; check in Studio that the title, description, thumbnail, synthetic-content flag and the Short classification came out right, and fix this note with what differs.

## 5. First real run (5 Oct 2026): what happened

- **Consent error "Access blocked… 403 access_denied":** the consent link opened in the user's *default browser*, which was signed into a different Google profile ("REDTAIL") that was not on the app's test-user list. **Fix: open the link in the profile signed in as the account on the test-user list** (here `s.altamiranorid@gmail.com`), pick the Redtail channel if asked, then Advanced → Go to the app → Allow. Claude in Chrome cannot operate accounts.google.com, so the consent click is always the user's.
- **"Publish app" is greyed out while the app has a logo:** a logo on the consent screen requires Google verification before publishing. Choices: stay in **Testing** (the refresh token lasts 7 days: run `auth` again each week) or remove the logo, then publish (unverified production shows the warning once, no 7-day expiry). The user's app is still in Testing.
- **The token goes to `.env` without being printed** (`YT_REFRESH_TOKEN`); the agent never echoes it. The `auth` command waits on `127.0.0.1:8765` for one redirect: start it in the background and watch its output.
- **Upload worked:** 81 MB in one streamed PUT, private, `uploaded <id>`; Studio showed the metadata, the video still processing.
- **Thumbnail:** none sent (not made; Shorts thumbnails need the Partner Program).
