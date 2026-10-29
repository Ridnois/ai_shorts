---
type: script
updated: 2026-10-28
series: How it works
words: 126
---

# Script: Helium and AI chips

Status: [[Helium and AI chips - Status]] · rules: [[Playbook]] §2a · first video built with the Anatomy medium ([[Design system]] *Anatomy figures*)

## Idea (P1)

- **Y:** more AI chips, on time. **X:** every chip is etched in a plasma chamber where helium under the wafer is the only practical way to carry the heat away, and a third of the world's helium came from one Qatari gas complex. **Series:** How it works (the mechanism), with a What's coming test at the end.
- **Real case:** QatarEnergy's helium offline from 2 Mar 2026 after the Ras Laffan attacks (force majeure 4 Mar).
- **Facts bank (research 28 Oct 2026; V verified at the page, S secondhand):**
  1. Qatar 63 of 190 million m³ of world helium in 2025, 33 % (USGS MCS 2026, 5 Feb 2026) V · 2. US 81 of 190, 43 % (same) V · 3. grade-A base price about $12 per m³ (same) V · 4. US helium use: 17 % is controlled atmospheres, fibre optics and semiconductors together (same) V · 5. USGS: large-volume helium seldom recycled V · 6. Ras Laffan: LNG and helium halted 2 Mar 2026, force majeure 4 Mar, second strike 18 to 19 Mar hit LNG trains 4 and 6 (Anadolu, Fortune/AP via Alupetra) S · 7. restart explosion 21 Jun 2026 (QatarEnergy via gasworld) S · 8. helium capacity about 25 % of normal in Aug 2026 S · 9. spot price roughly doubled in March (Reuters via Korea Herald) S · 10. 64.7 % of South Korea's 2025 helium from Qatar (KITA via Korea Herald, 24 Mar 2026) V at second hand · 11. Nikkei Asia 14 Jul 2026: US share of Taiwan's helium and noble-gas imports under 4 % in 2025, nearly 60 % in H1 2026; Qatar from about 88 % to about 30 % V · 12. Reuters 31 Mar 2026: Samsung and SK hynix stocks last to at least June, 4 to 6 months per a supplier source V · 13. SK hynix: "almost no chance" of impact (Reuters, Mar 2026) S · 14. thermal conductivity at 300 K: helium 0.1513, argon 0.01772 W/(m·K), 8.5 times (Wikipedia table, CRC data) V · 15. backside helium pressure 2 to 15 Torr (patents US7017652 and US6628503) V · 16. IDTechEx, 10 Sep 2024: wafer cooling has "no viable alternatives" S · 17. helium escapes Earth at about 1,600 t a year (RSC, Pitt; arXiv 2509.14499) S · 18. EUV scanners use hydrogen, not helium (Edwards Vacuum) S.
- **Not reached / not verified:** the exact shutdown date (28 Feb is the war, 2 Mar the helium); 30 % versus 33 % (we say a third); no late-October Qatari output; no named fab confirmed output cuts and none confirmed HBM or GPU packaging effects, so the script claims neither; recycling rates are conflicting (80 to 95 %), left out; Korea's Qatar share is 64.7 % (helium, KITA) or 55 % (Nikkei, noble-gas basket), we say "nearly two thirds" and name KITA; demand check not run (no YouTube token). The wafer model in the figure is a schematic.
- **Hooks (five types):** surprising fact ← "Chips for AI are cooled by helium." · number "A third of the world's helium went offline." · question "What cools an AI chip?" · contradiction "The AI race runs on a balloon gas." · stakes "One gas plant could stall AI chips." **Street-lamp:** headlines say helium threatens chips; none shows what helium does inside the chamber: pass. **Expert test:** the backside-cooling gap is "the interesting part". **Theme line:** AI chips are made on helium they never show.
- **Variety guard:** previous video used `balance`, counters and code panels; this one uses the Anatomy wafer chuck and a USGS page capture.

## Package

- **Promise:** why AI chips need helium, and the one question to ask when a shortage hits.
- **Titles:** **Why AI Chips Need Helium (A Third of It Went Offline)** ← · The Gas That Cools Every AI Chip · One Gas Complex Could Slow AI Chips
- **Thumbnail:** the wafer chuck, wafer hot in ember, words **COOLED BY HELIUM**; beats neighbours because the object is a real machine, not a logo.
- **Opening map:** scene 1 = the promise; scene 2 = proof (USGS, KITA) and the plan (why it cannot be swapped).

## Loop ledger (Playbook §2a)

| Loop | Opened | Closed | Re-hook / turn |
| --- | --- | --- | --- |
| L1 how does a gas cool a chip? | 1 | 3 | |
| L2 why not swap it for another gas? | 2 | 3 (8 times argon), 41 % of words | stake: South Korea, nearly two thirds |
| L3 so did chips stop? | 3 (end) | 4 | **turn "But"** at 54 % |
| L4 what do I ask when a shortage hits? | 4 (end) | 5 | |
| L5 (loop-back) who holds the stock? | 6 | the hook, wafer cooled | last frame = frame 0, changed |

## Scenes

| # | Question it answers | Raises | Voice (exact text) | Words | Visual beat | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | (hook) | how does a gas cool a chip? | Chips for AI are cooled by helium. In March, a third of the world's helium went offline. | 17 | Anatomy chuck, wafer hot; helium on, wafer cools; helium off, it heats again | USGS, QatarEnergy |
| 2 | where did it come from? | why not swap it? | It all came from one Qatari gas complex. South Korea bought nearly two thirds of its helium there. | 18 | real USGS page, camera onto the Qatar row; counter 64.7 % | USGS MCS 2026; KITA via Korea Herald |
| 3 | why can't it be swapped? | did chips stop? | Chipmakers cannot just swap it. Plasma heats the wafer while it is etched. Helium flows under the wafer and carries that heat into a cooled plate. It conducts heat more than eight times better than argon. | 36 | plasma on, wafer ember; wafer slides out, helium in the channels; back, clamped, cools; two bars 0.151 and 0.0177 | CRC data; patents; IDTechEx |
| 4 | did the chips stop? | what do I do with this? | But the fabs held months of stock. Then Taiwan switched: American helium went from under four percent of its imports to nearly sixty. | 23 | counters 4 % to 60 %; card | Reuters 31 Mar 2026; Nikkei 14 Jul 2026 |
| 5 | what do I ask? | (who?) | So a shortage is a stock question. Ask one thing of any chipmaker: how many months of helium do they hold? | 21 | close on the helium tank, its gauge falling; callout STOCK | |
| 6 | what is the point? | (loop-back) | AI chips depend on a gas nobody sees. Who holds the stock? | 12 | wafer cooled, frame 0 changed; comment prompt | |

Words: 127. Cut test: each scene answers one question and raises the next. Not verified: how the take sounds.
