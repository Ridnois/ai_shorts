---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
tags: [investigación, youtube, pipeline, hub]
---

# 🏭 Pipeline de videos

← [[Canal YouTube]] · [[Proceso de producción]] · [[Flujo rápido]]

Una **nota por idea** en `Pipeline/Ideas/`; su propiedad `estado` es la columna de la tabla. Cambiar `estado` en la tabla  es la orden; el runner hace el trabajo y deja el siguiente estado.

![[Tabla pipeline.base]]

## Estados

```
idea ──▶ construir-guion ──▶ construyendo-guion ──▶ guion-listo
                  ▲ tú              ▲ runner              │ revisas P1–P4a y P4
                                                          ▼
render-listo ◀── (montaje, a mano) ◀── ilustraciones-listas ◀── generando-assets ◀── generar-assets
                                              ▲ runner                ▲ runner            ▲ tú
                                                                                  (exige presupuesto aprobado)
```

| Estado | Quién lo pone | Significa |
| --- | --- | --- |
| `idea` | tú | Solo la nota; no pasa nada |
| `construir-guion` | **tú** (disparador) | Pide investigación, guion, dirección, prompts y presupuesto (etapas 0–4, solo texto) |
| `construyendo-guion` | runner | En curso |
| `guion-listo` | runner | Texto y presupuesto estimado listos. **Aquí revisas P1–P4** |
| `generar-assets` | **tú** (disparador) | Pide voz e imágenes. Solo corre si `presupuesto_aprobado_usd` > 0 |
| `generando-assets` | runner | Gastando en Replicate |
| `ilustraciones-listas` | runner | Voz e imágenes en `Media/`. **Aquí revisas P6** |
| `render-listo` | tú | Montaje en Blender hecho ([[Montaje en Blender]]); P7 aprobada |
| `error` | runner | Algo falló; el motivo está en la columna *Error*. Corrígelo y vuelve a poner el disparador |

## Cómo se usa (todo desde Obsidian)

El runner corre solo como servicio de usuario (`youtube-pipeline.service`, revisa la tabla cada 15 s). No hay que abrir una terminal.

1. En la tabla (vista **Esta semana**), botón **New**: escribe el título. En ≈ 15 s la nota recibe sus propiedades. Rellena `publicar` (fecha) y el tema en el cuerpo.
2. Cambia `estado` a `construir-guion` → pasa a `construyendo-guion` → `guion-listo`. Revisa.
3. Si apruebas el presupuesto, escribe la cifra en `presupuesto_aprobado_usd` y pon `generar-assets`.
4. Revisa láminas y voz (`ilustraciones-listas`); monta; pon `render-listo`.

Servicio: `systemctl --user status youtube-pipeline` · registro: `journalctl --user -u youtube-pipeline -f` · parar: `systemctl --user stop youtube-pipeline`.

## Reglas

- **El controlador vive fuera del vault**, en `~/Documents/youtube-pipeline` (repo propio). El vault solo tiene notas y la tabla.
- **No se gasta sin presupuesto aprobado** (regla madre de [[Proceso de producción]]). El tope duro es ×1,2 de `presupuesto_aprobado_usd`.
- El runner de guion **no puede llamar a Replicate** (solo lee y escribe notas); el de assets sí.
- El tope se aplica por instrucción al modelo y se comprueba **después** con `costo_real_usd`; no es un corte técnico.
- Una idea en `*-ando` (en curso) tras un corte del runner queda atascada: vuelve a poner el disparador en la tabla.
