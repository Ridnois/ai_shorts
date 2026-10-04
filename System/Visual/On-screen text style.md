---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v4 · word-by-word captions and the caption zone added; the Magnetar feedback called the card style "good and appealing" (4 Oct 2026); v3 text with purpose and personality
tags: [research, youtube, style, typography, text]
---

# On-screen text style

← [[Illustration pipeline]] · [[Channel identity]] · [[Blender editing]] · [[YouTube Channel]]

> **Feedback (4 Oct 2026, Twisted carbon):** the text and added content were *"too generic, soulless and with lack of personalization"*. v3 changes **what the text is for**, not only how it looks. v1 and v2 (a label, a title and a detail on every plate) produced cards like "Same material" or "The takeaway" that fit any video.

## 1. What on-screen text is for

| Purpose | Format | Rule |
| --- | --- | --- |
| **Name a part** (explain a machine or a structure) | **Callout**: a copper dot on the part, a leader line, a short label | 1 to 4 words, a noun phrase naming the real part ("Vacuum gap", "Top layer: 1.1°"); at least one on every photo or explainer; at most 3 per plate |
| **Quantify** | **Number card**: the big figure with its unit, what it measures and the source | one per video, the figure the argument rests on |
| **Frame and source** | **Context card**: label, title, detail | label = the frame (a place, date, person or mechanism), title = the strongest fact as a statement with a verb, detail = the source, the scale or the caveat |
| **Give a voice** | **Margin note**: a short aside in the narrator's voice ([[Channel identity]]) | at most 2 per video; ≤ 60 characters; no jokes that need explaining |

**Not every plate needs a card.** A plate that carries callouts or a number does not also need a context card. Silence on screen is fine.

## 2. Writing rules (the specificity test)

1. **The specificity test:** could this text appear unchanged in a video about another topic? If yes, rewrite it with a name, a number, a place or a mechanism from this topic.
2. **Banned generic labels:** *The takeaway, Key point, Fun fact, Same material, Why it matters, Did you know, In summary*. Labels name something: "Manchester, 2004", "Where the helium goes", "Layer 2".
3. **Titles are statements**, not topics: "Electrons slow to a crawl" beats "Flat bands". Max 26 characters; if it does not fit, shorten the idea, not the size.
4. **Details carry evidence:** a source (journal, agency, year), a scale ("about the width of a hair") or a caveat ("manufacturer's figure"). Max 40 characters.
5. **Do not repeat the narration.** The text adds what the voice does not say: a number, a part name, a source, a caveat, a human detail.
6. **Figures:** with unit and a thin space, English formatting: `180 °C`, `72.5 %`, `1,000`. Check the typeface has every symbol (`→`, `≈` may be missing in Noto Sans Display Bold: use `·` or "to").
7. **No exclamation marks, no emojis, no sustained capitals** (only the label is spaced capitals).
8. **English, with the channel's banned words list** in [[Channel identity]].

## 3. Design

| Element | Specification |
| --- | --- |
| **Typefaces** | Noto Sans Display Bold (titles, numbers), Noto Sans Regular (labels, details, callouts) |
| **Context card** | warm paper `#F9F6EE` at 94 %, 16 px corners, 1 px graphite border at 25 %, **8 px copper bar** on the left; 894 × 280 px, centred at **28.5 % of the height from the bottom** (the caption zone stays free); label 32 px spaced capitals in copper `#C76B38`, title 56 px bold in ink `#1C1A17`, detail 34 px in `#4D4741` |
| **Number card** | same card; the figure 124 px bold in copper, caption 44 px bold, source 30 px |
| **Margin note card** | same card; label "Margin note" in copper, the text on two lines of ≤ 30 characters, 46 px bold |
| **Callout** | copper dot (13 px) with a ring, leader line (2 px), label in a small paper box with a copper bar, 34 px; **never over the card**: labels move above it automatically |
| **Motion** | fade in over 0.25 s with a 24 px rise (cards), out over 0.2 s; the card enters 0.45 s after its plate; callouts enter 1 s after the plate, 0.6 s apart |
| **One at a time** | one card per plate; never two cards at once |
| **Captions (every video)** | one word at a time, centred at **16.5 % from the bottom**, Noto Sans Display Bold 88 px, capitals, white with a dark outline and a soft shadow, figures in copper; cards and callouts never enter this zone (callout labels are clamped above it). Rules and timing: [[Shorts quality bar]] §3 |
| **Backdrop** | a card or callout always sits on a real photo or a faithful explainer, never on a bare gradient ([[Illustration pipeline]] §1.7) |

Implementation: `System/scripts/build_video.py` reads the plate's `card` (a list for a context card, or `{"kind": "number" | "note", …}`) and its `callouts` from `plan.json` ([[Illustration pipeline]] §6, [[Blender editing]]).

**Keep exactly (Superconductors feedback, 4 Oct 2026: text boxes, callouts and highlight 5 of 5, captions 5 of 5; *"keep: text distribution, and notes"*):** the card, callout, margin-note and caption layout in §3; only the caption size changed (104 to 88 px). **No branding on the video itself** (progress bar, mark, series tag were rated 0 and removed). The user's earlier verdict on the style (Magnetar, 4 Oct 2026): *"The style of the added text is good and appealing, keep improving."* **The card, callout and copper-accent look stays as it is**; improvements go into specificity (§2), placement over real images and the captions, not into a redesign.

The whole system (tokens, components, safe zones, highlight rule) is written as one table in [[Channel playbook]] §3.

## 4. Copy examples (Twisted carbon, rewritten with the specificity test)

| Plate | Before (v2) | After (v3) |
| --- | --- | --- |
| twisted layers | `Magic angle · Twist one sheet by 1.1° · Two graphene layers, MIT, 2018` | number card: **1.1°** · "twist between two graphene layers" · "Cao et al., Nature, 2018" |
| pencils | `Same material · Pencil lead is graphite · Graphene is a single layer of it` | margin note: "Yes, the same carbon as your pencil lead." |
| dewar | `1911, Leiden · Mercury cooled in helium · Resistance vanishes near 4.2 K` | callouts on the dewar: "Liquid helium, 4.2 K", "Vacuum jacket"; context card: `Leiden, 8 April 1911 · Onnes's mercury wire hits zero · Gilles Holst reads the galvanometer` *(only if sourced)* |
| close | `The takeaway · Same carbon, new layout · Design instead of discovery` | context card: `What the 1.1° buys · One element, three behaviours · Insulator, conductor, superconductor` |
