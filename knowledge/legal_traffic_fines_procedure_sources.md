# Traffic Fines Procedure Sources - Tu Abogado RD

## Propósito

Este archivo registra reglas de orientación prudente para preguntas sobre multas de tránsito en República Dominicana, pago voluntario, impugnación, plazo para pagar o impugnar, rebeldía, recargos, multas a peatones y pasajeros, y límites de lo que el bot puede afirmar cuando no estén cargadas plataformas, bancos, costos o procedimientos completos.

Versión del módulo: **V2.0.8**

---

# Regla principal

Este módulo debe usarse cuando la pregunta trate sobre:

- cómo pagar una multa de tránsito;
- cuánto tiempo tengo para pagar una multa;
- si puedo pagar sin ir al tribunal;
- pago voluntario de multas;
- impugnación de multas;
- plazo de 30 días;
- rebeldía por no pagar ni impugnar;
- recargo por pago tardío;
- multas a peatones;
- multas a pasajeros;
- consecuencias generales de no pagar una multa;
- si una multa puede pagarse en bancos;
- si una multa puede pagarse por plataforma digital;
- si necesito abogado para impugnar;
- si puedo reclamar o pedir revocación de una multa;
- qué pasa si acepto la multa;
- qué pasa si no acepto la multa.

El bot debe responder con base en los artículos cargados de la Ley 63-17 y no debe inventar bancos, plataformas, montos exactos en pesos, formularios, oficinas, tribunal específico por localidad, requisitos no cargados ni pasos procesales completos.

---

# Fuentes principales actualmente cargadas

## Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial

Artículos cargados relevantes:

- Artículo 293: pago voluntario de multa.
- Artículo 294: multas a peatones y pasajeros.
- Artículo 295: plazo para pagar o impugnar multas.
- Artículo 296: tasa de recargo por multas.

Fuente oficial registrada:

- DGII.
- URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf
- Estado de vigencia: pendiente de verificación.

---

# Artículo 293 — Pago voluntario de multa

## Regla cargada

Cuando el infractor decide aceptar la penalidad de una multa, sin acudir a un tribunal de tránsito, puede pagarla directamente en o a través de entidades bancarias autorizadas.

En caso de pago voluntario, el importe a pagar será el de menor cuantía dentro del rango establecido para la sanción correspondiente en la ley.

## Uso permitido

El bot puede afirmar:

- que existe pago voluntario de multas;
- que si el infractor acepta la multa, puede pagar sin acudir al tribunal de tránsito;
- que el pago puede hacerse directamente o a través de entidades bancarias autorizadas;
- que en caso de pago voluntario se paga la menor cuantía dentro del rango legal aplicable a esa infracción.

## Limitación

El bot no debe afirmar:

- bancos específicos autorizados;
- plataformas digitales específicas;
- enlaces de pago;
- oficinas exactas;
- formularios;
- horarios;
- si existe descuento adicional;
- si el pago elimina responsabilidad civil o penal;
- si el pago elimina consecuencias administrativas no cargadas;
- procedimiento práctico completo si no está cargado.

---

# Regla de menor cuantía en pago voluntario

Cuando una infracción tenga una sanción expresada en rango de salarios mínimos, y el usuario pregunte por pago voluntario, el bot puede explicar que el artículo 293 indica que se pagaría la menor cuantía del rango legal.

Ejemplos:

## Multa de 1 a 5 salarios mínimos

- Rango legal cargado: uno (1) a cinco (5) salarios mínimos.
- Pago voluntario según artículo 293: menor cuantía del rango.
- Menor cuantía: un (1) salario mínimo del sector público centralizado.

Si se usa el valor preliminar de RD$10,000.00:

> Tomando como referencia el monto de RD$10,000.00 pesos, el pago voluntario preliminar sería RD$10,000.00. Este cálculo está pendiente de verificación oficial vigente y no debe tomarse como monto oficial definitivo.

## Multa de 1 a 3 salarios mínimos

- Rango legal cargado: uno (1) a tres (3) salarios mínimos.
- Pago voluntario según artículo 293: menor cuantía del rango.
- Menor cuantía: un (1) salario mínimo del sector público centralizado.

Si se usa el valor preliminar de RD$10,000.00:

> Tomando como referencia el monto de RD$10,000.00 pesos, el pago voluntario preliminar sería RD$10,000.00. Este cálculo está pendiente de verificación oficial vigente y no debe tomarse como monto oficial definitivo.

## Multa de 5 a 10 salarios mínimos

- Rango legal cargado: cinco (5) a diez (10) salarios mínimos.
- Pago voluntario según artículo 293: menor cuantía del rango.
- Menor cuantía: cinco (5) salarios mínimos del sector público centralizado.

Si se usa el valor preliminar de RD$10,000.00:

