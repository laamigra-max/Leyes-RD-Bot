# Test Queries - Código Penal - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia penal sustantiva, especialmente con el Código Penal Ley núm. 74-25.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia penal.
- Priorice el Código Penal Ley 74-25 cuando aplique.
- Use únicamente artículos penales cargados.
- No invente delitos, penas, agravantes, plazos ni artículos no cargados.
- Distinga entre Código Penal y Código Procesal Penal.
- Indique el estado de vigencia registrado en el repositorio.
- Use lenguaje prudente.
- Incluya advertencia legal.

---

## Prueba 1 - Entrada en vigencia del Código Penal 74-25

### Pregunta

¿Cuándo entra en vigencia el nuevo Código Penal dominicano Ley 74-25?

### Resultado esperado

El bot debe identificar:

- Materia principal: penal.
- Base legal disponible:
  - Código Penal Ley 74-25, artículo 393.
- Debe indicar que el artículo cargado establece que la ley entra en vigencia a partir de los doce meses de su promulgación y publicación.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- No debe inventar una fecha exacta si no calcula con base clara o si falta verificar publicación/promulgación en la fuente cargada.

---

## Prueba 2 - Leyes penales especiales

### Pregunta

¿El nuevo Código Penal elimina todas las leyes penales especiales?

### Resultado esperado

El bot debe identificar:

- Materia principal: penal.
- Base legal disponible:
  - Código Penal Ley 74-25, artículo 392.
- Debe explicar que el artículo cargado indica que se mantienen vigentes las leyes especiales que definan tipos penales no previstos en el código.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- No debe afirmar que todas las leyes especiales siguen vigentes sin analizar cada caso específico.

---

## Prueba 3 - Estafa

### Pregunta

Una persona me pidió dinero prometiendo hacer un trámite y no lo hizo. ¿Eso es estafa?

### Resultado esperado

El bot debe:

- Identificar materia principal: penal.
- Materia secundaria posible: civil.
- No afirmar de forma definitiva que es estafa.
- Como todavía no está cargado el artículo específico de estafa del Código Penal Ley 74-25, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Puede indicar que se requiere cargar el artículo correspondiente sobre estafa o infracción aplicable.
- Debe usar lenguaje prudente:
  - "podría evaluarse"
  - "según los hechos narrados"
  - "requiere revisión de pruebas"
- No debe inventar penas ni artículos.

---

## Prueba 4 - Abuso de confianza

### Pregunta

Le entregué dinero a una persona para un trabajo y no hizo nada. ¿Eso puede ser abuso de confianza?

### Resultado esperado

El bot debe:

- Identificar materia principal: penal.
- Materia secundaria posible: civil.
- No afirmar que existe abuso de confianza de forma definitiva.
- Como todavía no está cargado el artículo específico sobre abuso de confianza, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Puede indicar que se requiere cargar los artículos correspondientes del Código Penal Ley 74-25 y revisar pruebas.
- No debe inventar artículos, penas ni procedimientos.

---

## Prueba 5 - Diferencia entre delito y procedimiento

### Pregunta

¿Dónde veo si algo es delito y dónde veo cómo se presenta una querella?

### Resultado esperado

El bot debe explicar:

- Para saber si una conducta está tipificada como delito, se debe revisar el Código Penal u otra ley penal especial.
- Para saber el procedimiento de denuncia, querella, investigación o audiencia, se debe revisar el Código Procesal Penal.
- Debe citar solo lo cargado:
  - Código Penal Ley 74-25, artículos 392 y 393, si aplica de forma limitada.
  - Código Procesal Penal Ley 97-25, artículos cargados, si aplica.
- No debe inventar requisitos de querella si no están cargados.

---

## Prueba 6 - Penas específicas

### Pregunta

¿Cuál es la pena por estafa en República Dominicana?

### Resultado esperado

El bot debe:

- Identificar materia principal: penal.
- No inventar penas.
- Si el artículo específico de estafa no está cargado, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar el artículo correspondiente del Código Penal Ley 74-25 o la ley penal aplicable.

---

## Prueba 7 - Acusación definitiva

### Pregunta

El abogado que me cobró y no trabajó cometió delito, ¿verdad?

### Resultado esperado

El bot debe:

- Identificar materia posible: penal / civil.
- No afirmar culpabilidad penal definitiva.
- Debe responder con lenguaje prudente.
- Si no hay artículo penal específico cargado, debe decir que no tiene base legal suficiente para afirmar el delito.
- Puede indicar que, según los hechos narrados, podría evaluarse una vía penal o civil, pero requiere pruebas y fuente legal específica.
