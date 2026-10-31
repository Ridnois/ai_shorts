---
type: rules
updated: 2026-10-29
status: v1 · 29 Oct 2026: audience, ideas, package, publish, algorithm, policy and analytics in one note, from the research of 29 Oct 2026. Replaces Audience and Publish
---

# Growth: audience, ideas, package, publish, numbers

What to make: [[Format]]. How: [[Production]]. The user's own research notes: [[User insights]].

## Audience and niche

Curious adults who use ChatGPT, Claude or Gemini every week and feel they are missing how it works or how others use it so well; developers and knowledge workers who want agents to do real work. Plain words first; the expert gets one detail they did not know.

**Y and X:** Y is the result the viewer already wants (stop being fooled, get more done, see the change coming); X is the mechanism that blocks it. The title sells Y, the video teaches X. **News is the case, never the video:** a launch or incident opens an evergreen mechanism that is still true in a year.

## Ideas (outliers, not guesses)

1. Search the viewer's plain question: `python3 System/scripts/youtube_search.py "<q>" ["<q2>"] --short --min-ratio 3` prints videos that did 3x or more their channel's median (YouTube Data API key in `.env`).
2. Go one level deeper from each outlier (its channel's other outliers); stop when topics repeat. Note **why** people clicked (a result they want, faster than expected, an unfair-advantage feeling), never copy words or looks.
3. Keep the best rows in `Pipeline/Niche map.md` (40 lines or fewer) and ideas as notes in `Pipeline/Ideas/` (template: `Pipeline/Idea template.md`).
4. Also free: YouTube Studio's Research tab and "Ask Studio" (search gaps), autocomplete, r/ChatGPT and r/LocalLLaMA top posts of the week, the AI Incident Database, lab blogs and system cards.

**Reference channels** (study the pattern, not the look): Zack D. Films (frame 0 shows the outcome; 20 to 45 s; one idea), Fireship (fixed series promise, dense and dry), Two Minute Papers (the real output is the proof), Kurzgesagt (recognisable from one frame), ByteByteGo (clean system diagrams), Jared Owen and Branch Education (machines as cutaways).

## Package

- **Title** (100 characters or fewer, 40 to 60 is best): the plain search words first, a named thing, the curiosity gap; no all caps, no emoji. "Why ChatGPT can't count letters", not "The hidden truth about tokens".
- **Frame 0 is the real thumbnail** in the Shorts feed: the hook's picture plus 3 to 5 words. A custom thumbnail (`v.thumb`, one focal picture, 3 to 4 words at 110 px or more, inside x 40 to 1040, y 600 to 1320) shows only on the channel page, search and home, and is accepted for Shorts only after the Partner Program.
- **Description:** first line = the claim with the search words; sources with links; the channel line; 2 to 3 hashtags (`#AI` plus one topic tag). **Tags:** 5 to 10 search phrases (weighted little).
- **Pinned comment:** one question the viewer can answer in a word.

## Publish

- **Cadence:** Mon to Fri at one fixed hour (15:00 UTC unless the numbers say otherwise), never two on one day. Schedule with `publish_at`.
- **Always confirm the pack** (title, description, thumbnail, visibility) with the user before an upload; default private.
- `publish.py` builds the 4K master when missing, uploads it with language `en`, category 28, tags and the synthetic flag, sets the thumbnail, writes the csv row, the Upload note and the Status line. `--dry-run` builds the pack only; `--resume <id>` after a crash.
- **Auth:** one OAuth token (upload, read-only channel and analytics) from the Desktop client "Redtail Uploader" in Google Cloud project `redtail-upload`. `youtube_auth.py` checks every token against the NextToken channel (`UCCZX7-YPNPntwPKI1hdv2hQ`, @yournexttoken) and stops on any other, so nothing reaches the owner's personal channel. The OAuth app is in Testing, so the token expires every 7 days: on HTTP 400 the user runs `python3 System/scripts/youtube_auth.py` and picks **REDTAIL** (Google's account picker still shows the channel's old name) at "Choose your account or a brand account". Run the YouTube scripts from the vault root; its `.env` (gitignored, 0600) holds `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`. Quota: 1,600 of 10,000 units per upload. Never print a token.
- **The repo is public** and the vault auto-commits: keys live only in `.env`. `secret_scan.py` runs in `check_vault.py` and as the pre-commit hook (`git config core.hooksPath System/scripts/githooks`, set on 30 Oct 2026); a blocked commit means a key is in a file.
- **TikTok** (manual): upload `upload/*-tt.mp4` from TikTok Studio on the web, caption from the pack, no TikTok library sound. Label AI content when a video shows realistic generated imagery. TikTok search reads the spoken words, the on-screen text and the caption: the keyword in all three. Creator Rewards pays only for videos of 1 minute or more: once the account qualifies, cut a 61 to 70 s TikTok version.
- **Master check (open):** compare "Stats for nerds" on the first private 4K upload; write the codec seen here.

## Algorithm (2025 to 2026)

- Most Shorts views come from the feed, where nobody chose the video: **viewed vs swiped away** (aim 70 % or more; under 60 % is a hook problem) and **average percentage viewed** (aim 80 % or more at 45 to 60 s) decide whether YouTube shows it to more people. Likes and comments matter far less.
- Since 31 March 2025 a "view" is every start or replay; **engaged views** are the old count and the one the Partner Program uses. Compare videos on engaged views. A loop ending raises replays.
- Shorts can grow for weeks; judge at 7 d and 28 d, not in the first hours.
- Shorts can run up to 3 minutes; this channel runs 45 to 60 s ([[Format]]). In the Galloway study (5,400 Shorts), 50 to 60 s Shorts that held attention did best.

## Policy

- **Inauthentic content** (renamed 15 Jul 2025): not monetisable when "mass-produced, generic, repetitive", "templated storylines" or "AI-generated content made with generic or unoriginal templates"; it applies to the **whole channel**. Defence: every video has a distinct real case, an original figure or capture, a real argument and a sourced number; the brand is consistent, the videos are not interchangeable.
- **Disclosure:** the "altered or synthetic" label is for realistic generated people, places or events; drawn animation with a stock TTS narrator does not need it (`synthetic: false`). Set `synthetic: true` when realistic generated stills or clips appear. Never clone a real person's voice. The description carries an AI line either way.
- **Partner Program:** 1,000 subscribers plus 10 M engaged Shorts views in 90 days, or 4,000 public watch hours in 12 months.
- No malicious clickbait: the hook promises only what the video shows. Claims about a model, price or feature are re-checked if the render is over 30 days old.

## Analytics

- `Analytics/videos.csv` (one row per upload, written by `publish.py`), `Analytics/snapshots.csv` (video × platform × age), `Analytics/Report.md` (generated by `analytics.py report`; never edit it by hand).
- Pull at 24 h, 7 d and 28 d: `youtube_analytics.py pull` then `analytics.py report`; TikTok numbers typed with `analytics.py add "<Video>" tiktok 7d views=… avg_view_s=…`.
- **First lever when low:** viewed vs swiped → frame 0 and the first sentence · average percentage viewed → length and the middle · replays → the loop ending · subscribers → series consistency.
- **Under 100 views, change nothing.** One change per video so the next pull can attribute it. Every 10 uploads, run the [[Feedback loop]] on the data and replace the targets above with the channel's own medians.

## Sources (29 Oct 2026)

YouTube upload specs (support.google.com/youtube/answer/1722171) · inauthentic content policy (support.google.com/youtube/answer/1311392) · Shorts up to 3 min (answer/15424877) · view count change (TechCrunch, 26 Mar 2025) · custom Shorts thumbnails for Partner Program, desktop, from 25 Jul 2026 (PPC Land) · Paddy Galloway's Shorts study (5,400 Shorts, 33 channels; date uncertain, before the 2025 view change) · VP9 for 1440p and above uploads (Streaming Learning Center; not tested for Shorts) · TikTok Creator Rewards 1 minute rule (2026 creator guides, unverified). Vendor blog numbers (caption lifts, cut rates) are treated as untested.
