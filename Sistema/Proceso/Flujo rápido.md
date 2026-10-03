---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v2 · reordenado; las lecciones de cada video pasaron a las guías
tags: [investigación, youtube, proceso, costos, replicate]
---

# Flujo rápido

← [[Canal YouTube]] · [[Guías para nuevos guiones]] · [[Proceso de producción]] · [[Modelos del canal]]

**Para producir un video se leen dos notas: esta (cómo y con qué se produce) y [[Guías para nuevos guiones]] (qué reglas de calidad se aplican).** Lo demás es referencia.

## 1. Ahorro de tokens

- **Sonnet 5.5, sin subagentes**: el trabajo es secuencial y corto.
- **Lectura mínima al empezar:** estas dos notas + `<Tema> - Estado` + el guion vigente.
- **Solo si hace falta:** [[Guía de narración]] (al escribir), [[Estilo visual - miniaturas de plastilina]], [[Modelos del canal]] (si cambia el modelo), [[Montaje en Blender]] y [[Transiciones y efectos]] (en el montaje).
- **Una sola nota por video** (`<Tema> - Estado`), con etapas, presupuesto, prompts y registro de predictions. Sin notas de prompts aparte.
- **Los resultados de Replicate no se leen enteros:** se guarda la URL o el archivo y una línea de bitácora.
- **Las imágenes se miran en lotes**, al terminar la categoría.

## 2. Flujo en 5 paquetes

Las etapas son las de [[Proceso de producción]]; se revisan juntas:

| Paquete | Incluye | Puerta |
| --- | --- | --- |
| **A · Texto** | Idea, investigación con fuentes, guion y dirección (solo texto) | **P1–P3 + P4a**, una revisión |
| **B · Presupuesto** | Prompts de imagen y voz, y el costo en dólares (§5) | **P4**: aquí se autoriza gastar |
| **C · Prueba** | Voz de la escena 1 y una imagen (≈ $0,10 máx.) | **P5** |
| **D · Generación** | **Por categoría, en orden: voz → imagen** (sonido solo si el guion lo exige) | P6, una aprobación por categoría |
| **E · Montaje y publicación** | Render, descripción | **P7–P8** |

**Regla madre: no se llama a Replicate antes de P4.** Si el usuario delega («sigue tú hasta el render»), se anota en el Estado y se sigue sin parar dentro del tope.

## 3. Modelos por tarea

| Tarea | Modelo | Precio | Notas |
| --- | --- | --- | --- |
| **Imagen · por defecto (decisión del usuario, 3-oct-2026)** | `black-forest-labs/flux-kontext-pro` **con una referencia real** (foto del objeto) | ≈ $0,04 (**de memoria; confirmar en el panel**) | 4 a 7 s. Es un modelo de **edición**: una sola `input_image`. Config y límites en §7 |
| Imagen · alternativa | `wan-video/wan-2.7-image` | ≈ $0,02 (tercero; **sin confirmar**) | Entiende prompts largos y 3 referencias, pero dibuja objetos reales de memoria. Se usa si Kontext no resuelve la imagen |
| Imagen · alternativa | `openai/gpt-image-1.5` (calidad media, **solo 2:3**) | ≈ $0,05 | Si Kontext no resuelve la imagen; se extiende a 9:16 en el montaje |
| Imagen · edición difícil | `google/nano-banana-2` (1K, 9:16, `image_search` para objetos reales) | ≈ $0,067 | Puede escribir palabras |
| Imagen · borrador | `black-forest-labs/flux-2-klein-4b` | ≈ $0,015 | Falla en conteos y copia referencias |
| Imagen · escena difícil | `bytedance/seedream-5-lite` | $0,035 | Solo esa escena |
| **Voz** | `elevenlabs/v3` | ≈ $0,10 por 1.000 caracteres | Elegida por el usuario. Parámetros en [[Guías para nuevos guiones]] §3 |
| Voz · alternativa barata | `qwen/qwen3-tts` | ≈ $0,02 por 1.000 | Sin `speed`, ≈ 122 palabras por minuto |
| Sonido | `sepal/audiogen` | ≈ $0,011 | **Solo si el guion lo pide**; 16 kHz. `mmaudio` falla en solo texto |
| Animación y música | Ninguna | $0 | El montaje funde láminas en Blender |

**No se usan:** `qwen-image-edit-plus` para generar (copia las referencias), `flux-2-pro` (caro), `stable-audio-2.5` ($0,20 por archivo).

**Cómo se llama a Replicate sin gastar de más:** el esquema se lee con `GET /v1/models/<owner>/<name>` (gratis); modelos comunitarios van por `POST /v1/predictions` con `version`; con `urllib` hace falta un `User-Agent` (si no, 403). Se reutiliza `Sistema/scripts/replicate_helper.py`. Un comando con más de ≈ 15 llamadas supera el límite de tiempo: lotes de ≤ 10 y se comprueba qué archivos faltan.

