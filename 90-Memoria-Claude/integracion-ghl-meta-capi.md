---
name: integracion-ghl-meta-capi
description: Worker Cloudflare activo para todas las 5 sedes de Innovart; envía 9 eventos a Meta CAPI con PII hasheada, ctwa_clid y fbc. FASE 1 y FASE 2 completadas al 2026-06-08.
metadata:
  type: project
---

# GHL ↔ Meta CAPI — Estado al 2026-06-08

## Infraestructura desplegada

**Worker:** `innovart-meta-capi` en Cloudflare  
**URL:** `https://innovartmedicalips.workers.dev`  
**Cron:** cada 5 minutos (pull de contactos y oportunidades)  
**Meta Pixel:** `1642103999710262` (Pixel CRM)  
**Meta Token:** en el Worker (variable hardcoded)

## Sedes activas (5)

| Ciudad | Location ID | ctwaFieldId | fbFieldId |
|--------|-------------|-------------|-----------|
| Bucaramanga | s40Wa8mXYBxlFCieKohO | UHB4VHlBQ2XnnZODeGRK | FYVJpTGSmAPhiqoRwm97 |
| Medellín | h8DplQKVE6epDbbj5Kg8 | 4V2IZiwCCkLdt0jTUI8K | SFpTjWRflMI3AURvNBqF |
| Panamá | 45SKYgIDgr4Eh6a6JcFz | Ckdb2494518FRWLHLb7n | LkIdo9AQD1a7tevGrfzM |
| Barranquilla | cXH8KbMaAPGzkmf3Z2pP | lr9AYYbE3MKxcbMqGOew | fMwEe8gzC5AxkOw8D7D5 |
| IPS Principal (Bogotá-CRM) | NPhQTmLOHd6FbDtqLPnG | pmfzBxCFdjeojgCLmEWu | wy6FYlxKsMDvtXljeC9O |

> ⚠️ **CORRECCIÓN 2026-06-13:** La subcuenta **Bogotá Ads (DgjjDzD9nkCKv8AGF1Qb) NO está en este cron — y SÍ era necesario.** Es el **intake principal de WhatsApp FB/IG ads (25,627 contactos)**. Al no estar en el cron, esos leads NO mandaban `Lead` server-side (y al entrar por WhatsApp, tampoco había evento de navegador) = **hueco grande**. Cerrado con un webhook de Lead independiente → ver [[capi-webhook-worker]]. Pendiente: el funnel de DgjjDzD9 (si los leads avanzan ahí dentro) y capturar `ctwa_clid` (no existe el campo en DgjjDzD9).

## Eventos enviados a Meta CAPI

| Evento Meta | Trigger GHL | Notas |
|-------------|-------------|-------|
| Lead | Nuevo contacto creado | Desde processNewContacts |
| InitiateCheckout | Stage "Frio Setter" / "Interesado" | Solo Medellín, Panamá, Barranquilla, IPS Principal |
| Contact | Stage "Cte Calificado" | Todas las sedes |
| CompleteRegistration | Stage "Cte Comprometido" | Todas las sedes |
| Schedule | Stage "Cte Agenda Valoracion" (presencial) | Todas las sedes |
| Schedule | Stage "Valoración Virtual Seguimiento" (virtual) | Medellín, Panamá, Barranquilla, IPS Principal |
| ViewContent | Stage "En Valoración" | Todas las sedes |
| NoShow | Stage "No Show" | Todas las sedes |
| Purchase | Stage "Ganado" con monetaryValue | Todas las sedes; COP en Colombia, USD en Panamá |
| Lost | Stage "Perdido" | Todas las sedes |

## Datos enviados con cada evento

- `em`, `ph`, `fn`, `ln` → SHA-256 hasheados
- `external_id` → contactId de GHL (clave de matching persistente)
- `ct` → ciudad, `country` → código país
- `ctwa_clid` → si existe en customField (leads WhatsApp)
- `fbc` → `fb.1.{timestamp}.{fbclid}` si existe en customField fb_click_id
- `event_id` → `{contactId}_{eventName}_{Math.floor(eventTime/300)}` para deduplicación por ventana 5min

