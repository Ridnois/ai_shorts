---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v2 · reajustada con el feedback · el usuario delegó las decisiones hasta el render
tags: [investigación, youtube, guion, queque, shorts]
---

# Guion: cómo hacer un queque (Short vertical de ≈ 80 s)

← [[Queque - Estado]] · [[Investigación - Queque]] · [[Canal YouTube]] · [[Flujo rápido]] · [[Guía de narración]]

> **Formato:** Short vertical 9:16, **179 palabras**; a ≈ 135 palabras por minuto son ≈ 80 s con las pausas. El ritmo exacto se mide con la voz real y, **con un modelo de voz con control de velocidad, se ajusta la voz al guion y no el guion a la voz**.
> **Pregunta central:** ¿qué pasos deciden si un queque sale esponjoso o duro, y por qué?
> **Idea que hace pensar:** no es una lista de pasos, es una lista de **causas**: cada paso lleva su porqué (el aire, la emulsión, el gluten). Cierre: *si sale mal, no es la receta: es un paso.*
> **Datos a:** 3-oct-2026. Fuentes y discrepancias en [[Investigación - Queque]].

## Cómo se aplicó el feedback acumulado

| Feedback (de [[Brasil y embajadas - Estado]] y la [[Guía de narración]])             | Cómo se aplica aquí                                                                             |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| La tensión viene del contexto, no de la espera; todo gancho se resuelve en la escena | El gancho (*"esponjoso o ladrillo, seis pasos"*) se responde con los seis pasos, uno por escena |
| Simplificar no es quitar el porqué                                                   | Cada paso lleva su causa en la misma frase                                                      |
| Hacer pensar al espectador                                                           | Cierre: *revisa cuál de estos pasos te saltaste*                                                |
| Las frases no se cortan; el audio no se recorta                                      | Cola de voz de 0,25 s y comprobación en el montaje                                              |
| El guion se adapta al ritmo, no al revés (o se controla la velocidad)                | Modelo de voz con `speed`; 8 tomas, una por escena                                              |
| Ilustraciones descriptivas: el mecanismo, no el objeto                               | 20 láminas: cada una muestra *qué pasa dentro* (burbujas, emulsión, gluten)                     |
| Números y fechas en pantalla, no en la voz                                           | `180 °C`, `35–40 min` y los seis pasos, en edición                                              |
| Verbos con "podría"/"puede" cuando la fuente es débil                                | "Puede quedar duro" (afirmación 13)                                                             |

## Guion

#### 1 · Gancho · 21 palabras · Seis pasos

> Un queque de limón sale esponjoso o sale un ladrillo. La diferencia son seis pasos, y cada uno tiene un porqué.

#### 2 · Ingredientes · 40 palabras · Paso 1: temperatura ambiente

> Dos tazas de harina, una de azúcar, una de leche, media de mantequilla, dos huevos, dos cucharaditas de polvos de hornear y la ralladura de un limón. Mantequilla y huevos a temperatura ambiente, para que se mezclen y atrapen aire.

#### 3 · Cremar · 24 palabras · Paso 2: mantequilla y azúcar

> Primero, bate la mantequilla con el azúcar hasta que quede pálida. Los cristales abren pequeños bolsillos de aire, y esos bolsillos serán la miga.

#### 4 · Los huevos · 15 palabras · Paso 3: de a uno

> Después, los huevos de a uno. Si van fríos o juntos, la mezcla se corta.

#### 5 · Secos y leche · 28 palabras · Paso 4: sin batir de más

> Tamiza la harina con los polvos y agrégala alternando con la leche. Mezcla solo hasta integrar: batir de más puede dejarlo duro. Al final, la ralladura de limón.

#### 6 · Horno · 29 palabras · Paso 5: 180 °C

> Vierte la masa en una fuente rectangular de vidrio, enmantequillada y enharinada, y al horno a ciento ochenta grados. El calor dilata el aire atrapado y la masa sube.

#### 7 · La prueba · 22 palabras · Paso 6: el palillo

> A los cuarenta minutos, más o menos, clava un palillo: si sale limpio, está listo. Déjalo reposar unos minutos antes de desmoldar.

#### 8 · Cierre · 18 palabras · La pregunta

> Si el próximo sale mal, no culpes a la receta: revisa cuál de estos seis pasos te saltaste.

**Total: 197 palabras** (≈ 1107 caracteres).

## v2: feedback del usuario (3-oct-2026)

> *«Horrible illustration, look for home queque, no nuts on them, no circles, search on the internet homemade queque so you understand, fuente rectangular transparente para horno, queque con ceste de limon. Readjust the script. Elevenlabs is better, no batidora sound.»*

| Feedback | Cambio |
| --- | --- |
| Queque casero con **ralladura de limón** | Es un **queque de limón**: la ralladura entra en los ingredientes y al final de la masa; se saca la vainilla |
| **Fuente rectangular transparente** para horno | Escena 6: *«fuente rectangular de vidrio, enmantequillada y enharinada»*; todas las láminas muestran esa fuente |
| Sin frutos secos, **sin círculos** | Las láminas se piden sin círculos numerados ni burbujas redondas: flechas con punta y bolsillos de aire irregulares |
| `elevenlabs/v3` es mejor | Voz elegida: `elevenlabs/v3`, voz `Roger`, `es` |
| Sin sonido de batidora | **Se eliminan todos los efectos de sonido** |
| Afirmaciones débiles | «batir de más **puede** dejarlo duro»; reposo «unos minutos»; horno «a los cuarenta minutos, más o menos» |

## Revisar al leerlo en voz alta (P3)

- [ ] ¿Los **seis pasos** se cuentan bien? (1 temperatura ambiente, 2 cremar, 3 huevos, 4 secos y leche, 5 horno, 6 palillo y reposo).
- [ ] **Escena 5:** "batir de más desarrolla gluten, y el queque queda duro" es más categórico que la fuente. Alternativa: *"batir de más puede dejarlo duro"*.
- [ ] **Escena 7:** "treinta y cinco, cuarenta minutos" y "diez minutos de reposo": las fuentes dicen 30–60 y "unos minutos". ¿Se deja o se dice *"cuando el palillo salga limpio"* sin minutos?
- [ ] ¿El cierre ("revisa cuál de estos seis pasos te saltaste") deja pensar o suena a reproche?
- [ ] ¿Es muy larga para un Short? (≈ 80 s con 20 imágenes: una cada ≈ 4 s).

## Dirección y prompts

En [[Queque - Estado]].
