---
name: flujo-financiacion-bta-capi
description: Flujo GHL Bogotá para landing de financiación Meddipay (asignación + respuesta WhatsApp + CAPI Purchase) y datos técnicos reutilizables (píxeles, WABA, mecánica CAPI)
metadata:
  type: project
---

# Flujo Financiación BTA — Asignación + Respuesta + CAPI Purchase (2026-06-13)

> ⚠️ **ACTUALIZACIÓN 2026-06-13 (noche):** el paso 7 ya **NO es custom_code** (GHL no puede hacer fetch). Ahora es una acción **Webhook** → worker `innovart-capi-webhook-no-tocar` que hashea PII y manda a Meta. Aplicado y validado en las 3 sedes (Bogotá `20eb73fb`, Medellín `c3572764`, Barranquilla `2f258215`). Ver [[capi-webhook-worker]]. El resto de esta nota describe el flujo original; los pasos 1–6 siguen iguales.

Landing dedicada de financiación de Bogotá → ver [[landing-financiacion-bogota]] · URL pública `https://implantecapilarencolombia.com/financiacionbta` (funnel **FINANCIACIONBTA1** `kNAZ3wagHyMEj6UBqb5H`, página `RSAIRRYLw6yLh6MZfkDd`). NO tiene formulario GHL: es iframe de **Meddipay** + clic a **WhatsApp**. CTA WhatsApp = **573208167253** (4 ocurrencias en la página tras el cambio del 2026-06-13).

## Workflow publicado (sub Bogotá `DgjjDzD9nkCKv8AGF1Qb`)
**`LP Financiación BTA — Asignación + Respuesta + CAPI Purchase`** · ID `20eb73fb-df7d-4fc0-a196-7df581626933` · published, trigger active.

- **Disparador:** `customer_reply` con 2 condiciones → `message.type == 19` (= WhatsApp) **Y** `message.body contains "Meddipay"`. Así NO se dispara con mensajes normales de WhatsApp, solo con el texto pre-cargado del CTA.
- **Pasos (lineales):**
  1. `add_contact_tag`: `ai_parar`, `financiamiento`, `landing_financiacion_bta`
  2. `update_conversation_ai_status` → `status:"inactive"`, `assignedEmployeeId:"keep-same"` (apaga el bot IA para que no confunda al paciente)
  3. `create_opportunity` → pipeline **Ventas** `RpC0O3mYkxyKV1jvMqm6`, etapa **Paciente MeddiPay** `7f727e11-e11b-4975-a91d-f193b0e8b010`, valor `8000000`, `allow_backward:false`, `allow_multiple:false`
  4. `assign_user` → **`only_unassigned_contact:true`** + `user_list:["ajPncm2f7Yvjgle1kZwy"]` (Sofia Forero). Respeta al comercial existente; solo asigna Sofia si está libre.
  5. `send_whatsapp_message` → `from_phone_number:"609046938958518"`, `template_id:"0"` (texto libre, válido por ventana de 24h)
  6. `internal_notification` → `userType:"assign"` (notifica al comercial asignado)
  7. `custom_code` → **Meta CAPI Purchase**
- `allowMultiple:false` (una vez por contacto).
- ⚠ Pendiente de prueba end-to-end: que el paso 5 (WhatsApp texto libre) envíe; si GHL exigiera plantilla, usar `whatsapp_v2` o plantilla aprobada.

## Réplicas por sede (mismo flujo, publicado y activo) — 2026-06-13
Mismo patrón en las 3 sedes. Sofia (`ajPncm2f7Yvjgle1kZwy`) como fallback en todas. Píxeles `1642103999710262`/`1625645205284016` + `{{custom_values.meta_capi_token}}` (compartidos en las 3). Purchase $8.000.000 COP.

