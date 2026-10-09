---
type: research
created: 2026-10-09
updated: 2026-10-09
status: P1 to P3 done as text; no media, no spend; waiting for the user
tags: [research, youtube, script, battery, everyday-tech, week-01]
---

# Script · Phone charging slows (Week 01, Friday 9 Oct)

← [[Phone charging slows - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

Source: `Analytics/Generated ideas/Takeaways - youtube.md` (YouTube's channel read, 9 Oct 2026): physical-limit topics get reach (160 to 280 views), everyday tech questions hold viewers (Netflix 52.6 % stayed, 59.0 % retention); **best angle = a physical constraint behind an everyday gadget**. This idea is the everyday half with a material limit under it. **Y:** a phone that charges fast and keeps its battery for years. **X:** near full, a strong current can leave lithium as metal on the graphite, so the charger tapers on purpose. **Theme line:** *the slow end of charging is the phone protecting its battery.* **One question:** why does a phone charge fast at first and crawl at the end?

## 0. Facts bank (**read** = page opened 9 Oct 2026; **snippet** = search result only; attribute or keep off the voice)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Stage 1, constant current: a high current "will quickly fill the battery to about 70 percent" | Battery University BU-409 (**read**) |
| 2 | Stage 2, constant voltage: once the voltage limit is reached the current must taper; higher current makes the saturation longer | BU-409 (**read**) |
| 3 | Cobalt-blend Li-ion charges to 4.20 V per cell (plus or minus 50 mV) | BU-409 (**read**) |
| 4 | At the 4.20 V cutoff the cell holds about 85 %; saturation adds about 10 % "but adds stress due to high voltage" | BU-409 (**read**) |
| 5 | Full = voltage limit reached and current down to about 3 to 5 % of the rating | BU-409 (**read**) |
| 6 | Li-ion "cannot absorb overcharge", so the current must stop when full | BU-409 (**read**) |
| 7 | "Charge-and-run" chargers reach "Ready" in about an hour at about 85 %, skipping saturation | BU-409 (**read**) |
| 8 | Holding a 4.20 V cell above 4.30 V plates metallic lithium on the anode; the cathode then turns oxidizing, gas builds, pressure rises | BU-409 (**read**) |
| 9 | Fast charging can trigger lithium plating on graphite (large anode overpotential): a main source of capacity fade and safety risk | University of Michigan, Deep Blue abstract (snippet) |
| 10 | Fully lithiated graphite sits close to the potential of metallic lithium, so it is prone to plating | Ossila, lithium plating (snippet) |
| 11 | Plating begins at a lower state of charge as the charge rate rises | study abstract via search (snippet) |
| 12 | Apple Optimized Battery Charging learns your routine and waits to finish past 80 % until you need the phone | Apple support via search summary (snippet) |
| 13 | Apple: if the battery is too warm, software might limit charging above 80 % | Apple support via search summary (snippet) |
| 14 | Samsung Protect Battery, when on, limits charge to 85 % ("Charging paused. Protect battery limits you to 85%") | Samsung support via search summary (snippet) |
| 15 | Agent's reading of 1 to 11: the controller tapers near the top because graphite is nearly full, so the same current that is safe at 50 % can plate at 90 %; the exact onset (70, 80 or 85 %) differs by phone | agent, **not sourced as one claim** |
| 16 | Not found: any phone maker's own statement of why its taper starts where it does | agent; the voice says "near the top", never "at 80 %" as a fact about every phone |

## 1. Idea gate

**Street-lamp test:** the headline answer ("it slows to protect the battery", "to avoid overheating") is everywhere; **pass only with the mechanism beyond it**, stated in one sentence: *near full, graphite has little room left, so a strong current can pile lithium on it as metal; the charger holds the voltage and lets the current fade (facts 2, 8 to 10).* If scene 3 is cut, this is a generic explainer and fails: it must stay. Not borderline: the metal-plating step is the added mechanism.
**Scores:** surprise 3 · scale 4 · depth 4 · evidence 3 (one page read, three snippets) · showable 4 · plain 5. **Surprise is 3, below the required 4 for the thread.** Proposed fix: the hook's twist is that **the phone does it on purpose, and the stake is the battery's life**, not that charging is slow. If the user judges the surprise still 3, the idea drops behind a stronger candidate (below).
**Coffee test:** *"Your phone charges slowly at the end on purpose, because fast charging a nearly full battery can plate metal inside."* "Oh, so that's why." surprise 3 to 4.
**Expert test:** an electrochemist's "interesting part" is plating on graphite near the lithium potential (facts 8 to 10): in scene 3. A power-electronics engineer's is constant current then constant voltage (fact 2): in scene 4.
**Against the idea:** (1) "I know it protects the battery": answered by the metal-plating step; (2) "I do not care about 20 %": answered by the stake (years of battery life) in the conclusion; (3) "another battery video" (the channel has EV battery and lithium): the angle is the everyday phone, not the metal supply. Rescored: surprise stays 3.
**Rejected candidates (one line each):** Wi-Fi through walls (strong everyday question, weaker material link, networks family: first alternate if this scores too low) · why a phone cannot have a bigger battery (no clear mechanism found) · data-center hardware (YouTube's read: low uptake).
**Demand check: not run.** `youtube_search.py` needs `YT_ANALYTICS_REFRESH_TOKEN`, absent on this machine. Evidence in hand: YouTube's takeaways (everyday questions hold viewers; battery videos reached 160 to 280 views). **Topic family:** energy; previous video Neon for chips (materials): spread ok. Series suggestion: *Everyday tech, hidden limit* (Netflix screenshot, Neon, this).
**Five hooks (different types):** contradiction (leading) "Your phone slows its own charging on purpose." · stakes "The slow end of your phone's charge is what keeps the battery alive." · surprising fact "Past about 70 percent, a phone battery cannot take the current it took at the start." · question-as-claim "Why does a phone charge fast, then crawl?" · number "The last stretch of a charge adds about ten percent and the most stress." (fact 4).

## 2. Package

**Y/X:** above. **Promise:** your phone slows its charging near full on purpose, to protect the battery. **Titles:** *Why Your Phone Charges Slower After 80%* (recommended, 39 characters; the plain question people search) · *Your Phone Slows Its Own Charging on Purpose* (43) · *Why the Last 20% of Charging Takes So Long* (41). **Thumbnail:** hero = stock photo of a phone on a charger ($0, to find); kicker **PHONE BATTERY**; lines **SLOWS ON** / **PURPOSE** (second orange); chips **FAST TO ABOUT 70%** (Battery University) · **LITHIUM PLATES ON GRAPHITE** (26) · **THE LAST 10% ADDS STRESS** (23). Beats neighbours (to check in search) by saying "on purpose" instead of "tips". **Opening map:** scene 1 promise; scene 2 proof (the strong current fills most of it fast) and plan; scene 3 the catch.

## 3. Script (P2): compact test video, 114 words, 5 scenes

Written to the low-attention rule ([[Playbook]] §2): first sentence one plain claim, no jargon in the voice, sentences ≤ 12 words, spoken conclusion before the question. Bridges: 2 "At first" · 3 "But" · 4 "So" · 5 "So here is the point". **Facts (4):** strong current fills most of the battery fast; lithium goes into graphite; nearly full graphite can end up with lithium as metal; the charger holds the voltage and lets the current fade. **Spoken figures:** none (70 %, 4.20 V and 10 % are on screen). **Original synthesis:** none beyond the plain chain; the on-screen curve shows current falling while voltage holds. **Cut test:** 4.20 V, 85 %, CID, heat, Samsung's 85 % (screen only if at all).

| Scene | Voice text | Words | Delivery | Pause after (s) |
| --- | --- | --- | --- | --- |
| 1 | Your phone slows its own charging on purpose. It is protecting the battery. | 13 | plain, direct | 0.60 |
| 2 | At first, the charger pushes in a strong current. That fills most of the battery fast. | 16 | light, clear | 0.45 |
| 3 | But the lithium goes into graphite. When the graphite is nearly full, too much current can leave lithium as metal on its surface. That metal damages the battery. | 29 | slower, a little grave on "metal" | 0.90 (before the turn) |
| 4 | So the charger holds the voltage and lets the current fade. The last stretch is slow, and some phones even wait until you need them. | 26 | steady, calm | 0.90 (before the conclusion) |
| 5 | So here is the point. The slow end of charging is your phone protecting its battery. Should phones let you choose speed over battery life? Tell me what you think. | 30 | warm, slower on the point, open on the question | (tail) |

114 words by count. Inner pauses: after "purpose" (1), "current" and "fast" (2), "graphite" and "surface" (3), "voltage" (4), "point" and "battery" (5). Digits: none spoken. **Honesty:** "some phones even wait until you need them" is Apple's Optimized Battery Charging (fact 12, snippet): put the name on screen and open the Apple page before P4; "can leave lithium as metal" is hedged ("can") and rests on facts 8 to 11.

## 4. Visual plan (P3): 12 plates, prefix `pc`, folder `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/` (nothing downloaded: P4 not passed)

Candidates to find (Commons, Openverse, NASA): a phone on a charger (CC0), a lithium-ion cell or cutaway, a graphite or battery electrode photo, a charger and cable, a wall socket. No brand or screen text readable, no identifiable people.

| # | Sc | Type · layout | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- |
| 1 | 1 | S full + callout | a phone on a charger, so the hook is an everyday moment |
| 2 | 1 | S contain blur + number card | "70% to 100%" with "slow end" label, source Battery University |
| 3 | 2 | D split | a charge curve: strong current flat at first while the battery fills |
| 4 | 2 | S full + callout | a charger and cable, so "the charger pushes in current" is real |
| 5 | 3 | D split | lithium ions entering graphite layers (schematic) |
| 6 | 3 | D split | nearly full graphite and a strong current: lithium left as metal on the surface (schematic, faithful to facts 8 to 10) |
| 7 | 3 | S contain blur + card | a cell photo with "Lithium plating damages the cell" (BU-409) |
| 8 | 4 | D split | the same curve, now voltage held flat and current fading to a trickle |
| 9 | 4 | S full + callout | a phone at night, so "wait until you need them" is a bedside charger |
| 10 | 4 | S contain blur + card | "Optimized Battery Charging waits past 80% until you need it" (Apple) |
| 11 | 5 | S full + card | conclusion card: "The slow end protects the battery" |
| 12 | 5 | S contain blur + margin note | the closing question on screen; last plate repeats plate 1 (loop) |

**Mix:** 6 S, 4 D, 0 G (drawn schematics are exact: no generated plate needed), plus the repeat. Weak points known now: the plating schematic simplifies graphite; no photo shows lithium plating itself; stock phone photos stand for every brand.

## 5. Not verified

Facts 9 to 14 are snippets; one page (BU-409) was read; the exact taper onset per phone (fact 16); whether Apple's feature is as the summary says; whether "too much current can leave lithium as metal" is stated by a primary page for phones (BU-409 states it for overvoltage); the demand check; voice, pace and everything the agent cannot hear. P7 is the user's.
