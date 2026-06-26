---
name: campana-whatsapp-business-medellin-2026-06-25
description: Análisis de la campaña WHATSAPP BUSSINES (MEDELLIN) — 11 ad sets, objetivos heterogéneos (CONVERSATIONS vs LEAD_GENERATION), utm_source por tipo de anuncio, Pixel CRM 62 + App CLAUDE CODE DA-JF.
metadata:
  type: project
  date: 2026-06-25
  company: Innovart
---

# Campaña WHATSAPP BUSSINES — MEDELLIN (25 junio 2026)

## Estado Actual

**Campaign ID:** 120246851116100679  
**Account:** MEDELLIN (`act_874169544322810`)  
**Status:** Mix (5 ACTIVOS + 6 PAUSED)  
**Ad Sets:** 11 total  
**Pixel:** 1642103999710262 (CRM "Pixel CRM terminado 62")  
**App (CAPI):** 1698932239801923 (CLAUDE CODE DA-JF)  

## 11 Ad Sets — Análisis por Objetivo

| Ad Set ID | Nombre | Status | Objetivo | Placements | utm_source | Presupuesto/día |
|-----------|--------|--------|----------|------------|-----------|-----------------|
| 120248999028870679 | BOGOTÁ - TEST-/18/06/2026 | ✅ ACTIVE | CONVERSATIONS | WhatsApp Business | `whatsapp` | $90K COP |
| 120248878894410679 | BOGOTÁ - TEST-/16/06/2026-(ESTETICO) | ✅ ACTIVE | CONVERSATIONS | WhatsApp Business | `whatsapp` | $76.9K COP |
| 120248669330110679 | PANAMA- WB - TEST-11/06/2026 | ✅ ACTIVE | CONVERSATIONS | WhatsApp Business | `whatsapp` | $130K COP |
| 120248511820560679 | BARRANQUILLA - WB - TEST-9/06/2026 | ✅ ACTIVE | CONVERSATIONS | WhatsApp Business | `whatsapp` | $42K COP |
| 120248503915610679 | BOGOTÁ - TEST-/09/06/2026 | ⏸️ PAUSED | CONVERSATIONS | WhatsApp Business | `whatsapp` | $60K COP |
| 120247608277780679 | BOGOTÁ - TEST MUNDIAL 26/05/2026 | ⏸️ PAUSED | CONVERSATIONS | WhatsApp Business | `whatsapp` | $40K COP |
| 120247329482990679 | BOGOTÁ - Copia | ⏸️ PAUSED | LEAD_GENERATION | Facebook/Instagram Forms | `lead_gen` | $270K COP |
| 120247329448560679 | BARRANQUILLA - WB | ⏸️ PAUSED | LEAD_GENERATION | Facebook/Instagram Forms | `lead_gen` | $80K COP |
| 120246856693680679 | BOGOTÁ | ⏸️ PAUSED | LEAD_GENERATION | Facebook/Instagram Forms | `lead_gen` | $40K COP |
| 120246856491410679 | MEDELLIN | ✅ ACTIVE | LEAD_GENERATION | Facebook/Instagram Forms | `lead_gen` | $130K COP |
| 120246851116090679 | BARRANQUILLA | ⏸️ PAUSED | LEAD_GENERATION | Facebook/Instagram Forms | `lead_gen` | $90K COP |

**Total presupuesto activo:** $468.9K COP/día  
**Gasto PAUSED:** $520K COP/día (puede reactivarse)

## Lógica utm_source

**Por objetivo:**
- **CONVERSATIONS** (6 ad sets) → `utm_source=whatsapp` — objetivo es generar DMs/mensajes
- **LEAD_GENERATION** (5 ad sets) → `utm_source=lead_gen` — objetivo es generar leads por formulario de Facebook/Instagram

## ⚠️ Hallazgo Crítico

**Ad set MEDELLIN (120246856491410679):**
- 43% del gasto total activo ($130K de $468.9K)
- Objetivo: LEAD_GENERATION (no CONVERSATIONS)
- Pero el nombre de la campaña es "WHATSAPP BUSSINES"
- **Implicación:** Este ad set usa formularios, NO Click-to-WhatsApp

**Pregunta resuelta:** ¿UTM correcto para WHATSAPP BUSSINES?
- Ad sets de CONVERSATIONS → `utm_source=whatsapp`
- Ad set de LEAD_GENERATION → `utm_source=lead_gen`
- **NO es `utm_source=instagram` para todos**

## Próximos Pasos (Javier)

1. **Validar utm_source por ad set** — Confirmar que la tabla arriba refleja la realidad (placements reales por objetivo)
2. **Carga de UTMs** — Aplicar UTMs sugeridos a todos los ads usando el método [[metodo-carga-utms-api-meta]]
3. **Validación post-carga** — Meta Ads Manager → verificar parámetros en URLs + Pixel 62 asignado + App CLAUDE CODE DA-JF en eventos

## Referencias

- [[metodo-carga-utms-api-meta]] — Cómo cargar UTMs por API
- [[feedback-cuentas-meta-no-son-sedes]] — Los nombres de ad set (BOGOTÁ, PANAMA, BARRANQUILLA) NO indican la sede real; están dentro de la cuenta MEDELLIN
- [[guia-mcp-meta-ads]] — Account IDs y herramientas disponibles
