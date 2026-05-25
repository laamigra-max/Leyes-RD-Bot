# Legal Core Sources - Tu Abogado RD

## Propósito

Este archivo consolida las fuentes legales cargadas en el piloto **Tu Abogado RD / Leyes-RD-Bot** para reducir la cantidad de archivos necesarios en el Knowledge del GPT.

Versión actual del piloto legal: **V2.0.1**

Este archivo contiene:

- metadata básica de cada fuente;
- estado de vigencia registrado;
- versión del piloto;
- artículos actualmente cargados;
- limitaciones de uso;
- reglas para evitar respuestas inventadas.

---

# Regla principal de uso

El bot solo debe responder con base en los artículos y fuentes expresamente cargados en este archivo o en otros archivos del Knowledge.

Si el artículo específico no está cargado, el bot debe responder:

> No tengo base legal suficiente en las fuentes cargadas para afirmarlo.

o:

> No encontré un artículo específico en las fuentes cargadas para sostener esa afirmación.

No se deben inventar:

- leyes;
- artículos;
- plazos;
- multas;
- montos;
- penas;
- sanciones;
- procedimientos;
- jurisprudencia;
- requisitos;
- autoridades competentes;
- facultades de autoridades.

---

# V1.0 - Constitución de la República Dominicana 2024

## Metadata

- Título: Constitución de la República Dominicana 2024
- Tipo de norma: Constitución
- Materia: constitucional
- Autoridad emisora: Asamblea Nacional Revisora
- Fuente oficial: https://www.consultoria.gov.do/News/GetNewsDocument?newsId=9357
- Archivo del repositorio: constitucion/constitucion_rd_2024.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.0
- Uso: fuente constitucional prioritaria actual

## Artículos cargados

### Artículo 6 - Supremacía de la Constitución

Todas las personas y los órganos que ejercen potestades públicas están sujetos a la Constitución, norma suprema y fundamento del ordenamiento jurídico del Estado.

Son nulos de pleno derecho toda ley, decreto, resolución, reglamento o acto contrarios a esta Constitución.

## Uso permitido

El bot puede afirmar que:

- la Constitución es norma suprema;
- las personas y órganos públicos están sujetos a la Constitución;
- toda ley, decreto, resolución, reglamento o acto contrario a la Constitución es nulo de pleno derecho, según el artículo cargado.

## Limitación

No inventar procedimientos constitucionales como amparo, acción directa de inconstitucionalidad, control difuso, recursos o plazos si los artículos específicos no están cargados.

---

# V1.1 - Ley 358-05 de Protección de los Derechos del Consumidor o Usuario

## Metadata

- Título: Ley General de Protección de los Derechos del Consumidor o Usuario
- Número: 358-05
- Tipo de norma: ley_ordinaria
- Materia: consumidor
- Autoridad: Pro Consumidor
- Fuente oficial: https://www.proconsumidor.gob.do/files/Ley_General_de_Proteccin_de_los_Derechos_del_Consumidor_o_Usuario_No__358-05.pdf
- Archivo del repositorio: consumidor/ley_358_05_proteccion_consumidor.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.1

## Artículos cargados

### Artículo 1

La presente ley tiene por objeto establecer un régimen de defensa de los derechos del consumidor y usuario que garantice la equidad y seguridad jurídica en las relaciones entre proveedores y consumidores.

En caso de duda, sus disposiciones deben interpretarse de la forma más favorable al consumidor.

### Artículo 2

Las disposiciones de esta ley son de orden público e interés social.

### Artículo 3

Esta ley se aplica a los actos jurídicos celebrados entre proveedores y consumidores o usuarios dentro del territorio nacional.

## Uso permitido

El bot puede afirmar que:

- la Ley 358-05 protege derechos de consumidores y usuarios;
- en caso de duda, las disposiciones cargadas favorecen la interpretación más favorable al consumidor;
- aplica a relaciones entre proveedores y consumidores dentro del territorio nacional, según artículos cargados.

## Limitación

No inventar reglas específicas sobre:

- precio marcado;
- publicidad engañosa;
- garantías;
- devoluciones;
- sanciones;
- procedimientos ante Pro Consumidor;
- plazos de reclamación.

Si el usuario pregunta por esos temas y no hay artículo específico cargado, responder que falta base legal suficiente.

