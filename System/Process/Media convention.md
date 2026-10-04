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
├── _canal/                          shared by every video
│   ├── estilo/                      the channel's visual definition
│   ├── investigacion/               model tests (not counted as video cost)
│   └── musica-y-sfx/                reusable sounds
└── <Video> - <N seconds>/           one folder per version of the video
    ├── voz/                         narration takes
    ├── audio/                       sounds and ambiences
    ├── ilustraciones/               frames per scene
    │   ├── _referencias/            the references used in this version
    │   └── _descartes/              discarded attempts
    ├── miniatura/
    └── render/                      final video and exports
```

- **The inner folder names (`voz`, `ilustraciones`, `render`, `_canal`…) are kept in Spanish on purpose:** the build scripts in `System/scripts/` and the existing `.blend` projects refer to them. Changing them breaks the old projects.
- **Folders of videos 1 to 6 keep their original Spanish names** (`Imanes - 38 segundos`, `Brasil y embajadas - 60 segundos`, `Chips - 85 segundos`…) for the same reason. **New videos use English folder names: `<Video> - <N seconds>`.**

## Unique names across the whole vault

**Every media file carries its video's prefix**, for example `helio-e1-final-v1.png`. Obsidian resolves `![[name]]` by **file name, without the path**: if two videos have `e1-final-v1.png`, a note shows the other video's image. It happened with the helium video and the magnets video's images. Before creating a file, check that its name does not already exist in `Media/`.

`_canal/` always lives **inside `Media/`** (never at the vault root): that is the only way Git ignores it.

## File names

The name says where it goes, without opening the file:

| Type | Pattern | Example |
| --- | --- | --- |
| Illustration | `<video>-i<nn>-v<n>.png` (one per plate), or `<video>-e<scene>[take]-<initial\|final>-v<n>.png` | `chips-i01-v1.png` |
| Voice | `<video>-e<scene>-voz-v<n>.mp3` (the model is added if several are compared) | `chips-e1-voz-v1.mp3` |
| Audio | `<video>-e<scene>-<sound>-v<n>.mp3` (models deliver MP3) | `helio-e4-siseo-gas-v1.mp3` |
| Thumbnail | `<video>-miniatura-v<n>.png` | `helio-miniatura-v2.png` |
| Render | `<video>-<duration>-9x16-r<n>.mp4` | `chips-93s-9x16-r1.mp4` |

- `v<n>` is the attempt. The approved one is kept and the discarded ones go to a `_descartes/` subfolder inside the same folder, which is emptied on publishing.
- The scene number is the one in that version's script.
