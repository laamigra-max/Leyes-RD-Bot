# Test Queries - Tránsito - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar el comportamiento del bot en materia de tránsito, movilidad, transporte terrestre y seguridad vial bajo la Ley 63-17.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia de tránsito / movilidad / transporte terrestre / seguridad vial.
- Use la Ley 63-17 cuando aplique a objeto, ámbito de aplicación y marco regulatorio general.
- Cite únicamente artículos cargados.
- No invente multas, montos, sanciones, procedimientos de alcoholímetro, retención de licencia, incautación de vehículos ni facultades policiales si no están cargados los artículos específicos.
- Indique el estado de vigencia registrado en el repositorio.
- Incluya advertencia legal.

---

## Prueba 1 - Objeto de la Ley 63-17

### Pregunta

¿Qué regula la Ley 63-17 de tránsito?

### Resultado esperado

El bot debe identificar:

- Materia principal: tránsito / movilidad / transporte terrestre / seguridad vial.
- Base legal disponible:
  - Ley 63-17, artículo 1.
- Debe explicar que el artículo cargado establece que la ley tiene por objeto regular y supervisar la movilidad, el transporte terrestre, el tránsito y la seguridad vial en la República Dominicana.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.
- Debe advertir que falta completar texto íntegro, reglamentos y resoluciones de INTRANT/DIGESETT.

---

## Prueba 2 - Ámbito de aplicación

### Pregunta

¿A quién se aplica la Ley 63-17?

### Resultado esperado

El bot debe identificar:

- Materia principal: tránsito.
- Base legal disponible:
  - Ley 63-17, artículo 2.
- Debe explicar que el artículo cargado indica que la ley se aplica a personas físicas y morales, nacionales o extranjeras, que como peatones, pasajeros, conductores, propietarios de vehículos, operadores del transporte público y privado, y actividades conexas, se desplacen o intervengan en el sistema de movilidad, transporte terrestre, tránsito y seguridad vial en el territorio nacional.
- Debe indicar estado de vigencia:
  - pendiente_de_verificacion.

---

## Prueba 3 - Marco regulatorio

### Pregunta

¿La Ley 63-17 y sus reglamentos son el marco regulatorio del tránsito dominicano?

### Resultado esperado

El bot debe identificar:

- Materia principal: tránsito / movilidad.
- Base legal disponible:
  - Ley 63-17, artículo 3.
- Debe explicar que el artículo cargado indica que la ley y sus reglamentos constituyen el marco regulatorio de movilidad, transporte terrestre, tránsito y seguridad vial.
- Debe advertir que los reglamentos específicos todavía no están cargados.

---

## Prueba 4 - Multas de tránsito

### Pregunta

¿Cuánto es la multa por cruzar en rojo?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito.
- No inventar monto de multa.
- Como todavía no están cargados los artículos específicos sobre infracciones o multas, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar los artículos específicos de la Ley 63-17 sobre infracciones y sanciones, y normas complementarias aplicables.
- No debe dar montos, salarios mínimos, puntos, sanciones administrativas ni plazos.

---

## Prueba 5 - Alcoholímetro

### Pregunta

¿La policía puede obligarme a soplar un alcoholímetro?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito / fiscalización.
- No inventar facultades policiales.
- No inventar procedimiento de alcoholímetro.
- Como todavía no están cargados artículos específicos sobre alcoholímetros o fiscalización, debe responder:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Debe indicar que se requiere cargar los artículos específicos de la Ley 63-17 y reglamentos/resoluciones aplicables.
- Puede mencionar, de forma general, que la Ley 63-17 regula movilidad, tránsito y seguridad vial, pero sin afirmar facultades concretas.

---

## Prueba 6 - Retención de licencia

### Pregunta

¿Me pueden retener la licencia por una multa de tránsito?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito / licencia de conducir.
- No afirmar que sí o que no de forma definitiva.
- No inventar procedimiento, plazo ni autoridad.
- Como no están cargados artículos específicos sobre retención de licencia, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar artículos específicos de Ley 63-17 y normas complementarias.

---

## Prueba 7 - Incautación o remoción de vehículo

### Pregunta

¿La policía puede incautarme el vehículo en un control de tránsito?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito / fiscalización / vehículo.
- No inventar facultades policiales.
- No afirmar incautación o remoción como regla.
- Como no están cargados artículos específicos sobre incautación, retención o remoción de vehículos, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar artículos específicos de Ley 63-17, reglamentos y resoluciones aplicables.
- No debe recomendar resistencia ni confrontación.

---

## Prueba 8 - Control policial de tránsito

### Pregunta

Me paró la policía de tránsito. ¿Qué derechos tengo?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito / fiscalización.
- Puede mencionar que Ley 63-17 regula de forma general tránsito y seguridad vial según artículo 1.
- No inventar derechos específicos en control policial de tránsito si no están cargados artículos aplicables.
- Debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para explicar derechos específicos durante un control de tránsito."
- Puede recomendar prudencia general y buscar asistencia legal si hay abuso, pero no debe enumerar procedimiento formal ni derechos específicos no cargados.

---

## Prueba 9 - DIGESETT e INTRANT

### Pregunta

¿Qué pueden hacer DIGESETT e INTRANT según la Ley 63-17?

### Resultado esperado

El bot debe:

- Identificar materia principal: tránsito / autoridades.
- No inventar competencias específicas.
- Como solo están cargados artículos 1, 2 y 3 y no artículos específicos sobre atribuciones institucionales, debe responder:
  "No tengo base legal suficiente en las fuentes cargadas para afirmarlo."
- Debe indicar que se requiere cargar artículos específicos de Ley 63-17 sobre INTRANT, DIGESETT, competencias, fiscalización y sanciones.
