---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v1 · diseñado para Shorts verticales 9:16
tags: [investigación, youtube, estilo, tipografía, texto]
---

# Estilo de texto en pantalla

← [[Estilo visual - miniaturas de plastilina]] · [[Montaje en Blender]] · [[Canal YouTube]]

> **Encargo (3-oct-2026):** *«Design a style for text, it must be sober, professional and modern.»*

**Principio:** el texto es una **etiqueta sobria**, no un subtítulo ni un titular. Habla poco, se lee de un vistazo y no compite con la imagen. Es una tarjeta de papel, tinta y el mismo acento cobre-naranja de las ilustraciones ([[Estilo visual - miniaturas de plastilina]]).

## Pieza: tarjeta de etiqueta (*lower third*)

Una tarjeta por escena, alineada a la izquierda, con **dos líneas**: una etiqueta pequeña y un título.

| Elemento | Especificación |
| --- | --- |
| **Etiqueta** (línea 1) | Mayúsculas con espaciado ancho (espacios finos U+200A entre letras), **Noto Sans Regular, 34 px**, color cobre `#C76B38`. Ejemplos: `P A S O  1`, `6  P A S O S` |
| **Título** (línea 2) | **Noto Sans Display Bold, 58 px**, color tinta `#1C1A17`, **frase en minúscula** (solo la primera letra en mayúscula), una sola línea, **máximo 26 caracteres** |
| **Tarjeta** | Papel cálido `#F9F6EE` al 94 % de opacidad, esquinas de 16 px, borde de 1 px en grafito al 25 %, **barra cobre de 8 px en el borde izquierdo**. Ancho 894 px (margen izquierdo 56 px y 130 px a la derecha, donde Shorts pone sus botones), alto ≈ 210 px |
| **Posición** | Entre el 22 % y el 33 % de la altura desde abajo: **sobre la zona de subtítulos y botones de Shorts**; el 6 % superior queda libre |
| **Aparece / sale** | Fundido de 0,25 s con un ascenso de 24 px; sale con fundido de 0,2 s. Entra 0,5 s después de que empieza la escena y sale 0,15 s antes de que termine |
| **Una a la vez** | Nunca dos tarjetas ni texto sobre texto |

## Reglas de redacción

1. **Máximo cuatro palabras de contenido**; si el título no cabe en una línea, se acorta, no se baja el tamaño.
2. **Sin signos de exclamación, sin emojis, sin mayúsculas sostenidas** (solo la etiqueta va en mayúsculas).
3. **Cifras con su unidad y un espacio fino**: `180 °C`, `40 min`.
4. **El texto nombra lo que el dibujo no puede**: el paso, la cifra o la condición. No repite la narración.
5. **Idioma del video**, con tildes.

## Por qué esta tipografía

- **Noto Sans Display Bold:** sans-serif neutra, de trazo uniforme y legible en pantallas pequeñas; es sobria y no tiene personalidad propia que compita con los dibujos. Está instalada en esta máquina (`/usr/share/fonts/truetype/noto/`), se publica con licencia libre (SIL OFL) y Blender la lee sin conversión.
- **Etiqueta espaciada en cobre:** ordena sin gritar y reutiliza el acento del canal.
- **Tarjeta de papel con barra de acento:** da contraste sin una caja negra de subtítulo.
- **Una sola jerarquía:** etiqueta pequeña y título grande bastan; no se usan sombras ni contornos.

## Cómo se implementa (Blender 5.2)

- Tarjeta: imagen RGBA del tamaño del cuadro, generada con `numpy` (rectángulo redondeado y barra), como tira de imagen con `blend_alpha` y desplazamiento en `transform.offset_y`.
- Texto: dos tiras `TEXT` con `font`, `font_size`, `location` normalizada, `anchor_x = "LEFT"` y `align_x = "LEFT"`; el espaciado de la etiqueta se logra con espacios finos.
- Script: `Sistema/scripts/build_queque.py` (sección *tarjeta de etiqueta*).

## Copias por escena (Queque, 3-oct-2026)

| Escena | Etiqueta | Título |
| --- | --- | --- |
| 1 | 6 pasos | Queque de limón |
| 2 | Paso 1 | Temperatura ambiente |
| 3 | Paso 2 | Batir hasta dejar pálido |
| 4 | Paso 3 | Los huevos, de a uno |
| 5 | Paso 4 | Mezclar lo justo |
| 6 | Paso 5 | Horno a 180 °C |
| 7 | Paso 6 | El palillo sale limpio |
| 8 | (sin tarjeta) | |

## Pendiente

- [ ] Probar el estilo en un video no de cocina (por ejemplo, cifras de un tema político): ¿una tarjeta de dos líneas sirve para un dato y su fuente?
- [ ] Definir la versión para 16:9.