---

# V1.2 - Constitución de la República Dominicana 2015

## Metadata

- Título: Constitución de la República Dominicana 2015
- Tipo de norma: Constitución
- Materia: constitucional
- Autoridad emisora: Asamblea Nacional Revisora
- Fuente oficial: https://presidencia.gob.do/sites/default/files/statics/transparencia/base-legal/Constitucion-de-la-Republica-Dominicana-2015-actualizada.pdf
- Archivo del repositorio: constitucion/constitucion_rd_2015.md
- Estado de vigencia registrado: historica_pendiente_verificacion
- Versión del piloto: V1.2
- Uso: fuente histórica

## Uso permitido

Puede usarse solo como referencia histórica.

## Limitación

No priorizar Constitución 2015 sobre Constitución 2024 para consultas actuales.

---

# V1.3 - Código Civil de la República Dominicana

## Metadata

- Título: Código Civil de la República Dominicana
- Tipo de norma: código
- Materia: civil
- Fuente oficial: https://www.oas.org/dil/esp/C%C3%B3digo%20Civil%20de%20la%20Rep%C3%BAblica%20Dominicana.pdf
- Archivo del repositorio: civil/codigo_civil_rd.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.3

## Uso permitido

Usar únicamente los artículos cargados en el repositorio o Knowledge.

## Limitación

No inventar reglas civiles sobre:

- contratos;
- obligaciones;
- daños y perjuicios;
- prescripción;
- propiedad;
- responsabilidad civil;
- nulidades;
- prueba;
- procedimiento civil.

---

# V1.4 - Código Procesal Penal Ley 76-02

## Metadata

- Título: Código Procesal Penal de la República Dominicana
- Número: 76-02
- Tipo de norma: código
- Materia: penal / procedimiento_penal
- Fuente oficial: https://pgr.gob.do/wpfd_file/ley-no-76-02/
- Archivo del repositorio: penal/codigo_procesal_penal_76_02.md
- Estado de vigencia registrado: pendiente_de_verificacion frente a Ley 97-25
- Versión del piloto: V1.4
- Uso: fuente anterior o histórica pendiente de verificación

## Uso permitido

Puede mencionarse como fuente anterior pendiente de verificación.

## Limitación

No usar como fuente prioritaria para procedimiento penal actual si la Ley 97-25 aplica y está cargada.

---

# V1.5 - Código Procesal Penal Ley 97-25

## Metadata

- Título: Código Procesal Penal de la República Dominicana
- Número: 97-25
- Tipo de norma: ley_organica
- Materia: penal / procedimiento_penal
- Fuente oficial: https://www.consultoria.gov.do/Documents/GetDocument?reference=3d44f7a1-8bbb-4b9f-8564-90f3bad77acb
- Archivo del repositorio: penal/codigo_procesal_penal_97_25.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.5

## Artículos cargados

### Artículo 1

El proceso penal debe realizarse conforme al Código Procesal Penal y con respeto a las garantías procesales.

### Artículo 4

Toda persona tiene derecho a participar en la administración de justicia penal por medio de los mecanismos establecidos en el Código Procesal Penal.

## Uso permitido

El bot puede afirmar de forma general que:

- el proceso penal debe respetar garantías procesales;
- la participación en la justicia penal debe realizarse por los mecanismos establecidos en el Código Procesal Penal.

## Limitación

No inventar procedimiento específico sobre:

- querella;
- denuncia;
- víctima;
- acción penal;
- actor civil;
- Ministerio Público;
- competencia;
- plazos;
- medidas de coerción;
- audiencias;
- depósito;
- requisitos de forma.

Si el usuario pregunta cómo presentar una querella o denuncia y no están los artículos específicos cargados, responder que no hay base suficiente para explicar el procedimiento completo.

---

# V1.6 - Código Penal Ley 74-25

## Metadata

- Título: Código Penal de la República Dominicana
- Número: 74-25
- Tipo de norma: ley_organica
- Materia: penal
- Fuente oficial: https://www.consultoria.gov.do/News/GetNewsDocument?newsId=9359
- Archivo del repositorio: penal/codigo_penal_74_25.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.6

## Artículos cargados

- Artículo 392
- Artículo 393

## Uso permitido

Usar solo los artículos cargados.

## Limitación

No inventar:

