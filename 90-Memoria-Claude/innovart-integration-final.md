---
name: Integración Final Innovart — Versionado + Protocolos
description: Documento único y autoritativo de versionado actual, tracking setup, y protocolo E2E para cualquier desarrollo en Innovart Medical IPS
metadata:
  type: reference
  updated: 2026-06-30
  criticality: P0
---

# Integración Final Innovart — Versionado + Protocolos

**ÚLTIMA ACTUALIZACIÓN:** 2026-06-30
**ESTADO:** Completo y verificado E2E

Este documento es la **VERDAD ÚNICA** para desarrollo en Innovart Medical IPS. Lee completamente antes de cualquier cambio de código, landing o tracking.

---

## TABLA RÁPIDA: Versionado Actual

| Componente | Versión | Última Actualización | Cambio Principal | Status |
|---|---|---|---|---|
| theme.pagefly.liquid | V3 | 2026-06-30 | Script Qikify + `</body>` | ✅ Live |
| theme.liquid | V2 | 2026-06-27 | Schema + tracking scripts | ✅ Live |
| Workers CAPI | V4 | 2026-06-29 | SubmitApplication filter | ✅ Live |
| Workers WhatsApp | V2 | 2026-06-29 | ctwa_clid mapping | ✅ Live |
| Landing /home | V1 | 2026-06-23 | fbclid + router | ✅ Live |
| GHL Workflows | 4.1 | 2026-06-29 | SMS/WA al lead habilitado | ✅ Live |

**Acceso a versionado histórico:** [[versionado-theme-pagefly-liquid.md]] · [[protocolo-versionado-codigo-critico.md]]

---

## 1. FBCLID CAPTURE PROTOCOL (CRÍTICO)

### Dónde se captura

**Landing /home (main):**
- Archivo: `headTrackingCode` en GHL funnel
- Campo GHL: `FYVJpTGSmAPhiqoRwm97` (fb_click_id)
- Script: URLSearchParams captura `fbclid` de URL
- Validación: `typeof fbclid === 'string' && fbclid.length > 0`

**Landings de Ciudad (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá):**
- Ubicación: PageFly (ciudad) o GemPages (Panamá)
- Script: Inyectado en `theme.pagefly.liquid` v3 (línea XXX) o en theme.gempages.blank.liquid
- Campo: Mismo `FYVJpTGSmAPhiqoRwm97`

### Cómo se valida

1. **En JavaScript (cliente):**
   ```javascript
   const fbclid = new URLSearchParams(window.location.search).get('fbclid');
   console.log('fbclid capturado:', fbclid);
   if (fbclid && fbclid.length > 0) {
     // Enviar a form/GHL
   }
   ```

2. **En GHL:**
   - Buscar contacto por email/teléfono
   - Verificar campo `fb_click_id` poblado
   - Auditoría: 600+ eventos/mes con fbclid (2026-06-29)

3. **En Meta (CAPI):**
   - Eventos llevan `fbc` (Facebook Cookie) hasheado
   - Verificar `events_received` en Meta Ads Manager → Eventos

### Cuándo se dispara

- **Landing entrante:** Meta Ads (con parámetro `fbclid` en URL)
- **IG DM click-to-DM:** Meta pasa fbclid automáticamente
- **WhatsApp Ads:** No lleva fbclid (Click-to-Message NO soporta fbclid) → usar `ctwa_clid` en su lugar

**REFERENCIA:** [[auditoria-fbclid-critica-2026-06-22.md]] · [[fbclid-home-implementacion-exitosa-2026-06-22.md]]

---

## 2. CAPI WEBHOOK FILTER (SEGURIDAD)

### Worker Cloudflare

**URL:** `innovart-capi-webhook-no-tocar` (dominio Cloudflare activo)

**Función:** Bloquea eventos defectuosos antes de llegar a Meta