## Arquitectura técnica clave

- **stages object:** `{stageId: eventName}` (no al revés) — permite N stages → mismo evento (Schedule presencial + virtual)
- **Bogotá sin InitiateCheckout:** Bucaramanga no tiene stage equivalente; simplemente omitido
- **Purchase valor:** `opp.monetaryValue` del campo monetario de la oportunidad en GHL

## Detalles verificados del código (descargado 2026-06-13)
Fuente descargable vía CF API: `GET https://api.cloudflare.com/client/v4/accounts/<acc>/workers/scripts/innovart-meta-capi` (endpoint `/content` da 405 con User API Token; el endpoint sin `/content` sí devuelve el JS). Cuenta `d85e2b4ba4cdb4d7a59d17621f80eb3c`.
- **1 SOLO píxel** en el cron: `1642103999710262` (los webhooks nuevos mandan a 2: +`1625645205284016`). Token Meta del cron ≠ token del webhook worker (son distintos, ambos válidos). `action_source: system_generated`, Graph `v21.0`.
- `processNewContacts`: trae contactos creados en ventana de **6 min** (`startAfter`), `limit=100` **sin paginar** → cada uno manda **Lead**. Cron cada 5 min (overlap 1 min).
- `processOpportunities`: trae **100 oportunidades sin `startAfter` ni paginación** y filtra en código por `lastActivityDate`/`updatedAt` ≥ 6 min → a volumen alto **puede perder cambios de etapa** (depende del orden que devuelva el endpoint). Riesgo real a vigilar.
- Cada sede tiene su **PIT** (`pit-...`) hardcodeado y su mapa `stageId → eventName` (están en el código). Los PIT coinciden con los que usa el MCP de ghl por sede.
- Match (`sendToMeta`): `external_id` + `ct`(ciudad) + `country` siempre; + `em/ph/fn/ln` SHA-256 si existen; + `ctwa_clid`/`fbc` si los campos custom de esa sede tienen valor.

## FASE 1 completada: Match de Identidad

Los campos `ctwa_clid` y `fb_click_id` fueron creados en todas las 5 sedes activas vía GHL API.

## FASE 2 completada: Pipeline completo de ventas

Todos los stages del pipeline de Ventas de cada sede están mapeados a eventos Meta CAPI. El pipeline de Operaciones fue excluido deliberadamente — foco en la venta primero.

## Pendiente — FASE 3: Audiencias Inteligentes

Crear en Meta Ads Manager:
- Audiencia retargeting: Schedule sin Purchase (180 días)
- Audiencia retargeting: ViewContent sin Schedule (90 días)
- Audiencia retargeting: NoShow (30 días, reimpactar)
- Lookalike 1% basado en Purchase
- Lookalike 1% basado en Schedule
- Exclusión: Lost + Purchase (no malgastar presupuesto)

## Pendiente — FASE 4: Optimización por Purchase

Cuando se acumulen ~50 eventos Purchase/semana:
- Cambiar optimización de campaña: Lead → Purchase
- Activar Value-Based Bidding con monetaryValue de GHL
- Comunicar al trafiker cuando alcance el umbral

## Pendiente — fbclid en funnels restantes

Los funnels de Medellín, Panamá, Barranquilla, IPS Principal aún NO tienen el JS que captura fbclid. El campo fb_click_id existe en GHL pero no se llena desde tráfico web. Javier indicó no tocar esas landing pages por ahora.

## Informe generado

PDF: `Innovart_CAPI_Informe_2026-06-08` en Drive CLAUDE (ID: 1TYWY7axJFjFQGagtQJWzB7s2GKFXgjqz)

**Why:** La integración CAPI server-side es la base para mejorar EMQ (objetivo 8.0+), reducir CPL, y eventualmente optimizar por Purchase con valor real.  
**How to apply:** No duplicar eventos ya mapeados. Al agregar nuevas sedes o stages, seguir el patrón `{stageId: eventName}` en LOCATIONS.