> Tomando como referencia el monto de RD$10,000.00 pesos, el pago voluntario preliminar sería RD$50,000.00. Este cálculo está pendiente de verificación oficial vigente y no debe tomarse como monto oficial definitivo.

## Limitación importante

El bot debe aclarar que el cálculo en pesos usando RD$10,000.00 es preliminar y está pendiente de verificación oficial vigente.

No debe presentar RD$10,000.00 como monto oficial definitivo.

---

# Artículo 295 — Plazo para pagar o impugnar multas

## Regla cargada

La persona contra quien se levante un acta de infracción tiene treinta (30) días para:

- pagar la multa; o
- impugnarla.

La solicitud formal de revocación se hace mediante apoderamiento directo al tribunal competente.

Si no se paga voluntariamente ni se impugna en el plazo establecido, el infractor será declarado en rebeldía.

## Uso permitido

El bot puede afirmar:

- que el plazo cargado para pagar o impugnar es de treinta (30) días;
- que dentro de ese plazo la persona puede pagar o impugnar;
- que la impugnación se realiza mediante solicitud formal de revocación por apoderamiento directo al tribunal competente;
- que si no paga ni impugna dentro del plazo, la persona puede ser declarada en rebeldía.

## Limitación

El bot no debe afirmar:

- tribunal específico por provincia o municipio;
- pasos procesales completos;
- si necesita abogado;
- si puede representarse solo;
- formularios;
- costos judiciales;
- horarios;
- plataforma exacta;
- resultados automáticos;
- si la rebeldía produce impedimento de salida, antecedente penal, arresto o bloqueo de licencia, salvo que una fuente cargada lo confirme.

---

# Artículo 296 — Tasa de recargo por multas

## Regla cargada

Los pagos realizados después de vencido el plazo establecido sin que la persona haya solicitado revocación tendrán un recargo de conformidad con las disposiciones del Código Tributario y leyes complementarias.

## Uso permitido

El bot puede afirmar:

- que puede existir recargo por pago tardío;
- que el recargo aplica cuando se paga después del plazo sin haber solicitado revocación;
- que la Ley 63-17 remite al Código Tributario y leyes complementarias para ese recargo.

## Limitación

El bot no debe:

- calcular el recargo;
- inventar porcentaje;
- inventar monto;
- explicar reglas del Código Tributario si esos artículos no están cargados;
- afirmar consecuencias adicionales no cargadas.

Frase recomendada:

> No puedo calcular el recargo porque las reglas específicas del Código Tributario aplicables al cálculo no están cargadas.

---

# Artículo 294 — Multas a peatones y pasajeros

## Regla cargada

Las multas a peatones y pasajeros se impondrán utilizando el número de cédula de identidad y electoral.

Estas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

## Uso permitido

El bot puede afirmar:

- que las multas a peatones y pasajeros pueden registrarse usando la cédula;
- que la Ley 63-17 indica que esas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

## Limitación

El bot no debe afirmar:

- que toda multa de peatón genera automáticamente antecedente penal;
- consecuencias prácticas específicas no cargadas;
- bloqueo de trámites específicos no cargados;
- procedimiento completo de pago o eliminación;
- tiempo de permanencia del registro;
- si puede impedir trabajo, viaje o renovación de documentos.

---

# Integración con infracciones específicas

Cuando el usuario pregunte por una multa específica, el bot debe combinar:

1. el artículo de la infracción específica; y
2. los artículos de procedimiento de multas cuando el usuario pregunte cómo pagar, impugnar, plazo, pago voluntario, recargo o rebeldía.

Ejemplos:

## Semáforo en rojo

Usar:

- Artículos 133 y 134 para la infracción.
- Artículo 293 si pregunta por pago voluntario.
- Artículo 295 si pregunta plazo para pagar o impugnar.
- Artículo 296 si pregunta recargo por pago tardío.

## Seguro obligatorio

Usar:

- Artículo 217 para la infracción y retención por no portar póliza.
- Artículo 293 si pregunta por pago voluntario.
- Artículo 295 si pregunta plazo para pagar o impugnar.
- Artículo 296 si pregunta recargo.

## Peatón cruzando fuera del paso peatonal

Usar:

- Artículo 218 para la infracción.
- Artículo 294 si pregunta cómo se registra la multa a peatones.
- Artículo 293 si pregunta por pago voluntario.
- Artículo 295 si pregunta plazo.
- Artículo 296 si pregunta recargo.

---

# Respuestas modelo

## Pregunta: “¿Cuánto tiempo tengo para pagar una multa de tránsito?”

✅ Respuesta rápida

La Ley 63-17 establece un plazo de treinta (30) días para pagar la multa o impugnarla.

⚖️ Ley que aplica

Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial, artículo 295.

🛡️ Qué te protege o favorece

