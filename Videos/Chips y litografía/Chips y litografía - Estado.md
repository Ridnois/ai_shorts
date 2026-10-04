---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: etapas 0–4 en borrador · P5 aprobada · generación hecha (7 voces, 8 láminas) · render r1 · esperando P7
tags: [investigación, youtube, estado, chips, canon, shorts]
---

# Chips y litografía · estado

← [[Canal YouTube]] · [[Flujo rápido]]

Quinto video del canal, **Short vertical (9:16)**. Idea: [[Chips - países y marcas, Canon y los 2 nm]]. Solo texto hasta P4: **no se llamó a Replicate ni se creó nada en `Media/`.**

## Registro de etapas

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ✅ | 3-oct-2026 · "Perfect go for the next" | Pedido: cómo compiten países y marcas en fabricar microchips y cómo avanza Canon en la escala de 2 nm |
| 1 Investigación | ✅ P2 | 3-oct-2026 · "I approve, go for package B" | [[Investigación - Chips y litografía]]: 15 afirmaciones; 4 quedan fuera por débiles u obsoletas |
| 2 Guion | ✅ P3 | 3-oct-2026 · ídem | [[Guion - Chips y litografía (85 segundos)]]: 211 palabras, ≈ 84 s, 7 escenas |
| 3 Dirección | ✅ P4a | 3-oct-2026 · ídem | 8 láminas, en el guion |
| 4 Prompts y presupuesto | ✅ P4 | 3-oct-2026 · "I approve, go ahead" | ≈ $0,44, tope ≈ $0,50 |
| 5 Prueba | ✅ P5 | 3-oct-2026 · "Everything ok, go ahead" | Imagen 1 y voz de la escena 1 aceptadas |
| 6 Generación | ✅ P6 | 3-oct-2026 · misma frase (se entendió como seguir hasta el render, dentro del tope) | 7 voces, 8 láminas + 1 reintento |
| 7 Montaje | ⏳ P7 | — | `Media/Chips - 85 segundos/render/chips-93s-9x16-r1.mp4` |

## Fotos de referencia (una por lámina; Kontext admite una sola `input_image`)

**R1 descargada** a `Media/Chips - 85 segundos/ilustraciones/_referencias/` (R2 y R3 se bajan si se aprueba la prueba). Licencias comprobadas en Wikimedia Commons el 3-oct-2026:

