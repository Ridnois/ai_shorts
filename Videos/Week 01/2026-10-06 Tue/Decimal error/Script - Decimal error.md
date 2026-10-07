---
type: research
created: 2026-10-06
updated: 2026-10-06
status: P1 to P6 done; r1 built and rendering; P7 is the user's
tags: [research, youtube, script, programming, floating-point, week-01]
---

# Script · Decimal error (Week 01, Tuesday 6 Oct)

← [[Decimal error - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]] · [[Why 0.1 plus 0.2 is not 0.3]] · [[Niche map]]

User choice (6 Oct 2026): *"I think we should go to the idea about decimals"*. **Y:** code that adds money correctly. **X:** a computer counts in twos, so one tenth is an endless fraction that gets cut off; each cut is tiny and tiny cuts add up. **Theme line:** *A computer cannot hold one tenth, and a tiny cut-off, repeated, once cost lives.* **One question:** why does a computer get a sum like 0.1 + 0.2 wrong, and does it ever matter?

## 0. Facts bank (**read** = page opened 6 Oct 2026; **run** = agent ran the arithmetic)

| #   | Fact                                                                                                                                                                                                                 | Source                                                    |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1   | In binary, one tenth is the endless fraction 0.000110011001100... ("1100" repeats forever), so it cannot be stored exactly in any finite precision                                                                   | Wikipedia, Floating-point arithmetic (**read**)           |
| 2   | Same idea as one third in decimal (0.33...): you must round                                                                                                                                                          | floating-point-gui.de (**read**)                          |
| 3   | 0.1 + 0.2 gives 0.30000000000000004 in standard double precision; neither number is stored exactly before the sum                                                                                                    | floating-point-gui.de (**read**); Python 3 (**run**)      |
| 4   | The double stored for 0.1 is 0.1000000000000000055511151231257827... and for 0.2 is 0.2000000000000000111022302462515654...; their sum differs from 0.3                                                              | Python `Decimal(0.1)` (**run**)                           |
| 6   | 25 Feb 1991, Dhahran: a Patriot battery failed to track and intercept a Scud; the Scud hit a barracks, **killing 28 Americans**                                                                                      | US GAO IMTEC-92-26, 4 Feb 1992 (**read**)                 |
| 7   | Cause: a software problem in the weapons control computer; the tracking error "became worse the longer the system operated"; the battery had run **over 100 hours**                                                  | GAO (**read**)                                            |
| 8   | The clock counted **tenths of a second** as a whole number; converting it to a real number was only as precise as **24-bit registers** allow, so precision was lost                                                  | GAO (**read**)                                            |
| 9   | After 100 hours the clock was off by **0.3433 s**, which shifted the range gate by **687 m** (1 h: 7 m; 8 h: 55 m; 20 h and the target is already outside)                                                           | GAO Appendix II (**read**)                                |
| 10  | My check: chopping 0.1 to 23 binary places leaves an error of 9.5e-8 per tick; times 100 h at 10 ticks per second = 0.3433 s, GAO's number                                                                           | agent (**run**)                                           |
| 12  | Israeli data on 11 Feb 1991 showed a 20 % range-gate shift after 8 hours; the fixed software reached Dhahran on **26 Feb**, the day after; interim fix: reboot every few hours                                       | GAO (**read**)                                            |
| 14  | For money, store whole cents (integers) or use a decimal type                                                                                                                                                        | floating-point-gui.de (**read**)                          |

## 1. Idea gate

Scores: surprise 4 · scale 3 · depth 4 · evidence 5 · showable 4 · plain 4. **Scale is 3, below the thread's required 4:** the video cannot rest on a big number. Fix: the scale is the **consequence** (lives, a 687 m miss), and the **100-hour growth** (7 m, 55 m, 137 m, 330 m, 687 m, from the GAO table) is the drawn comparison: a speck that grows. If the scale does not read in the script, the idea fails.
Rejected, one line each: **Ariane 5** (different bug, overflow, not decimals; not read); **JavaScript money bugs** (no source); **a tutorial on Decimal types** (a how-to, not a mechanism).
**Street-lamp test: pass.** Search headline "0.1 + 0.2 is not 0.3" answers the central question for the many tiny videos (best 200k, [[Niche map]]); the video adds the mechanism no headline gives: the **error grows with running time** (GAO table: 0.0034 s at 1 h to 0.3433 s at 100 h), so a harmless speck becomes a 687 m miss. One-line mechanism sentence: *the error is per tick, not per sum, so it scales with how long the machine runs.*
**Coffee test:** *"A computer cannot store one tenth exactly, and in 1991 that tiny error, repeated for 100 hours, made a missile battery look 687 metres from where the target was."* "Wait, really?" surprise 4.
**Expert test:** a numerical analyst would say the interesting part is accumulation (and that the Patriot error came from a fixed-point conversion, not IEEE doubles): the script must say "a similar cut-off", never "0.1 + 0.2 caused it" (honesty rule).
**Against the idea (three reasons to scroll past):** (1) "I know this meme": answered by the 1991 turn; (2) "only programmers care": answered by the stake (lives, clock, money); (3) "the Patriot story is old": the **mechanism** is what generalises (any counter that runs long). If the Patriot story reads as trivia, surprise drops to 3.
**Demand check:** medium ([[Niche map]], youtube_search 6 Oct 2026): best 200k views (wazpam, "The simple math problem computers get wrong"); the rest 9 to 17k. **Topic family:** software; previous video Grid chokepoint (energy and grid): spread ok.
**Five hooks (different types, voice-take check pending):** surprising fact (leading) "A computer cannot store one tenth, and that once cost twenty-eight lives." · stakes "The tiniest rounding error in a computer once made a missile battery look in the wrong place." · surprising number "After one hundred hours, a clock error of a third of a second became six hundred and eighty-seven meters." · contradiction "Your computer says point one plus point two is not point three, and it is not wrong in the way you think." · consequence "Code that adds up money can be quietly wrong, for the same reason a missile once missed." Hook test on the leading line: plain (no jargon), stake (lives), open question (how can a tenth cost lives?), honest (needs the "cut-off" framing).

