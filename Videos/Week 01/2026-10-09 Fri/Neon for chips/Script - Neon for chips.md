---
type: research
created: 2026-10-09
updated: 2026-10-09
status: P1 to P3 done as text; stopped at P4 (no media, no spend); compact test video
tags: [research, youtube, script, semiconductors, neon, week-01]
---

# Script · Neon for chips (Week 01, Friday 9 Oct)

← [[Neon for chips - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

Source idea: `Analytics/Generated ideas/Youtube idea #4.md` (YouTube's suggestion, 9 Oct 2026). **Y:** the chips in every device keep getting made. **X:** their lasers need neon, and neon is a by-product of big steel plants, so the supply sat in very few places. **Theme line:** *Chips depend on a leftover gas from steel plants.* **One question:** why does the most advanced factory on Earth depend on steel mills?

## Corrections to the source idea

| Idea said | Found | Script does |
| --- | --- | --- |
| Neon "generates that ultraviolet wavelength" | The wavelengths come from argon fluoride (193 nm) and krypton fluoride (248 nm) (Wikipedia, Excimer laser, **read**). Neon is part of the mixture, not the light source | Voice: argon and fluorine make the light, neon is the gas they are mixed in. **Open:** buffer role and its share are snippet-level, open ASML or Cymer before P4 |
| Neon comes "from industrial steel smelting" | It is a by-product of the **air separation** units that steel mills run to get oxygen and nitrogen; only very large plants can recover it (gasworld, Springer, snippets) | Voice: "steel mills split air for oxygen" |
| "Half the world's supply" | Reuters via Techcet: **two** Ukrainian firms (Ingas, Cryoin) supplied 45 to 54 % of **semiconductor-grade** neon in 2021; other outlets say 70 % of all neon, Bain says about two fifths from Russia and Ukraine | Voice: "about half of the neon for chips, from two companies", attributed on screen to Reuters and Techcet, 2022 |
| "Map of steel hubs" | No sourced map found | Plate shows the Ukrainian share as a bar, not a map |

## 0. Facts bank (**read** = page opened 9 Oct 2026; **snippet** = search result only, not for the voice unless attributed)

| # | Fact | Source |
| --- | --- | --- |
| 1 | KrF and ArF excimer lasers give 248 and 193 nm light for photolithography | Wikipedia, Excimer laser (**read**) |
| 2 | An excimer laser uses a noble gas (argon, krypton or xenon) plus a reactive gas (fluorine or chlorine) | same (**read**) |
| 3 | Neon is part of the gas mixture in the lasers used for chip lithography | Silicon Republic, Reuters coverage (snippet) |
| 4 | Ingas (Mariupol) and Cryoin (Odessa) supplied 45 to 54 % of semiconductor-grade neon in 2021 | Reuters with Techcet data, 2022 (snippet) |
| 5 | Chip neon demand in 2021: about 540 t | Techcet via Reuters (snippet) |
| 6 | Ingas sent 75 % of its output to chipmakers; customers in Germany, Taiwan, South Korea, China, US | Reuters (snippet) |
| 7 | Both Ukrainian firms shut after the invasion (company statements to Reuters, March 2022) | Reuters (snippet) |
| 8 | Largest fabs (Intel, Samsung, TSMC) could cover "two months or more" from stock | Techcet, PC Gamer (snippet) |
| 9 | After 2014 chipmakers cut neon use and raised stock; suppliers and fabs held 3 to 12 months | Bain's Peter Hanbury (snippet) |
| 10 | ASML reportedly cut its reliance on Ukrainian neon to about 20 % of before | PC Gamer / Silicon Republic (snippet) |
| 11 | Neon, krypton and xenon are by-products of the air separation steel plants run | gasworld, Springer (snippet) |
| 12 | Neon is about 18.2 ppm of air by volume, so about 55,000 litres of air hold one litre (agent's arithmetic from the ppm) | Wikipedia, Neon; patent US 5100446 (snippet) |
| 13 | Recovery pays only at very large plants | gasworld (snippet) |
| 14 | New neon capacity elsewhere would take nine months to two years | Supplyframe via Reuters (snippet) |
| 15 | Chinese neon price quadrupled, 400 to 1,600 yuan per m3, Oct 2021 to Feb 2022 | Reuters (snippet) |
| 16 | Kametstal reported shipping 16,000 m3 of neon-helium mixture in 2022 | GMK Center (snippet, not for voice) |
| 17 | Not found: current (2026) share of Ukraine or China in chip neon | agent; **the video must say "in 2022"** |

## 1. Idea gate

**Street-lamp test: pass, with a limit.** The headline ("Ukraine war threatens chip neon") ran in March 2022. What it skipped, and this video adds: **why a steel mill is a neon plant** (air separation, 18 ppm, only the largest plants pay) and that neon is the **carrier, not the light**. One-sentence mechanism: *chip lasers need neon, neon is 1 part in 55,000 of air, and only big steel-plant air units recover it, so supply sits where the steel is.*
**Scores:** surprise 4 · scale 4 · depth 4 · evidence 3 (snippets, to read before P4) · showable 3 · plain 4. Thread ≥ 4 on surprise, scale, plain: met.
**Coffee test:** *"The most advanced chips are made with a gas that steel mills leave over."* "Wait, really?" surprise 4.
**Expert test:** a lithography engineer's interesting part is the buffer gas and purity; a gas engineer's is the air separation. Both are in. Open: read one primary page on the buffer role.
**Against the idea:** (1) "old 2022 news": answered by the mechanism, and the video dates itself; (2) "neon is just signs": answered by hook; (3) "already supply fixed": honest close says the 2026 state was not found. If scene 4 reads as a news recap, surprise drops to 3.
**Demand check: not run.** `youtube_search.py` needs `YT_ANALYTICS_REFRESH_TOKEN`, absent on this machine. Evidence in hand: YouTube's own diagnostic says chokepoint videos (Spruce Pine quartz, copper) lead; 2022 neon coverage was wide. Run the search when the token is present. **Topic family:** materials and resources (series: *Materials behind modern tech*); the last published video was Netflix screenshot (software): spread ok.
**Five hooks:** surprising fact (leading) "Chip factories depend on a leftover gas from steel plants, and about half of it came from two companies in Ukraine." · contradiction "The most advanced factory on Earth cannot run without an old steel mill." · stakes "Every phone chip needs a gas that almost nobody sets out to make." · number "One litre of neon hides in 55,000 litres of air." · question-as-claim "Why does making a chip need a steel plant?"

## 2. Package

**Y/X:** above. **Promise:** chips depend on a gas that steel mills leave over. **Titles:** *Why Chips Depend on a Steel Plant Leftover* (recommended) · *Half the Neon for Chips Came From Two Companies* (2022 date in description) · *The Gas Every Chip Laser Needs*. **Thumbnail:** hero = chip-lithography machine or wafer photo (stock, $0, to find); kicker **SEMICONDUCTORS**; lines **A STEEL MILL'S** / **LEFTOVER GAS** (second orange); chips **ABOUT HALF FROM 2 FIRMS** · **1 LITRE IN 55,000** · **2022 DATA**. Beats neighbours (to check at search) by naming the odd link, steel to chips. **Opening map:** scene 1 promise; scene 2 proof (lasers, neon in the mix) and plan.

## 3. Script (P2), rewritten 9 Oct 2026 after P7 feedback: compact test video, 117 words, 5 scenes

User feedback: *"i feel the hook weak, i got lost before 5 seconds. and i saw no conclussion. content should be low attention proof"*. **Changes:** hook is one plain sentence a stranger gets with half an ear ("Every chip is made with a gas from steel mills") followed by the stake; argon, fluorine and "ultraviolet" removed from the voice (jargon lost the viewer in scene 2); every sentence ≤ 12 words with one idea; the conclusion is spoken ("So here is the point...") and shown on a card before the question.

Bridges: 2 "The gas is neon" · 3 "So why steel mills?" · 4 "So very few places make it" · 5 "So here is the point". **Facts (4):** neon is used in chip lasers; steel-mill air plants leave it over; only very large plants recover it; two Ukrainian firms supplied about half in 2021 and shut in 2022. **Spoken figures:** 1 (half) plus the year. **Cut test:** laser gases, 55,000 (screen only), firm names, China price, ASML.

| Scene | Voice text | Words | Delivery | Pause after (s) |
| --- | --- | --- | --- | --- |
| 1 | Every chip is made with a gas from steel mills. And about half of it came from two companies in Ukraine. | 21 | plain, direct, a little surprised | 0.60 |
| 2 | The gas is neon. Many chip machines use it inside their lasers. Without neon, those machines stop. | 17 | clear, simple | 0.45 |
| 3 | So why steel mills? They split air to make oxygen. Neon is a tiny leftover in that air. Only very large plants can catch it. | 25 | light, one fact at a time | 0.45 |
| 4 | So very few places make it. In twenty twenty-two, those two companies shut down. Chipmakers had to live off their stock. | 21 | steady, grave on "shut down" | 0.90 (before the conclusion) |
| 5 | So here is the point. The most advanced chips depend on a leftover from old steel mills. Should the chips that run everything depend on a leftover gas? Tell me what you think. | 33 | warm, slower on the point, open on the question | (tail) |

Inner pauses after "mills" (scene 1, 0.6), "neon" (2, 0.4), "mills" and "oxygen" (3), "it" (4), "point", "mills", "gas" (5). On screen: scene 5 plate 10 carries the conclusion card ("Chips rely on steel mills"), plate 11 the question. "About half" is the Reuters and Techcet 45 to 54 % estimate (fact 4); "those two companies" are Ingas and Cryoin; "had to live off their stock" is Techcet's "two months or more" for the largest fabs (fact 8, snippet): open before any upload.

## 4. Visual plan (P3): 12 plates, prefix `ne`, folder `Media/Week 01/2026-10-09 Fri/Neon-for-chips/` (nothing downloaded: P4 not passed)

Candidates to find (Commons, NASA, Openverse; need ≥ 1,080 px, licence): a DUV lithography machine or wafer; a steel plant at night; an air separation unit; a neon sign (hook contrast); a phone or circuit board. No identifiable people, no Ukraine war imagery.

| # | Sc | Type · layout | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- |
| 1 | 1 | S full + callout | a steel plant, so the hook's "steel" is real |
| 2 | 1 | S contain blur + number card | "about 50 %, 2022, Reuters and Techcet" over a phone photo |
| 3 | 2 | S full + callout | a lithography machine, so "chip machines" is a real thing |
| 4 | 2 | G split + inset | a laser tube with argon and fluorine making light and neon as the carrier (schematic, only what fact 2 and the open buffer note support) |
| 5 | 2 | D split | 193 and 248 nm sit in the ultraviolet, off the visible band |
| 6 | 3 | D split | one litre in 55,000: a litre bottle against a grid of 55,000 dots |
| 7 | 3 | S full + callout | an air separation unit, so "steel mills split air" is a plant |
| 8 | 3 | D split | air in; oxygen, nitrogen and traces of neon out |
| 9 | 4 | S contain blur + card | "only the largest plants recover it" (gasworld) |
| 10 | 4 | D split | a bar: two firms, 45 to 54 % (Reuters), the rest |
| 11 | 5 | S full | a phone, the question coming |
| 12 | 5 | S contain blur + margin note | the closing question; last plate repeats plate 1's steel plant (loop) |

**Mix:** 5 S, 5 D, 1 G, 1 shared. Weak points: 12 plates for about 40 s means 3 to 4 s each; two figures (55,000, 45 to 54 %) are drawn schematically; no photo of neon itself in a laser.

## 5. Not verified

Facts 3 to 16 are search snippets; the buffer-gas role and its share; Ukraine's or China's current share (fact 17); the arithmetic in fact 12; voice, pace and everything the agent cannot hear. P7 is the user's.
