---
name: utm-tracking-avance-general
description: Estado de implementación UTM tracking completo por fuente — Innovart Medical IPS
metadata:
  type: project
---

# UTM Tracking — Estado General por Fuente
**Última actualización:** 26 junio 2026

**Por qué:** Los leads llegaban sin UTMs al CRM. No se sabía qué campaña, ciudad o fuente generaba cada lead. EMQ Meta bajo (4.9). Objetivo: tracking 100% por fuente.

---

## ✅ FUENTE 1: Landing — COMPLETADA Y PROBADA EN PRODUCCIÓN (26 jun 2026)

### GHL
- 5 custom fields UTM creados: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`
- IDs en: [[utm-tracking-landing-shopify]]
- Workflow activo: `LANDING - Procesar UTMs y Asignar Lead` (ID: `abcee3aa-0676-40a7-b3f3-9e65430a90b8`)
- Trigger: tag `fuente_landing` → actualiza Lead Source, agrega tags, nota interna

### Shopify theme.pagefly.liquid (tema "Dawn — GEO IA Innovart", ID 181331001645)
- **Script 1** (UTM Capture): en `<head>` después de `<!-- End Google Tag Manager -->` ✅
- **Script 2** (WA + Form): antes de `</body>` ✅ — formato sufijo actualizado 26-jun-2026
- Token GHL: Private Integration "Landing UTM Tracker" en GHL → Settings → Private Integrations
- ⚠️ NO tocar estos bloques en ediciones futuras del tema
- ⚠️ ARCHIVO CORRECTO: `theme.pagefly.liquid` NO `theme.liquid` — la landing usa PageFly

### Formato del sufijo WhatsApp (versión final 26-jun-2026)
- Formato: `[{src_corto}/{medium_corto}]`
- Mappings: `facebook→fb`, `instagram→ig`, `retargeting→rtg`, `paid_social→paid`, `instagram_dm→ig-dm`, `facebook_dm→fb-dm`
- Ejemplo real probado: `utm_source=facebook&utm_medium=retargeting` → mensaje llega con `[fb/rtg]` ✅
- Si no hay UTMs en la URL → no aparece sufijo (tráfico directo)

### Por qué el sufijo importa
- Para leads de WhatsApp de la landing, el sufijo ES el único tracking — no hay llamada API a GHL al hacer clic en WA
- Para leads del formulario → UTMs van automáticamente a GHL vía API (independiente del sufijo)
- Sin sufijo = lead de WA anónimo, sin ciudad ni fuente identificada

### Campañas activas con UTMs en Meta (LANDING DIEGO)
- **Cuenta:** LANDING DIEGO (act_1176352666815422)
- **Campaña:** Tráfico a web RM (Fase 2) (ID: 120243618086010735)
- **5 ads activos:** v2, v3, v4, v5, v6 — Landing Feb 2026
- **UTMs configurados:** `utm_source=facebook&utm_medium=retargeting&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&utm_id={{campaign.id}}`
- ⚠️ Creativos viejos (2025) en la misma cuenta van a la landing SIN UTMs — pendiente actualizar
- **URL de prueba:** `https://www.innovartmedical.com/?utm_source=facebook&utm_medium=retargeting`

### Cómo funciona
- Botones WhatsApp (9): el mensaje pre-llenado incluye `[fb/rtg]` para que el consultor identifique la fuente
- Formulario "Agendar Cita" (`#bcontact-form-483316`): al enviar, crea/actualiza contacto en GHL con teléfono + UTMs directo

---

## ✅ FUENTE 2: DM Instagram — TRACKING BÁSICO ACTIVO + CITY DETECTION EN PRUEBA (act. 2026-06-28)

### Workflow paralelo PUBLICADO
- **"UTM - IG DM Source Tracker"** (ID: `397ac2f1-d195-44ec-bdde-df9786a21e3c`) — PUBLISHED **v7**
- ⚠️ NOTA: El ID `a05e11f3-52f4-47cb-ab46-b94a19074714` del archivo anterior era INCORRECTO
- Trigger: `customer_reply` con `message.type == 18` (Instagram DM)
- Acción 1: setea `utm_source = instagram` (campo `ffBWPx4Qlhxb6D6toNWO`) ✅ CONFIRMADO
- Acción 2: setea `utm_medium = instagram_dm` (campo `46qWfYJubx8IAOhyFlgT`) ✅ CONFIRMADO
- Acción 3: agrega tag `fuente_dm_instagram` ✅ CONFIRMADO
- `allowMultiple: false` — solo se ejecuta UNA VEZ por contacto

### Workflow existente INTACTO
- `3. Recibir msj IG` (ID: `da35ea2a-4fcd-412b-9364-d0c49e278788`) — NO modificado

