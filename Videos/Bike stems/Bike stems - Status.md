---
type: research
created: 2026-10-03
updated: 2026-10-03
status: render r2 hecho (63,4 s) · esperando P7 · generación delegada y completa
tags: [investigación, youtube, estado, potencias, shorts]
---

# Potencias de bici · estado

← [[YouTube Channel]] · [[Fast workflow]] · [[Guidelines for new scripts]]

Quinto video del canal, **tercer Short vertical (9:16)**, pedido de 40 s y **ampliado a 60 s** (3-oct-2026). Hecho con [[Fast workflow]] y [[Guidelines for new scripts]]. Medios en `Media/Potencias - 60 segundos/`.

> **Pedido (3-oct-2026):** «la historia de las *bike tees* en 40 segundos, de los diseños más antiguos a los modernos; mostrar la evolución del manillar y, en cada evolución, el ajuste (*fitting*), las medidas y las mejoras sobre la generación anterior».

## Registro de etapas

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ✅ P1 | **3-oct-2026** · «Correct, it is about stems, potencias, tees» | «Tees» = potencias (*stems*). Pregunta: ¿cómo cambió y qué ganó y perdió cada generación? |
| 1 Investigación | ✅ P2 | 3-oct-2026 · implícita al pedir pasar a la siguiente etapa | [[Research - Bike stems]]: 24 afirmaciones y mapa de 10 tipos de montaje; **sin fuente fechada anterior a 1946** (el guion arranca en la potencia de tubo) |
| 2 Guion | ✅ P3 | 3-oct-2026 · «make it 60 seconds» | [[Script - Bike stems (40 seconds)]] (v2, **60 s**): 159 palabras, 5 escenas |
| 3 Dirección | ✅ P4a | 3-oct-2026 · «the 8 sheets» | 8 láminas, abajo |
| 4 Prompts y presupuesto | ✅ P4 | **3-oct-2026** · «i approve the budget» | ≈ $0,23 con tope ≈ $0,28 |
| 5 Pruebas | ⏭️ omitida | 3-oct-2026 · «skip image test, go direct with the illustrations for the render» | La voz tampoco se probó aparte: se generaron las 5 tomas |
| 6 Generación | ✅ P6 | 3-oct-2026 · **delegada** hasta el render | 5 voces y 8 láminas (9 predictions de imagen). Ver *Generación y montaje* |
| 7 Montaje | ✅ render r2 · ⏳ P7 | ⏳ | `render/potencias-60s-9x16-r2.mp4`, **63,38 s**, 1080×1920 |
| 8 Publicación | ⏳ no iniciada | — | Falta título, descripción con fuentes y declaración de IA |

## Dirección (vertical 9:16 · 1080×1920)

Reglas de [[Guidelines for new scripts]] §2: **una lámina grande por imagen que muestra el mecanismo**, sin texto, cifras ni rostros dentro del dibujo; foco entre el 15 y el 60 % de la altura; acento cobre-naranja en lo que cambió. Las cifras van en pantalla ([[On-screen text style]]).

| # | Escena | Qué explica la lámina | Acento |
| --- | --- | --- | --- |
| 1 | 1 Gancho (0–5 s) | **Dónde está la potencia**: vista lateral del frente de una bici, con la potencia uniendo horquilla y manillar | La potencia |
| 2 | 2 De tubo (5–14 s) | **Dos cortes de potencia de tubo, lado a lado**: a la izquierda con cuña y a la derecha con cono expansor, perno largo en ambos | La cuña y el cono |
| 3 | 2 De tubo | **Subir el manillar**: perno flojo, potencia que sube por la horquilla, con la marca de inserción mínima | La flecha de subida |
| 4 | 3 Sin rosca (14–23 s) | **Vista explosionada del Aheadset**: horquilla, espaciadores, potencia que abraza por fuera, tapa y perno | La pinza exterior |
| 5 | 3 Sin rosca | **Altura con espaciadores**: dos frentes lado a lado, uno con espaciadores bajo la potencia y otro sobre ella | Los espaciadores |
| 6 | 4 Medidas (23–32 s) | **Diámetro de la pinza**: tres centros de manillar en fila, cada uno más grueso, con la tapa de la potencia | El más grueso |
| 7 | 4 Medidas | **El largo mueve el manillar**: dos siluetas del frente de una bici, potencia larga y potencia corta, con una flecha del alcance | La potencia corta |
| 8 | 5 Cierre (32–40 s) | **Pieza integrada**: manillar y potencia de carbono en una pieza, con un corte que muestra los cables por dentro | La unión |

