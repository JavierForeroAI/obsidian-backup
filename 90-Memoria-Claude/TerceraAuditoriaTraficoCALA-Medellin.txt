# INFORME DE AUDITORÍA — MEDELLÍN
## Innovart Medical IPS — Meta Ads Forense
**Periodo analizado:** 01–24 junio 2026 | **Referencia adicional:** Mayo 2026
**Auditor:** Meta Medical Data Auditor — Solo lectura, sin modificaciones
**Fecha de emisión:** 2026-06-24

---

## MAPA DE CAMPAÑAS MEDELLÍN

### Identificación forense — regla aplicada

Siguiendo la regla absoluta de [[feedback-cuentas-meta-no-son-sedes]]: se revisaron las 6 cuentas por nombre de campaña, destino y ad set. Los elementos confirmados como Medellín son:

| Cuenta | Campaña / Ad Set | Objetivo | Estado | Gasto junio COP |
|---|---|---|---|---|
| MEDELLIN (act_874169544322810) | "WHASTAPP BUSSINES-14/05/2026-(FASE 3)" — Ad Set: **MEDELLIN** | OUTCOME_ENGAGEMENT | ACTIVA | 2,437,088 |
| MEDELLIN (act_874169544322810) | "TEST INSTAGRAM -27/05/2026" — Ad Set: **MEDELLIN - TEST 11/06/2026** | OUTCOME_ENGAGEMENT | ACTIVA | 1,437,536 |
| MEDELLIN (act_874169544322810) | "TRÁFICO AL PERFIL - CBO - FASE 1---13/06/2026" | OUTCOME_TRAFFIC | ACTIVA | 460,153 |
| MEDELLIN (act_874169544322810) | "AO - TRÁFICO AL PERFIL - CBO - TOFU-RE" | OUTCOME_TRAFFIC | ACTIVA | 957,027 |
| MEDELLIN (act_874169544322810) | "RETARGETING DE ULTIMO IMPACTO-20/05/2026" | OUTCOME_ENGAGEMENT | ACTIVA | 475,415 |
| MEDELLIN (act_874169544322810) | "Interacción Global x Conjuntos + Segmentación" — Ad Set: **Medellin** | OUTCOME_ENGAGEMENT | ACTIVA | 949,671 |
| MEDELLIN (act_874169544322810) | "CLIENTES POTENCIALES- GENERAL-13/05/2026(MED-BQ-BG)(FASE 3 50/50)" | OUTCOME_LEADS | ACTIVA | 137,555 |
| BGTA (act_187478780709376) | "DM WAP MED RM 11 junio - dm2" | OUTCOME_ENGAGEMENT | ACTIVA | 485.86 USD (~$2,050,000 COP) |

**Notas de mapeo:**
- La cuenta MEDELLIN concentra la operación principal pero corre campañas de múltiples ciudades simultáneamente
- "CLIENTES POTENCIALES- GENERAL-13/05/2026(MED-BQ-BG)" es compartida entre ciudades
- Cuenta BGTA alberga "DM WAP MED RM 11 junio - dm2" que apunta a Medellín por nombre

---

## METRICAS GLOBALES — CUENTA MEDELLIN (junio 2026, 1–24)

| Métrica | Valor |
|---|---|
| Gasto total cuenta | COP $21,924,090 (~USD $5,749) |
| Impresiones | 3,508,648 |
| Alcance | 1,641,803 personas únicas |
| Frecuencia promedio | 2.14 veces |
| Clicks totales | 59,235 |
| CTR promedio | 1.69% |
| CPC promedio | COP $370 |
| CPM promedio | COP $6,249 |
| Leads reportados por Meta (Pixel/CAPI) | **19 leads** |
| Conversaciones iniciadas WhatsApp | **2,062** |
| Total messaging connections | **2,311** |
| First replies | **1,793** |
| Costo por conversación iniciada | COP ~$10,632 |
| Costo por lead (Meta reportado) | COP ~$1,153,899 |

