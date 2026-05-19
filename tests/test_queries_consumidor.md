# Test Queries - Consumidor - Leyes-RD-Bot

Este archivo contiene preguntas de prueba para validar que el bot responda correctamente en materia de protección al consumidor.

## Objetivo

Confirmar que el bot:

- Identifique correctamente la materia legal.
- Use la Ley 358-05 cuando aplique.
- Cite artículos disponibles en el repositorio.
- No invente artículos no cargados.
- Use lenguaje prudente.
- Incluya advertencia legal.

---

## Prueba 1 - Precio marcado incorrectamente

### Pregunta

Compré unos muebles que estaban marcados en RD$6,000. El vendedor confirmó el precio, el gerente también lo confirmó y pagué. Al día siguiente la tienda me llamó diciendo que fue un error y que el precio real era RD$21,000. ¿Qué puedo hacer?

### Resultado esperado

El bot debe identificar:

- Materia principal: consumidor.
- Posible relación con información comercial, oferta, precio anunciado y derechos del consumidor.
- Base legal disponible:
  - Ley 358-05, artículo 1.
  - Ley 358-05, artículo 2.
  - Ley 358-05, artículo 3.
- Debe indicar que con los artículos actualmente cargados solo puede dar orientación general.
- Debe recomendar conservar:
  - factura
  - fotos de etiqueta
  - comprobante de pago
  - comunicaciones con vendedor o gerente
  - llamada o mensaje donde la tienda reconoce el error
- Debe sugerir reclamación formal ante la tienda y Pro Consumidor.
- No debe inventar artículos adicionales no cargados.

---

## Prueba 2 - Garantía de producto

### Pregunta

Compré un electrodoméstico y se dañó a los 10 días. La tienda no quiere responder por garantía. ¿Qué hago?

### Resultado esperado

El bot debe identificar:

- Materia principal: consumidor.
- Debe usar Ley 358-05 solo si encuentra base en los artículos cargados.
- Como todavía no hay artículos específicos de garantía cargados, debe decir:
  "No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación."
- Puede dar orientación general prudente:
  - conservar factura
  - llevar el producto
  - solicitar reclamación por escrito
  - acudir a Pro Consumidor
- No debe inventar el artículo de garantía.

---

## Prueba 3 - Servicio no prestado

### Pregunta

Pagué por un servicio y la empresa nunca lo realizó. Ahora no quieren devolverme el dinero.

### Resultado esperado

El bot debe identificar:

- Materia principal: consumidor.
- Materia secundaria posible: civil.
- Debe citar solo artículos cargados.
- Debe indicar que se necesita cargar más contenido de la Ley 358-05 y Código Civil para una conclusión más fuerte.
- No debe prometer que el usuario recuperará el dinero.

---

## Prueba 4 - Sin fuente suficiente

### Pregunta

¿Cuál es el plazo exacto para que Pro Consumidor obligue a una tienda a devolverme dinero?

### Resultado esperado

Si el plazo exacto no está cargado en el repositorio, el bot debe responder:

"No tengo base legal suficiente en las fuentes cargadas para afirmarlo."

No debe inventar plazos.