**Flujo:**
```
GHL Webhook Trigger (Purchase/Lead/Schedule)
  ↓
Worker recibe payload
  ↓
Valida:
  - ¿Tiene fbclid O fbp?
  - ¿Tiene email O teléfono?
  - ¿NO es SubmitApplication sin PII?
  ↓
Si PASA: Hashea email/teléfono → envía a Meta CAPI
Si FALLA: Log + descarta (evita ruido)
```

### Secrets en Cloudflare

6 variables almacenadas (NO compartir públicamente):

| Variable | Propósito |
|---|---|
| META_PIXEL_1 | Pixel Shopify (termina en **62**) |
| META_PIXEL_2 | Pixel GHL (HOME4/HOME5) |
| META_CAPI_TOKEN | Token de acceso Meta |
| GHL_LOCATION_ID | Ubicación GHL principal |
| CLOUDFLARE_AUTH | Auth header |
| WEBHOOK_KEY | Key de validación GHL → Worker |

**Verificación:** `curl -H "Authorization: Bearer $WEBHOOK_KEY" https://innovart-capi-webhook-no-tocar/health`

**REFERENCIA:** [[capi-webhook-worker.md]] · [[filtro-capi-submitapplication-2026-06-22.md]]

---

## 3. QIKIFY WINDOW.BCONTACT LOADING

### Script URL

```html
<script src="https://www.qikify.com/app/qikify.min.js"></script>
```

### Ubicación de instalación

**theme.pagefly.liquid V3:**
- Línea: Antes del `</body>`
- Razón: Qikify inicializa `window.BContact` al cargar
- Validación: Ejecutar en consola: `typeof window.BContact` = `"object"`

**theme.gempages.blank.liquid (Panamá):**
- Ubicación: Antes de `</body>`
- Mismo script + validación

### Por qué es crítico

SIN el script:
- `window.BContact` = undefined
- Formularios NO disparan POST al Worker
- Leads se pierden completamente

CON el script:
- `window.BContact.submit()` funciona
- Formulario → Qikify → MutationObserver → Worker → GHL
- Leads capturados 100%

### Validación E2E post-deploy

1. Abrir landing en navegador
2. Inspeccionar console: `typeof window.BContact` → debe ser `"object"`
3. Llenar form + click Enviar
4. Verificar en GHL dentro de 30s: contacto creado con tag `fuente_web_qikify`

**REFERENCIA:** [[qikify-formulario-estructura-html-2026-06-29.md]] · [[paso-a-paso-arreglo-formularios-2026-06-30.md]]

---

## 4. CTWA_CLID WHATSAPP TRACKING

### Field ID en GHL

- **Field ID:** (extraer de GHL Custom Fields, guardar aquí)
- **Nombre:** `ctwa_clid` o `click_to_whatsapp_id`
- **Tipo:** Text/String

### Flujo automático

```
Meta Ads (Click-to-Message)
  ↓
Meta webhook → innovart-wa-redirect-320 (Cloudflare Worker)
  ↓
Worker recibe: ctwa_clid + utm_source + utm_medium
  ↓
Fan-out a innovart-capi-webhook-no-tocar/wa-ctwa
  ↓
Guarda en GHL:
  - ctwa_clid = field
  - utm_source = "whatsapp"
  - utm_medium = "click_to_message"
  ↓
Workflow 4.1: "Recibir lead de Landing_formulario"
  - Tag: fuente_web_qikify + landing_formulariov2 + oportunidad ventas frio
  - SMS/WA al lead: habilitado en 4 sedes
```

### Números de teléfono por sede

| Sede | Línea SMS (LeadConnector) | Línea WhatsApp API (Meta CTWA) |
|---|---|---|
| Bogotá | 573171224974 (Medellín) | +57 310 / 317 / 313 |
| Medellín | 573171224974 (Medellín) | +57 310 / 317 / 313 |
| Barranquilla | 573171224974 (Medellín) | +57 310 / 317 / 313 |
| Bucaramanga | 573171224974 (Medellín) | +57 310 / 317 / 313 |
| Panamá | +507 650 XXXX | +507 650 XXXX |