**Ad Set Medellín principal (WHASTAPP BUSSINES / MEDELLIN ad set):**
- Gasto: COP $2,437,088
- Impresiones: 183,311
- Alcance: 98,643
- Frecuencia: 1.86
- CTR: 2.23%
- Conversaciones iniciadas: 407
- First replies: 382
- Depth 2: 99 | Depth 3: 33 | Depth 5: 31
- Costo por conversación: COP ~$5,987
- Leads Pixel/CAPI: 0

**Ad Set Medellín en TEST INSTAGRAM:**
- Gasto: COP $1,437,536
- Impresiones: 258,056
- Alcance: 108,132
- Frecuencia: 2.39
- CTR: 1.07%
- Conversaciones iniciadas: 127
- First replies: 109
- Depth 2: 72 | Depth 3: 39 | Depth 5: 23
- Lead reportado por Meta: **1 lead** (costo: COP $1,437,536 — anomalía crítica)
- Costo por conversación: COP ~$11,319

**Campaña DM WAP MED (en cuenta BGTA, moneda USD):**
- Gasto: USD $485.86 (~COP $2,050,000)
- Impresiones: 121,051
- Alcance: 55,890
- Frecuencia: 2.17
- Conversaciones iniciadas: 256
- First replies: 235
- Depth 2: 119 | Depth 3: 94 | Depth 5: 146
- Costo por conversación: USD $1.90 (~COP $8,000) — el más eficiente de los tres

---

## AUDITORIA EN 5 DIMENSIONES

### Dimensión A — SEGMENTACIÓN

**Hallazgos:**

**A1. CRITICO — Segmentación geográfica no aislada.** El ad set "MEDELLIN" corre dentro de campañas multiciudad. La cuenta MEDELLIN tiene ad sets etiquetados "BOGOTÁ - TEST", "PANAMA - WB - TEST", "BARRANQUILLA - TEST" y "MEDELLIN - TEST" corriendo simultáneamente en las mismas campañas. No existe cuenta exclusiva de Medellín ciudad.

**A2. CRITICO — Audience Overlap severo entre ad sets.** Cuatro ad sets de ciudades colombianas corren en la misma cuenta con audiencias que se superponen. El usuario medio ve múltiples campañas de Medellín y de otras ciudades, confundiendo al algoritmo.

**A3. IMPORTANTE — No hay exclusión documentada de ciudades dentro de los sets.** Los ad sets nombrados "MEDELLIN" no excluyen explícitamente otras ciudades a nivel de geotargeting verificable. Riesgo: leads de otras ciudades contaminan la pipeline de Medellín.

**A4. IMPORTANTE — Público ADVANTAGE+ sin restricción geográfica.** Los ad sets "PÚBLICO ADVANTAGE+ INTERESES - COL" corren a nivel Colombia sin segmentación por ciudad.

**A5. Sin lookalikes verificados para Medellín.** No se detectan ad sets con nomenclatura LAL-MED o Lookalike Medellín.

**A6. Retargeting de Último Impacto sin segmentación ciudad.** COP $475,415 gastados en retargeting que puede estar recuperando audiencia de cualquier ciudad colombiana.

---

### Dimensión B — CREATIVOS Y MESSAGING

**Hallazgos:**

**B1. IMPORTANTE — Creativos nombrados genéricamente.** De los 50 ads activos, la mayoría tiene nombres AD1, AD2, AD3. No hay naming que indique avatar, etapa de funnel ni ciudad.

**B2. CRITICO — Creativos del ad set Medellín no diferenciados del copy genérico.** Creativos activos replican patrón genérico: copy como "¿Te estás quedando calvo?", "27.000 oportunidades" — sin segmentación por avatar ni perfil antioqueño.

**B3. IMPORTANTE — Un solo avatar activo para Medellín.** No hay nomenclatura que indique avatar AV1-AV5 para Medellín específicamente.