## 2. Package (gate P3, [[Playbook]] §2b, rules in [[Audience]])

- **Y:** correct money code. **X:** a cut-off that repeats grows with running time. **Promise:** a computer cannot hold one tenth exactly, and in 1991 that tiny cut-off, repeated, made a missile battery look in the wrong place.
- **Titles:** *The Tiny Rounding Error That Made a Missile Miss* (recommended; honest: GAO traces the missed intercept to the software error, the Scud caused the deaths) · *Your Computer Can't Store 0.1. A Missile Battery Found Out.* · *Why 0.1 + 0.2 Is Not 0.3, and When It Matters*. The hook says "cost twenty-eight lives": keep the title softer than the hook.
- **Thumbnail:** hero = Patriot launch (`Patriot missile launch b.jpg`, public domain, Commons); kicker **PROGRAMMING**; lines **THE TINY ERROR** / **THAT MISSED A SCUD** (second line orange); chips **0.3433 S OFF** · **687 M OFF TARGET** · **100 HOURS**. Beats its neighbours (search 6 Oct 2026: code screens showing 0.30000000000000004) by showing the missile and the stake, with the numbers as proof. One idea: a small error, a big miss.
- **Opening map:** scene 1 promise (hook) · scene 2 proof (binary tenth, the cut) and plan ("the cut repeats").

## 3. Script (P2): 164 words, 845 characters, 7 scenes

