---
type: research
created: 2026-10-03
updated: 2026-10-03
status: etapas 0–4 en borrador · esperando P1–P3 + P4a y P4 · NADA generado
tags: [investigación, youtube, estado, brasil, shorts]
---

# Brasil y embajadas · estado

← [[YouTube Channel]] · [[Fast workflow]]

Tercer video del canal y **primer Short vertical (9:16, 60 s)**. Hecho con [[Fast workflow]]: solo texto hasta P4. **No se llamó a Replicate ni se creó nada en `Media/`.**

## Registro de etapas

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | 3-oct-2026 · implícita ("Script is good") | Pedido: guion de 60 s sobre la situación política de Brasil y el cierre de embajadas brasileñas. **Feedback v1:** enfocar en los candidatos, sus delitos y cómo se sabotea la elección (sospecha de coacción). **Corrección de premisa:** Brasil no cerró embajadas; *advirtió que podría*. Los cierres consumados son de EE. UU. y Australia en Brasil. El guion cuenta ambas |
| 1 Investigación | ✅ P2 | 3-oct-2026 · implícita; **los datos débiles se quedan fuera del guion o atribuidos** | [[Research - Brazil and embassies]]: 24 afirmaciones; **sostenidas: casos de Jair, Lula y las rachadinhas; débiles: investigación de Flávio (preliminar), cifra de Dark Horse, mesas en Río y memorando de R$ 352 M** |
| 2 Guion | ✅ v3 → v4 | v3 aprobado el 3-oct-2026; **v4 la pidió el usuario** (adaptar el guion al ritmo de la voz): 123 palabras | [[Script - Brazil and embassies (60 seconds)]]: v3 con tu segundo feedback (profundizar en los casos judiciales y hacer pensar): condena firme · anulación · archivo, 153 palabras, ≈ 59 s |
| 3 Dirección | ✅ P4a | 3-oct-2026 · implícita ("procede al siguiente paso") | Planos abajo |
| 4 Prompts y presupuesto | ✅ P4 | **3-oct-2026** · "Si consulta el modelo de la API y procede al siguiente paso" | Abajo: **≈ $0,21 con tope de ≈ $0,30** (v3) |
| 5 Pruebas | ✅ P5 | **3-oct-2026** · "1: adapta el guion al ritmo, 2: imagen ok, 3: audio ok" | Ver *Resultado de la prueba P5* |
| 6 Generación | ✅ P6 | 3-oct-2026 · "apruebo el item, continua con el montaje" (se interpretó como encuadrar `e6`, sin reintento) | voz 7/7, imagen 6/6, sonido 2/2. Ver *Generación P6* |
| 7 Montaje | ✅ render r3 · ⏳ P7 | ⏳ | `render/brasil-60s-9x16-r3.mp4`, **63,37 s, 1080×1920**, con las láminas descriptivas. r1 tenía las frases cortadas (arreglado en r2); ver *Montaje r2* y *Láminas v3* |
| 8 Publicación | ⏳ no iniciada | — | Falta título, descripción con fuentes y declaración de IA |

## Dirección (vertical 9:16 · 1080×1920) · v3

Reglas de [[Fast workflow]] §8: un sujeto, composición alta, nada clave en el tercio inferior ni en el 6 % superior, **1 imagen por toma**. Estilo: estilo visual de bocetos técnicos (retirado) (acento cobre-naranja = lo que importa). **Sin rostros ni personas reconocibles: cada caso es un objeto**, el mismo tratamiento para los tres. Sin palabras, banderas legibles ni logos. La imagen de la escena 5 es el **centro del video**: junta los tres objetos para que el espectador compare.

