---
name: capi-webhook-worker
description: Worker Cloudflare dedicado (innovart-capi-webhook-no-tocar) que recibe el Webhook de GHL, hashea PII y manda a Meta CAPI. Reemplaza el custom_code de GHL que no puede hacer fetch.
metadata:
  type: project
---

# Worker CAPI vía Webhook — `innovart-capi-webhook-no-tocar` (2026-06-13)

**Por qué existe:** el `custom_code` de GHL NO puede hacer `fetch` (sandbox sin red) → no se puede mandar CAPI desde ahí (ver [[feedback-mcp-ghl-update-page]]). Solución: acción **Webhook** nativa de GHL → este worker, que sí puede llamar a Meta.

## Worker
- **Nombre:** `innovart-capi-webhook-no-tocar` (Cloudflare, cuenta `Innovartmedicalips@gmail.com`, acc `d85e2b4ba4cdb4d7a59d17621f80eb3c`).
- **URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev`
- **Código fuente local:** `/Users/javierforero/innovart-capi-webhook-no-tocar/` (`src/index.js` + `wrangler.toml`).
- **Deploy:** `cd` a la carpeta y `CLOUDFLARE_API_TOKEN=<token> wrangler deploy`. Token de API se crea en dash.cloudflare.com/profile/api-tokens (plantilla "Edit Cloudflare Workers").
- **Secrets:** `META_CAPI_TOKEN` (token de Meta, el mismo del diagnóstico/custom_value) + `WEBHOOK_KEY` = `7743365e334edde60edadf38dec1ad21` (clave compartida, va en `?k=`).
- **Píxeles:** postea a los 2 (`1642103999710262`, `1625645205284016`) por defecto. `action_source: system_generated`. `event_id` = `{contactId}_{event}_{floor(ts/300)}` (dedup 5min, igual que el cron worker).
- Independiente del worker del cron `innovart-meta-capi` (NO lo toca). Ver [[integracion-ghl-meta-capi]].

## Cómo se conecta GHL (acción Webhook)
- Acción tipo `webhook` con `attributes: {url, method:"POST"}`. **SÍ se persiste por MCP** (`update_workflow_actions`) y **NO exige "test" en la UI** (a diferencia del custom_code) → ejecuta directo.
- **Config del evento va en el query string de la URL** (no en el body):
  `…/?k=<KEY>&event=Purchase&value=8000000&currency=COP` (opcional `&country=CO&pixels=ID,ID&test=<code>&debug=1`).
- **El PII lo saca del body nativo de GHL.** Formato validado (2026-06-13) que GHL manda: `contact_id, first_name, last_name, full_name, email, phone, country, tags, location{}, user{}, workflow{}, customData{}`. ⚠ Los **custom fields (fbclid, etc.) NO vienen** por defecto (`customData:{}` vacío) — habría que agregarlos como "custom data" en la acción Webhook si se quieren. El worker ya lee `customData.fbclid` por si se agrega.
- **Claves de match logradas** sin custom data: `em, ph, fn, ln, country, external_id` (6 → EMQ alto). En financiación el fbclid va vacío igual (landing sin form).
- `debug=1` → el worker devuelve el body recibido sin mandar a Meta (para inspeccionar).

## Workflows que ya lo usan (paso "CAPI Meta Webhook (NO TOCAR)")
- **Financiación Purchase ($8M COP):** Bogotá `20eb73fb` · Medellín `c3572764` · Barranquilla `2f258215`. (Reemplazaron el custom_code roto.)
- **Lead — Bogotá Ads (DgjjDzD9):** workflow `CAPI Lead WhatsApp/Ads Bogota (NO TOCAR)` `fd50246d-3b6b-40ba-9fb5-97f7d9f5a66e`, trigger **`contact_created`** (todo contacto nuevo, sin condiciones) → webhook `event=Lead`. Publicado 2026-06-13. **Cierra el hueco grande:** los ~25K leads de WhatsApp FB/IG ads caen en DgjjDzD9, que NO está en el cron → no mandaban Lead. Validado: events_received:1 en ambos píxeles, match por `ph,fn,ln,country,external_id` (estos leads solo traen tel+nombre).

## Cobertura CAPI por sede (auditoría 2026-06-13, leyendo el código real del cron)
- **Cron `innovart-meta-capi`** cubre 5 sedes (Bucaramanga, Medellín, Panamá, Barranquilla, IPS Principal/NPhQ): Lead por contacto nuevo + funnel por etapa. **NO cubre DgjjDzD9 (Bogotá Ads)**.
- **DgjjDzD9 (25,627 contactos, intake principal de WhatsApp FB/IG ads):** ahora tiene **Lead** (webhook nuevo) + **Purchase financiación** (webhook). ⚠ Aún SIN funnel (Contact/Schedule/ViewContent/NoShow/Purchase-Ganado) si el lead avanza dentro de DgjjDzD9.

## Pendiente / decisiones
- **ctwa_clid NO se captura** en DgjjDzD9 (no existe el campo) → los leads de WhatsApp matchean por teléfono+nombre, no por click del anuncio. Mejorar = cambio a nivel de la integración applevel (pasar el referral ctwa_clid a un campo). Proyecto aparte.
- **Funnel de DgjjDzD9:** decidir si los leads avanzan dentro de DgjjDzD9 (→ faltan webhooks de etapa o meter DgjjDzD9 al cron con un PIT) o si se mueven a una sede cubierta (→ ya cubierto).
- Los demás flujos CAPI por custom_code (Panamá 8 eventos, `CAPI Frio Stale 45d` lost_lead ×varias) **nunca funcionaron** y la mayoría son **redundantes con el cron**. Opción: borrar el custom_code roto, o reconstruir como webhook solo los únicos.
- El cron manda a 1 píxel (1642); los webhooks a 2.

**Why:** es la única forma de mandar CAPI en tiempo real desde un evento de GHL (el custom_code no puede). Centraliza el hasheo + envío en un solo punto → si cambia el mapeo de campos, se arregla 1 vez en el worker, no en N workflows.
**How to apply:** para un nuevo evento CAPI desde GHL, agrega una acción Webhook (por MCP: `type:"webhook"`, `attributes:{url,method:"POST"}`) con la URL del worker + `&event=<Nombre>&value=<n>&currency=<X>`. Nada más.

## Referencias técnicas (validadas por MCP, 2026-06-13)
- **Trigger de contacto nuevo:** `type:"contact_created"`, `masterType:"highlevel"`, `conditions:[]` (todo contacto). Flujo: `create_workflow` (queda draft) → `update_workflow_actions` (triggers+actions) → `publish_workflow`. La acción `webhook` **NO exige test** (a diferencia del custom_code) → ejecuta directo al publicar.
- ⚠ Al reenviar acciones por `update_workflow_actions`, el paso `update_conversation_ai_status` necesita `workflowsActionType:"INTERNAL"` + `attributes.__customInputs__:{}` o da "corrupted type".
- **Body nativo que manda GHL al webhook:** `contact_id, first_name, last_name, full_name, email, phone, country, tags, location{}, user{}, workflow{}, customData{}` (custom fields NO vienen salvo que se agreguen como customData).
- **Campos custom DgjjDzD9** (para customData si se quiere subir match): fb_click_id `1hdDWOfia3IljwbLwqNC` (`{{contact.fb_click_id}}`) · fbclid `DnKbVMv2xH3kNEksDV5h` · fbp `xqGgBJ8iteGTBGOzRYeY` · Lead Event ID `PeFjDIT5Bcaca0mpCNe7`. **NO existe campo ctwa_clid.**

Relacionado: [[integracion-ghl-meta-capi]] · [[flujo-financiacion-bta-capi]] · [[feedback-mcp-ghl-update-page]] · [[feedback-whatsapp-applevel-sms]]
