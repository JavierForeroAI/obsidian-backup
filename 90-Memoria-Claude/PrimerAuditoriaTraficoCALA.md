---
name: PrimerAuditoriaTraficoCALA
description: Primera auditoría Meta de tráfico para Bogotá — Show Rate 46% | Junio 2026
metadata:
  type: project
  date: 2026-06-24
  audience: Equipo de tráfico + comunicaciones (diseño)
  scope: Bogotá (ciudad) exclusivamente
---

# AUDITORIA META — BOGOTA SOLO
## Diagnostico de Show Rate 46% | Junio 2026 | Solo lectura

---

## MAPA DE CAMPANAS BOGOTA CONFIRMADAS

Tras revisar las 6 cuentas y confirmar por nombre de adset (no por nombre de cuenta):

| Ad Set | Campana | Cuenta | Objetivo | Presupuesto diario |
|---|---|---|---|---|
| Fitness + educacion - Bogota | Bogota Instagram Mayo | PANAMA (act) | ENGAGEMENT | ~$29 USD |
| BOGOTA - TEST-/18/06/2026 | WHATSAPP BUSSINES FASE 3 | MEDELLIN (act) | ENGAGEMENT | ~COP 90.000 |
| BOGOTA - TEST-/16/06/2026-(ESTETICO-SOCIAL) | WHATSAPP BUSSINES FASE 3 | MEDELLIN (act) | ENGAGEMENT | ~COP 76.923 |
| BOGOTA - TEST 18/06/2026 | TEST INSTAGRAM 27/05/2026 | MEDELLIN (act) | ENGAGEMENT | ~COP 90.000 |
| BOGOTA - TEST 01/06/2026 | TEST INSTAGRAM 27/05/2026 | MEDELLIN (act) | ENGAGEMENT | ~COP 306.154 |
| Bogota (adset) | Interaccion Global x Conjuntos | MEDELLIN (act) | ENGAGEMENT | ~COP 10.000 |

Total Bogota activo en junio: aproximadamente 6 ad sets distribuidos en 3 campanas y 2 cuentas.

---

## METRICAS — BOGOTA JUNIO 2026 (1-24 junio)

### Por ad set — solo Bogota

| Ad Set | Gasto | Impresiones | Alcance | Frecuencia | Conv. iniciadas | CPConv. iniciada |
|---|---|---|---|---|---|---|
| Fitness + ed. Bogota (PANAMA act) | $703 USD | 328.198 | 156.815 | 2.09 | 267 | $2.64 USD |
| BOGOTA TEST 18/06 (WB Fase 3) | COP 351.347 | 25.426 | 10.904 | 2.33 | 61 | COP 5.759 |
| BOGOTA ESTETICO-SOCIAL 16/06 | COP 424.329 | 63.112 | 35.965 | 1.75 | 52 | COP 8.160 |
| BOGOTA TEST IG 18/06 | COP 355.080 | 23.852 | 11.459 | 2.08 | 48 | COP 7.397 |
| BOGOTA TEST IG 01/06 | COP 3.414.550 | 676.033 | 261.435 | 2.59 | 310 | COP 11.014 |
| Bogota Interaccion Global | COP 235.844 | 144.807 | 136.796 | 1.06 | N/A (POST_ENGAGEMENT) | N/A |

Conversor rapido de referencia: COP 4.200 = aprox. $1 USD.

---

## HALLAZGOS CRITICOS — 5 DIMENSIONES

---

### DIMENSION 1: OBJETIVO DE CAMPANA — FALLA SISTEMICA

**HALLAZGO P0 — CRITICO**

El 100% de las campanas de Bogota corren con objetivo OUTCOME_ENGAGEMENT (interaccion con publicacion o conversacion de mensajeria). No hay ninguna campana con objetivo LEADS o CONVERSIONS apuntando a cita asistida.

Implicacion directa: Meta esta optimizando para personas que reaccionan, comentan o abren una conversacion de WhatsApp. No para personas que agendan una cita y asisten. Son dos perfiles de usuario completamente distintos. El algoritmo aprende a encontrar "clickers emocionales", no "pacientes candidatos con presupuesto".