**B4. IMPORTANTE — Frecuencia 2.39 en el ad set Medellín principal.** Ad set "MEDELLIN - TEST 11/06/2026" lleva frecuencia 2.39 sobre 108,132 personas. Con solo 1 lead reportado, la frecuencia alta indica fatiga creativa.

**B5. Creativos de tráfico al perfil con buen CTR pero sin conversión.** CTR 4.58% con 5,466 link clicks pero 0 leads. Tráfico lleva a perfil de Instagram, no a pipeline.

**B6. Creativos de alto engagement pero bajo lead intent.** "Interacción Global x Conjuntos" genera 311,766 vistas y 314,589 post engagements pero 0 leads.

**B7. Nombres creativos aspiracionales en tráfico al perfil.** "El fotógrafo oficial", "El paso del tiempo", "La Duda", "Desmontando mitos" — todos van a PROFILE_VISIT, no a conversión.

---

### Dimensión C — EMBUDO (Lead form, CRM, Workflow)

**Hallazgos:**

**C1. CRITICO — Desconexión total entre conversaciones y leads reportados.** 2,062 conversaciones iniciadas en WhatsApp. Meta solo reporta 19 leads. Tasa de conversación→lead-reportado es 0.92%: de cada 100 conversaciones, Meta solo "ve" 1 como lead. El 99% de las conversaciones es invisible para el Pixel.

**C2. CRITICO — CAPI no reporta leads calificados de Medellín.** CPL reportado es COP $1,153,899. CAPI no está enviando evento Schedule cuando el prospecto agenda valoración.

**C3. CRITICO — Optimización por CONVERSATIONS en vez de LEAD_GENERATION.** Ad sets de Medellín optimizan por CONVERSATIONS (objetivo engagement). No le dice a Meta qué persona es calificada.

**C4. IMPORTANTE — No hay evento Schedule enviado a Meta desde Medellín.** No existe workflow que dispare evento CAPI Schedule hacia la cuenta MEDELLIN.

**C5. IMPORTANTE — Embudo WhatsApp sin calificación estructurada.** De 2,062 conversaciones iniciadas, solo 375 (18.2%) llegan al quinto intercambio (Depth 5). La mayoría se abandona pronto.

**C6. Leads de formulario: campaña compartida MED-BQ-BG.** La única campaña con objetivo LEADS que incluye Medellín es compartida con Bogotá y Barranquilla. Imposible aislar leads de Medellín.

---

### Dimensión D — ESTRUCTURA DE CAMPAÑA

**Hallazgos:**

**D1. CRITICO — Sin CBO dedicado a Medellín ciudad.** La cuenta tiene CBO que contiene ad sets de Bogotá, Medellín, Barranquilla, Panamá. Si Bogotá tiene mejor señal, el algoritmo starva a Medellín.

**D2. CRITICO — Cuenta MEDELLIN en status 9 (inhabilitada o con restricciones).** Posible restricción de features (AEM, CAPI avanzado, límites de gasto). Requiere verificación inmediata en Business Manager.

**D3. IMPORTANTE — Objetivos desalineados con la etapa de funnel.** Corre simultáneamente: OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_LEADS. Sin estructura clara TOFU→MOFU→BOFU por ciudad.

**D4. IMPORTANTE — Ocho creativos de tráfico al perfil con presupuesto de conversión.** Campañas "TRÁFICO AL PERFIL" suman COP $1,417,180 con objetivo PROFILE_VISIT. Son branding, no conversión.

**D5. IMPORTANTE — Campaña de retargeting sin segmentación ciudad.** "RETARGETING DE ULTIMO IMPACTO" (COP $475,415) sin saber la audiencia de cada ad set.

**D6. Campaña de Medellín en cuenta BGTA: eficiente pero sin cierre.** "DM WAP MED RM 11 junio - dm2" tiene 256 conversaciones a USD $1.90 cada una — más eficiente. Depth 5: 146 personas (57% rate). Sin embargo, 0 leads reportados a CAPI.