### 🔑 INSIGHT KEY (2026-06-27) — Los leads de click-to-DM envían ciudad en el mensaje
Todos los leads de anuncios click-to-DM envían exactamente:
```
Quiero una valoración gratuita en [Ciudad] 📍
```
Ciudades detectadas en producción: "Bogotá", "Medellín", "Ciudad de Panamá". Los orgánicos escriben texto libre.

### ⚠️ HALLAZGO CRÍTICO (2026-06-28) — conditionType:contact_reply NO funciona en IF/ELSE
Se intentó evaluar `message.body` directamente en condiciones IF/ELSE usando `conditionType:"contact_reply"` + `conditionSubType:"body"`. **GHL acepta el JSON pero falla silenciosamente en producción** — el bloque IF/ELSE completo no ejecuta, ni rama SÍ ni rama NO. Confirmado con test E2E real. Ver [[referencia-ghl-workflows-mcp]].

### Workaround v7 — ABANDONADO (2026-06-28)
La lógica IF/ELSE sobre `utm_campaign` como campo temporal fue desplegada pero resultó no validada. Se optó por un enfoque más limpio: 5 workflows paralelos con trigger condicional por ciudad.

### ✅ SOLUCIÓN ACTIVA — 5 workflows por ciudad (publicados 2026-06-28)
En lugar de un IF/ELSE complejo, se crearon 5 workflows independientes en CRM Principal. Cada uno se dispara SOLO cuando el mensaje contiene la keyword de esa ciudad (GHL evalúa `message.body` al nivel de trigger, aunque no en IF/ELSE de acciones).

| Workflow | ID | Trigger keyword | utm_term que setea |
|---|---|---|---|
| UTM IG DM — Bogotá | `f3c21f45-9a22-4919-beb9-6ab4480c819c` | "Bogotá" | `bogota` + tag `ciudad_bogota` |
| UTM IG DM — Medellín | `06a7435d-e196-45d7-b35a-62b1d132b6d3` | "Medellín" | `medellin` + tag `ciudad_medellin` |
| UTM IG DM — Barranquilla | `3cae2544-0cd3-4d4f-87bc-6f1ee2905dfe` | "Barranquilla" | `barranquilla` + tag `ciudad_barranquilla` |
| UTM IG DM — Panamá | `186016c6-a456-4c16-a92b-05525906a24b` | "Panamá" | `panama` + tag `ciudad_panama` |
| UTM IG DM — Bucaramanga | `2fc70935-abe4-4f72-9e96-36efbb3ce252` | "Bucaramanga" | `bucaramanga` + tag `ciudad_bucaramanga` |

- Todos en **CRM Principal** (`NPhQTmLOHd6FbDtqLPnG`) — status: **published**
- Trigger: `customer_reply` + condición `message.body contains "[Ciudad]"` evaluada al disparar
- Conviven con Workflow A (`397ac2f1`) que setea utm_source/utm_medium/tag — no se duplican campos

### Lo que sigue faltando
- **Validar en producción** con lead real de DM con ciudad en el texto
- Campaña específica (cuál ad generó el DM) — requiere `ctwa_clid` + Meta Graph API vía N8N

---

## 🟡 FUENTE 3: DM Facebook — TRACKING BÁSICO ACTIVO (2026-06-26)

### Workflow paralelo creado y PUBLICADO
- **"UTM - FB DM Source Tracker"** (ID: `90630621-6e3b-49ac-9c65-416c3a7720ee`) — PUBLISHED
- Trigger: `message.type == 11` (Facebook Messenger DM)
- Acción: setea `utm_source = meta`, `utm_medium = facebook_dm`
- Estrategia: workflow paralelo que corre simultáneo con `2. Recibir msj FB` sin tocarlo

### Workflow existente INTACTO
- `2. Recibir msj FB` (ID: `9cae02ee-b2e8-48ed-9921-dedd5dcb2dba`) — NO modificado

### Lo que sigue faltando (para tracking completo)
- Campaña específica (cuál ad generó el DM) — pendiente N8N + Meta Graph API

---

## ✅ FUENTE 4: Formulario Qikify innovartmedical.com — COMPLETADO Y VERIFICADO E2E (2026-06-28)

### Arquitectura
- JS interceptor en `theme.liquid` (BLOQUE B v3) y `theme.pagefly.liquid` (BLOQUE C)
- Evento: `bcontact:beforeFormSubmitted` (dispara ANTES del AJAX de Qikify)
- POST a Cloudflare Worker ruta `/qikify-lead` (Worker: `innovart-capi-webhook-no-tocar`)
- Worker mapea sede → GHL sub-cuenta correcta, crea contacto con UTMs + fbclid por IDs específicos de cada sub-cuenta
- Tags: `fuente_web_qikify` + `landing_formulariov2`
- Manejo de duplicados: si GHL retorna 400 con contactId, actualiza el contacto existente (PUT)

