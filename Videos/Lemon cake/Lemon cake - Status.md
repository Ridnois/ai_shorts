---
type: research
created: 2026-10-03
updated: 2026-10-03
status: etapas 0–4 en borrador · esperando P1–P3 + P4a y P4 · NADA generado
tags: [investigación, youtube, estado, queque, shorts]
---

# Queque · estado

← [[YouTube Channel]] · [[Fast workflow]]

Cuarto video del canal, **segundo Short vertical (9:16)**. Hecho con [[Fast workflow]]: solo texto hasta P4. **No se llamó a Replicate ni se creó nada en `Media/`.**

## Registro de etapas

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | **3-oct-2026** · "apruebo el enfoque" | Pedido: "un guion sobre cómo hacer un queque"; **hasta 20 imágenes** y **un modelo de voz que suene mejor y sea barato** (3-oct-2026) |
| 1 Investigación | ✅ P2 | **3-oct-2026** · "publicamos como receta base" (no se hornea antes) | [[Research - Lemon cake]]: 15 afirmaciones; **las cantidades se contradicen entre fuentes** (huevos 2 o 4; polvos 1 o 2 cucharaditas; horno 30 a 60 min). **No se probó la receta** |
| 2 Guion | ✅ P3 | 3-oct-2026 · implícita al aprobar el enfoque | [[Script - Lemon cake (80 seconds)]]: 179 palabras, ≈ 80 s, 8 escenas |
| 3 Dirección | ✅ P4a | 3-oct-2026 · implícita | 20 láminas, abajo |
| 4 Prompts y presupuesto | ✅ P4 | **3-oct-2026** · "apruebo el presupuesto" | **≈ $0,70, tope ≈ $0,90** |
| 5 Pruebas | ✅ P5 | 3-oct-2026 · "Horrible illustration… elevenlabs is better, no batidora sound" | Se eligió `elevenlabs/v3`; la imagen se rehízo |
| 6 Generación | ✅ P6 | 3-oct-2026 · **delegada**: "follow the rest yourself till the render… make all decisions" | 8 voces, 20 láminas, 0 sonidos. Ver *Generación y montaje* |
| 7 Montaje | ✅ render r2 · ⏳ P7 | ⏳ | `render/queque-80s-9x16-r2.mp4`, **81,22 s, 1080×1920**, con `gpt-image-1.5` y el nuevo estilo de texto. La r1 usaba las láminas antiguas |
| 8 Publicación | ⏳ no iniciada | — | Falta título, descripción con fuentes (**declarar "receta base de varias fuentes"**) y declaración de IA |

## Voz: más natural y barata (propuesta, se decide en P5)

**Por qué cambiar:** la voz de `qwen3-tts` salió a ≈ 122 palabras por minuto, sin control de velocidad y con pausas largas ([[Brazil and embassies - Status]]). Un modelo con `speed` permite ajustar la voz al guion y evita recortar el texto o regenerar.

| Modelo | Precio (Replicate, 3-oct-2026, de [[Channel models]]) | Costo de este guion (≈ 1.010 caracteres) | Por qué |
| --- | --- | --- | --- |
| **`minimax/speech-2.8-turbo`** (recomendado) | ≈ $0,06 por 1.000 tokens (≈ 1 token por carácter) | **≈ $0,06** | Multilingüe, con control de velocidad y emoción; más natural que un TTS abierto según las comparativas que leí. **Hay que confirmar en la pestaña API el nombre de `speed` y de las voces en español** |
| `elevenlabs/v3` | $0,10 por 1.000 caracteres | ≈ $0,10 | La voz más expresiva, a un costo aún pequeño |
| `qwen/qwen3-tts` (actual) | $0,02 por 1.000 caracteres | ≈ $0,02 | Línea base: ya conocida, más lenta |

- **Prueba P5 de voz:** solo la escena 1 (≈ 100 caracteres) en `minimax/speech-2.8-turbo` y en `elevenlabs/v3`: **≈ $0,02 en total**. **Yo no puedo oír la diferencia: la eliges tú.** Se elige una y no se vuelve a cambiar.
- Español de Chile o neutro: se elige una voz en la prueba.
- **Limitación:** "suena mejor" es una impresión que solo tú puedes juzgar.