| Sede | Workflow ID | Pipeline Ventas | Etapa Paciente MeddiPay | WABA (from_phone_number) | Tag landing |
|---|---|---|---|---|---|
| Bogotá | `20eb73fb-df7d-4fc0-a196-7df581626933` | `RpC0O3mYkxyKV1jvMqm6` | `7f727e11-e11b-4975-a91d-f193b0e8b010` | `609046938958518` | `landing_financiacion_bta` |
| Medellín | `c3572764-06a6-41f1-90c6-69fbb9bc0e69` | `8vqcl7aQIBiR2YiebPv3` | `20df7bef-69fc-479f-b377-e6c1fba8e220` | `611850088685930` | `landing_financiacion_mde` |
| Barranquilla | `2f258215-8c93-454d-a636-42ffcc6cd3bb` | `fJqdW5ZKRTQZ68Dv57Sr` | `47818463-4c4e-4d0f-bcda-ae0dc0798520` | `625405087319822` | `landing_financiacion_baq` |

⚠ La **página** (landing) NO se replica por MCP (ver [[feedback-mcp-ghl-update-page]]); se copia con "Copy to Sub-Account" nativo de GHL y se le cambia el número/​logo por sede. Los workflows quedan "armados" esperando el primer mensaje "Meddipay".

## Datos técnicos reutilizables (GHL Bogotá)
- **Píxeles Meta (CAPI):** `1642103999710262` y `1625645205284016` (se postea a ambos).
- **WABA / from_phone_number (WhatsApp conectado):** `609046938958518`.
- **Token CAPI:** custom value `{{ custom_values.meta_capi_token }}` (`BhBhR3Hj03iYSAMHcS8L`).
- **`message.type == 19` = canal WhatsApp** en triggers `customer_reply`.
- **Apagar IA conversacional:** acción `update_conversation_ai_status` `status:"inactive"` + tag `ai_parar`. (AI employee id activador visto: `xfDdztcpy2UUQmGlO71X`.)
- **Asignación condicional sin if/else:** `assign_user` con `only_unassigned_contact:true`.
- **Mecánica CAPI (patrón CORREGIDO 2026-06-13):** custom_code que hashea PII SHA-256, **`action_source:'system_generated'`** (⚠ NO usar `'crm'` — es inválido, Meta rechaza el evento), `event_id:'ghl_'+cid+'_'+EVENT+'_'+TS`, **`fbc` desde el fbclid real `{{ contact.fb_click_id }}`** con guarda (NO desde `attributions[0].mediumId`, eso era un bug), POST a `graph.facebook.com/v20.0/<pixel>/events`. Purchase lleva `custom_data:{currency:'COP',value:8000000}`; lost_lead sin custom_data. Aplicado y unificado en los 6 flujos CAPI (3 Purchase financiación + 3 `CAPI Frio Stale 45d` lost_lead) de BTA/MDE/BAQ. ⚠ Tras editar por MCP, el custom_code queda "sin testear" → hay que correr Test en UI (ver [[feedback-mcp-ghl-update-page]]). El fbclid solo se llena en landings con formulario (home4); en la de financiación (sin form) el fbc saldrá vacío y matchea por PII. Mismo patrón que [[integracion-ghl-meta-capi]].
- **Sofia Forero** (fallback comercial) = user `ajPncm2f7Yvjgle1kZwy`.

**Why:** este flujo recupera leads de retargeting con aprobación Meddipay y manda el evento de mayor valor (Purchase) a Meta; los IDs de píxeles/WABA y la mecánica se reutilizan en cualquier flujo CAPI/WhatsApp de Bogotá.
**How to apply:** para nuevos flujos de WhatsApp en Bogotá, clonar este patrón (trigger `customer_reply` type 19 + filtro de body, apagar IA con `ai_parar`+`update_conversation_ai_status`, asignación con `only_unassigned_contact`, CAPI por custom_code a los 2 píxeles).

Relacionado: [[landing-financiacion-bogota]] · [[integracion-ghl-meta-capi]] · [[landing-home4-routing]] · [[stack-pauta]] · [[feedback_fbclid_landing_pages]] · [[feedback-mcp-ghl-update-page]]