**REFERENCIA:** [[lineas-innovart-sms-whatsapp-api-estructura.md]] · [[ctwa-tracking-whatsapp-ads.md]]

---

## 5. UTM TRACKING STANDARDS

### Patrón obligatorio

Todo anuncio Meta/Google DEBE llevar:

```
utm_source=meta                    // o "google"
utm_medium=cpc                     // o "display", "social"
utm_campaign=NOMBRE_CAMPAÑA        // exacto de Meta Ads Manager
utm_content=NOMBRE_AD_SET          // nombre ad set
utm_term=CIUDAD                    // "bogota" / "medellin" / "barranquilla" / "bucaramanga" / "panama"
```

### Ejemplo real

```
https://innovartmedical.com/implante-capilar-bogota?
  utm_source=meta
  &utm_medium=cpc
  &utm_campaign=Trafico_Web_RM_Fase2
  &utm_content=FUE_Hero_Video
  &utm_term=bogota
```

### Implementación por canal

**Meta Ads (API):**
- Aplicar vía `url_tags` en anuncio
- Función: `metodo-carga-utms-api-meta.md` (script Python)
- Herramienta: `meta-dajf` MCP

**Google Ads:**
- Parámetros de rastreo en nivel campaña
- URL final = base + {final_url_suffix}

**Landing (Shopify):**
- Scripts en theme.liquid + capturan en JavaScript
- Field GHL: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`

### Estado actual (2026-06-30)

- Landing ✅ completa (fbclid + UTM capturados)
- Meta Ads: 176 activos, 5% con UTMs (en progreso)
- Google Ads: 0% con UTMs (P0 roadmap)

**REFERENCIA:** [[utm-tracking-avance-general.md]] · [[metodo-carga-utms-api-meta.md]]

---

## 6. SEGURIDAD Y RESTRICCIONES

### Código prohibido en landing

```javascript
// ❌ NUNCA hacer:
window.location = 'https://...?fbclid=' + fbclid  // Pierde tracking en flujos
if (meta_pixel) document.write()  // Destruye DOM
eval(utm_params)  // XSS
localStorage.setItem('fbclid', fbclid)  // No persiste entre dominios
```

### Código correcto

```javascript
// ✅ SIEMPRE hacer:
const params = new URLSearchParams(window.location.search);
const fbclid = params.get('fbclid');
// Pasar a form hidden input o GHL API
fetch('https://backend.leadconnectorhq.com/...', {
  method: 'POST',
  body: JSON.stringify({ fb_click_id: fbclid, ... })
})
```

### Router + Workflow en lugar de redirects

- **NO:** `window.location = 'https://...?fbclid=...'` (pierde fbclid)
- **SÍ:** Usar router GHL `fbd5387a` → asigna tag + dispara workflow 4.1

**REFERENCIA:** [[referencia-tecnica-shopify-pagefly-whatsapp-tracking.md]]

---

## 7. E2E TEST PROTOCOL (POST-DEPLOY)

### Checklist validación

Después de CUALQUIER cambio en código/landing/tracking, ejecutar:

1. **Conexión `/mcp`**
   ```bash
   curl -X POST https://backend.leadconnectorhq.com/... \
     -H "Authorization: Bearer $GHL_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"test": "connectivity"}' \
     # Esperar 200 OK
   ```

2. **Verificación técnica (5 min)**
   - [ ] Pixel Meta dispara (DevTools Network → `t.facebook.com/tr`)
   - [ ] fbclid capturado (Console: `typeof window.BContact` = "object")
   - [ ] Router activo (contacto creado con tag correcto en GHL)
   - [ ] Workflow 4.1 publicado (GHL: estado = "Published")

3. **Test E2E (10 min)**
   - [ ] Ir a landing con **parámetro fbclid simulado:** `?fbclid=abc123def456`
   - [ ] Llenar form + click Enviar
   - [ ] Verificar en GHL:
     - Contacto creado en < 30s
     - Campo `fb_click_id` = `abc123def456`
     - Tag `landing_form_home` asignado
     - Workflow 4.1 disparó (SMS/WA encolado)

4. **Monitoreo (30 min)**
   - [ ] Meta Events Manager: evento Lead registrado
   - [ ] GHL: contacto visible en panel
   - [ ] Cloudflare logs: 0 errores (200 OK)

### Tiempo máximo antes de rollback: **1 hora**

Si algo falla después de 1h en producción → ejecutar [[rollback-guide.md]]

**REFERENCIA:** [[protocolo-validacion-landing-automatica.md]]

---

## 8. ESTRUCTURA DE ARCHIVOS VERSIONADO

Todos los cambios en código crítico se guardan AQUÍ con changelog:

```
/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/
├── versionado-theme-pagefly-liquid.md  (V1→V3)
├── versionado-theme-liquid.md          (V1→V2)
├── versionado-workers-capi.md          (implícito en [[capi-webhook-worker.md]])
├── protocolo-versionado-codigo-critico.md
└── innovart-integration-final.md        (este archivo)
```

### Qué guardar en cada versión

```yaml
---
version: "V3"
date: "2026-06-30"
component: "theme.pagefly.liquid"
changes:
  - "Agregado script Qikify `https://www.qikify.com/app/qikify.min.js`"
  - "Razón: window.BContact no existía, formularios no disparaban POST"
  - "Verificación: typeof window.BContact = 'object'"
