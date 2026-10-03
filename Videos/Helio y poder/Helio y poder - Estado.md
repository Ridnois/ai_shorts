---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: render r1 hecho (71,9 s) · esperando tu revisión (P7)
tags: [investigación, youtube, estado, helio]
---

# Helio y poder · estado

← [[Canal YouTube]] · [[Proceso de producción]]

Segundo video del canal, el primero que sigue el [[Proceso de producción]] completo. Se llegó a la puerta P4 solo con texto. Tras la aprobación del usuario se generó **únicamente la prueba de la etapa 5** (3 predictions). Lo demás espera P5.

## Registro de etapas

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ✅ | 3-oct-2026 · implícita | Pedido: "un guion sobre las tensiones alrededor del helio". El usuario respondió "lets do it" al paquete completo de P1 a P4 |
| 1 Investigación | ✅ | 3-oct-2026 · implícita | [[Investigación - Helio]]: 24 afirmaciones: 4 con una sola fuente o fechas dudosas (no se usan o se matizan) y 1 descartada. **Rechequear Ormuz y Ras Laffan antes de grabar** |
| 2 Guion | 🔁 reabierta | ⏳ P3 | El usuario pidió **70 s** (3-oct-2026): [[Guion - Helio (70 segundos)]], 176 palabras, ≈ 70 s. El texto de 2 minutos estaba aprobado; el recorte necesita nueva aprobación. La lectura en voz alta de P3 sigue sin confirmarse |
| 3 Dirección | ✅ | 3-oct-2026 · implícita | Planos en el estilo de estilo visual de bocetos técnicos (retirado) |
| 4 Prompts y presupuesto | ✅ | **3-oct-2026** | Decisiones: voz B (más joven y ágil), imágenes fundidas sin modelo de video; el largo pasó de 258 palabras a 176 (70 s). Presupuesto: 26 prompts base, sin cambios |
| 5 Pruebas | ✅ | **3-oct-2026** · "images and audio ok, proceed" | Voz de la escena 1 (perfil B) y toma 1 de imagen aprobadas |
| 6 Generación | ✅ | 3-oct-2026 · **implícita** al pedir el montaje | 6 voces (67,8 s de voz útil), 3 sonidos, 8 tomas × 2 fotogramas y miniatura. 32 predictions (23 de imagen, por 6 reintentos). No se pidió aprobación categoría por categoría; si alguna no te convence, se rehace |
| 7 Montaje | ✅ render r1 · ⏳ esperando P7 | ⏳ | `render/helio-70s-r1.mp4`, **71,9 s**. Detalle en [[Guion - Helio (70 segundos)]] (*Montaje*) y diseño en [[Transiciones y efectos]] |
| 8 Publicación | ⏳ no iniciada | — | Falta miniatura con título, descripción con fuentes y declaración de IA |

## Qué espera tu decisión (P7)

1. **Mira y escucha** `Media/Helio y poder - 70 segundos/render/helio-70s-r1.mp4`. Dura 71,9 s; para quedar en 70 se corta "En marzo, su precio se duplicó" (escena 4).
2. Juzga lo que no pude comprobar: el **equilibrio entre la voz y los sonidos de fondo**, el timbre de las seis voces y el ritmo.
3. Desviaciones de imagen que conviene que mires: 3a (tanques de igual altura), 5a (falta el sello), 5b (una sola mano al final) y 6 (iconos repetidos).
4. Antes de publicar: rechequear Ormuz y Ras Laffan, añadir cifras en pantalla y la miniatura con título.

## Incidencias resueltas

- **Imágenes de otro video aparecían en este guion.** Obsidian resuelve los embeds por nombre de archivo y los dos videos compartían nombres (`e1-final-v1.png`…). Todos los archivos de este video llevan ahora el prefijo `helio-`; la regla quedó en [[Convención de media]].
- **`_canal/` estaba en la raíz del vault.** Se movió de vuelta a `Media/_canal/`, donde Git la ignora. **Sigue en el historial de GitHub** (el commit automático de las 05:18 la subió): sacarla del historial requiere reescribirlo y un `push --force`, que no hice sin tu permiso.
- **Límite de ritmo de Replicate:** las peticiones en paralelo recibieron un 429; se envían en serie.

## Notas

- [[Guion - Helio (70 segundos)]]
- [[Investigación - Helio]]
- Medios en `Media/Helio y poder - 70 segundos/` (solo en esta máquina, [[Convención de media]]).
