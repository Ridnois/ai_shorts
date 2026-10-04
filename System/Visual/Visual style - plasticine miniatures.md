---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · defined from Kontext test B; used in the Chips Short; English-only since 3 Oct 2026
tags: [research, youtube, style, illustration, flux-kontext]
---

# Visual style: plasticine miniatures with a real reference

← [[YouTube Channel]] · [[Fast workflow]] · [[Narration guide]] · [[Prompt - per-scene generation guide]] · [[Research - Flux Kontext Pro with references (power)]]

> **User decision (3 Oct 2026):** *"From now on we're using flux-kontext pro plus real references."* It fixes the model and the method. The look comes from the only evidence: of three styles tested with Kontext, **only plasticine was recognised as a style** (flat vector and screen print came out as renders), and it is the look of the first video ("looks good"). **It is a choice derived from evidence, not a verdict from the user: it can be vetoed.** It was used in full for the first time in [[Chips and lithography - Status]] (8 plates; see "Result" there).

**Why it fits:** Kontext *edits* a photo, and "turn it into a clay miniature" is a natural edit; it keeps the real object's shape; and it is clearly a model, not a photo of an event ([[YouTube with AI - quality content guide]]).

## The language

| Element | Rule |
| --- | --- |
| **Material** | Handmade plasticine and clay, rounded forms, visible fingerprints and imperfections |
| **Scene** | Model on a table, soft studio light, plain warm background |
| **Colour** | Matte grey and cream clay; **a single copper-orange accent** on what matters |
| **Subject** | One large focal point; the rest barely hinted |
| **People** | Only hands, backs or clay silhouettes; no faces |
| **Format** | Vertical 9:16; subject between 15 % and 60 % of the height; nothing key in the bottom third or the top 6 % |
| **Text and figures** | Never inside the image: in editing ([[On-screen text style]]) |
| **Mechanism** | One image = one state; before and after are two images linked by the edit |

## How an image is produced

1. **Real-object sheet:** what it truly looks like and which parts must not be lost.
2. **Reference photo** with license, **cropped to the object and in the orientation of the result** (vertical for 9:16; a horizontal photo on a vertical canvas is rotated and distorted). A single `input_image`; a collage does not work. License and attribution go in the video's Status; with CC BY-SA, check before publishing. **Look for text and brands in the photo:** they leak into the image (a padlock's "PRADO BRAZIL").
3. **Prompt as an editing instruction** (template below).
4. **Review by eye** (missing parts, extra pieces) and **one retry**; if it fails twice, accept it, reframe it or drop the shot.

```
Redraw this exact {{object}} as a handmade plasticine clay miniature. Keep the exact shape and proportions: {{parts that must be kept}}. Replace the background with a plain warm tabletop. {{what happens in this scene according to the narration}}. The {{element that matters}} is in bright copper-orange clay. The {{object}} fills the frame, vertical composition.
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

Prompts in the positive. "Remove all lettering and logos" worked in the test; "no text" is not requested as a general style. Prompts are English, like the narration.

**Scenes with no object that has a photo** (a place, an idea): redesign them around an object that does have one; or use a photo of the place, or an already approved image from the same video. Kontext with text only: **unverified** (read the schema, free).

## Evidence from the Chips Short (8 plates, 3 Oct 2026)

- It **works with objects that have a photo** (wafer, padlock, lithography machine): the clay look and the copper accent hold.
- It **works only partly without a photo of the object** (a stamp, a mold): the model improvises from the nearest photo (a wafer); the stamp read well, the mold and the "lifting off" states did not.
- With a **photo of a real miniature or a physical machine** it can look almost like a photograph (the machine plate): less clay, more model photo.

## Known Kontext errors

| Error | Rule |
| --- | --- |
| Rotated or deformed piece (horizontal photo, 9:16 canvas) | Vertical input, or `match_input_image` and frame in editing |
| "Vector" or "screen print" come out as renders | Use plasticine |
| Parts missing or rings added | Name parts and quantities in the prompt; check by eye |
| Brand or text from the reference leaks into the result | Ask for a blank, unmarked surface; retry once |
| Interaction states (a mold pressing, a plate lifting) | Not reliable without a reference of that action; accept "almost right" |

## Open

- [ ] Test `match_input_image` and a prepared vertical input.
- [ ] Test a scene with no object using Kontext's real schema.
- [ ] Confirm `flux-kontext-pro`'s price (≈ $0.04, from memory).
- [ ] Have the user approve the look at P5 of a full video.