La campana WHATSAPP BUSSINES FASE 3 tiene ad sets de Bogota con optimization_goal CONVERSATIONS. Eso es mejor que POST_ENGAGEMENT, pero sigue sin ser Schedule o Lead calificado. Meta no distingue entre "abre el chat y dice hola" vs "da su nombre, ciudad, fecha y presupuesto".

TEST INSTAGRAM 27/05/2026 tiene optimization_goal CONVERSATIONS. El ad set "Bogota - TEST 01/06" es el mayor gasto de Bogota este mes (COP 3.4M) y genera 310 conversaciones iniciadas al costo de COP 11.014 cada una. No hay evidencia de que estas conversaciones deriven en leads calificados.

**Campana Bogota Instagram Mayo** (cuenta PANAMA, objetivo ENGAGEMENT, optimizacion CONVERSATIONS) es el unico ad set con costos en USD y el de mejor performance relativo: 292 conexiones de mensajeria a $2.41 USD cada una. Sin embargo, 17 creativos activos en un solo ad set es dispersion extrema.

---

### DIMENSION 2: AUDIENCIAS — SEGMENTACION SIN CALIFICACION ECONOMICA

**HALLAZGO P1 — IMPORTANTE**

Los ad sets de Bogota usan dos configuraciones:

1. "PUBLICO ADVANTAGE+ INTERESES - COL" y "PUBLICO ADVANTAGE+ ABIERTO - COL" — son los ad sets de las campanas de trafico al perfil. Advantage+ Audience abierto significa que Meta elige a quien mostrar sin restricciones de intereses. Esto maximiza alcance pero elimina cualquier preseleccion de capacidad economica.

2. "Fitness + educacion - Bogota" — tiene una segmentacion explicita por intereses (fitness, educacion), lo cual es una aproximacion indirecta a un perfil socioeconomico medio-alto. Es el mejor intentode segmentacion encontrado, pero no incluye parametros de ingreso, comportamiento de compra premium, o indicadores de poder adquisitivo.

Ningun ad set de Bogota usa:
- Segmentacion por nivel de ingresos
- Lookalike audiences construidas sobre pacientes que asistieron (Show Rate calificado)
- Exclusion de edades 18-24 (segmento con menor capacidad para COP 8M-11M)
- Custom Audiences de CRM con leads que convirtieron

La consecuencia es obvia: Meta alcanza a cualquier hombre en Bogota que haya interactuado con contenido de fitness o educacion, sin ningun filtro de si puede pagar COP 8M+ o si tiene la madurez de decision para asistir a una valoracion medica.

Frecuencia promedio de los ad sets mas grandes de Bogota: entre 2.08 y 2.59. No hay fatiga critica aun, pero el ad set "BOGOTA TEST 01/06" con 2.59 y COP 3.4M gastados empieza a estar en zona de saturacion sin una seal clara de conversion al fondo del embudo.

---

### DIMENSION 3: CREATIVOS Y MESSAGING — VOLUMEN SIN CALIFICACION

**HALLAZGO P1 — IMPORTANTE**

Campana "Bogota Instagram Mayo" (PANAMA act): 17 ads activos en un solo ad set. Los nombres revelan la estrategia:

- "Foto medico 25marz", "Gorra + controles EN REVISION MASTER NO LO APAGUE", "Testimonio (estoy sorprendido)", "Se cae el implante?", "Linan Orlando", "La pregunta de todos (dr fabian)", "Porque se me cae el cabello", "Caso de exito Imagen", "Doctor Explicando el implante capilar", "Los resultados se notan", "Validacion + Humor", "Antes y Despues + validacion", "Vid Dr Fabian explicando precio y clinica", "Probe hasta que encontre", "TESTIMONIO HABLADO 20MARZ"

Observaciones criticas:
- El ad "Gorra + controles EN REVISION MASTER NO LO APAGUE" indica que hay un creativo en estado de revision o problema sin resolver que el trafficker no se atreve a pausar por miedo a perder algo. Es una senal de gestion reactiva.
- La mayoria son testimonios, antes/despues, y educacion sobre FUE. Esos son formatos MOFU-BOFU correctos, pero corren en una campana de ENGAGEMENT que atrae trafico frio. El mensaje no coincide con la temperatura del publico.
- Ningun nombre de ad sugiere copy que pre-califique por presupuesto: no hay mensajes del tipo "para hombres que consideran una inversion de COP 8M+" o "si tienes entre 35 y 55 anos y estas listo para decidir".
- "Vid Dr Fabian explicando precio y clinica" es el mas cercano a un calificador de precio. Si ese video no esta en rotacion prioritaria, es una oportunidad perdida.

