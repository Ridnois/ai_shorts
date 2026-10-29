---
name: short-idea
description: Find, test and score Next Token Short ideas from YouTube outliers and real AI cases, and write them into Pipeline/Ideas. Use when the user asks for ideas, topics, "what should we make next", a niche or competitor study, or when /short needs an idea.
---

# /short-idea: ideas from outliers, not guesses

Rules: `System/Format.md` §1 and §2, `System/Growth.md` §Audience and §Ideas. Read `Analytics/Report.md` first: the channel's own numbers beat any outside pattern once there are 10 uploads.

## Steps

1. **Seed questions:** write 3 plain questions per series in the viewer's words ("why does ChatGPT lie", "can AI agents use my computer", "why does AI need so much power"). Mix in this week's news only as a case for an evergreen mechanism.
2. **Outliers:** `python3 System/scripts/youtube_search.py "<q1>" "<q2>" … --short --min-ratio 3` from the vault root (the YouTube key is in `.env`; when it fails, say so and use WebSearch for "site:youtube.com/shorts <q>"). Never invent a view count.
3. **Go one level deeper** from the best outliers (their channels' other outliers). Stop when topics repeat. For each keeper write one row in `Pipeline/Niche map.md`: link · views vs channel median · Y · promise · why people clicked. Keep it under 40 lines; delete stale rows.
4. **Real things:** for each candidate, find the named, dated case at its primary source (AI Incident Database, court records, lab blogs and system cards, Epoch AI, METR, arXiv, the product's own docs, or a run we record ourselves).
5. **Test** each with the 4 tests of [[Format]] §2 (real thing, curiosity gap, demand, showable). A candidate failing any test is dropped in one line.
6. **Score** 1 to 5 on curiosity gap, demand, showable and real-thing strength (out of 20). Write 3 hooks of different types (strange fact, number, contradiction, stakes).
7. **Write** one note per keeper from `Pipeline/Idea template.md` into `Pipeline/Ideas/<title>.md` with `status: next`, `series`, `score`. Never duplicate an idea already in the folder: update it instead.

## Output to the user

A table of the top 5 (title, series, score, the real thing, the demand evidence) and your pick for the next video, with one line on why it beats the others. The next pick never shares the last video's series.
