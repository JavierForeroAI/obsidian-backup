---
name: auditoria-capimetaghl-base
description: "Diagnóstico maestro + base para el AGENTE DE AUDITORÍA DIARIA del sistema CAPIMETAGHL (6 subcuentas GHL ↔ Meta CAPI). Inventario, 3 mecanismos de envío, matriz de eventos, estándar canónico, checklist de auditoría con herramientas y valores esperados. Estado 2026-06-14."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4e59d124-363f-4666-9838-f5c75f5725c2
---

# Sistema CAPIMETAGHL — Diagnóstico Maestro y Base de Auditoría Diaria

> Innovart Medical IPS · 6 subcuentas GoHighLevel ↔ Meta Conversions API · **estado verificado 2026-06-14**
> Este documento es la **línea base** del agente de auditoría diaria. Todo valor "esperado" aquí es el estándar contra el cual auditar.

---

## 0. Resumen ejecutivo

**CAPIMETAGHL** = el envío de conversiones server-side desde GoHighLevel (CRM) hacia Meta (Conversions API), por sede.

**3 mecanismos de envío coexisten** (en orden de validez):

| # | Mecanismo | Estado | Úsalo |
|---|---|---|---|
| A | **Webhook worker** `innovart-capi-webhook-no-tocar` | ✅ FUNCIONA (validado `events_received:1`) | **SÍ — estándar** |
| B | **Cron worker** `innovart-meta-capi` | ⚠️ Dudoso (HTTP 000 hoy, ~apagado) | A confirmar |
| C | **`custom_code` dentro de workflows GHL** | ❌ MUERTO (GHL no hace `fetch` + `action_source:'crm'` inválido) | **NO — migrar a webhook** |

**Estado global a 2026-06-14:** el **Purchase de venta** (lo más valioso) **ya llega a Meta** en las 4 sedes que venden (migrado a webhook hoy). Antes era **0**. El **Lead de Bogotá Ads** (intake principal, ~25K) también se cerró por webhook (2026-06-13). Falta migrar el **funnel intermedio** (Contact/Schedule/ViewContent/NoShow) que aún depende del cron dudoso y de custom_code muerto.

---

## 1. Inventario de las 6 subcuentas GHL

| Sede | Location ID | ¿Vende? | En cron? | Rol | API key (PIT) |
|---|---|---|---|---|---|
| **Bogotá Ads** | `DgjjDzD9nkCKv8AGF1Qb` | ✅ Sí | ❌ No | **Intake principal** WhatsApp FB/IG ads (~25.627 contactos) | `pit-5aef6ddf…` |
| **Medellín** | `h8DplQKVE6epDbbj5Kg8` | ✅ Sí | ✅ Sí | Sede comercial | `pit-dc7562f7…` |
| **Barranquilla** | `cXH8KbMaAPGzkmf3Z2pP` | ✅ Sí | ✅ Sí | Sede comercial | `pit-b7a6804a…` |
| **Panamá** | `45SKYgIDgr4Eh6a6JcFz` | ✅ Sí (USD) | ✅ Sí | Sede comercial (USD) | `pit-bcca0797…` |
| **IPS Principal** | `NPhQTmLOHd6FbDtqLPnG` | ❌ No | ✅ Sí | Intake leads de redes (no cierra ventas) | `pit-0a14244b…` |
| **Bucaramanga** | `s40Wa8mXYBxlFCieKohO` | ❌ (vacía) | ✅ Sí | Nueva, ~0 oportunidades (solo tests) | `pit-083c9e3c…` |

> Nota: las API keys (PIT) están en el registro del MCP `ghl` y, las de las 5 sedes del cron, hardcodeadas en el cron worker.

---

## 2. Infraestructura de envío