- delitos no cargados;
- penas;
- multas penales;
- agravantes;
- atenuantes;
- entrada en vigencia;
- derogaciones;
- disposiciones transitorias.

Ejemplo: si el usuario pregunta por la pena de estafa y no está cargado el artículo de estafa, responder que no hay base legal suficiente.

---

# V1.7 - Ley 4314 de Inquilinato

## Metadata

- Título: Ley 4314 sobre prestación, aplicación y devolución de los valores en el inquilinato
- Número: 4314
- Tipo de norma: ley_ordinaria
- Materia: inmobiliario / inquilinato / alquiler
- Fuente oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/4314.pdf
- Archivo del repositorio: inmobiliario/ley_4314_inquilinato.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.7

## Artículo cargado

### Artículo 1

Los depósitos, adelantos, anticipos u otros valores exigidos o recibidos por el arrendador con motivo de contratos de alquiler deben ser depositados conforme a la ley aplicable.

## Uso permitido

El bot puede orientar sobre depósitos, adelantos, anticipos u otros valores exigidos en contratos de alquiler según el artículo cargado.

## Limitación

No inventar:

- procedimiento completo;
- plazos;
- sanciones;
- devolución;
- intereses;
- competencia;
- jurisprudencia constitucional;
- impacto de TC/0208/21.

La sentencia TC/0208/21 está pendiente de cargar.

---

# V1.8 - Decreto 4807 sobre Control de Alquileres y Desahucios

## Metadata

- Título: Decreto 4807 sobre Control de Alquileres y Desahucios
- Número: 4807
- Tipo de norma: decreto
- Materia: inmobiliario / inquilinato / alquiler / desahucio
- Fuente oficial: https://dgii.gov.do/legislacion/decretos/Documents/2007/Decreto48-07.pdf
- Archivo del repositorio: inmobiliario/decreto_4807_control_alquileres_desahucios.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.8

## Artículos cargados

### Artículo 1

Se crea el Control de Alquileres de Casas y Desahucios.

### Artículo 2

Regula aspectos relacionados con aumento de renta, según el texto cargado.

### Artículo 3

Queda prohibido el desahucio del inquilino por persecución del propietario, salvo en los casos previstos por el decreto, incluyendo la falta de pago del alquiler.

## Uso permitido

El bot puede afirmar con prudencia que:

- el Decreto 4807 crea el Control de Alquileres y Desahucios;
- el artículo 3 cargado menciona la prohibición de desahucio del inquilino por persecución del propietario salvo casos previstos, incluyendo falta de pago.

## Limitación

No inventar:

- procedimiento de desalojo;
- tribunal o autoridad competente;
- plazos;
- documentos;
- intimaciones;
- ejecución;
- uso de fuerza;
- cambio de cerradura;
- corte de servicios.

Nunca recomendar vías de hecho.

---

# V1.9 - Ley 5038 sobre Condominios

## Metadata

- Título: Ley 5038 sobre Condominios
- Número: 5038
- Tipo de norma: ley_ordinaria
- Materia: inmobiliario / condominio / propiedad_horizontal
- Fuente oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/5038.pdf
- Archivo del repositorio: inmobiliario/ley_5038_condominios.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.9

## Artículo cargado

### Artículo 1

La propiedad de edificios de dos o más pisos podrá pertenecer a distintas personas, por pisos, departamentos, viviendas o locales independientes, siempre que los propietarios registren sus derechos conforme al régimen establecido por la ley.

## Uso permitido

El bot puede explicar que el artículo cargado reconoce un régimen donde edificios de dos o más pisos pueden pertenecer a distintas personas por pisos, departamentos, viviendas o locales independientes.

## Limitación

No inventar reglas sobre:

- áreas comunes;
- cuotas de mantenimiento;
- administración;
- asambleas;
- porcentajes de participación;
- sanciones;
- uso exclusivo;
- reglamento de condominio.

---

# V1.10 - Ley 108-05 de Registro Inmobiliario

## Metadata

- Título: Ley 108-05 de Registro Inmobiliario
- Número: 108-05
- Tipo de norma: ley_ordinaria
- Materia: inmobiliario / registro_inmobiliario
- Fuente oficial: https://poderjudicial.gob.do/wp-content/uploads/2021/06/LEY_108_05.pdf
- Archivo del repositorio: inmobiliario/ley_108_05_registro_inmobiliario.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V1.10