| Escena | Segundos | Imagen | Plano | Emoción | Acento cobre-naranja |
| --- | --- | --- | --- | --- | --- |
| 1 · Gancho | 0–4 | **1** (`e1`) | Una urna de cartón con ranura, en primer plano sobre una mesa; detrás, siluetas de votantes dibujadas; vista alta | Suspenso contenido | La ranura |
| 2 · Jair: condena firme | 4–11 | **1** (`e2`) | Un mazo de juez sobre un bloque de sonido, con una gruesa pila de páginas atadas con cinta al lado | Peso, algo definitivo | El mazo |
| 3 · Lula: anulación | 11–21 | **1** (`e3`) | Un expediente grueso con **el sello de lacre roto en dos** y las páginas sueltas | Algo que se deshace | El lacre roto |
| 4 · Flávio: archivo | 21–34 | **1** (`e4`) | Una carpeta cerrada y atada con cinta, una lupa encima, y a un lado un sobre abierto | Algo guardado, sin cerrar | La cinta |
| 5 · La pregunta | 34–42 | **1** (`e5`) | **Los tres objetos** (mazo, expediente con lacre roto, carpeta con lupa) sobre tres pedestales en fila, y un cuarto pedestal **vacío** al frente; vista frontal y alta | Quietud, pregunta | El pedestal vacío |
| 6 · Votación en disputa | 42–53 | **1** (`e6`) | Una cabina de votación de escuela al fondo de un pasillo, barricada de sacos y una cadena cruzada | Tensión | La cadena |
| 7 · Cierre | 53–60 | **0** · reutiliza `e1` | Fundido de vuelta a la urna | Reflexión | — |

**Texto en pantalla (en edición):** "4 oct" (esc. 1), "27 años · 4 a 1" (esc. 2), "580 días · 2021" (esc. 3), "2022" (esc. 4), "47 detenidos" (esc. 6). Rótulos neutros, sin nombres sobre los dibujos.
**Sonido (2):** un golpe seco de mazo sobre madera (esc. 2) y murmullo de escuela con una cadena (esc. 6). Silencios y cortes secos, en montaje: **un silencio de un segundo antes de la escena 5** (la pregunta).
**Movimiento (Blender, sin modelo de video):** empuje lento; en la escena 5 el empuje avanza hacia el pedestal vacío. Formato y pasos de [[Blender editing]] con `W, H = 1080, 1920`.

## Prompts (P4: pendiente de aprobación)

**Bloque de estilo (en positivo, se pega al final de cada prompt de imagen):**

```
Detailed industrial design concept sketch on warm off-white paper, vertical 9:16 sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat cool-grey marker fills in several tones, and a single copper-orange marker accent on the one important element. Technical-drawing feel with blank dimension lines and arrowheads, empty numbered callout circles, and plain unmarked surfaces. A hand-drawn design sheet, with the subject in the upper two thirds and open paper at the bottom.
```

**Imágenes** (modelo `black-forest-labs/flux-2-klein-4b`, `aspect_ratio` 9:16, una referencia de `_canal/estilo/` elegida en P5; `e5` recibe además `e2`, `e3` y `e4` como referencias solo si P5 muestra que los objetos no se mantienen: son 3 referencias extra, ≈ $0,045 más):

| Id | Prompt (antes del bloque de estilo) |
| --- | --- |
| `e1` | A cardboard ballot box with a slot in close foreground on a table, a row of drawn voter silhouettes behind it, seen from slightly above; the slot is the copper-orange accent. |
| `e2` | A judge's gavel resting on a round sound block, a thick stack of bound pages tied with ribbon beside it, seen from a slightly high angle; the gavel is the copper-orange accent. |
| `e3` | A thick case file on a desk with its wax seal broken in two and loose pages fanning out, seen from above; the broken seal is the copper-orange accent. |
| `e4` | A closed folder tied with a ribbon, a magnifying glass resting on it, and an open empty envelope beside it, seen from above; the ribbon is the copper-orange accent. |
| `e5` | Four plinths in a row seen from the front and slightly above: on the first a judge's gavel, on the second a case file with a broken wax seal, on the third a ribbon-tied folder with a magnifying glass, and the fourth plinth empty and in front; the empty plinth is the copper-orange accent. |
| `e6` | A school voting booth at the end of a corridor, a barricade of sandbags and a chain stretched across the foreground, seen from a high angle; the chain is the copper-orange accent. |

**Voz** (`qwen/qwen3-tts`, `voice_clone`, **sin diseñar una voz nueva**): referencia = `helio-e1-voz-qwen-design-v1.wav` (voz del canal, perfil B, ya aprobada) con su texto como transcripción. `style_instruction`: *speak at a brisk, fluent, steady pace in a calm, informative documentary tone*. Una prediction por escena (7) con el texto exacto del guion. Archivos: `brasil-e<n>-voz-qwen-clone-v1.wav`.

**Sonido** (`zsxkib/mmaudio`, texto a audio, 2 s cada uno; **confirmar en *API* que acepta solo texto**):
- `brasil-e2-mazo-v1`: *a single wooden gavel strike on a sound block in a large quiet courtroom, dry, short natural echo.*
- `brasil-e6-escuela-v1`: *echoing school corridor with distant voices and footsteps, a metal chain rattling once, steady and tense.*

