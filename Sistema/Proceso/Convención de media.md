---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: borrador
tags: [investigación, youtube, media, organización]
---

# Convención de media

← [[Canal YouTube]] · [[Proceso de producción]] · [[Prompt - guía de generación por escena]]

**Nada se genera en `Media/` antes de la puerta P4** ([[Proceso de producción]]).

La media generada (imágenes, voz, audio, video) vive en `Media/` en la raíz del vault. **Está en `.gitignore`: solo existe en esta máquina y no sube a GitHub.** Lo que sí se versiona son los prompts y los guiones; si se pierde la carpeta, se regenera desde ellos.

## Estructura

```
Media/
└── Canal YouTube/
    ├── _canal/                      lo compartido por todos los videos
    │   ├── estilo/                  definición visual del canal
    │   ├── referencias/             hojas de IMÁN, MANO y paleta de acento
    │   └── musica-y-sfx/            sonidos reutilizables
    └── Imanes - <versión>/          una carpeta por versión del episodio
        ├── voz/                     tomas de narración
        ├── audio/                   sonidos y ambientes
        ├── ilustraciones/           fotogramas por escena
        │   └── _referencias/        las referencias usadas en esta versión
        ├── miniatura/
        └── render/                  video final y exportaciones
```

Versiones creadas: `Imanes - 38 segundos`, `Imanes - 100 segundos`, `Imanes - versión larga`.

## Nombres únicos en todo el vault

**Cada archivo de medios lleva el prefijo de su video**, por ejemplo `helio-e1-final-v1.png`. Obsidian resuelve `![[nombre]]` por el **nombre de archivo, sin la ruta**: si dos videos tienen `e1-final-v1.png`, una nota muestra la imagen del otro video. Pasó con el video de helio y las imágenes del de los imanes. Antes de crear un archivo, se comprueba que su nombre no exista ya en `Media/`.

`_canal/` vive **siempre dentro de `Media/`** (nunca en la raíz del vault): solo así Git la ignora.

## Nombres de archivo

El nombre dice dónde va, sin abrir el archivo:

| Tipo | Patrón | Ejemplo |
| --- | --- | --- |
| Ilustración | `<video>-e<escena>[toma]-<inicial\|final>-v<n>.png` | `helio-e3a-inicial-v2.png` |
| Voz | `<video>-e<escena>-voz-<modelo>-v<n>.wav` | `helio-e1-voz-qwen-design-v1.wav` |
| Audio | `<video>-e<escena>-<sonido>-v<n>.mp3` (los modelos entregan MP3) | `helio-e4-siseo-gas-v1.mp3` |
| Miniatura | `<video>-miniatura-v<n>.png` | `helio-miniatura-v2.png` |
| Render | `<video>-<duración>-r<n>.mp4` | `helio-70s-r1.mp4` |

- `v<n>` es el intento. Se conserva el aprobado y los descartados van a una subcarpeta `_descartes/` dentro de la misma carpeta, que se vacía al publicar.
- El número de escena es el del guion de esa versión; la escena 1 y la 4a de la versión de 38 s comparten encuadre.
