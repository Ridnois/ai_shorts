---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v1 · feedback de los 4 videos comprimido en reglas
tags: [investigación, youtube, guion, guías, feedback]
---

# Guías para nuevos guiones

← [[Canal YouTube]] · [[Flujo rápido]]

**Léela entera antes de escribir un guion.** Es el feedback de los cuatro videos ([[Imanes y geopolítica - Estado]], [[Helio y poder - Estado]], [[Brasil y embajadas - Estado]], [[Queque - Estado]]) reducido a reglas. Cada regla dice de dónde sale. El detalle de producción (modelos, precios, presupuesto) está en [[Flujo rápido]].

> **Qué es buen contenido (definición del usuario):** el que, *aun sabiendo que es IA, puedes disfrutar y seguir viendo*; informativo o absurdo, pero entrega su mensaje. Meta del canal: **aprendizaje narrado**, educar y entretener. Referencias: *Sleep on Physics*, *Sleep on Science*. Detalle: [[YouTube con IA - guía de contenido de calidad]].

## 1. Guion

**Oficio y estructura de un Short: [[Guía de narración]]** (fuente de verdad). Esta tabla es el feedback que la originó.

| # | Regla | Viene de |
| --- | --- | --- |
| 1.1 | **La tensión viene del contexto, no de la espera.** Un dato concreto que muestra qué está en juego tensa más que una pausa. | Imanes: «lenta, como forzando la curiosidad» |
| 1.2 | **Todo gancho se resuelve dentro de su escena o la siguiente**, y responde las tres: **qué es**, **por qué pasó**, **qué significa**. | Imanes: «¿faltaba un imán? ¿por qué? ¿qué significa?» |
| 1.3 | **Simplificar no es quitar el porqué.** Si hay que recortar, se sacrifica el detalle lateral (fechas, nombres, cifras secundarias), no la cadena causa → efecto. | Imanes |
| 1.4 | **Hacer pensar.** Se entrega una idea que el espectador cierra solo (p. ej. «un caso que cae por el procedimiento nunca llega a juzgar los hechos»; «si sale mal, no es la receta: es un paso»). Una lista de datos no basta. | Brasil (feedback 2) |
| 1.5 | **Enfocarse en causas, no en listas.** Cada paso o caso lleva su porqué en la misma frase. | Queque |
| 1.6 | **Ritmo ágil:** frases cortas llenas de información, sin pausas de relleno. El silencio se usa **una vez, con intención** (p. ej. 1,2 s antes de la pregunta central). | Imanes, Brasil |
| 1.7 | **Una idea nueva por escena.** Si una escena explica dos cosas, se parte. | Imanes |
| 1.8 | **Se escribe para el oído y se lee en voz alta.** Lo que suena forzado o dramático se reescribe. | Imanes |
| 1.9 | **Cifras y fechas van en pantalla, no en la voz** (`180 °C`, `27 años · 4 a 1`). | Brasil, Queque |

### Rigor

- **Cada cifra con fuente y fecha**; lo débil queda fuera del guion o atribuido («según…»). Verbos con «puede» / «podría» cuando la fuente es débil. Revisar la premisa del pedido: Brasil *advirtió que podría* cerrar embajadas, no las cerró.
- **Condenado ≠ acusado ≠ investigado ≠ archivado.** Se usan las palabras exactas del fallo; mismo tratamiento para todos los personajes; nadie recibe adjetivos.
- **Si las fuentes se contradicen** (cantidades de la receta), se publica como «receta base de varias fuentes» y se dice en la descripción.
- **Enfoque del pedido:** si el usuario fija foco («candidatos, sus delitos y cómo se sabotea la elección»), se respeta; no se amplía.

### Duración y ritmo

- Un Short (9:16) cabe en ≈ 60 s, pero **«más largo está bien»** si hace falta (63 a 81 s funcionaron). Sin acelerar la voz para que quepa.
- **Se adapta el guion al ritmo de la voz, o se usa un modelo con `speed`**; no se recorta a ciegas ni se regenera. Planificación: ≈ 150 palabras por minuto con `elevenlabs/v3` a `speed` 0,95 (Queque: 197 palabras → 77,6 s). Se **mide con el guion completo**, no con una frase (una frase de prueba dio 122; el guion entero, 156).
- Gancho en los **primeros 3 s**, con la imagen más fuerte.

### Lista de comprobación antes de P3

- [ ] ¿Cada gancho responde qué es, por qué y qué significa?
- [ ] ¿Hay pausa o frase que existe solo para crear suspenso?
- [ ] ¿Alguien que no sabe nada entiende la cadena causa → efecto **sin ver las imágenes**?
- [ ] ¿Deja una idea que hace pensar, sin reproche ni sermón?
- [ ] ¿Leído en voz alta: dónde se arrastra?
- [ ] ¿Cada afirmación está sostenida o atribuida?

## 2. Ilustraciones: `flux-kontext-pro` + foto real

Estilo, método y plantilla de prompt: [[Estilo visual - miniaturas de plastilina]]. Feedback de origen: Brasil («no hay relación entre las ilustraciones y el contenido… el prompt se volvió genérico y se olvidó del research»); Queque («Horrible illustration… busca queque casero para que entiendas»).

