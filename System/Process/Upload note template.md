---
type: research
created: 2026-10-05
updated: 2026-10-05
status: template · copy to Videos/Week NN/<Topic>/Upload - <Topic>.md at P8; models: Upload - Copper and the AI race
tags: [template, upload, youtube, tiktok, analytics]
---

# Upload note template

← [[YouTube Channel]] · [[YouTube upload]] · [[TikTok upload]] · [[Analytics]] · [[Guidelines for new scripts]] ("Copy-paste text", "Upload package")

Every video gets an `Upload - <Topic>.md` at **P8**, built from this skeleton. **Rules that apply to the whole note:** English; every text the user pastes (description, caption, pinned comment) is in its own ```` ```text ```` block, **plain ASCII** (`-` bullets, `|` separators, no `>` quote marks, no curly quotes, no `<` `>`); the cadence line says **"New Shorts every day."**; sources are real links with a cut-off date; photo credits for CC BY and CC BY-SA; the AI disclosure line; 3 to 5 relevant hashtags last.

## Skeleton (sections, in order)

1. **Header and status:** video embedded, render path, duration, word count; status line (not uploaded, uploaded and visibility, id).
2. **Titles:** three candidates (≤ 100 characters, keyword first, no banned words), one recommendation and why.
3. **YouTube description** (code block): claim and search words in the first two lines, "New Shorts every day.", SOURCES, PHOTO CREDITS, the AI line, hashtags last.
4. **Hashtags:** five, relevant.
5. **Thumbnail:** candidates and the pick (the Partner Program route, or the opening frame).
6. **Pinned comment** (code block): a one-line question plus the invitation to correct a figure.
7. **Studio settings:** visibility and the daily slot, not made for kids, the synthetic-content answer, playlist.
8. **TikTok** (the `## TikTok` section; steps in [[TikTok upload]]): file (upload from the web), cover, visibility (**Only me first on the very first TikTok video** for the safe-zone test, then Everyone), AI-generated content **ON**, caption (code block, the claim plus 1 to 2 key sources plus 3 to 5 hashtags), pinned comment (code block), checklist.
9. **Why these choices:** a table of claims, sources and strength (official, trade press, third-party hypothesis).
10. **After publishing:** do **not** keep a metrics table here; the numbers live in `Analytics/snapshots.csv` ([[Analytics]] §3). Write only the reading guide (what each low metric means and what to change first, from [[Analytics]] §2) and a link to the report.
11. **Checklist before pressing publish:** facts rechecked; description, hashtags and pinned comment pasted intact; thumbnail; settings; `Analytics/videos.csv` row filled (`youtube_id`, `published`, words, duration, `hook_type`); run `youtube_analytics.py pull` at about 24 h, 7 d and 28 d.