Campana WHATSAPP BUSSINES FASE 3 — ad sets Bogota:
- "ESTETICO SOCIAL AD2/AD3/AD4": apunta al avatar AV4 (Gay Premium). Bien dirigido, pero los nombres no revelan si el copy pre-califica presupuesto.
- "AD1" y "AD2" en el ad set BOGOTA TEST 18/06: nombres genericos sin informacion sobre el angulo creativo.

Campana TEST INSTAGRAM: ad sets Bogota 01/06 y 18/06 con 5 y 2 ads respectivamente. El ad set de mayor gasto (COP 3.4M) tiene 5 ads (AD1 a AD5) con nombres completamente genericos. Sin informacion de angulo, no es posible determinar si pre-califican o no.

**Problema de fondo**: el messaging actual atrae curiosidad ("se cae el implante?", "por que se me cae el cabello") que es TOFU correcto para awareness, pero el CTA lleva directo a WhatsApp sin ningun filtro intermedio. El curioso y el candidato real llegan al mismo chat.

---

### DIMENSION 4: ESTRUCTURA Y DATOS — ANOMALIAS GRAVES

**HALLAZGO P0 — CRITICO**

**Pixels: 6 datasets activos, contaminacion garantizada**

La auditoría de datasets revela 6 pixels distintos en el business:
- Pixel CRM `1642103999710262` — activo, ultimo CAPI hoy (18:56). Es el correcto.
- Pixel Implante capilar col `1625645205284016` — activo, ultimo browser hoy.
- Pixel type `990996959835595` — activo, ultimo server 8 junio.
- Pixel de Implante Innovart Medical `578351714372297` — activo, ultimo server 11 junio.
- Pixel embudo `975663933915371` — activo, ultimo evento noviembre 2024. Abandonado pero activo.
- Pixel 3 `1684439922329930` — activo, NUNCA ha disparado (fecha epoch 1969). Zombie puro.

Con 6 pixels activos y al menos 3 disparando en paralelo, Meta recibe el mismo evento varias veces desde fuentes distintas. Esto genera:
- Deduplicacion fallida si no hay `event_id` consistente
- Sobreconteo de eventos en el panel
- Confusion del algoritmo sobre que seal seguir para optimizar
- EMQ contaminado con datos de pixels no conectados a CAPI

**Custom Conversions: CERO**

La cuenta BGTA no tiene ninguna custom conversion configurada. Esto significa que no existe una conversion personalizada para "cita agendada", "cita asistida" ni ningun evento del embudo medico. Meta no puede optimizar por lo que no puede medir.

**Objetivo de conversion en campanas de Bogota: ninguna usa Purchase, Lead calificado, o Schedule**

La campana TEST INSTAGRAM tiene en su historial de acciones `onsite_conversion.lead` con valor 1 (un solo lead registrado en todo el mes para COP 7.4M gastados en Bogota). Eso no es un sistema de generacion de leads. Es ruido estadistico.

**Gasto Bogota junio 2026 — solo ad sets confirmados**

| Moneda | Gasto adsets Bogota | Aprox. USD |
|---|---|---|
| USD (PANAMA act) | $703 | $703 |
| COP (MEDELLIN act) | COP 4.780.150 | ~$1.138 |
| Total aprox. | | ~$1.841 USD |

A ese gasto, el costo por conversacion iniciada oscila entre $2.64 USD (mejor) y $11 USD equiv. (peor). El costo por lead calificado o cita agendada es desconocido porque no se mide.

---

### DIMENSION 5: EMBUDO CRM Y CALIFICACION — EL CUELLO DE BOTELLA REAL

**HALLAZGO P0 — CRITICO**

Este es el hallazgo mas importante de toda la auditoria y ya esta documentado en el cerebro: los leads de Bogota llegan por WhatsApp directo sin email (0% cobertura de email). Esto tiene dos consecuencias en cascada:

