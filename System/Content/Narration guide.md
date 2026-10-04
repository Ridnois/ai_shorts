---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · oficio de narración corta de historia + reglas del feedback de 4 videos
tags: [investigación, youtube, guion, narración]
---

# Guía de narración

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Production process]] · [[Channel voice]] · [[Visual style - plasticine miniatures]] · [[YouTube with AI - quality content guide]]

Se aplica en la etapa 2 (guion) y la 3 (dirección) del [[Production process]], y se comprueba antes de P3. **Es la fuente de verdad para escribir un guion**; el resto de notas la enlazan.

Base: oficio de dirección y guion de cortos (un gancho en los primeros segundos, una sola idea, estructura planteamiento → conflicto → resolución, imagen antes que exposición) ([fuente](https://glcoverage.com/2024/12/25/tips-for-writing-short-film/), [fuente](https://subscribr.ai/youtube-strategy/scripting-youtube-shorts-engagement)), más el feedback de los cuatro videos del canal. **Se descarta el cierre con llamada a la acción** que recomiendan las guías de Shorts: aquí se cierra con una idea.

## 1. Una historia, una pregunta

El video responde **una pregunta**, formulada en una frase antes de escribir («¿por qué se detuvo una fábrica por un imán?»). Todo lo que no ayude a responderla, fuera. Si el tema pide dos preguntas, son dos videos.

## 2. Estructura de un Short (≈ 60 a 80 s, 6 a 8 escenas)

| Escena | Función | Palabras |
| --- | --- | --- |
| 1 · **Gancho** (0 a 3 s) | Un momento concreto y específico, ya empezado, con lo que está en juego. Sin saludo, sin «en este video», sin «¿sabías que…?» | 12 a 20 |
| 2 · **Contexto mínimo** | Qué es y por qué importa, justo lo que hace falta para entender la frase siguiente | 20 a 30 |
| 3 a 5 · **Cadena causal** | Tres eslabones. Cada uno nace del anterior con **«porque» o «por eso»**, nunca con «y luego» | 20 a 30 c/u |
| 6 · **Giro** | Lo que cambia cómo se entiende todo (hacia el 60 a 70 % del video) | 20 a 30 |
| 7 · **Cierre** | Responde la pregunta y deja **una idea que el espectador cierra solo**; una o dos frases; sin moraleja ni resumen ni llamada a la acción | 15 a 25 |

Presupuesto: ≈ 150 palabras por minuto con `elevenlabs/v3` a `speed` 0,95 ([[Channel voice]]); 150 palabras ≈ 60 s, 200 ≈ 80 s. **Una toma de voz por escena.**

## 3. Reglas de oficio

1. **El gancho es un titular, no un saludo.** Un hecho concreto que muestra qué está en juego («En mayo de 2025, una línea de montaje en Chicago dejó de moverse») gana a una pregunta genérica. El contexto da la tensión; la espera no.
2. **Todo gancho se resuelve en su escena o la siguiente**, y responde las tres: **qué es**, **por qué pasó**, **qué significa**. No se deja una pregunta abierta solo para sostener la curiosidad.
3. **Causa → efecto, no lista.** Cada eslabón lleva su porqué en la misma frase. «Porque / por eso / pero» une; «y luego» enumera. Si hay que recortar, se sacrifica el detalle lateral (fechas, nombres, cifras secundarias), **nunca el porqué**.
4. **Lo concreto gana a lo abstracto.** Un objeto, un lugar, una cifra por idea. Un tornillo de 3 cm cuenta más que «una dependencia crítica». Los datos son pocos y van al final de la frase, donde la voz los marca.
5. **Un hilo que vuelve.** Un objeto o personaje que reaparece (el imán, la fuente de vidrio) ordena el relato y permite cerrar con un eco del gancho. Ese objeto es además la **foto de referencia** de la imagen ([[Visual style - plasticine miniatures]]).
6. **Cada escena sube la apuesta o cambia la lectura.** Si una escena solo informa, se funde con otra o se corta. **Una idea nueva por escena.**
7. **Hacer pensar.** El final entrega una idea, no un dato («un caso que cae por el procedimiento nunca llega a juzgar los hechos»; «si sale mal, no es la receta: es un paso»), sin reproche ni sermón.
8. **Se escribe para el oído y se lee en voz alta.** Frases de 8 a 16 palabras, una idea cada una, verbo activo y concreto; sin paréntesis ni subordinadas encadenadas. Un solo tiempo verbal en todo el video (presente histórico: «En 1973, un barco llega…»). Si suena forzado o dramático al decirlo, se reescribe.
9. **Ritmo.** Frases cortas y llenas, variadas de largo. **El silencio se usa una vez, con intención** (≈ 1,2 s antes de la pregunta central); no como estilo.
10. **La voz nombra lo que la imagen no puede; la imagen muestra lo que la voz nombra.** La voz no describe la imagen. Las **cifras y fechas van en pantalla**, no en la voz ([[On-screen text style]]).
11. **Rigor.** Cada cifra con fuente y fecha; lo débil, atribuido («según…») o con «podría». Se usan las palabras exactas del fallo o del hecho y el mismo trato para todos los personajes: nadie recibe adjetivos. Se revisa la premisa del pedido. Detalle en [[Guidelines for new scripts]] §1.

## 4. Formato del guion (entrada de etapas 3 y 4)

Cada escena es una fila; así el guion alimenta directamente los prompts de [[Prompt - per-scene generation guide]]:

| Escena | Voz (texto exacto) | Palabras | Qué se ve: objeto real y foto de referencia | Texto en pantalla | Fuente |
| --- | --- | --- | --- | --- | --- |
| 1 | … | | objeto + enlace y licencia de la foto | etiqueta · título (máx. 4 palabras) | |

- **Una imagen por escena** por defecto (dos solo si el plano pide un antes y un después); cada imagen cita el segundo del guion donde se usa.
- La fila **«qué se ve» no se puede rellenar** si la escena no tiene un objeto concreto: señal de que la escena es abstracta y hay que reescribirla alrededor de una cosa.
- Si el usuario fija un foco («candidatos, sus delitos y cómo se sabotea la elección»), se respeta; no se amplía.

## 5. Comprobación antes de P3

- [ ] ¿El video responde **una** pregunta, escrita en una frase?
- [ ] ¿El gancho es un hecho concreto en ≤ 20 palabras, sin saludo?
- [ ] ¿Cada gancho responde qué es, por qué y qué significa?
- [ ] ¿Cada escena nace de la anterior con un porqué, y trae **una** idea?
- [ ] ¿Alguien que no sabe nada entiende la cadena **sin ver las imágenes**?
- [ ] ¿Hay pausa o frase que existe solo para crear suspenso?
- [ ] ¿El cierre deja una idea, sin moraleja ni llamada a la acción?
- [ ] ¿Cada escena tiene un objeto concreto con foto de referencia?
- [ ] ¿Cada afirmación está sostenida o atribuida?
- [ ] Leído en voz alta, ¿dónde se arrastra? ¿La duración, con la voz real, cabe sin acelerar?

## 6. Ejemplo: reescribir un gancho

Antes (espera): «Faltaba un imán.» → no dice qué es, por qué ni qué significa.
Después (contexto): «En mayo de 2025, una línea de montaje en Chicago se detuvo: China había exigido licencias para exportar los imanes de tierras raras que mueven los motores del auto.» → qué es, por qué y qué está en juego, en una frase.
