---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · layout updated to the real structure; English since 3 Oct 2026
tags: [research, youtube, media, organization]
---

# Media convention

← [[YouTube Channel]] · [[Production process]] · [[Prompt - per-scene generation guide]]

**Nothing is generated in `Media/` before gate P4** ([[Production process]]).

Generated media (images, voice, audio, video) lives in `Media/` at the vault root. **It is in `.gitignore`: it only exists on this machine and is not pushed to GitHub.** What is versioned are the prompts and the scripts; if the folder is lost, it is regenerated from them.

## Structure

```
Media/
├── _canal/                          shared by every video (legacy Spanish names kept)
│   ├── estilo/                      old visual definitions (retired styles)
│   ├── investigacion/               model tests (not counted as video cost)
│   └── musica-y-sfx/                reusable sounds
└── <Video> - <N seconds>/           one folder per version of the video (English name)
    ├── voice/                       narration takes (mp3) and voice/_padded/ (wav, made by the builder)
    ├── plates/                      generated images and cutouts (png) + _refs/ (references) + _descartes/ (discards)
    ├── stock/                       free stock photos + _credits.jsonl (title, author, license, page)
    ├── plan.json                    the video's plan for System/scripts/build_video.py
    └── render/                      final video, the .blend and render/_fx/ (generated layers)
```

- **New videos (from 4 Oct 2026) use English inner names** (`voice`, `plates`, `stock`, `render`) because `build_video.py` reads them. Sound, if the script asks for it, goes in `sound/`.
- **Older videos keep their Spanish inner names** (`voz`, `ilustraciones`, `render`, folders such as `Imanes - 38 segundos`, `Brasil y embajadas - 60 segundos`, `Chips - 85 segundos`) because their per-video scripts and `.blend` projects refer to them. Changing them breaks those projects.
- `<N seconds>` is the **measured** duration of the render, set after the voice exists (the folder can be called `<Video> (wip)` until then).

## Unique names across the whole vault

**Every media file carries its video's prefix**, for example `helio-e1-final-v1.png`. Obsidian resolves `![[name]]` by **file name, without the path**: if two videos have `e1-final-v1.png`, a note shows the other video's image. It happened with the helium video and the magnets video's images. Before creating a file, check that its name does not already exist in `Media/`.

`_canal/` always lives **inside `Media/`** (never at the vault root): that is the only way Git ignores it.

## File names

The name says where it goes, without opening the file:

| Type | Pattern | Example |
| --- | --- | --- |
| Generated plate or cutout | `<video>-p<nn>-v<n>.png` | `tc-p03-v1.png` |
| Stock photo | `<video>-s<nn>-<slug>.jpg` (credit in `_credits.jsonl`) | `tc-s02-cryostat.jpg` |
| Reference photo | `<video>-ref-<slug>.jpg`, in `plates/_refs/` | `tc-ref-graphite.jpg` |
| Voice | `<video>-e<scene>-voice-v<n>.mp3` | `tc-e1-voice-v1.mp3` |
| Audio | `<video>-e<scene>-<sound>-v<n>.mp3` (models deliver MP3) | `helio-e4-siseo-gas-v1.mp3` |
| Render | `<video>-<duration>s-9x16-r<n>.mp4` (the builder names it) | `tc-85s-9x16-r1.mp4` |

- `v<n>` is the attempt. The approved one is kept and the discarded ones go to a `_descartes/` subfolder inside the same folder, which is emptied on publishing. Older videos keep their old names (`chips-i01-v1.png`, `helio-e1-final-v1.png`).
- The scene number is the one in that version's script.
