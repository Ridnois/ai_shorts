---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v1 · definido desde la prueba B de Kontext · sin probar en un video completo
tags: [investigación, youtube, estilo, ilustración, flux-kontext]
---

# Estilo visual: miniaturas de plastilina con referencia real

← [[YouTube Channel]] · [[Fast workflow]] · [[Narration guide]] · [[Prompt - per-scene generation guide]] · [[Research - Flux Kontext Pro with references (power)]]

> **Decisión del usuario (3-oct-2026):** *«From now on we're using flux-kontext pro plus real references.»* Fija el modelo y el método. El look sale de la única evidencia: de tres estilos probados con Kontext, **solo la plastilina se reconoció como estilo** (plano vectorial y serigrafía salieron como renders), y es el look del primer video («luce bien»). **Es una elección derivada de la evidencia, no un veredicto del usuario: se puede vetar.**

**Por qué encaja:** Kontext *edita* una foto, y «conviértelo en una miniatura de arcilla» es una edición natural; conserva la forma del objeto real; y es claramente una maqueta, no una foto de un hecho ([[YouTube with AI - quality content guide]]).

## El lenguaje

| Elemento | Regla |
| --- | --- |
| **Material** | Plastilina y arcilla hechas a mano, formas redondeadas, huellas e imperfecciones visibles |
| **Escena** | Maqueta sobre una mesa, luz suave de estudio, fondo liso y cálido |
| **Color** | Arcilla gris y crema mate; **un solo acento cobre-naranja** en lo que importa |
| **Sujeto** | Un punto focal grande; el resto, apenas insinuado |
| **Personas** | Solo manos, espaldas o siluetas de arcilla; sin rostros |
| **Formato** | Vertical 9:16; sujeto entre el 15 % y el 60 % de la altura; nada clave en el tercio inferior ni en el 6 % superior |
| **Texto y cifras** | Nunca dentro de la imagen: en edición ([[On-screen text style]]) |
| **Mecanismo** | Una imagen = un estado; el antes y después son dos imágenes que enlaza el montaje |

## Cómo se produce una imagen

1. **Ficha del objeto real:** cómo se ve de verdad y qué partes no deben perderse.
2. **Foto de referencia** con licencia, **recortada al objeto y con la orientación del resultado** (vertical para 9:16; una foto horizontal en lienzo vertical se gira y deforma). Una sola `input_image`; un collage no funciona. Licencia y atribución van en el Estado del video; con CC BY-SA, revisar antes de publicar.
3. **Prompt como instrucción de edición** (plantilla abajo).
4. **Revisión a ojo** (partes que faltan, piezas de más) y **un reintento**; si falla dos veces, se acepta, se reencuadra o se quita la toma.

```
Redraw this exact {{objeto}} as a handmade plasticine clay miniature. Keep the exact shape and proportions: {{partes que deben conservarse}}. Replace the background with a plain warm tabletop. {{qué pasa en esta escena según la narración}}. The {{elemento que importa}} is in bright copper-orange clay. The {{objeto}} fills the frame, vertical composition.
Style: handmade plasticine clay miniature photographed on a tabletop with soft studio lighting, soft rounded forms, visible fingerprints and small imperfections in the clay, matte muted grey and cream clay, warm tactile stop-motion look.
```

Prompts en positivo. «Remove all lettering and logos» funcionó en la prueba; no se pide «no text» como estilo general.

**Escenas sin objeto con foto** (un lugar, una idea): se rediseñan alrededor de un objeto que sí la tenga; o se usa una foto del lugar, o una imagen ya aprobada del mismo video. Kontext solo con texto: **sin verificar** (se lee el esquema, gratis).

## Errores conocidos con Kontext

| Error | Regla |
| --- | --- |
| Pieza girada o deformada (foto horizontal, lienzo 9:16) | Entrada vertical, o `match_input_image` y encuadrar en el montaje |
| «Vectorial» o «serigrafía» salen como render | Usar plastilina |
| Faltan partes o sobran anillos | Nombrar partes y cantidades en el prompt; verificar a ojo |

## Pendiente

- [ ] Probar `match_input_image` y una entrada vertical preparada.
- [ ] Probar una escena sin objeto con el esquema real de Kontext.
- [ ] Confirmar el precio de `flux-kontext-pro` (≈ $0,04, de memoria).
- [ ] Que el usuario apruebe el look en P5 de un video completo.