## Dirección: 20 láminas (vertical 9:16 · 1080×1920)

Reglas de [[Fast workflow]] §8 y §9: **una sola lámina grande por imagen, que explica el mecanismo** (flechas, círculos numerados vacíos, vistas en corte), foco entre el 15 y el 60 % de la altura, nada clave en el tercio inferior ni en el 6 % superior. Estilo: estilo visual de bocetos técnicos (retirado); **acento cobre-naranja = lo que importa en cada paso**. Sin rostros ni palabras ni cifras dentro del dibujo (se ponen en edición). Las cantidades que importan se **verifican a ojo**.

| # | Escena | Qué explica la lámina | Acento |
| --- | --- | --- | --- |
| 1 | 1 Gancho | **El resultado**: dos cortes de queque lado a lado, uno bajo y denso (el ladrillo) y uno alto con muchas burbujas | La miga alta |
| 2 | 1 Gancho | **Los seis pasos**: un camino de seis piedras numeradas desde un bol hasta un horno, cada una con su icono | La flecha del camino |
| 3 | 2 Ingredientes | **Los ingredientes**: 2 tazas de harina, 1 de azúcar, 1 de leche, media taza de mantequilla, 2 huevos, cucharaditas y vainilla, en fila | La mantequilla |
| 4 | 2 Ingredientes | **A temperatura ambiente**: una barra de mantequilla con un dedo hundiéndola; dos huevos al lado; una flecha del refrigerador a la mesa | La huella del dedo |
| 5 | 2 Ingredientes | **Por qué**: un bol con mantequilla y huevos y un círculo de aumento que muestra la emulsión con burbujas de aire atrapadas | Las burbujas |
| 6 | 3 Cremar | **Batir**: una batidora eléctrica de mano sobre un bol con mantequilla y azúcar, con flechas en las varillas | Las varillas |
| 7 | 3 Cremar | **El porqué, en corte**: cristales de azúcar abriendo bolsillos de aire dentro de la mantequilla | Los bolsillos de aire |
| 8 | 3 Cremar | **Antes y después**: dos boles, uno con mezcla amarilla y densa y otro con crema pálida y esponjosa, con una flecha | La flecha |
| 9 | 4 Huevos | **De a uno**: una mano rompe un huevo sobre el bol mientras otro huevo espera aparte | El huevo que cae |
| 10 | 4 Huevos | **Si se corta**: dos boles, uno con mezcla cortada y grumosa (huevo frío) y otro liso y brillante | La mezcla cortada |
| 11 | 5 Secos y leche | **Tamizar**: un tamiz sobre un bol con harina y polvos cayendo | El polvo cayendo |
| 12 | 5 Secos y leche | **Alternar**: un bol con tres flechas en secuencia, harina, leche, harina | Las flechas |
| 13 | 5 Secos y leche | **El gluten**: a la izquierda una espátula que mezcla con suavidad; a la derecha una batida fuerte con hebras elásticas en un círculo de aumento | Las hebras |
| 14 | 6 Horno | **El molde**: un pincel con mantequilla y harina espolvoreada en un molde alargado | El pincel |
| 15 | 6 Horno | **Verter**: la masa cayendo de un bol al molde con una espátula | La masa |
| 16 | 6 Horno | **Por qué sube**: un horno en corte con el molde dentro, flechas de calor y burbujas expandiéndose dentro de la masa | Las flechas de calor |
| 17 | 7 La prueba | **El palillo**: un queque con un palillo clavado en el centro y otro palillo limpio aparte | El palillo limpio |
| 18 | 7 La prueba | **Reposo**: el molde sobre una rejilla con un reloj de arena y una flecha hacia el desmolde | El reloj de arena |
| 19 | 8 Cierre | **El resultado**: un queque cortado con una rebanada levantada que muestra la miga con burbujas | La rebanada |
| 20 | 8 Cierre | **Los seis pasos**: seis objetos en una repisa (mantequilla, huevo, tamiz, espátula, molde, palillo) con **un hueco vacío** | El hueco vacío |

