---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · probado con dos videos
tags: [investigación, youtube, montaje, blender]
---

# Montaje en Blender

← [[YouTube Channel]] · [[Production process]] · [[Transitions and effects]] · [[Media convention]]

Etapa 7 del [[Production process]]: el corte se arma en el secuenciador de video de Blender 5.2 (instalado en esta máquina) desde un script, sin abrir la interfaz y sin necesitar ffmpeg. El **lenguaje de transiciones y efectos** está en [[Transitions and effects]].

## Cómo se ejecuta

Desde la carpeta del video en `Media/`:

```
blender -b --factory-startup --python render/build_<video>.py
```

El script coloca las tomas de voz (recortando sus silencios), los sonidos y las imágenes con sus transiciones y efectos, guarda el proyecto `.blend` y renderiza el `.mp4` (1920×1080; **1080×1920 en vertical para Shorts**, ver [[Fast workflow]], 24 fps, H.264 y AAC). Con `SOLO_PROYECTO=1` en el entorno solo arma y guarda el proyecto, sin renderizar: sirve para revisar los tiempos en segundos.

## Scripts

Copias versionadas en `Sistema/scripts/` (el original vive junto a los medios, en `render/`, que no se sube a GitHub):

| Script | Video | Qué incluye |
| --- | --- | --- |
| `build_38s.py` | Imanes y geopolítica, versión de 38 s | Voz recortada, imágenes con fundido inicial → final, corte a negro. Sin efectos |
| `build_brasil.py` | Brasil y embajadas, Short vertical de 59 s | **Base para Shorts 9:16**: 1080×1920, una imagen por escena con recorte del dibujo secundario, texto en pantalla, silencio de énfasis y sonido puntual |
| `build_helio.py` | Helio y poder, 70 s | Todo lo de [[Transitions and effects]]: cambios de estado sincronizados con la voz, pasar la hoja, empuje de cámara, viñeta, grano y sonidos de ambiente con corte seco. **Es la base para los videos nuevos** |

## Notas de la API de Blender 5.2 (aprendidas al escribir los scripts)

- **Salida de video:** hay que fijar `image_settings.media_type = "VIDEO"` antes de elegir `file_format = "FFMPEG"`.
- **Colecciones de tiras:** `sequence_editor.strips` (antes `sequences`); `new_image`, `new_sound` y `new_effect`.
- **`new_effect`:** la duración va como argumento con nombre, `length=...`.
- **Recortes:** `frame_offset_start` y `frame_final_end` funcionan, con un aviso de que se retirarán en Blender 6.0.
- **Interpolación lineal de los keyframes:** `bpy.context.preferences.edit.keyframe_new_interpolation_type = "LINEAR"` antes de insertarlos; sin esto el zoom y los fundidos aceleran y frenan.
- **Mezcla de capas:** `strip.blend_type = "MULTIPLY"` u `"OVERLAY"` con `blend_alpha` da la viñeta y el grano.
- **Imágenes de efecto:** se generan con `numpy` (incluido en el Python de Blender) y se guardan con `bpy.data.images`.
- **Audio MP3:** Blender lo decodifica sin problema; los modelos de sonido de Replicate entregan MP3 aunque se pida WAV.
- **Escala de imágenes:** una imagen que se escala a `max(ancho_video / ancho_imagen, alto_video / alto_imagen)` llena el cuadro sin franjas.

## Notas del montaje vertical (Shorts)

- **`view_transform = "Standard"`:** el valor por defecto de Blender 5 (AgX) apaga el color del papel y de los dibujos. Siempre se fija.
- **Recorte de tiras:** en Blender 5.2 no existe `use_crop`; `strip.crop.min_y` recorta por abajo y `crop.max_y` por arriba (en píxeles de la imagen). El recorte no recoloca la imagen: queda donde estaba.
- **Papel de fondo:** el efecto `COLOR` toma el valor tal cual (sin pasar de lineal a sRGB). Se mide el papel de los dibujos (mediana de una banda superior) y se usa ese valor para que no se vea el borde del recorte.
- **Texto:** `new_effect(..., "TEXT", ...)` con `font`, `font_size`, `location` normalizada y `anchor_x/anchor_y`. La tipografía por defecto es monoespaciada; se carga `DejaVuSans-Bold.ttf`.
- **Viñeta:** en cuadro vertical se suaviza (opacidad 0,22), o oscurece arriba y abajo.
- **Voz recortada:** `frame_offset_start` también adelanta el inicio visible. Para que lo audible empiece en `abs`, la tira se crea `ini` segundos antes y se comprueba con una `assert`; si no, cada frase pierde su final (error de la r1).
- **Láminas anchas en cuadro vertical:** acercamientos mayores a 1,0 cortan los bordes; se usan 0,96 a 1,0 y el empuje del 6 % es el que acerca.
- **Duración:** se mide con `SOLO_PROYECTO=1` antes de renderizar; el render de 59 s tardó ≈ 1 min 10 s.

## Reglas

- **No se corre sin puerta:** el montaje parte de medios ya aprobados en P6 ([[Production process]]).
- **Se revisa antes de entregar:** se renderizan fotogramas clave y se comprueba duración y presencia de audio. Lo que no se puede verificar (cómo suena, el ritmo) se dice.
- **No se renderiza en el mismo comando que se prueba:** el render completo de un video de ≈ 70 s tarda varios minutos; se arma primero el proyecto con `SOLO_PROYECTO=1`, se revisan los tiempos y luego se renderiza.

## Limitaciones conocidas

- El cambio de estado es un fundido entre dos láminas, no una animación del dibujo.
- No se oye ni se ve el video completo antes de entregarlo; la puerta P7 existe para eso.
- No hay texto en pantalla (cifras, títulos); se haría con tiras de texto del propio secuenciador.
