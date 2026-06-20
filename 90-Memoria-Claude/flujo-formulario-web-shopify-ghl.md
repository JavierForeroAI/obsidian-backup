---
name: flujo-formulario-web-shopify-ghl
description: El formulario /pages/contact de la web (Shopify nativo) no llegaba al CRM; flujo GHL + motor Ventas/Frio para conectarlo
metadata: 
  node_type: memory
  type: project
  originSessionId: 9c6a236f-2d91-4059-bb1b-2c2d280a4304
---

2026-06-19. **Problema:** el formulario de `innovartmedical.com/pages/contact` es el **formulario NATIVO de Shopify** (plantilla `templates/page.contact.json` → sección `type: "contact-form"`). Solo manda email a `innovartmedicalips@gmail.com`; **nunca toca GHL**. No estaba roto: nunca estuvo conectado. Fix = reemplazar por HTML propio que haga POST a un webhook entrante de GHL (un iframe no sirve: no captura `ctwa_clid`). El MCP de Shopify NO escribe el theme LIVE → el embed se pega a mano en una sección Custom Liquid.

**Flujo GHL (cuenta Principal `NPhQTmLOHd6FbDtqLPnG`):** `Web - Formulario Contacto Shopify (landing_formulario_web)` ID **`4bd84e2f-4925-415c-ab01-01f9ce450c87`**, trigger **inbound_webhook** (payload espera `fbclid`, `ctwa_clid`, `comment`, `page_url` + nombre/email/phone). Hoy solo: tag `landing_formulario_web` + guarda fb_click_id (`wy6FYlxKsMDvtXljeC9O`) / fbclid crudo (`ROjbROGU9919xi7GR9rO`) / ctwa_clid (`pmfzBxCFdjeojgCLmEWu`) + nota. **NO crea oportunidad.**

**Motor del CRM (clave):** crear una oportunidad en pipeline **Ventas (`ZUMTSA6dbzMnXFlOBGzi`) / etapa Frio (`dd4a2ec5-816a-4cd9-8748-0b40516e04c8`)** dispara solo el workflow **`Etiqueta Frio` (`401a3b8b-...`)** → tag `oportunidad ventas frio` + CAPI Lead a 2 píxeles (`1642103999710262`/`1625645205284016`). Así que el flujo web solo necesita **crear la oportunidad en Ventas/Frio** y el resto del motor (etiquetas, CAPI, ruteo, asignación) se engancha. Pipeline `GENERAL` (`5uJNzSwMdJJisHsoC6EB`) tiene etapas por sede (Bogota/Barranquilla/Panama/Medellin) para ruteo.

**Prueba E2E 2026-06-19 (✅):** contacto Javier Forero (`pUw0OCg3vxvjXAFdf3nD`, `francisco2javierforero@gmail.com`/`+573002181681`) creado simulando el form → oportunidad `tTX51AxOTg9RG5PgacNv` en Ventas/Frio → el motor auto-agregó `oportunidad ventas frio`. Cadena confirmada: form → contacto → oportunidad → motor.

**Webhook URL confirmada (HTTP 200):** `https://services.leadconnectorhq.com/hooks/NPhQTmLOHd6FbDtqLPnG/webhook-trigger/1BHgVzcPhgiOWGjChdcp` (patrón `/hooks/{locationId}/webhook-trigger/{triggerId}`; NO sale por MCP, la dio Javier desde el builder).

**Nodo crear-oportunidad RESUELTO (2026-06-19, workflow v4):** el tipo correcto es **`create_opportunity`** con campos PLANOS en attributes: `{"type":"create_opportunity","pipeline_id":"...","pipeline_stage_id":"...","opportunity_name":"{{contact.name}}","opportunity_source":"...","monetary_value":"","fields":[]}`. NO es `internal_update_opportunity` ni `__customInputFields__` (eso rechazaba). Forma copiada de `12. Recepción leads_typeform VIEJO` (`d50346c3`). Agregado al flujo + validate `ok`. Tocar solo `actions` (omitir `triggers`) en `update_workflow_actions` preserva el trigger y la URL.