### A) Webhook worker — `innovart-capi-webhook-no-tocar` ✅ ESTÁNDAR
- **URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev`
- **Clave:** `?k=7743365e334edde60edadf38dec1ad21` (WEBHOOK_KEY, obligatoria)
- **Píxeles:** postea a los **2** por defecto (`1642103999710262`, `1625645205284016`).
- **action_source:** `system_generated` · `event_id`: `{contactId}_{event}_{floor(ts/300)}` (dedup 5 min).
- **Config por query string:** `&event=<Nombre>&value=<n>&currency=<COP|USD>` (opcional `&country=`, `&pixels=`, `&test=<code>`, `&debug=1`).
- **PII:** la saca del **body nativo de GHL** (`contact_id, first_name, last_name, email, phone, country, tags…`). Los custom fields (fbclid) NO vienen salvo que se agreguen como "custom data" en la acción Webhook.
- **Match logrado sin custom data:** `em, ph, fn, ln, country, external_id` (6 claves → EMQ alto).
- **Secrets:** `META_CAPI_TOKEN`, `WEBHOOK_KEY`. **Fuente local:** `/Users/javierforero/innovart-capi-webhook-no-tocar/` · deploy `wrangler deploy`. CF acc `d85e2b4ba4cdb4d7a59d17621f80eb3c`.
- **Cómo se conecta en GHL:** acción `type:"webhook"`, `attributes:{url, method:"POST"}`. **Se persiste por MCP** (`update_workflow_actions`) y **NO exige "test"** (a diferencia del custom_code) → ejecuta directo al publicar.

### B) Cron worker — `innovart-meta-capi` ⚠️ A CONFIRMAR
- **URL:** `https://innovartmedicalips.workers.dev` — **hoy responde HTTP 000 (parece apagado).**
- Cron cada 5 min. Manda a **1 píxel** (`1642103999710262`). `action_source: system_generated`, Graph v21.0.
- Cubre **5 sedes** (Bucaramanga, Medellín, Panamá, Barranquilla, IPS Principal) — **NO Bogotá Ads**.
- Hace: **Lead** por contacto nuevo (ventana 6 min) + **funnel por etapa** (`stageId → eventName`).
- **Riesgos estructurales:** (1) trae 100 oportunidades **sin paginar** → a volumen alto puede perder cambios de etapa; (2) el poll de 5 min **no alcanza el pase transitorio por "Ganado Y cancelado"** (la opp se mueve a Operaciones en segundos) → por eso el Purchase de venta nunca salió por el cron.

### C) custom_code en workflows ❌ MUERTO — NO USAR
- El `custom_code` de GHL **no puede hacer `fetch`** (sandbox sin red) → cualquier paso "CAPI → Meta" por custom_code **no envía nada**.
- Además muchos usaban `action_source:'crm'` (inválido, Meta rechaza). El válido es `system_generated`.
- **Todo custom_code CAPI debe migrarse a acción Webhook.** Pendientes vivos: matriz de Panamá (Lead/Contact/Schedule/ViewContent/no_show/lost_lead) y los `CAPI Frio Stale 45d`.

---

## 3. Píxeles Meta

| Píxel | Rol | Qué recibe hoy |
|---|---|---|
| `1642103999710262` | "Pixel CRM" | Casi solo **PageView web** (~133K/28d). CAPI server por webhook/cron. **La web Shopify `www.innovartmedical.com` dispara a ESTE píxel (el "262")** — confirmado por Javier 2026-06-17. |
| `1625645205284016` | Pixel web/funnel | Eventos de navegador del funnel (Lead, ViewContent, InitiateCheckout, Schedule, clickfunnel…) + CAPI por webhook. |

> El **webhook** manda a los 2; el **cron** manda solo a `1642`. **Estándar: ambos píxeles.** Token CAPI = custom value `{{ custom_values.meta_capi_token }}` (`BhBhR3Hj03iYSAMHcS8L`).

---

## 4. Mapa de pipelines y etapas por sede (IDs) — para detectar drift

| Sede | Pipeline Ventas | Etapa "Ganado Y cancelado" (dispara Purchase) | Pipeline Operaciones | Etapa "Programación de cirugía" (ventas reales) |
|---|---|---|---|---|
| Bogotá Ads | `RpC0O3mYkxyKV1jvMqm6` | `50d2786c-a074-4812-819f-c6395bc739f4` | `B9faYO7EER00acsuqxv9` | `88e69b46-7e15-42b0-8b2d-1626d35d0cd0` |
| Medellín | `8vqcl7aQIBiR2YiebPv3` | `847bb988-3fdf-4693-9cc1-3e782e1e1bfe` | `SxkXqYkZzNjl84WJnBeq` | `dc3cfbb6-e68c-4ed3-8834-2d83ef479679` |
| Barranquilla | `fJqdW5ZKRTQZ68Dv57Sr` | `2489801f-ee0a-4001-b6cd-f7d9c27a158d` | `NchoLsboSYN89VwflGM7` | `12105dcf-115b-4bc1-9ee0-803d9e8bfab4` |
| Panamá | `uFYBp4Jr378BK7bWYn58` | `48807d03-b21f-4cfc-8c04-e889be1ec902` | `LDjxHqsvjVap61Z1nOAr` | `b284a6fe-bfe5-454f-8dc3-8ab01d137095` |
| IPS Principal | `ZUMTSA6dbzMnXFlOBGzi` | `b09608a9-0a27-48d7-820e-82249242721a` | `HgGTdUkQTFC15Wjqean6` | `10d4147c-f701-49ee-8adf-69dc626f1a5a` |
| Bucaramanga | `r6twTNR4DbLvYrtXCIHR` (+ dup `qwGmtY8FB2p4ImnppWCE` — borrar) | `84f5adf8-107e-43f9-aa51-a19009181adc` | `nFn2m2clpGe9UAKFAbwO` | `34ff4408-b1f5-4617-80c4-afc9e474c002` |

