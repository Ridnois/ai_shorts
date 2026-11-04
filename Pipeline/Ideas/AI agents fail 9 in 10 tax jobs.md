---
type: video-idea
status: next
series: What's coming
hook_pattern: surprising-result
medium: capture
score: 18
publish: 
video: 
created: 2026-11-04
updated: 2026-11-04
tags: [youtube, pipeline]
---

# AI agents fail 9 in 10 tax jobs

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim** (one line a stranger would say "wait, why?" to): the best AI agents of November 2026 pass about one real tax job in ten, and the misses are the expensive kind: a deadline nobody asked about.

**Real thing** (named product, company, person or incident, dated, with its source): Surge AI, "DAYJOB: Tax" (surgehq.ai/blog/dayjob-tax, 27 Oct 2026, read 4 Nov 2026): 50 tax environments, 1,789 workspace files (PDFs, spreadsheets, emails). Pass@1 at a 95 % rubric: Claude Sonnet 5.5 10.8 %, Claude Fable 5.1 9.6 %, Claude Opus 5.5 9.2 %. Case: a condo sale where the agent compared the closing dates but missed that the seller's exclusion lapses around August 2027 ("Across five attempts, Astra never identified the deadline. Opus identified it in all five attempts"). No human baseline in the post. HN 266 points.

**Y · X** (the result the viewer wants · the mechanism in the way): to know which money tasks to hand an agent · an agent answers the question it was asked; a professional's value is the question nobody asked, and a 95 % bar punishes one missed issue.

**Hook pattern** (an id from [[Strategy]] §Hooks) and why people click it: `surprising-result`; tax season fear plus "the AI did my taxes in 5 minutes" videos everyone has seen.

**Demand** (rows from [[Radar]] or `youtube_search.py`: link, views, ratio; or the autocomplete): `youtube_search.py "can ai do my taxes" --short --min-ratio 3` (4 Nov 2026): Z5aBWeRxijI 2,480 (183.7x); J0snaaI5dXc 2,733 (103.1x); ZshuHDxCZ3c 1,026 (14.9x); mEIrbupU81s 2,957 (9.0x); H1w96Mbvl2I 12,786 (5.8x); 9OPRCqou1qc 16,259 (3.4x).

**Own fit** (how our videos of this series and pattern did, from [[Report]]): What's coming 788 (n=2), surprising-result 702.5 (n=4), both above our 585.5 median. Warning: "Can AI replace lawyers" (similar job angle, How AI works) did 66 engaged; lead with the result, not "can AI replace".

**Showable** (the medium of the mechanism, [[Picture]] §Medium, the one real run or model output, and the spine): capture of the Surge page and its scores; a `probs`-style bar of the three pass rates against the 95 % line; the condo case as a timeline (two closing dates, the August 2027 cliff). A run of our own on one public task is possible (cost and licence to check at P1).

**Score** demand 5 · own fit 5 · showable 3 · real thing 5 = 18 / 20

**Hooks** (3, different patterns):

1. surprising-result: Claude's best model passed 9 % of real tax jobs.
2. incident: The AI compared both closing dates. It missed the one that cost money.
3. stakes: Before you let an agent do your taxes, here's its score.
