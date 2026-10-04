---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v4 · one generic builder driven by plan.json; padded and checked voices; plate types and callouts (4 Oct 2026)
tags: [research, youtube, editing, blender]
---

# Blender editing

← [[YouTube Channel]] · [[Production process]] · [[Transitions and effects]] · [[Media convention]] · [[Illustration pipeline]] · [[On-screen text style]]

Stage 7 of the [[Production process]]: the cut is assembled in Blender 5.2's video sequencer (installed on this machine) from a script, without opening the interface and without ffmpeg. **Since 4 Oct 2026 there is one generic builder, `System/scripts/build_video.py`, driven by a `plan.json` per video**; the per-video scripts of earlier videos are kept only to re-render those videos (table below). The **language of transitions and effects** is in [[Transitions and effects]].

## How it runs

```
VIDEO="Media/<Video> - <N seconds>" SOLO_PROYECTO=1 CHECK=1 blender -b --factory-startup --python System/scripts/build_video.py   # assemble, measure, check the voices
VIDEO="Media/<Video> - <N seconds>" blender -b --factory-startup --python System/scripts/build_video.py                          # assemble and render
```

- Run the first command, read the printed timings and the `CHECK` lines, then render **in the background** (≈ 3 to 5 minutes for 85 s). Paths in the saved `.blend` are absolute, so it can be reopened from anywhere.
- Output: `render/<prefix>-<duration>s-9x16-r<n>.mp4` (1080×1920, 24 fps, H.264 and AAC) and the `.blend`. **To look at frames without ffmpeg**, open the `.blend` in background mode and render stills with `bpy.ops.render.render(write_still=True)` at `resolution_percentage = 33`.

## The plan file (`plan.json`)

Full schema and plate types: [[Illustration pipeline]] §6. Top level: `prefix`, `size`, `fps`, `gaps` (silence between scenes), `start`, `tail`, `voices` (paths relative to the video folder), `scenes[].plates[]`. Each plate: `type` (`full`, `contain`, `cutout`), `file`, placement (`focus`, `pos`, `size`, `width`), gradient (`bg`, `bg_angle`), `callouts[]` and a `card` (context list, or `{"kind": "number" | "note", …}`, see [[On-screen text style]]).

## Voices: complete, padded and checked

Feedback (Twisted carbon, 4 Oct 2026): *"small voice cut on the start of the video, make sure voices clips are complete and well put into the blender video sequencer."* What the data showed: the TTS files often **start abruptly** (scene 1 had 0.06 s of silence before the speech; scenes 2 and 5 began mid-sound at 10 to 40 % amplitude at sample 0) and end abruptly, so a hard start plays like a cut. The builder now:

1. **Pads every take** into `voice/_padded/<name>.wav`: 0.30 s of silence, a 20 ms fade-in, the voice, a 50 ms fade-out, 0.40 s of silence (Blender's `aud`: `Sound.silence(rate).limit(...)`, `.join(...)`, `.fadein/.fadeout`, `.write(...)`; the rate must be an `int`, `specs[0]` is a float).
2. **Places it complete:** the strip shows the speech plus ≥ 0.12 s before and ≥ 0.30 s after (`LEAD_KEEP`, `TAIL_KEEP`); the strip is created `ini` seconds earlier because `frame_offset_start` also advances the visible start, and an `assert` checks the start frame.
3. **Checks it** (`CHECK=1`): per voice it prints the file range played, the speech range, and whether the lead-in, tail and padded silence are as expected and nothing overlaps (`CHECK RESULT all voices complete`). **Blender's background mixdown is silent** (`bpy.ops.sound.mixdown` writes zeros without a display), so the check reads the strips and the padded files instead of the mix.
4. Still true: **no sentence is ever cut**; not hearing the audio is declared at P7.

## Plates, backgrounds, callouts and cards

- **Types:** `full` (cover with a focus point and a slow push), `contain` (fitted with rounded corners and a soft shadow on a gradient), `cutout` (transparent PNG over a gradient with a soft shadow). The gradient is generated in the script from two colours and an angle (`numpy`).
- **Layers are composed in `numpy` inside Blender** (`bpy.data.images` + `foreach_get/foreach_set`; `Image.scale` to resize), saved as PNG in `render/_fx/` and used as `ALPHA_OVER` strips. The system Python has **no numpy**; Blender's has.
- **Channels:** 1 paper · 2 gradient A · 3 plate A · 4 gradient B · 5 plate B (alternating so cross-fades never overlap on one channel) · 6 callout overlays · 7 card · 8 to 10 card texts · 11 to 13 callout texts · 14 vignette · 15 grain.
- **Callouts:** a dot with a ring, a leader line and a paper label (copper bar); the label is moved above the card if it would overlap it. They enter 1 s after the plate, 0.6 s apart.
- **Cards:** context, number and note kinds, 894 × 280 px at 28.5 % from the bottom.

## Legacy per-video scripts

Kept in `System/scripts/` only to re-render earlier videos (they read the old Spanish folder names and hard-coded timings):

| Script | Video |
| --- | --- |
| `build_38s.py` | Magnets and geopolitics, 38 s |
| `build_brasil.py` | Brazil and embassies (the base of the 9:16 Shorts) |
| `build_helio.py` | Helium and power (the state-change and sound design in [[Transitions and effects]]) |
| `build_potencias.py`, `build_queque.py` | Bike stems, Lemon cake |
| `build_chips.py`, `build_helium2.py`, `build_twisted_carbon.py` | Chips, Helium (English), Twisted carbon: plasticine plates, one 3-line card per plate |

**New videos use `build_video.py`.** Do not copy a legacy script.

## Notes on the Blender 5.2 API (learned while writing the scripts)

- **Video output:** set `image_settings.media_type = "VIDEO"` before choosing `file_format = "FFMPEG"`.
- **Strip collections:** `sequence_editor.strips` (formerly `sequences`); `new_image`, `new_sound` and `new_effect`. **`new_effect`:** the duration goes as a named argument, `length=...`.
- **Trims:** `frame_offset_start` and `frame_final_end` work, with a warning that they will be removed in Blender 6.0.
- **Linear keyframe interpolation:** `bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"` before inserting keyframes; without it zooms and fades speed up and slow down.
- **Layer blending:** `strip.blend_type = "ALPHA_OVER"` for PNG layers with transparency, `"MULTIPLY"` and `"OVERLAY"` with `blend_alpha` for the vignette and the grain.
- **`view_transform = "Standard"`:** Blender 5's default (AgX) mutes colours. Always set it. The `COLOR` effect takes its value as is.
- **Text:** `new_effect(..., "TEXT", ...)` with `font`, `font_size`, normalised `location` and `anchor_x/anchor_y`; the default typeface is monospaced; load Noto Sans Display Bold and Noto Sans Regular ([[On-screen text style]]).
- **Absolute paths:** a `.blend` saved in `render/` resolves relative image paths from its own folder; images then show as magenta. Use absolute paths.
- **Image scale:** `max(video_width / image_width, video_height / image_height)` fills the frame without bars; horizontal photos in a vertical frame use `contain` instead of cropping.
- **MP3 audio:** Blender decodes it, but the padded WAVs avoid the decoder's start-up delay and give exact onsets.

## Rules

- **It does not run without a gate:** editing starts from media approved at P6 ([[Production process]]).
- **Review before delivering:** render key frames and check duration; state what cannot be verified (how it sounds, the pace).
- **Do not render in the same command you test with:** assemble first (`SOLO_PROYECTO=1 CHECK=1`), read the timings and the voice check, then render in the background.
- **Hanging jobs:** never `pkill -f` a pattern that appears in your own command; match processes with `ps` and `awk`.

## Known limitations

- No animation of the drawings beyond a push and cross-fades; callouts appear, they do not draw themselves.
- Plate changes are not synced to individual words, only to the scene.
- The full video is neither heard nor watched before delivering; gate P7 exists for that.