### Routing por sede (campo dropdown del formulario)
- "Bogotá" → GHL Bogotá (`DgjjDzD9nkCKv8AGF1Qb`) ✅ verificado
- "Medellin" → GHL Medellín (`h8DplQKVE6epDbbj5Kg8`) ✅ verificado
- "Barranquilla" → GHL Barranquilla (`cXH8KbMaAPGzkmf3Z2pP`) ✅ verificado
- "Bucaramanga" → GHL Bucaramanga (`s40Wa8mXYBxlFCieKohO`) ✅ verificado (solo fbclid — faltan campos UTM)
- "Panama" → GHL Panamá (`45SKYgIDgr4Eh6a6JcFz`) ✅ verificado (country=PA auto-detectado)

### Cobertura
- Funciona desde CUALQUIER página de `innovartmedical.com` (main + landings de ciudad)
- Routing por sede elegida en el formulario, no por URL
- N8N reemplazado completamente — sin dependencias externas
- ⚠️ Bucaramanga pendiente: crear campos utm_source/medium/campaign/content en esa sub-cuenta
- Ver detalles completos: [[plan-formulario-qikify-innovartmedical]]

---

## ✅ FUENTE 5: WhatsApp Directo — COMPLETADA (2026-06-28)

### 5 workflows "UTM - WA Directo Tracker" PUBLICADOS (v3)
- **Bogotá** — `ec3d0cbb-f68b-4806-b3de-2a913cbcbafe`
- **Medellín** — `2fe984c3-6ac1-454c-8e6c-8debd3326969`
- **Barranquilla** — `e1c8709e-a55a-4aee-ad18-e1c86376ce35`
- **Bucaramanga** — `d10dcfdc-5d04-4485-b10b-991450141203` (campos UTM creados en esta sesión)
- **Panamá** — `5722994e-4a17-416b-bec4-fa12283d2f48`

### Trigger: `customer_reply` con `message.type == 3` (WhatsApp), `allowMultiple: false`
### Lógica (3 ramas):
- **ctwa_clid presente** → utm_source=facebook, utm_medium=whatsapp_ads, tag `fuente_whatsapp_ads`
- **ctwa_clid vacío + utm_source con valor** → tag `fuente_whatsapp_landing`
- **ambos vacíos** → utm_source=directo, utm_medium=whatsapp_organico, tag `fuente_whatsapp_directo`

### Pendiente: prueba E2E por sede (Paso 4 del BRIEF)

---

## ⏳ FUENTE 5: Typeform — PENDIENTE

- Typeform conectado a GHL (verificar integración existente)
- Falta: mapear campos UTM en el Typeform → custom fields GHL

---

## ⏳ FUENTE 6: Lead Forms Meta — PENDIENTE

- Formularios nativos de Meta (Facebook/Instagram Lead Ads)
- Workflow existente: `Recibir Lead forms de Facebook` (publicado)
- Falta: agregar UTMs y asignación por ciudad

---

## 📊 Resumen de Estado

| Fuente | GHL Custom Fields | Workflow | JS/Código | Estado |
|--------|------------------|----------|-----------|--------|
| Landing WA + Form (implantecapilarencolombia.com) | ✅ | ✅ publicado | ✅ Shopify | **COMPLETA** |
| DM Instagram | ✅ (mismos campos) | ✅ paralelo publicado v3 | N/A | **COMPLETO** (source+medium+tag) |
| DM Facebook | ✅ (mismos campos) | ✅ paralelo publicado | N/A | **BÁSICO** (fuente+medio) |
| Formulario Qikify (innovartmedical.com) | ✅ (mismos campos) | N/A | ✅ Shopify + CF Worker | **COMPLETA** (routing 5 sedes + UTMs + fbclid) |
| WhatsApp Directo | ✅ (mismos campos) | ✅ 5 workflows publicados | N/A | **COMPLETA** |
| Typeform | ✅ (mismos campos) | ⏳ verificar | ❌ mapear | PENDIENTE |
| Lead Forms Meta | ✅ (mismos campos) | ⏳ auditar | N/A | PENDIENTE |

---

## Próximos pasos (orden recomendado)
1. DM Instagram + DM Facebook (workflows ya existen, solo auditar y enriquecer)
2. Lead Forms Meta (workflow existe)
3. WhatsApp Directo (requiere crear workflows nuevos)
4. Typeform (depende de integración existente)

**How to apply:** Al retomar este trabajo, cargar este archivo primero para saber exactamente dónde se quedó y qué fuente sigue.