## Presupuesto en dólares (tope = base × 1,2)

| Categoría | Modelo | Cantidad base | Precio unitario | Subtotal | Tope |
| --- | --- | --- | --- | --- | --- |
| Voz | `qwen3-tts` | 7 (≈ 944 caracteres) | ≈ $0,02 por 1.000 caracteres | **≈ $0,02** | 8 predictions |
| Sonido | `mmaudio` | 2 | ≈ $0,005 | **≈ $0,01** | 2 |
| Imagen | `flux-2-klein-4b` | 6 | ≈ $0,015 + referencia de entrada (≤ $0,015) → **≈ $0,03** | **≈ $0,18** | 7 (≈ $0,21) |
| **Total** | | | | **≈ $0,21** | **≈ $0,30** |

- **Prueba P5 (parte del total, no extra):** voz de la escena 1 + imagen `e1` + sonido de la escena 5 ≈ **$0,04**.
- Supuestos sin confirmar: el precio de klein (agregadores, no Replicate) y cuánto cobra por la referencia. Si P5 muestra otra cifra, se avisa antes de seguir.
- Sin miniatura (Shorts) y con las escenas 6 y 7 reutilizando imágenes: ahorro ≈ $0,09 frente al flujo anterior.
- Para comparar: Helio costó ≈ $2 en 32 predictions.

## Qué espera tu decisión

1. **P1–P3 + P4a:** ¿el nuevo foco, el texto v3 (léelo en voz alta) y las reglas de rigor (condenado ≠ investigado; sin atribuir la coacción)? Brasil *podría* cerrar embajadas, no cerró.
2. **P2:** los dos datos débiles (memorando de R$ 352 M; fecha de la elección). Si quieres, los verifico con más búsquedas antes de grabar; no cuesta nada de Replicate.
3. **P4:** el presupuesto de ≈ $0,21 (tope ≈ $0,30) y los prompts. Sin tu OK no genero nada.

## Registro de predictions

Formato: `escena · categoría · modelo · seed · estado · URL`.