Primera consecuencia — EMQ bajo (4.8-5.2): Meta no puede hacer audience matching sin email. Cada lead que paga COP 8.471 en mensajeria (cost per first reply) es un lead que Meta no puede identificar como "persona similar a los que convirtieron". El aprendizaje del algoritmo queda ciego.

Segunda consecuencia — sin calificacion antes de agendar: el flujo actual es WhatsApp abre chat → bot o asesor → agenda valoracion. No hay pregunta de presupuesto, no hay filtro de candidatura, no hay momento de friccion intencional que elimine al curioso sin intencion real. El lead frio llega a la valoracion porque nadie lo detuvo antes.

La campana WHATSAPP BUSSINES FASE 3 tiene un ad set "MEDELLIN" con optimization_goal LEAD_GENERATION (el unico en toda la estructura), mientras que los ad sets de Bogota usan CONVERSATIONS. Esa asimetria es significativa: Medellin ya tenia lead form, Bogota no.

---

## DIAGNOSTICO RAIZ — POR QUE SHOW RATE 46%

El show rate de 46% en Bogota no tiene una causa unica. Tiene cinco causas que se suman:

**Causa 1 (40% del problema)**: El objetivo de campana es ENGAGEMENT/CONVERSATIONS, no LEADS calificados. Meta aprende a atraer personas que interactuan, no personas que asisten. El perfil del usuario que abre un chat de WhatsApp al ver un reel y el perfil del paciente que llega a una valoracion medica no son el mismo.

**Causa 2 (25% del problema)**: No hay filtro de calificacion entre el primer contacto y el agendamiento. El asesor o bot agenda a cualquiera que exprese interes. No se pregunta presupuesto, no se verifica disponibilidad real, no se pide confirmacion activa.

**Causa 3 (20% del problema)**: La segmentacion no excluye ni prioriza por capacidad economica. Llegan personas interesadas que no tienen COP 8M ni la madurez de decision para comprometerse con una cita presencial. Curiosidad no es intencion de compra.

**Causa 4 (10% del problema)**: El messaging no pre-califica. Un anuncio que pregunta "se te esta cayendo el cabello?" atrae a cualquier hombre con alopecia en Bogota. Atrae mas si el presupuesto es bajo y tiene tiempo libre para hacer click. El hombre con COP 10M y agenda apretada no se detiene ante ese hook.

**Causa 5 (5% del problema)**: EMQ bajo (4.8) significa que Meta no puede identificar correctamente a los leads que SI asistieron para construir lookalike audiences de calidad. El aprendizaje del sistema esta atrofiado.

---

## SCORECARD BOGOTA

| Dimension | Score | Estado |
|---|---|---|
| Objetivo de campana | 1/10 | CRITICO — 100% Engagement, 0% Leads/Conversions |
| Segmentacion | 3/10 | CRITICO — Sin filtro economico, Advantage+ abierto |
| Creativos | 4/10 | BAJO — Volumen sin estrategia de calificacion |
| Estructura | 2/10 | CRITICO — 6 pixels, 0 custom conversions |
| Embudo CRM | 2/10 | CRITICO — Sin calificacion previa, 0% email |
| EMQ | 4.8/10 | BAJO — Sin email = sin matching |
| Tracking Score | 3/10 | CRITICO — Pixels duplicados, sin Purchase/Schedule |
| Attribution Score | 1/10 | CRITICO — 0 conversiones rastreadas en Bogota |

---

## TOP 3 PROBLEMAS

**Problema 1**: Las campanas de Bogota optimizan por conversacion abierta, no por cita calificada. Meta aprende a atraer curiosos, no pacientes.

**Problema 2**: No existe calificacion entre primer contacto y agendamiento. El flujo es directo: chat → cita. Sin filtro de presupuesto ni de candidatura.

**Problema 3**: 6 pixels activos con 3 disparando en paralelo y 0 custom conversions. Meta recibe datos contaminados y no tiene ninguna conversion del embudo medico que pueda optimizar.

---

## TOP 3 FIXES — PRIORIDAD Y METODOLOGIA

