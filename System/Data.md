---
type: rules
updated: 2026-11-03
status: v2 · 3 Nov 2026 vault rebuild. Owns the numbers before and after an upload, the review and the feedback loop. Replaces Growth §Algorithm and §Analytics and the Feedback loop note
---

# Data: learn from every upload

What we make: [[Strategy]]. The words: [[Story]]. The picture: [[Picture]]. Commands: [[Build]]. Generated report: [[Report]].

## What decides reach (Shorts, 2025 to 2026)

- Most Shorts views come from the feed (our median `feed_pct` is 80 to 90 %), where nobody chose the video. **Viewed vs swiped away** and **average percentage viewed** decide whether YouTube shows it to more people. Likes and comments matter far less.
- Since 31 March 2025 a Shorts **view** is every start or replay. **Engaged views** are the old count, and the one the Partner Program uses: compare videos on engaged views. `audienceWatchRatio` counts replays, so it can exceed 1; read its shape, not its level.
- Shorts can grow for weeks: judge at 7 d and 28 d, not in the first hours. Our first 24 h usually stops near 1.1 k to 1.4 k views (the feed's test batch); the 7 d number is the verdict.

## Before the upload: the pre-flight card

Written in the Status note when the script is done (`/short-script`), five lines:

1. **Hook pattern** (an id from [[Strategy]] §Hooks) and its [[Radar]] evidence.
2. **Title against the field:** the 5 nearest Radar outlier titles; why ours is the clearer choice.
3. **First 7 seconds:** the hook line, the stake line, and what is on screen at 0 s, 3 s and 6 s. The 4 to 7 s window is where we lose people (§Review).
4. **Weakest beat:** the beat most likely to lose viewers, and why.
5. **Prediction:** engaged views at 7 d, against our median (above, at or below).

At 7 d the agent writes the result next to the prediction. The report counts the hit rate.

## After the upload

| When | Command (vault root) | What it gives |
| --- | --- | --- |
| daily (scheduled, [[Build]] §Schedule) | `youtube_analytics.py pull && analytics.py report` | every video's live counts (Data API), rates and traffic source (Analytics API, lags 1 to 2 days), and the 100-point retention curve with `relativeRetentionPerformance` |
| 24 h and 7 d after an upload | the user reads **viewed vs swiped** from Studio (Content › Shorts) and the agent types it: `analytics.py add "<Video>" youtube 7d viewed_pct=…` | the one key number no API returns |
| any time | `analytics.py beats "<Video>"` | where viewers left: hold at 3 s, the two steepest drops with the words spoken there, a frame of each drop (`render/_drops/`) |

`Analytics/Report.md` (generated, never edited by hand) holds the windows (24 h, 7 d, 28 d), the cuts by series, hook pattern and main medium, and the "where viewers leave" table. Rules for reading it:

- **Under 100 views, change nothing.** Groups of 1 are anecdotes. One change per video, so the next pull can attribute it.
- **First lever when low:** viewed vs swiped low → frame 0 and the first sentence; average % viewed low → the drop beats in `beats`; a low curve end → the loop ending; no subscribers → series consistency.

## Review (every 10 uploads; the first ran 3 Nov 2026 on 18 videos)

Steps: pull, report, then read the cuts and the drops. Replace the targets below with the new medians. Name the best and worst pattern and medium. Edit the one rule that owns the gap (§Feedback loop).

**Targets (our medians, 7 d, 16 videos, 3 Nov 2026):** 793 views · **368 engaged views** · **59 % average viewed** · 80 % from the Shorts feed · hold at 3 s 95 % of start. A video is *above* when its engaged views beat 368 at 7 d. Outside benchmarks (70 % viewed vs swiped, 80 % average viewed) are retired until we record our own viewed-vs-swiped median.

**Findings of 3 Nov 2026:**

1. **We lose people at 4 to 7 s, on a citation.** In 12 of 14 curves the steepest drop sits between 4 and 7 s, on words that source the hook instead of raising its stakes: "was July 2025. Founder" (Agent deleted a database), "a 2019 paper, Frankle and Carbin" (Lottery ticket), "WHO counted it." (Antibiotics), "Therabot, in a trial of 210 people" (Therapist), "is a dial in Claude Code. Low," (Effort). → [[Story]] §Beats: the stake line raises the stakes; names, dates and papers go on screen, not in the voice, before 10 s.
2. **Series:** What's coming (median 788 engaged, n=2) and Agent at work (680, n=4) beat How AI works (631, n=7), and both hold better (75 % and 62 % average viewed against 55 %). How AI works is our most made and our weakest on average viewed; its hooks need a real case, not a concept.
3. **Patterns:** `incident` (721, n=3), `surprising-result` (703, n=4) and `cost-why` (658, n=2, with the best average viewed, 72 %) lead. `name-it` (195, n=1) and `stakes` (363, n=2) trail. Off-niche (Antibiotics) is the worst on every number and is no longer made ([[Strategy]] §Series).
4. **Medium: no winner yet.** Capture-led videos (59 % average viewed, n=3) and figure-led ones (57 %, n=10) hold about the same. The two best curves (Effort level, a recorded run, and ETH, a figure: ends 0.64 and 0.62, `rel` 0.7) both show a real output on screen in the mechanism. → [[Picture]] §Medium: every video shows one real run or real model output; the new primitives get tagged `primitive` so the next review can compare them.
5. **Length:** every video is 40 to 60 s, so length cannot be judged yet. The next compact (35 to 45 s) video tests it.

## Feedback loop (how the vault learns)

The vault is the single source of knowledge: feedback is done only when the vault says it.

1. **Record** the user's words verbatim in the video's Status note under *Feedback*. A data finding is recorded here under §Review.
2. **Find the gap** in one line: what the video did that the user (or the curve) did not want.
3. **Edit the one rule that owns it:** audience, ideas, hooks, package, policy → [[Strategy]] · words → [[Story]] · picture, medium, pacing → [[Picture]] · look, components, commands, budget, checks → [[Build]] and `hfkit.py` together · numbers and this loop → [[Data]] · agent behaviour → `CLAUDE.md`.
4. **The newest feedback wins:** replace the older rule in the same pass; never keep both. Delete what it replaces (git keeps history).
5. **A fault that comes back twice becomes a check** (an `hfkit` warning, `check3d.mjs`, `pace.py`, a `check_vault.py` invariant), not a reminder.
6. **Apply forward:** renders already waiting ship unless the feedback names a defect in them.
7. **Answer** with what changed where and what is still unverified.

## Instagram (typed by hand at 7 d)

No script reads Instagram: the Graph API needs a professional account linked to a Facebook page and a Meta app, not set up (3 Nov 2026). At 7 d the user reads the Reel's Insights and the agent types them:

`analytics.py add "<Video>" instagram 7d views=… viewed_pct=<100 − skip rate> avg_view_s=… shares=<sends> saves=… subs_gained=<follows>`

- **Skip rate** is the share who swipe away in the first 3 s; 100 minus it is our `viewed_pct`, so it compares with YouTube's viewed vs swiped. Insights also shows *your typical skip rate*: write it in `notes`.
- **Sends** are the signal Instagram names first for reach to non-followers; read them per 1,000 views.
- The Report's cuts use YouTube only; Instagram rows sit in its windows. Compare Instagram to Instagram once 5 Reels have 7 d numbers.

## API facts (checked 3 Nov 2026)

- YouTube Analytics API: `elapsedVideoTimeRatio` gives 100 points per video with `audienceWatchRatio` and `relativeRetentionPerformance` (0 to 1, 0.5 = the median of similar-length videos). Adding `startedWatching`/`stoppedWatching` to that query returns no rows. `insightTrafficSourceType = SHORTS` is the feed. Source: developers.google.com/youtube/analytics/dimensions and /metrics.
- **Viewed vs swiped away is only in Studio**; no API has it (support.google.com/youtube/answer/12220281).
- **Test & Compare does not test Shorts** (support.google.com/youtube/answer/13861714): hooks are tested by the pre-flight card and the curve, not by A/B.
- TikTok numbers are not tracked (the user's decision, 3 Nov 2026). Instagram numbers are typed by hand (§Instagram).
