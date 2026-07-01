---
name: E2E Validation Checklist
description: Validación integral después de cambios en landings, tracking, workflows y CRM
metadata:
  type: checklist
  category: testing
  last_updated: 2026-06-30
  applies_to: landings, forms, tracking, workflows, CRM
---

# E2E Validation Checklist — Post-Deploy

**Cuándo usar:** Después de cualquier cambio en landing, form, script de tracking, workflow o CRM.
**Duración:** 15–30 min según cambios.
**Owner:** Javier / Esneider / Dev Team

---

## 1. LANDING PAGE — Accesibilidad y Renderizado

### Desktop (Chrome)
- [ ] **Home** (`innovartmedical.com/home`) carga sin errores
  - [ ] Inspeccionar console (`F12 → Console`): CERO errores rojos
  - [ ] Red tab: CERO requests fallidas (status 4xx/5xx)
  - [ ] Performance: Largest Contentful Paint (LCP) < 2.5s
- [ ] **Sedes** (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá) cargan
  - [ ] `/bogota` → H1 correcto, hero loads, form visible
  - [ ] `/medellin` → idem
  - [ ] `/barranquilla` → idem
  - [ ] `/bucaramanga` → idem
  - [ ] `/panama` → idem
- [ ] **Botones WhatsApp** funcionan
  - [ ] Click en CTA → abre WhatsApp Web con prefijo correcto (`Quiero una valoración gratuita` o equivalente)
  - [ ] Mismo teléfono por sede (ej: +57 310... Medellín)

### Mobile (iPhone / Android Chrome)
- [ ] Home carga en móvil sin layout breaking
  - [ ] Scroll fluido, sin saltos
  - [ ] Hero image responsive (no crop roto)
  - [ ] Sticky bar visible (88px reservado)
  - [ ] Form no oculto bajo fold (scroll <30% para acceder)
- [ ] Botones WA clickeables en móvil (target area >44×44px)
- [ ] Video hero (si aplica) NOT autoplay 🔊 en móvil (respeta mute)

---

## 2. FORMULARIOS — Captura y Envío

### Form Rendering
- [ ] Form aparece en página (`<div contactform-embed="[ID]"></div>`)
  - [ ] IDs correctos por sede (PageFly + GemPages Panamá)
  - [ ] Sin "Formulario no disponible" o mensajes de error
- [ ] Campos visibles y accesibles
  - [ ] Nombre (`type="text"`)
  - [ ] Teléfono (`type="tel"` o `type="number"`)
  - [ ] Email (si aplica, usualmente OCULTO en WhatsApp directo)
  - [ ] Botón Enviar no gris/deshabilitado

### Form Submission
- [ ] **Click en "Enviar"** → Request POST se dispara
  - [ ] DevTools Network tab: POST a `innovart-capi-webhook-no-tocar.workers.dev` o equivalente
  - [ ] Status 200 (OK)
  - [ ] **CRÍTICO:** Si POST NO aparece → revisar [[paso-a-paso-arreglo-formularios-2026-06-30]]
- [ ] **GHL recibe contacto** (validar en GHL admin)
  - [ ] Login GHL → Búsqueda por email o teléfono
  - [ ] Tags correctos: `fuente_web_qikify` + `landing_formulario` + `oportunidad_ventas_frio`
  - [ ] Oportunidad creada en pipeline **Ventas → Frío**
  - [ ] UTM fields poblados (si se capturan por URL)

### Error Handling
- [ ] Form validation (campos obligatorios)
  - [ ] Intentar enviar sin nombre → mensaje de error (no POST silencioso)
  - [ ] Intentar enviar teléfono inválido (ej: 123) → error o accept
  - [ ] Intentar enviar sin teléfono → error (requerido)
- [ ] Mensaje post-envío
  - [ ] "Gracias, nos contactaremos pronto" (o equivalente)
  - [ ] Form se limpian o deshabilita (no reenvío duplicado)

---

## 3. TRACKING — fbclid, UTM, Pixel

### fbclid Capture
- [ ] Landing recibe `fbclid` en URL
  - [ ] DevTools → Application → Cookies: verificar `_fbc` cookie
  - [ ] Script captura y guarda en custom field GHL `fbclid_capture`
  - [ ] Comando console: `console.log(localStorage.getItem('fbclid'))` → devuelve valor (no `null`)
- [ ] GHL contacto tiene `fbclid`
  - [ ] Abrir contacto en GHL → Custom Fields → `fbclid_capture` contiene ID (ej: `fb.1.xxx`)

