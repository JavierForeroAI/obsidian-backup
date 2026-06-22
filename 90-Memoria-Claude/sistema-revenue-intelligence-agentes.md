---
name: sistema-revenue-intelligence-agentes
description: Ecosistema de 4 agentes especializados en Revenue Intelligence y CAPI para Innovart — creados el 2026-06-21. Arquitectura, ubicaciones, cadena de orquestación y cuándo usar cada uno.
metadata:
  type: project
---

# Sistema Revenue Intelligence — 4 Agentes CAPI

Creados el 2026-06-21. El objetivo es convertir datos del funnel en aprendizaje real del algoritmo de Meta (ingresos, no formularios).

## Cadena lógica

```
chief-revenue-intelligence-officer   ← Director estratégico (coordina los 3)
             │
  ┌──────────┼──────────┐
  ▼          ▼          ▼
meta-medical-  capi-revenue-  meta-learning-
auditor        orchestrator   architect
(detecta fugas)(construye)    (entrena Meta)
```

---

## 1. `meta-medical-auditor` — Auditor forense (solo lectura)

**Tipo:** custom agent (`~/.claude/agents/meta-medical-auditor.md`)
**Invocación:** `Agent(subagent_type: "meta-medical-auditor", ...)`

**Qué hace:** Detecta fugas de datos que impiden que Meta aprenda correctamente. NUNCA modifica nada.

Audita: Meta (Pixel, CAPI, Dataset, EMQ, Custom Conversions, AEM, Audiencias, Campañas) + GHL (Pipelines, Workflows, Forms, Tags, Custom Fields) + Shopify (Customers, Orders, LTV) + Supabase (Eventos, Tablas, Integridad).

**Entrega:** Scorecard con 8 dimensiones (Tracking, Meta, CAPI, CRM, Revenue, Learning, Attribution, Data Integrity).

---

## 2. `capi-revenue-orchestrator` — CTO de Tracking

**Tipo:** custom agent (`~/.claude/agents/capi-revenue-orchestrator.md`)
**Invocación:** `Agent(subagent_type: "capi-revenue-orchestrator", ...)`

**Qué hace:** Diseña, construye y mantiene toda la infraestructura de captación, seguimiento y atribución. Siempre inicia con MCP Discovery Phase (mapeo completo de sistemas activos antes de actuar).

**MCPs disponibles:** Meta (meta-dajf), GHL Master, Shopify, Supabase, Gmail, Google Calendar, Google Drive, Canva, Apify, Stitch.

**Eventos maestros que gestiona:** Lead → QualifiedLead → Contact → AppointmentScheduled → AppointmentConfirmed → AppointmentAttended → TreatmentAccepted → Purchase → Patient → VIPPatient → HighValuePatient → RepeatPatient

---

## 3. `meta-learning-architect` — Entrenador del algoritmo

**Tipo:** skill (`~/.claude/skills/meta-learning-architect/skill.md`)
**Invocación:** `/meta-learning-architect`

**Qué hace:** Descubre qué características tienen los pacientes que generan más ingresos y le enseña eso a Meta. No audita infraestructura — esa es tarea del Orquestador.

**Analiza:** Leads, Pacientes, Ventas, Asistencias, No-Shows, Recompras, LTV, Fuente, Campaña, Anuncio, Audiencia.

**Clasifica:** Lead / Lead Calificado / Paciente / Paciente Ideal / Paciente Premium / Paciente VIP.

**Entregables:** Perfil Paciente Ideal, Patrones Detectados, Señales Recomendadas, Eventos Recomendados, Audiencias Recomendadas, Roadmap de Aprendizaje, Plan de Optimización.

**North Star:** Cambiar de CPL → Costo por Asistido → ROAS real.

---

## 4. `chief-revenue-intelligence-officer` (CRIO) — Director estratégico

**Tipo:** skill (`~/.claude/skills/chief-revenue-intelligence-officer/skill.md`)
**Invocación:** `/chief-revenue-intelligence-officer`

**Qué hace:** Lee las auditorías, arquitecturas y hallazgos de los 3 agentes → prioriza acciones → calcula impacto → diseña el roadmap. No ejecuta configuraciones, dirige estrategia.

**Pregunta maestra:** ¿Qué acción genera el mayor impacto en ingresos con el menor esfuerzo?

**Priorización:**
- P1: Impacto Alto + Esfuerzo Bajo
- P2: Impacto Alto + Esfuerzo Medio
- P3: Impacto Medio + Esfuerzo Bajo
- P4: Impacto Bajo

**Entregables:** Dashboard ejecutivo (7 dimensiones), Top Problemas, Top Oportunidades, Acciones Prioritarias, Roadmap 30/90/180 días, KPIs recomendados.

---

## Cuándo usar cada uno

| Necesidad | Agente |
|---|---|
| Visión ejecutiva + roadmap | `/chief-revenue-intelligence-officer` (arrancar aquí siempre) |
| "¿Qué está roto en CAPI?" | `meta-medical-auditor` |
| "Construir/reparar infraestructura de tracking" | `capi-revenue-orchestrator` |
| "¿Qué le enseñamos a Meta?" + audiencias | `/meta-learning-architect` |

**Why:** Javier diseñó este ecosistema para atacar el problema de fondo: Meta lleva meses optimizando para el hombre que abre un chat curioso, no para el que opera. El EMQ era 4.9 y Purchase recién activado (2026-06-14).

**How to apply:** Siempre arrancar con el CRIO para decidir qué agente lanzar primero según el objetivo de negocio del momento.
