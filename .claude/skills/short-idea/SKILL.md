---
name: short-idea
description: Find, test and score Next Token Short ideas from the watchlist radar, early signals, YouTube outliers and real AI cases, and write them into Pipeline/Ideas. Use when the user asks for ideas, topics, "what should we make next", a niche or competitor study, or when /short needs an idea.
---

# /short-idea: ideas from outliers and signals, not guesses

Rules: `System/Strategy.md` (§Hooks, §Ideas, §The idea passes). Read `Analytics/Report.md` first: our own cuts by series and hook pattern feed the *own fit* score.

## Steps

1. **Refresh the radar and signals** from the vault root if older than 7 days: `python3 System/scripts/radar.py pull && python3 System/scripts/radar.py report` (about 100 quota units), `python3 System/scripts/signals.py`. When the token fails, say so and work from the last files.
2. **Read `Research/Radar.md`:** for each Short outlier at 3x or more on an AI topic, write the hook pattern ([[Strategy]] §Hooks) and why people clicked (a result they want, faster than expected, an unfair-advantage feeling). `early` rows are leads only.
3. **Read `Research/Signals.md`:** an *Unexplained* term that keeps rising is a `name-it` candidate; check it against the radar and autocomplete before calling it demand.
4. **Go one level deeper** from the best outliers (the same channel's other outliers; `youtube_search.py "<plain question>" --short --min-ratio 3` for the viewer's question; `radar.py discover` for new channels, added to `Research/Channels.md`). Stop when topics repeat. Never invent a view count. Weekly, also read `Research/Instagram.md` (its watchlist's Reels tabs, by hand) and add outliers to its table.
5. **Real things:** for each candidate, find the named, dated case at its primary source (AI Incident Database, court records, lab blogs and system cards, Epoch AI, METR, arXiv, the product's own docs, or a run we record ourselves).
6. **Test** with the 4 tests and **score** with the table in [[Strategy]] §The idea passes (demand · own fit · showable · real thing). A candidate failing a test is dropped in one line. Write 3 hooks of different patterns.
7. **Write** one note per keeper from `Pipeline/Idea template.md` into `Pipeline/Ideas/<title>.md` with `status: next`, `series`, `hook_pattern`, `medium`, `score`. Never duplicate an idea already in the folder: update and rescore it.

## Output to the user

A table of the top 5 (title, series, pattern, score, the real thing, the radar evidence) and your pick for the next video, with one line on why it beats the others. The next pick never shares the last video's series.