## Artículos cargados

### Artículo 1

La presente ley se denomina Ley de Registro Inmobiliario.

### Artículo 2

La presente ley tiene por objeto regular el saneamiento y el registro de todos los derechos reales inmobiliarios, así como las cargas y gravámenes susceptibles de registro, en relación con los inmuebles que conforman el territorio de la República Dominicana.

### Artículo 3

La Jurisdicción Inmobiliaria tiene competencia exclusiva para conocer de todo lo relativo a derechos inmobiliarios y su registro en la República Dominicana, desde que se solicita la autorización para la mensura y durante toda la vida jurídica del inmueble, salvo en los casos expresamente señalados por la ley.

## Uso permitido

El bot puede explicar:

- denominación de la ley;
- objeto general de la Ley 108-05;
- saneamiento;
- registro de derechos reales inmobiliarios;
- cargas y gravámenes susceptibles de registro;
- competencia general de la Jurisdicción Inmobiliaria, según artículos cargados.

## Limitación

No inventar procedimientos sobre:

- deslinde;
- transferencia;
- litis;
- mensura;
- Registro de Títulos;
- recursos;
- nulidad;
- saneamiento completo;
- plazos;
- requisitos.

---

# V2.0 - Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial

## Metadata

- Título: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial
- Número: 63-17
- Tipo de norma: ley_ordinaria
- Materia: tránsito / movilidad / transporte_terrestre / seguridad_vial
- Fuente oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf
- Archivo del repositorio: transito/ley_63_17_transito_movilidad_seguridad_vial.md
- Estado de vigencia registrado: pendiente_de_verificacion
- Versión del piloto: V2.0

## Artículos cargados

### Artículo 1

La presente ley tiene por objeto regular y supervisar la movilidad, el transporte terrestre, el tránsito y la seguridad vial en la República Dominicana.

### Artículo 2

La presente ley es de orden público y de interés social, y sus disposiciones se aplican a todas las personas físicas y morales, nacionales o extranjeras, que como peatones, pasajeros, conductores, propietarios de vehículos, operadores del servicio público y privado de transporte terrestre y sus actividades conexas, se desplacen o intervengan en el sistema de movilidad, transporte terrestre, tránsito y seguridad vial en el territorio nacional.

### Artículo 3

La presente ley y sus reglamentos constituyen el marco regulatorio de la movilidad, el transporte terrestre, el tránsito y la seguridad vial en la República Dominicana.

## Uso permitido

El bot puede explicar:

- objeto general de la Ley 63-17;
- ámbito general de aplicación;
- marco regulatorio general de movilidad, transporte terrestre, tránsito y seguridad vial.

## Limitación estricta V2.0

La Ley 63-17 está cargada solo con artículos 1, 2 y 3, más el módulo V2.0.1 sobre alcohol, alcoholímetro y alcoholemia.

No inventar temas no cargados, incluyendo:

- multas no cargadas;
- montos no cargados;
- sanciones no cargadas;
- puntos de licencia no cargados;
- retención de licencia no cargada;
- suspensión de licencia no cargada;
- incautación de vehículos no cargada;
- retención de vehículos no cargada;
- remoción de vehículos no cargada;
- grúas no cargadas;
- controles policiales no cargados;
- fiscalización vehicular específica no cargada;
- facultades de DIGESETT no cargadas fuera de los artículos de alcoholímetro;
- facultades de INTRANT no cargadas;
- inspecciones no cargadas;
- procedimientos no cargados;
- plazos no cargados;
- requisitos no cargados;
- consecuencias administrativas específicas no cargadas.

## Respuesta obligatoria para preguntas de tránsito no cargadas

Si el usuario pregunta sobre multas, retención de licencia, incautación, remoción, grúas, controles policiales, DIGESETT, INTRANT o fiscalización fuera de los artículos cargados, responder:

> Con las fuentes cargadas, todavía no puedo confirmarte eso. La Ley 63-17 sí está cargada, pero solo tenemos artículos específicos sobre objeto general, ámbito de aplicación, marco general y alcoholímetro/alcoholemia. Para responder sobre ese punto, falta cargar los artículos específicos y los reglamentos o resoluciones aplicables.

---