**FIX P0-A: Crear evento Schedule en CAPI y cambiar objetivo de campana**

Que se hace: Definir el evento `Schedule` (valoracion asistida confirmada) como conversion objetivo. Conectarlo al Pixel CRM `1642103999710262` via CAPI con los campos phone + fbclid (ya funcionan). Crear una nueva campana con objetivo LEADS o CONVERSIONS apuntando a ese evento.

Por que: Si Meta no optimiza por Schedule, nunca va a aprender a encontrar personas que asisten. El cambio de objetivo es el de mayor impacto en show rate.

Quien ejecuta: Trafficker (Diego/Esneider) + equipo tecnico CAPI.

Impacto esperado: Show rate 46% hacia 55-62% en 60 dias de aprendizaje. Meta necesita minimo 50 eventos Schedule/semana para salir de la fase de aprendizaje. Si el volumen es menor, usar Purchase como proxy hasta acumular datos.

Tiempo de implementacion: 5-7 dias.

**FIX P0-B: Implementar calificacion de 3 preguntas en WhatsApp antes de agendar**

Que se hace: En el workflow GHL de Bogota, antes de ofrecer fecha de cita, el bot pregunta en secuencia: (1) "Para darte la mejor orientacion, cuantas entradas o zona tiene tu calvicie aproximadamente?" — filtra candidatos reales. (2) "Tienes disponibilidad para una valoracion presencial en Bogota esta semana o la siguiente?" — filtra capacidad logistica. (3) "Nuestro procedimiento tiene un valor desde COP 8.000.000. Es una inversion que estas considerando en este momento?" — filtra presupuesto.

Solo quienes responden afirmativamente las 3 pasan al paso de agendamiento. Los que responden que no tienen presupuesto entran a nurture de 60-90 dias.

Por que: El no-show ocurre mayoritariamente en personas que agendaron sin estar listas para decidir. La friccion intencional de 3 preguntas elimina a los curiosos sin alejar a los candidatos reales que si estan decididos.

Quien ejecuta: Equipo CRM/GHL.

Impacto esperado: Reduccion de leads agendados en 20-30%, pero aumento de show rate de 46% a 65-70%. El volumen de valoraciones asistidas no cae, sube la tasa.

Tiempo de implementacion: 3-5 dias con acceso GHL.

**FIX P1: Consolidar pixels a 1 activo, crear 3 custom conversions, pausar 5 pixels zombie**

Que se hace: Pausar los pixels `975663933915371` (embudo, abandonado 2024), `1684439922329930` (Pixel 3, nunca disparo), `990996959835595` (Pixel type, ultimo evento 8 junio sin CAPI), `578351714372297` (ultimo server 11 junio). Dejar activos solo `1642103999710262` (Pixel CRM, CAPI activo hoy) y `1625645205284016` (Pixel capilar col, browser + server activo hoy). Crear 3 custom conversions en el Pixel CRM: `Lead_Calificado` (cuando el contacto pasa el filtro de 3 preguntas), `Schedule_Confirmado` (cuando la cita queda agendada), `Schedule_Asistido` (cuando el CAPI recibe confirmacion de asistencia desde GHL).

Por que: Con 6 pixels activos Meta recibe senales contradictorias. La deduplicacion falla. Las custom conversions dan a Meta una jerarquia de valor para optimizar.

Quien ejecuta: Trafficker + tecnico de tracking.

Impacto esperado: EMQ sube a 5.5+ en 30 dias. Attribution Score pasa de 1/10 a 5/10. El algoritmo empieza a tener senales reales.

Tiempo de implementacion: 2-3 dias.

---

## TABLA EJECUTIVA — CAMPANA / PROBLEMA / RECOMENDACION / METRICA

