---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · reevaluación de costos sin ejecutar modelos · precios leídos en las páginas de Replicate el 3-oct-2026
tags: [investigación, youtube, modelos, replicate, costos]
---

# Modelos del canal

> **Selección vigente: [[Fast workflow]]** (§3: `flux-kontext-pro` + foto real, `elevenlabs/v3`). Esta nota solo conserva las tablas de precios; donde difiera, manda [[Fast workflow]].

← [[YouTube Channel]] · [[Production process]] · [[Prompt - per-scene generation guide]] · [[Channel voice]] · [[Visual style - plasticine miniatures]]

Qué modelo se usa en cada caso, **con su precio real en Replicate**. Esta versión nace de una queja del usuario: *"it's getting expensive, too much test"*. Se reevaluó **sin ejecutar ningún modelo**: solo se leyeron las páginas de precio y los esquemas de entrada.

**Usado** = ya generó archivos de un video. **Candidato** = no se ha probado. Los modelos se fijan en la etapa 5 del [[Production process]]; nada se ejecuta antes de la puerta P4.

## Precios (Replicate, 3-oct-2026)

Leídos en la sección *Pricing* de cada modelo. Los precios por megapixel cuentan **entrada y salida**: una imagen de referencia también se cobra.

### Imagen

| Modelo                                     | Precio                                                                                                                    | Referencias de entrada                         | Notas                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `black-forest-labs/flux-kontext-pro` **(vigente)** | ≈ $0,04 por imagen (**de memoria, sin confirmar**) | una sola `input_image` | Edita una foto real; ver [[Fast workflow]] §7 |
| `black-forest-labs/flux-2-pro` (usado antes) | $0,015 por ejecución + $0,015 por megapixel de entrada + $0,015 por megapixel de salida → **≈ $0,045 con una referencia** | hasta 8                                        | **No entiende prompts negativos**: "no text" puede añadir texto (ver abajo)                         |
| `black-forest-labs/flux-2-flex`            | $0,06 por megapixel de entrada y de salida                                                                                | hasta 10                                       | Más caro; pensado para tipografía                                                                   |
| `black-forest-labs/flux-2-max`             | $0,04 por ejecución + $0,03 por megapixel de entrada y de salida                                                          | hasta 8                                        | El más caro de la familia                                                                           |
| `bytedance/seedream-5-lite`                | **$0,035 por imagen de salida**, plano                                                                                    | hasta 14                                       | Razonamiento integrado (espacio y física), lotes secuenciales; sin cargo aparte por las referencias |
| `ideogram-ai/ideogram-v3-turbo`            | **$0,03 por imagen** (balanceado $0,06; calidad $0,09)                                                                    | hasta 3 de estilo                              | Presets de estilo; fuerte en texto, que aquí no queremos                                            |
| `recraft-ai/recraft-v4.1`                  | $0,04 por imagen                                                                                                          | **ninguna** (solo prompt, tamaño y proporción) | Enfoque de diseño; no sirve para generar el final desde el inicial                                  |
| `google/imagen-4-ultra`                    | $0,06 por imagen                                                                                                          | —                                              | Solo texto a imagen                                                                                 |
| `google/nano-banana-2`                     | $0,067 (1K), $0,101 (2K), $0,151 (4K) por imagen                                                                          | hasta 14                                       | Edición conversacional y mezcla de imágenes; el más caro útil para editar                           |
| `openai/gpt-image-2`                       | sin precio legible en la página                                                                                           | —                                              | No evaluado                                                                                         |

### Voz

| Modelo                         | Precio                                                         | Costo de un guion de ≈ 1.000 caracteres         |
| ------------------------------ | -------------------------------------------------------------- | ----------------------------------------------- |
| `qwen/qwen3-tts` **(usado)**   | $0,02 por 1.000 caracteres                                     | **≈ $0,02**                                     |
| `resemble-ai/chatterbox-turbo` | $0,025 por 1.000 caracteres                                    | ≈ $0,025                                        |
| `minimax/speech-2.8-turbo`     | $0,06 por 1.000 tokens (≈ 1 token por carácter)                | ≈ $0,06                                         |
| `minimax/speech-2.8-hd`        | $0,10 por 1.000 tokens                                         | ≈ $0,10                                         |
| `elevenlabs/v3`                | $0,10 por 1.000 caracteres                                     | ≈ $0,10                                         |
| `google/gemini-3.1-flash-tts`  | $2 por millón de tokens de entrada + $0,04 por 1.000 de salida | ≈ $0,015 por una toma de 15 s; ≈ $0,07 por 70 s |

### Sonido

| Modelo                                      | Precio                 | Notas                                                                            |
| ------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| `stability-ai/stable-audio-2.5` **(usado)** | **$0,20 por archivo**  | El más caro por unidad de todo el canal                                          |
| `zsxkib/mmaudio`                            | ≈ $0,005 por ejecución | **≈ 38 veces más barato**; genera sonido desde texto o para un video. Sin probar |
| `sepal/audiogen`                            | ≈ $0,011 por ejecución | Texto a sonido. Sin probar                                                       |
| `declare-lab/tango`                         | ≈ $0,054 por ejecución | Texto a sonido. Sin probar                                                       |
| `tencent/hunyuanvideo-foley`                | ≈ $0,057 por ejecución | Necesita un video ya animado; hoy no aplica                                      |

## Cuánto se ha gastado (estimación)

Lo que muestra la lista de predictions de Replicate desde que empezó el trabajo del canal, a precios de lista. **No es tu factura**: el consumo real está en el panel de Replicate.

| Concepto               | Predictions                                  | Costo estimado                                  |
| ---------------------- | -------------------------------------------- | ----------------------------------------------- |
| `flux-2-pro`           | 55                                           | **≈ $2,5 a $3,3** (con una referencia cada una) |
| `stable-audio-2.5`     | 3                                            | $0,60                                           |
| `qwen3-tts`            | 18 (≈ 1.000 caracteres en las más recientes) | **centavos**                                    |
| `gemini-3.1-flash-tts` | 6                                            | ≈ $0,1                                          |
| **Total**              | 82                                           | **≈ $3,3 a $4,1**                               |

**Lo que dicen los números:**

- **La voz casi no cuesta.** Un guion entero a $0,02 con qwen; incluso la voz más cara (elevenlabs/v3 o minimax HD) cuesta ≈ $0,10. Probar voces no es lo que encarece el canal.
- **Lo que cuesta es la imagen**, y sobre todo los **reintentos y los experimentos**: 55 predictions de imagen para unas 37 imágenes útiles. Cambiar de modelo ahorra poco (≈ $0,045 → $0,035 por imagen, ≈ 22 %); **evitar reintentos ahorra bastante más**.
- **El sonido a $0,20 por archivo es el más caro por unidad** y tiene alternativa ≈ 38 veces más barata.

## Notas de uso

- **Límite de ritmo de Replicate:** no lanzar más de unas pocas peticiones a la vez; las excedentes reciben un 429. Enviar en serie con reintentos.
- Los parámetros de entrada cambian por modelo: se copian de la pestaña *API* de cada uno.
- Fuentes de precio: la sección *Pricing* de cada página de modelo en Replicate, leída el 3-oct-2026. Los precios pueden cambiar.

