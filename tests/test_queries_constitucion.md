# Test Queries - Constitución - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia constitucional.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia constitucional.
- Use únicamente artículos constitucionales cargados.
- Cite la Constitución 2015 como documento histórico pendiente de verificación.
- No invente artículos constitucionales no cargados.
- Indique cuando sea necesario cargar la Constitución 2024.
- Incluya advertencia legal.

---

## Prueba 1 - Supremacía constitucional

### Pregunta

¿Qué pasa si una ley o resolución contradice la Constitución dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal disponible:
  - Constitución de la República Dominicana 2015, artículo 6.
- Debe indicar que el artículo 6 establece la sujeción de personas y órganos públicos a la Constitución como norma suprema.
- Debe indicar que esta versión está marcada como:
  - historica_pendiente_verificacion
- Debe advertir que debe cargarse y verificarse la Constitución 2024 para una respuesta vigente definitiva.

---

## Prueba 2 - Dignidad humana

### Pregunta

¿La dignidad humana está protegida por la Constitución dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal disponible:
  - Constitución de la República Dominicana 2015, artículo 5.
  - Constitución de la República Dominicana 2015, artículo 7.
  - Constitución de la República Dominicana 2015, artículo 8.
- Debe explicar de manera prudente que esos artículos cargados reconocen la dignidad humana como fundamento y función esencial del Estado.
- Debe indicar estado de vigencia:
  - historica_pendiente_verificacion

---

## Prueba 3 - Separación de poderes

### Pregunta

¿Cuáles son los poderes del Estado dominicano?

### Resultado esperado

El bot debe identificar:

- Materia principal: constitucional.
- Base legal disponible:
  - Constitución de la República Dominicana 2015, artículo 4.
- Debe responder que el gobierno se divide en Poder Legislativo, Poder Ejecutivo y Poder Judicial, citando el artículo cargado.
- Debe indicar que la Constitución 2015 está pendiente de verificación frente a la Constitución 2024.

---

## Prueba 4 - Pregunta sin artículo cargado

### Pregunta

¿Cuál artículo exacto protege el derecho de propiedad en República Dominicana?

### Resultado esperado

Si el artículo específico de propiedad no está cargado, el bot debe responder:

"No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."

También debe indicar que se requiere cargar el artículo constitucional correspondiente o la Constitución 2024 completa para responder con precisión.

---

## Prueba 5 - Constitución vigente

### Pregunta

¿Cuál es la Constitución vigente de República Dominicana?

### Resultado esperado

El bot no debe responder definitivamente usando solo la Constitución 2015.

Debe indicar:

- En el repositorio solo está cargada la Constitución 2015 como documento histórico pendiente de verificación.
- Para responder con precisión sobre vigencia actual, debe cargarse y verificarse la Constitución 2024.
- No debe inventar contenido de la Constitución 2024 si no está cargada.