**Texto en pantalla (en edición):** esc. 2 `Potencia de tubo` y `Cinelli 1A · pinza de 26,4 mm` · esc. 3 `1990 · Aheadset` · esc. 4 `25,4 → 31,8 mm` y `100+ → 35–60 mm` · esc. 5 `Integrada`.
**Sonido:** ninguno (regla por defecto). **Montaje:** `build_queque.py` como base, 1080×1920, una lámina cada ≈ 4 s, «pasar la hoja» entre escenas.

## Prompts (P4: pendiente de aprobación)

**Modelo:** `wan-video/wan-2.7-image`, `size` `1152*2048`, `num_outputs` 1, **3 referencias** de la biblioteca de referencias de sketch técnico (retirada): `ref-explosionada-colt`, `ref-explosionada-bloques` y `ref-corte-recipiente-color` (en el #7, `ref-patente-mecanismo-flujo` en lugar de la última).

**Plantilla de cada prompt:** *«Use the references only as a guide to technique (line, hatching, cutaway, arrows); do not copy their objects, labels or text.»* + **contexto** + **sujeto** + **composición** + **acento** + bloque de estilo.

**Contexto común (se pega al inicio de todos):** *This sheet belongs to a 40-second explainer on how the bicycle stem, the part joining the fork to the handlebar, evolved from the quill stem to the threadless Aheadset, to larger handlebar clamps, shorter stems and integrated cockpits. Every sheet explains one mechanism.*

**Fichas de objetos reales** (se verificaron en las fuentes de la investigación; conviene mirar una foto real antes de P5):
- **Potencia de tubo:** un vástago vertical que entra en la horquilla, una extensión que sale hacia adelante en ángulo y termina en una pinza redonda para el manillar; un perno largo cruza el vástago desde arriba hasta una cuña o cono en la punta inferior.
- **Aheadset:** la horquilla sobresale por encima del rodamiento; sobre ella van anillos espaciadores, luego la potencia con una pinza lateral de dos pernos alrededor de la horquilla y una placa frontal de cuatro pernos para el manillar, y arriba una tapa con un solo perno central.
- **Manillar:** el centro es la zona más gruesa; se ensancha en comparación con los extremos.

| # | Sujeto, composición y acento (en inglés, antes del bloque de estilo) |
| --- | --- |
| 1 | One single large drawing filling the sheet: a side view of the front end of a bicycle showing the head tube, the fork, a short stem and a flat handlebar, with a long arrow pointing along the stem from the fork to the handlebar. The stem is the copper-orange accent. |
| 2 | One single large drawing filling the sheet: two vertical cutaways of a quill stem inside a fork steerer tube, side by side; the left one with a long bolt pulling a diagonal wedge at the bottom of the shaft, the right one with a long bolt pulling a conical expander; short arrows on each show it pushing outward against the tube wall; exactly two cutaways. The wedge and the cone are the copper-orange accent. |
| 3 | One single large drawing filling the sheet: a loosened quill stem rising out of the steerer tube with a tall upward arrow, a thin horizontal line on the shaft marking the minimum insertion, and the handlebar raised with it. The upward arrow is the copper-orange accent. |
| 4 | One single large drawing filling the sheet: an exploded vertical view of a threadless stem assembly, from the bottom up: the fork steerer sticking out of the headset, three thin spacer rings, a stem clamping around the outside of the steerer with two side bolts, a top cap with one central bolt; dashed alignment lines between the parts. The outer clamp of the stem is the copper-orange accent. |
| 5 | One single large drawing filling the sheet: two fronts of a bicycle side by side, on the left three spacer rings below the stem and the handlebar high, on the right the same three spacer rings above the stem and the handlebar low, with a double-headed vertical arrow between them. The spacer rings are the copper-orange accent. |
| 6 | One single large drawing filling the sheet: three handlebar centre sections in a row, each thicker than the previous, each with its stem face plate and four bolts around it, and a thin dimension line across each; exactly three bars, no more. The thickest bar is the copper-orange accent. |
| 7 | One single large drawing filling the sheet: two side silhouettes of a bicycle front end stacked vertically, the upper with a long stem and the handlebar far forward, the lower with a short stem and the handlebar closer to the rider, with a horizontal arrow between the head tube and the handlebar on each. The short stem is the copper-orange accent. |
| 8 | One single large drawing filling the sheet: a one-piece carbon road handlebar and stem seen from above and slightly from the front, a cutaway along the stem showing two thin cables routed inside it, thin leader lines ending in small arrowheads. The junction between bar and stem is the copper-orange accent. |

**Bloque de estilo (v3 del estilo visual de bocetos técnicos (retirado), se pega al final):**

```
Hand-drawn industrial design concept sketch on warm off-white paper, vertical sheet. Confident black ink and graphite linework with light visible construction lines, cross-hatching for volume, flat marker colour in cool greys with natural metal and rubber tones where the object needs them, and a single copper-orange marker accent on the one element that matters. Technical-drawing language made of straight lines, thin leader lines ending in small arrowheads, blank dimension lines, cutaway views and angular shapes. Real, recognisable bicycle parts drawn accurately. Clean paper around the subject.
```

**Voz:** `elevenlabs/v3`, voz `Roger`, `language_code: es`, `speed` 0,95 (se sube a ≈ 1,05 solo si P5 lo permite), 5 tomas, una por escena, con el texto exacto del guion. Se copia el esquema de la pestaña *API* antes de llamar.

## Presupuesto en dólares (tope = base × 1,2)

| Categoría | Modelo | Cantidad base | Precio unitario | Subtotal | Tope |
| --- | --- | --- | --- | --- | --- |
| Imagen | `wan-2.7-image` | **8** (cada una con su segundo en la tabla de dirección) | ≈ $0,02 (**sin confirmar en Replicate**) | **≈ $0,16** | 9 imágenes (≈ $0,18) |
| Voz | `elevenlabs/v3` | 5 tomas (≈ 640 caracteres) | ≈ $0,10 por 1.000 caracteres | **≈ $0,07** | 6 predictions (≈ $0,08) |
| Sonido | — | 0 | — | $0 | — |
| **Total** | | | | **≈ $0,23** | **≈ $0,28** |

- **Prueba P5 (dentro del total):** voz de la escena 1 (≈ $0,02) + imagen #4, la más difícil por tener más piezas (≈ $0,02): **≈ $0,04**.
- Reintentos: **uno por imagen**, solo si cambia el prompt; las más propensas a fallar por conteo son la **#6** (tres manillares) y la **#5** (tres espaciadores a cada lado).
- Sin miniatura (Short).
- Para comparar: Brasil ≈ $0,46 (7 imágenes), Queque ≈ $1,57 (20 láminas).

## Generación y montaje (3-oct-2026)

**Cambios sobre lo aprobado:** el guion pasó a 60 s (159 palabras); las 8 láminas y los prompts son los de arriba, con el contexto de la narración de cada escena y 3 referencias de la biblioteca externa. La lámina #2 pide «dos cortes» (cuña y cono).

| Categoría | Predictions | Costo (estimado) |
| --- | --- | --- |
| Voz | 5 (`elevenlabs/v3`, 843 caracteres) | ≈ $0,08 |
| Imagen | **9** (8 láminas + 1 reintento de la #5) = tope | ≈ $0,18 (`wan-2.7-image`, **precio sin confirmar en Replicate**) |
| Sonido | 0 | $0 |
| **Total** | **14** | **≈ $0,26**; tope aprobado ≈ $0,28 |

**Se llegó al tope de imágenes (9 de 9).** No quedan reintentos sin aprobación.

| Escena | Categoría | Modelo | Estado | Predicción |
| --- | --- | --- | --- | --- |
| 1 | voz | `elevenlabs/v3` | ✅ | [ta80qxe46srmr0d10dks711kcm](https://replicate.com/p/ta80qxe46srmr0d10dks711kcm) |
| 2 | voz | `elevenlabs/v3` | ✅ | [9erj836mz1rmw0d10dkv4mpkww](https://replicate.com/p/9erj836mz1rmw0d10dkv4mpkww) |
| 3 | voz | `elevenlabs/v3` | ✅ | [bxt5zcqcqxrmr0d10dkrzvvyhc](https://replicate.com/p/bxt5zcqcqxrmr0d10dkrzvvyhc) |
| 4 | voz | `elevenlabs/v3` | ✅ | [re77q486e1rmt0d10dmbh1za6c](https://replicate.com/p/re77q486e1rmt0d10dmbh1za6c) |
| 5 | voz | `elevenlabs/v3` | ✅ | [d1sc27ry21rmy0d10dm8amhvvr](https://replicate.com/p/d1sc27ry21rmy0d10dm8amhvvr) |
| 1 | imagen #1 | `wan-2.7-image` | ✅ | [rpb64wek49rmy0d10dmbefy4v4](https://replicate.com/p/rpb64wek49rmy0d10dmbefy4v4) |
| 2 | imagen #2 | `wan-2.7-image` | ✅ | [c846gcrx0nrmt0d10dmte8h6d4](https://replicate.com/p/c846gcrx0nrmt0d10dmte8h6d4) |
| 2 | imagen #3 | `wan-2.7-image` | ✅ | [2mr53vk8d5rmr0d10dmvn9shdw](https://replicate.com/p/2mr53vk8d5rmr0d10dmvn9shdw) |
| 3 | imagen #4 | `wan-2.7-image` | ✅ | [nfh6xnnhk1rmt0d10dmvvfhw1g](https://replicate.com/p/nfh6xnnhk1rmt0d10dmvvfhw1g) |
| 3 | imagen #5 v1 | `wan-2.7-image` | ❌ descartada (los dos frentes salían idénticos) | [yenrz99r15rmt0d10dn8ffe06w](https://replicate.com/p/yenrz99r15rmt0d10dn8ffe06w) |
| 3 | imagen #5 v2 | `wan-2.7-image` | ✅ | [ds7zb4r771rmt0d10dpaw9vfk0](https://replicate.com/p/ds7zb4r771rmt0d10dpaw9vfk0) |
| 4 | imagen #6 | `wan-2.7-image` | ✅ | [nmrbyech0nrmy0d10dnah4nwq8](https://replicate.com/p/nmrbyech0nrmy0d10dnah4nwq8) |
| 4 | imagen #7 | `wan-2.7-image` | ✅ | [809d2xz35hrmw0d10dn8j7q3yr](https://replicate.com/p/809d2xz35hrmw0d10dn8j7q3yr) |
| 5 | imagen #8 | `wan-2.7-image` | ✅ | [83gxeqtczhrmy0d10dntb4mbhm](https://replicate.com/p/83gxeqtczhrmy0d10dntb4mbhm) |

**Render r2:** `render/potencias-60s-9x16-r2.mp4`, **63,38 s**, 1080×1920, 24 fps. Script: `Sistema/scripts/build_potencias.py` (base `build_queque.py`). La voz útil suma ≈ 59 s; el resto son silencios de 0,35 s entre escenas, 0,7 s antes del cierre, 0,3 s de entrada y 0,8 s de cola. Las frases no se cortan (cada tira cubre su voz más 0,25 s). Láminas: 1, 2, 2, 2 y 1 por escena, con fundido cruzado y «pasar la hoja»; una tarjeta de etiqueta por escena ([[On-screen text style]]); sin sonido ni música. La r1 se descartó: la flecha «→» no existe en la tipografía y salía como un cuadro; ahora se usa «·».

### Qué revisé y qué no

- ✅ Duración y pistas del render; cinco fotogramas clave (láminas, tarjetas legibles, sin glifos rotos tras el arreglo; el de la escena 4 lo cambié sin volver a mirarlo).
- ❌ **No oí el audio ni vi el video completo:** timbre, ritmo, y si la tarjeta tapa algo.
- **Láminas, mirando las ocho juntas:** #1, #2, #3 y #7 explican bien. **#4:** el despiece parece un buje más que una potencia, con numeritos «(1) (2) (3)» dentro del dibujo. **#5 (v2):** la diferencia de altura se ve; la posición de los anillos es dudosa. **#6:** las tres pinzas flotan con mucho papel vacío y traen sus cotas escritas (`25.4mm`, `31.8mm`, `35mm`, correctas). **#8:** tiene un marco.
- **Rigor:** «veinticinco» en la voz es 25,4 mm; «según las marcas» en el cierre. Sigue sin fuente para antes de 1946.

### Qué espera tu decisión (P7)

1. **Mira y escucha** el mp4: ¿ritmo y voz bien? ¿Los cambios de lámina caen donde corresponde?
2. ¿Rehago la **#4** (despiece) y la **#6** (pinzas)? Ya llegamos al tope de 9 imágenes: ≈ $0,02 cada una, hay que aprobarlo.
3. ¿Los 63 s sirven, o recorto ≈ 3 s de silencios?
4. Para publicar (P8): título, descripción con fuentes (la de [[Research - Bike stems]]) y declaración de IA.