**WEBHOOK DESCARTADO:** probado 2 veces — el trigger **inbound_webhook de GHL NO crea el contacto** (POST da 200 pero no crea nada; el panel del trigger solo tiene "Mapping Reference" para variables, no mapeo a contacto; los Lead_capture/Lead_api de la cuenta también dependen de una integración externa que crea el contacto antes). No hay acción "crear contacto" en workflows.

**SOLUCIÓN FINAL (2026-06-19, workflow v6) — Formulario nativo GHL:** form **`Contacto Web Innovart`** (`X4zQ4jv8SNtap08XU1rs`) creado por API (`create_form` + `update_form` con `formData.form.fields`, campos standard `first_name/last_name/phone/email/city` + submit). Un form GHL **crea el contacto solo** (por diseño). Workflow `4bd84e2f` **reconectado**: trigger cambiado de inbound_webhook → **`form_submission`** (cond `form.id is-any-of [X4zQ4jv8SNtap08XU1rs]`); acciones limpiadas a: tag `landing_formulario_web` → nota → **`create_opportunity` Ventas/Frio**. `validate_workflow` OK (3 refs). Form vivo HTTP 200 en `https://api.leadconnectorhq.com/widget/form/X4zQ4jv8SNtap08XU1rs`. Embed iframe + `link.msgsndr.com/js/form_embed.js`.

**Receta GHL form por API:** `create_form` da base vacía; `update_form` EXIGE pasar `name` explícito la 1ª vez; campos standard mapean al contacto por su `tag`. Submit por curl lo bloquea Cloudflare (403) → probar desde navegador.

**Campos ocultos AÑADIDOS (2026-06-19, vía `update_form`):** 2 hidden fields → `fbclid` (hiddenFieldQueryKey `fbclid`) mapeado a fb_click_id (`wy6FYlxKsMDvtXljeC9O`) y `ctwa_clid` (query key `ctwa_clid`) a ctwa_clid (`pmfzBxCFdjeojgCLmEWu`). Shape que GHL acepta y NO normaliza: `{id, model:"contact", label, name, fieldKey, dataType:"TEXT", type:"text", typeLabel:"Text", tag, placeholder:"", required:false, standard:false, hidden:true, hiddenFieldQueryKey, fieldWidthPercentage:100}`. Al enviar, el form guarda el fbclid solo en el contacto; el embed debe **inyectar `?fbclid=`** (preferir cookie `_fbc`; si no, armar `fb.1.<ts>.<fbclid>` para que sirva a CAPI).

**Embed final (dinámico):** JS que lee `_fbc`/`?fbclid` y construye el iframe `https://api.leadconnectorhq.com/widget/form/X4zQ4jv8SNtap08XU1rs?fbclid=...` + `link.msgsndr.com/js/form_embed.js`.

**✅ COMPLETADO Y EN VIVO (2026-06-19):** Javier pegó el embed dinámico en `/pages/contact` (sección **Liquid personalizado**) y **ocultó** la sección **Formulario de contacto** nativa, desde **Personalizar** (el MCP de Shopify NO edita el theme LIVE; pasos en español por [[feedback-idioma-espanol-ghl]]). **Prueba E2E real OK:** envío con `?fbclid=TEST123` → contacto `KtA329a5JgVzOPf2o3pQ` (source `Contacto Web Innovart`, createdBy FORM) + custom field **fb_click_id = `fb.1.1781909674078.TEST123`** (el embed convierte fbclid→formato CAPI `fb.1.<ts>.<fbclid>`) + tags `landing_formulario_web` y `oportunidad ventas frio` + oportunidad `aiVepAyOzxGYyDc5M8It` en Ventas/Frío. Cadena web→contacto→fbclid→tag→oportunidad→motor→CAPI confirmada de punta a punta.

**Limpieza HECHA (2026-06-19):** contactos de prueba borrados (`KtA329a5JgVzOPf2o3pQ` eliminado; `pUw0OCg3vxvjXAFdf3nD` ya no existía). Sin pendientes — proyecto cerrado.

Relacionado: [[referencia-ghl-cuentas-innovart]], [[feedback_fbclid_landing_pages]], [[auditoria-capimetaghl-base]], [[referencia-ghl-workflows-mcp]], [[shopify-ecosistema-mcp]].
