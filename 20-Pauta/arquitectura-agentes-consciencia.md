---
title: Arquitectura de Agentes de AI por Nivel de Consciencia
description: Framework técnico completo para sistema de prospección conversacional con agentes especializados por nivel de consciencia del lead — diseñado para negocios de alto ticket en salud/estética
metadata:
  type: architecture
  status: draft
  created: 2026-06-12
  version: v1.0
  categoria: CRM / Automatización / AI Agents
  aplicacion: GoHighLevel + WhatsApp/Instagram/Facebook
  ticket_objetivo: $5,000–$15,000 USD
tags:
  - agentes-ai
  - ghl
  - whatsapp
  - automatizacion
  - consciencia-del-lead
  - alto-ticket
  - salud-estetica
related:
  - "[[avatares-clientes]]"
  - "[[crm-funnel]]"
  - "[[whatsapp-nurture-clinica]]"
---

# Arquitectura de Agentes de AI por Nivel de Consciencia del Lead

> Framework técnico replicable para negocios de alto ticket en salud/estética. Diseñado para GoHighLevel con canales WhatsApp, Instagram DM y Facebook Messenger.

---

## DIAGRAMA GENERAL DEL SISTEMA

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        ENTRADA DE LEADS (Todos los canales)                     │
│              WhatsApp / Instagram DM / Facebook Messenger / Landing             │
└─────────────────────────────────────┬───────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    AGENTE 0 — CLASIFICADOR (Intake Agent)                       │
│           3 preguntas → determina Nivel de Consciencia + Arquetipo              │
│           Tags: [nivel:X] [avatar:Y] [temperatura:Z]                           │
└──────┬────────────┬─────────────┬────────────┬────────────┬──────────┬──────────┘
       │            │             │            │            │          │
       ▼            ▼             ▼            ▼            ▼          ▼
  [nivel:0]    [nivel:1]     [nivel:2]    [nivel:3]   [nivel:4]  [nivel:5]
       │            │             │            │            │          │
       ▼            ▼             ▼            ▼            ▼          ▼
┌───────────┐ ┌───────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐
│ AGENTE 1  │ │ AGENTE 2  │ │ AGENTE 3 │ │ AGENTE 4 │ │AGENTE 5 │ │AGENTE 5  │
│ SEMBRADOR │ │ EDUCADOR  │ │EXPLORADOR│ │COMPARADOR│ │DECISOR  │ │PREPARADOR│
│           │ │           │ │          │ │          │ │         │ │          │
│Siembra    │ │Educa sobre│ │Cualifica │ │Diferencia│ │Empuja al│ │Confirma  │
│problema   │ │soluciones │ │y acerca  │ │vs compet.│ │cierre   │ │y prepara │
└─────┬─────┘ └─────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬────┘ └────┬─────┘
      │             │            │             │            │           │
      │             │            │             │            │           │
      ▼             ▼            ▼             ▼            ▼           ▼
      └─────────────┴────────────┴─────────────┴────────────┘           │
                              PROGRESIÓN NATURAL                        │
                                      │                                  │
                                      ▼                                  ▼
                              ┌───────────────┐               ┌─────────────────┐
                              │   AGENTE 5    │               │  NO-SHOW /      │
                              │  PREPARADOR   │──[no show]──► │  AGENTE 6       │
                              │  [agendó]     │               │  RECUPERADOR    │
                              └───────┬───────┘               └────────┬────────┘
                                      │[fue a valoración]              │
                                      ▼                                 │
                              ┌───────────────┐               [recuperó cita]
                              │   AGENTE 7    │                        │
                              │   CERRADOR    │◄───────────────────────┘
                              │ [post-consult]│
                              └───────┬───────┘
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                  [cerró venta]             [necesita humano]
                  Pipeline:                 ASESOR COMERCIAL
                  Operaciones               (escalada urgente)
```

---

## SISTEMA DE CUALIFICACIÓN INICIAL (AGENTE 0)

### Nombre: Agente Clasificador — "La Bienvenida Inteligente"

Este agente no vende. No educa. Solo clasifica con precisión quirúrgica en menos de 3 minutos.

### Las 3 Preguntas de Clasificación

Estas preguntas parecen conversacionales pero extraen las 2 dimensiones críticas: **temperatura** (urgencia) y **arquetipo** (perfil psicológico).

**Pregunta 1 — Temperatura y estado de consciencia:**
> "¡Hola! Gracias por escribirnos. Para poder orientarte mejor: ¿estás buscando información general sobre el procedimiento, o ya tienes en mente hacerlo pronto?"

| Respuesta | Señal | Nivel asignado |
|---|---|---|
| "Solo quiero info" / "curiosidad" | Temperatura baja | Nivel 1–2 |
| "Estoy pensándolo" / "investigando" | Temperatura media | Nivel 2–3 |
| "Ya sé lo que quiero" / "quiero agendar" | Temperatura alta | Nivel 3–4 |
| "Tenía cita / cancelé / no pude ir" | No-show o post-consulta | Nivel 6–7 |

**Pregunta 2 — Tiempo y urgencia real:**
> "¿Hace cuánto tiempo estás pensando en esto?"

| Respuesta | Señal | Acción |
|---|---|---|
| "Hace meses / años" | Procrastinador — frustración acumulada | Activa ángulo pérdida de tiempo |
| "Recién empecé a investigar" | Exploratorio — educación necesaria | Activa ángulo educación |
| "Pronto, quiero hacer algo este mes" | Urgencia real | Activa agente decisor directo |
| "Tengo un evento importante" | Urgencia de fecha | Prioridad máxima + humano |

**Pregunta 3 — Perfil y arquetipo (indirecta):**
> "¿A qué te dedicas, si no es mucha indiscreción? Así podemos recomendarte la mejor opción para tu estilo de vida."

| Respuesta | Arquetipo asignado | Tag |
|---|---|---|
| Ejecutivo, gerente, profesional, abogado, médico | Profesional Premium | `[avatar:profesional]` |
| Militar, policía, piloto, oficial | Militar | `[avatar:militar]` |
| Político, funcionario, contratista | Gubernamental | `[avatar:gubernamental]` |
| Emprendedor, negocio propio, independiente | Emprendedor | `[avatar:emprendedor]` |
| Estilista, diseñador, influencer, lifestyle | Estético Social | `[avatar:estetico]` |
| No responde / evasivo | Genérico | `[avatar:generico]` |

### Lógica del Agente 0

```
Mensaje 1: Bienvenida + Pregunta 1
   ↓ (responde en < 2h)
Mensaje 2: Afirmación empática + Pregunta 2
   ↓ (responde en < 2h)
Mensaje 3: Afirmación + Pregunta 3
   ↓
CLASIFICACIÓN AUTOMÁTICA:
   → Aplica tags [nivel:X] [avatar:Y] [temperatura:Z]
   → Mueve a pipeline correcto
   → Activa workflow del agente correspondiente
   
Si NO responde en 24h:
   → Tag: [temperatura:fria]
   → Nivel 1 por defecto
   → Activa Agente 1 con secuencia de reactivación larga
```

### Tags de Salida del Agente 0

```
Temperatura:
  [temperatura:caliente]   → responde rápido, urgencia expresada
  [temperatura:tibia]      → responde pero sin urgencia clara
  [temperatura:fria]       → no respondió el agente 0 completo

Nivel asignado:
  [nivel:0] [nivel:1] [nivel:2] [nivel:3] [nivel:4] [nivel:5] [nivel:6] [nivel:7]

Avatar:
  [avatar:profesional] [avatar:militar] [avatar:gubernamental]
  [avatar:emprendedor] [avatar:estetico] [avatar:generico]

Canal de entrada:
  [canal:whatsapp] [canal:instagram] [canal:facebook] [canal:landing]

Fuente de tráfico (si se puede detectar):
  [fuente:organico] [fuente:pauta] [fuente:referido] [fuente:remarketing]
