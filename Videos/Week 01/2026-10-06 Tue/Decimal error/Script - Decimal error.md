---
type: research
created: 2026-10-06
updated: 2026-10-06
status: P1 (idea and research) done and passed; script and package next (P2 and P3)
tags: [research, youtube, script, programming, floating-point, week-01]
---

# Script · Decimal error (Week 01, Tuesday 6 Oct)

← [[Decimal error - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]] · [[Why 0.1 plus 0.2 is not 0.3]] · [[Niche map]]

User choice (6 Oct 2026): *"I think we should go to the idea about decimals"*. **Y:** code that adds money correctly. **X:** a computer counts in twos, so one tenth is an endless fraction that gets cut off; each cut is tiny and tiny cuts add up. **Theme line:** *A computer cannot hold one tenth, and a tiny cut-off, repeated, once cost lives.* **One question:** why does a computer get a sum like 0.1 + 0.2 wrong, and does it ever matter?

## 0. Facts bank (**read** = page opened 6 Oct 2026; **run** = agent ran the arithmetic)

| # | Fact | Source |
| --- | --- | --- |
| 1 | In binary, one tenth is the endless fraction 0.000110011001100... ("1100" repeats forever), so it cannot be stored exactly in any finite precision | Wikipedia, Floating-point arithmetic (**read**) |
| 2 | Same idea as one third in decimal (0.33...): you must round | floating-point-gui.de (**read**) |
| 3 | 0.1 + 0.2 gives 0.30000000000000004 in standard double precision; neither number is stored exactly before the sum | floating-point-gui.de (**read**); Python 3 (**run**) |
| 4 | The double stored for 0.1 is 0.1000000000000000055511151231257827... and for 0.2 is 0.2000000000000000111022302462515654...; their sum differs from 0.3 | Python `Decimal(0.1)` (**run**) |
| 5 | IEEE 754, the floating-point standard, dates from 1985 | Wikipedia (**read**) |
| 6 | 25 Feb 1991, Dhahran: a Patriot battery failed to track and intercept a Scud; the Scud hit a barracks, **killing 28 Americans** | US GAO IMTEC-92-26, 4 Feb 1992 (**read**) |
| 7 | Cause: a software problem in the weapons control computer; the tracking error "became worse the longer the system operated"; the battery had run **over 100 hours** | GAO (**read**) |
| 8 | The clock counted **tenths of a second** as a whole number; converting it to a real number was only as precise as **24-bit registers** allow, so precision was lost | GAO (**read**) |
| 9 | After 100 hours the clock was off by **0.3433 s**, which shifted the range gate by **687 m** (1 h: 7 m; 8 h: 55 m; 20 h and the target is already outside) | GAO Appendix II (**read**) |
| 10 | My check: chopping 0.1 to 23 binary places leaves an error of 9.5e-8 per tick; times 100 h at 10 ticks per second = 0.3433 s, GAO's number | agent (**run**) |
| 11 | Scuds fly at about Mach 5 (3,750 mph); the Army learned the software limits only during the war | GAO (**read**) |
| 12 | Israeli data on 11 Feb 1991 showed a 20 % range-gate shift after 8 hours; the fixed software reached Dhahran on **26 Feb**, the day after; interim fix: reboot every few hours | GAO (**read**) |
| 13 | Vancouver Stock Exchange index: started at 1000 in Jan 1982, truncated (not rounded) to 3 decimals about 3000 times a day; after 22 months it read 524.811 against a correct 1098.892 (fixed over 25 to 28 Nov 1983) | Wikipedia, Vancouver Stock Exchange (**read**; secondary) |
| 14 | For money, store whole cents (integers) or use a decimal type | floating-point-gui.de (**read**) |
| 15 | Summing 0.1 ten times in Python gives exactly 1.0 here, so errors do not always show; the visible ones come from specific sums | Python (**run**) |
| 16 | The Patriot's 24-bit registers: today's computers have registers of up to 64 bits | GAO (**read**) |

Not used: Scud speed in m/s (GAO gives mph; "570 m" from a secondary page: the GAO's 687 m is used), "28 killed and about 100 injured" (the 100 comes from a secondary page).

## 1. Idea gate

Scores: surprise 4 · scale 3 · depth 4 · evidence 5 · showable 4 · plain 4. **Scale is 3, below the thread's required 4:** the video cannot rest on a big number. Fix: the scale is the **consequence** (lives, a 687 m miss), and the **100-hour growth** (7 m, 55 m, 137 m, 330 m, 687 m, from the GAO table) is the drawn comparison: a speck that grows. If the scale does not read in the script, the idea fails.
Rejected, one line each: **Ariane 5** (different bug, overflow, not decimals; not read); **JavaScript money bugs** (no source); **a tutorial on Decimal types** (a how-to, not a mechanism).
**Street-lamp test: pass.** Search headline "0.1 + 0.2 is not 0.3" answers the central question for the many tiny videos (best 200k, [[Niche map]]); the video adds the mechanism no headline gives: the **error grows with running time** (GAO table: 0.0034 s at 1 h to 0.3433 s at 100 h), so a harmless speck becomes a 687 m miss. One-line mechanism sentence: *the error is per tick, not per sum, so it scales with how long the machine runs.*
**Coffee test:** *"A computer cannot store one tenth exactly, and in 1991 that tiny error, repeated for 100 hours, made a missile battery look 687 metres from where the target was."* "Wait, really?" surprise 4.
**Expert test:** a numerical analyst would say the interesting part is accumulation (and that the Patriot error came from a fixed-point conversion, not IEEE doubles): the script must say "a similar cut-off", never "0.1 + 0.2 caused it" (honesty rule).
**Against the idea (three reasons to scroll past):** (1) "I know this meme": answered by the 1991 turn; (2) "only programmers care": answered by the stake (lives, clock, money); (3) "the Patriot story is old": the **mechanism** is what generalises (any counter that runs long). If the Patriot story reads as trivia, surprise drops to 3.
**Demand check:** medium ([[Niche map]], youtube_search 6 Oct 2026): best 200k views (wazpam, "The simple math problem computers get wrong"); the rest 9 to 17k. **Topic family:** software; previous video Grid chokepoint (energy and grid): spread ok.
**Five hooks (different types, voice-take check pending):** surprising fact (leading) "A computer cannot store one tenth, and that once cost twenty-eight lives." · stakes "The tiniest rounding error in a computer once made a missile battery look in the wrong place." · surprising number "After one hundred hours, a clock error of a third of a second became six hundred and eighty-seven meters." · contradiction "Your computer says point one plus point two is not point three, and it is not wrong in the way you think." · consequence "Code that adds up money can be quietly wrong, for the same reason a missile once missed." Hook test on the leading line: plain (no jargon), stake (lives), open question (how can a tenth cost lives?), honest (needs the "cut-off" framing).

## 2. Next (not done)

P2 script (130 to 190 words) with the **Package** section ([[Playbook]] §2b) written first: titles and thumbnail from the [[Why 0.1 plus 0.2 is not 0.3]] draft, revised for the 687 m hook; P3 visual plan; then the voice **test stage** on `elevenlabs/turbo-v2.5`.

## 3. Not verified

Vancouver figures are from one Wikipedia page. The Patriot error is a 24-bit fixed-point conversion of 0.1, not IEEE double arithmetic; the video must not say they are the same. I did not read the competitor videos' transcripts. The agent cannot hear or watch: P7 is the user's.