| Escena | Categoría | Modelo | Estado | Predicción |
| --- | --- | --- | --- | --- |
| 1 | voz | `qwen3-tts` clon | ⏳ P5 | [smemm5tpc9rmr0d1092at9z238](https://replicate.com/p/smemm5tpc9rmr0d1092at9z238) |
| 1 | imagen `e1` | `flux-2-klein-4b` (referencia `estilo-motor-v1`) | ⏳ P5 | [sm9cb1swv9rp60d1092vhzvt5r](https://replicate.com/p/sm9cb1swv9rp60d1092vhzvt5r) |
| 2 | sonido | `mmaudio` ×2 | ❌ falló (sin audio; probablemente no se cobra) | sin id (error en solo texto) |
| 2 | sonido | `sepal/audiogen` | ⏳ P5 | [34ceyecda9rmr0d1092vf5nng8](https://replicate.com/p/34ceyecda9rmr0d1092vf5nng8) |

**Predictions: 3 útiles + 2 fallidas de 8 previstas en el tope.**

## Resultado de la prueba P5 (3-oct-2026)

Archivos en `Media/Brasil y embajadas - 60 segundos/` (`voz/`, `ilustraciones/`, `audio/`).

| Prueba | Resultado | Lo que no pude comprobar |
| --- | --- | --- |
| **Voz, escena 1** (`brasil-e1-voz-qwen-clone-v1.wav`) | 5,68 s; voz útil 4,91 s; **≈ 122 palabras por minuto** en esta frase de 10 palabras (con 1 pausa entre frases) | **El timbre** y si suena igual a la de Helio |
| **Imagen `e1`** (`brasil-e1-v1.png`, 768×1360) | **Estilo y vertical bien**: papel crema, tinta y marcador, acento cobre en la ranura de la urna, siluetas sin rostro. **Defectos:** cifras de cota ilegibles (garabatos), recuadro vacío abajo (cartucho), y la composición ocupa todo el cuadro (urna al centro, votantes arriba) | Si lo aceptas visualmente |
| **Sonido, escena 2** (`brasil-e2-mazo-v1.wav`) | 2,0 s, **un solo golpe a los 0,76 s con caída rápida**, que coincide con "un golpe de mazo". 16 kHz mono (calidad baja) | **Cómo suena** |
| **`mmaudio`** | **Falló en solo texto** ("Input Tensor has to be 2D"); no sirve sin video | |

### Tres decisiones para ti (P5)

1. **Ritmo de la voz:** si todo el guion sale a ≈ 122 a 136 palabras por minuto, **las 153 palabras duran 68 a 75 s, no 59**. En Helio fueron 156. Opciones: (a) generar el guion entero (≈ $0,02) y medir antes de decidir; (b) pedir un ritmo más rápido (`style_instruction`) y volver a medir; (c) recortar el guion (aprobado: tendría que reabrirse P3). **Recomiendo (a) y luego (b).**
2. **Look de la imagen:** ¿lo apruebas? Los garabatos de cota y el cartucho vacío se pueden tapar en el montaje (encuadre un poco más cerrado y un velo de papel), no se vuelven a generar.
3. **Sonido:** `mmaudio` queda descartado; `audiogen` sale a 16 kHz. Si no te convence, la alternativa sería otro modelo (a probar solo con tu OK).

**Gasto de la prueba (estimado):** voz ≈ $0,002 · imagen ≈ $0,03 (klein + 1 referencia; **precio sin confirmar en Replicate**) · sonido ≈ $0,011 · **≈ $0,04**, igual que lo previsto.

## Generación P6 (3-oct-2026)

**Guion v4 (123 palabras, 765 caracteres)** adaptado al ritmo de la voz, por pedido del usuario: ver [[Script - Brazil and embassies (60 seconds)]].

| Categoría | Archivos | Resultado |
| --- | --- | --- |
| **Voz 7/7** | `brasil-e1..e7-voz-qwen-clone-v1.wav` | Voz útil **55,8 s**; con ≈ 3 s de silencios entre escenas el corte queda en **≈ 58–59 s**. Ritmos por escena: 122, 116, 99, 156, 137, 139 y 153 palabras por minuto (las escenas 2 y 3 son lentas por los dos puntos; **no pude oír el timbre**) |
| **Imagen 6/6** | `brasil-e1..e6-v1.png` y `brasil-e5-v2.png` (usar la v2) | `e1`, `e2`, `e3` bien. `e4` ✅ con reservas: parece un regalo con lazo. `e5-v2` ✅: cuatro pedestales, el cuarto con un bloque cobre (no vacío) y pequeño en el cuadro. **`e6` ⚠️:** abajo, sacos con una cadena cobre (bien); arriba, **piezas de máquina en un pasillo** (contaminación de la referencia de estilo). Los 768×1360 px se escalan a 1080×1920 |
| **Sonido 2/2** | `brasil-e2-mazo-v1.wav`, `brasil-e6-escuela-v1.wav` | Mazo: un golpe a 0,76 s. Escuela: 4 s (pedí 2, subí a 4) |

### Predictions y costo (estimado)

| Categoría | Predictions | Costo |
| --- | --- | --- |
| Voz | 7 (1 de P5 + 6) | ≈ $0,02 |
| Imagen | 7 (6 + 1 reintento de `e5`) | ≈ $0,21 (con referencia, ≈ $0,03 c/u, **sin confirmar**) |
| Sonido | 2 (+ 2 fallidas de `mmaudio`) | ≈ $0,02 |
| **Total** | **16 útiles** | **≈ $0,25**; tope ≈ $0,30 (imagen: 7 de 7) |

**Se llegó al tope de imágenes (7).** Rehacer `e6` pasa del tope y necesita tu OK (≈ +$0,03). Alternativa sin costo: en el montaje se encuadra solo la mitad inferior de `e6` (sacos y cadena).

## Montaje (3-oct-2026)

**Render r1:** `Media/Brasil y embajadas - 60 segundos/render/brasil-60s-9x16-r1.mp4`, **59,17 s**, 1080×1920, 24 fps, H.264 y AAC (con pista de audio). Script: `Sistema/scripts/build_brasil.py`.

| Qué | Cómo |
| --- | --- |
| Voz | 7 tomas con silencio de 0,2 s entre escenas y **0,7 s antes de la escena 5** (la pregunta) |
| Imagen | Una por escena, "pasar la hoja" entre escenas y empuje lento del 6 %. La escena 7 vuelve a `e1` |
| Recortes | Se quita por abajo el dibujo secundario (libro, sobre) de `e2`, `e3`, `e4`, `e5`; el hueco lo llena el papel. `e6`: solo la franja de sacos y cadena, subida fuera de la zona de subtítulos |
| Texto en pantalla | `27 años · 4 a 1` (esc. 2), `580 días · 2021` (esc. 3), `2020 → 2022` (esc. 4), `47 detenidos` (esc. 6), en DejaVu Sans Bold sobre el papel, a la altura del 30 % desde abajo. **Se quitó "4 oct"**: caía sobre la urna |
| Sonido | Mazo en el segundo 3,0 de la voz 2 (**estimado, no medido**: puede no caer justo en "condenado"); escuela con cadena bajo la escena 6 |
| Textura | Viñeta suave y grano, como en Helio |

### Qué verifiqué y qué no

- ✅ Duración (59,17 s), resolución y pistas (video y audio), por las cabeceras del mp4.
- ✅ Siete fotogramas clave revisados: recortes sin borde visible salvo `e6` (tenue), texto legible y fuera de la zona de subtítulos.
- ❌ **No puedo ver ni oír el video completo.** Sin comprobar: timbre y ritmo de la voz, volumen del mazo y la escuela frente a la voz, si el golpe cae en "condenado", y los fundidos entre escenas.

### Qué espera tu decisión (P7)

1. **Mira y escucha** el mp4. ¿Ritmo, voz y sonido bien?
2. **Defectos de imagen que conviene que juzgues:** `e4` parece un regalo con lazo; `e5` tiene el cuarto pedestal con un bloque cobre (no vacío); `e6` tiene un borde tenue del recorte.
3. **Antes de publicar (P8):** confirmar la fecha de la primera vuelta en el TSE, la fuente original del memorando de R$ 352 M (ya no está en el guion) y si EE. UU. y Australia reabrieron; título, descripción con fuentes y declaración de IA.

## Montaje r2 (3-oct-2026): frases cortadas, corregido

**Feedback:** "phrases cut mid sentence, voice clip cut before they end, adjust the render, you can make it longer".

- **Causa (error mío, no del audio):** en Blender, `frame_offset_start` también adelanta el inicio visible de la tira. Las tomas de voz tienen ≈ 0,5 a 0,7 s de silencio inicial, así que cada voz arrancaba tarde y terminaba ≈ 0,6 s antes. Los archivos de voz **terminan en silencio** (comprobado: energía 0 en los últimos 80 ms).
- **Arreglo:** la tira se crea `ini` segundos antes, de modo que lo audible empieza en `abs` y termina en `abs + dur`, y hay una `assert` que lo comprueba. La cola pasó de 0,08 a 0,25 s.
- **Ritmo, más largo:** silencios entre escenas 0,45 a 0,5 s (antes 0,2), **1,2 s antes de la pregunta** (antes 0,7), 0,5 s de entrada y 1,2 s de cola. Dura **63,37 s** (antes 59,17), todavía un Short.
- **Verificado:** cada tira cubre toda la voz útil de su archivo, más 0,25 s de cola (p. ej. voz 2: se oye 0,62–8,71 s y la voz útil es 0,69–8,45 s). **No pude medir el audio mezclado** (la mezcla en segundo plano sale vacía): lo confirmas al escuchar.
- El texto sigue siendo el de la v4; recuperar frases de la v3 ("4 a 1", "580 días", "financiación de una película") exige generar de nuevo esas voces (≈ $0,02).

## Ilustraciones más descriptivas (propuesta v2 · pendiente de tu aprobación)

**Feedback:** "rework on the illustrations, make them more descriptive".

**Qué fallaba:** cada imagen era un objeto aislado (mazo, sello, carpeta). Contaban el *tema*, no el *mecanismo*. El estilo del canal (láminas de diseñador industrial) sirve justo para mostrar cómo funciona algo: aquí, cada imagen explica **qué pasó y cómo**, con flechas y círculos numerados vacíos. También se evitan los dibujos secundarios (se pide "una sola lámina grande") y la contaminación de la referencia `estilo-motor`: **la referencia pasa a ser `brasil-e2-v1.png`** (el mazo, que sí salió bien).

| Escena | Qué explica la lámina (v2) | Prompt (antes del bloque de estilo) | Acento |
| --- | --- | --- | --- |
| 1 | **Tres casos, tres finales** | One single large drawing filling the sheet: a cardboard ballot box in the foreground; behind it a single thick case folder from which three numbered arrows diverge to three small objects: a judge's gavel, a broken wax seal, and a closed archive box with a lid. | La urna |
| 2 | **Condena firme, 4 a 1** | One single large drawing filling the sheet: a long courtroom bench seen from the front with five identical high-backed chairs behind it; four chairs have a copper seat cushion and one chair has a grey cushion; on the bench a gavel on a sound block and a thick bound dossier tied with ribbon; numbered callout circles on the chairs. | Los cuatro cojines |
| 3 | **580 días y una anulación** | One single large drawing filling the sheet: on the left a small prison cell with a barred door standing open and a wall covered in tally marks grouped in fives; on the right a thick case file on a desk with its wax seal broken in two; a long curved arrow from the file to the open door. | El sello roto |
| 4 | **Cómo funcionaba el esquema y por qué se archivó** | One single large drawing filling the sheet: on the left five small desks in a row, each with an envelope, and dotted arrows carrying the envelopes into one open drawer of a larger desk; on the right a magnifying glass over a torn page, and a closed archive box with its lid half shut. | El cajón |
| 5 | **La pregunta** | One single large drawing filling the sheet: four identical stone plinths in a row; on the first a gavel, on the second a case file with a broken wax seal, on the third a closed archive box with a magnifying glass, and the fourth plinth topped by a large hand-drawn question mark. | El signo de pregunta |
| 6 | **Votos bajo presión: cambio de ubicación** | One single large drawing filling the sheet: an isometric view of a small neighbourhood block; on one side a school with a sandbag barricade and a chain across its entrance, on the other side a second school across the street; a large curved arrow carries a cardboard ballot box from the barricaded school to the second school. | La cadena |

**Reglas de rigor:** sin rostros, sin banderas ni letras; los números y años siguen yendo en edición.

**Presupuesto (en dólares):** 6 imágenes × ≈ $0,03 (klein + 1 referencia, **precio sin confirmar**) = **≈ $0,18**; **tope: 7 imágenes (≈ $0,21)** con un solo reintento. Gasto acumulado del video: ≈ $0,25 + $0,21 = **≈ $0,46** (el tope inicial era $0,30: **pasa del tope, necesita tu aprobación**).

**Aprobado por el usuario ("adelante") y ejecutado: ver *Láminas v3*.** (Plan original: genero en serie, miro la hoja de las seis juntas, rehago como máximo una, muevo las v1 a `_descartes/`, actualizo recortes del montaje (con láminas completas ya no hace falta recortar) y renderizo la r3.)

## Láminas v3 (3-oct-2026): ilustraciones más descriptivas

**Aprobado:** "adelante" (≈ $0,21, tope de 7 imágenes). Generadas en serie con `brasil-e2-v1.png` como referencia de estilo: `brasil-e1-v3`, `e2-v4`, `e3-v3`, `e4-v3`, `e5-v3`, `e6-v3` (7 predictions: 6 + 1 reintento de `e2`).

| Escena | Qué muestra | Resultado |
| --- | --- | --- |
| 1 | Urna y un expediente con mazo, sello y caja de archivo | ✅ pero **las flechas numeradas no salieron**: los tres objetos están sobre el expediente |
| 2 | Banco de tribunal con 5 sillas | ✅ en el **reintento**: **4 cojines cobre y 1 gris** (el primero salió 3 y 2) |
| 3 | Celda abierta con marcas de días, flecha al expediente de sello roto | ✅ |
| 4 | Escritorios con sobres hacia un cajón, lupa sobre hoja rota y caja de archivo | ✅ |
| 5 | Mazo, expediente, caja con lupa y pedestal con signo de pregunta | ✅ |
| 6 | Dos escuelas, barricada con cadena y una flecha que lleva la urna | ✅ |

**Gasto del video: ≈ $0,25 + 7 × $0,03 ≈ $0,46** (tope original $0,30; el exceso lo aprobó el usuario). Las versiones anteriores están en `ilustraciones/_descartes/`.

**Montaje r3:** sin recortes (las láminas v3 no traen dibujos secundarios), acercamiento base entre 0,96 y 1,0 para que no se corten los bordes, dibujo subido 90 px y texto en pantalla al 27 % de la altura. Papel de fondo medido de nuevo. **No he visto el video completo**; revisé cinco fotogramas clave.