```

---

## AGENTE 1 — EL SEMBRADOR

**Nivel objetivo:** Nivel 0 — INCONSCIENTE
**Nombre operacional:** Sembrador de Dolor

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Hacer consciente el problema que el lead ya tiene pero no reconoce activamente |
| **Personalidad** | Cálido, cercano, sin presión de venta. Como un amigo que "casualmente" menciona algo |
| **Tono** | Conversacional, curioso, empático. NUNCA vendedor |
| **Velocidad** | Lento — este nivel requiere tiempo y repetición |

### Métricas de Éxito

- Tasa de apertura de mensajes: objetivo >65%
- Tasa de respuesta al menos 1 mensaje: objetivo >25%
- Tasa de avance a Nivel 1: objetivo >15%
- Tiempo promedio en nivel: 14–21 días

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag aplicado `[nivel:0]` por Agente 0 | Activación principal |
| Lead entra por contenido orgánico (reels, posts) | Venía mirando contenido pero no declaró intención |
| Remarketing de audiencia fría (>90 días sin contacto) | Reactivación de base dormida |
| Referido que "no sabe bien por qué le mandaron" | Llega sin contexto propio |

### Señales de Comportamiento que Indican Nivel 0

- Escribe solo "hola" o "info" sin elaborar
- No ha visto el precio ni lo pregunta
- No menciona alopecia directamente — habla de "el cabello" en general
- Responde preguntas del Agente 0 con respuestas muy cortas
- Tiempo de respuesta >6 horas en el Agente 0

### Lógica de Conversación

**Secuencia de mensajes (máximo 6, en 21 días):**

```
Día 1 — Mensaje de Valor (no de venta):
"[Nombre], ¿sabías que más del 50% de los hombres nota cambios en su cabello 
antes de los 40 años? Lo interesante es que la mayoría no lo relaciona con 
nada hasta que ya está muy avanzado. ¿Has notado algo en tu caso?"

   SÍ responde → Escuchar, validar, hacer Pregunta 2
   NO responde en 48h → continuar secuencia

Día 4 — Mensaje de Contenido Social (testimonio suave):
[Enviar imagen/video de antes-después con historia de vida, sin precio]
"Este es [nombre ficticio], 38 años, ingeniero. Nos escribió exactamente 
como tú, sin saber muy bien por qué. Solo quería información. 
¿Qué fue lo que más te llamó la atención cuando llegaste aquí?"

   SÍ responde → Clasificar respuesta, avanzar si hay señal
   NO responde → continuar

Día 8 — Mensaje de Dolor Suave (adaptado al avatar detectado):
Profesional: "La imagen que proyectamos en el trabajo comunica más 
de lo que creemos. ¿Cómo sientes que afecta tu presencia profesional?"
Emprendedor: "Dicen que la imagen vende antes que las palabras. 
¿Cómo crees que te perciben en tu entorno de negocios?"
[continuar para cada avatar]

   SÍ responde con reflexión → Señal de avance → mover a Nivel 1
   NO responde → continuar

Día 12 — Mensaje de Urgencia Suave (tiempo):
"Una cosa que muchos de nuestros pacientes nos dicen después es que 
desearían haber actuado antes. El tratamiento funciona mejor 
cuanto antes se hace. ¿Hay algo que te haya detenido hasta ahora?"

Día 17 — Último Contenido de Valor:
[Video educativo corto: qué es la alopecia androgenética, sin pitch]

Día 21 — Cierre de Ciclo:
"[Nombre], entiendo que quizás no es el momento. Voy a dejarte tranquilo.
Si en algún momento quieres conversar sobre opciones, aquí estaremos. 
¿Hay algo en lo que pueda ayudarte antes de que me despida?"

   SÍ responde → Reiniciar ciclo o escalar según respuesta
   NO responde → Tag [estado:latente] → salir del flujo activo → 
                  nurture pasivo (1 mensaje/mes con contenido)
```

### Árbol de Decisión Principal

```
Lead entra en Agente 1
        │
        ▼
¿Responde al mensaje 1?
    SÍ ──► ¿Menciona dolor o problema? ──SÍ──► Escalar a Nivel 1 ahora
    │              │
    │              NO──► Seguir secuencia normal día 4
    │
    NO ──► Esperar 48h ──► Mensaje día 4
                │
          ¿Responde? ──SÍ──► Retomar desde esa respuesta
                │
                NO ──► Continuar secuencia hasta día 21
                              │
                        ¿Responde en algún punto?
                              │
                     SÍ ──► Clasificar y enrutar
                     NO ──► [estado:latente] → nurture mensual
```

### Triggers de Escalada

| Señal | Acción |
|---|---|
| Menciona "quiero" + procedimiento | Escalar a Nivel 3 directamente |
| Hace pregunta sobre precios | Escalar a Nivel 2 |
| Responde con reflexión emocional profunda | Escalar a Nivel 1 |
| Menciona "ya lo había pensado" | Escalar a Nivel 2 |
| Dice "no me interesa" / "no es para mí" | Tag `[estado:perdido]` → archivar |
| Menciona fecha/evento específico | Escalar a humano urgente |

### Handoff al Siguiente Agente

```yaml
campos_a_pasar:
  - nombre_lead
  - avatar_detectado
  - canal_entrada
  - dolor_mencionado: "texto exacto de la respuesta más relevante"
  - tiempo_en_nivel: días
  - mensajes_enviados: número
  - ultimo_mensaje_respondido: fecha
tags_a_aplicar:
  - "[nivel:1]"
  - "[desde:sembrador]"
  - "[dolor:confirmado]"  # si mencionó dolor específico
nota_para_siguiente_agente: "Lead tardó X días en responder. Mencionó [dolor]. Avatar probable: [Y]"
```

---

## AGENTE 2 — EL EDUCADOR

**Nivel objetivo:** Nivel 1 — PROBLEMA CONSCIENTE
**Nombre operacional:** Educador Empático

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Validar el dolor y presentar que existen soluciones médicas reales |
| **Personalidad** | Experto accesible. Como un médico amigo que explica sin jerga |
| **Tono** | Cálido + autoridad médica. Confianza, no presión |
| **Velocidad** | Media — el lead está procesando nueva información |

### Métricas de Éxito

- Tasa de respuesta: objetivo >40%
- Tasa de avance a Nivel 2: objetivo >30%
- Tiempo promedio en nivel: 7–14 días
- Mensajes promedio hasta conversión: 3–4

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag `[nivel:1]` aplicado | Escalada del Agente 1 |
| Lead responde con emoción/reflexión | Menciona cómo le afecta en su vida |
| Lead hace pregunta genérica sobre soluciones | "¿Qué opciones hay?" |
| Lead entra directamente por ad de problema | Ad tipo "¿Lo has notado?" |

### Señales de Comportamiento que Indican Nivel 1

- Siente el dolor pero cree que "es normal" o "no tiene solución"
- Ha "resignado" la situación
- Puede mencionar que familiares lo tienen también ("es genético")
- Busca validación más que solución
- Pregunta "¿eso funciona realmente?"

### Lógica de Conversación

**Secuencia de mensajes (máximo 5, en 14 días):**

```
Día 1 — Validación del Dolor (personalizada por avatar):
Profesional: "Lo que describes es más común de lo que parece en hombres 
que trabajan bajo presión constante. El estrés, la genética y la edad 
se combinan. Y lo mejor: hoy tiene solución médica probada. 
¿Cuánto tiempo llevas notando esto?"