**Diseño de pase (importante):** el comercial mueve la venta a "Ganado Y cancelado" → el workflow **`11. Venta-Ganado → Operacion-Programacion`** la **mueve sola** a Operaciones › "Programación de cirugía". Por eso "Ganado Y cancelado" siempre está en **0 opps** (es de paso). **El Purchase debe dispararse en la ENTRADA a "Ganado Y cancelado"** (no en Operaciones; ahí sería tarde / doble).

---

## 5. Matriz de eventos CAPI (estado canónico 2026-06-14)

| Evento Meta | Qué lo dispara | Mecanismo correcto | Sedes | Estado |
|---|---|---|---|---|
| **Lead** | Contacto nuevo | Webhook (Bogotá Ads) / Cron (otras) | Todas | Bogotá ✅ webhook · resto ⚠️ depende del cron |
| **Purchase (venta)** | Entra a "Ganado Y cancelado" | **Webhook** | Bogotá, Med, Baq (COP 8M) · Panamá (USD 3500) | ✅ **HECHO HOY** |
| **Purchase (financiación)** | `customer_reply` "Meddipay" | Webhook | Bogotá, Med, Baq | ✅ (2026-06-13) |
| Contact / Schedule / ViewContent / NoShow | Etapas del funnel Ventas | Cron (hoy) | 5 sedes | ⚠️ depende del cron + custom_code muerto redundante |
| lost_lead | Frío estancado 45d / Perdido | Webhook (debe) | varias | ❌ hoy custom_code muerto |

---

## 6. Estado por sede (detalle)

- **Bogotá Ads** `DgjjDzD9` — NO en cron. ✅ Lead webhook (`fd50246d`, trigger `contact_created`). ✅ Purchase venta webhook (`b2028df1` v9). ✅ Purchase financiación webhook (`20eb73fb`). ⚠️ Sin funnel intermedio (Contact/Schedule/…) si el lead avanza dentro de DgjjDzD9. ⚠️ No existe campo `ctwa_clid` (match por tel+nombre). Custom fields: fb_click_id `1hdDWOfia3IljwbLwqNC`, fbclid `DnKbVMv2xH3kNEksDV5h`, fbp `xqGgBJ8iteGTBGOzRYeY`.
- **Medellín** `h8Dpl…` — en cron. ✅ Purchase venta webhook (`2f78cf72` v9, COP 8M). ✅ Financiación webhook (`c3572764`). ~54 opps en Operaciones/Programación.
- **Barranquilla** `cXH8K…` — en cron. ✅ Purchase venta webhook (`5b2fdd06` v8, COP 8M). ✅ Financiación webhook (`2f258215`). ~42 en Operaciones.
- **Panamá** `45SKY…` — en cron. ✅ Purchase venta webhook (`aa67d560` v6, **USD 3500**). `ec941c4f` "Etiqueta Ganado y cancelado" = solo tags (se le quitó el Purchase duplicado). ⚠️ Tiene matriz completa de funnel como custom_code (MUERTO) — migrar a webhook. ~32 en Operaciones.
- **IPS Principal** `NPhQ…` — **no vende** (intake de redes). En cron. 46 won históricos dispersos (legacy). No requiere Purchase.
- **Bucaramanga** `s40Wa…` — vacía (1 contacto de test). ⚠️ Pipeline "Ventas" duplicado (`qwGmtY8F…`) — borrar.

---

## 7. Lo que logramos (changelog)

**2026-06-13**
- Diagnóstico raíz: el `custom_code` de GHL no hace `fetch` → todo CAPI por custom_code estaba muerto.
- Se creó el **webhook worker** `innovart-capi-webhook-no-tocar` (hashea PII + manda a 2 píxeles).
- Migrado el **Purchase de financiación** (Meddipay) a webhook en Bogotá/Med/Baq → validado `events_received:1`.
- **Lead de Bogotá Ads** por webhook (`fd50246d`, `contact_created`) → cerró el hueco de ~25K leads que no mandaban Lead (DgjjDzD9 no está en el cron).