**Texto en pantalla (en edición):** `Paso 1` a `Paso 6` (escenas 2 a 7), `180 °C` (esc. 6), `35–40 min` (esc. 7). Los números de paso van a la altura del 27 % desde abajo, como en [[Brazil and embassies - Status]].
**Sonido (2 efectos, opcional):** batidora eléctrica corta (esc. 3) y el aviso del horno (esc. 7), con `sepal/audiogen`.
**Montaje (Blender):** `build_brasil.py` como base; una imagen cada ≈ 4 s, "pasar la hoja" entre escenas, fundido cruzado dentro de una escena. Se cambia `W, H = 1080, 1920`, ya está.

## Prompts (P4: pendiente de aprobación)

**Bloque de estilo (en positivo, al final de cada prompt):**

```
Detailed industrial design concept sketch on warm off-white paper, vertical 9:16 sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat cool-grey marker fills in several tones, and a single copper-orange marker accent on the one important element. Technical-drawing feel with blank dimension lines and arrowheads, empty numbered callout circles, and plain unmarked surfaces. A hand-drawn design sheet.
```

**Imágenes:** `black-forest-labs/flux-2-klein-4b`, `aspect_ratio` 9:16, formato PNG, **una referencia**: `brasil-e4-v3.png` (la lámina que mejor explica un mecanismo). Todos los prompts empiezan con *"One single large drawing filling the sheet:"* y terminan con *"<X> is the copper-orange accent."*

| # | Prompt (antes del bloque de estilo) |
| --- | --- |
| 1 | two cross-sections of baked cakes side by side: on the left a low flat dense loaf with tiny holes, on the right a tall domed loaf full of round air bubbles; numbered callouts on both. The tall loaf's golden crust |
| 2 | six numbered stepping stones forming a winding path from a mixing bowl at the bottom to an oven at the top; on the stones a butter block, an egg, a sieve, a spatula, a loaf pan and a toothpick. The path's arrow |
| 3 | a flat-lay of baking ingredients in a row: two measuring cups of flour, one measuring cup of sugar, one measuring cup of milk, half a cup of butter, two eggs, two measuring spoons and a small vanilla bottle. The butter |
| 4 | a block of butter on a counter with a finger pressing a dent into it, two eggs beside it, and a curved arrow from an open refrigerator to the counter. The dent in the butter |
| 5 | a mixing bowl with soft butter and two eggs inside, and a large magnifying circle showing a smooth emulsion with tiny trapped air bubbles. The air bubbles |
| 6 | a handheld electric mixer with two beaters over a bowl of butter and sugar, curved arrows around the beaters. The beaters |
| 7 | a cutaway of a block of butter with sugar crystals cutting small round air pockets inside it, with an enlarged circle and arrows. The air pockets |
| 8 | two bowls side by side with an arrow between them: on the left a dense yellow mixture, on the right pale fluffy cream. The arrow |
| 9 | a hand cracking an egg over a mixing bowl while a second egg waits on the counter beside it. The falling egg |
| 10 | two bowls side by side: on the left a curdled lumpy mixture with a cold egg and an ice cube beside it, on the right a smooth glossy mixture. The curdled lumps |
| 11 | a sieve held over a bowl with flour and baking powder falling in a fine cloud. The falling powder |
| 12 | a mixing bowl with three arrows in sequence around it: a scoop of flour, a jug of milk, a scoop of flour. The three arrows |
| 13 | two panels: on the left a spatula gently folding batter, on the right a whisk beating hard with elastic gluten strands shown in an enlarged circle. The gluten strands |
| 14 | a brush spreading butter inside a long loaf pan while flour is dusted over it. The brush |
| 15 | batter pouring from a bowl into a loaf pan with a spatula scraping the bowl. The pouring batter |
| 16 | a cutaway of an oven with a loaf pan inside, heat arrows rising from below, and the batter in the pan showing expanding round bubbles and a rising dome. The heat arrows |
| 17 | a baked loaf with a toothpick stuck in the centre and a second clean toothpick lying beside it. The clean toothpick |
| 18 | a baked loaf in its pan on a wire cooling rack with a large sand timer beside it and a curved arrow toward an unmoulding. The sand timer |
| 19 | a sliced loaf with one slice lifted to show a crumb full of small air holes. The lifted slice |
| 20 | a wooden shelf with six objects in a row (a butter block, an egg, a sieve, a spatula, a loaf pan, a toothpick) and one empty slot in the row. The empty slot |