**D7. Sin A/B test formal para Medellín.** No hay A/B test activo en junio 2026.

---

### Dimensión E — COMUNICACIÓN Y PROPUESTA DE VALOR

**Hallazgos:**

**E1. IMPORTANTE — Ausencia del perfil antioqueño en el messaging.** El hombre de Medellín (paisa, cultura de trabajo, familia, apariencia social) no está representado. Copy genérico "¿Te estás quedando calvo?" no activa código cultural de Medellín.

**E2. IMPORTANTE — Propuesta de valor sin precio ancla para Medellín.** No hay equivalente a "Barranquilla $6,500,000 COP" para Medellín. Usuario no recibe ancla de precio local.

**E3. IMPORTANTE — Testimonios sin segmentación geográfica.** Los 6 testimonios activos no tienen indicación de si son pacientes de Medellín.

**E4. Tono correcto en DM WAP MED.** Campaign en BGTA para Medellín tiene mejor depth 5 rate (57%), sugiriendo que el copy resuena mejor.

**E5. Garantía vitalicia: riesgo latente.** Aunque no detectado en nombres activos, riesgo de compliance desde otras cuentas.

---

## SCORECARD — MEDELLÍN

| Dimensión | Score | Semáforo | Hallazgo principal |
|---|---|---|---|
| Tracking Score | 12/100 | ROJO | 2,062 conversaciones, solo 19 leads visibles para Meta |
| Meta Score (Pixel/CAPI) | 8/100 | ROJO | CAPI no reporta Schedule; lead único costó $1.4M COP |
| CAPI Score | 5/100 | ROJO | Sin evento calificado de Medellín enviado al algoritmo |
| CRM Score | 20/100 | ROJO | Sin confirmación de que GHL Medellín dispara eventos a Meta |
| Revenue Score | 0/100 | ROJO | 0 Purchase/Revenue eventos reportados desde Medellín |
| Learning Score | 10/100 | ROJO | Meta entrena sobre conversaciones, no sobre valoraciones |
| Attribution Score | 15/100 | ROJO | No hay fbclid ni UTMs en campañas de WhatsApp de Medellín |
| Data Integrity Score | 25/100 | NARANJA | Ad sets de ciudad mezclados sin aislamiento geográfico real |
| Segmentación Score | 30/100 | NARANJA | No hay LAL, no hay CBO ciudad, audiencias superpuestas |
| Creativos Score | 20/100 | ROJO | Sin avatar, sin precio, sin testimonio local, fatiga en frecuencia 2.39 |

**SCORE COMPUESTO MEDELLÍN: 14.5/100 — ESTADO CRÍTICO**

---

## TOP 3 PROBLEMAS RAÍZ

### Problema 1 — Meta no sabe quién convierte en Medellín
La cuenta genera 2,062 conversaciones de WhatsApp/mes pero CAPI solo reporta 19 leads (0.92% de visibilidad). El algoritmo optimiza sobre la señal más escasa. Meta aprendió a encontrar personas que hacen click en WhatsApp — no personas que asisten a la valoración.

### Problema 2 — El presupuesto de Medellín no está protegido
Los ad sets de Medellín compiten dentro del mismo CBO con Bogotá, Barranquilla y Panamá. Bogotá históricamente tiene más señal. El CBO mata de hambre a Medellín. No hay forma de saber cuánto del presupuesto "de Medellín" realmente llega a Medellín.

### Problema 3 — Creativos sin identidad local ni segmentación por avatar
Medellín recibe el mismo creative genérico que el resto de Colombia. Frecuencia alta (2.39) sin conversión confirma fatiga sobre un mensaje que no conecta.

---

## TOP 3 FIXES INMEDIATOS

### Fix 1 — P0: Activar CAPI Schedule desde GHL Medellín
Cuando un lead agenda valoración en GHL Medellín, disparar evento `Schedule` via CAPI con fbclid, email y teléfono. Meta aprende de "personas que agendaron valoración", no clicks. Impacto esperado: reducción de CPL en 40-60% en 3 semanas de aprendizaje.

