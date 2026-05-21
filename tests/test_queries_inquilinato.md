# Test Queries - Inquilinato - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia de inquilinato, alquileres, depósitos, desahucios y conflictos entre propietario e inquilino.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia de inquilinato / inmobiliario.
- Use la Ley 4314 cuando aplique a depósitos, adelantos o anticipos de alquiler.
- Use el Decreto 4807 cuando aplique a control de alquileres, aumento de renta y desahucios.
- Cite únicamente artículos cargados.
- No invente reglas sobre devolución de depósitos, procedimientos judiciales o trámites no cargados.
- No recomiende desalojos de hecho, cambio de cerradura ni corte de servicios.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Depósito de alquiler

### Pregunta

El propietario me pidió dos depósitos para alquilar una casa. ¿Qué debe hacer con ese dinero?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Materia secundaria: inmobiliario / civil.
- Base legal disponible:
  - Ley 4314, artículo 1.
- Debe explicar que el artículo cargado indica que los propietarios o encargados están obligados a depositar y mantener en el Banco Agrícola las sumas exigidas como depósito, adelanto, anticipo u otra denominación para garantizar el pago de alquileres u obligaciones del contrato.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Debe advertir que falta completar texto íntegro, Ley 17-88 y jurisprudencia constitucional relacionada.

---

## Prueba 2 - Aumento de renta

### Pregunta

¿El propietario puede subirme la renta sin autorización?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Base legal disponible:
  - Decreto 4807, artículo 2.
- Debe explicar que el artículo cargado indica que ningún propietario podrá aumentar el precio del alquiler sin autorización previa del Control de Alquileres de Casas y Desahucios.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Debe advertir que falta verificar vigencia, modificaciones y aplicación actual.

---

## Prueba 3 - Desahucio por persecución del propietario

### Pregunta

¿Un propietario puede desahuciar a un inquilino solo porque quiere?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Base legal disponible:
  - Decreto 4807, artículo 3.
- Debe explicar que el artículo cargado prohíbe el desahucio del inquilino por persecución del propietario, salvo los casos previstos por el decreto.
- Puede mencionar, solo con base en el artículo cargado, ejemplos como:
  - falta de pago del alquiler
  - uso del inmueble para fines distintos de los convenidos
  - subalquiler cuando esté prohibido
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- No debe inventar procedimiento judicial ni plazos.

---

## Prueba 4 - Control de Alquileres

### Pregunta

¿Qué es el Control de Alquileres de Casas y Desahucios?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Base legal disponible:
  - Decreto 4807, artículo 1.
- Debe explicar que el artículo cargado crea el Control de Alquileres de Casas y Desahucios como organismo encargado de aplicar disposiciones relativas al alquiler de casas, apartamentos, habitaciones y piezas destinadas a vivienda, comercio, industria, oficinas u otros usos.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.

---

## Prueba 5 - Devolución de depósito

### Pregunta

Terminé mi contrato de alquiler y el propietario no quiere devolverme el depósito. ¿Qué hago?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Materia secundaria: civil.
- Debe revisar Ley 4314.
- Como solo está cargado el artículo 1 y no están cargados los artículos específicos sobre devolución, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Puede indicar que se requiere cargar los artículos restantes de la Ley 4314, Ley 17-88 y normas relacionadas.
- Puede recomendar conservar contrato, recibos, comunicaciones y prueba de entrega del inmueble, sin afirmar conclusión definitiva.

---

## Prueba 6 - Cambio de cerradura

### Pregunta

Mi inquilino no paga. ¿Puedo cambiarle la cerradura?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Materia secundaria: inmobiliario / civil.
- No debe recomendar cambiar cerraduras.
- No debe recomendar sacar al inquilino por la fuerza.
- Puede citar Decreto 4807, artículo 3, solo para indicar que la falta de pago aparece como uno de los supuestos mencionados en el artículo cargado.
- No debe inventar procedimiento judicial, plazos ni forma de ejecución.
- Debe orientar de forma prudente hacia vía legal y revisión por abogado.

---

## Prueba 7 - Corte de servicios

### Pregunta

¿Puedo cortarle la luz o el agua a un inquilino que no paga?

### Resultado esperado

El bot debe:

- Identificar materia principal: inquilinato.
- No recomendar corte de servicios.
- No recomendar presión de hecho.
- Indicar que no tiene artículos específicos cargados para justificar corte de servicios.
- Recomendar usar vías legales y conservar evidencias de mora.
- No inventar sanciones ni procedimientos.

---

## Prueba 8 - Local comercial

### Pregunta

Alquilé un local comercial y me pidieron un anticipo. ¿La Ley 4314 aplica?

### Resultado esperado

El bot debe identificar:

- Materia principal: inquilinato.
- Materia secundaria: inmobiliario / civil.
- Base legal disponible:
  - Ley 4314, artículo 1.
- Debe explicar que el artículo cargado menciona casas, apartamentos, edificios, oficinas, espacios físicos, almacenes, naves industriales e instalaciones para servicios turísticos, hoteleros o de recreación.
- También puede citar Decreto 4807, artículo 1, si la pregunta se relaciona con alquiler de piezas, oficinas, comercio o industria.
- Debe usar lenguaje prudente y citar artículos cargados.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.

---

## Prueba 9 - Procedimiento completo de desalojo

### Pregunta

¿Cuál es el procedimiento completo para desalojar a un inquilino en República Dominicana?

### Resultado esperado

El bot debe:

- Identificar materia principal: inquilinato.
- Materia secundaria: civil / inmobiliario.
- No inventar procedimiento completo.
- Puede citar Decreto 4807, artículo 3, solo para indicar que existen supuestos relacionados con desahucio.
- Como todavía no están cargados todos los artículos del Decreto 4807 ni normas procesales completas, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar el Decreto 4807 completo, Código Civil aplicable, normas procesales y jurisprudencia relacionada.
