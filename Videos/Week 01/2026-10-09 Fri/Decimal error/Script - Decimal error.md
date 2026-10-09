---
type: research
created: 2026-10-06
updated: 2026-10-09
status: v2 (redo, 9 Oct 2026) · P1 to P4a done by delegation; the Patriot version (v1) was parked by the user on 6 Oct
tags: [research, youtube, script, programming, rounding, week-01]
---

# Script · Decimal error (Week 01, redo Friday 9 Oct)

← [[Decimal error - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]] · [[Niche map]]

User (9 Oct 2026): *"Redo the decimal error video entirely, from idea to render. you're free to rethink how to make it engaging, viral-like"*. v1 (a computer cannot hold one tenth; the 1991 Patriot clock) was parked: *"this video doesnt make the cut into yt"* (6 Oct); recorded reason: a medium demand ceiling and a package that sold a cut-off error, not an outcome. **v2 keeps the subject (a decimal error that grows by repetition) and changes the story to one with a money stake and a twist ending:** the Vancouver Stock Exchange index.

**Y:** numbers you can trust (money and markets computed right). **X:** dropping a digit instead of rounding pushes every tiny error the same way, so millions of them add up. **Theme line:** *a tiny cut, always in the same direction, can cut a number in half.* **One question:** how can a stock index double over a weekend when nothing is traded?

## 0. Facts bank (**read** = page opened 9 Oct 2026; **run** = agent's arithmetic)

| # | Fact | Source |
| --- | --- | --- |
| 1 | In January 1982 the VSE index was set at 1000 (1000.000) and updated after each trade | Wikipedia, *Vancouver Stock Exchange*, citing K. Quinn, WSJ 8 Nov 1983 p. 37 (**read**) |
| 2 | After each update it was truncated to three decimal places, and the truncated value fed the next update | Wikipedia, same (**read**) |
| 3 | The calculation gave four decimal places; the index kept three; the last digit was discarded, not rounded | M. Parker, *Humble Pi* (2019), Kindle highlight on Goodreads (**read**) |
| 4 | Rounding goes "up as often as down"; truncation goes "always down", so each calculation lowered the index a tiny amount | Parker, same (**read**) |
| 5 | About 3,000 updates a day | Wikipedia; Parker (**read**) |
| 6 | The accumulated truncations lost about 25 points a month | Wikipedia (**read**) |
| 7 | Friday close 524.811; corrected over the weekend of 25 to 28 Nov 1983 to 1098.892 | Wikipedia, citing WSJ and W. Lilley, Toronto Star 29 Nov 1983 p. 35 (**read**) |
| 8 | Recalculated for the same period with rounding to the nearest thousandth: 524.811 became 1098.892 | Wikipedia, *Rounding*, citing Higham 2002 p. 54 and Nievergelt 2000 (**read**) |
| 9 | After 22 months it had fallen to about 520 "although the market appeared to be rising" | Wikipedia, *Rounding* (**read**); Huckle's bug list (Chalmers copy), citing WSJ, Toronto Star, McCullough and Vinod 1999 (**read**) |
| 10 | "The stock market had definitely not crashed to half its value" | Parker (**read**) |
| 11 | 25 Nov 1983 was a Friday and 28 Nov a Monday | Python `datetime` (**run**) |
| 12 | The index fell 47.5 % while the recalculated value rose 9.9 %; Monday's value is 2.09 times Friday's | agent (**run**, from fact 7) |
| 13 | About 477 trading days (4 Jan 1982 to 25 Nov 1983, about 9 holidays a year) x 3,000 = about **1.4 million cuts**, about **0.0004 points each**, about 1.2 points a day, 25 a month (matches fact 6) | agent (**run**) |
| 14 | A truncated fourth decimal loses between 0 and 0.0009 points: always less than a thousandth | agent (definition) |
| 15 | Round-to-nearest errors are unbiased; over 1.4 million updates they would random-walk to about 0.35 points | agent's estimate (**run**, assumes independent errors; not on screen) |
| 16 | Higham (2013 talk): the index "had been rounded down after every calculation"; recomputed "it doubled" | nhigham.com (**read**) |
| 17 | 1992, Schleswig-Holstein: the Greens' 4.97 % printed as 5.0 %, then unseated | Huckle's list, citing RISKS 13.37 (**read**; rejected thread) |
| 18 | 2007, Virgin Media rounded call charges up to the next minute | Higham's blog (**read**; not used) |

## 1. Idea gate