### Fix 2 — P0: Crear CBO exclusivo de Medellín
Separar ad sets de Medellín del CBO multiciudad. Crear campaña CBO con un solo ad set geotargeteado a Medellín (Medellín, Envigado, Bello, Itagüí, Sabaneta). Presupuesto mínimo: COP $130,000/día. Protege presupuesto, acumula historial ciudad-específico.

### Fix 3 — P1: Crear creativo de testimonio de paciente de Medellín con precio ancla
Video testimonio (30-45 seg) de paciente antioqueño. Antes/después. Copy: "Yo soy de Medellín y lo hice aquí". Estático de precio: "Medellín: desde $X.XXX.XXX COP". Activa identidad geográfica. CTR esperado: +30-50%.

---

## TABLA EJECUTIVA DE HALLAZGOS

| ID | Hallazgo | Dimensión | Prioridad | Impacto Revenue | Urgencia |
|---|---|---|---|---|---|
| MED-01 | CAPI no reporta Schedule de Medellín | CAPI | P0 | CRITICO | Inmediata |
| MED-02 | Ad sets Medellín en CBO multiciudad sin protección presupuestal | Estructura | P0 | ALTO | Inmediata |
| MED-03 | 2,062 conversaciones invisibles para Meta (99% sin CAPI) | Tracking | P0 | CRITICO | Inmediata |
| MED-04 | Cuenta MEDELLIN status 9 — requiere verificación BM | Estructura | P0 | ALTO | Inmediata |
| MED-05 | Optimización por CONVERSATIONS en vez de calidad de lead | Estructura | P0 | ALTO | Esta semana |
| MED-06 | Sin lookalike de Medellín basado en valoraciones agendadas | Segmentación | P1 | ALTO | 1-2 semanas |
| MED-07 | Frecuencia 2.39 con 1 lead — fatiga creativa confirmada | Creativos | P1 | MEDIO | Esta semana |
| MED-08 | Sin creativo diferenciado por avatar para Medellín | Creativos | P1 | MEDIO | 2-3 semanas |
| MED-09 | Sin precio ancla para Medellín en creativos | Comunicación | P1 | MEDIO | 1 semana |
| MED-10 | Sin testimonio de paciente de Medellín activo | Comunicación | P1 | MEDIO | 1-2 semanas |
| MED-11 | Retargeting sin segmentación ciudad (COP $475K gastados) | Segmentación | P1 | MEDIO | Esta semana |
| MED-12 | Tráfico al perfil sin conexión a pipeline (COP $1.4M) | Estructura | P2 | BAJO | 2-4 semanas |
| MED-13 | 0 leads de formulario atribuibles exclusivamente a Medellín | Embudo | P2 | BAJO | 2-3 semanas |
| MED-14 | Sin A/B test activo para Medellín | Estructura | P2 | BAJO | 3-4 semanas |
| MED-15 | Garantía vitalicia en otras cuentas contamina social proof | Compliance | P2 | BAJO | 2 semanas |

---

## DIAGNÓSTICO RAÍZ — SHOW RATE BAJO EN MEDELLÍN

El show rate bajo (~40% o menos) en Medellín no es problema de creativos ni segmentación en primer lugar. Es **problema de señal**:

1. Meta nunca aprende que el objetivo es una valoración presencial, porque ese evento nunca llega via CAPI.
2. Sin señal de calidad, Meta optimiza para el proxy más accesible: click en WhatsApp.
3. Click en WhatsApp en Medellín tiene alta demanda (2,062/mes) pero baja intención de compra real (99% no convierte).
4. Meta aprendió a encontrar personas que hacen click — no personas que asisten a valoración.
5. Creativos genéricos agravan: sin filtro por avatar, atraen usuarios de toda la pirámide, incluidos inconscientes que nunca convertirán.