**2026-06-14 (hoy)**
- Auditoría completa de las 6 cuentas (pipelines, oportunidades, workflows, stats de Meta).
- Confirmado: **Purchase de venta = 0** en 28 días (ambos píxeles). Causa: custom_code muerto + cron no alcanza el pase transitorio por Ganado.
- Confirmado el **diseño de pase** (Ganado → Operaciones por wf11) con prueba en vivo.
- **Migrado el Purchase de venta a webhook** en las 4 sedes que venden (Bogotá/Med/Baq COP 8M, Panamá USD 3500). Triggers intactos.
- Panamá: eliminado el Purchase duplicado (`ec941c4f` quedó solo con tags).
- **Verificación definitiva:** POST de prueba → Meta `events_received:1` en los 2 píxeles, 6 match keys, sin errores.
- Memoria del sistema actualizada ([[integracion-ghl-meta-capi]]).

---

## 8. Estándar canónico (cómo debe quedar TODO el sistema)

1. **Todo evento CAPI sale por la acción Webhook** al worker `innovart-capi-webhook-no-tocar`. Cero `custom_code` con `fetch`.
2. **Siempre a los 2 píxeles** (`1642103999710262` + `1625645205284016`).
3. **`action_source: system_generated`** (nunca `crm`).
4. **`event_id` con ventana de 5 min** para dedup (lo hace el worker).
5. **Valor por país:** COP `8000000` en Colombia · USD `3500` en Panamá.
6. **Purchase de venta dispara en la ENTRADA a "Ganado Y cancelado"** (Opportunity Created + Pipeline Stage Changed), nunca en Operaciones.
7. **Un solo workflow manda cada evento por sede** (evitar duplicados como el de Panamá).
8. Workflows CAPI **publicados** y con **triggers activos**.

---

## 9. ⭐ ESPECIFICACIÓN DEL AGENTE DE AUDITORÍA DIARIA

**Objetivo:** verificar cada día que el sistema CAPIMETAGHL está enviando conversiones correctas a Meta, sin huecos ni duplicados, y alertar desviaciones.
**Frecuencia:** diaria. **Alcance:** las 6 subcuentas + 2 píxeles + 2 workers.

### Checklist (cada check: qué · cómo · esperado · severidad · remediación)

**C1 — Purchase llegando a Meta** 🔴
- Cómo: `ads_get_dataset_stats(dataset_id=1642103999710262, event_name="Purchase", aggregation="event_source", últimos 1-2 días)` y en `1625645205284016`.
- Esperado: `Purchase > 0` en días con ventas (cruzar con C11). Server/CRM, no solo web.
- Si 0 con ventas reales → 🔴 revisar workflows C4 + worker C6.

**C2 — Calidad de match / EMQ** 🟠
- Cómo: `ads_get_dataset_quality(dataset_id, query_type=["crm"])` en ambos píxeles.
- Esperado: canal `crm`/server presente, freshness reciente, EMQ alto (objetivo ≥ 6-8).
- Bajo EMQ → revisar que el body lleve em/ph/fn/ln/country/external_id.

**C3 — Volumen de eventos por tipo** 🟠
- Cómo: `ads_get_dataset_stats(aggregation="event", últimos 1-7 días)` por píxel → totales por evento.
- Esperado: Lead > 0 diario; Contact/Schedule/Purchase proporcionales al funnel.
- Caída brusca vs baseline (p.ej. Lead a 0) → 🔴.

**C4 — Workflows CAPI sanos (por sede)** 🔴
- Cómo: `switch_location` + `get_workflow_full(<id>)` de cada workflow CAPI (ver §11).
- Esperado por workflow: `status:"published"` · paso CAPI `type:"webhook"` (❌ NO `custom_code`) · URL del worker con `k`+`event`+`value`+`currency` correctos · **triggers `active:true`** en la etapa correcta (ver §4).
- Cualquier paso CAPI que sea `custom_code` → 🔴 (no envía).

**C5 — Píxeles consistentes** 🟠
- Esperado: cada acción webhook apunta a los 2 píxeles (el worker lo hace por defecto; verificar que no se haya forzado `&pixels=` a uno).

**C6 — Webhook worker vivo** 🔴
- Cómo: `curl -s -X POST ".../?k=7743365e334edde60edadf38dec1ad21&event=Purchase&value=8000000&currency=COP&debug=1" -d '{"contact_id":"audit","first_name":"A","last_name":"B","email":"a@b.com","phone":"+573000000000","country":"CO"}'`
- Esperado: HTTP 200 + JSON. (Con `debug=1` NO manda a Meta; quitar `debug` para test real → `events_received:1`.)
- HTTP 000 / error → 🔴 worker caído → redeploy desde `/Users/javierforero/innovart-capi-webhook-no-tocar/`.

