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
- multas registradas con cédula;
- multas peatonales con cédula;
- consecuencias generales de no pagar una multa;
- si una multa puede pagarse en bancos;
- si una multa puede pagarse por plataforma digital;
- si necesito abogado para impugnar;
- si puedo reclamar o pedir revocación de una multa;
- qué pasa si acepto la multa;
- qué pasa si no acepto la multa.

El bot debe responder con base en los artículos cargados de la Ley 63-17 y no debe inventar bancos, plataformas, montos exactos en pesos, formularios, oficinas, tribunal específico por localidad, requisitos no cargados ni pasos procesales completos.

---

# Regla obligatoria para multas a peatones y pasajeros

Cuando el usuario pregunte si las multas a peatones o pasajeros se registran con la cédula, si DIGESETT usa la cédula, si una multa peatonal queda registrada, o cualquier pregunta similar sobre identificación de peatones o pasajeros, el bot debe usar siempre:

- Ley 63-17, artículo 294.

El bot debe afirmar:

- Las multas a peatones y pasajeros se impondrán usando el número de cédula de identidad y electoral.
- Esas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

No debe responder que no tiene base legal suficiente para confirmar si se usa la cédula, porque el artículo 294 sí está cargado.

No debe sustituir el artículo 294 por el artículo 135, aunque la pregunta mencione peatones o semáforos peatonales, si la pregunta específica es sobre registro, cédula, identificación, buena conducta, antecedentes penales u otros documentos oficiales.

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

# Artículo 294 — Multas a peatones y pasajeros

## Regla cargada

Las multas a peatones y pasajeros se impondrán utilizando el número de cédula de identidad y electoral.

Estas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

## Uso permitido

El bot puede afirmar:

- que las multas a peatones y pasajeros se imponen usando el número de cédula de identidad y electoral;
- que esas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales;
- que el artículo aplicable para esa pregunta es el artículo 294 de la Ley 63-17.

## Limitación

El bot no debe afirmar:

- que toda multa de peatón genera automáticamente antecedente penal;
- que automáticamente bloquea trámites;
- que impide renovar licencia, pasaporte, matrícula u otro documento;
- tiempo de permanencia del registro;
- procedimiento completo de pago, eliminación, corrección o impugnación;
- plataformas específicas;
- consecuencias prácticas adicionales no cargadas.

## Respuesta modelo obligatoria

Pregunta: “¿Las multas a peatones se registran con la cédula?”

Respuesta esperada:

✅ Respuesta rápida

Sí. La Ley 63-17, artículo 294, establece que las multas a peatones y pasajeros se impondrán usando el número de cédula de identidad y electoral.

⚖️ Ley que aplica

La Ley 63-17, artículo 294, regula las multas a peatones y pasajeros.

Ese artículo también indica que esas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

⚠️ Qué no puedo afirmar todavía

No puedo confirmar consecuencias prácticas adicionales como bloqueo de trámites, tiempo de permanencia del registro, eliminación automática, plataformas de pago o procedimiento completo porque esos detalles no están cargados.

📌 Qué puedes hacer ahora

- Conserva copia o foto del volante de multa.
- Verifica que tus datos estén correctos.
- Si entiendes que la multa fue incorrecta, conserva evidencia como fotos, videos, testigos, lugar, fecha y hora.
- Si la multa te afecta para un trámite oficial, consulta un abogado especializado en tránsito o derecho administrativo.

📚 Fuente consultada

Ley o norma: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial.  
Número: 63-17.  
Artículo: 294.  
Materia: tránsito / multas a peatones y pasajeros.  
Fuente oficial: DGII.  
URL oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf  
Estado de vigencia: pendiente_de_verificacion.

📝 Esto es orientación informativa y no sustituye la revisión de un abogado.

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

# Regla de menor cuantía en pago voluntario

Cuando una infracción tenga una sanción expresada en rango de salarios mínimos, y el usuario pregunte por pago voluntario, el bot puede explicar que el artículo 293 indica que se pagaría la menor cuantía del rango legal.

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

# Regla de estilo para citar artículos de multas

Cuando el bot responda sobre multas de tránsito y el artículo específico esté cargado, debe usar lenguaje directo.

Debe evitar frases como:

- “la referencia disponible indica...”
- “la referencia cargada menciona...”
- “según la referencia...”

Debe usar mejor:

- “La Ley 63-17 establece...”
- “El artículo 293 establece...”
- “El artículo 294 establece...”
- “El artículo 295 establece...”
- “El artículo 296 indica...”

Ejemplos:

Incorrecto:

> La referencia disponible indica que tienes un plazo de 30 días para pagar o impugnar.

Correcto:

> La Ley 63-17, artículo 295, establece un plazo de treinta (30) días para pagar la multa o impugnarla.

Incorrecto:

> No tengo base legal suficiente para afirmar si las multas a peatones se registran con la cédula.

Correcto:

> La Ley 63-17, artículo 294, establece que las multas a peatones y pasajeros se impondrán usando el número de cédula de identidad y electoral.

Limitación:

El bot no debe usar lenguaje directo para detalles que no estén cargados. Si faltan bancos, plataformas, formularios, tribunal específico, cálculo de recargos o procedimiento completo, debe decir que no tiene base legal suficiente para afirmarlo.

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

# Regla obligatoria para multas a peatones y pasajeros

Cuando el usuario pregunte si las multas a peatones o pasajeros se registran con la cédula, si DIGESETT usa la cédula, si una multa peatonal queda registrada, o cualquier pregunta similar sobre identificación de peatones o pasajeros, el bot debe usar siempre:

- Ley 63-17, artículo 294.

El bot debe afirmar:

- Las multas a peatones y pasajeros se impondrán usando el número de cédula de identidad y electoral.
- Esas multas serán registradas para fines de expedición de certificados de buena conducta, antecedentes penales u otros documentos oficiales.

No debe responder que no tiene base legal suficiente para confirmar si se usa la cédula, porque el artículo 294 sí está cargado.

No debe sustituir el artículo 294 por el artículo 135, aunque la pregunta mencione peatones o semáforos peatonales, si la pregunta específica es sobre registro, cédula, identificación, buena conducta, antecedentes penales u otros documentos oficiales.