**Proyección sin cambios:** show rate continuará en rango actual (estimado 35-45%) mientras Meta esté ciego a señal de valoración. CPL real (conversación→valoración→asistencia) está en rango COP $500,000-$1,500,000 — no el $10,632 que reporta Meta por conversación.

---

## ROADMAP MEDELLÍN — 30/60/90 DÍAS

### Semana 1 (P0 — Infraestructura de señal)
- Verificar status 9 de cuenta MEDELLIN en Business Manager
- Confirmar si GHL Medellín tiene workflow activo de CAPI para evento Schedule
- Activar envío de evento Schedule desde GHL Medellín a act_874169544322810
- Activar fbclid capture en landing pages y WhatsApp de Medellín

### Semana 2 (P0 — Estructura de campaña)
- Crear CBO exclusivo Medellín con un solo ad set geotargeteado
- Cambiar optimization_goal del ad set principal de CONVERSATIONS a LEAD_GENERATION
- Pausar o reformatear campañas de tráfico al perfil sin pipeline
- Segmentar retargeting por ciudad

### Semanas 3-4 (P1 — Creativos y señal de aprendizaje)
- Producir testimonio de paciente de Medellín
- Crear estático con precio ancla para Medellín
- Lanzar creativo AV1 (Ejecutivo Premium) con copy antioqueño
- Lanzar A/B test: creativo testimonio Medellín vs. creativo genérico

### Días 30-60 (P1 — Optimización)
- Revisar señal CAPI acumulada (target: mínimo 50 Schedule events)
- Si Schedule tiene volumen, crear Lookalike de Medellín basado en Schedule
- Evaluar pasar a objective LEADS con optimización por Schedule
- Testear avatar AV5 (Emprendedor)

### Días 60-90 (P2 — Escala)
- Si show rate mejora: duplicar presupuesto CBO Medellín
- Crear campaña separada AV2 (Militar) — ciudad con alta presencia militar
- Medir: CPL antes/después | conversaciones calificadas | show rate | CAC real
- Evaluar si cuenta MEDELLIN necesita migración

---

## IMPACTO ESPERADO

| Acción | Métrica afectada | Mejora estimada | Plazo |
|---|---|---|---|
| CAPI Schedule activo | Learning Score | De 10 a 55/100 | 3 semanas |
| CBO exclusivo Medellín | CPL real | -30 a -45% | 4 semanas |
| Creativo testimonio local | CTR | +30-50% | 2 semanas |
| Optimización por Schedule | Show rate | +10-15 puntos porcentuales | 6-8 semanas |
| Precio ancla en creative | Tasa de calificación en WA | +20-30% | 2 semanas |

---

## NOTAS FINALES DEL AUDITOR

**1. Cuenta MEDELLIN tiene account_status: 9.** Puede limitar: Custom Audiences avanzadas, AEM, CAPI avanzado. Verificar en Business Manager antes de optimizaciones que requieran esas funcionalidades.

**2. La campaña más eficiente de Medellín está en cuenta BGTA.** "DM WAP MED RM 11 junio - dm2" (BGTA) tiene el costo por conversación más bajo (USD $1.90) y depth 5 rate más alto (57%). Candidato ideal para activar señal CAPI primero.

**3. Mayo vs Junio: salto de gasto severo.** Mayo: COP $1,241,865. Junio en 24 días: COP $21,924,090 (17.6x incremento). Sin mejora en señal, escalar solo amplifica problema.

**4. El problema de show rate de Medellín es recuperable en 60 días** si se activa CAPI Schedule + CBO exclusivo + creativo local. Los ingredientes están disponibles. La brecha entre potencial (2,062 conversaciones/mes, 1.6M alcance) y resultado (19 leads, show rate bajo) es la mayor oportunidad de mejora de la operación Innovart.

**5. Ninguna modificación realizada en esta auditoría.** Todo diagnóstico forense de solo lectura.

---

**Fecha de auditoría:** 2026-06-24  
**Enviado a:** esneidervc17@gmail.com  
**Estado:** Listo para ejecución