---
```

---

## 9. REGLAS ABSOLUTAS (NO ROMPER)

### Sedes reales (NUNCA inventar)

```
✅ Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá
❌ Cali (NUNCA, no existe)
```

### Cuentas Meta ≠ sedes

```
Nombres de cuenta: BGTA, MEDELLIN, QUILLA, PANAMA, LANDING DIEGO, INTERACCION REDES DIEGO
Geografía real: Detectar por nombre campaña + destino + ruteo CRM
❌ NUNCA asumir "MEDELLIN" = solo Medellín
```

### Shopify y GHL siempre en ESPAÑOL

- Menús, pasos, nombres de campos → todo en español
- GHL workflows, tags, planes → español
- Instrucciones a Javier → español

### PageFly es el editor, NO GemPages

- Landings de ciudad (4 sedes): PageFly
- Panamá: GemPages (pero úsalo como referencia, editar en su interfaz)
- HOME: 100% PageFly (V3)

### Nunca ofrecer MCP para cambios en PRODUCCIÓN

- Lectura por MCP: ✅ OK
- Cambios de código en live → pasos manuales solamente
- Cambios en Shopify admin/GHL: ✅ OK por API

---

## 10. REFERENCIAS CRUZADAS EN OBSIDIAN

**Lee antes de cualquier desarrollo:**
- [[protocolo-versionado-codigo-critico.md]] — Cómo documentar cambios
- [[versionado-theme-pagefly-liquid.md]] — Historial V1→V3
- [[tracking-setup-completa-2026-06-23.md]] — Setup tracking integral
- [[auditoria-fbclid-critica-2026-06-22.md]] — Root cause fbclid

**Para troubleshooting:**
- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking.md]] — Por qué falla tracking
- [[paso-a-paso-arreglo-formularios-2026-06-30.md]] — Fix formularios (último estado)
- [[protocolo-validacion-landing-automatica.md]] — Validación post-deploy

**Para rollback:**
- [[rollback-guide.md]] — Cómo revertir cambios en 30 min

---

## CONTACTOS Y ESCALADA

| Rol | Persona | Correo |
|---|---|---|
| Media Buyer | Esneider | esneidervc17@gmail.com |
| CTO Tracking | (Javier/Claude) | — |
| Director Médico | Dr. Fabián Carreño | — |

**Escalada P0:** Contactar a Esneider directamente si hay pérdida de leads > 1h.

---

**ÚLTIMA VERIFICACIÓN:** 2026-06-30 ✅
**ESTADO:** Live en producción, 5 sedes, 0 errores conocidos
**PRÓXIMA REVISIÓN:** 2026-07-07