## 4. Reglas para no generar de más

1. **Solo imágenes que aparecen en el corte**; cada fila del presupuesto cita el segundo del guion donde se usa.
2. **1 imagen por toma**; 2 solo si el plano pide un antes y un después.
3. **Tope por video = imágenes base × 1,2.** Pasarlo exige aprobación.
4. **Prueba mínima (P5):** una escena, una imagen, un modelo. Comparar modelos solo si el usuario lo pide.
5. **Una referencia real por toma** (Kontext admite una sola `input_image`).
6. **Prompts en positivo**; se corrige el prompt **antes** de reintentar y se reintenta **una vez**.
7. **Serie, no paralelo** (429).
8. **Los descartes van a `_descartes/`** y no se regeneran «para comparar».
9. **Sin miniatura en Shorts**; en videos largos se reutiliza una imagen del video.
10. **Una investigación de modelos no cuenta como costo del video** (ver [[Guías para nuevos guiones]] §5).

## 5. Presupuesto de P4 (formato fijo, en dólares)

| Categoría | Modelo | Cantidad | Precio unitario | Subtotal | Tope (×1,2) |
| --- | --- | --- | --- | --- | --- |
| Voz | `elevenlabs/v3` | tomas (por escena) | ≈ $0,10 por 1.000 caracteres | | |
| Imagen | `flux-kontext-pro` | láminas (cada una con su segundo) | ≈ $0,04 (sin confirmar) | | |
| Sonido | `audiogen` | solo si el guion lo pide | ≈ $0,011 | | |
| Prueba P5 | uno de cada | | | (dentro del total) | |
| **Total y tope** | | | | | |

**Referencias de costo real:** Helio ≈ $2 (32 predictions); Brasil ≈ $0,46 (7 imágenes); Queque ≈ $1,57 (20 láminas con `gpt-image-1.5`). Con `flux-kontext-pro`, 20 láminas ≈ $0,80 más voz ≈ $0,11 (estimado).

**Registro por video**, una línea por prediction y sin copiar el input: `escena · categoría · modelo · seed · ✅ usada / ❌ descartada · URL`. Al cerrar cada categoría, cuántas predictions frente al tope; si pasa de ×1,2, se anota por qué.

## 6. Formato Shorts (0 a 2 min): vertical 9:16

- **Imagen:** `aspect_ratio` 9:16 (o `match_input_image` con Kontext, ver §7); un solo sujeto, composición alta. Zona segura y reglas de imagen: [[Estilo visual - miniaturas de plastilina]] y [[Guías para nuevos guiones]] §2.
- **Render en Blender:** `W, H = 1080, 1920`, 24 o 30 fps, H.264 y AAC; escala `max(...)` para llenar el cuadro.
- **Duración:** ≈ 150 palabras para 60 s; más largo está bien si hace falta.
- **Nombre del render:** `<video>-<duración>-9x16-r<n>.mp4` ([[Convención de media]]).
- Los videos de más de 2 min siguen en 16:9.

## 7. Imagen por defecto: `flux-kontext-pro` + referencia real (3-oct-2026)

> **Decisión del usuario:** *«From now on we're using flux-kontext pro plus real references.»* Evidencia y pruebas: [[Investigación - Flux Kontext Pro con referencias (potencia)]].

- **Modelo:** `black-forest-labs/flux-kontext-pro`. Entradas: `prompt`, **`input_image` (una sola)**, `aspect_ratio` (acepta `match_input_image` y 9:16), `output_format`, `seed`. ≈ 4 a 7 s por imagen.
- **Referencia real:** una **foto del objeto** (Wikimedia Commons u otra fuente con licencia, **recortada al objeto**, sin fondo que distraiga). Se anota la licencia y la atribución de cada foto; con CC BY-SA hay que revisarla antes de publicar.
- **Una sola imagen:** el modelo no admite varias. **Un collage de dos referencias no funciona** (la foto perdió fuerza y salieron solo anillos).
- **Prompt como instrucción de edición:** *«Redraw this exact <objeto>… Keep the exact shape and proportions… Replace the background… Remove all lettering and logos…»* + línea de estilo. Se indican las partes que deben conservarse.
- **Orientación:** el modelo respeta la composición de la entrada; **una foto horizontal con un lienzo 9:16 se gira y se deforma**. Se prueba con `match_input_image` o una entrada ya vertical.
- **Estilo:** miniatura de plastilina, el único que Kontext reconoció como estilo («vectorial plano» y «serigrafía» salieron como renders). Definición y plantilla de prompt: [[Estilo visual - miniaturas de plastilina]].
- **Costo y reintentos:** igual que §4 (un reintento por imagen, serie, tope ×1,2). Una imagen de prueba antes de un lote.
- **Respaldo:** `wan-2.7-image` (llamada anterior: `prompt` con contexto de escena, `images` = hasta 3 fotos reales de referencia, `size` `1152*2048`).
