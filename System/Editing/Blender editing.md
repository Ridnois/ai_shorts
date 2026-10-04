---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · tested on six videos; English-only since 3 Oct 2026
tags: [research, youtube, editing, blender]
---

# Blender editing

← [[YouTube Channel]] · [[Production process]] · [[Transitions and effects]] · [[Media convention]]

Stage 7 of the [[Production process]]: the cut is assembled in Blender 5.2's video sequencer (installed on this machine) from a script, without opening the interface and without needing ffmpeg. The **language of transitions and effects** is in [[Transitions and effects]].

## How it runs

Newer scripts (`build_queque.py`, `build_chips.py`) run from the vault root and find their media folder themselves:

```
SOLO_PROYECTO=1 blender -b --factory-startup --python System/scripts/build_chips.py   # assembles and measures
blender -b --factory-startup --python System/scripts/build_chips.py                  # assembles and renders
```

Older scripts lived next to the media, in `render/`, and ran from the video's folder in `Media/`.

The script places the voice takes (trimming their silences), the sounds and the images with their transitions and effects, saves the `.blend` project and renders the `.mp4` (1920×1080; **1080×1920 vertical for Shorts**, see [[Fast workflow]], 24 fps, H.264 and AAC). With `SOLO_PROYECTO=1` in the environment it only assembles and saves the project, without rendering: useful to check timings in seconds.

**To look at frames without ffmpeg:** open the saved `.blend` in background mode and render stills with `bpy.ops.render.render(write_still=True)` at `resolution_percentage = 25` (this machine has neither `ffmpeg` nor `ffprobe`).

## Scripts

Versioned copies in `System/scripts/`:

| Script | Video | What it includes |
| --- | --- | --- |
| `build_38s.py` | Magnets and geopolitics, 38 s version | Trimmed voice, images with initial → final fade, cut to black. No effects |
| `build_brasil.py` | Brazil and embassies, 59 s vertical Short | **Base for 9:16 Shorts**: 1080×1920, one image per scene with the secondary drawing cropped, on-screen text, emphasis silence and spot sound |
| `build_helio.py` | Helium and power, 70 s | Everything in [[Transitions and effects]]: state changes synced with the voice, page turn, camera push, vignette, grain and ambient sounds with a hard cut |
| `build_potencias.py` | Bike stems, 63 s Short | Vertical, 8 plates |
| `build_queque.py` | Lemon cake, 81 s Short | Mp3 voice analysed with `aud`, plates spread per scene with cross-fade, label card ([[On-screen text style]]), no sound effects |
| `build_chips.py` | Chips and lithography, ≈ 93 s Short | **Base for new videos**: derived from `build_queque.py`; 7 voices, 8 plates, per-image `OFF_X` / `ZOOM_IMG` overrides for horizontal photos, label cards on scenes 1 to 6 |

## Notes on the Blender 5.2 API (learned while writing the scripts)

- **Video output:** set `image_settings.media_type = "VIDEO"` before choosing `file_format = "FFMPEG"`.
- **Strip collections:** `sequence_editor.strips` (formerly `sequences`); `new_image`, `new_sound` and `new_effect`.
- **`new_effect`:** the duration goes as a named argument, `length=...`.
- **Trims:** `frame_offset_start` and `frame_final_end` work, with a warning that they will be removed in Blender 6.0.
- **Linear keyframe interpolation:** `bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"` before inserting them; without it zooms and fades speed up and slow down.
- **Layer blending:** `strip.blend_type = "MULTIPLY"` or `"OVERLAY"` with `blend_alpha` gives the vignette and the grain.
- **Effect images:** generated with `numpy` (included in Blender's Python) and saved with `bpy.data.images`.
- **MP3 audio:** Blender decodes it fine; Replicate's sound models deliver MP3 even if WAV is requested.
- **Image scale:** an image scaled to `max(video_width / image_width, video_height / image_height)` fills the frame without bars.

## Notes on vertical editing (Shorts)

- **`view_transform = "Standard"`:** Blender 5's default (AgX) mutes the colour of the paper and the drawings. Always set it.
- **Strip cropping:** Blender 5.2 has no `use_crop`; `strip.crop.min_y` crops from the bottom and `crop.max_y` from the top (in image pixels). Cropping does not reposition the image: it stays where it was.
- **Background paper:** the `COLOR` effect takes the value as is (no linear-to-sRGB conversion). Measure the drawings' paper (median of a top band) and use that value so the crop edge is not visible.
- **Text:** `new_effect(..., "TEXT", ...)` with `font`, `font_size`, normalised `location` and `anchor_x/anchor_y`. The default typeface is monospaced; load `NotoSansDisplay-Bold.ttf` ([[On-screen text style]]).
- **Vignette:** in vertical frames it is softened (opacity 0.22), or darkens top and bottom.
- **Trimmed voice:** `frame_offset_start` also advances the visible start. For the audible part to start at `abs`, the strip is created `ini` seconds earlier and checked with an `assert`; otherwise every sentence loses its ending (r1 error).
- **Wide plates in a vertical frame:** zooms above 1.0 cut the edges; use 0.96 to 1.0, and the 6 % push is what moves in.
- **Horizontal photos in a vertical frame:** scale to cover the height and shift with `transform.offset_x` so the subject stays inside the visible window (Chips plate 2: −300 px, no push).
- **Duration:** measure with `SOLO_PROYECTO=1` before rendering; the 59 s render took ≈ 1 min 10 s; the 93 s Chips render took about 4 minutes.

## Rules

- **It does not run without a gate:** editing starts from media already approved at P6 ([[Production process]]).
- **Review before delivering:** render key frames and check duration and presence of audio. What cannot be verified (how it sounds, the pace) is stated.
- **Do not render in the same command you test with:** a full render of a ≈ 70 s video takes several minutes; assemble the project first with `SOLO_PROYECTO=1`, check the timings, then render (in the background).

## Known limitations

- The state change is a fade between two plates, not an animation of the drawing.
- The full video is neither heard nor watched before delivering; gate P7 exists for that.
