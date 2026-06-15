---
name: integracion-ghl-meta-capi
description: "Worker Cloudflare activo para todas las 5 sedes de Innovart; envía 9 eventos a Meta CAPI con PII hasheada, ctwa_clid y fbc. FASE 1 y FASE 2 completadas al 2026-06-08."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e59d124-363f-4666-9838-f5c75f5725c2
---

# GHL ↔ Meta CAPI — Estado al 2026-06-08

## ⚠️ Estado 2026-06-14 — El Purchase de VENTA ("Ganado") sigue SIN llegar a Meta

**Verificado en Meta (Events Manager API, 28 días, ambos píxeles `1642103999710262` + `1625645205284016`): `Purchase = 0`.** Nada manda el Purchase de venta. Dos causas confirmadas:

1. **Cron `innovart-meta-capi`** mapea Ganado→Purchase, PERO la opp **pasa por "Ganado Y cancelado" en segundos** (el workflow `11. Venta-Ganado → Operacion-Programacion` la mueve de inmediato a Operaciones) → el poll de 5 min **no la alcanza**. Por eso la etapa está **siempre vacía (0 opps en las 6 sedes)**: es de **paso por diseño**, NO un bypass del comercial. URL del cron no responde (HTTP 000) — posiblemente apagado.
2. **El `custom_code` "CAPI → Meta (Purchase)"** del workflow "Etiqueta Ganado y cancelado" (Bogotá `b2028df1`, Medellín `2f78cf72`, Barranquilla `5b2fdd06`, Panamá dedicado `aa67d560`) **NO funciona**: GHL custom_code no puede hacer `fetch` + usa `action_source:'crm'` (inválido). Parte del set "nunca funcionó" → ver [[capi-webhook-worker]].

**Diseño de pase CONFIRMADO por prueba (2026-06-14):** creé una opp en "Ganado Y cancelado" (Barranquilla) → el workflow corrió (aplicó tags `oportunidad ganado` + `oportunidad operacion programacion de cirugia`, opp movida a Operaciones por wf11). El gatillo está BIEN. **NO mover el trigger a Operaciones** (sería doble disparo). El cuello no es el trigger — es el método de envío (custom_code muerto).

**✅ FIX HECHO Y VERIFICADO (2026-06-14):** convertido el Purchase de venta de `custom_code` (muerto, no hace fetch) → **acción Webhook** al worker `innovart-capi-webhook-no-tocar` en el workflow "Etiqueta Ganado y cancelado" de las 4 sedes que venden. Pasos: Add Tag `oportunidad ganado` → Remove Tags → **Webhook "CAPI Meta Webhook (NO TOCAR)"** (POST). Triggers (Opportunity Created + Pipeline Stage Changed en etapa Ganado) intactos.

| Sede | Workflow | Versión | URL webhook (Purchase) |
|---|---|---|---|
| Bogotá Ads | `b2028df1` | v9 | `…/?k=7743365e334edde60edadf38dec1ad21&event=Purchase&value=8000000&currency=COP` |
| Medellín | `2f78cf72` | v9 | idem (COP 8M) |
| Barranquilla | `5b2fdd06` | v8 | idem (COP 8M) |
| Panamá | `aa67d560` ("…CAPI Purchase USD") | v6 | `…&event=Purchase&value=3500&currency=USD` |

⚠ Panamá: al `ec941c4f` "Etiqueta Ganado y cancelado" se le **quitó** el custom_code Purchase (quedó solo tags) para no duplicar con `aa67d560`. El `value` 8M que se había metido al custom_code (Med/Baq) quedó obsoleto: el paso ahora es webhook.

**Verificación 2026-06-14:**
1. **GHL:** crear opp en "Ganado Y cancelado" → workflow corre, aplica tags y wf11 mueve a Operaciones (pase confirmado).
2. **Meta (definitiva):** `curl` POST Purchase $8M COP al worker → Meta respondió **`events_received:1` en AMBOS píxeles** (`1642…` + `1625…`), matchKeys `em,ph,fn,ln,country,external_id`, `messages:[]` (sin errores). Cadena completa funcionando. Aparece agregado en Events Manager en ~15-30 min.

Cron `innovart-meta-capi` no responde (HTTP 000 → ~apagado) = sin riesgo de doble Purchase.

**Pendiente:** (a) confirmar visualmente en Events Manager las próximas ventas reales; (b) si se quiere `fbc`/fbclid en el match, agregar custom data en la acción Webhook (hoy matchea por PII, 6 claves = EMQ alto); (c) IPS Principal no vende (no requiere Purchase); (d) Bucaramanga: borrar pipeline "Ventas" duplicado.

**Mapa de IDs — trigger del Purchase de venta por sede:**

| Sede | Location | Pipeline Ventas | Etapa "Ganado Y cancelado" | Pipeline Operaciones | Etapa "Programación cirugía" |
|---|---|---|---|---|---|
| Bogotá Ads | DgjjDzD9nkCKv8AGF1Qb | RpC0O3mYkxyKV1jvMqm6 | 50d2786c-a074-4812-819f-c6395bc739f4 | B9faYO7EER00acsuqxv9 | 88e69b46-7e15-42b0-8b2d-1626d35d0cd0 |
| Medellín | h8DplQKVE6epDbbj5Kg8 | 8vqcl7aQIBiR2YiebPv3 | 847bb988-3fdf-4693-9cc1-3e782e1e1bfe | SxkXqYkZzNjl84WJnBeq | dc3cfbb6-e68c-4ed3-8834-2d83ef479679 |
| Barranquilla | cXH8KbMaAPGzkmf3Z2pP | fJqdW5ZKRTQZ68Dv57Sr | 2489801f-ee0a-4001-b6cd-f7d9c27a158d | NchoLsboSYN89VwflGM7 | 12105dcf-115b-4bc1-9ee0-803d9e8bfab4 |
| Panamá | 45SKYgIDgr4Eh6a6JcFz | uFYBp4Jr378BK7bWYn58 | 48807d03-b21f-4cfc-8c04-e889be1ec902 | LDjxHqsvjVap61Z1nOAr | b284a6fe-bfe5-454f-8dc3-8ab01d137095 |
| IPS Principal | NPhQTmLOHd6FbDtqLPnG | ZUMTSA6dbzMnXFlOBGzi | b09608a9-0a27-48d7-820e-82249242721a | HgGTdUkQTFC15Wjqean6 | 10d4147c-f701-49ee-8adf-69dc626f1a5a |
| Bucaramanga | s40Wa8mXYBxlFCieKohO | r6twTNR4DbLvYrtXCIHR (+ dup `qwGmtY8FB2p4ImnppWCE` — borrar) | 84f5adf8-107e-43f9-aa51-a19009181adc | nFn2m2clpGe9UAKFAbwO | 34ff4408-b1f5-4617-80c4-afc9e474c002 |

**Notas:** IPS Principal **no hace ventas** (es el intake de leads de redes) → no necesita Purchase. Valores del Purchase por sede: **Panamá USD 3.500** (`system_generated`, +507, v3.1 — el más completo), **Bogotá/Medellín/Barranquilla COP 8.000.000**. Panamá además tiene la **matriz CAPI completa** como workflows separados (Lead/Contact/Schedule/ViewContent/no_show/lost_lead/Purchase) — todos custom_code, así que también muertos hasta pasarlos a webhook.

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