Día 3 — Educación sin Venta (contenido + pregunta):
[Enviar infografía o video corto: "¿Por qué ocurre la alopecia 
androgenética?" — explicación médica simple]
"Este es el proceso exacto que sucede. Lo que muchos no saben 
es que hay una ventana de tiempo en la que el tratamiento 
es más efectivo. ¿Sabes en qué fase estás tú?"

Día 6 — Prueba Social Educativa (testimonio + transformación):
[Video testimonio: "Yo también pensé que no tenía solución"]
"[Nombre del paciente] pensó lo mismo que tú. 
Hoy lleva 18 meses con el resultado. 
¿Qué es lo que más te frena para explorar esto?"

Día 10 — La Pregunta Clave (cualificación):
"Para orientarte bien: ¿has consultado alguna vez con algún médico 
sobre esto, o todavía no?"
   SÍ consultó → preguntar qué le dijeron → Nivel 3
   NO consultó → continuar educando

Día 14 — Cierre de Ciclo Educativo:
"[Nombre], lo que te he compartido es solo el comienzo. 
Si quisieras saber exactamente qué solución aplicaría a tu caso específico, 
una valoración virtual es gratis y tarda 20 minutos. 
¿Te interesa explorar esa opción esta semana?"
   SÍ → Escalar a Nivel 3/4
   NO → Nurture de largo plazo (1 pieza de contenido educativo por semana)
```

### Sistema de Detección de Intención (Agente 2)

**SEÑALES DE AVANCE:**
```
Frases que indican listo para Nivel 3:
- "¿cuánto cuesta?"
- "¿tienen sede en [ciudad]?"
- "¿qué procedimiento hacen exactamente?"
- "¿cuánto tiempo tarda la recuperación?"
- "un amigo lo hizo"
- "ya lo había pensado antes"
- "¿en qué consiste el proceso?"
- cualquier pregunta específica sobre el procedimiento
```

**SEÑALES DE OBJECIÓN:**
```
"muy caro" / "no tengo presupuesto" →
  Respuesta: "Entiendo perfectamente. ¿Cuál sería un rango que sí te 
  funcionaría explorar? Tenemos opciones de financiamiento."

"¿y si no funciona?" / "¿tiene garantía?" →
  Respuesta: "Excelente pregunta. Precisamente por eso hacemos primero 
  una valoración — para decirte con honestidad si eres buen candidato 
  o no. No todos lo son, y eso es algo que respetamos."

"tengo miedo" / "me da pena" / "¿duele?" →
  Respuesta: "El miedo es válido y normal. ¿Qué es exactamente lo que 
  más te preocupa? Hay cosas que aclarar y otras que son reales — 
  quiero ser honesto contigo."

"no sé si es para mí" →
  Respuesta: "Por eso existe la valoración gratuita — para que tú decidas 
  con información real, no con suposiciones. Sin compromiso."
```

**SEÑALES DE PÉRDIDA:**
```
"no me interesa más"
"ya lo decidí, no voy a hacerlo"
"es muy invasivo para mí"
"mi esposa no quiere"
→ Acción: no insistir. Tag [estado:objecion-bloqueo]. 
   Esperar 30 días → reactivar con 1 mensaje de caso clínico similar.
```

**SEÑALES DE ESCALADA URGENTE (→ humano ya):**
```
"tengo un evento en [fecha específica próxima]"
"me lo operé antes y salió mal"
"tengo una condición médica, ¿puedo hacerlo?"
"¿cuándo es la primera cita disponible?"
"quiero agendar hoy"
→ Acción: notificar asesor en <15 minutos. Tag [escala:urgente]
```

### Triggers de Escalada

| Señal | Destino |
|---|---|
| Pregunta precio o procedimiento | Agente 3 (Explorador) |
| Compara con otra clínica | Agente 4 (Comparador) directamente |
| Dice "quiero agendar" | Agente 5 (Decisor) + notificar humano |
| Objeción médica o caso especial | Escalar a humano inmediato |

### Handoff al Siguiente Agente

```yaml
campos_a_pasar:
  - objeciones_mencionadas: lista de objeciones expresadas
  - contenido_consumido: qué piezas se le enviaron
  - nivel_conocimiento_actual: "básico / intermedio / avanzado"
  - preguntas_realizadas: preguntas específicas que hizo
  - señal_de_avance: frase exacta que disparó la escalada
tags_a_aplicar:
  - "[nivel:2]" o "[nivel:3]" según señal
  - "[desde:educador]"
  - "[objecion:precio]" / "[objecion:miedo]" / etc. si aplica
```

---

## AGENTE 3 — EL EXPLORADOR

**Nivel objetivo:** Nivel 2 — SOLUCIÓN CONSCIENTE
**Nombre operacional:** Explorador de Opciones

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Posicionar la clínica como la mejor opción entre todas las que el lead está evaluando |
| **Personalidad** | Consultor imparcial, seguro, transparente. No es vendedor — es guía |
| **Tono** | Confiado, directo, educativo + algo de autoridad técnica |
| **Velocidad** | Media-rápida — el lead está activo en su proceso de búsqueda |

### Métricas de Éxito

- Tasa de respuesta: objetivo >50%
- Tasa de avance a Nivel 3: objetivo >40%
- Tasa de solicitud de valoración: objetivo >25%
- Tiempo promedio en nivel: 5–10 días

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag `[nivel:2]` | Escalada de agentes anteriores |
| Lead pregunta precio o procedimiento específico | Señal de investigación activa |
| Lead llega por ad de retargeting (vio la página) | Ya conoce la clínica |
| Lead menciona que está "comparando opciones" | Nivel 2 explícito |

### Señales de Comportamiento que Indican Nivel 2

- Hace preguntas técnicas: "¿qué técnica usan?", "¿injertos o láser?"
- Pregunta sobre tiempos de recuperación
- Menciona que ha buscado información en internet
- Compara explícitamente: "vi que otras clínicas hacen X"
- Pregunta sobre médicos o credenciales

### Lógica de Conversación

**Secuencia de mensajes (máximo 4, en 10 días):**

```
Mensaje 1 — Reconocer que está investigando + diferenciador clave:
"Veo que ya tienes bastante información. Perfecto — eso significa 
que podremos tener una conversación más directa. Una pregunta: 
¿Qué es lo más importante para ti al momento de elegir dónde hacerlo? 
¿El precio, el resultado, la seguridad médica, o algo más?"

   Responde precio → activar argumento ROI + opciones de financiamiento
   Responde resultado → activar portafolio de resultados reales
   Responde seguridad → activar credenciales médicas + protocolos
   Responde todos → hacer la pregunta más específica

Mensaje 2 — El Diferenciador Principal (basado en respuesta):
[Si precio]: "Te entiendo. El precio importa. Pero déjame compartirte 
algo que cambia el análisis: el costo de un procedimiento mal hecho 
para corregirlo es 3 veces mayor. ¿Has visto casos de correcciones?"
[Video: casos de corrección de malos procedimientos — sin nombrar clínicas]

[Si resultado]: "El resultado depende de 3 cosas: el médico, 
la técnica y la candidatura del paciente. No todos los candidatos 
son iguales. Por eso lo primero que hacemos es una valoración honesta 
— a veces le decimos a alguien que no es buen candidato todavía."

[Si seguridad]: "Nuestro equipo está certificado en [credencial]. 
El procedimiento se realiza en [tipo de instalación]. 
¿Quieres que te comparta la ficha técnica del equipo médico?"

Mensaje 3 — Invitación a Valoración (sin presión):
"La forma más inteligente de decidir es con información real de tu caso.
Una valoración virtual de 20 minutos con nuestro médico es completamente 
gratis. No te compromete a nada. Solo te da datos reales sobre 
tu candidatura y las opciones que tienes. ¿Tiene sentido para ti?"

   SÍ → Pasar a Agente 5 (Decisor) para agendar
   Más dudas → Mensaje 4

Mensaje 4 — Manejo de última objeción + cierre suave:
"[Respuesta personalizada a la última objeción expresada]
¿Qué necesitarías saber para sentirte listo para esa valoración?"
```

### Triggers de Escalada

| Señal | Destino |
|---|---|
| "¿cuándo puedo ir?" / "¿cómo agendo?" | Agente 5 directo |
| "ya fui a [otra clínica] y me dijeron X" | Agente 4 (Comparador) |
| Objeción de precio recurrente | Activar módulo financiamiento |
| Pregunta médica específica/compleja | Escalar a humano |
| "quiero hablar con alguien" | Escalar a humano ya |

### Handoff al Siguiente Agente

```yaml
campos_a_pasar:
  - criterio_decision_principal: precio / resultado / seguridad / confianza
  - objeciones_resueltas: lista
  - objeciones_pendientes: lista
  - competidores_mencionados: si los hay
  - nivel_de_urgencia_percibido: bajo / medio / alto
tags_a_aplicar:
  - "[nivel:3]"
  - "[desde:explorador]"
  - "[criterio:precio]" / "[criterio:resultado]" / "[criterio:seguridad]"
  - "[comparando:activo]" si mencionó otras clínicas
```

---

## AGENTE 4 — EL COMPARADOR

**Nivel objetivo:** Nivel 3 — PRODUCTO CONSCIENTE
**Nombre operacional:** Diferenciador de Valor

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Ganar la comparación sin atacar a la competencia — diferenciarse por valor, no por precio |
| **Personalidad** | Seguro, transparente, maduro. No agresivo. No defensivo |
| **Tono** | Directo, consultivo, con datos y prueba social |
| **Velocidad** | Rápida — este lead está a punto de decidir |

### Métricas de Éxito

- Tasa de respuesta: objetivo >60%
- Tasa de solicitud de valoración: objetivo >45%
- Tasa de cierre post-valoración: objetivo >35%
- Tiempo promedio en nivel: 3–7 días

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag `[comparando:activo]` | Llegó mencionando otra clínica |
| Tag `[nivel:3]` | Escalada directa |
| Lead pregunta "¿por qué ustedes y no X?" | Explícito |
| Lead pide descuento o match de precio | Comparando en precio |
| Lead dice "en otro lado me ofrecieron X" | Comparación activa |

### Señales de Comportamiento que Indican Nivel 3

- Tiene el presupuesto aproximado en mente
- Ha consultado con al menos 1 otra clínica
- Compara características específicas (técnica, injertos, garantía)
- Pide descuento o pregunta si hay promociones
- Habla de "decidir esta semana" o "necesito pensarlo"

### Lógica de Conversación

**Secuencia de mensajes (máximo 3, en 7 días):**

```
Mensaje 1 — Reconocer la comparación + preguntar el criterio real:
"Me parece muy inteligente que estés comparando. Es una decisión 
importante y merece análisis. Una pregunta directa: 
¿qué fue lo que más te gustó de la otra opción, y qué te hace 
seguir buscando?"

   [La respuesta revela exactamente el gap que debemos llenar]

Mensaje 2 — Respuesta al gap específico + prueba social directa:
[Si precio fue mejor allá]: 
"Entiendo. La diferencia de precio existe y no voy a ignorarla. 
Lo que te puedo decir es esto: [diferenciador técnico específico]. 
¿Puedo mostrarte 3 casos de pacientes que compararon exactamente 
como tú y por qué eligieron quedarse aquí?"
[Enviar: portafolio de resultados + testimonio de video corto]

[Si técnica diferente]:
"Interesante. La técnica que mencionas tiene sus ventajas. 
La que usamos nosotros tiene estas diferencias para tu tipo de caso: 
[explicación técnica simple]. ¿Quieres que el médico te explique 
directamente cuál es mejor para TU caso específico?"

[Si dudas de resultados]:
"Esa duda es completamente válida. Por eso propongo algo concreto: 
te conecto con uno de nuestros pacientes que pasó por la misma 
duda. ¿Te parece?"
[Testimonio en video o llamada breve con paciente embajador]

Mensaje 3 — Cierre de la comparación:
"[Nombre], en este punto creo que la mejor forma de cerrar 
esta comparación no es con más información — es con una valoración 
real donde el médico vea tu caso y te dé una recomendación honesta. 
Eso es lo que va a darte certeza, no más mensajes de mi parte. 
¿Lo hacemos esta semana?"
```

### Módulo Anti-Competencia (reglas estrictas)

```
PROHIBIDO:
- Mencionar el nombre de clínicas competidoras
- Decir que la competencia es mala o hace malos procedimientos
- Prometer precios menores sin autorización del equipo comercial

PERMITIDO:
- Hablar de los diferenciales propios con evidencia
- Mostrar portafolio de resultados reales
- Conectar con pacientes embajadores (con permiso)
- Explicar diferencias técnicas de forma neutral y educativa
- Ofrecer una valoración gratuita como desempate
```

### Triggers de Escalada

| Señal | Destino |
|---|---|
| "¿cuándo puedo ir?" / "quiero agendar" | Agente 5 (Decisor) |
| Pide hablar con alguien del equipo | Humano inmediato |
| Objeción de precio que necesita aprobación | Asesor comercial |
| Menciona caso médico complejo | Médico director |

### Handoff al Siguiente Agente

```yaml
campos_a_pasar:
  - competidor_mencionado: nombre o referencia (sin datos de la clínica)
  - gap_detectado: precio / técnica / resultado / confianza
  - argumento_que_funcionó: qué mensaje generó la señal de avance
  - presupuesto_aproximado: si lo mencionó
tags_a_aplicar:
  - "[nivel:4]"
  - "[desde:comparador]"
  - "[gap:precio]" / "[gap:confianza]" / "[gap:tecnica]"
  - "[alto:valor]" si claramente tiene capacidad de pago
```

---

## AGENTE 5 — EL DECISOR

**Nivel objetivo:** Nivel 4 — MÁS CONSCIENTE
**Nombre operacional:** Cerrador de Compromiso

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Lograr que el lead agende la valoración (cita con médico) |
| **Personalidad** | Directo, seguro, eficiente. Respeta el tiempo del lead |
| **Tono** | Decisivo pero no presionador. Facilitador, no vendedor |
| **Velocidad** | Rápida — este lead está listo. No se le puede dar tiempo de enfriar |

### Métricas de Éxito

- Tasa de conversión a cita agendada: objetivo >60%
- Tiempo promedio en nivel: 1–3 días
- Tasa de show rate de las citas generadas: objetivo >65%
- Mensajes promedio hasta agendar: 2–3

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag `[nivel:4]` | Escalada de agentes previos |
| Lead dice "quiero agendar" en cualquier agente | Prioridad máxima |
| Lead pregunta disponibilidad de fechas | Señal directa de nivel 4 |
| Lead ha pasado >7 días en nivel 3 sin avanzar | Activar empujón final |

### Señales de Comportamiento que Indican Nivel 4

- Pregunta disponibilidad de fechas o sedes
- Pregunta tiempos de recuperación específicos ("necesito estar bien para X fecha")
- Ha completado toda la investigación y solo le falta "dar el paso"
- Responde rápido y con mensajes más cortos (decisión mental ya tomada)
- Dice "solo quiero confirmar una cosa más"

### Lógica de Conversación

**Secuencia de mensajes (máximo 3, en 3 días):**

```
Mensaje 1 — Facilitar la decisión (no vender, facilitar):
"[Nombre], con toda la información que tienes, creo que el siguiente 
paso natural es la valoración con el médico. Es gratis, dura 20 minutos, 
y te va a dar un diagnóstico real de tu caso. ¿Prefieres hacerla 
esta semana o la próxima?"
[Nota: dar 2 opciones, nunca pregunta abierta de calendario]

   Responde con fecha → confirmar y pasar a Agente 5B (Preparador)
   Duda → Mensaje 2

Mensaje 2 — El empujón final:
"Entiendo que quieres estar seguro. Mira, te voy a ser directo: 
la valoración no te compromete a nada. Si el médico dice que 
no eres buen candidato, te lo va a decir honestamente. 
Eso es lo que hace diferente esta primera consulta. 
¿Qué te impide hacerla esta semana?"

   Responde con objeción → responder y cerrar en mismo mensaje
   Dice "nada, esta semana" → confirmar y pasar a Preparador

Mensaje 3 — Urgencia real (solo si hay razón legítima):
[Si hay cupo limitado real]: "Hay disponibilidad el [día] a las [hora]. 
¿Reservo ese espacio para ti?"
[Si no hay urgencia legítima]: No inventar escasez. 
Simplemente: "¿Qué necesitas para tomar esa decisión hoy?"
```

### Módulo de Agendamiento

```
Una vez confirmada la cita:
1. Enviar confirmación con:
   - Fecha y hora exacta
   - Dirección/link si es virtual
   - Nombre del médico
   - Qué llevar / qué preparar

2. Aplicar tags:
   [estado:agendado]
   [cita:valoracion]
   [fecha-cita:YYYY-MM-DD]

3. Mover oportunidad a etapa "Agenda Valoración" en pipeline

4. Activar Agente 5B (Preparador) inmediatamente
```

### Triggers de Escalada

| Señal | Destino |
|---|---|
| Confirma cita | Agente 5B (Preparador) |
| Solicita hablar por teléfono | Asesor comercial en <15 min |
| Pregunta sobre financiamiento | Módulo financiamiento + humano |
| 3 días sin respuesta | Tag `[nivel:6-riesgo]` → activar recuperación anticipada |

---

## AGENTE 5B — EL PREPARADOR

**Nivel objetivo:** Nivel 5 — COMPROMETIDO (Agendó cita)
**Nombre operacional:** Acompañante Pre-Procedimiento

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Garantizar que el lead llegue a la cita — reducir no-shows y aumentar la certeza de compra |
| **Personalidad** | Cálido, cercano, cuidadoso. Como un asistente personal |
| **Tono** | Atento, empático, tranquilizador |
| **Velocidad** | Según los días antes de la cita |

### Métricas de Éxito

- Tasa de show rate: objetivo >70% (desde <40% actual)
- Tasa de confirmación de asistencia: objetivo >85%
- Índice de satisfacción post-valoración: medido por respuesta al mensaje post-cita

### Lógica de Conversación (Secuencia Pre-Cita)

```
D-3 (3 días antes de la cita):
"[Nombre], nos vemos el [día] a las [hora]. Solo quería recordarte 
que no necesitas venir en ayuno ni prepararte de ninguna forma especial. 
Lo único que te pido es que vengas con tiempo y con las ganas de 
conocer tu diagnóstico real. ¿Hay algo que quieras preguntar antes?"

D-1 (día anterior):
"Mañana es tu valoración. Ya está todo listo de nuestro lado. 
[Dirección / link de videollamada]. ¿Confirmas que todo está bien 
de tu lado?"
   Confirma → excelente, enviar recordatorio en D-day
   No responde → llamada de confirmación por humano (asesor)
   Cancela → activar protocolo de reagendamiento inmediato

D-day (mañana de la cita — 2 horas antes):
"Buenos días [Nombre]. Hoy es tu valoración a las [hora]. 
Te esperamos en [sede/link]. Cualquier imprevisto, escríbeme 
de inmediato y te ayudo."

D-day (si no llegó — 1 hora después de la hora de cita):
→ Activar Agente 6 (Recuperador) automáticamente
→ Tag: [estado:no-show]
→ Notificar a recepción/asesor

Post-cita (mismo día, 2 horas después):
"[Nombre], ¿cómo estuvo tu valoración? ¿Quedaste con alguna duda 
o pregunta que no hiciste en la consulta?"
→ Si responde → escuchar, consolidar, pasar a Agente 7 (Cerrador)
→ Si no responde en 24h → Agente 7 activa su secuencia
```

---

## AGENTE 6 — EL RECUPERADOR

**Nivel objetivo:** Nivel 6 — NO-SHOW
**Nombre operacional:** Recuperador de Cita Perdida

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Recuperar el lead que no llegó a su cita sin hacerlo sentir juzgado |
| **Personalidad** | Empático, sin juicio, facilitador. NO presionador |
| **Tono** | Comprensivo, cálido, con sentido de urgencia suave |
| **Velocidad** | Rápida — actuar en las primeras 4 horas post no-show |

### Métricas de Éxito

- Tasa de recuperación (reagendó): objetivo >45%
- Tiempo promedio hasta reagendamiento: <48 horas
- Tasa de show en segunda cita: objetivo >80%

### Lógica de Conversación

**Secuencia (máximo 4 mensajes en 7 días):**

```
H+1 (1 hora después del no-show):
"[Nombre], vi que no pudiste llegar hoy. Sé que las cosas pasan. 
¿Estás bien? ¿Hubo algún imprevisto?"
[Esperar respuesta — no hacer más preguntas todavía]

H+4 si no responde:
"Quedamos con el espacio reservado para ti. No hay problema — 
podemos reagendar para esta semana o la próxima, 
lo que mejor te quede. ¿Cuándo tendrías 20 minutos?"

D+2 si sigue sin responder:
"[Nombre], entiendo si algo cambió. Solo quiero que sepas 
que el espacio sigue disponible para cuando estés listo. 
¿Hay algo que pueda ayudarte a resolver antes de volver a agendar?"

D+7 último intento:
"[Nombre], voy a dejar el contacto abierto por si en algún momento 
quieres retomar. Solo dime 'sí' y te organizo la nueva cita 
en 5 minutos. Sin compromisos."
   
No responde en 7 días → Tag [estado:latente] → Nurture mensual ligero
```

### Protocolo para Reagendamiento

```
Al confirmar reagendamiento:
1. Agradecer sin hacer sentir culpa
2. Confirmar nueva fecha con entusiasmo tranquilo
3. Activar Agente 5B nuevamente para la nueva cita
4. Añadir nota en el CRM: "No-show [fecha]. Reagendó [fecha]."
5. Tag: [estado:reagendado] [no-show:registrado]

Para segunda cita: activar confirmación con 1 día de anticipación 
+ llamada humana de confirmación obligatoria (no solo bot)
```

---

## AGENTE 7 — EL CERRADOR

**Nivel objetivo:** Nivel 7 — POST-CONSULTA (Fue pero no cerró)
**Nombre operacional:** Cerrador de Objeciones

### Perfil del Agente

| Dimensión | Definición |
|---|---|
| **Objetivo único** | Resolver las objeciones post-valoración y cerrar la venta |
| **Personalidad** | Consultor experimentado. Seguro, paciente, con autoridad |
| **Tono** | Directo, empático, concreto. NO desesperado, NO agresivo |
| **Velocidad** | Media — respetar el proceso de decisión pero sin dejar enfriar |

### Métricas de Éxito

- Tasa de cierre post-consulta: objetivo >40%
- Tiempo promedio hasta cierre: 3–10 días
- Tasa de objeciones resueltas: objetivo >55%
- Valor promedio de venta generada desde este agente

### Triggers de Entrada

| Trigger | Descripción |
|---|---|
| Tag `[nivel:7]` | Automático después de valoración sin cierre |
| Asesor marca "valoración realizada" en pipeline | Manual |
| Lead pide "tiempo para pensarlo" en la valoración | Post-consulta con objeción activa |

### Mapa de Objeciones Post-Consulta

Este agente opera con un árbol de objeciones específicas detectadas en la valoración:

```
OBJECIÓN 1: PRECIO / "Está muy caro"
Respuesta primaria:
"[Nombre], entiendo. ¿Te compartió el médico las opciones de financiamiento?
Tenemos acceso a crédito médico donde pagas en cuotas mensuales cómodas.
¿Quieres que te calcule cuánto sería la cuota mensual para tu caso?"
   
   SÍ → Enviar simulador de cuotas → cerrar en esa conversación
   NO / Sigue en duda → Respuesta secundaria:
   "Mira, entiendo que es una inversión importante. 
   ¿Qué te ayudaría a sentir que es una decisión financiera inteligente?"

OBJECIÓN 2: "Necesito consultarlo con mi pareja"
Respuesta primaria:
"Completamente válido — es una decisión que involucra a la familia. 
¿Hay alguna forma en que yo pueda ayudarte a preparar esa conversación?
Tenemos material que explica el procedimiento de forma simple para parejas."
   
   → Enviar: "Guía para hablar con tu pareja sobre el procedimiento"
   → Ofrecer: Valoración virtual para la pareja también

OBJECIÓN 3: "Tengo miedo a la cirugía" / "Necesito más tiempo"
Respuesta primaria:
"El miedo es completamente válido. ¿Qué es lo que más te preocupa, 
el procedimiento en sí, la recuperación, o el resultado?"
   → Respuesta específica según lo que mencione
   → Testimonio de paciente con el mismo miedo específico

OBJECIÓN 4: "Quiero esperar un poco más"
Respuesta primaria:
"Puedo esperarte. Solo quiero que sepas una cosa: hay una razón médica 
por la que los mejores resultados se logran antes de cierta etapa 
de la alopecia. ¿Puedo pedirle al médico que te explique 
tu ventana de tiempo óptima?"

OBJECIÓN 5: "Vi mejor precio en otro lado"
→ Activar Módulo Anti-Competencia del Agente 4
→ Ofrecer revisar la propuesta con el asesor

OBJECIÓN 6: "Lo pospongo para después del año/después de vacaciones"
Respuesta:
"Entiendo. ¿Cuál sería ese momento específico? 
Porque si ya tienes una fecha en mente, podemos reservar tu espacio 
ahora sin costo — para cuando estés listo."
→ Oferta: reserva sin pago inicial (si la política lo permite)
```

### Secuencia de Mensajes Post-Valoración

```
D+1 (día después de la valoración sin cierre):
"[Nombre], ¿cómo estás procesando todo lo que viste ayer?
¿Surgió alguna duda después de que te fuiste que quieras resolver?"

D+3 (si no hay decisión):
"[Nombre], sé que estás evaluando. ¿Hay algo puntual que esté 
frenando la decisión? Sin presión — solo quiero ayudarte a tener 
la claridad que necesitas."

D+5 (activar objeción más probable según perfil):
[Mensaje personalizado por objeción detectada o por avatar]

D+8 (cierre empático + urgencia real si existe):
"[Nombre], quiero ser honesto contigo. Tu candidatura es buena 
y el médico quiere trabajar contigo. La pregunta es el momento. 
¿Qué necesitaría pasar para que tomes la decisión esta semana?"

D+12 (si sigue abierto — último mensaje antes de cadencia larga):
"Voy a dejarte espacio. Cuando estés listo, escríbeme y en 24 horas 
tenemos todo organizado. ¿Hay algo más en lo que pueda ayudarte?"

D+12 en adelante → Cadencia larga:
1 mensaje cada 2 semanas durante 3 meses con contenido de valor:
- Testimonios de pacientes
- Artículos educativos
- Ofertas temporales si existen
```

### Triggers de Escalada

| Señal | Destino |
|---|---|
| "Quiero agendar / listo para hacerlo" | Asesor comercial inmediato + pipeline "Operaciones" |
| Objeción de precio que requiere aprobación especial | Asesor comercial |
| Pregunta médica compleja post-valoración | Médico tratante |
| "Definitivamente no" después de D+12 | Tag `[estado:perdido-final]` |

---

## ARQUITECTURA TÉCNICA EN GoHighLevel

### Sistema de Tags — Naming Convention

Todos los tags siguen el formato `[categoría:valor]` para facilitar filtrado y automatización.

```
=== NIVEL DE CONSCIENCIA ===
[nivel:0]               — Inconsciente
[nivel:1]               — Problema consciente
[nivel:2]               — Solución consciente
[nivel:3]               — Producto consciente
[nivel:4]               — Más consciente
[nivel:5]               — Comprometido / Agendado
[nivel:6]               — No-show
[nivel:7]               — Post-consulta sin cierre

=== AVATAR / ARQUETIPO ===
[avatar:profesional]    — Ejecutivo, profesional
[avatar:militar]        — Fuerzas militares/seguridad
[avatar:gubernamental]  — Funcionario público
[avatar:emprendedor]    — Empresario, freelance
[avatar:estetico]       — Perfil estético/social
[avatar:generico]       — Sin clasificar

=== TEMPERATURA ===
[temperatura:caliente]  — Alta urgencia, responde rápido
[temperatura:tibia]     — Interesado pero sin urgencia
[temperatura:fria]      — Baja respuesta, largo plazo

=== ESTADO DEL LEAD ===
[estado:activo]         — En flujo activo
[estado:latente]        — Sin respuesta, nurture pasivo
[estado:agendado]       — Cita confirmada
[estado:reagendado]     — Reagendó después de no-show
[estado:no-show]        — No asistió a cita
[estado:valuado]        — Asistió a valoración
[estado:cerrado]        — Venta cerrada (moved to Operaciones)
[estado:perdido]        — No va a comprar (primera señal)
[estado:perdido-final]  — Definitivamente no comprará

=== CANAL Y FUENTE ===
[canal:whatsapp]
[canal:instagram]
[canal:facebook]
[canal:landing]
[fuente:organico]
[fuente:pauta]
[fuente:referido]
[fuente:remarketing]

=== AGENTE QUE PROCESÓ ===
[desde:clasificador]
[desde:sembrador]
[desde:educador]
[desde:explorador]
[desde:comparador]
[desde:decisor]
[desde:preparador]
[desde:recuperador]
[desde:cerrador]

=== OBJECIONES DETECTADAS ===
[objecion:precio]
[objecion:miedo]
[objecion:pareja]
[objecion:tiempo]
[objecion:competencia]
[objecion:medica]

=== CRITERIO DE DECISIÓN ===
[criterio:precio]
[criterio:resultado]
[criterio:seguridad]
[criterio:confianza]
[criterio:conveniencia]

=== ESCALADA ===
[escala:urgente]        — Necesita humano en <15 minutos
[escala:asesor]         — Requiere asesor comercial
[escala:medico]         — Requiere médico
[escala:financiamiento] — Requiere módulo de crédito

=== CITAS ===
[cita:valoracion]
[cita:virtual]
[cita:presencial]
[fecha-cita:YYYY-MM-DD] — Fecha específica de la cita

=== COMPARACIÓN ===
[comparando:activo]     — Está evaluando otras clínicas
[gap:precio]
[gap:confianza]
[gap:tecnica]

=== NURTURE LARGO PLAZO ===
[nurture:mensual]
[nurture:quincenal]
[nurture:semanal]
```

---

### Custom Fields Necesarios en GHL

```
=== CAMPOS DE CLASIFICACIÓN ===
lead_nivel_actual           (Número: 0-7)
lead_nivel_historial        (Texto: "0→1→2→3" — trayectoria)
lead_avatar                 (Dropdown: profesional/militar/gubernamental/emprendedor/estetico/generico)
lead_temperatura            (Dropdown: caliente/tibia/fria)
lead_fuente_de_dolor        (Texto largo: frase exacta donde expresó su dolor)
lead_criterio_decision      (Dropdown: precio/resultado/seguridad/confianza)

=== CAMPOS DE CITA ===
cita_fecha_valoracion       (Fecha)
cita_tipo                   (Dropdown: virtual/presencial)
cita_estado                 (Dropdown: agendada/confirmada/asistio/no-show/cancelada)
cita_no_show_count          (Número: veces que no fue)

=== CAMPOS COMERCIALES ===
presupuesto_estimado        (Número o rango)
financiamiento_solicitado   (Sí/No)
objecion_principal          (Dropdown: precio/miedo/pareja/tiempo/competencia/medica)
competidor_mencionado       (Texto: sin nombrar la clínica, solo "otra clínica")
propuesta_enviada           (Sí/No)
propuesta_fecha             (Fecha)

=== CAMPOS DE COMUNICACIÓN ===
canal_preferido             (Dropdown: whatsapp/instagram/facebook)
ultimo_mensaje_enviado      (Fecha)
ultimo_mensaje_respondido   (Fecha)
dias_en_nivel_actual        (Número — calculado)
mensajes_totales_enviados   (Número)
agente_actual               (Texto: nombre del agente/workflow activo)

=== CAMPOS DE CONVERSACIÓN ===
respuesta_pregunta_1        (Texto: respuesta a "¿estás buscando info o quieres hacerlo pronto?")
respuesta_pregunta_2        (Texto: respuesta a "¿hace cuánto tiempo piensas en esto?")
respuesta_pregunta_3        (Texto: respuesta a "¿a qué te dedicas?")
nota_handoff                (Texto largo: nota del agente anterior)
```

---

### Estructura de Workflows por Agente

```
=== WORKFLOWS PRINCIPALES ===

WF-00: Intake Clasificador
  Trigger: Nuevo contacto entra por cualquier canal
  Acciones:
    1. Enviar Mensaje 1 (bienvenida + pregunta 1)
    2. Esperar respuesta (timeout 24h)
    3. Analizar respuesta → aplicar tag temperatura
    4. Enviar Mensaje 2 (pregunta 2)
    5. Esperar respuesta (timeout 24h)
    6. Enviar Mensaje 3 (pregunta 3)
    7. Esperar respuesta (timeout 24h)
    8. Aplicar tags de nivel + avatar
    9. Enrutar al workflow del agente correspondiente
  Timeout total: 72h → si no responde nada → WF-01 (Sembrador, nivel 0)

WF-01: Sembrador (Nivel 0→1)
  Trigger: Tag [nivel:0] aplicado
  Acciones: Secuencia 6 mensajes en 21 días
  Salidas:
    → Respuesta con señal de avance → Tag [nivel:1] → WF-02
    → Sin respuesta en 21 días → Tag [estado:latente] → WF-NURTURE

WF-02: Educador (Nivel 1→2)
  Trigger: Tag [nivel:1] aplicado
  Acciones: Secuencia 5 mensajes en 14 días
  Salidas:
    → Señal de avance → Tag [nivel:2] o [nivel:3] → WF-03 o WF-04
    → Señal de objeción → activar módulo de objeción correspondiente
    → Sin respuesta en 14 días → Tag [estado:latente] → WF-NURTURE

WF-03: Explorador (Nivel 2→3)
  Trigger: Tag [nivel:2] aplicado
  Acciones: Secuencia 4 mensajes en 10 días
  Salidas:
    → Menciona comparación → Tag [comparando:activo] → WF-04
    → Pide agendar → WF-05
    → Sin respuesta en 10 días → WF-NURTURE

WF-04: Comparador (Nivel 3→4)
  Trigger: Tag [nivel:3] o [comparando:activo]
  Acciones: Secuencia 3 mensajes en 7 días
  Salidas:
    → Señal de cierre → WF-05 (Decisor)
    → Solicita hablar con humano → Notificar asesor inmediato

WF-05: Decisor (Nivel 4→Agendado)
  Trigger: Tag [nivel:4]
  Acciones: Secuencia 3 mensajes en 3 días
  Salidas:
    → Confirma cita → aplicar [estado:agendado] + [cita:valoracion] → WF-05B
    → Sin confirmación en 3 días → Tag [nivel:6-riesgo] → notificar humano

WF-05B: Preparador (Nivel 5)
  Trigger: Tag [estado:agendado]
  Acciones:
    → D-3: recordatorio suave
    → D-1: confirmación
    → D-day -2h: mensaje final
    → D-day +1h: verificar asistencia
      SÍ asistió: Tag [estado:valuado] → WF-07
      NO asistió: Tag [estado:no-show] → WF-06

WF-06: Recuperador (Nivel 6)
  Trigger: Tag [estado:no-show]
  Acciones: Secuencia 4 mensajes en 7 días
  Salidas:
    → Reagenda → Tag [estado:reagendado] → WF-05B (reinicia)
    → Sin respuesta en 7 días → Tag [estado:latente] → WF-NURTURE

WF-07: Cerrador (Nivel 7)
  Trigger: Tag [estado:valuado]
  Acciones: Secuencia 6 mensajes en 12 días
  Salidas:
    → Cierra venta → Tag [estado:cerrado] → mover a pipeline "Operaciones"
    → Objeción → activar módulo de objeción + escalar si necesario
    → Sin cierre en 12 días → WF-NURTURE largo plazo

WF-NURTURE: Nurture Pasivo
  Trigger: Tag [estado:latente]
  Acciones:
    → 1 pieza de contenido de valor por mes
    → Análisis de respuesta mensual
    → Si responde con interés → clasificar nuevamente desde WF-00
    → Máximo 6 meses, luego [estado:perdido-final]

=== WORKFLOWS DE SOPORTE ===

WF-URGENTE: Escalada Urgente
  Trigger: Tag [escala:urgente]
  Acciones:
    1. Notificación push al asesor comercial
    2. Notificación por email
    3. Crear tarea "Contactar en 15 min"
    4. Si no hay respuesta del asesor en 15 min → notificar supervisor

WF-OBJECION-PRECIO: Módulo Financiamiento
  Trigger: Tag [objecion:precio]
  Acciones:
    1. Enviar información de opciones de financiamiento
    2. Enviar simulador de cuotas
    3. Notificar asesor para seguimiento personalizado

WF-CONFIRMACION-CITA: Protocolo No-Show Prevention
  Trigger: 48h antes de cualquier cita
  Acciones:
    1. Mensaje de confirmación automático
    2. Si no confirma en 24h → llamada humana obligatoria
    3. Si confirma → enviar preparación pre-cita
```

---

### Reglas de Asignación de Conversaciones

```
ASIGNACIÓN AUTOMÁTICA (bot):
  Condición: Lead está en Nivel 0, 1, 2, 3 y temperatura = tibia/fría
  Acción: Mantener en flujo de bot, sin asignar asesor

ASIGNACIÓN MIXTA (bot + monitoreo):
  Condición: Lead está en Nivel 3 con temperatura = caliente
  Condición: Lead agendó cita (Nivel 5)
  Acción: Asignar asesor para monitoreo + bot continúa el flujo
           El asesor puede intervenir manualmente en cualquier momento

ASIGNACIÓN HUMANA OBLIGATORIA (asesor toma el control):
  Condición: Tag [escala:urgente] aplicado
  Condición: Lead en Nivel 4 solicita llamada
  Condición: Lead llega a Nivel 7 (post-consulta) — el bot apoya pero el asesor lidera
  Condición: Objeción de precio que requiere aprobación especial
  Condición: Lead menciona condición médica preexistente
  Acción: Notificar asesor en <15 min. El bot envía: 
          "En un momento un asesor te contacta directamente."

PRIORIDAD DE RESPUESTA:
  🔴 Urgente (<15 min): [escala:urgente] + Nivel 4 caliente + post-cita
  🟡 Alta (<2 horas): Nivel 3 caliente + reagendamiento
  🟢 Normal (<4 horas): Niveles 1-2 en flujo activo
  ⚪ Nurture (diario): [estado:latente]
```

---

### Integración con Pipeline de Oportunidades

```
PIPELINE "VENTAS" — Etapas y Correspondencia con Niveles

Etapa CRM                  | Nivel del Lead | Agente Activo
---------------------------|----------------|------------------
Frío                       | Nivel 0-1      | Sembrador
Primer Contacto            | Nivel 1-2      | Educador
Tibio                      | Nivel 2-3      | Explorador/Comparador
Agenda Valoración          | Nivel 4-5      | Decisor/Preparador
Val Virtual                | Nivel 5        | Preparador
Asistió                    | Nivel 7        | Cerrador
No Asistió                 | Nivel 6        | Recuperador
Ganado                     | Cierre         | → Pipeline Operaciones
Perdido                    | Estado Final   | Archivado

REGLAS DE MOVIMIENTO:
- Mover etapa SIEMPRE que cambie el nivel del lead
- El workflow de cada agente es responsable de mover la etapa
- NUNCA cerrar una oportunidad como "Ganada" hasta que el paciente 
  firme o pague (integración con Pipeline Operaciones)

PIPELINE "OPERACIONES" — Creación de Oportunidad:
  Trigger: Tag [estado:cerrado] en Pipeline Ventas
  Acción: Crear nueva oportunidad en Pipeline Operaciones con:
    - Nombre del paciente
    - Procedimiento acordado
    - Valor de venta
    - Fecha estimada del procedimiento
    - Médico asignado
```

---

## SISTEMA DE DETECCIÓN DE INTENCIÓN — DICCIONARIO GLOBAL

Este diccionario aplica a TODOS los agentes. Los workflows deben monitorear estas palabras/frases en tiempo real.

### SEÑALES DE AVANCE UNIVERSAL (→ Escalar nivel)

```
SEÑALES DE ALTA INTENCIÓN:
"quiero agendar", "quiero hacerlo", "me interesa", "¿cuándo puedo ir?",
"¿tienen citas?", "¿cuánto cuesta?", "¿qué incluye?", "ya lo decidí",
"quiero hacerlo pronto", "para cuándo puedo tener cita",
"cuánto tarda la recuperación", "¿tienen financiamiento?",
"ya hablé con mi pareja", "ya revisé el precio", "quiero comenzar",
"¿cómo es el proceso?", "necesito hacerlo antes de [fecha]"

SEÑALES MEDIAS DE INTENCIÓN:
"suena bien", "me llama la atención", "lo estoy pensando",
"estoy comparando", "ya vi otras opciones", "vi su Instagram",
"un conocido lo hizo", "¿cómo quedó ese señor del video?",
"¿tienen sede en [ciudad]?", "¿se puede hacer sin que se note?"
```

### SEÑALES DE PÉRDIDA (→ Cambiar estrategia)

```
ABANDONO TEMPORAL (→ Nurture pasivo):
"por ahora no", "no es el momento", "estoy ocupado",
"luego te escribo", [no responde por 14+ días]

ABANDONO REAL (→ [estado:perdido]):
"no me interesa", "no voy a hacerlo", "ya decidí no hacerlo",
"es muy caro para mí", "mi esposa no quiere que lo haga",
"prefiero no hacerme nada", "voy a hacerlo en otro lado"

OBJECIÓN DE BLOQUEO (→ Protocolo especial):
"me operé antes y salió mal" → Empatía + médico que habla directamente
"tengo una enfermedad" → Escalar a médico inmediato
"soy alérgico a anestesia" → Escalar a médico inmediato
```

### SEÑALES DE ESCALADA URGENTE (→ Humano <15 min)

```
"quiero hablar con alguien ya", "¿me pueden llamar?",
"tengo un evento el [fecha próxima]", "necesito hacerlo urgente",
"tengo el presupuesto listo", "ya tengo el dinero",
"¿cuándo es la próxima cita disponible?",
"mi caso me lo operaron mal antes", [cualquier mención de emergencia médica],
"soy médico y quiero referir a un paciente", "quiero el precio exacto ahora"
```

---

## KPIs DEL SISTEMA COMPLETO

### KPIs por Agente

| Agente | KPI Principal | Objetivo | KPI Secundario | Objetivo |
|---|---|---|---|---|
| Agente 0 (Clasificador) | Tasa de clasificación completa | >80% | Tiempo promedio de clasificación | <48h |
| Agente 1 (Sembrador) | Tasa de avance a Nivel 1 | >15% | Tasa de respuesta al mensaje 1 | >30% |
| Agente 2 (Educador) | Tasa de avance a Nivel 2-3 | >30% | Tasa de solicitud de valoración | >20% |
| Agente 3 (Explorador) | Tasa de solicitud de valoración | >25% | Tiempo promedio en nivel | <10 días |
| Agente 4 (Comparador) | Tasa de victoria vs. competencia | >50% | Tasa de solicitud de cita | >45% |
| Agente 5 (Decisor) | Tasa de conversión a cita | >60% | Tiempo hasta agendar | <3 días |
| Agente 5B (Preparador) | Show rate | >70% | Tasa de confirmación D-1 | >85% |
| Agente 6 (Recuperador) | Tasa de recuperación no-show | >45% | Tiempo hasta reagendamiento | <48h |
| Agente 7 (Cerrador) | Tasa de cierre post-consulta | >40% | Tiempo promedio hasta cierre | <10 días |

### KPIs del Sistema Completo

```
FUNNEL COMPLETO (metas del sistema):
Lead entra → Completa clasificación         : >80%
Clasificado → Responde algún mensaje         : >45%
Responde → Solicita valoración               : >35%
Solicita → Agenda cita                       : >75%
Agenda → Asiste (Show Rate)                  : >70%  [desde <40% actual]
Asiste → Cierra venta                        : >40%
Cierra → Llega a pipeline Operaciones        : 100% (control crítico)

MÉTRICAS DE EFICIENCIA:
Tiempo promedio lead-to-cita                 : <14 días
Tiempo promedio lead-to-cierre               : <30 días
Mensajes promedio por cierre                 : <12
Costo por cita agendada                      : [calcular según CAC]
Costo por venta cerrada                      : [calcular según ROAS]

MÉTRICAS DE SALUD DEL SISTEMA:
% de leads en estado:latente vs activo       : monitorear semanalmente
% de escaladas urgentes resueltas en <15 min : objetivo >90%
Tiempo de respuesta promedio del bot         : <2 minutos
Tiempo de respuesta promedio de humano       : <2 horas (horario laboral)
```

### Dashboard de Control Semanal

```
REPORTE SEMANAL RECOMENDADO:

1. ENTRADAS:
   - Leads totales por canal
   - Leads clasificados vs. sin clasificar
   - Distribución por nivel asignado
   - Distribución por avatar

2. FLUJO:
   - Leads por nivel actualmente
   - Leads que avanzaron de nivel esta semana
   - Leads que cayeron a latente
   - Escaladas urgentes resueltas / no resueltas

3. CITAS:
   - Citas agendadas esta semana
   - Show rate de citas de esta semana
   - No-shows recuperados
   - Citas pendientes próxima semana

4. CIERRES:
   - Valoraciones realizadas
   - Cierres de venta
   - Tasa de conversión post-valoración
   - Objeciones más frecuentes en Nivel 7

5. ALERTAS:
   - Leads en [escala:urgente] sin atender
   - Leads en Nivel 7 hace >7 días sin movimiento
   - No-shows sin recuperación hace >48h
```

---

## GUÍA DE IMPLEMENTACIÓN EN GHL

### Orden Recomendado de Implementación

```
FASE 1 — Fundamentos (Semana 1-2):
  ✓ Crear todos los custom fields
  ✓ Crear sistema de tags (cargar lista completa)
  ✓ Construir WF-00 (Clasificador)
  ✓ Construir WF-URGENTE (Escalada)
  ✓ Configurar reglas de asignación básicas
  ✓ Prueba con 10 leads reales

FASE 2 — Agentes de Siembra y Educación (Semana 3-4):
  ✓ Construir WF-01 (Sembrador) — variantes por avatar x5
  ✓ Construir WF-02 (Educador) — variantes por avatar x5
  ✓ Configurar módulos de objeción básicos
  ✓ Prueba con leads nivel 0-1

FASE 3 — Agentes de Conversión (Semana 5-6):
  ✓ Construir WF-03 (Explorador)
  ✓ Construir WF-04 (Comparador)
  ✓ Construir WF-05 (Decisor)
  ✓ Integración con sistema de agendamiento
  ✓ Prueba con leads nivel 2-4

FASE 4 — Agentes de Cierre y Recuperación (Semana 7-8):
  ✓ Construir WF-05B (Preparador)
  ✓ Construir WF-06 (Recuperador)
  ✓ Construir WF-07 (Cerrador)
  ✓ Construir WF-NURTURE
  ✓ Construir WF-OBJECION-PRECIO
  ✓ Prueba del sistema completo end-to-end

FASE 5 — Optimización (Semana 9+):
  ✓ Activar dashboard de control semanal
  ✓ Revisión de KPIs cada 7 días
  ✓ A/B testing de mensajes clave
  ✓ Refinamiento de detección de intención
  ✓ Calibración de tiempos de espera por canal
```

### Notas Críticas de Implementación

```
1. PERSONALIZACIÓN POR AVATAR:
   Los workflows de Nivel 0, 1 y 2 deben tener ramas separadas 
   por avatar. El mensaje para el avatar:profesional es distinto 
   al de avatar:emprendedor. No usar mensajes genéricos en estos niveles.

2. VENTANAS HORARIAS:
   Configurar todos los mensajes para enviarse solo en horario:
   Lunes–Viernes: 8:00 AM – 8:00 PM (hora local del lead)
   Sábado: 9:00 AM – 2:00 PM
   Domingo: Solo confirmaciones de cita urgentes

3. CANAL PREFERIDO:
   El sistema debe responder siempre en el canal por donde llegó 
   el lead. No migrar de WhatsApp a email sin permiso explícito.

4. TONO POR CANAL:
   WhatsApp: Más conversacional, mensajes cortos, uso de emojis moderado
   Instagram DM: Más visual, referencias al contenido que vio
   Facebook: Más formal, puede ser más largo

5. LÍMITE DE MENSAJES POR DÍA:
   Máximo 2 mensajes en 24 horas por lead
   (excepto en D-day de cita: hasta 3)
   Violar este límite genera sensación de spam y baja la tasa de respuesta

6. REGISTRO DE CONVERSACIÓN EN CRM:
   Todo mensaje enviado y recibido debe quedar en el registro del contacto.
   Esto es crítico para el handoff entre agentes y para el análisis 
   posterior de objeciones.
```

---

*Documento técnico para implementación interna. Framework replicable para negocios de alto ticket en salud/estética. No contiene información de pacientes ni datos confidenciales.*
