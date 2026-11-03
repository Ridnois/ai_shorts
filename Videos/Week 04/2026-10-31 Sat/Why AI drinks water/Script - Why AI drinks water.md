---
type: script
updated: 2026-10-31
series: What's coming
words: 149
---

# Script: Why AI drinks water

Status: [[Why AI drinks water - Status]] · rules: [[Story]] §Beats

## Research (31 Oct 2026)

All figures read at the source, not from news summaries (the first search disagreed with itself: 7.2, 10.5 and 10.9 billion gallons, from different years and scopes).

1. **Google Cloud blog, "Measuring the environmental impact of AI inference"**, 21 Aug 2025 (read and captured 31 Oct 2026): "the median Gemini Apps text prompt uses 0.24 watt-hours (Wh)", "consumes 0.26 milliliters (or about five drops) of water", "0.03 grams of carbon dioxide equivalent". Footnote: "Water consumption per prompt was estimated based on energy per prompt, and applying Google's 2024 average fleetwide water usage effectiveness." So the five drops are an estimate from a fleet average, not a per-prompt measurement. A narrower active-chip-only method gives 0.12 mL; the video uses Google's headline (comprehensive) number.
2. **Google 2025 Environmental Report** (PDF, 120 pages, read and captured 31 Oct 2026; data year 2024), p. 40: "In 2024, we consumed a total of approximately 8.1 billion gallons (31 billion liters or 31 million cubic meters) of water across our data centers (excluding those operated by third parties) and offices. To put that consumption into perspective, that's about what it takes to irrigate 54 golf courses annually, on average, in the southwestern United States." Scope is **all of Google's own data centers and offices, not only AI**; the voice says so. The same page: cooling systems "frequently use water due to its energy efficiency"; overall consumption rose 28 % from 2023 to 2024.
3. Same report, data table p. 110: freshwater consumption 7,210 million gallons in 2024 (5,601 in 2023; 4,770 in 2022); water replenished 4,590 million gallons, 64 % of freshwater consumption. Total water consumption (all water, Alphabet) 8,135 million gallons, defined in the Alphabet water table as water "withdrawn and incorporated into Alphabet's operations, including through evaporation, and is therefore not released back" (p. 110 and 112). So 8.1 B is the total and 7.2 B the freshwater share: both are in the report, and the news figure of 7.2 B is the freshwater one.
4. Same report, p. 102 (methodology): "We calculate water consumption by subtracting water discharge from water withdrawal." Evaporated water is not discharged, so it counts as consumed (the voice's "Vapor never comes back, so Google counts it as consumed" is that definition applied to the vapour; the report does not say it in those words).
5. Same report, p. 41: at Waltham Cross (UK) Google chose "air cooling technology at this site, an approach that doesn't consume water for cooling during routine operations"; "We're taking a similar approach in other areas identified as having high water risk ... such as our facilities under development in Mesa, Arizona and Canelones, Uruguay."
6. **Google data centers site, "Operating sustainably"** (datacenters.google, read and captured 31 Oct 2026): "Water cooling is an energy-efficient way to remove heat"; cooling with water "has been shown to help reduce energy consumption and related carbon emissions" compared with air-based cooling; Google "acknowledges this tradeoff will increase our data center water footprint".
7. **Physics, no number on screen:** a chip's electrical power ends as heat (conservation of energy); a cooling tower removes it by letting part of the water evaporate, which carries heat away (the report's own photo caption names "cooling towers at our data center in Mayes County, Oklahoma"; Google's page describes water cooling as removing heat but does not describe evaporation, so that step is textbook thermodynamics and Google's definition of consumption, not a Google quote).

**Not verified:** (a) the 0.26 mL is Google's own estimate for Gemini Apps, one product on one date (not ChatGPT, not another model, not another year); Google says "consumes", the video says "uses up" in the hook and "evaporates" only once the mechanism is shown. (b) The dial's jump to "more power" under air cooling is a schematic of Google's statement that water cooling reduces energy compared with air; it is not a measurement and has no number. (c) The 2026 environmental report (2025 data) was not read; a third-party page gave 10.5 B gallons for 2025 and this video does not use it. (d) The Mesa, Arizona site is "under development" in the report; "plans air cooling" matches that.

## Package

