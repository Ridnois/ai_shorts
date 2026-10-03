---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
aliases: [Canal YouTube]
tags: [investigación, youtube, hub]
---

# 🎬 Canal YouTube

(índice del vault)

Canal de aprendizaje narrado, hecho con IA y con el criterio de [[YouTube con IA - guía de contenido de calidad]]. Esta carpeta es el **proceso para producir videos de forma iterativa**: pasos fijos y medios generados solo después de que el usuario aprueba.

> **Regla madre:** no se genera ningún medio hasta la puerta P4 ([[Proceso de producción]]).

**Cola de ideas y estados: [[Pipeline]].**

## Para producir un video, lee solo dos notas

1. **[[Guías para nuevos guiones]]**: qué reglas de calidad aplicar (guion, ilustración, voz, montaje, costos). Es el feedback de todos los videos, comprimido.
2. **[[Flujo rápido]]**: cómo se produce (paquetes, modelos, precios, presupuesto, formato Shorts).

Más la nota `<Tema> - Estado` del video y su guion. Todo lo demás es referencia.

## Mapa

```
Canal YouTube.md
├── Sistema/
│   ├── Guías para nuevos guiones.md   ← entrada principal
│   ├── Proceso/     Flujo rápido · Proceso de producción · Convención de media
│   ├── Contenido/   Guía de narración · Voz del canal · YouTube con IA (guía de calidad)
│   ├── Visual/      Estilo visual · Estilo de texto · Prompt por escena
│   ├── Montaje/     Montaje en Blender · Transiciones y efectos
│   ├── Modelos/     Modelos del canal (precios)
│   └── scripts/     build_*.py · replicate_helper.py
├── Investigación/   notas generales de modelos y estilos, sin relación con un guion
└── Videos/          una carpeta por video: Estado, guiones, investigación
```

Un video nuevo = una carpeta en `Videos/` con su nota `<Tema> - Estado`, copiada de la plantilla de [[Proceso de producción]].

## Referencia por tema

| Tema | Nota |
| --- | --- |
| Etapas y puertas | [[Proceso de producción]] |
| Dónde se guardan los medios | [[Convención de media]] |
| Cómo se escribe | [[Guía de narración]] · [[Voz del canal]] |
| Cómo se ve | [[Estilo visual - miniaturas de plastilina]] · [[Estilo de texto en pantalla]] |
| Cómo se pide a Replicate | [[Prompt - guía de generación por escena]] · [[Modelos del canal]] |
| Cómo se monta | [[Montaje en Blender]] · [[Transiciones y efectos]] |
| Investigación de modelos | [[Investigación - Flux Kontext Pro con referencias (potencia)]] |

## Videos

| Video | Etapa | Estado | Nota |
| --- | --- | --- | --- |
| Imanes y geopolítica (38 s) | 7 · corte provisional | Primer video; se hizo antes del proceso | [[Imanes y geopolítica - Estado]] |
| Helio y poder (70 s) | 7 · r1, espera P7 | Voz, sonido, imagen y montaje | [[Helio y poder - Estado]] |
| Brasil y embajadas (Short 9:16, 63 s) | 7 · r3, espera P7 | ≈ $0,46 | [[Brasil y embajadas - Estado]] |
| Queque (Short 9:16, 81 s) | 7 · r2, espera P7 | `elevenlabs/v3` y 20 láminas `gpt-image-1.5` (≈ $1,57) | [[Queque - Estado]] |
| Potencias de bici (Short 9:16, 63 s) | 7 · r2, espera P7 | `elevenlabs/v3` y 8 láminas `wan-2.7-image` (≈ $0,26) | [[Potencias de bici - Estado]] |
