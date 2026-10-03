---
tipo: investigación
creado: 2026-10-03
actualizado: 2026-10-03
estado: v1 · diseñado y aplicado en el montaje del video "Helio y poder"
tags: [investigación, youtube, montaje, transiciones, efectos, blender]
---

# Transiciones y efectos

← [[Canal YouTube]] · [[Montaje en Blender]] · [[Estilo visual - miniaturas de plastilina]] · [[Proceso de producción]]

El lenguaje de montaje del canal: **qué transición se usa en cada situación, qué efectos se aplican y por qué**, para que todos los videos se vean y se sientan igual. Se aplicó por primera vez en [[Guion - Helio (70 segundos)]]; el script que lo implementa es `build_helio.py` (ver [[Montaje en Blender]]).

## Idea de diseño

Todo el canal es una **sucesión de maquetas de plastilina** ([[Estilo visual - miniaturas de plastilina]]). El montaje se comporta como un stop-motion sobrio:

- una imagen **cambia en el sitio** cuando algo cambia en la historia (se apaga una llama, baja un nivel);
- la cámara solo se **acerca o se aleja despacio**, como quien mira una maqueta de cerca;
- entre escenas se **pasa la hoja** (corte suave);
- el papel tiene **grano y bordes más oscuros**, para que se sienta un objeto físico y no una pantalla.

Regla de oro: **ninguna transición dura más de medio segundo y ninguna llama la atención sobre sí misma**; la voz manda.

## Vocabulario de transiciones

| Situación | Transición | Duración | Cómo se implementa |
| --- | --- | --- | --- |
| **Algo cambia dentro de la lámina** (inicial → final de una toma) | **Cambio de estado**: el fotograma final se funde sobre el inicial, sincronizado con la voz | 0,5 a 4 s según el cambio | La capa final sube su opacidad de 0 a 1 en la hora de la palabra que provoca el cambio |
| **Otra toma en la misma escena** (3a → 3b, 5a → 5b) | **Fundido cruzado** | 0,3 s | La toma entrante, en un canal superior, sube de 0 a 1 sobre la saliente |
| **Cambio de escena** | **Pasar la hoja**: la imagen sale al color del papel y la siguiente sale de él | 0,2 s + 0,2 s | Una tira de color papel va de fondo; cada toma baja su opacidad a 0 al final y sube de 0 a 1 al empezar |
| **Apertura** | Sin transición: la primera lámina ya está en pantalla cuando entra el sonido | — | La toma 1 no tiene entrada |
| **Cierre** | **Corte seco a negro** tras 1 s de lámina fija | — | La última toma no tiene salida; el video termina |

**Qué se evita:** wipes, deslizamientos, iris y cualquier transición "de plantilla". Son ruido visual que no sale del mundo de la libreta.

### Sincronía con la voz

El **momento del cambio de estado** se ancla a una palabra concreta, no a un porcentaje de la toma. Se calculan las pausas de cada voz y se convierten en tiempos de la línea de tiempo:

| Toma | El cambio ocurre | Palabra o idea |
| --- | --- | --- |
| 1 | la llama se apaga en 0,5 s | "**Se detuvo** el gas" |
| 2 | acercamiento de 4 s a las bobinas | "…se usa para fabricar chips" |
| 3a | el corchete agrupa a los tres países | "Estados Unidos, Qatar y Rusia" |
| 3b | la barrera cierra el paso | "…que la guerra dejó casi cerrado" |
| 4 | el nivel baja durante 3,4 s | "…y, a las seis semanas, se evapora" |
| 5a | se cierra la válvula con el candado | "…hasta fines de 2027" |
| 5b | la llave cambia de manos | "…vendió su reserva federal" |
| 6 | aparecen las dependencias | "Un gas que casi nadie nombra sostiene hospitales y fábricas de chips" |

## Efectos

| Efecto | Qué hace | Valor | Por qué |
| --- | --- | --- | --- |
| **Empuje lento de cámara** | Zoom lineal sobre toda la toma, igual en la capa inicial y en la final | +6 % (acercamiento); −6 % en la toma 6 (retroceso) | Da vida a una imagen fija y marca la dirección de la atención; el retroceso del cierre "abre" el diagrama |
| **Viñeta** | Oscurece los bordes con un gradiente radial | multiplicar, opacidad 0,55 | Enfoca el centro y da la sensación de hoja bajo una lámpara |
| **Grano de papel** | Ruido fino estático | superponer, opacidad 0,10 | Quita el aspecto digital liso del dibujo generado |
| **Papel de fondo** | Tira de color crema detrás de todo | color papel (lineal 0,89 / 0,83 / 0,68) | Es lo que se ve entre escenas al pasar la hoja |

Los dos efectos de textura se **generan con el propio script** (viñeta y grano en `render/_fx/`), así que no hay archivos que mantener.

## Sonido

| Elemento | Tratamiento |
| --- | --- |
| **Voz** | Volumen 1,0. Se recortan los silencios de entrada y salida de cada toma y se dejan 0,3 s entre escenas |
| **Zumbido de la planta** (escena 1) | Bajo la voz (volumen 0,30), entra suave y **se corta en seco** en "Se detuvo el gas": el único silencio intencional del video |
| **Sonidos de escena** (resonancia, siseo) | Volumen 0,18 a 0,22, con entrada de 0,3 s y salida de 0,4 s; arrancan 0,2 s después del cambio de escena y terminan 0,1 s antes del siguiente |
| **Música** | Ninguna |

Los volúmenes de los sonidos de fondo son estimaciones sin oír el resultado; se ajustan en los parámetros del script al escuchar el video.

## Parámetros (en `build_helio.py`)

Todo se controla desde las constantes del inicio del script:

```
GAP_ESCENA = 0.30   # silencio entre voces (s)
INICIO_VOZ = 0.40   # entrada de la primera voz
COLA       = 1.00   # lámina fija tras la última palabra, antes del corte a negro
DIP        = 0.20   # media duración de "pasar la hoja"
CRUCE      = 0.30   # fundido cruzado dentro de una escena
ZOOM       = 0.06   # empuje de cámara
VIGNETA    = 0.55   # opacidad de la viñeta
GRANO      = 0.10   # opacidad del grano
```

Y la lista `tomas` define, por toma, el canal, los tiempos, las dos imágenes y **cuándo y cuánto dura el cambio de estado** (calculado desde las pausas de la voz).

## Cómo se aplica a un video nuevo

1. Copiar `build_helio.py` a `render/build_<video>.py` de la carpeta del video.
2. Cambiar los nombres de archivo y la lista `tomas`: tiempos de cambio según la voz (la función `cue(escena, tiempo_en_el_archivo)` convierte un tiempo del archivo de voz en tiempo de la línea de tiempo).
3. Ajustar las constantes si el video lo pide; no cambiar el vocabulario sin actualizar esta nota.
4. Ejecutar y revisar fotogramas clave antes de entregar ([[Montaje en Blender]]).

## Qué no hace todavía

- **No anima el dibujo:** el cambio de estado es un fundido entre dos imágenes, sin animación del objeto.
- **No hay texto en pantalla** (cifras, títulos): se añadiría como tiras de texto del propio secuenciador, con [[Estilo de texto en pantalla]].
- **No se oyó el resultado:** el equilibrio entre voz y sonidos de fondo es una estimación.
