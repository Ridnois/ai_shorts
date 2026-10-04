---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · 4 imágenes de prueba · el estilo se logra a medias y la forma no se conserva
tags: [investigación, youtube, modelos, imagen, flux-kontext]
---

# Flux Kontext Pro con referencias: despiece de una potencia

← [[YouTube Channel]] · [[Visual style - plasticine miniatures]] · [[Fast workflow]]

Investigación general del canal, **independiente de cualquier guion**: sirve para cualquier video con piezas reales. El tema de prueba es la misma lámina que `wan-2.7-image` dibujó como un buje: el **despiece de una potencia sin rosca** (Aheadset).

> **Encargo (3-oct-2026):** *«Generate a stem image with flux-kontext-pro, use image references and show it on the research.»*

## Cómo se hizo

- **Modelo:** `black-forest-labs/flux-kontext-pro`. Entradas del esquema (leído gratis): `prompt`, **`input_image` (una sola imagen)**, `aspect_ratio` (9:16), `output_format`, `seed`, `safety_tolerance` y `prompt_upsampling`.
- **Una sola imagen de entrada, así que hice un collage** de dos referencias, unidas lado a lado en un archivo: a la izquierda una **foto real** de una potencia sin rosca, para la forma; a la derecha un **despiece simple** de la biblioteca, para la disposición.
- **Prompt:** *«Use the LEFT photo only as the exact shape reference… use the RIGHT image only as a guide for how an exploded view is laid out»* + descripción del despiece de abajo hacia arriba (horquilla, **tres** espaciadores, potencia con pinza trasera y delantera, tapa con un perno) + estilo plano vectorial con acento cobre-naranja. Texto completo en `Media/_canal/investigacion/potencia-kontext/prompt-A.txt`.
- **Costo:** **1 prediction**, [`h43qrsc3q5rmt0d10ecvy2j5cg`](https://replicate.com/p/h43qrsc3q5rmt0d10ecvy2j5cg), ≈ 5 s. Tarifa habitual de este modelo ≈ $0,04 por imagen (**de memoria, sin confirmar en la página de Replicate**). No cuenta como costo de ningún video.

## Referencias

| Referencia | Qué aporta | Licencia |
| --- | --- | --- |
| ![[ref-stem-foto-a.jpg]] | Foto real de una potencia sin rosca con tapa, pinza trasera y placa delantera | CC BY-SA 3.0 (Wikimedia Commons: [Threadless stem with hole for front brake cable](https://commons.wikimedia.org/wiki/File:Threadless_stem_with_hole_for_front_brake_cable.JPG)) |
| `ref-explosionada-bloques.jpg` (ilustración de despiece) | Disposición de un despiece | Dominio público |

Otras fotos descargadas y no usadas: `ref-stem-foto-b.jpg` (potencia con adaptador de tubo, CC BY-SA 4.0, Troy Sankey) y `ref-stem-foto-c.jpg` (potencia ajustable, CC BY-SA 3.0). Si algún día se publica una lámina derivada de una foto con CC BY-SA hay que revisar la atribución.

## Resultado

![[potencia-kontext-A-v1.png]]

**Lo que salió bien**
- **El estilo:** vectorial plano, papel crema, grises cálidos y **un solo acento cobre-naranja** (la flecha). Es la mitad que se pedía y sale limpia, sin texto ni cifras.
- **La disposición:** una columna vertical con líneas de guía discontinuas, como en el despiece de referencia.
- **Velocidad:** ≈ 5 s, frente a 14 a 21 s de `wan-2.7-image`.

**Lo que salió mal**
- **No hay potencia.** Son anillos y copas: una tapa, un aro, tres espaciadores, un aro punteado y una copa de dirección con ventanas. **Falta el cuerpo de la potencia, la pinza del manillar y el tubo de la horquilla**, justo lo que la foto de referencia mostraba.
- **El modelo copió la idea de «despiece de anillos» del collage** y siguió el texto de los espaciadores, pero ignoró la forma real. La foto, de un fondo con ladrillo y rejas, no se tradujo en geometría.
- **El acento cobre-naranja** está en la flecha y no en la pinza, como se pedía (la pinza no existe).

## Lectura

- **El estilo no es el problema.** `flux-kontext-pro` entrega el estilo plano a la primera y rápido, pero **no extrae la forma de un objeto desde una foto con fondo cuando va dentro de un collage**. El collage probablemente le restó fuerza a la foto (la segunda imagen era mucho más ancha y ocupó casi todo el cuadro).
- **Kontext está pensado para editar una imagen**, no para generar a partir de dos. Con una sola imagen de entrada, lo natural es pasar **la foto sola** y pedir *«redraw this exact stem as a flat vector illustration»*, y despiezar después.

## Ronda 2 · foto sola y tres estilos (3-oct-2026)

> **Encargo:** *«Remember on the vault that from now on we're using flux-kontext pro plus real references; generate a test image with three different illustration styles optimized for this model.»*

**Cómo se hizo (cambios sobre la ronda 1):**
- **La foto sola, recortada** a la potencia (`ref-stem-foto-a-recorte.jpg`, sin ladrillo ni reja), sin collage.
- **Prompts escritos como instrucciones de edición**, que es como Kontext funciona: *«Redraw this exact bicycle stem… Keep the exact shape and proportions… Replace the background… Remove all lettering and logos…»* + una línea de estilo. Textos en `_canal/investigacion/potencia-kontext/prompt-solo-A/B/C.txt`.
- `aspect_ratio` 9:16, una imagen por estilo. **3 predictions**: A [`d49bwxdjwxrmt0d10edsegamkc`](https://replicate.com/p/d49bwxdjwxrmt0d10edsegamkc), B [`x8ppqqek01rmt0d10edvymqw5g`](https://replicate.com/p/x8ppqqek01rmt0d10edvymqw5g), C [`59vxwgxdg1rmr0d10eg9wyhk3g`](https://replicate.com/p/59vxwgxdg1rmr0d10eg9wyhk3g). Con la ronda 1 son **4 predictions de Kontext** (≈ $0,16 si la tarifa es de ≈ $0,04; sin confirmar). La conexión se cayó a mitad de la serie: recuperé la predicción B ya terminada en lugar de repetirla, así que no se pagó dos veces.

| Estilo | Resultado |
| --- | --- |
| **A · plano vectorial** ![[potencia-kontext-A-solo-v1.png]] | **No es vectorial plano:** es una pieza 3D gris, mate, con una huella de tornillo naranja. **No parece una potencia**: es un soporte con dos orejas. La foto casi no se conservó |
| **B · plastilina** ![[potencia-kontext-B-solo-v1.png]] | **El estilo sí se logra:** arcilla gris con grietas y huellas, fondo de mesa, tapa cobre-naranja. La forma es la más cercana: una pieza en T con tapa y dos tornillos laterales, **pero con anillos de más** y sin el brazo hacia el manillar |
| **C · serigrafía** ![[potencia-kontext-C-solo-v1.png]] | **No es serigrafía:** es un render fotográfico con colores planos, sin semitono ni desajuste de capas. La **forma es reconocible** (cuerpo, pinza delantera redonda con cuatro tornillos, tapa con perno), pero **de pie** y con la tapa deformada |

### Lectura

- **Kontext respeta la composición de la imagen de entrada.** La foto tiene la potencia **horizontal** y pedí un lienzo **vertical** (9:16): el modelo la giró y la recompuso, y eso rompió la forma. En los tres casos se perdieron el brazo hacia el manillar y la relación con la horquilla.
- **De los tres estilos, solo B se reconoce como estilo.** A y C quedaron como renders: «flat vector» y «screenprint» no bastan como instrucción de edición, y el modelo conserva el aspecto de objeto 3D de la foto.
- **Los tres eliminaron el texto y el fondo**, como se pedía (la marca «ITM» desapareció).
- **Velocidad y costo:** 4 a 7 s por imagen, mucho más rápido que `wan-2.7-image` (14 a 21 s).
- **Ninguna de las tres sirve todavía como lámina del video.** Falta resolver la orientación, no el estilo.

### Qué probaría después (cada uno ≈ $0,04; **no lo hice**, necesita tu OK)

1. **`aspect_ratio: match_input_image`** (la foto horizontal, sin forzar 9:16) y encuadrar en vertical en el montaje, como se hizo con `gpt-image-1.5`.
2. **Preparar la entrada vertical:** colocar la foto recortada de la potencia, sin girarla, sobre un lienzo 9:16 en blanco o crema, para que Kontext complete el resto.
3. **Instrucción de estilo más pegada a la imagen,** en pasos: primero *«turn this photo into a clay miniature»* (B, que ya funciona) y luego edición del encuadre o el color.
4. **Plantilla de edición de ida y vuelta:** primero «redraw as a flat illustration» con un ejemplo de estilo real como segunda imagen, **pero Kontext solo admite una imagen**, así que habría que usar la ficha de estilo en texto.

## Pendiente

- [x] Estilo del canal: **B (plastilina)**, definido en [[Visual style - plasticine miniatures]] (puede vetarlo el usuario).
- [ ] Probar la entrada con `match_input_image` y un lienzo vertical preparado.
- [ ] Comparar con `wan-2.7-image` en la misma lámina y con el mismo estilo.
- [ ] Confirmar el precio de `flux-kontext-pro` en Replicate.