**C7 — Estado del cron worker** 🟠
- Cómo: `curl https://innovartmedicalips.workers.dev` + revisar si el funnel (Contact/Schedule/…) sigue llegando (C3).
- Hoy: HTTP 000 (parece apagado). Decidir: reactivar o migrar funnel a webhook.

**C8 — Sin doble disparo** 🟠
- Cómo: en cada sede, un solo workflow debe mandar cada evento (revisar que no haya 2 workflows con webhook Purchase en la misma etapa — caso Panamá ya corregido).
- El `event_id` (dedup 5 min) protege entre worker-cron-webhook, pero 2 webhooks distintos en <5 min con mismo contacto también dedup; aún así, evitar duplicados de diseño.

**C9 — Captura de fbclid / ctwa_clid** 🟢
- Esperado: idealmente el match incluye `fbc`. Hoy va por PII (6 claves). DgjjDzD9 no tiene `ctwa_clid`.

**C10 — Drift de pipelines/etapas** 🟠
- Cómo: `get_pipelines(<location>)` y comparar IDs de Ventas/Ganado/Operaciones contra §4.
- Si cambió un stage ID → los triggers de los workflows CAPI quedan apuntando al viejo → 🔴 actualizar.

**C11 — Conciliación CRM vs Meta** 🟠
- Cómo: contar ventas reales = opps que entraron a Operaciones › "Programación de cirugía" en el día (`search_opportunities` por stage) y comparar con Purchase recibidos en Meta (C1).
- Gap grande (ventas >> Purchase) → 🔴 algo no dispara.

### Salida del agente (formato sugerido)
- Tabla por sede × check con ✅/🟠/🔴 + nota.
- Lista de alertas 🔴 priorizadas con remediación.
- KPIs del día: Lead, Purchase (COP/USD por separado), EMQ por píxel.
- Guardar histórico para detectar tendencias.

> ⚠️ Reportes por correo: HTML email-safe (tablas + inline styles). Entregables de auditoría GHL → Drive `1LCzzvFFQgz-SHm_5raj2DTBOoJYsli3A`. Ver [[feedback-email-formato]], [[feedback-carpeta-auditoria-ghl]].

---

## 10. Pendientes / roadmap

- **Migrar el funnel intermedio** (Contact/Schedule/ViewContent/NoShow) y `lost_lead` de custom_code/cron → **webhook** (sobre todo Panamá y, si el cron está apagado, todas).
- **Confirmar destino del cron** `innovart-meta-capi` (apagar oficialmente o reactivar).
- **Bogotá Ads:** decidir si el funnel avanza dentro de DgjjDzD9 (faltan webhooks de etapa) o se mueve a una sede cubierta.
- **ctwa_clid** en DgjjDzD9 (no existe el campo) → proyecto applevel.
- **Bucaramanga:** borrar pipeline "Ventas" duplicado.
- **FASE 3 (Audiencias):** retargeting Schedule-sin-Purchase, ViewContent-sin-Schedule, NoShow; LAL de Purchase/Schedule; exclusión Lost+Purchase.
- **FASE 4 (Optimización):** al acumular ~50 Purchase/sem, cambiar optimización Lead→Purchase + Value-Based Bidding.

---

## 11. Referencias rápidas (IDs / keys / URLs)

- **Webhook worker:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev` · key `7743365e334edde60edadf38dec1ad21`
- **Cron worker:** `https://innovartmedicalips.workers.dev` (⚠️ HTTP 000)
- **Píxeles:** `1642103999710262` (CRM) · `1625645205284016` (web)
- **Token CAPI (custom value):** `{{ custom_values.meta_capi_token }}` = `BhBhR3Hj03iYSAMHcS8L`
- **CF account:** `d85e2b4ba4cdb4d7a59d17621f80eb3c`
- **Workflows CAPI Purchase venta:** Bogotá `b2028df1` · Medellín `2f78cf72` · Barranquilla `5b2fdd06` · Panamá `aa67d560`
- **Workflows CAPI Lead/Financiación:** Lead Bogotá `fd50246d` · Financiación Bogotá `20eb73fb` / Med `c3572764` / Baq `2f258215`
- **Workflow de pase:** `11. Venta-Ganado → Operacion-Programacion` (mueve Ventas→Operaciones)

Relacionado: [[integracion-ghl-meta-capi]] · [[capi-webhook-worker]] · [[flujo-financiacion-bta-capi]] · [[feedback-mcp-ghl-update-page]] · [[crm-funnel]] · [[stack-pauta]]
