# Test Queries - Registro Inmobiliario - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia de registro inmobiliario, derechos reales, títulos, saneamiento y Jurisdicción Inmobiliaria.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia inmobiliaria / registro inmobiliario.
- Use la Ley 108-05 cuando aplique a derechos reales inmobiliarios, saneamiento, registro, cargas, gravámenes y competencia de la Jurisdicción Inmobiliaria.
- Cite únicamente artículos cargados.
- No invente procedimientos de deslinde, saneamiento, litis, transferencia o recursos si todavía no están cargados.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Objeto de la Ley 108-05

### Pregunta

¿Qué regula la Ley 108-05 de Registro Inmobiliario?

### Resultado esperado

El bot debe identificar:

- Materia principal: inmobiliario / registro_inmobiliario.
- Base legal disponible:
  - Ley 108-05, artículo 2.
- Debe explicar que el artículo cargado indica que la ley regula el saneamiento y el registro de todos los derechos reales inmobiliarios, así como cargas y gravámenes susceptibles de registro, respecto de inmuebles en República Dominicana.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Debe advertir que falta verificar modificaciones por Ley 51-07, reglamentos y jurisprudencia relacionada.

---

## Prueba 2 - Competencia de la Jurisdicción Inmobiliaria

### Pregunta

¿Qué conoce la Jurisdicción Inmobiliaria?

### Resultado esperado

El bot debe identificar:

- Materia principal: inmobiliario.
- Base legal disponible:
  - Ley 108-05, artículo 3.
- Debe explicar que el artículo cargado indica que la Jurisdicción Inmobiliaria tiene competencia exclusiva sobre derechos inmobiliarios y su registro en República Dominicana, desde la solicitud de autorización para mensura y durante la vida jurídica del inmueble, salvo casos expresamente señalados por la ley.
- No debe inventar procedimientos específicos no cargados.

---

## Prueba 3 - Nombre de la ley

### Pregunta

¿Cómo se llama formalmente la Ley 108-05?

### Resultado esperado

El bot debe identificar:

- Materia principal: inmobiliario.
- Base legal disponible:
  - Ley 108-05, artículo 1.
- Debe responder que la ley se denomina Ley de Registro Inmobiliario.
- Debe citar archivo del repositorio, fuente oficial y estado de vigencia.

---

## Prueba 4 - Deslinde

### Pregunta

¿Cómo hago un deslinde en República Dominicana?

### Resultado esperado

El bot debe:

- Identificar materia principal: inmobiliario / registro_inmobiliario.
- No inventar procedimiento de deslinde.
- Como todavía no están cargados los artículos específicos de deslinde, reglamentos o resoluciones aplicables, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar los artículos y reglamentos específicos sobre deslinde, mensuras catastrales y procedimiento ante la Jurisdicción Inmobiliaria.

---

## Prueba 5 - Título de propiedad

### Pregunta

Tengo un contrato de venta de un solar, ¿eso significa que ya soy dueño registrado?

### Resultado esperado

El bot debe:

- Identificar materia principal: inmobiliario.
- Materia secundaria posible: civil / contratos.
- No afirmar titularidad registrada definitiva sin documentos.
- Puede citar Ley 108-05, artículo 2, de forma limitada, para explicar que la ley regula el registro de derechos reales inmobiliarios.
- Debe indicar que se requiere revisar contrato, certificado de título, registro, cargas, gravámenes y documentos del inmueble.
- No debe inventar procedimiento de transferencia si no está cargado.

---

## Prueba 6 - Cargas y gravámenes

### Pregunta

¿La Ley 108-05 trata sobre cargas y gravámenes de inmuebles?

### Resultado esperado

El bot debe identificar:

- Materia principal: inmobiliario / registro_inmobiliario.
- Base legal disponible:
  - Ley 108-05, artículo 2.
- Debe explicar que el artículo cargado menciona cargas y gravámenes susceptibles de registro en relación con inmuebles del territorio dominicano.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