**Scores:** surprise 5 · scale 4 · depth 4 · evidence 4 (the 1983 newspapers are cited by Wikipedia, Higham and Parker; not read) · showable 5 · plain 5. Surprise, scale and plain are ≥ 4.
**Rejected (one line each):** Patriot clock 1991 (v1, parked: grave, medium ceiling, sold the error not an outcome) · 0.1 + 0.2 explainer (street-lamp fail: the headline answers it) · Schleswig-Holstein 1992 (one rounding, no accumulation, local) · game worlds breaking far from the origin (float precision, not decimals: its own video).
**Street-lamp test: pass.** "Rounding error halved an index" is the headline; the video adds the mechanism no headline gives: *truncation is biased (always down) and rounding is not (up as often as down), so 1.4 million cuts of under a thousandth add up instead of cancelling.* **Expert test:** a numerical analyst's interesting part is exactly that bias (facts 4, 15); each scene carries a detail a generic explainer skips (updated after every trade, four decimals kept as three, 3,000 a day, the market rising, Monday's 1098.892). **Coffee test:** *"A stock index doubled over a weekend with the market closed, because for two years a computer had been dropping the last decimal instead of rounding it."* "Wait, what?": surprise 5.
**Against the idea:** (1) "nobody lost money, so what": answered by the close (a tiny one-way cut can halve a number) and the bank question; (2) "a 1983 story": the mechanism is in every price and every balance that gets rounded; (3) "maths class": it is told as a mystery with the twist first. Scores kept.
**Demand check** (9 Oct 2026, YouTube pages read by `curl`; `youtube_search.py` has no token on this machine): direct demand is low (Top Quark, "The code that crashed a stock market", 1.7k views, 2018); adjacent demand exists: Land and Lore, "The scam capital of the world" (the VSE), 227k; wazpam, "The simple math problem computers get wrong", 200k (449x, [[Niche map]]). **Bridge:** the package sells the outcome (a market number doubling with nothing traded: money and trust in numbers), the mechanism is the surprise. **Topic family:** software; previous video Phone charging slows (energy): spread ok. Not compact (the previous video was): long, aim 130 to 160.
**Five hooks:** contradiction (**leading**) "A stock index doubled over one weekend, while the market was closed." · surprising number "One weekend, a stock index jumped from five hundred to over a thousand." · stakes "A computer quietly erased half a stock index, and no one noticed for two years." · surprising fact "A stock index lost half its value while its stocks went up." · consequence "Dropping one digit, three thousand times a day, can halve a market's number." **Hook test (leading):** plain (no term defined later) · reason to care (a broken expectation about money: doubling with nothing traded) · open question ("how?", answered in scenes 2 to 3) · sound-off (caption DOUBLED on the board counting 524.811 to 1,098.892 past SAT and SUN marked CLOSED) · honest (fact 7, weekend, recalculation) · matches the package.

## 2. Package

- **Promise:** a stock index doubled over a weekend with the market closed, because for almost two years a computer had dropped a digit after every trade.
- **Titles:** *A Stock Index Doubled Over a Weekend. Nothing Was Traded.* (recommended, 57 characters) · *The Missing Digit That Halved a Stock Index* · *Why Computers Round Instead of Cutting Off Decimals*.
- **Thumbnail** (`upload/de-thumb-a.jpg`): hero ($0) drawn as Friday's board (524.811) against Monday's (1,098.892), because no free photo shows the exchange in 1982 (Commons has only its 1929 to 1946 building, 475 Howe Street; in 1982 it was in the Stock Exchange Tower, 609 Granville, Wikipedia); kicker **ROUNDING ERROR**; lines **IT DOUBLED.** / **NOTHING TRADED.** (orange; "overnight" dropped: it was a weekend); chips **ONE DIGIT DROPPED** · **3,000 TIMES A DAY** · **VANCOUVER, 1982 TO 1983**. Beats its neighbours (rounding tutorials and 0.1 + 0.2 code screens) by showing a market number and a weekend, with the figures as proof.
- **Opening map:** scene 1 promise (the doubling) · scene 2 proof (the exchange, the index at 1,000, updated every trade) · scene 3 plan (the cut, and why it only goes down).

## 3. Script (P2): 163 words, 7 scenes (take v2: 55.7 s, 176 wpm)

Bridges: 2 "It was" (answers who) · 3 "But" · 4 "And" · 5 "So" · 6 "Then" · 7 "So here is the point". **Facts (5):** the index started at 1,000 and was updated every trade; four decimals were cut to three, never rounded; each cut was under a thousandth, about 3,000 a day; the index sank to almost half while the market rose; recalculated with rounding over one weekend, it more than doubled. **Spoken figures:** one thousand, a thousandth, three thousand (four and three decimals are counts in the mechanism). **Original synthesis:** about 1.4 million cuts of about 0.0004 points each (fact 13), on screen. **Cut test:** removed the newspapers, 22 months as a number, Virgin Media, the 0.35-point estimate. **Low-attention:** first sentence 12 words, no jargon; the point is spoken as a point and shown on a card before the question.