# V2.0.1 - Alcohol, alcoholímetro y alcoholemia

## Metadata

- Versión del módulo: V2.0.1
- Fuente: Ley 63-17 de Movilidad, Transporte Terrestre, Tránsito y Seguridad Vial
- Materia: tránsito / alcoholímetro / alcoholemia / DIGESETT / seguridad vial
- Estado de vigencia registrado: pendiente_de_verificacion
- Fuente oficial: https://dgii.gov.do/legislacion/leyesTributarias/Documents/Otras%20Leyes%20de%20Inter%C3%A9s/63-17.pdf

## Artículo 256 - Prohibición de conducir en estado de embriaguez

### Resumen normativo cargado

La Ley 63-17 prohíbe a los conductores de vehículos ingerir bebidas alcohólicas mientras transitan por las vías públicas o conducir en estado de embriaguez.

La violación a esta disposición está asociada a multa de cinco (5) a diez (10) salarios mínimos del sector público centralizado y reducción de puntos de la licencia según reglamento, sin perjuicio de disposiciones sobre suspensión y cancelación de licencia.

### Uso permitido

El bot puede afirmar que la Ley 63-17 prohíbe conducir en estado de embriaguez y que el artículo 256 contiene una sanción de multa expresada en salarios mínimos del sector público centralizado y reducción de puntos según reglamento.

### Limitación

No convertir automáticamente esos salarios mínimos a pesos dominicanos si no hay fuente actual cargada sobre el salario mínimo aplicable.

No afirmar puntos específicos de licencia si el reglamento de puntos no está cargado.

No afirmar suspensión o cancelación de licencia si no están cargados los artículos específicos aplicables.

---

## Artículo 257 - Conducción bajo efectos de drogas o sustancias controladas

### Resumen normativo cargado

La Ley 63-17 prohíbe conducir un vehículo bajo los efectos de drogas o sustancias controladas.

La violación a esta disposición está asociada a multa de cinco (5) a diez (10) salarios mínimos del sector público centralizado y reducción de puntos de licencia según reglamento, sin perjuicio de disposiciones sobre suspensión y cancelación de licencia.

### Uso permitido

El bot puede afirmar que está prohibido conducir bajo efectos de drogas o sustancias controladas y que el artículo 257 contiene sanción expresada en salarios mínimos y puntos según reglamento.

### Limitación

No afirmar procedimiento penal o administrativo completo.

No aplicar la Ley 50-88 salvo que el artículo específico o fuente complementaria esté cargada.

No convertir salarios mínimos a pesos dominicanos sin fuente actual cargada.

---

## Artículo 258 - Alcoholemia

### Resumen normativo cargado

La Ley 63-17 considera ilegal conducir un vehículo de motor por vías públicas cuando el grado de alcoholemia sea superior a:

- 0.5 gramos por litro de alcohol en la sangre; o
- 0.25 miligramos por litro en el aire espirado.

Para conductores de transporte público de pasajeros, transporte de carga y personas con permiso de aprendizaje, el límite indicado es:

- 0.0 gramos de alcohol por litro de sangre; o
- 0.0 miligramos por litro en el aire espirado.

Para motocicletas, la ley indica que no deben conducirse con más de:

- 0.2 gramos de alcohol por litro de sangre; o
- 0.1 miligramos por litro en el aire espirado.

### Uso permitido

El bot puede responder preguntas sobre límites de alcoholemia según el artículo 258 cargado.

### Ejemplo permitido

Con las fuentes cargadas, la Ley 63-17 establece en el artículo 258 que para conductores generales es ilegal conducir con alcoholemia superior a 0.5 g/l en sangre o 0.25 mg/l en aire espirado.

Para transporte público, transporte de carga y permiso de aprendizaje, el límite indicado es 0.0.

Para motocicletas, el límite indicado es 0.2 g/l en sangre o 0.1 mg/l en aire espirado.

### Limitación

No afirmar cómo se calibra el equipo ni procedimiento operativo completo si no se cita el artículo 263 o reglamentos complementarios.

---

## Artículo 259 - Prueba del alcoholímetro

### Resumen normativo cargado

La Ley 63-17 establece que las pruebas del alcoholímetro se efectúan sobre conductores y peatones que deben espirar sobre el instrumento, con el propósito de detectar presencia de alcohol en la respiración y determinar el grado consumido.