**Voz:** `minimax/speech-2.8-turbo` (y `elevenlabs/v3` solo en la prueba), 8 tomas, una por escena, con el texto exacto del guion; velocidad fijada en la prueba P5. Se copia el esquema de la pestaña API antes de llamar.
**Sonido:** `sepal/audiogen`, 2 s cada uno: *"an electric hand mixer whirring briefly over a metal bowl, close microphone, steady"* y *"a kitchen oven timer bell ringing twice, quiet kitchen"*.

## Presupuesto en dólares (tope = base × 1,2)

| Categoría | Modelo | Cantidad base | Precio unitario | Subtotal | Tope |
| --- | --- | --- | --- | --- | --- |
| Imagen | `flux-2-klein-4b` | **20** | ≈ $0,03 (klein + 1 referencia, **sin confirmar**) | **≈ $0,60** | 24 imágenes (≈ $0,72) |
| Voz | `minimax/speech-2.8-turbo` | 8 tomas (≈ 1.010 caracteres) | ≈ $0,06 por 1.000 | **≈ $0,06** | 10 predictions |
| Voz · prueba | los dos candidatos, escena 1 | 2 | ≈ $0,01 c/u | **≈ $0,02** | |
| Sonido | `sepal/audiogen` | 2 | ≈ $0,011 | **≈ $0,02** | 2 |
| **Total** | | | | **≈ $0,70** | **≈ $0,90** |

