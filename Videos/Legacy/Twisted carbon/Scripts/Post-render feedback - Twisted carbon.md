---
type: feedback
created: 2026-10-04
updated: 2026-10-04
status: received · applied to the vault on 4 Oct 2026 (see Response at the end)
tags: [youtube, feedback, twisted-carbon]
---

# Post-render feedback · Twisted carbon

← [[Twisted carbon - Status]] · [[Feedback loop]]

## Narrative
Narrative ig good, content is interesting, data is on point and appealing to listen, no modification required on the voice generation pipeline.

## Illustrations
This is where we're failing. the images feel not to be representing the content, nor describing the scenes, those shapes and styles are not helping.

I see to little focus on the prompt quality, is not related enough with the content. my take here: less aproach on scene description, is not a theatre show, is modern content. more focus on usslower than last time, so I'd plan 135–145.slower than last time, so I'd plan 135–145.ing illustrations where they are useful, describe machines and explaining processes. also i want you to use free stock photos, redesign the vault video generation to do the images this way, a mix of generated images with fully descriptive prompt and references and free stock photos.

I think you should use the model on the style it performs best, not custom illustration style, get as close as generic style as possible so we make better use of the model.

Based on all i told you, redesign the illustration pipeline in order to integrate outside sources and generate better, more related with the content images. you could generate images with transparent background and apply background gradient colors and styles on blender.

Work more on the vault's definition of text and added content, it still being too generic, souless and with lack of personalization, consider this requirement into the image generation pipeline too. (Remember, edit the vault to make it work better on next iterations)

## Technical

Small voice cut on the start of the video, make sure voices clips are complete and well put into the blender video sequencer.

## Vault management

I want to make sure that all suggestions and requirements always ends on improvements on the knowledge present on this vault. our focus is to edit the content based on my feedback, you can show me what you changed but focus on seeing all the vault as a single source of knowledge and keep it coherent with general ideas and feedback accross all documents.

Make sure the agent that works on this vault gets their guide


---

## Response (4 Oct 2026)

| Feedback | Where it now lives |
| --- | --- |
| **Narrative is good; no change to the voice pipeline** | Nothing changed in the script or the voice generation ([[Channel voice]], [[Narration guide]]). Recorded as confirmation that the idea gates and the hook rule work: [[Idea and hook quality]] |
| **Illustrations fail: they do not represent or describe the content; shapes and styles do not help** | The plasticine style is **retired**. New method: [[Illustration pipeline]] (usefulness test per plate; visual plan before any prompt; real things photographed, hidden things explained). Rule block 2.x in [[Guidelines for new scripts]]; stage 3 of [[Production process]] is now the visual plan |
| **Too little focus on prompt quality; less scene description ("not a theatre show"), modern content; describe machines and explain processes** | [[Prompt - per-scene generation guide]] v4: a prompt is a *specification, not a scene* (exact object or process, parts and arrangement, view, what must be readable, what each reference supplies); banned mood words; worked examples (cutaway, process, cutout) |
| **Use free stock photos; mix generated images (fully descriptive prompts, references) with stock photos; redesign the vault to do it this way** | [[Illustration pipeline]] §2 (types and the default mix: ≥ a third stock, ≥ a third explainers or cutouts, ≤ 5 generated, no two consecutive plates of one type) and §5 (sources). Tool: `System/scripts/stock_photos.py` (Openverse, NASA, Wikimedia; credits logged). [[Fast workflow]] packages A to C and §3 to §7; [[Media convention]] (`stock/`, `_credits.jsonl`) |
| **Use the model in the style it performs best, not a custom style; as generic as possible** | [[Illustration pipeline]] §1.4 and §4; [[Guidelines for new scripts]] rule 2.5 (no style block); `gpt-image-1.5` for generated plates, `flux-kontext-pro` demoted to photo edits ([[Channel models]], [[Fast workflow]]) |
| **Transparent backgrounds, with gradients and styles applied in Blender** | [[Illustration pipeline]] §3 and §6; builder `System/scripts/build_video.py` with plate types `full`, `contain`, `cutout` over generated gradients, soft shadows, callouts and cards from a `plan.json` ([[Blender editing]]). Tested end to end on a synthetic plan |
| **Text and added content too generic, soulless, no personalization; apply it to the image pipeline too** | New [[Channel identity]] (the curious specialist, recurring devices, banned words, the specificity test) and [[On-screen text style]] v3 (callouts that name parts, number card, margin note, specific context cards). The same callouts are part of every plate in the visual plan |
| **Technical: small voice cut at the start; clips complete and well placed in the sequencer** | Diagnosed with the actual audio: the TTS files start abruptly (scene 1 had 0.06 s of silence; scenes 2 and 5 started mid-sound). `build_video.py` pads and fades every take and checks every voice (`CHECK=1`): [[Blender editing]] ("Voices: complete, padded and checked"), [[Guidelines for new scripts]] §4 |
| **Vault management: every suggestion ends in improvements to the vault's knowledge; one coherent source across all documents; the agent gets its guide** | [[Feedback loop]] (the procedure and the layer map), `System/scripts/check_vault.py` (broken links, front matter, index, encoded-feedback invariants), and **`CLAUDE.md` at the vault root**, the agent's guide: read order, hard rules, feedback protocol, tooling and gotchas. The pipeline runner reads the same notes |

