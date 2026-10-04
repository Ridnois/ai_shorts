---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v6 · brand layer removed, captions 88 px, 8 % alternating push, LONG PLATE warning (Superconductors feedback, 4 Oct 2026); v5 captions and guards; v4 one generic builder driven by plan.json
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

Full schema and plate types: [[Illustration pipeline]] §6. Top level: `prefix`, `size`, `fps`, `gaps` (silence between scenes), `start`, `tail`, `voices` (paths relative to the video folder), `texts` (the exact narration of each scene, one string per voice, for captions), `scenes[].plates[]`. Each plate: `type` (`full`, `contain`, `cutout`), `file`, placement (`focus`, `pos`, `size`, `width`), gradient (`bg`, `bg_angle`), `callouts[]` and a `card` (context list, or `{"kind": "number" | "note", …}`, see [[On-screen text style]]).

## Voices: complete, padded and checked

Feedback (Twisted carbon, 4 Oct 2026): *"small voice cut on the start of the video, make sure voices clips are complete and well put into the blender video sequencer."* What the data showed: the TTS files often **start abruptly** (scene 1 had 0.06 s of silence before the speech; scenes 2 and 5 began mid-sound at 10 to 40 % amplitude at sample 0) and end abruptly, so a hard start plays like a cut. The builder now:

1. **Pads every take** into `voice/_padded/<name>.wav`: 0.30 s of silence, a 20 ms fade-in, the voice, a 50 ms fade-out, 0.40 s of silence (Blender's `aud`: `Sound.silence(rate).limit(...)`, `.join(...)`, `.fadein/.fadeout`, `.write(...)`; the rate must be an `int`, `specs[0]` is a float).
2. **Places it complete:** the strip shows the speech plus ≥ 0.12 s before and ≥ 0.30 s after (`LEAD_KEEP`, `TAIL_KEEP`); the strip is created `ini` seconds earlier because `frame_offset_start` also advances the visible start, and an `assert` checks the start frame.
3. **Checks it** (`CHECK=1`): per voice it prints the file range played, the speech range, and whether the lead-in, tail and padded silence are as expected and nothing overlaps (`CHECK RESULT all voices complete`). **Blender's background mixdown is silent** (`bpy.ops.sound.mixdown` writes zeros without a display), so the check reads the strips and the padded files instead of the mix.
4. Still true: **no sentence is ever cut**; not hearing the audio is declared at P7.

## Captions (word by word)

Feedback (Magnetar, 4 Oct 2026): *"add transcriptions to the video, word by word, so users can follow the narrative with the audio off."* Every video has them:

1. `plan.json` gets `texts`: one narration string per voice take, exactly as voiced (the builder asserts the counts match).
2. `python3 System/scripts/word_timings.py Media/<Video>` asks `vaibhavs10/incredibly-fast-whisper` (`timestamp: word`) for the word times of each take and writes `voice/<take>.words.json` (≈ $0.01 per take, 429s are retried by the helper). If a file is missing, the builder **estimates** the times from the characters and punctuation inside the measured speech span.
3. `build_video.py` maps the script's own words onto those times (if whisper heard a different number of words, the script words are spread over the heard span by characters) and adds one `TEXT` strip per word on **channel 16**: Noto Sans Display Bold 104 px, capitals, white, outline and shadow, copper when the word has a digit, centred at `CAP_Y` = 83.5 % from the top. A word stays until the next starts, up to 0.55 s across a pause.
4. `keywords` in `plan.json` (≤ 6 key terms) are shown in copper like figures; the builder also writes `render/<prefix>.srt` (5 words per cue) to upload as a caption track.
5. It prints `CAPTIONS n words, timed by whisper | estimated`. **Verify by stills** (a word is on screen where the voice speaks it is *not* verifiable by the agent).

## Sound design

- **No branding layer** (progress bar, mark, series tag): built and removed on the user's feedback of 4 Oct 2026 (*"unnecessary"*); the builder has no code for it.
- **Sound design** (`sound` in `plan.json`: `{"sfx": true, "bed": true, "sfx_gain": 0.7, "bed_gain": 1.0}`): `synth_sound()` builds two mono 48 kHz WAVs with numpy, `render/_fx/sound_sfx.wav` and `sound_bed.wav`, added as sound strips on channels 31 and 32 under the voice (channel 30). Events come from the build itself: an opening **thump** (58 Hz sweeping down, 0.55 s), a **whoosh** at each scene cut (low-passed then high-passed noise sweep, 0.42 s, ending on the cut), a quieter **tick** at each plate change inside a scene (0.22 s), a **ping** when a card arrives (880 and 1320 Hz, 0.7 s decay), a **click** when a callout arrives (2.6 kHz, 60 ms), and a **drone bed** (A minor: 110, 164.8, 220 and 329.6 Hz with slow swells, fading in over 1.2 s and out over 1.6 s). The build prints `SOUND sfx|bed: seconds, peak, rms`.
- **Levels (Superconductors r2):** voice ≈ −22 dBFS while speaking (peak ≈ 0.5), effects peak 0.15 after `sfx_gain` 0.7 (≈ −31 dBFS active), bed ≈ −37 dBFS. **The agent cannot hear it and Blender's background mixdown is silent**, so the mix is checked by numbers only; the user's ear at P7 decides, and `sfx_gain` and `bed_gain` are the dials. Synthesized sound has no license; any recording or music track follows [[Guidelines for new scripts]] §3.

## Guards

- **Long plates are reported:** the build prints `PLATES n | durations [...]` and `LONG PLATE (> 5 s, add a reference image)` with the plate numbers; fix them before rendering ([[Shorts quality bar]] §4).
- **Motion:** pushes are 8 % and alternate (in on odd plates, out on even ones); cross-fades within a scene are 0.2 s.

- **Bare backdrops are refused:** a plate whose file name contains `blank` stops the build ([[Illustration pipeline]] §1.7); `allow_bare: true` in the plan overrides it only if the user asks. Missing plate files also stop the build.
- **Callout labels are clamped above the caption zone**, and moved above the card as before.

## Plates, backgrounds, callouts and cards

- **Types:** `full` (cover with a focus point and a slow push), `contain` (fitted with rounded corners and a soft shadow on a gradient), `cutout` (transparent PNG over a gradient with a soft shadow). The gradient is generated in the script from two colours and an angle (`numpy`).
- **Layers are composed in `numpy` inside Blender** (`bpy.data.images` + `foreach_get/foreach_set`; `Image.scale` to resize), saved as PNG in `render/_fx/` and used as `ALPHA_OVER` strips. The system Python has **no numpy**; Blender's has.
- **Channels:** 1 paper · 2 gradient A · 3 plate A · 4 gradient B · 5 plate B (alternating so cross-fades never overlap on one channel) · 7 card · 8 to 10 card texts · 14 vignette · 15 grain · 16 captions · 20 to 22 callout overlays · 24 to 26 callout texts · 30 voices · 31 sound effects · 32 drone bed (**each callout on its own channel**: overlapping strips on one channel are bumped into the card's channels and ghosted the number card on the Superconductors diamond-anvil plate, which has three callouts). Words longer than ≈ 14 characters shrink to fit the frame ("NEAR-ROOM-TEMPERATURE" was cut at 104 px).
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