### UTM Tracking
- [ ] URL landing contiene UTMs (de Meta ad)
  - [ ] Ejemplo: `/home?utm_source=meta&utm_medium=cpc&utm_campaign=leads_bogota&utm_content=imagen_1`
  - [ ] Console: `new URLSearchParams(window.location.search).get('utm_source')` → `"meta"` (no null)
- [ ] GHL campos poblados
  - [ ] `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` visibles en contacto GHL
  - [ ] Reporte: filtrar por `utm_source=meta` → X contactos (debe haber)

### Pixel Firing
- [ ] Meta Pixel dispara
  - [ ] DevTools → Network → Search `facebook` o `connect.facebook`
  - [ ] Request POST a `graph.facebook.com` con `ev=PageView` u otro evento
  - [ ] Status 200
- [ ] CAPI Event (si aplica)
  - [ ] Network → buscar POST a `innovart-capi-webhook` → Status 200
  - [ ] Payload contiene `user_data` (email, phone, fbclid)

### Google Ads Conversion (si aplica)
- [ ] gtag.js cargado
  - [ ] Console: `typeof gtag === "function"` → `true`
  - [ ] Network: `google-analytics.com/g/collect` requests (GA4)

---

## 4. WORKFLOWS — Disparo y Acciones

### GHL Workflow Activation
- [ ] Workflow **4.1 Recibir lead de Landing** (o equivalente) dispara
  - [ ] GHL contacto recibe automáticamente:
    - [ ] **SMS 0-5 min:** "Hola [Nombre]..." (en línea SMS LeadConnector)
    - [ ] **WhatsApp 5-15 min:** "Hola, gracias por tu interés..."
    - [ ] **Tags + Task:** `lead_recibido`, `contactado`
- [ ] **Condición por ciudad** funciona (si applica)
  - [ ] Test Bogotá → tag `ciudad_bogota` se asigna
  - [ ] Test Medellín → tag `ciudad_medellin` se asigna
  - [ ] (Validar con ContactID en GHL UI)

### Email Sequence (si aplica)
- [ ] Email 1 llega en bandeja (check spam)
  - [ ] De: `noreply@gohighlevel.com` o sender correcto
  - [ ] Subject: "Tu evaluación gratuita de implante capilar" (o similar)
  - [ ] Links clickeables + tracking UTM

---

## 5. WHATSAPP — Captura e Integración

### WhatsApp Button Click
- [ ] Click en botón WA (`href="https://wa.me/57..."`)
  - [ ] Desktop → abre WhatsApp Web o redirecciona a app
  - [ ] Mobile → abre WhatsApp app con conversación prefillada
  - [ ] Mensaje pre-escrito visible en chat (ej: "Quiero una valoración")
- [ ] **CTWA Tracking** (si es Meta Click-to-Message ad)
  - [ ] URL contiene `ctwa_clid=[ID]`
  - [ ] GHL captura `ctwa_clid` custom field
  - [ ] Webhook `innovart-wa-redirect-320` dispara (logs en Cloudflare)

### WhatsApp API Message Incoming
- [ ] Mensaje llega a línea WA (ej: +57 310...)
  - [ ] GHL recibe como Conversation automáticamente
  - [ ] Contact asignado correctamente por teléfono
  - [ ] Workflow de respuesta automática activa (ej: "Hola, gracias por escribir...")

---

## 6. CRM — Datos Íntegros

### Contact Creation
- [ ] Contacto existe en GHL
  - [ ] Email poblado (si capturado)
  - [ ] Teléfono poblado y formateado (+57 XXXX...)
  - [ ] Nombre poblado
- [ ] **Custom Fields** completados
  - [ ] `fbclid_capture`: tiene valor o vacío (si no se capturó)
  - [ ] `utm_source`, `utm_medium`, `utm_campaign`: tienen valores o vacío
  - [ ] `date_created`: timestamp correcto
  - [ ] `oportunidad_ventas_frio`: status **Nuevo** o **Frío**

### Opportunity Creation
- [ ] Oportunidad aparece en pipeline **Ventas → Frío**
  - [ ] Nombre: "Consulta — [Nombre Contacto]" (o template correcto)
  - [ ] Value (presupuesto): "$0" o monto default (no NULL)
  - [ ] Date created: hoy (no histórico)
  - [ ] Status: **Nuevo** (no Cerrado)
- [ ] Pipeline flow respetado
  - [ ] Siguiente etapa al actualizar status (ej: Nuevo → Seguimiento)