- **Promise:** why a chatbot answer costs water: heat becomes steam, Google's own numbers, and the choice behind it (water or power).
- **Titles:** **How Much Water Does AI Use? Google's Own Numbers** ← (50 chars) · Why AI Data Centers Evaporate Water (and Why It's On Purpose) · One Gemini Answer Uses 5 Drops of Water: How?
- **Frame 0:** 5 DROPS OF WATER over the cooling-tower figure, running. **Thumbnail:** the figure with the five lamps lit and yellow vapour, "5 DROPS OF WATER".
- **Hooks (3, different types):** number ← "One Gemini answer uses up five drops of water." · contradiction "Computers hate water. AI data centers can't run without it." · stakes "Google's data centers drank eight billion gallons in one year."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | One Gemini answer uses up five drops of water. | 9 | `cooling-tower` running (red fins, beads, vapour); five lamps light on "five drops" | 1 |
| 2 | stake | That's Google's own median for a text prompt. All of Google's own data centers and offices, not only AI, consumed 8.1 billion gallons in 2024: 54 golf courses, watered for a year. | 32 | the Google post's phrase crops (median text prompt, 0.26 milliliters, five drops); ALL OF GOOGLE / NOT ONLY AI over the figure; the report's "8.1 billion gallons"; 54 counted golf-course tiles | 1, 2 |
| 3 | mechanism 1 | Why water? A chip turns nearly all its power into heat. Warm water carries that heat to a cooling tower. | 20 | fins turn red; warm beads ride the channel; callout WARM WATER; camera to the tower | 7 |
| 4 | mechanism 2 | There, a fan pulls air past it. Some evaporates and takes the heat along. The cooled rest goes back to the chips. Vapor never comes back, so Google counts it as consumed. | 32 | fan turns; yellow vapour rises from the stack; callout HEAT LEAVES; blue beads return; the report's definition rows; CONSUMED | 4, 7 |
| 5 | turn (63 %) | But Google does this on purpose. It says water cooling saves electricity compared with air. In Mesa, Arizona, where water is scarce, it plans air cooling instead. | 27 | ON PURPOSE; the site's "energy-efficient way"; the report's "Mesa, Arizona", "air cooling technology", "doesn't consume water"; vapour stops, dial needle rises | 5, 6 |
| 6 | payoff, loop | So every answer is paid for in water or in power. Next time you see an AI water number, ask which one it hides. That's the trade Google made. | 29 | WATER OR POWER; five lamps lit; the hit on "trade"; ends on 5 DROPS OF WATER | 6 |

Words: 149 (48.2 s take, 49.8 s video). Turn ("But") at 63 %. Loop: "…That's the trade Google made. One Gemini answer uses up five drops of water."

## Main picture

First idea (the category's costume): a water drop or a data-centre rack with a blue pipe. Second: a counted 54-tile golf grid (kept, as the picture of the 8.1 billion). Third and chosen: **the cooling tower as a bench machine** (new Anatomy figure `cooling-tower`): a server block with a heat sink that glows when it works, warm and cool channels with beads, a tower whose fan pulls air and whose stack lets yellow vapour rise, a rail of five lamps (the drops) and a dial (the electricity). Only this topic needs it: heat, water and vapour are the whole mechanism, and the lamps and dial hold the video's two sides (water, power).

## Beat sheet

| Cue word | Imp. | Picture event | Camera | In | Text | Sound |
| --- | --- | --- | --- | --- | --- | --- |
| five drops | 3 | five lamps light one by one | close on the lamps (shifted down) | start | 5 DROPS OF WATER | click |
| median | 1 | Google's phrase crop pops | held | whip | none | |
| not only AI | 2 | ALL OF GOOGLE, NOT ONLY AI over the figure; tags DATA CENTERS, OFFICES | held | | headline | |
| 8.1 billion | 2 | the report crop under a big number | push to 1.2 and back | | 8.1 BILLION GALLONS | |
| 54 | 3 | 54 tiles pop one by one | held | | 54 GOLF COURSES | pop |
| heat | 2 | fins glow red, warm beads start | push, then wide | push | POWER → HEAT | click |
| Warm | 1 | callout on the channel | wide | | | click |
| evaporates | 3 | vapour rises from the stack (acted word) | close on stack, then vapour | blur | EVAPORATES | click |
| cooled | 1 | blue beads return | close on the channel | | COOLED WATER BACK | |
| consumed | 2 | the report's definition rows | wide | | COUNTS AS CONSUMED | |
| But | 3 | the world turns | | dip | ON PURPOSE | impact |
| saves | 2 | the site's phrase crop | close on the dial | | WATER SAVES POWER | |
| air | 3 | vapour stops, needle rises | close on the stack | | AIR: MORE POWER | click |
| trade | 3 | payoff hit; headline returns to the hook's | | whip | 5 DROPS OF WATER | payoff |

## Self-test

- [x] 149 words (130 to 170); counted from `plan.json`.
- [x] Hook 9 words, names Gemini, says "water", no banned opener; frame-0 text and picture say the same thing (5 DROPS OF WATER over the running machine).
- [x] Stake by 10 s: median number in the first 5 s; 8.1 billion gallons at 9 to 11 s.
- [x] One running example (the tower); each step changes the picture (heat, warm beads, fan and vapour, cool beads, definition).
- [x] Turn ("But") at 63 %; re-hooks at about 3 s (median), 9 s (8.1), 15 s (why water), 22 s (fan), 24 s (evaporates), 28 s (never comes back), 31 s (but), 36 s (Mesa), 41 s (paid for).
- [x] Payoff the viewer can use ("ask which one it hides"); loop reads as one sentence.
- [x] Ear: sentences of 4 to 18 words; numbers as spoken; no exclamation marks; no banned words.
- [x] Cut test, sentences deleted while drafting: "Across everything it runs" (replaced by "All of Google's own… not only AI"), "Google compares that to" (the report's comparison is on screen), a separate "Google counts consumed water as water taken in minus water sent back" (the definition rows are on screen instead).
- [x] Every number, abstract noun and "but" has a picture (5 → lamps, 54 → tiles, 8.1 billion → the crop, heat → red fins, "but" → dip and the headline).
- [x] One word acted out: "evaporates" (the vapour rises and leaves).
- [x] No copy shapes. One line to watch: "paid for in water or in power".
- [x] Sources for every number: rows 1 to 6 above.