Cuando la prueba del alcoholímetro resulte positiva, el agente de DIGESETT puede mantener bajo vigilancia al conductor hasta por cuatro (4) horas.

El conductor puede marcharse inmediatamente si se presenta un familiar o relacionado que se responsabilice de llevarlo a su destino.

### Uso permitido

El bot puede afirmar que el artículo 259 regula la prueba del alcoholímetro y la vigilancia de hasta cuatro horas cuando la prueba sea positiva.

### Limitación

No decir que la vigilancia es arresto penal.

No explicar procedimiento de traslado, acta o tribunal si no se está usando también el artículo 263.

---

## Artículo 260 - Prueba toxicológica

### Resumen normativo cargado

La Ley 63-17 regula pruebas toxicológicas mediante toma de saliva con detector de drogas estéril y descartable, debidamente acreditado, para detectar sustancias prohibidas o controladas que disminuyan la aptitud y facultades para conducir.

### Uso permitido

El bot puede explicar que la Ley 63-17 contempla pruebas toxicológicas.

### Limitación

No explicar detalles técnicos del detector, cadena de custodia, laboratorio o procedimiento completo si no están cargados reglamentos o normas complementarias.

---

## Artículo 261 - Pruebas a conductores y peatones

### Resumen normativo cargado

La Ley 63-17 autoriza a los agentes de DIGESETT a practicar a conductores y peatones controles de alcoholemia o toxicológicos para comprobar la existencia de alcohol o drogas, en determinaciones cualitativas o cuantitativas, cuando disminuyan la aptitud y facultades para conducir o circular.

Cuando esos procedimientos impliquen pruebas orgánicas o invasivas, conductores o peatones deben otorgar su consentimiento.

Dichos controles deben realizarse con respeto a la dignidad e integridad de las personas.

### Uso permitido

El bot puede afirmar que el artículo 261 autoriza controles de alcoholemia o toxicológicos por agentes de DIGESETT y que, si son pruebas orgánicas o invasivas, se requiere consentimiento y respeto a la dignidad e integridad.

### Limitación

No afirmar que toda prueba requiere consentimiento.

Distinguir entre soplar alcoholímetro y pruebas orgánicas o invasivas.

---

## Artículo 262 - Pruebas aleatorias a conductores

### Resumen normativo cargado

La Ley 63-17 permite practicar alcoholimetría o prueba toxicológica de manera preventiva, circunstancial o como parte de operativos a personas en lugares públicos que pretendan conducir un vehículo de motor, cuando el agente considere que su comportamiento es inadecuado y presenta síntomas evidentes de disminución de aptitud y facultades para conducir.

### Uso permitido

El bot puede explicar que la ley contempla pruebas preventivas o aleatorias en las condiciones indicadas por el artículo 262.

### Limitación

No afirmar que cualquier persona puede ser sometida a prueba en cualquier circunstancia sin analizar los supuestos del artículo.

---

## Artículo 263 - Procedimiento para alcoholimetría y pruebas toxicológicas

### Resumen normativo cargado

La Ley 63-17 establece que los agentes de DIGESETT realizarán alcoholimetría y pruebas toxicológicas con instrumentos que garanticen calidad de medición o detección, certificados y calibrados, usando con cada individuo un dispositivo personal de material descartable.

Si el conductor se niega a realizarse la prueba, el agente de DIGESETT debe hacerlo constar en el acta levantada al efecto y conducirlo al Tribunal Especial de Tránsito más cercano o al juzgado de paz correspondiente.

Si se dificulta constatar el nivel de alcohol por causa atribuible al conductor, se procede igual que ante la negativa.

Si la prueba resulta positiva, el conductor puede solicitar análisis confirmatorios como contraprueba.

Los gastos médicos, insumos u otros derivados de la prueba solicitada estarán a cargo del interesado.

### Uso permitido

El bot puede responder preguntas sobre negativa al alcoholímetro, acta, tribunal o juzgado de paz y contraprueba, siempre citando el artículo 263.

### Limitación

No afirmar resultado judicial, arresto definitivo, condena, antecedentes, multas exactas adicionales ni procedimiento completo fuera de lo expresamente cargado.

---

# Respuestas modelo permitidas para alcoholímetro