### Email Verification (EMQ Score)
- [ ] EMQ (Email Match Quality) score visible
  - [ ] GHL Ads Manager → Audiences → EMQ
  - [ ] Target: >5.0 (hoy ~4.9, objetivo 5.5+)
  - [ ] Validar después de N contactos (48h para actualizar)

---

## 7. SECURITY — Anti-XSS, Anti-Injection

### Input Validation
- [ ] Form **NO acepta HTML/JS directo**
  - [ ] Intentar: `<script>alert(1)</script>` en campo Nombre → se guarda como texto (no ejecuta)
  - [ ] GHL muestra: `&lt;script&gt;alert(1)&lt;/script&gt;` o similar (encoded)
- [ ] URL parámetros NO ejecutados
  - [ ] Intentar: `?utm_source="><script>alert(1)</script>` → no aparece alerta

### CAPI Event Validation
- [ ] CAPI payload validado (filtro Cloudflare)
  - [ ] Evento sin `fbclid`/`fbp` → rechazado (logs: "Missing fbclid/fbp")
  - [ ] Evento sin PII (email/phone) → rechazado (logs: "Missing PII")
  - [ ] **Esto previene ruido de eventos fantasma**

### Cookie Security
- [ ] `_fbc` cookie tiene flags correctos
  - [ ] SameSite: Lax (no Strict para Meta tracking)
  - [ ] Secure: true (HTTPS)
  - [ ] HttpOnly: false (JS debe leer para guardar en custom field)

---

## 8. PERFORMANCE — Carga y Renderizado

### Page Load Time
- [ ] LCP (Largest Contentful Paint) < 2.5s
- [ ] FID (First Input Delay) < 100ms
- [ ] CLS (Cumulative Layout Shift) < 0.1
  - [ ] **Cómo medir:** DevTools → Lighthouse → Run audit

### Script Overhead
- [ ] Qikify (`qikify.min.js`) carga: Network tab, <100ms
- [ ] Form rendering: <500ms después de Qikify
- [ ] CAPI event: POST dispatch <1s (no bloquea form)

### Bundle Size
- [ ] Hero image: <250KB (WebP preferred, JPEG fallback)
- [ ] Theme CSS: <100KB combined
- [ ] Third-party scripts: <500KB total (Qikify, Pixel, GA4, Clarity)

---

## 9. BROWSER COMPATIBILITY

- [ ] **Chrome (v120+):** ✅ Funcionan todos (testing principal)
- [ ] **Safari (iOS 15+):** 
  - [ ] Form activo (Qikify compatible)
  - [ ] WhatsApp button abre app
  - [ ] Pixel dispara (sin restricción de ITP por ahora)
- [ ] **Firefox (v121+):** ✅ Funciona
- [ ] **Samsung Internet:** ✅ WhatsApp activo

---

## 10. REGRESSION — Cambios No Afecten Existente

- [ ] **Home page funciona igual** (no regresión de cambios de otra sede)
- [ ] **Otros workflows en GHL no rompidos** (ej: workflow de email marketing)
- [ ] **Reporting Meta** sigue capturando conversiones (fbclid no se perdió)
- [ ] **Líneas SMS/WA** siguen activas (no deshabilitadas)

---

## Quick Checklist (5 min)

Use esto si solo hiciste un cambio pequeño:

- [ ] Form POST dispara (Network tab)
- [ ] GHL recibe contacto (búsqueda por email)
- [ ] Tags correctos (`fuente_web_qikify` presente)
- [ ] WhatsApp button funciona
- [ ] Console sin errores rojos

---

## Testing en Paralelo (Multi-Ambiente)

| Ambiente | URL | Login | Notas |
|---|---|---|---|
| **GHL Bogotá (Main)** | https://gohighlevel.com | innovartmedicalips@gmail.com | 6 subcuentas aquí |
| **Meta Ads (Dev)** | Business Manager | same | Test ad con landing |
| **Shopify** | https://admin.shopify.com/store/implantecapilarencolombia | same | Theme edits |
| **Cloudflare** | https://dash.cloudflare.com | cloudflare account | Workers logs |

---

## Documentación de Referencia

- [[paso-a-paso-arreglo-formularios-2026-06-30]] — Si forms NO disparan POST
- [[flujo-crm-qikify-verificado-2026-06-29]] — Integración GHL confirmada
- [[protocolo-validacion-landing-automatica]] — Proceso automático (14 pasos)
- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]] — Deep dive técnico
