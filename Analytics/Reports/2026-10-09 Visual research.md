---
type: research
created: 2026-10-09
updated: 2026-10-09
status: v1 · evidence behind the visual redesign of 9 Oct 2026; rules now live in [[Playbook]] §3 and [[Style]]; channel data has not tested them yet
tags: [research, visuals, motion, footage, policy]
---

# Visual research · 9 Oct 2026

← [[Playbook]] §3 (the rules) · [[Style]] (motion plates) · [[Workflow]] (tools, budget) · [[YouTube Channel]]

**Trigger** (user, 9 Oct 2026): *"Plates and additional stock images are not helping make the content easier to understand, that makes the short boring, visual content need a lot of improvement yet. redesign the way you decide which photos to use, where put them, what kind of support content you use and how you display the elements. consider other ways of media not contempladed before like videos."*

## 1. Diagnosis of the Neon (r3) and Phone charging (r1) renders

- **Pictures of nouns, not of what happens.** A rock for "graphite", an office tower for "chip machine maker", a charger with a callout reading "Charger". Each picture names a thing the voice says; none shows the change the sentence is about.
- **Repetition to meet the plate count.** Phone charging r1: 14 plates from 5 photos; the same phone photo on 3 plates plus 2 insets; the same graphite rock on 3 plates plus 2 insets (the builder now prints `REPEAT`). The 16 to 20 plates rule produced quantity, not relevance (the 5 Oct assessment had already warned of this).
- **Nothing moves.** 0 % of r1's runtime was footage or animation (the builder now prints `MOTION SHARE`): stills with an 8 % push. YouTube's monetization policy names *"image slideshows ... with minimal or no narrative"* as ineligible.
- **Cuts land on arbitrary syllables.** Plates split each scene into equal parts, so a picture rarely arrived with the word it illustrates.
- **Too many layers, small text.** Diagram box, blurred backdrop, inset, card, callout and caption at once. Diagram labels of 20 to 30 px are unreadable on a phone, and cards repeated the narration.

## 2. Evidence (full citations kept in the research agent's report; key ones here)

| Finding | Source |
| --- | --- |
| Temporal contiguity (picture with its word) is among the largest design effects: median d 1.30; coherence 0.70; signalling 0.46; redundancy 0.87 | Mayer 2017, *J. Computer Assisted Learning*, doi 10.1111/jcal.12197 (abstract) |
| Design matters most in **system-paced** media (a Short cannot be paused to study) and for complex material | Noetel et al. 2022, *Review of Educational Research*, 29 meta-analyses |
| Seductive details (interesting but irrelevant pictures) lower learning across 58 studies, most when static and next to a relevant diagram | Sundararajan & Adesope 2020 |
| Decorative pictures give about no benefit; representational help; organizational and explanatory help most | Carney & Levin 2002 |
| Animation beats static pictures, d 0.37 overall, 0.76 for realistic video; 0.34 with narration; it wins when the **change** must be understood, statics win for spatial layout | Höffler & Leutner 2007; Berney & Bétrancourt 2016; Ploetzner et al. 2021 |
| More camera changes **within one scene** raise attention and memory; fast cuts to new content lower memory of the words | Lang et al. 2000; Lang, Potter & Bolls 1999 |
| On-screen key terms help; verbatim text next to narrated visuals tends to hurt; captions help comprehension and sound-off viewing | Adesope & Nesbit 2012; Trypke et al. 2023; Gernsbacher 2015 |
| Policy: YouTube YPP *"inauthentic content"* (renamed 15 Jul 2025) excludes slideshows and mass-produced AI templates; AI use must be disclosed for photorealistic scenes that did not occur (infographics and full animation exempt); TikTok requires labels on realistic AI scenes (rules effective 24 Sep 2026) | support.google.com/youtube/answer/1311392 and /14328491; tiktok.com community guidelines, read 9 Oct 2026 |

No credible retention study ties a cut rate to Shorts retention; "change every 1.5 to 4 s" appears only in blogs. Top explainer channels in the niche (Zack D. Films, Jared Owen, Kurzgesagt) are animation-first; Jared Owen animates first and fits narration to it.

## 3. New media checked (live, 9 Oct 2026)

- **Footage:** Wikimedia Commons is the only keyless source with modern footage: 0 to 3 relevant clips per technical query (copper mine 3, nodules 3, EV charging 3, phone charging 0, lithium plating 0). Pexels and Pixabay (free keys, commercial use, portrait filter on Pexels) are the volume sources; NASA and Internet Archive are niche. A 1080p landscape clip cropped to 9:16 is 608 px wide (soft but fine for 3 to 4 s); 4K crops at full quality. Accept PD, CC0, CC BY, CC BY-SA, Pexels, Pixabay only.
- **Animated explainers:** cairo (already installed) draws a 1080×1920 frame in about 13 ms; a 6 s plate renders in about 5 s at $0. Built as `System/scripts/motion.py`.
- **AI image-to-video (opt-in):** cheapest credible on Replicate is `lightricks/ltx-2.5-fast` (9:16, 720p, 4 s, audio off) at about **$0.12 a clip**; fallback `bytedance/seedance-1.5-pro` at about $0.10 (prices read from the model pages on 9 Oct 2026, **unconfirmed by a bill**). Only gentle motion on a checked real photo; never the mechanism; photoreal clips get YouTube "AI use" and the TikTok AI label.

## 4. Test: Phone charging r2 (same voice and words as r1, new visuals, $0)

8 motion plates on the word, 100 % moving runtime, 0 repeats, every text ≥ 40 px and outside the caption band (checked by `motion.py`). The phone returns as a visual anchor (scenes 1, 2, 5) and changes state each time; the charge curve builds its two stages on "holds" and "fade". Not yet judged by the user (P7); no channel data. Weak spots seen on stills: the lower third is calm (dark) on several plates, and no real footage was available without a Pexels key.

## 5. Open

Pexels and Pixabay keys (the user's call); one paid AI-video test (about $0.70 for 2 photos on 3 models) before any clip enters a Short; whether the motion-first look holds retention: compare 4 Shorts in the new style with the last 4 ([[Publish]] §Analytics loop), plus a muted check (one transfer question, three viewers).