Bridges: 2 "That is because" · 3 "So add" · 4 "But" · 5 "And those cuts add up" · 6 "so" inside · 7 "So the longer". **Facts (5):** one tenth is endless in binary; 0.1 + 0.2 shows the cut-off; the Patriot clock counted tenths; the drift grew to a third of a second in 100 hours; the search area was off by hundreds of metres (GAO). **Spoken figures (3):** twenty-eight, a hundred hours, a third of a second; every other number is on screen (0.3433 s, 687 m, 7 m to 687 m table). **Original synthesis:** the growth of the error with run time drawn from the GAO table, and the 3,600,000 ticks (10 per second × 360,000 s, agent's arithmetic). **Cut test:** removed the Vancouver index, the 0.1 + 0.2 double values, Ariane, the reboot workaround. **Honesty:** "cut-off at every tick" simplifies a 24-bit fixed-point conversion; Status marks it *schematic*. **Close:** concrete payoff (a long run drifts; money in whole cents).

| Scene | Voice text | Words | Delivery | Pause after (s); inner pauses |
| --- | --- | --- | --- | --- |
| 1 | A computer cannot hold one tenth exactly, and a tiny cut-off once cost twenty-eight lives. | 2 | That is because computers count in twos, and in twos one tenth never ends, like a third in decimal. So the machine cuts it off, and the cut repeats. | 29 | curious, explaining | 0.45; after "in twos," 0.25 |
| 3 | So add point one and point two, and you get point three plus a speck at the very end. The speck is the cut-off. | 24 | light, a small smile at the speck | 0.25 (same thought); after "point three" 0.25 |
| 4 | One speck does no harm. But a Patriot missile battery kept time in tenths of a second, and cut off a little at every tick. | 25 | calm, turning to the stakes | 0.25 (same thought); after "harm." 0.5 |
| 5 | And those cuts add up: after a hundred hours, the clock had drifted by a third of a second. | 19 | steady, building | 0.80 (before the miss); none |
| 6 | A Scud is so fast that this drift put the radar's search area hundreds of meters from the target, so the Patriot looked in the wrong place. The Scud hit a barracks. | 32 | grave, measured, slows at the miss | 1.00 (before the payoff); after "place." 0.4 |
| 7 | So the longer a machine runs, the further a tiny cut-off drifts. That is why programmers keep money in whole cents. | 21 | calm, closing; the last plate is the first | (tail); after "drifts." 0.5 |

`gaps` = [0.60, 0.45, 0.25, 0.25, 0.80, 1.00]. **Voice:** `elevenlabs/turbo-v2.5`, Austin, one take per scene with `previous_text` and `next_text` ([[Playbook]] §5); scene 1 is the test take.

## 4. Visual plan (P3): S stock photo · D drawn (Pillow, $0), 18 plates, prefix `de`, 3 generated

Photo candidates (found with `stock_photos.py search`, **not downloaded**, no file in `Media/` before P4): `Patriot missile launch b.jpg` (public domain), `Scud downed by Patriot missiles.JPEG` (public domain), `AN MPQ 53.jpg` (public domain), `Scud missile on TEL vehicle, National Museum of Military History` (CC BY-SA 2.0, credit), `Disected Scud missile.jpg` (public domain). No photo of code or a clock was found: those are D plates.

| # | Sc | Type · layout | Source | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- | --- |
| 1 | 1 | S full + callout | Patriot launch | the real machine, so "a tiny cut-off cost lives" is about a missile system |
| 2 | 1 | S contain blur + number card | Scud downed by Patriot | card **28 / Americans killed, Dhahran, 25 Feb 1991 / US GAO 1992**: the stake |
| 3 | 2 | D split + inset | 1/3 = 0.333... above 1/10 = 0.000110011... (inset: Patriot launch) | that both fractions never end, one in decimal and one in binary |
| 4 | 2 | **G** split + inset | schematic: a row of 23 cells (filled = 1) with a cut line, the rest fading past it (inset: radar) | where the cut falls |
| 5 | 2 | D split | tick marks, a sliver cut off each | that the cut repeats |
| 6 | 3 | D split + inset | 0.1 + 0.2 = 0.30000000000000004, last digit marked (inset: radar) | the speck |
| 7 | 3 | D split | the stored values of 0.1 and 0.2 side by side (Python) | that neither is exact before the sum |
| 8 | 4 | S full + callout | AN/MPQ-53 radar | what tracks the Scud |
| 9 | 4 | D split + inset | clock ticking in tenths, cut-off sliver at each tick (inset: radar) | the clock counting tenths |
| 10 | 5 | D split | bars: error after 1, 8, 20, 48, 72, 100 hours (GAO Appendix II) | the error growing with time |
| 11 | 5 | S contain blur + number card | Patriot launch, other crop | card **0.3433 s / clock error after 100 hours / US GAO 1992** |
| 12 | 5 | D number plate on photo | Patriot launch | **3,600,000 ticks** in 100 hours (10 a second) |
| 13 | 6 | S full + callout | Scud on TEL (CC BY-SA 2.0) | the target; callout "Scud, about Mach 5" |
| 14 | 6 | **G** split + inset | two-panel schematic: radar gate centred on the Scud, then shifted off it (GAO figures 4 and 5 as references) (inset: Scud) | what "looking in the wrong place" means |
| 15 | 6 | D split | bars: range-gate shift 7, 55, 137, 330, 687 m at 1, 8, 20, 48, 100 h (GAO Appendix II) | the distance of the miss |
| 16 | 6 | **G** full + context card | top-down incident schematic: battery and radar, the Scud arc, the barracks, the radar gate short of the Scud; card **GAO · 1992 / Fixed software arrived 26 Feb / the day after** | the incident as a diagram: where the radar looked against where the Scud was |
| 17 | 7 | D split + inset | 0.1 against **10 cents** stored as the whole number 10 (inset: radar) | the fix, a whole count |
| 18 | 7 | S full | Patriot launch (hook image again) | the loop |

**Mix (user, 6 Oct 2026: mix stock photos with generated illustrations, `gpt-image-2`):** 6 S, 8 D, **3 G** (plates 4, 14, 16; the cap); 17 plates after plate 12 was merged into plate 10 (5 of the D plates are data figures from the GAO or Python; 164 words is above the 130 to 160 aim, inside 190). **Weak points known now:** the generated plates are **schematics, not scenes**: no photoreal depiction of the real strike, no people, no fire (Style: no fakes of real events); image models miscount cells, so plate 4 is checked cell by cell and falls back to a drawn plate after one retry; no real photo of Dhahran or the barracks (not shown, and no identifiable people); the range-gate drawing is a schematic of GAO figures 4 and 5; Patriot photos are of later models, labelled as file photos; plate 15 skips the 72 h row (494 m) to keep five bars; the table rows are 1, 8, 20, 48, 72, 100 h. **On-screen text** limited to the cards above; symbols avoided (the font lacks them).

## 5. Next

**P4 is the user's gate** (prompts in Status, stock download, budget). Estimate: voice about $0.09 (unconfirmed price), timings 7 × $0.01, **3 generated plates at about $0.25 each = $0.75** (price unconfirmed; `quality: medium` would cut it), stock $0: **base about $0.91, cap about $1.09**, about double a usual Short. Before anything else: the voice test of scenes 1 and 2 (about $0.02).

## 6. Not verified

The Patriot error is a 24-bit fixed-point conversion of 0.1, not IEEE double arithmetic. I did not read the competitor videos' transcripts. The agent cannot hear or watch: P7 is the user's.
