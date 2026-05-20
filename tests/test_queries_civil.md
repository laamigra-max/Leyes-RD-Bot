# Test Queries - Civil - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia civil.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia civil.
- Use únicamente artículos civiles cargados.
- Cite el Código Civil cuando el artículo esté disponible.
- No invente artículos sobre contratos, deudas, daños, prescripción u obligaciones si todavía no están cargados.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Irretroactividad de la ley

### Pregunta

¿Una ley nueva puede aplicarse hacia atrás en República Dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: civil.
- Materia secundaria posible: constitucional.
- Base legal disponible:
  - Código Civil de la República Dominicana, artículo 2.
- Debe explicar que el artículo 2 cargado indica que la ley no dispone sino para el porvenir y no tiene efecto retroactivo.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- No debe inventar excepciones si no están cargadas.

---

## Prueba 2 - Orden público y contratos

### Pregunta

¿Puedo hacer un contrato privado que deje sin efecto una ley de orden público?

### Resultado esperado

El bot debe identificar:

- Materia principal: civil.
- Base legal disponible:
  - Código Civil de la República Dominicana, artículo 6.
- Debe explicar que las leyes que interesan al orden público y a las buenas costumbres no pueden ser derogadas por convenciones particulares.
- Debe indicar que el Código Civil está pendiente de verificación contra fuente dominicana oficial o versión consolidada vigente.

---

## Prueba 3 - Juez no quiere decidir

### Pregunta

¿Qué pasa si un juez dice que no puede decidir porque la ley no es clara?

### Resultado esperado

El bot debe identificar:

- Materia principal: civil.
- Base legal disponible:
  - Código Civil de la República Dominicana, artículo 4.
- Debe explicar de forma prudente que el artículo cargado se refiere a denegación de justicia cuando el juez rehúsa juzgar por silencio, oscuridad o insuficiencia de la ley.
- No debe inventar procedimiento penal, sanción específica o trámite si no está cargado.

---

## Prueba 4 - Bien inmueble de extranjero

### Pregunta

Un extranjero tiene un inmueble en República Dominicana. ¿Qué ley rige ese inmueble?

### Resultado esperado

El bot debe identificar:

- Materia principal: civil.
- Materia secundaria posible: inmobiliario.
- Base legal disponible:
  - Código Civil de la República Dominicana, artículo 3.
- Debe explicar que el artículo cargado indica que los bienes inmuebles, aunque estén poseídos por extranjeros, están regidos por la ley dominicana.
- Debe usar lenguaje prudente y recomendar verificar normas inmobiliarias específicas si el caso es sobre título, deslinde o registro.

---

## Prueba 5 - Contrato incumplido

### Pregunta

Firmé un contrato y la otra persona no cumplió. ¿Puedo demandar por daños y perjuicios?

### Resultado esperado

El bot debe identificar:

- Materia principal: civil.
- Materia secundaria posible: contratos / responsabilidad civil.
- Como todavía no están cargados los artículos específicos sobre obligaciones contractuales, incumplimiento o daños y perjuicios, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Puede indicar que se necesita cargar los artículos del Código Civil sobre obligaciones, contratos y responsabilidad civil para una respuesta más precisa.
- No debe inventar artículos.

---

## Prueba 6 - Prescripción

### Pregunta

¿Cuál es el plazo para demandar una deuda civil en República Dominicana?

### Resultado esperado

El bot debe:

- Identificar materia principal: civil.
- No inventar plazos.
- Si no hay artículos de prescripción cargados, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar los artículos aplicables sobre prescripción.