Dentro de ese plazo puedes pagar la multa o impugnarla ante el tribunal competente mediante solicitud formal de revocación.

⚠️ Qué no puedo afirmar todavía

No puedo confirmar el tribunal específico, formularios, costos, plataforma exacta o pasos completos porque esos detalles no están cargados.

📚 Fuente consultada

Ley o norma: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial.  
Artículo: 295.  
Materia: tránsito / multas / plazo para pagar o impugnar.  
Fuente oficial: DGII.  
URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf  
Estado de vigencia: pendiente de verificación.

📝 Esto es orientación informativa y no sustituye la revisión de un abogado.

---

## Pregunta: “¿Puedo pagar una multa sin ir al tribunal?”

✅ Respuesta rápida

Sí. La Ley 63-17 permite el pago voluntario cuando el infractor decide aceptar la multa sin acudir al tribunal de tránsito.

⚖️ Ley que aplica

Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial, artículo 293.

🛡️ Qué te protege o favorece

En caso de pago voluntario, el importe a pagar será el de menor cuantía dentro del rango establecido para la sanción correspondiente.

⚠️ Qué no puedo afirmar todavía

No puedo confirmar bancos específicos, plataformas, enlaces de pago, oficinas, horarios ni procedimiento práctico completo porque esos detalles no están cargados.

📚 Fuente consultada

Ley o norma: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial.  
Artículo: 293.  
Materia: tránsito / multas / pago voluntario.  
Fuente oficial: DGII.  
URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf  
Estado de vigencia: pendiente de verificación.

📝 Esto es orientación informativa y no sustituye la revisión de un abogado.

---

## Pregunta: “¿Qué pasa si no pago una multa de tránsito?”

✅ Respuesta rápida

La Ley 63-17 establece que si no pagas voluntariamente ni impugnas dentro del plazo establecido, puedes ser declarado en rebeldía.

⚖️ Ley que aplica

Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial, artículo 295.

⚠️ Recargo

Si el pago se realiza después de vencido el plazo sin haber solicitado revocación, la Ley 63-17 indica que habrá recargo conforme al Código Tributario y leyes complementarias.

⚠️ Qué no puedo afirmar todavía

No puedo calcular el recargo ni confirmar consecuencias adicionales como arresto, antecedentes, bloqueo de licencia, impedimento de salida u otras medidas porque esas reglas específicas no están cargadas.

📚 Fuente consultada

Ley o norma: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial.  
Artículos: 295 y 296.  
Materia: tránsito / multas / rebeldía / recargo.  
Fuente oficial: DGII.  
URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf  
Estado de vigencia: pendiente de verificación.

📝 Esto es orientación informativa y no sustituye la revisión de un abogado.

---

## Pregunta: “Si acepto la multa, ¿cuánto pago?”

✅ Respuesta rápida

Si aceptas la multa y haces pago voluntario, la Ley 63-17 indica que el importe a pagar será el de menor cuantía dentro del rango establecido para la sanción correspondiente.

⚖️ Ley que aplica

Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial, artículo 293.

💰 Cálculo preliminar

Si la infracción tiene una sanción de uno (1) a cinco (5) salarios mínimos del sector público centralizado, la menor cuantía sería un (1) salario mínimo.

Tomando como referencia el monto de RD$10,000.00 pesos, el cálculo preliminar sería RD$10,000.00.

Ese cálculo está pendiente de verificación oficial vigente y no debe tomarse como monto oficial definitivo.

⚠️ Qué no puedo afirmar todavía

No puedo confirmar el monto oficial definitivo en pesos, plataformas, bancos, oficinas o pasos completos porque esos detalles no están cargados.

📚 Fuente consultada

Ley o norma: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial.  
Artículo: 293.  
Materia: tránsito / multas / pago voluntario.  
Fuente oficial: DGII.  
URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf  
Estado de vigencia: pendiente de verificación.

📝 Esto es orientación informativa y no sustituye la revisión de un abogado.

---

# Reglas de estilo

El bot debe evitar repetir varias veces:

- “con las fuentes cargadas”;
- “según las fuentes cargadas”;
- “en las fuentes cargadas”.

Debe preferir:

> Después de revisar las leyes y artículos cargados...

Usar esa frase solo una vez cuando sea necesario.

---

# Fuentes pendientes para completar este módulo

Pendiente cargar fuentes oficiales sobre:

- portal oficial de consulta y pago de multas;
- bancos o entidades autorizadas actualmente;
- procedimiento práctico de pago;
- tribunal competente por localidad;
- formularios o requisitos de impugnación;
- procedimiento completo de revocación;
- cálculo de recargos conforme al Código Tributario;
- consecuencias administrativas prácticas por rebeldía;
- si se requiere abogado para impugnar;
- si la persona puede representarse sola;
- tabla oficial vigente de infracciones y multas.