## Pregunta: ¿La policía o DIGESETT puede pedirme soplar un alcoholímetro?

Respuesta modelo:

Con las fuentes cargadas, sí hay base para decir que la Ley 63-17 regula la prueba del alcoholímetro.

La ley que aplica es la Ley 63-17, artículos 259, 261 y 263. El artículo 259 habla de la prueba del alcoholímetro sobre conductores y peatones; el artículo 261 autoriza a agentes de DIGESETT a practicar controles de alcoholemia o toxicológicos; y el artículo 263 regula el procedimiento con equipos certificados/calibrados y dispositivo personal descartable.

Lo que te protege o favorece es que, si se trata de pruebas orgánicas o invasivas, el artículo 261 exige consentimiento y respeto a la dignidad e integridad. Además, el artículo 263 permite solicitar análisis confirmatorios si la prueba resulta positiva.

Esto es orientación informativa y no sustituye la revisión de un abogado.

## Pregunta: ¿Qué pasa si me niego al alcoholímetro?

Respuesta modelo:

Con las fuentes cargadas, el artículo 263 de la Ley 63-17 dice que si el conductor se niega a realizarse la prueba, el agente de DIGESETT debe hacerlo constar en un acta y conducirlo al Tribunal Especial de Tránsito más cercano o al juzgado de paz correspondiente.

No puedo afirmar el resultado judicial ni una sanción final automática, porque eso dependería del caso y de normas o procedimientos adicionales.

Esto es orientación informativa y no sustituye la revisión de un abogado.

## Pregunta: ¿Cuál es el límite de alcohol permitido?

Respuesta modelo:

Con las fuentes cargadas, la Ley 63-17 establece en el artículo 258 que para conductores generales se considera ilegal conducir con alcoholemia superior a 0.5 gramos por litro de sangre o 0.25 miligramos por litro en aire espirado.

Para transporte público, transporte de carga y personas con permiso de aprendizaje, el límite indicado es 0.0.

Para motocicletas, el límite indicado es 0.2 gramos por litro de sangre o 0.1 miligramos por litro en aire espirado.

Esto es orientación informativa y no sustituye la revisión de un abogado.

---

# Fuentes pendientes para próximas fases

## V2.1 - Código de Trabajo Ley 16-92

Pendiente de cargar.

No calcular prestaciones, derechos laborales, plazos, cesantía, preaviso, vacaciones, salario de Navidad, despido o dimisión hasta cargar artículos específicos.

## V2.2 - Ley Monetaria y Financiera No. 183-02

Pendiente de cargar.

No afirmar reglas bancarias específicas hasta cargar artículos aplicables.

## V2.3 - Reglamento o normas de protección al usuario financiero

Pendiente de cargar.

No afirmar procedimientos, plazos o derechos específicos del usuario financiero hasta cargar la fuente.

## V2.4 - Sentencia TC/0208/21 sobre Ley 4314

Pendiente de cargar.

No aplicar su criterio como fuente activa hasta cargar y verificar la sentencia.

---

# Reglas para preguntas de procedimiento

Si el usuario pregunta:

- cómo hacer;
- cómo presentar;
- cuáles son los pasos;
- qué documentos necesito;
- dónde se deposita;
- cuál es el procedimiento;
- cómo hago una querella;
- cómo hago una denuncia;
- cómo demando;
- cómo hago un deslinde;
- cómo reclamo;
- cómo desalojo.

Solo dar pasos concretos si los artículos específicos del procedimiento están cargados.

Si no están cargados, responder:

> No tengo base legal suficiente en las fuentes cargadas para explicar el procedimiento completo.

No enumerar documentos, pasos, plazos, autoridad competente ni requisitos si no están respaldados por fuentes cargadas.

---

# Estilo recomendado de respuesta

Responder de forma sencilla, amigable y profesional.

Formato recomendado:

## Respuesta rápida

Explicar en una o dos frases.

## Ley que aplica

Mencionar ley, artículo cargado y estado.

## Qué te protege o favorece

Explicar de forma práctica qué parte de la fuente cargada ayuda al usuario.

## Qué no puedo afirmar todavía

Decir claramente qué falta cargar.

## Próximo paso prudente

Dar orientación general segura sin inventar procedimiento.

## Advertencia breve

> Esto es orientación informativa y no sustituye la revisión de un abogado.
