---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · reescrita para flux-kontext-pro + foto real y voz elevenlabs
tags: [investigación, youtube, ilustración, audio, prompt, replicate]
---

# Prompt guía: generación por escena

← [[YouTube Channel]] · [[Fast workflow]] · [[Narration guide]] · [[Visual style - plasticine miniatures]] · [[Channel models]] · [[Media convention]]

> **No se ejecuta ningún prompt antes de P4** (prompts y presupuesto aprobados, en dólares). Modelos y precios: [[Fast workflow]] §3. Aquí solo cómo se escribe cada prompt a partir de la fila de escena del guion ([[Narration guide]] §4).

Todo prompt termina en una *prediction* de Replicate (`Sistema/scripts/replicate_helper.py`). Los parámetros cambian por modelo: se leen del esquema (`GET /v1/models/<owner>/<name>`, gratis), no de esta nota.

## 1. Imagen: `flux-kontext-pro` + foto real

Una imagen por escena. Entrada: **una foto real recortada** (`input_image`), con la orientación del resultado. El prompt es una **instrucción de edición**; el método completo y el estilo están en [[Visual style - plasticine miniatures]].

Cada prompt lleva, en este orden:

1. **Qué dice la narración en ese momento** (la frase del guion, en inglés): evita el prompt genérico que olvida el research.
2. **El objeto real y las partes que deben conservarse** (de la ficha del objeto).
3. **Qué estado muestra** la imagen (una imagen = un estado).
4. **El único acento cobre-naranja**: qué elemento.
5. **Composición**: vertical 9:16, sujeto en los dos tercios superiores.
6. **Bloque de estilo** de [[Visual style - plasticine miniatures]].

Reglas: prompts en positivo; sin texto, cifras ni rostros en la imagen; conteos y partes se verifican a ojo; un reintento con el prompt corregido, en serie. Una escena sin objeto con foto se rediseña alrededor de uno.

## 2. Voz: `elevenlabs/v3`

Una toma por escena, **con el texto exacto del guion** (nunca se corta una frase). Parámetros vigentes (voz, `speed`, `previous_text` / `next_text`) en [[Channel voice]]. Cifras y siglas se escriben como se dicen si el modelo las lee mal, y se anota el cambio.

## 3. Sonido y música

Ninguno por defecto. Solo si el guion lo exige, y con aprobación en P4 ([[Guidelines for new scripts]] §3). No hay animación: el montaje funde las imágenes ([[Blender editing]]).

## 4. Bitácora

Por cada prediction, una línea: `escena · categoría · modelo · seed · ✅ usada / ❌ descartada · https://replicate.com/p/<id>`. Los archivos se guardan según [[Media convention]]; los descartes, en `_descartes/`.