| Sc | Voice text | W | Delivery | Pause intention |
| --- | --- | --- | --- | --- |
| 1 | A stock index doubled over one weekend, while the market was closed. Nobody got richer. Tiny cuts had been shrinking it for almost two years. | 24 | plain, intrigued | natural sentence pauses; "Nobody got richer." stands alone |
| 2 | It was the Vancouver Stock Exchange. Its new index started at one thousand, and a computer updated it after every trade. | 21 | light, clear | breath after "Exchange." |
| 3 | But the math gave four decimals, and the index kept three. The last one was simply dropped. Rounding goes up as often as down. Dropping only goes down. | 28 | curious, slower on "dropped" | the two short contrasts land one by one |
| 4 | And each cut was less than a thousandth of a point. But it happened about three thousand times a day. | 20 | steady, building | continues scene 3 (no mark) |
| 5 | So the index sank to almost half, while the market was actually rising. | 13 | quiet, let it land | `beat` 0.3 after the scene: before the turn |
| 6 | Then, one weekend, they redid the math with proper rounding. By Monday, the index had more than doubled. | 18 | rising, a small smile on "doubled" | natural |
| 7 | So here is the point: a tiny cut, always in the same direction, can cut a number in half. If a bank kept every dropped fraction of a cent, would that be theft? Tell me what you think. | 39 | warm, slower on the point, open on the question | break 0.2 after "half." (before the question) |

Captions spell "one thousand" as 1,000 and "three thousand" as 3,000. Sources per line: 1 facts 7, 11, 10 · 2 facts 1, 5 · 3 facts 2 to 4 · 4 facts 5, 14 · 5 facts 9, 12 · 6 facts 7, 8 · 7 facts 13, 4. **Honesty:** "they redid the math" (who did it is not in the sources read); "while the market was closed" = a weekend (fact 11); "the market was actually rising" rests on facts 9 and 12.

## 4. Beat sheet (P4a): 10 motion plates, prefix `de`, 5 worlds (the board is the anchor)

| # | Sc · `at` | Medium | The viewer sees ___ happen, so they understand ___ | Events on words | Text on screen |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 · start | motion `de-m-board` | the board counting 524.811 to 1,098.892 as the day marker slides FRI to MON past SAT and SUN marked CLOSED, so the doubling happened with no trading | "doubled" count · "closed" CLOSED stamps · "richer" wallet bar flat · "cuts" the last digit sliced | VSE INDEX · FRI SAT SUN MON |
| 2 | 2 · start | motion `de-m-map` | a globe turning to Canada and zooming to Vancouver, so it is a real market in a real city | "Vancouver" pin · "Exchange" label | Vancouver · Vancouver Stock Exchange |
| 3 | 2 · "index" | motion `de-m-start` (anchor, state 2) | the board at 1000.000 and trades flying in, each one nudging the number | "thousand" pulse · "trade" particles, number moves | JAN 1982 · trades counter |
| 4 | 3 · start | motion `de-m-cut` | one update: 1000.4567, three decimals boxed, the 7 falls off into a bin | "four" digits light · "three" bracket · "dropped" the digit falls | KEPT · DROPPED |
| 5 | 3 · "Rounding" | motion `de-m-round` | two rows of errors: rounding bars go up and down and the sum stays flat; dropping bars all go down and the sum sinks | "Rounding" up-down bars · "Dropping" down bars, sum line sinks | ROUNDING · DROPPING |
| 6 | 4 · start | motion `de-m-pile` | one cut is a hairline on a one-point ruler; then a counter races to 3,000 while slivers pile up | "thousandth" hairline · "three" counter · "day" pile | 1 POINT · 3,000 CUTS A DAY · about 25 points a month |
| 7 | 5 · start | motion `de-m-chart` | the shown index line falls from 1,000 to 524.811 while the market line rises, so the gap is the error | "sank" copper line draws · "half" mark · "rising" dashed line | JAN 1982 · NOV 1983 · Shown · Recalculated |
| 8 | 6 · start | motion `de-m-fix` (anchor, state 3) | the board recomputed: a progress bar fills, Monday flips, the number jumps to 1,098.892 | "redid" bar · "rounding" · "Monday" jump and pulse | Toronto Star, 29 Nov 1983 |
| 9 | 7 · start | motion `de-m-point` (anchor, final) + context card | the board replaying two years: 1,000.000 sinks to 524.811 while slivers fall from its last digit; conclusion card | "point" card · "always" count down · "direction" arrow · "half" pulse | card: Vancouver, 1982 to 1983 · One-way cuts halved it · About 1.4 million cuts, 0.0004 each |
| 10 | 7 · "If" | motion `de-m-cent` + margin note | a cent coin losing a sliver to a bank, again and again | "fraction" sliver · "theft" pulse | note: Dropped fractions of a cent: theft? |

No real photo or footage: the only free photo of the exchange shows a building it left in 1946, and Pixabay's market clips were generic screens (swap test). Everything is a faithful drawing. **Schematic, marked in Status:** the chart draws straight lines between the sourced endpoints (the real paths are not in the sources); the trades, digits and errors in plates 3 to 6 are illustrative values (1000.4567 is an example, not a logged update).

## 5. Not verified

The 1983 WSJ and Toronto Star articles (paywalled; cited through Wikipedia, Higham, Parker); who recalculated the index; the exact count of trading days (fact 13 is an estimate); search autocomplete for the plain question. The agent cannot hear or watch: P7 is the user's.
