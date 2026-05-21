# Test Queries - Condominios - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia de condominios, propiedad horizontal y conflictos entre propietarios.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia de condominio / inmobiliario.
- Use la Ley 5038 cuando aplique a propiedad dividida por pisos, departamentos, viviendas o locales independientes.
- Cite únicamente artículos cargados.
- No invente reglas sobre cuotas, administración, áreas comunes, asambleas o sanciones si todavía no están cargadas.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Qué es un condominio

### Pregunta

¿Qué es un condominio según la ley dominicana?

### Resultado esperado

El bot debe identificar:

- Materia principal: condominio.
- Materia secundaria: inmobiliario.
- Base legal disponible:
  - Ley 5038, artículo 1.
- Debe explicar que el artículo cargado permite que la propiedad de edificios de dos o más pisos pertenezca a distintas personas por pisos, departamentos, viviendas o locales independientes, siempre que los propietarios registren sus derechos conforme al régimen establecido por la ley.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Debe advertir que falta completar texto íntegro, verificar modificaciones, vigencia y relación con Ley 108-05.

---

## Prueba 2 - Apartamento independiente

### Pregunta

Compré un apartamento en un edificio. ¿Eso puede ser propiedad independiente?

### Resultado esperado

El bot debe identificar:

- Materia principal: condominio.
- Materia secundaria: inmobiliario.
- Base legal disponible:
  - Ley 5038, artículo 1.
- Debe explicar de forma prudente que el artículo cargado contempla propiedad por pisos, departamentos, viviendas o locales independientes.
- Debe indicar que se requiere revisar título, registro inmobiliario, régimen de condominio y documentos del inmueble.
- No debe afirmar titularidad definitiva sin documentos.

---

## Prueba 3 - Áreas comunes

### Pregunta

¿Quién es dueño de las áreas comunes de un condominio?

### Resultado esperado

El bot debe:

- Identificar materia principal: condominio.
- No inventar reglas sobre áreas comunes.
- Como solo está cargado el artículo 1 y no están cargados artículos específicos sobre áreas comunes, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Debe indicar que se requiere cargar el texto completo de la Ley 5038, reglamento de condominio y normas relacionadas.

---

## Prueba 4 - Cuotas de mantenimiento

### Pregunta

¿Me pueden cobrar mantenimiento en un condominio?

### Resultado esperado

El bot debe:

- Identificar materia principal: condominio.
- No inventar obligaciones de pago.
- Si no hay artículos específicos cargados sobre cuotas o mantenimiento, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Puede indicar que se requiere cargar artículos aplicables de la Ley 5038, reglamento del condominio y documentos contractuales.

---

## Prueba 5 - Conflicto entre vecinos

### Pregunta

Un vecino del condominio está usando un área común como si fuera privada. ¿Qué puedo hacer?

### Resultado esperado

El bot debe:

- Identificar materia principal: condominio.
- Materia secundaria posible: civil / inmobiliario.
- No inventar procedimiento o sanción.
- Debe indicar que no hay artículos específicos cargados sobre uso de áreas comunes.
- Puede recomendar revisar reglamento del condominio, título, acta de asamblea, administración y documentos del inmueble.
- Debe indicar que se requiere cargar normas específicas antes de una conclusión legal.

---

## Prueba 6 - Registro del condominio

### Pregunta

¿Un condominio debe estar registrado?

### Resultado esperado

El bot debe identificar:

- Materia principal: condominio.
- Materia secundaria: registro inmobiliario.
- Base legal disponible:
  - Ley 5038, artículo 1.
- Debe explicar que el artículo cargado condiciona ese régimen a que los propietarios registren sus derechos conforme a la ley.
- Debe indicar que se necesita cargar Ley 108-05 de Registro Inmobiliario para mayor precisión.
