# Test Queries - Constitución - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia constitucional.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia constitucional.
- Priorice la Constitución 2024 para consultas actuales.
- Use únicamente artículos constitucionales cargados.
- Cite la Constitución 2024 cuando el artículo esté disponible.
- Cite la Constitución 2015 solo como fuente histórica cuando sea necesario.
- No invente artículos constitucionales no cargados.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Supremacía constitucional

### Pregunta

¿Qué pasa si una ley o resolución contradice la Constitución dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal prioritaria disponible:
  - Constitución de la República Dominicana 2024, artículo 6.
- Debe indicar que el artículo 6 establece la sujeción de personas y órganos públicos a la Constitución como norma suprema.
- Debe indicar que el estado registrado es:
  - pendiente_de_verificacion
- Puede mencionar que la Constitución 2015 también está cargada, pero como documento histórico.

---

## Prueba 2 - Dignidad humana

### Pregunta

¿La dignidad humana está protegida por la Constitución dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal prioritaria disponible:
  - Constitución de la República Dominicana 2024, artículo 5.
  - Constitución de la República Dominicana 2024, artículo 7.
  - Constitución de la República Dominicana 2024, artículo 8.
- Debe explicar de manera prudente que esos artículos cargados reconocen la dignidad humana como fundamento y función esencial del Estado.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion

---

## Prueba 3 - Separación de poderes

### Pregunta

¿Cuáles son los poderes del Estado dominicano?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal prioritaria disponible:
  - Constitución de la República Dominicana 2024, artículo 4.
- Debe responder que el gobierno se divide en Poder Legislativo, Poder Ejecutivo y Poder Judicial, citando el artículo cargado.
- Debe indicar que el estado registrado de la Constitución 2024 es pendiente_de_verificacion.

---

## Prueba 4 - Pregunta sin artículo cargado

### Pregunta

¿Cuál artículo exacto protege el derecho de propiedad en República Dominicana?

### Resultado esperado

Si el artículo específico de propiedad no está cargado, el bot debe responder:

"No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."

También debe indicar que se requiere cargar el artículo constitucional correspondiente de la Constitución 2024 para responder con precisión.

---

## Prueba 5 - Constitución vigente

### Pregunta

¿Cuál es la Constitución vigente de República Dominicana?

### Resultado esperado

El bot debe indicar:

- En el repositorio está cargada la Constitución 2024 como fuente constitucional prioritaria.
- El estado registrado todavía es pendiente_de_verificacion.
- La Constitución 2015 está cargada como documento histórico.
- Para una conclusión formal de vigencia debe verificarse el texto completo y la publicación oficial correspondiente.
- No debe inventar datos no contenidos en los documentos cargados.

---

## Prueba 6 - Estado social y democrático de derecho

### Pregunta

¿Qué significa que República Dominicana es un Estado Social y Democrático de Derecho?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal prioritaria disponible:
  - Constitución de la República Dominicana 2024, artículo 7.
- Debe explicar únicamente con base en el artículo cargado.
- No debe inventar doctrina adicional si no está cargada.