| Ref. | Foto | Autor · licencia | Usada en láminas |
| --- | --- | --- | --- |
| R1 | [Wafer with Pentium chips](https://commons.wikimedia.org/wiki/File:Wafer_with_Pentium_chips.jpg) (1200×1600) | Naotake Murayama · **CC BY 2.0** | 1, 3, 5, 6, 7, 8 |
| R2 | [Extreme ultraviolet lithography tool](https://commons.wikimedia.org/wiki/File:Extreme_ultraviolet_lithography_tool.jpg) (713×605) | Lawrence Livermore National Laboratory · **dominio público** | 2 |
| R3 | [Padlock with chain](https://commons.wikimedia.org/wiki/File:Padlock_with_chain.jpg) (3264×2448) | Lacz02 · **CC BY-SA 4.0** | 4 |

- **Atribución** en la descripción: R1 y R3 (CC BY y CC BY-SA 4.0: revisar condiciones antes de publicar).
- **Limitación honesta:** **R2 es un prototipo de EUV de los años 90 (Livermore), no una máquina de ASML** ni una de hoy. En plastilina solo se verá «una máquina grande»; no se afirma que sea de ASML. **No encontré foto libre de la FPA-1200NZ2C de Canon ni de un molde de nanoimpresión**: esas láminas (1, 5, 6, 7) se dibujan a partir de la oblea R1 con el molde descrito en el prompt, **sin verificar que Kontext lo haga bien** (por eso la prueba P5).
- Las tres fotos son horizontales o 3:4: se usa `match_input_image` y el montaje llena el cuadro 9:16 con la escala `max`.

## Prompts de imagen (P4: pendiente de aprobación)

**Modelo:** `black-forest-labs/flux-kontext-pro`, `aspect_ratio` `match_input_image`, PNG, una `input_image` (ver arriba). Cada prompt lleva la frase de la narración, el objeto, el estado, el acento cobre-naranja y el bloque de estilo.

**Bloque de estilo (al final de cada prompt):**

```
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

| # | Ref. | Prompt (antes del bloque de estilo) |
| --- | --- | --- |
| 1 | R1 | Narration: "Canon shipped to Texas a machine that does not project chips with light: it stamps them, like a seal." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of small rectangular chips. Replace the background with a plain warm tabletop. A large grey clay rubber stamp with a round handle presses down onto the wafer from above. The stamp's handle is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 2 | R2 | Narration: "The most advanced chips are drawn with extreme ultraviolet light, and only one company builds those machines." Redraw this exact large lithography machine as a handmade plasticine clay miniature. Keep its large boxy body and its tall cylindrical column. Replace the background with a plain warm tabletop. A tiny clay figure stands next to it to show how big it is, back turned to the viewer. The machine's top light source is in bright copper-orange clay. The machine fills the frame, vertical composition. Remove all lettering and logos. |
| 3 | R1 | Narration: "Whoever does not have these machines cannot reach the smallest chips; one foundry makes almost three of every four dollars." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of small rectangular chips. Replace the background with a plain warm tabletop. All chips are matte grey clay and exactly one cluster of chips in the center is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 4 | R3 | Narration: "Countries fight over these machines: one bans their sale, another keeps advancing with older light." Redraw this exact padlock as a handmade plasticine clay miniature. Keep the rounded body, the curved shackle and the chain. Replace the background with a plain warm tabletop. The padlock is locked through the chain around a large grey clay machine crate behind it. The padlock body is in bright copper-orange clay. The padlock fills the frame, vertical composition. Remove all lettering and logos. |
| 5 | R1 | Narration: "Canon proposes another path: pressing a mold onto resin." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape. Replace the background with a plain warm tabletop. A flat square glass-like clay mold plate hovers just above a thin shiny layer of clay resin on the wafer, about to touch it. The hovering mold plate is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 6 | R1 | Narration: "With better molds, it would reach two nanometers." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape. Replace the background with a plain warm tabletop. A flat square clay mold plate is pressed into the thin resin layer on the wafer and a neat pattern of tiny lines is copied into the resin around its edge. The copied pattern is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 7 | R1 | Narration: "When the mold touches the wafer it sheds particles, and a single defect ruins the chip." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of chips. Replace the background with a plain warm tabletop. A clay mold plate lifts away from the wafer and a single small speck of dust sits trapped on one chip. The speck of dust is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |
| 8 | R1 | Narration: "The one that repeats the same chip, without failures, millions of times." Redraw this exact silicon wafer as a handmade plasticine clay miniature. Keep the round disc shape and the grid of identical small chips. Replace the background with a plain warm tabletop. Every chip is perfectly clean and identical, and a grey clay stamp is lifted high above the wafer. The stamp's handle is in bright copper-orange clay. The wafer fills the frame, vertical composition. Remove all lettering and logos. |

**Sin texto en la imagen:** etiquetas y cifras van en edición ([[Estilo de texto en pantalla]]).

## Voz: `elevenlabs/v3`

7 tomas, una por escena, con el **texto exacto** del guion (1.201 caracteres en total), voz `Roger`, idioma `es`, `speed` 0,95, `previous_text` y `next_text` de las escenas vecinas ([[Guías para nuevos guiones]] §3). **Esquema por confirmar** con `GET /v1/models/elevenlabs/v3` (gratis) antes de llamar. Si el modelo lee mal una sigla (ASML, TSMC), se reescribe como se dice y se anota. **La voz ya está elegida por el usuario** en videos anteriores.
**Sonido y música:** ninguno.

## Presupuesto en dólares (tope = base × 1,2)

| Categoría | Modelo | Cantidad base | Precio unitario | Subtotal | Tope |
| --- | --- | --- | --- | --- | --- |
| Imagen | `flux-kontext-pro` | **8** (una por lámina, cada una con su escena) | ≈ $0,04 (**de memoria, sin confirmar**) | **≈ $0,32** | 9 imágenes (≈ $0,36) |
| Voz | `elevenlabs/v3` | 7 tomas (1.201 caracteres) | ≈ $0,10 por 1.000 caracteres | **≈ $0,12** | 8 predictions (≈ $0,14) |
| Sonido | — | 0 | — | $0 | 0 |
| Prueba P5 | lámina 1 + voz escena 1 | 2 | — | (dentro del total; ≈ $0,05) | |
| **Total y tope** | | | | **≈ $0,44** | **≈ $0,50** |

- **Si el precio de Kontext es otro**, se confirma en el panel de Replicate antes de la prueba.
- **Riesgo principal:** que Kontext no dibuje bien el sello ni el molde sin foto de ellos. La prueba P5 es la lámina 1, que usa el sello: si sale mal, se cambia el prompt **antes** de reintentar, **una vez**, o se rediseña la escena alrededor del objeto con foto.
- Reintentos: uno por imagen, en serie; pasar de 9 imágenes pide tu aprobación.
- Referencias: Brasil ≈ $0,46; Queque ≈ $1,57; este video es un Short de 8 láminas.

## Qué esperaba tu decisión (P4, aprobada)

1. **Presupuesto:** ≈ $0,44, tope ≈ $0,50.
2. **Prompts y fotos de referencia** (R1–R3), con las limitaciones de arriba: ¿los apruebas, o prefieres que busque otras fotos (por ejemplo, de la máquina de Canon)?
3. **Después de P4:** hago solo la prueba P5 (lámina 1 y voz de la escena 1, ≈ $0,05) y paro; la generación sigue tras tu aprobación, o si delegas («sigue tú hasta el render»), sin parar dentro del tope.

## Registro de predictions

| Escena | Categoría | Modelo | Estado | Predicción |
| --- | --- | --- | --- | --- |
| 1 | imagen #1 | `flux-kontext-pro` (R1) | ⏳ P5 | [6dmnbnytdsrmr0d10hb8vgw5aw](https://replicate.com/p/6dmnbnytdsrmr0d10hb8vgw5aw) |
| 1 | voz | `elevenlabs/v3` (`Roger`, `es`, 0,95) | ⏳ P5 | [g1raw87q3nrmw0d10hbbag3s9g](https://replicate.com/p/g1raw87q3nrmw0d10hbbag3s9g) |

| 2 | voz | `elevenlabs/v3` | ✅ usada | [tfh30nbmk5rmr0d10hcvrx82a4](https://replicate.com/p/tfh30nbmk5rmr0d10hcvrx82a4) |
| 3 | voz | `elevenlabs/v3` | ✅ usada | [f3rwnycah9rmt0d10hcrqb5nf4](https://replicate.com/p/f3rwnycah9rmt0d10hcrqb5nf4) |
| 4 | voz | `elevenlabs/v3` | ✅ usada | [t66h2254ahrmw0d10hcsn3fsn0](https://replicate.com/p/t66h2254ahrmw0d10hcsn3fsn0) |
| 5 | voz | `elevenlabs/v3` | ✅ usada | [dymj9zdwy9rmw0d10hcv8sy5c0](https://replicate.com/p/dymj9zdwy9rmw0d10hcv8sy5c0) |
| 6 | voz | `elevenlabs/v3` | ✅ usada | [xg06hypdd5rmt0d10hcrdpaxww](https://replicate.com/p/xg06hypdd5rmt0d10hcrdpaxww) |
| 7 | voz | `elevenlabs/v3` | ✅ usada | [frbqg7f4w9rmt0d10hcvbbgb2w](https://replicate.com/p/frbqg7f4w9rmt0d10hcvbbgb2w) |
| 2 | imagen #2 | `flux-kontext-pro` (R2) | ✅ usada | [ztd0ecrtd5rmt0d10hd9kpsqc0](https://replicate.com/p/ztd0ecrtd5rmt0d10hd9kpsqc0) |
| 3 | imagen #3 | `flux-kontext-pro` (R1) | ✅ usada | [bwp75q256nrmw0d10hda761n2w](https://replicate.com/p/bwp75q256nrmw0d10hda761n2w) |
| 4 | imagen #4 v1 | `flux-kontext-pro` (R3) | ❌ descartada (marca «PRADO BRAZIL» legible) | [bzc7vmvk8srmw0d10hda94gay0](https://replicate.com/p/bzc7vmvk8srmw0d10hda94gay0) |
| 4 | imagen #4 v2 | `flux-kontext-pro` (R3) | ✅ usada (el reintento) | [q3va1exj31rmt0d10hdthftcmw](https://replicate.com/p/q3va1exj31rmt0d10hdthftcmw) |
| 5 | imagen #5 | `flux-kontext-pro` (R1) | ✅ usada | [vacpvecrpnrmw0d10hdbq2gysm](https://replicate.com/p/vacpvecrpnrmw0d10hdbq2gysm) |
| 5 | imagen #6 | `flux-kontext-pro` (R1) | ✅ usada (con reservas) | [jpnrzqe2w1rmt0d10hd8gt4vyg](https://replicate.com/p/jpnrzqe2w1rmt0d10hd8gt4vyg) |
| 6 | imagen #7 | `flux-kontext-pro` (R1) | ✅ usada (con reservas) | [cqx72f7s0srmr0d10hdbxd4cnw](https://replicate.com/p/cqx72f7s0srmr0d10hdbxd4cnw) |
| 7 | imagen #8 | `flux-kontext-pro` (R1) | ✅ usada (con reservas) | [ny8cbghb1nrmr0d10hdrqbyrxw](https://replicate.com/p/ny8cbghb1nrmr0d10hdrqbyrxw) |

**Predictions: 15 en total** (7 voces + 9 imágenes, incluida la prueba P5 y el reintento) frente al tope de 8 voces y 9 imágenes: **dentro del tope**. Costo estimado: voz ≈ $0,12 · imágenes 9 × ≈ $0,04 = ≈ $0,36 · **≈ $0,48** (precio de Kontext sin confirmar), tope ≈ $0,50.

## Resultado de la prueba P5 (3-oct-2026)

Archivos en `Media/Chips - 85 segundos/` (`ilustraciones/chips-i01-v1.png`, `voz/chips-e1-voz-v1.mp3`).

| Prueba | Resultado | Lo que no pude comprobar |
| --- | --- | --- |
| **Imagen #1** (880×1184, 3:4) | **Funciona:** una oblea de plastilina gris con cuadrículas de chips y un sello gris con mango cobre-naranja encima, estilo plastilina y fondo cálido. **Reservas:** el sello flota sobre la oblea (no la toca), la oblea parece más una tapa de alcantarilla que un disco de chips (cuadrados de tamaños desiguales), y la imagen es 3:4, no 9:16: se llena el cuadro en el montaje con la escala `max` | Si te gusta el look |
| **Voz** (`chips-e1-voz-v1.mp3`) | 141 KB a 128 kbps ≈ **8,8 s para 20 palabras** (≈ 136 palabras por minuto con pausas), calculado por tamaño de archivo | **Cómo suena, el acento y si lee bien "Canon" y "Texas"** |

**Con 211 palabras y ≈ 136 a 150 palabras por minuto, el video durará de 84 a 93 s.** Si es mucho, se sube `speed` o se recorta (Rapidus, energía).

## Generación y montaje (3-oct-2026)

- **Voz:** 7 tomas (`chips-e1` a `e7`), texto exacto del guion, `Roger`, `es`, 0,95, con `previous_text` y `next_text`. Suman ≈ 88 s de voz (≈ 144 palabras por minuto).
- **Láminas:** 8 (`chips-i01` a `i08`), una por escena y dos en la escena 5. Las 8 se miraron en una hoja de contacto. Reservas abajo.
- **Montaje:** `Sistema/scripts/build_chips.py` (base `build_queque.py`): voces sin cortar frases (cola de 0,25 s), 0,45 s entre escenas y 1,2 s antes del cierre, «pasar la hoja» entre escenas, empuje lento del 5 %, tarjetas de etiqueta en las escenas 1 a 6, viñeta y grano. Sin sonido ni música.
- **Render r1:** `render/chips-93s-9x16-r1.mp4`, **≈ 93 s**, 1080×1920 (la duración sale de las voces; es más larga que los 85 s del título del guion).

### Reservas

- **Duración ≈ 93 s** (voz 88 s + entrada y cola): más larga que lo planeado. Si es mucho, se recorta Rapidus (escena 4) y la energía (escena 5) y se vuelve a generar solo esas dos voces (≈ $0,03).
- **Una lámina cada ≈ 10 s** (la regla pide ≈ 4 s): solo hay 8 imágenes aprobadas.
- **#2:** la foto es del prototipo de Livermore, no de ASML; la imagen se ve casi como una foto de maqueta (poca plastilina) y la figura está recortada por el lateral al llenar 9:16.
- **#4 v2** (candado): limpia; el recorte lateral corta parte de las cadenas.
- **#6, #7, #8:** no muestran con claridad el molde (#6 no tiene molde, solo el patrón; #7 tiene dos placas en vez de una que se levanta; #8 tiene chips redondos y el sello es pequeño). Acepto «casi bien» (regla 2.7): ya no queda reintento en el tope.
- **Texto en pantalla:** la escena 5 no muestra «energía ≈ ÷10 (Canon)» (una tarjeta por vez); solo `5 nm hoy · 2 nm meta`. La escena 7 no lleva tarjeta.
- ✅ **Revisé:** el render terminó (64 MB, 1080×1920, 92,95 s según el montaje) y siete fotogramas (segundos 3, 15, 28, 44, 60, 76 y 88): tarjetas legibles, sin pisar el sujeto, texto sin símbolos que falten en la tipografía.
- ❌ **No oí el audio ni vi el video completo:** voz, ritmo, fundidos y si los cambios de lámina caen donde corresponde. La duración del mp4 no se leyó de la cabecera (no hay `ffprobe` en esta máquina); es la del montaje.

### Qué espera tu decisión (P7)

1. **Mira y escucha** el mp4: voz, ritmo y si las láminas caen donde corresponde.
2. ¿Recorto la duración (voz de las escenas 4 y 5) o la dejas en ≈ 93 s?
3. ¿Rehago #6, #7 u #8 (≈ $0,04 c/u, pasa del tope de 9 imágenes) o las dejas?
4. Para publicar: título, descripción con fuentes (atribución de R1 y R3, «datos a 3-oct-2026», cifra de TSMC como **estimación**) y declaración de IA.