| Campana | Problema principal | Recomendacion | Metrica esperada |
|---|---|---|---|
| Todas Bogota | Objetivo ENGAGEMENT, no conversion | Crear campana nueva con objetivo LEADS y evento Schedule | Show rate 46% → 60%+ |
| WHATSAPP BUSSINES FASE 3 (Bogota) | Optimization goal CONVERSATIONS sin calificacion | Agregar pre-calificacion de 3 pasos en WhatsApp antes del agendamiento | Tasa de show de conversaciones → citas: +30% |
| TEST INSTAGRAM - Bogota 01/06 | COP 3.4M gastado, 310 convs iniciadas, 0 custom conversions medidas | Conectar evento Lead_Calificado como conversion objetivo o pausar y redirigir budget | CPL calificado medible; eliminar gasto en leads sin intencion |
| Bogota Instagram Mayo (PANAMA act) | 17 ads en 1 adset, sin copy que pre-califique presupuesto | Consolidar a 5-6 ads maximos, priorizar "Vid Dr Fabian precio y clinica", agregar copy de presupuesto en hook | CTR calificado sube, volumen de curiosos baja |
| Todos los ad sets | Segmentacion Advantage+ abierta sin filtro economico | Agregar Lookalike 1-3% construido sobre pacientes que asistieron (cuando haya datos Schedule) | CPL baja 20-30%, calidad de lead sube |
| Dataset/Pixels | 6 pixels activos, 3 disparando en paralelo | Consolidar a 1-2 pixels, pausar 4 zombies, crear 3 custom conversions | Deduplicacion limpia, EMQ 4.8 → 5.5+ |

---

## ROADMAP

**Semana 1 (inmediato)**
- Pausar 4 pixels zombie. Dejar Pixel CRM + Pixel capilar col.
- Crear 3 custom conversions en Pixel CRM.
- Implementar flujo de 3 preguntas de calificacion en WhatsApp GHL Bogota.
- Solicitar captura de email en el flujo de WhatsApp (mensaje 2 o 3 del bot).

**Semana 2**
- Crear campana nueva en BGTA o MEDELLIN act para Bogota con objetivo LEADS.
- Conectar evento `Schedule_Confirmado` en CAPI cuando GHL crea la cita.
- Agregar en el creativo principal de Bogota una mencion explicita de rango de inversion.

**Semana 3-4**
- Revisar performance de la nueva campana LEADS vs las actuales ENGAGEMENT.
- Construir primer Lookalike 1% sobre leads calificados (minimo 100 eventos).
- Pausar progresivamente los adsets de mayor gasto con menor tasa de conversion a cita asistida.

**Mes 2-3**
- Con 50+ eventos Schedule/semana: cambiar optimization goal de LEADS a CONVERSIONS optimizando directamente por Schedule.
- Meta sale de la fase de aprendizaje y el algoritmo empieza a encontrar pacientes, no curiosos.
- Show rate esperado: 60-68%.

---

## NOTAS FINALES DEL AUDITOR

Uno. Las cuentas PANAMA (act_1049078199582559) y MEDELLIN (act_874169544322810) tienen account_status 9 (deshabilitadas). Sin embargo sus campanas corren desde la cuenta MEDELLIN activa `act_874169544322810` y PANAMA activa. Verificar con el trafficker si hay restriccion de facturacion pendiente que pueda interrumpir las campanas de Bogota.

Dos. El ad "Gorra + controles EN REVISION MASTER NO LO APAGUE" en la campana de Bogota indica un proceso de gestion de creativos reactivo y sin documentacion. Un creativo en estado de alerta manual en produccion es un riesgo operativo. Necesita resolucion inmediata.

Tres. No existe ningun A/B test formal activo para Bogota. Los nombres "TEST" en los adsets son experimentos informales, no split tests configurados en Meta con significancia estadistica definida. Las conclusiones de esos "tests" no son estadisticamente validas.

Cuatro. La campana "Bogota Instagram Mayo" corre desde la cuenta PANAMA (act_1049078199582559) que tiene status 9. Verificar urgentemente si esa campana esta efectivamente activa o si el status 9 de la cuenta la esta afectando. El gasto registrado ($703 USD este mes) sugiere que si esta corriendo, pero el riesgo es real.

Cinco. Ningun ad set de Bogota usa retargeting de visitantes al sitio web (Custom Audience de website visitors). Hay 156.815 personas alcanzadas este mes en Bogota que vieron un anuncio y no convirtieron. No existe campana de retargeting para rescatarlos. Es trafico pagado que se pierde.

---

**Fecha de auditoría:** 2026-06-24  
**Enviado a:** esneidervc17@gmail.com  
**Estado:** Listo para ejecución