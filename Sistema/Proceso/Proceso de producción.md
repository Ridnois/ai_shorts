---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v1 · rediseño a partir del feedback del primer video
tags: [investigación, youtube, proceso, producción]
---

# Proceso de producción de un video

← [[Canal YouTube]] · [[Guía de narración]] · [[Estilo visual - miniaturas de plastilina]] · [[Prompt - guía de generación por escena]] · [[Convención de media]]

> **Operación diaria: [[Flujo rápido]]** (revisión en 5 paquetes, modelos rápidos, tope de imágenes y presupuesto en dólares). Esta nota queda como referencia de las etapas y puertas.

> **Regla madre:** ningún medio (voz, imagen, sonido, video) se genera hasta que el usuario aprueba los prompts y el presupuesto de generación (puerta 4). Todo lo anterior se hace con texto, en el vault.

Nace del feedback del primer video ([[Guion - Imanes y geopolítica (38 segundos)]], sección *Feedback final del usuario*): el proceso se improvisó sobre la marcha y se generaron medios sin pasos ni aprobaciones definidos. Aquí quedan fijos.

## Las etapas y sus puertas

Cada etapa termina en una **puerta 🚦**: el usuario revisa y aprueba antes de pasar a la siguiente. Una puerta no aprobada devuelve el trabajo a su etapa; un cambio en una etapa ya aprobada reabre las posteriores.

| # | Etapa | Qué se produce (nota en el vault) | Puerta 🚦: el usuario aprueba |
| --- | --- | --- | --- |
| 0 | **Idea** | Tema, pregunta central, para quién y por qué ahora | **P1** · el tema y la pregunta |
| 1 | **Investigación** | Hoja de afirmaciones: cada cifra con fuente y fecha; lo no verificado, marcado | **P2** · que los hechos estén sostenidos |
| 2 | **Guion** | Narración por escena, escrita para el oído, según [[Guía de narración]] | **P3** · el texto, leído en voz alta |
| 3 | **Dirección** | Plano, emoción y sonido por escena, solo texto, según [[Estilo visual - miniaturas de plastilina]] | **P4a** · los planos |
| 4 | **Prompts y presupuesto** | Un prompt por voz, imagen y sonido, y la lista de *predictions* con modelo y cantidad ([[Prompt - guía de generación por escena]]) | **P4** · prompts y presupuesto. **Desde aquí se puede generar** |
| 5 | **Pruebas** | Referencias fijas y una sola escena de cada categoría | **P5** · el look y la voz |
| 6 | **Generación** | El resto, por categoría (voz → imagen; sonido solo si el guion lo exige), con lotes pequeños | **P6** · cada categoría, por separado |
| 7 | **Montaje** | Corte en Blender ([[Montaje en Blender]]) | **P7** · el corte |
| 8 | **Publicación** | Título, miniatura, descripción con fuentes y declaración de IA | **P8** · antes de publicar |

## Cuando se pide un video nuevo

Un pedido corto ("un guion sobre los movimientos de poder alrededor del helio") arranca el proceso y **termina en la puerta P4**, no en los medios:

1. Se crea la carpeta del video en `Videos/` con su nota `<Tema> - Estado`.
2. Se hacen las etapas 0 a 4 **solo con texto**: idea y pregunta, investigación con fuentes y fecha, guion según [[Guía de narración]], planos según [[Estilo visual - miniaturas de plastilina]], y los prompts de voz, imagen y sonido, listos para pegar, con el presupuesto de *predictions* por categoría.
3. Todo queda marcado como **borrador pendiente de aprobación**; las puertas P1 a P4 las aprueba el usuario, no Claude.
4. Se entrega un resumen y se **para**. No se llama a Replicate, no se crea nada en `Media/` y no se monta nada hasta que el usuario apruebe P4 y lo pida.

## Reglas de las puertas

- **El usuario decide.** Claude propone, mide y recomienda; no aprueba en su nombre ni pasa de etapa por inercia.
- **Se muestra antes de gastar, en dólares.** En P4 se entrega el presupuesto: cuántas *predictions* por categoría, con qué modelo, **su precio** (ver [[Modelos del canal]]) y una estimación de intentos. Las imágenes de referencia de entrada también se cobran.
- **Un tope por categoría.** Si lo real se pasa del presupuesto, se avisa y se pide aprobación antes de seguir.
- **Reintentos con criterio.** Se corrige el prompt antes de reintentar y se revisa cada resultado antes de lanzar el siguiente lote; las peticiones van en serie.
- **Lotes pequeños.** Primero el mínimo que prueba la idea (P5); el resto solo después. Una imagen o una voz que no pasó la prueba no se replica ×40.
- **Qué no se genera sin puerta:** ningún archivo en `Media/`, ninguna llamada a Replicate. Las excepciones se piden explícitamente.
- **Cada aprobación queda escrita** en la nota de estado del video (fecha y qué se aprobó), para que el proceso se pueda retomar sin contexto.
- **Los descartes no se borran** hasta P8; viven en `_descartes/` ([[Convención de media]]).

## Dónde vive cada cosa

```
(raíz del vault)  ← texto, versionado en git
├── Canal YouTube.md                 índice del canal
├── Sistema/                         reglas que valen para todos los videos
└── Videos/<Tema>/                   una carpeta por video
    ├── <Tema> - Estado.md           etapa actual y registro de aprobaciones
    └── Guiones/                     versiones del guion

Media/              ← medios, solo en esta máquina (ignorado por git)
├── _canal/                          lo compartido: estilo, referencias, música
└── <Video> - <versión>/             voz · audio · ilustraciones · miniatura · render
```

## Plantilla de estado por video

Cada video lleva una nota `<Tema> - Estado` con esta tabla, que se actualiza en cada puerta:

| Etapa | Estado | Aprobado | Nota |
| --- | --- | --- | --- |
| 0 Idea | ⏳ / ✅ | fecha | |
| 1 Investigación | | | |
| 2 Guion | | | |
| 3 Dirección | | | |
| 4 Prompts y presupuesto | | | |
| 5 Pruebas | | | |
| 6 Generación | | | por categoría |
| 7 Montaje | | | |
| 8 Publicación | | | |
