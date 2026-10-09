---
type: research
created: 2026-10-09
updated: 2026-10-09
status: DRAFT for the user's approval; nothing uploaded; `publish.py` rewrites this note at upload
tags: [upload, youtube, week-01]
---

# Upload · Phone charging slows (draft)

← [[Phone charging slows - Status]] · [[Script - Phone charging slows]] · [[Publish]]

Render: `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/render/pc-42s-9x16-r1.mp4` (42.4 s, 112 words). Visibility proposed: **private first**. Approval: **pending** (title, thumbnail, description, visibility). Draft `upload/publish.json` is ready; after your yes: `python3 System/scripts/publish.py "Media/Week 01/2026-10-09 Fri/Phone-charging-slows/upload/publish.json"`.

## Thumbnails

Variant A (recommended: the phone with a half-full battery and "SLOWS ON PURPOSE" restates the hook): `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/upload/thumb.jpg`

Variant B (battery cells, "THE LAST 20% IS ON PURPOSE"; stronger colour, but "20%" is a rounder claim than the video makes and a cell label is readable): `Media/Week 01/2026-10-09 Fri/Phone-charging-slows/upload/thumb-b.jpg`

Both: kicker PHONE BATTERY, chips FAST TO ABOUT 70% | LITHIUM PLATES ON GRAPHITE | LAST 10% ADDS STRESS (Battery University). To use B, change `thumb` in `publish.json` to hero `stock/pc-s02-cell.jpg`, lines `THE LAST 20%` / `IS ON PURPOSE`.

## Title (pick one)

```text
Why Your Phone Charges Slower After 80%
```

1. **Why Your Phone Charges Slower After 80%** (recommended, 39 characters; the plain question people type).
2. Your Phone Slows Its Own Charging on Purpose (43; the hook's words).
3. Why the Last 20% of Charging Takes So Long (41).

Note: the title says 80% because that is what people search; the video says "near full" because the point where it slows differs by phone (70, 80 or 85 %).

## YouTube description (paste as is)

```text
A phone charges fast at first and slows near full on purpose: when the graphite in its battery is almost full, a strong current can leave lithium as metal on the surface, so the charger holds the voltage and lets the current fade.

New Shorts every day.

SOURCES
- Two-stage charging (constant current, then constant voltage), the 70 percent fast stage and why saturation adds stress: https://batteryuniversity.com/article/bu-409-charging-lithium-ion
- Lithium plating on graphite anodes during fast charging causes capacity loss and safety risks: https://deepblue.lib.umich.edu/items/e193b4c5-58e5-4706-b6be-8e4dc0e1468a
- Fully lithiated graphite sits close to the potential of metallic lithium: https://ossila.com/pages/lithium-plating
- iPhone Optimized Battery Charging pauses at 80 percent and finishes before you usually unplug: https://support.apple.com/en-us/108055
Where the slow stage starts differs by phone and by battery. Only the Battery University page was read in full; the other sources were checked from search summaries. Cut-off 9 October 2026. Figures checked on 9 October 2026.

PHOTO CREDITS (Wikimedia Commons)
Seawhelan, CC BY-SA 4.0 | Robert M. Lavinsky, CC BY-SA 3.0 | SD hehua, CC BY 4.0 | 10kdollz, CC BY-SA 4.0 | Public domain and CC0 photos: Sevenethics

The narration is AI-generated and the diagrams were drawn for this video; the photos are real.

#phonebattery #lithiumion #charging #howitworks #tech
```

## Pinned comment

```text
Should phones let you choose speed over battery life? Tell me what you think, and tell me your phone's charge limit if it has one. Sources are in the description.
```

## Studio settings

Not made for kids; synthetic-content answer: yes (AI voice, drawn diagrams); captions: upload `render/pc.srt` by hand.

## TikTok caption (paste as is)

```text
Your phone slows its own charging on purpose. Near full, a strong current can leave lithium as metal on the battery, so the charger lets the current fade. Should phones let you choose speed over battery life? #battery #lithiumion #charging #tech
```

## Claims

| Claim | Source | Strength |
| --- | --- | --- |
| A high current fills the battery to about 70 percent quickly; then the current tapers at constant voltage | Battery University BU-409 | read in full 9 Oct 2026 |
| The last stretch (saturation) adds about 10 percent but adds stress | BU-409 | read |
| Holding a cell above its voltage limit plates metallic lithium on the anode | BU-409 | read |
| Fast charging can trigger lithium plating on graphite | University of Michigan, Deep Blue abstract | summary only |
| Fully lithiated graphite is near the potential of metallic lithium | Ossila | summary only |
| iPhone Optimized Battery Charging pauses at 80 percent and finishes before you usually unplug | Apple Support 108055 | summary only |
| "Too much current can leave lithium as metal" in a phone near full | agent's reading of the above; not one primary statement | **open** |

## Checklist

- [ ] Open the Apple, Deep Blue and Ossila pages and confirm the wording
- [ ] You choose title and thumbnail A or B, confirm visibility
- [ ] `Analytics/videos.csv` row (the P8 script writes it)
- [ ] Pulls at 24 h, 7 d, 28 d; compare `viewed_pct` with Neon for chips and Netflix screenshot