| # | Regla |
| --- | --- |
| 2.1 | **Cada imagen muestra un estado concreto de la historia** (qué pasó, quién, hacia dónde), no un objeto suelto. El antes y después son dos imágenes. |
| 2.2 | **El prompt hereda el research:** lleva la frase de la narración, el objeto con sus partes reales y el único acento cobre-naranja ([[Prompt - guía de generación por escena]]). |
| 2.3 | **Ficha del objeto real y foto de referencia antes de escribir prompts.** «Baking dish» genera un molde de pan; la foto real, recortada y con la orientación del resultado, fija la forma. Una sola `input_image`; licencia y atribución en el Estado. |
| 2.4 | **Un punto focal grande;** el resto, apenas insinuado. |
| 2.5 | **Sin texto, cifras ni rostros dentro de la imagen** (se ponen en edición). Prompts **en positivo**. |
| 2.6 | **Conteos y partes se verifican a ojo** (3 sillas en vez de 4). Plano simple y nombrar partes y cantidades. |
| 2.7 | **Una imagen «casi bien» se acepta.** Lo que se arregla en edición no se regenera. Un reintento por imagen; si falla dos veces, se acepta, se encuadra o se quita la toma. |
| 2.8 | **Vertical 9:16, zona segura:** sujeto entre el 15 % y el 60 % de la altura; nada clave en el tercio inferior ni en el 6 % superior. |
| 2.9 | **El resultado tiene que ser digno de verse:** si las imágenes no se entienden sin la voz, no están listas. |

## 3. Voz y sonido

- **Voz: `elevenlabs/v3`**, `Roger`, `es`, `speed` 0,95, `previous_text` / `next_text` para la entonación. «Elevenlabs is better.» (`qwen3-tts` solo como alternativa barata, sin control de velocidad.) **Yo no puedo oír la diferencia: la voz la elige el usuario** en P5, y no se cambia después.
- **Una toma por escena, con el texto exacto del guion.** Las frases nunca se cortan (ver §4).
- **Sin efectos de sonido por defecto.** `audiogen` suena a 16 kHz y el usuario rechazó el primero («no batidora sound»); solo se piden si el guion los exige. Pendiente del feedback de Brasil: «el audio está bien, la calidad podría mejorar bastante y agregar dinamismo» → probar otro modelo de sonido **solo con aprobación**.
- `mmaudio` no sirve en solo texto. `stable-audio-2.5` queda fuera por precio.

## 4. Montaje

- **Nunca se corta una frase de voz.** En Blender, `frame_offset_start` también adelanta el inicio visible; la tira se crea `ini` segundos antes y una `assert` comprueba que lo audible empieza y termina completo, con cola de 0,25 s (error de la r1 de Brasil).
- **Silencios:** 0,45 a 0,5 s entre escenas; 1,2 s antes de la pregunta central; 0,5 s de entrada y 1,2 s de cola.
- **Texto en pantalla:** tarjeta de etiqueta sobria (barra cobre, etiqueta espaciada, título en negrita), máx. 4 palabras: [[Estilo de texto en pantalla]]. Entre el 22 % y el 33 % desde abajo.
- **Láminas:** una cada ≈ 4 s, fundido cruzado dentro de la escena y «pasar la hoja» entre escenas; acercamientos 0,96 a 1,0, empuje lento del 6 %. Los cambios de lámina deberían caer en la palabra que explican (aún no sincronizados con cada palabra).
- **Se dice lo que no se verificó:** no se ve ni oye el video completo, solo fotogramas y cabeceras; la puerta P7 es del usuario.
- **Antes de poner un símbolo en pantalla** (→, ≈), comprobar que la tipografía lo tiene: Noto Sans Display Bold no tiene «→» y salía como un cuadro (Potencias, r1). Se usa «·» o «a».
- Detalles: [[Montaje en Blender]], [[Transiciones y efectos]].

## 5. Proceso, costos y archivos

- **Regla madre: no se genera ningún medio antes de P4** (prompts + presupuesto aprobados, en dólares). Cada aprobación se escribe en el Estado del video. Si el usuario **delega** («sigue tú hasta el render»), se anota y se ejecuta sin parar, pero se respeta el tope.
- **Costo:** al usuario le preocupa («se está poniendo caro, demasiada prueba»). Tope por categoría = base × 1,2; una prueba mínima en P5; series de ≤ 10 llamadas, **en serie**, nunca en paralelo; el prompt se corrige antes de reintentar. Pasar del tope exige aprobación.
- **Las imágenes que se generan son las del corte**, 1 por toma por defecto.
- **Las investigaciones van aparte de los guiones** (modelos, estilos, referencias): notas en `Investigación/`, pruebas en `Media/_canal/investigacion/`, costo separado. Una nota de video solo enlaza la conclusión.
- **No se mueven carpetas de otros videos.** Los archivos llevan el prefijo de su video (Obsidian resuelve los embeds por nombre). Los descartes van a `_descartes/`.
- **Notas en el vault, nunca artifacts ni Claude Docs.**
- **Sin miniatura en Shorts.** Descripción con fuentes, fecha de corte y declaración de IA.

## 6. Pendientes abiertos

- [ ] **Calidad y dinamismo del sonido** (feedback de Brasil): sin solución probada.
- [ ] **Cambios de lámina sincronizados con la palabra**, no solo con la escena.
- [ ] Probar el estilo de texto en un tema político (dato + fuente) y definir 16:9.
- [ ] Confirmar el precio de `flux-kontext-pro` en Replicate; probar `match_input_image` y una escena sin objeto ([[Estilo visual - miniaturas de plastilina]]).