- **Prueba P5 (dentro del total):** una imagen (la #1), la voz de la escena 1 en los dos modelos y un sonido: **≈ $0,06**.
- Reintentos: **una sola vez** por imagen, solo si cambia el prompt; las imágenes más propensas a fallar por conteo son la 3, la 20 y la 1.
- Para comparar: el Short de Brasil costó ≈ $0,46 con 7 imágenes; aquí 20 imágenes son ≈ $0,60.

## Qué espera tu decisión

1. **P1–P3 + P4a:** ¿el enfoque ("seis pasos, cada uno con su porqué"), el texto (léelo en voz alta) y las 20 láminas?
2. **P2:** las cantidades se contradicen entre fuentes y **la receta no se probó**: ¿hornea una vez antes de publicar, o publicamos como "receta base"?
3. **P4:** el presupuesto de ≈ $0,70 (tope ≈ $0,90) y los prompts. **Sin tu OK no genero nada.**

## Registro de predictions

Formato: `escena · categoría · modelo · estado · predicción`.

| Escena | Categoría | Modelo | Estado | Predicción |
| --- | --- | --- | --- | --- |
| 1 | voz | `minimax/speech-2.8-turbo` (voz `Casual_Guy`, `language_boost: Spanish`) | ⏳ P5 | [w657yw5gmxrmy0d10a3vszb1ww](https://replicate.com/p/w657yw5gmxrmy0d10a3vszb1ww) |
| 1 | voz | `elevenlabs/v3` (voz `Roger`, `es`) | ⏳ P5 | [qbdbkrpbt5rmr0d10a3rq3m3sw](https://replicate.com/p/qbdbkrpbt5rmr0d10a3rq3m3sw) |
| 1 | imagen #1 | `flux-2-klein-4b` (referencia `brasil-e4-v3`) | ⏳ P5 | [mmczstr0enrzy0d10a4859yx8c](https://replicate.com/p/mmczstr0enrzy0d10a4859yx8c) |
| 3 | sonido | `sepal/audiogen` | ⏳ P5 | [7axfrz9jdhrmr0d10a4a44xvam](https://replicate.com/p/7axfrz9jdhrmr0d10a4a44xvam) |

**Predictions: 4 de las 4 de la prueba.**

## Resultado de la prueba P5 (3-oct-2026)

Archivos en `Media/Queque - 80 segundos/` (`voz/`, `ilustraciones/`, `audio/`).

| Prueba | Resultado | Lo que no pude comprobar |
| --- | --- | --- |
| **Voz `minimax/speech-2.8-turbo`** (`queque-e1-voz-minimax-turbo-v1.wav`) | 7,98 s para 19 palabras (≈ 143 palabras por minuto con pausas), 32 kHz mono. Voz integrada `Casual_Guy`, con `language_boost: Spanish` | **Si suena natural, el acento y si lee bien "queque"** |
| **Voz `elevenlabs/v3`** (`queque-e1-voz-eleven-v3-v1.mp3`) | 6,73 s para las mismas 19 palabras (≈ 169 palabras por minuto con pausas), 44,1 kHz. Voz `Roger`, `es` | Lo mismo |
| **Imagen #1** (`queque-i01-v1.png`, 768×1344) | Comunica la idea: **un corte bajo y denso a la izquierda y una pieza alta con burbujas a la derecha**; estilo y cobre bien. **Reservas:** la pieza alta parece un pan largo más que un queque; cotas ilegibles (garabatos); el dibujo ocupa solo la franja media | Si lo aceptas |
| **Sonido** (`queque-e3-batidora-v1.wav`) | 2,0 s, 16 kHz mono | Cómo suena |

### Decisiones para ti (P5)

1. **Voz:** escucha las dos y elige. Estimación de ritmo con 179 palabras: `minimax` ≈ 80 a 85 s; `elevenlabs` ≈ 65 a 70 s. **Con `speed` se ajusta cualquiera.** `qwen` queda fuera. Costo de las pruebas de voz ≈ $0,02.
2. **Imagen:** ¿apruebas el look? Si no, qué cambiarías (por ejemplo, la pieza alta con forma de molde de queque).
3. **Sonido:** ¿te sirve?

**Gasto de la prueba (estimado):** voz ≈ $0,02 · imagen ≈ $0,03 (precio de klein sin confirmar) · sonido ≈ $0,011 · **≈ $0,06**, como estaba previsto.

## Feedback tras la prueba y decisiones (3-oct-2026)

> *«Horrible illustration, look for home queque, no nuts on them, no circles, search on the internet homemade queque so you understand, fuente rectangular transparente para horno, queque con ceste de limon. Readjust the script. Elevenlabs is better, no batidora sound.»* y *«follow the rest yourself till the render, you can make all decisions and wait for me with the render ready.»*

| Feedback | Qué hice |
| --- | --- |
| Ilustración "horrible": queque casero, sin frutos secos, **sin círculos** | La lámina anterior copiaba círculos numerados de la referencia `brasil-e4-v3`. **Se quitó la referencia, los círculos numerados y las burbujas redondas** del estilo (nuevo bloque en positivo: líneas rectas, flechas con punta, formas angulares e irregulares) |
| **Fuente rectangular transparente** y **limón** | Todas las láminas con horno o masa muestran la fuente rectangular de vidrio; ralladura de limón en la masa y rallador en los ingredientes. Búsqueda de queque de limón casero: se confirmó ralladura en la masa, 180 °C, fuente rectangular, palillo limpio |
| Reajustar el guion | Guion v2: queque **de limón**, fuente de vidrio, ralladura al final de la masa, sin vainilla; 197 palabras. Ver [[Script - Lemon cake (80 seconds)]] |
| `elevenlabs/v3` es mejor | Voz `Roger`, `es`, velocidad 0,95; `previous_text` y `next_text` para la entonación |
| Sin sonido de batidora | **Sin efectos de sonido** en todo el video (no puedo juzgar `audiogen` y se rechazó el primero) |

## Generación y montaje (3-oct-2026)

| Categoría | Predictions | Costo (estimado) |
| --- | --- | --- |
| Voz | 2 de prueba (P5) + 8 (`elevenlabs/v3`, 1.107 caracteres) | ≈ $0,12 |
| Imagen | 1 prueba v1 (con referencia) + 1 prueba v2 + 19 láminas + 2 reintentos (#18 y #20) = **23** (tope 24) | ≈ $0,36 (sin referencia ≈ $0,015 c/u; **precio sin confirmar**) |
| Sonido | 1 de prueba (descartada) | ≈ $0,01 |
| **Total** | **34** | **≈ $0,50**; tope aprobado ≈ $0,90 |

**Render r1:** `Media/Queque - 80 segundos/render/queque-80s-9x16-r1.mp4`, **81,22 s**, 1080×1920, video y audio (comprobado en las cabeceras del mp4). Script: `Sistema/scripts/build_queque.py`.

- **Voz:** 8 tomas; cada tira cubre su voz completa más 0,25 s de cola (comprobado con los tiempos del archivo); silencio de 0,4 s entre escenas y 0,9 s antes del cierre.
- **Láminas:** 20, repartidas por escena (2, 3, 3, 2, 3, 3, 2, 2) en partes iguales, con fundido cruzado de 0,3 s dentro de cada escena y "pasar la hoja" entre escenas; empuje lento del 6 %. **Los cambios de lámina no están sincronizados con cada palabra**, solo con la escena.
- **Texto:** `6 pasos`, `Paso 1` a `Paso 4`, `Paso 5 · 180 °C` y `Paso 6 · ≈ 40 min`, sobre una banda de papel al 20–34 % desde abajo.
- Sin efectos de sonido, sin música.

### Qué revisé y qué no

- ✅ Duración y pistas del mp4; ocho fotogramas clave (encuadre, banda y textos legibles).
- ❌ **No oí el audio ni vi el video completo:** voz, ritmo (las 8 tomas suman 77,6 s en bruto para 197 palabras, ≈ 150 palabras por minuto con pausas), fundidos y si la banda tapa algo importante.
- **Láminas que se desvían:** #2 (el camino de seis piedras muestra solo cuatro tarjetas con iconos legibles), #5 (inserto con puntitos naranja), #12 (las tres flechas parecen cucharas), #20 (cinco objetos en vez de seis, sin palillo, y el hueco no se ve claro). El resto sirve.
- **Receta:** sigue sin hornear; las cantidades salen de varias fuentes que no coinciden.

### Qué espera tu decisión (P7)

1. **Mira y escucha** el mp4: ¿voz y ritmo bien? ¿Los cambios de lámina caen donde corresponde?
2. ¿Rehago #2, #12 y #20 (≈ $0,05, 1 imagen de margen en el tope)?
3. **Antes de publicar (P8):** título, descripción como *receta base de varias fuentes* (el tiempo depende del horno) y declaración de IA.

## v3 de ilustraciones con `nano-banana-2` (3-oct-2026) · pendiente de aprobación del gasto

> *«Improve the estilo visual dataset, use nano-banana-2 for images and provide them more context, redo the prompts for the images adding more context of the scene they are representing, make this with the queque video and rerender it.»*

**Hecho (solo texto y una imagen de prueba):**
- **Dataset de estilo v2** en estilo visual de bocetos técnicos (retirado): bloque de estilo v3, plantilla de contexto de escena, fichas de objetos reales, catálogo de errores y 5 referencias en `_canal/estilo/v2/`.
- **20 prompts con contexto de escena** (≈ 200 a 270 palabras cada uno: de qué trata el video, qué dice la narración en ese momento, el sujeto con detalles reales, composición y acento): prompts de imagen de Queque (retirados).
- **Prueba de la imagen #1** con `google/nano-banana-2` (2 referencias del dataset e `image_search`): `ilustraciones/queque-i01-nb1.png`. Resultado: fuentes de vidrio con asas, queque dorado con grieta, medio limón, sin círculos. **Es una mejora clara frente a `flux-2-klein-4b`.**

**Presupuesto para terminar (en dólares):**

| Concepto | Cantidad | Precio | Subtotal |
| --- | --- | --- | --- |
| `nano-banana-2` (1K, 9:16), imágenes #2 a #20 | 19 | ≈ $0,067 (**sin confirmar si las referencias o `image_search` cobran aparte**) | **≈ $1,27** |
| Prueba ya hecha (#1) | 1 | ≈ $0,067 | ≈ $0,07 |
| Reintentos (máximo uno por imagen y hasta el tope de 24 imágenes) | hasta 4 | ≈ $0,067 | hasta ≈ $0,27 |
| Voz, montaje | reutiliza lo hecho | $0 | $0 |
| **Total de esta ronda** | | | **≈ $1,34**; tope **≈ $1,61** |

- Gasto previo del video: ≈ $0,50; con esta ronda el video llega a **≈ $1,85** (tope ≈ $2,10). **Pasa del tope aprobado ($0,90).**
- Es ≈ 4,5 veces lo que costó la ronda de `flux-2-klein-4b` (≈ $0,29 por las 19 láminas).
- **Si apruebas:** genero #2 a #20 en serie (lotes de ≤ 10), miro las 20 juntas, rehago como máximo las que fallen, adapto `build_queque.py` a las láminas nuevas y renderizo `queque-80s-9x16-r2.mp4`. La voz no cambia.
- **Si prefieres gastar menos:** se pueden generar solo las 10 láminas más importantes con `nano-banana-2` (#1, 5, 7, 10, 13, 16, 17, 19, 20 y 2) y dejar el resto con las de `flux-2-klein-4b`; ≈ $0,60.

## Ronda `gpt-image-1.5` + estilo de texto + render r2 (3-oct-2026)

> *«Design a style for text, it must be sober, professional and modern, then proceed with the next steps, remove the old photos and proceed with gpt-image-1.5.»*

| Qué | Cómo |
| --- | --- |
| **Estilo de texto** | Nueva tarjeta de etiqueta (barra cobre, etiqueta espaciada y título en negrita): [[On-screen text style]]. Escenas 1 a 7; la 8 queda sin tarjeta |
| **Imágenes** | Las 20 con `openai/gpt-image-1.5` (calidad media, 2:3, 3 referencias de biblioteca de referencias de sketch técnico (retirada) según el tipo de lámina, **sin referencias propias**). Se extendió el papel arriba y abajo hasta 9:16 con el color real del borde de cada lámina (`queque-iNN-gpt-v.png`) para no recortar los lados |
| **Fotos antiguas** | **Borradas:** las 20 láminas de `flux-2-klein-4b`, los reintentos (#18 y #20), la prueba de `nano-banana-2` (#1) y la carpeta `_descartes`; en `_canal/estilo/` se borró `v2/` (copias de láminas antiguas). **Se conservan:** los 20 originales de `gpt-image-1.5` y, en `_canal/estilo/`, `v1`, `v3-externas` y `v4-gpt`. *(Las imágenes de la investigación de modelos ya no están en esta carpeta: viven en `_canal/investigacion/`.)* |
| **Reintentos** | Ninguno: las 20 salieron y se aceptan (ver reservas) |

**Gasto de esta ronda (estimado):** 20 imágenes × ≈ $0,05 (tarifa de OpenAI para 1024×1536 en calidad media, **no confirmada en Replicate**) ≈ **$1,00**. Con la lámina de prueba de `nano-banana-2` (≈ $0,07), el video acumula **≈ $1,57**. *(La investigación de modelos de imagen se lleva aparte, no cuenta en el costo del video.)*

**Render r2:** `render/queque-80s-9x16-r2.mp4`, 81,22 s, 1080×1920, video y audio. La voz es la misma de la r1 (`elevenlabs/v3`).

### Reservas

- **Cajas de rotulado vacías** (pedí "cajas en blanco" para evitar texto): salen en casi todas las láminas y se leen como marcadores de posición sin rellenar. Si molestan, la v4 del prompt las pide como *líneas guía que terminan en una flecha pequeña*, sin cajas (costaría regenerar).
- **#1 y #20**: mucho papel vacío; #20 muestra un hueco naranja resaltado y no cinco objetos exactos.
- **No oí el audio ni vi el video completo**; vi ocho fotogramas clave del montaje (tarjetas, encuadre).
- La receta sigue **sin hornear**; publicar como *receta base de varias fuentes*.

### Qué espera tu decisión (P7)

1. Mira y escucha el mp4. ¿Estilo de texto y láminas bien?
2. ¿Regeneramos las láminas sin cajas vacías (≈ $1,00 con `gpt-image-1.5` en calidad media; ≈ $0,26 en calidad baja, no probada)?
3. Para publicar: título, descripción como *receta base*, declaración de IA.
