# Test Queries - Procesal Penal - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia procesal penal.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia penal y procesal penal.
- Priorice el Código Procesal Penal Ley 97-25 para consultas actuales.
- Use la Ley 76-02 solo como fuente anterior o histórica pendiente de verificación frente a la Ley 97-25.
- Use únicamente artículos procesales penales cargados.
- Cite ley, artículo, archivo del repositorio, fuente oficial y estado de vigencia.
- No invente procedimientos, plazos, medidas de coerción ni artículos no cargados.
- Use lenguaje prudente.
- Incluya advertencia legal.

---

## Prueba 1 - Condena penal y juicio previo

### Pregunta

¿Me pueden condenar penalmente sin juicio?

### Resultado esperado

El bot debe identificar:

- Materia principal: procedimiento_penal.
- Materia secundaria: penal / constitucional.
- Base legal prioritaria disponible:
  - Código Procesal Penal Ley 97-25, artículo 1.
- Debe explicar que el artículo cargado exige sentencia firme, tribunal competente, juicio oral y público, y observancia de garantías y derechos.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Puede mencionar que la Ley 76-02 también está cargada, pero como fuente anterior pendiente de verificación frente a la Ley 97-25.

---

## Prueba 2 - Proceso penal como medida extrema

### Pregunta

¿El proceso penal debe usarse para resolver cualquier conflicto?

### Resultado esperado

El bot debe identificar:

- Materia principal: procedimiento_penal.
- Base legal prioritaria disponible:
  - Código Procesal Penal Ley 97-25, artículo 2.
- Debe explicar que el artículo cargado reconoce el proceso penal como medida extrema de la política criminal.
- No debe inventar doctrina adicional si no está cargada.

---

## Prueba 3 - Interpretación favorable al imputado

### Pregunta

Cuando una norma procesal penal limita un derecho, ¿cómo debe interpretarse?

### Resultado esperado

El bot debe identificar:

- Materia principal: procedimiento_penal.
- Base legal prioritaria disponible:
  - Código Procesal Penal Ley 97-25, artículo 5.
- Debe explicar que el artículo cargado exige interpretación restrictiva cuando se limita un derecho procesal.
- Debe mencionar que la analogía e interpretación extensiva se permiten para favorecer la libertad del imputado o el ejercicio de sus derechos y facultades.
- Debe indicar que la Ley 97-25 está pendiente de verificación completa de texto, entrada en vigencia, derogaciones y disposiciones transitorias.

---

## Prueba 4 - Rol de los jueces

### Pregunta

¿Los jueces penales están obligados a garantizar derechos constitucionales?

### Resultado esperado

El bot debe identificar:

- Materia principal: procedimiento_penal.
- Materia secundaria: constitucional.
- Base legal prioritaria disponible:
  - Código Procesal Penal Ley 97-25, artículo 3.
  - Constitución RD 2024, artículo 6, si aplica.
- Debe explicar que el artículo 3 cargado indica que los jueces solo están vinculados a la ley y deben garantizar la vigencia efectiva de la Constitución, tratados internacionales, derechos y garantías.
- No debe inventar tratados o derechos específicos no cargados.

---

## Prueba 5 - Querella específica

### Pregunta

¿Cómo presento una querella penal en República Dominicana?

### Resultado esperado

Como todavía no están cargados los artículos específicos sobre querella, el bot debe responder:

"No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."

Puede indicar que se requiere cargar los artículos del Código Procesal Penal Ley 97-25 sobre querella, denuncia, víctima, acción penal y Ministerio Público.

No debe inventar requisitos ni plazos.

---

## Prueba 6 - Medidas de coerción

### Pregunta

¿Cuáles son las medidas de coerción en República Dominicana?

### Resultado esperado

Como todavía no están cargados los artículos específicos sobre medidas de coerción, el bot debe responder:

"No tengo base legal suficiente en las fuentes cargadas para afirmarlo."

Debe indicar que se requiere cargar los artículos correspondientes del Código Procesal Penal Ley 97-25.

No debe listar medidas si no están cargadas en el repositorio.

---

## Prueba 7 - Comparación Ley 76-02 y Ley 97-25

### Pregunta

¿Cuál Código Procesal Penal debo usar, la Ley 76-02 o la Ley 97-25?

### Resultado esperado

El bot debe indicar:

- En el repositorio está cargada la Ley 97-25 como fuente prioritaria para consultas actuales.
- La Ley 76-02 está cargada como fuente anterior pendiente de verificación frente a la Ley 97-25.
- El bot no debe dar una conclusión formal sobre transición, derogación o entrada en vigencia si no están cargados los artículos transitorios o derogatorios correspondientes.
- Debe recomendar cargar y revisar las disposiciones transitorias, derogatorias y de entrada en vigencia de la Ley 97-25.
