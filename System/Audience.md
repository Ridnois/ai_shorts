---
type: rules
updated: 2026-10-06
status: v1 · niche, deep-first search, outcome and mechanism, package (title + thumbnail) and opening; from [[User insights]] (6 Oct 2026)
---

# Audience: niche, search, package, opening

Owns everything that happens **before the click and in the first seconds after it**. Idea gate: [[Playbook]] §1. Package fields: [[Playbook]] §2b. Thumbnail build: [[Workflow]] §Thumbnail. Metrics: [[Publish]].

## Niche

**Technology and the physical and digital systems under it:** IT, engineering, human progress, global resource management, programming, civil engineering. Not general science. A topic outside this list needs one line saying which of the six it serves. Topic families for the spread rule: computing, networks, software, structures, materials and resources, energy and grid, manufacturing.

## Outcome and mechanism (the idea frame)

*"If you do not understand X (the mechanism), you do not understand Y (the outcome)."* **Y** is the result the viewer already wants; **X** is the thing they did not know was in the way. Each idea note states both in one line each.

- Direct demand for Y exists (searched, shared, outperforming videos) → build the video around Y and let X be the surprise.
- No demand for X alone → **bridge**: title and thumbnail sell Y; the video delivers X as the reason.
- Specific beats broad even if reach shrinks: the right viewer feeling understood is worth more than generic views.

## Deep-first search (P1, before choosing an idea)

1. Write 3 searches per topic family in the viewer's words (the plain question, not the jargon).
2. For each search open the results; note **outliers**: videos (Shorts included) with views far above their own channel's usual (about 5x or more). One level deeper from an outlier: its channel's other outliers, then its recommendations.
3. **When a branch stops giving new information, go back up and open another.** Stop when subjects, wording and formats repeat: the niche is understood, not one competitor.
4. For each outlier record **why people wanted to click** (the result they already want, faster than expected, an unfair-advantage feeling), never its words or looks.
5. Write it in `Pipeline/Niche map.md` (one line per outlier: link, views vs channel norm, Y, promise, format). Keep ≤ 40 lines; delete rows that were not useful.

**Tool:** `python3 System/scripts/youtube_search.py <query> [more queries] [--short] [--min-ratio 3]` (YouTube Data API, read-only token already in `.env`; 100 quota units per query plus about 2 per channel) prints outliers as Niche map rows: views against the median of the channel's last 10 uploads. Fill the Y, promise and why columns by hand. The browser tool cannot read YouTube pages. Never invent a view count.

## Package: title and thumbnail are one promise

- **The thumbnail is read first.** If the viewer cannot see problem and outcome in a glance, the title is never read. One idea per thumbnail, readable at phone size.
- **Judge beside the competition:** compare the package with 3 videos it will sit next to in search; the question is *does this give the right viewer a clearer reason to choose this one?*
- The promise must be **plain, specific, honest** ("China refines 48 % of copper and mines 8 %"), never a teaser the video cannot pay.
- Do not copy a winner's title; keep the psychology (Y, speed, surprise), change the subject.
- The package is **written at the script phase** ([[Playbook]] §2b) and the script is judged against it.

## Opening: promise, proof, plan

After the click the viewer asks: *am I getting what I clicked for? can this channel deliver it? is the rest worth my time?*

| Beat | Does | In a Short |
| --- | --- | --- |
| **Promise** | restates exactly what the package offered | scene 1 (the hook) |
| **Proof** | a reason to trust: a sourced figure or the named mechanism | scene 2, first sentence |
| **Plan** | where the video goes (the theme line or a count) | end of scene 2 |

Satisfaction is the target, not raw retention: right people click, watch, feel satisfied, YouTube shows it to more like them. A video that wins the click and the watch takes the attention (winner-take-all).

## Analytics link

Record each video's Y and package in its Status note; judge a package by the data in [[Publish]] when it exists, not by taste. Under about 100 views read counts only.
