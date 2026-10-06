---
type: process
created: 2026-10-06
updated: 2026-10-06
status: P1 to P3 done; waiting for the user's P4 (budget and voice test)
tags: [status, week-01]
---

# Decimal error · Status

← [[Script - Decimal error]] · [[YouTube Channel]] · [[Workflow]]

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research | done | 6 Oct 2026 (user chose the idea) | Y: correct money code. X: cut-off error that grows with running time. Hook type: surprising fact. Demand: medium (200k best). Street-lamp: pass with the accumulation mechanism. Scale scored 3: carried by the consequence and the 7 m to 687 m growth ([[Script - Decimal error]] §1) |
| 2 Script · 3 Visual plan | done (agent) | pending the user's read | 164 words, 7 scenes, 18 plates (5 S, 10 D, 3 G); package (titles, thumbnail, promise) in the Script note §2. Schematic: "cut-off at every tick" simplifies the 24-bit conversion |
| 4 Prompts, stock, budget | **waiting for the user** | | base about $0.91, cap about $1.09 (voice and gpt-image-2 prices unconfirmed); no media, no Replicate call yet; voice test of scenes 1 and 2 on turbo-v2.5 first |

*Not verified:* see the Script note §3. *Feedback:* none yet.

## Prompts for the 3 generated plates (`openai/gpt-image-2`, content first, no style words; not run)

Output line for all: "plain white background, no letters, numbers, labels or logos, flat diagram, no glow, no shadows". Text and numbers are added by the builder.

1. **Plate 4, register (no references).** Subject: a binary register shown as one horizontal row of 23 equal square cells, then a vertical cut line, then 5 more cells to its right drawn faded and cut off by the line. Fill (dark) or leave empty the 23 cells left to right as: empty empty empty filled filled empty empty filled filled empty empty filled filled empty empty filled filled empty empty filled filled empty empty. View: straight on, 2:3 portrait, the row in the upper half.
2. **Plate 14, range gate (references: GAO figures 4 and 5, rendered from the PDF).** Subject: two stacked panels. Each has a radar dish at the left, a thin beam going right, a rectangular gate drawn across the beam, and a simple missile outline. Panel 1: the missile is in the centre of the gate. Panel 2: the same gate sits further left and the missile is outside it, to the right. View: top-down, same scale in both panels.
3. **Plate 16, incident (no references).** Subject: a top-down schematic of open flat ground. At left a missile launcher and a radar dish (one battery); at right a rectangular low building. A dashed arc descends from the top right to the building (the Scud's path). A short beam from the radar ends in a small gate placed short of the arc, with no missile inside it. No people, no fire, no explosion, no other vehicles.

Checks after generation: count the cells and compare the pattern (plate 1), missile outside the gate only in panel 2 (plate 2), nothing added that the GAO report does not state (plate 3). One retry per image; a failed plate becomes a drawn plate.
