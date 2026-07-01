---
name: Security Audit Checklist
description: Auditoría de seguridad — XSS, injection, CSRF, autenticación, datos sensibles
metadata:
  type: checklist
  category: security
  last_updated: 2026-06-30
  applies_to: landings, forms, CRM, tracking, APIs
---

# Security Audit Checklist — XSS, Injection, CSRF, Auth, Data

**Cuándo usar:** Antes de publicar landing nueva, después de cambios en scripts tracking, antes de release a producción.
**Duración:** 20–45 min según cambios.
**Owner:** Javier / Tech Lead / QA

---

## 1. INPUT VALIDATION — Anti-XSS, Anti-Injection

### Form Fields
- [ ] **Nombre** (text input)
  - [ ] Intentar: `<script>alert('XSS')</script>` → NO ejecuta en página
  - [ ] GHL guarda como **texto limpio** (encoded: `&lt;script&gt;...&lt;/script&gt;`)
  - [ ] Console: no errores SyntaxError
- [ ] **Teléfono** (tel/number input)
  - [ ] Intentar: `+57 310 1234567 <img src=x onerror=alert(1)>` → se rechaza o escapa
  - [ ] Validación: solo dígitos + símbolos permitidos (`+`, espacio, `-`)
  - [ ] Formato GHL: `+57310...` (sin espacios en DB)
- [ ] **Email** (si aplica)
  - [ ] Intentar: `test@test.com<script>alert(1)</script>` → no válido (regex valida email)
  - [ ] RFC5322 compliance (si usa validación estricta)
  - [ ] Protección contra: `"test@test.com" onload="alert(1)"` (no válido como email)

### URL Parameters
- [ ] **UTM Parameters** (utm_source, utm_medium, utm_campaign, utm_content)
  - [ ] Intentar: `?utm_source="><script>alert(1)</script>` → no ejecuta
  - [ ] Script captura con `URLSearchParams` (safe)
  - [ ] Se guarda en custom field GHL (verificar encode en DB)
  - [ ] Reporte no renderiza raw HTML (ej: GHL dashboard escapa)
- [ ] **fbclid Parameter**
  - [ ] Intentar: `?fbclid=<img src=x onerror=alert(1)>` → se rechaza (patrón regex `fb.1.xxx`)
  - [ ] Validación: solo alphanuméricas + punto (no caracteres especiales)
  - [ ] Se guarda como string literal (no ejecutable)
- [ ] **Otros params (city, locale, etc.)**
  - [ ] Whitelist conocidos: aceptar solo valores esperados
  - [ ] Intentar: `?city=../../etc/passwd` → no accede a paths (frontend, no backend)
  - [ ] No se usa en `eval()` o `innerHTML` directo

### Form POST Payload
- [ ] **CAPI Event Validation** (en Worker Cloudflare)
  - [ ] Payload sin `fbclid` → rechazado (status 400)
  - [ ] Payload sin PII → rechazado (status 400)
  - [ ] Logs: "/innovart-capi-webhook-no-tocar?payload=filtered" (no leaks de datos)
  - [ ] **Filtro funciona:** bloquea `SubmitApplication` sin evento anterior
- [ ] **Form Serialization**
  - [ ] Datos NO contienen caracteres null (`\0`)
  - [ ] Content-Type: `application/json` o `application/x-www-form-urlencoded` (correcto header)
  - [ ] No múltiples POST simultáneos (CSRF token ausente, pero POST single-endpoint mitiga)

---

## 2. AUTHENTICATION & AUTHORIZATION

### GHL Access
- [ ] **GHL Login** usa OAuth o credenciales fuertes
  - [ ] Account email: `innovartmedicalips@gmail.com` ✅
  - [ ] 2FA habilitado (si disponible en GHL)
  - [ ] Sesiones activas: revisar "Connected Devices" (no logins sospechosos)
  - [ ] IP última: debe ser conocida (ej: Javier en Colombia, no China)
- [ ] **GHL API Keys** (Custom Integrations)
  - [ ] Token "Landing UTM Tracker" limitado a scopes necesarios (no full access)
  - [ ] Almacenado en GHL, no hardcodeado en tema Shopify
  - [ ] Rotación: cada 6 meses o si expuesto
- [ ] **GHL Subcuentas** (Bogotá, Medellín, etc.)
  - [ ] Acceso restringido por rol (ej: Esneider = Traffic Manager, Javier = Admin)
  - [ ] No compartir credenciales (SSO preferido)

### Meta Ads API
- [ ] **Access Token** (`meta-dajf` app)
  - [ ] Stored: Cloudflare secret (no en código)
  - [ ] Scope: `ads_read`, `ads_management`, `catalog_management` (verificar en App Roles)
  - [ ] Expiración: sin expiración (long-lived token) ✅
  - [ ] NO en git commits (`.gitignore` incluye `*.env` y `secrets.json`)
- [ ] **App Permissions**
  - [ ] App ID: `1698932398019234` (Claude Code app, verificado)
  - [ ] Business Account Owner: Javier (o delegado)
  - [ ] Revisar: "Roles" → solo Javier/Esneider tienen Business Admin

### Google Ads API
- [ ] **OAuth Credentials** (`~/google-ads.yaml`)
  - [ ] Type: Desktop OAuth (no service account, más seguro)
  - [ ] Client ID/Secret: en `~/google-ads.yaml` (no en repo)
  - [ ] Refresh token: rotado regularmente
  - [ ] MCC Account: `2084232674` (verificar es correcta)
  - [ ] ⚠️ NOTA: client_secret vio chat → regenerar en Google Cloud Console ASAP
- [ ] **Access Level**
  - [ ] Standard Access: NO (negado, pero no se necesita)
  - [ ] Basic Access: SÍ (basta para lectura + cambios campañas)

### Shopify API
- [ ] **Theme Edits** (PageFly/GemPages)
  - [ ] Acceso vía Shopify admin dashboard (OAuth, no token directo)
  - [ ] Account: `implantecapilarencolombia.myshopify.com`
  - [ ] Admin Staff: Javier + Esneider
  - [ ] Activity Log: revisar cambios recientes (theme edits)
- [ ] **Custom Apps** (si aplica)
  - [ ] Scope: `write_pages` + `read_products` (no more)
  - [ ] Instalado: 0 apps custom (PageFly/GemPages no custom app, son embeds)

### Cloudflare Workers
- [ ] **Worker Secrets** (Cloudflare dashboard)
  - [ ] `CAPI_ACCESS_TOKEN`: guardado en Cloudflare Secret Storage (no visible en logs)
  - [ ] `GHL_API_KEY`: ídem
  - [ ] `GHL_CONTACT_ID` (si usada): ídem
  - [ ] Acceso: solo Javier admin en dash.cloudflare.com
- [ ] **Worker Routes** (CORS, Rate Limiting)
  - [ ] `/innovart-capi-webhook-no-tocar/*` → rate limit 100 req/min (DDoS protection)
  - [ ] CORS: `Origin: innovartmedical.com` + `*.shopify.com` (whitelist)
  - [ ] POST solo (GET rechazado con 405)

---

## 3. CSRF & IDEMPOTENCY

### CSRF Tokens (si aplica)
- [ ] Form tiene **CSRF token** (POST a GHL/CAPI)
  - [ ] Token único por sesión + por-form
  - [ ] Token validado en backend antes de procesar
  - [ ] **Si NO hay token:** verificar SameSite cookie (SameSite=Lax mitiga)
- [ ] **Forma actual (Innovart):**
  - [ ] No hay token explícito (Qikify form + Worker backend)
  - [ ] Mitigation: `SameSite=Lax` en cookies + origin validation en Worker
  - [ ] POST al mismo dominio/subdomain (no cross-domain)

### Idempotency
- [ ] **Doble POST prevención**
  - [ ] Form se deshabilita post-submit (JavaScript)
  - [ ] Botón "Enviar" gris/disabled por 2-3s
  - [ ] Si usuario hace doble-click: solo 1 POST se dispara
  - [ ] **Test:** DevTools Network → Disable cache → Double-click "Enviar" → CERO requests duplicadas
- [ ] **GHL Duplicate Prevention**
  - [ ] Búsqueda por email: no crea 2 contactos si email dup
  - [ ] Workflow 4.1: no envía SMS 2× al mismo contacto (estado checked)

---

## 4. DATA PROTECTION — PII, Encriptación

### Sensitive Data in Transit
- [ ] **HTTPS Enforced**
  - [ ] URL: `https://innovartmedical.com` (no http://)
  - [ ] Certificate: valid, not self-signed
  - [ ] DevTools → Security tab: "Secure"
  - [ ] Shopify admin: automatically HTTPS ✅
  - [ ] GHL API: HTTPS ✅
  - [ ] Meta API: HTTPS ✅
  - [ ] Cloudflare Worker: HTTPS ✅
- [ ] **TLS Version**
  - [ ] Mínimo: TLS 1.2 (mejor 1.3)
  - [ ] DevTools → Security → "Secure connection" → TLS 1.3 (ideal)
- [ ] **Form Data Encryption**
  - [ ] Email/phone/fbclid enviados en POST body (no URL query)
  - [ ] Body encriptado por TLS (no visible en sniffer)
  - [ ] NO en localStorage visible (localStorage no encriptado localmente, pero HTTPS protege)

### Sensitive Data at Rest
- [ ] **GHL Database**
  - [ ] Email, teléfono, fbclid: almacenados encrypted (GHL responsibility)
  - [ ] Acceso: login + 2FA (si disponible)
  - [ ] Auditoría: GHL Activity Log activo
- [ ] **Cloudflare Worker Logs**
  - [ ] Logs NO contienen payload completo (filtrados con `payload=filtered`)
  - [ ] Verificar: `innovart-capi-webhook-no-tocar` logs en dashboard
  - [ ] Retención: 30 días (estándar Cloudflare)
- [ ] **Shopify Theme Code**
  - [ ] Scripts de tracking: NO hardcodean tokens/keys
  - [ ] Theme liquid: usa variables dinámicas (ej: `{{ ghl_token }}` si externalizado)
  - [ ] NO credentials en commits: `.gitignore` activo

### PII Minimization
- [ ] **Form recoge mínimo requerido**
  - [ ] Nombre: requerido ✅
  - [ ] Teléfono: requerido ✅
  - [ ] Email: **¿requerido?** (análisis pendiente en [[hallazgo-leads-sin-email-bgta-2026-06-23]])
  - [ ] Dirección: NO recogida (buen signo)
  - [ ] SSN/ID: NO recogida ✅
- [ ] **Retención**
  - [ ] GHL: retiene indefinido (política interna GHL)
  - [ ] GDPR: si EU users, debe haber "derecho a olvido" (compliance framework)
  - [ ] Colombia LSCA: similar a GDPR, revisar cumplimiento

---

## 5. COOKIES & LOCAL STORAGE

### Cookie Security
- [ ] **Meta Cookie (`_fbc`)**
  - [ ] Flags: `SameSite=Lax; Secure; HttpOnly=false`
  - [ ] Duración: 90 días (Meta estándar)
  - [ ] Almacena: fbclid
  - [ ] Verificar: DevTools → Application → Cookies → `_fbc` visible
- [ ] **Session Cookie (si aplica)**
  - [ ] Flags: `SameSite=Lax; Secure; HttpOnly=true` (best practice)
  - [ ] Duración: 30 min (no persistir sesión larga)
  - [ ] **Si NO hay session cookie:** verificar que no se requiere (stateless API OK)
- [ ] **Google Cookie (`_ga`)**
  - [ ] Flags: Secure; SameSite=Lax
  - [ ] Contenido: anonymous (no PII)
- [ ] **Microsoft Clarity (`_clid`)**
  - [ ] Flags: Secure; SameSite=Lax
  - [ ] Contenido: session ID (no PII)
- [ ] **Otros cookies** (audit completo)
  - [ ] Inventario: listar todos en landing
  - [ ] Cada uno: purpose, duration, PII? (crear tabla si muchos)

### Local Storage
- [ ] **fbclid almacenado (script captura)**
  - [ ] Ubicación: `localStorage.fbclid` o similar
  - [ ] Contenido: `fb.1.xxx` (no otras PII)
  - [ ] Limpieza: se borra si se hace hard-refresh o 30+ días inactividad
  - [ ] ⚠️ localStorage NO encriptado localmente (TLS protege en tránsito)
- [ ] **UTM parámetros**
  - [ ] Si se guardan en localStorage: junto con fbclid
  - [ ] Contenido: `utm_source=meta` etc. (no PII)
  - [ ] Limpieza: idem fbclid
- [ ] **Auditar:** DevTools → Application → Local Storage → innovartmedical.com
  - [ ] ¿Qué hay guardado?
  - [ ] ¿Contiene PII? (NO debe)
  - [ ] ¿Expiración clara? (NO indefinido)

---

## 6. API SECURITY — Rate Limiting, Validation

### Cloudflare Worker Endpoint
- [ ] **URL:** `https://innovart-capi-webhook-no-tocar.workers.dev`
  - [ ] Método: POST only (GET/PUT rechazadas)
  - [ ] Status 405 si GET/PUT/DELETE
- [ ] **Rate Limiting**
  - [ ] Límite: 100 req/min por IP
  - [ ] Exceeds: respuesta 429 (Too Many Requests)
  - [ ] Test: script que envía 101 POST rápido → esperado 429 en último
- [ ] **Input Validation**
  - [ ] `event_name` debe estar en whitelist (ej: `Contact`, `Schedule`)
  - [ ] `user_data` validado (no nulls, no injections)
  - [ ] Tamaño payload: max 10KB (DDoS prevention)
  - [ ] Test: enviar payload >10KB → rechazado
- [ ] **Output Sanitization**
  - [ ] Response NO contiene datos sensibles (no echo de payload)
  - [ ] Ejemplo: `{"status": "ok"}` (no `{"received": {...payload...}}`)
  - [ ] Logs truncados (ver punkt anterior)

### GHL API (via Custom Integration)
- [ ] **Endpoint Security**
  - [ ] Token en header: `Authorization: Bearer <token>` (no query param)
  - [ ] Token rotado cada 6 meses
  - [ ] Scope limitado: `crm/contact.write`, `crm/contact.read` (no full)
- [ ] **Payload Validation (incoming)**
  - [ ] Contact email: regex validated
  - [ ] Phone: format `+57...` o similar (país-específico)
  - [ ] Custom fields: IDs verificados (no arbitrary field names)
  - [ ] Tags: whitelist (ej: `fuente_web_qikify` existente en GHL)
- [ ] **Error Handling**
  - [ ] 400: Invalid input (ej: email malformado)
  - [ ] 401: Token expired/invalid
  - [ ] 429: Rate limit exceeded
  - [ ] 500: Server error (retry logic con backoff)

### Meta CAPI Endpoint
- [ ] **Token Freshness**
  - [ ] Token NO expirado (long-lived, pero revisar cada 3 meses)
  - [ ] Test: llamar CAPI → respuesta 200 (no 401)
- [ ] **Event Validation (before sending)**
  - [ ] `event_name`: en enum (`Purchase`, `Contact`, `Schedule`)
  - [ ] `user_data`: tiene al menos 1 PII (email, phone, fbclid, fbp)
  - [ ] `event_id`: UUID único (prevent duplicates)
  - [ ] `timestamp`: within 24h (histórico rechazado)
- [ ] **Response Handling**
  - [ ] 200: success → log `event_id`
  - [ ] 400: validation error → log + alert (ej: fbclid inválido)
  - [ ] 401: token error → rotate token ASAP
  - [ ] 429: rate limit → backoff exponencial (1s, 2s, 4s...)

---

## 7. XSS PREVENTION — Context-Specific Encoding

### HTML Context (page rendering)
- [ ] **Template escaping**
  - [ ] Nombres contacto: escapados (no `innerHTML`, sí `.textContent`)
  - [ ] UTM params en reportes: escapados
  - [ ] Testimonios: HTML puro (si incluidos) → sanitize con DOMPurify (opcional)
- [ ] **Developer console test**
  - [ ] Ir a GHL contacto con nombre `<img src=x onerror=alert(1)>`
  - [ ] Verificar: aparece como `&lt;img...&gt;` (escapado), NO executa script

### JavaScript Context (var/event handlers)
- [ ] **Variables en JS**
  - [ ] `const utm_source = "{{ utm_source }}"` → si contiene `">"` debe escaparse
  - [ ] Use: `JSON.stringify()` + parse, o usar template strings con validación
  - [ ] Test: `utm_source = '";alert(1);//'` → no ejecuta (variable string safe)
- [ ] **Event Handlers**
  - [ ] NO usar: `<a href="javascript:...">` (deprecado)
  - [ ] NO usar: `onclick="...constructor.call()"` (obfuscated JS)
  - [ ] SÍ usar: `addEventListener()` (safe, separado de HTML)

### URL Context (links, redirects)
- [ ] **WhatsApp links**
  - [ ] `href="https://wa.me/57..."`
  - [ ] NO: `href="javascript:..."` (safe, uses https)
  - [ ] Validar: URL scheme es `https://` (no `data:` o `blob:`)
- [ ] **Tracking redirects**
  - [ ] Si hay redirect (ej: shortlink): validar destino whitelist
  - [ ] Test: intentar `utm_source=https://attacker.com` → no se usa en redirect

### CSS Context (style injection)
- [ ] **Inline styles**
  - [ ] NO: `style="{{ user_input }}"`
  - [ ] SÍ: `style="color: {{ sanitize_color(user_input) }}"`
  - [ ] Validar: color es hex/rgb/hsl (no expressions)
- [ ] **Class injection**
  - [ ] `class="{{ user_class }}"` → whitelist classes (no arbitrary)
  - [ ] Test: `user_class = "x y z" onclick="alert(1)"` → rechazado

---

## 8. EXTERNAL SCRIPTS — Third-Party Risk

### Meta Pixel
- [ ] **Script URL:** `https://connect.facebook.net/en_US/fbevents.js`
  - [ ] Origem: Meta oficial (no typosquatting)
  - [ ] Integrity: si SRI (Subresource Integrity) available
  - [ ] Load: async + defer (no bloquea render)
- [ ] **Config**
  - [ ] Pixel ID: `1642103999710262` (correcto para Shopify)
  - [ ] eventos: PageView, ViewContent (no custom sin validar)
  - [ ] CAPI token: NO en cliente (server-side solo)
- [ ] **Permissions**
  - [ ] Pixel NO pide ubicación/cámara/micrófono
  - [ ] Cookies NO afectan compliance (Meta responsable de GDPR)

### Qikify (Form Embedding)
- [ ] **Script URL:** `https://www.qikify.com/app/qikify.min.js`
  - [ ] Origen: Qikify oficial (verify HTTPS cert)
  - [ ] Integrity: check script hash (si cambios sospechosos)
  - [ ] Load: async + after DOM ready
- [ ] **Form Embedding**
  - [ ] `<div contactform-embed="483316"></div>` (ID correcto)
  - [ ] NO data leak: form POST va directo a Qikify → Worker GHL (no Qikify cloud retiene)
  - [ ] Form source: Qikify dashboard (verificar form config, no malware)
- [ ] **Permissions**
  - [ ] Form NO pide datos beyond nombre/teléfono/email
  - [ ] Qikify TOS: revisar si datos van a terceros

### Google Analytics 4 (GA4)
- [ ] **Script URL:** `https://www.googletagmanager.com/gtag/js?id=G-XXXXX`
  - [ ] ID: debe ser correcto (Google propiedad)
  - [ ] Integrity: no cambios sin Google
  - [ ] Load: async
- [ ] **Config**
  - [ ] Events tracked: PageView, ViewContent, form_submit
  - [ ] NO PII enviado: email/phone NO a GA4 (enviar a GHL/Meta solo)
  - [ ] Anonymization: IP masking enabled

### Microsoft Clarity
- [ ] **Script URL:** `https://www.clarity.ms/tag/[PROJECT_ID]`
  - [ ] Project ID: verificado en Clarity dashboard
  - [ ] Integrity: no cambios
  - [ ] Load: async
- [ ] **Tracking**
  - [ ] Heatmaps: anónimos (no vinculan a usuario real)
  - [ ] Session replay: anónimo (PII oculto)
  - [ ] NO cookies PII
- [ ] **Permissions**
  - [ ] Privacy OK: no ropa/finanzas/salud mencionadas en recordings

---

## 9. ACCESS CONTROL — Team Permissions

### Shopify
- [ ] **Admin Users**
  - [ ] Listar en Shopify admin → Settings → Users & permissions
  - [ ] Javier: Full access ✅
  - [ ] Esneider: Theme/Product edit (no billing) ✅
  - [ ] Others: verificar roles (no acceso innecesario)
- [ ] **Theme Editor**
  - [ ] PageFly: acceso vía Shopify login (no separate credenciales)
  - [ ] GemPages: idem
  - [ ] Change log: revisar edits recientes (audit trail)

### GHL
- [ ] **Admin Accounts**
  - [ ] Owner: Javier
  - [ ] Admins: Esneider + Tech Lead (si aplica)
  - [ ] Otros roles: Marketer, Specialist (lectura solo)
- [ ] **API Keys**
  - [ ] Custom Integrations: listar
  - [ ] "Landing UTM Tracker" → verificar scope (no full access)
  - [ ] Rotación: cada 6 meses
- [ ] **Subcuentas**
  - [ ] Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá
  - [ ] Acceso: Javier (all), Esneider (traffic), Diego (landing pages)
  - [ ] No compartir credenciales entre sedes

### Meta Ads
- [ ] **Business Account**
  - [ ] Owner: Javier
  - [ ] Admin: Esneider + Tech
  - [ ] Role access: 6 Ad Accounts (BGTA, QUILLA, PANAMA, MEDELLIN, etc.)
- [ ] **App Roles**
  - [ ] App "CLAUDE CODE DA-JF" → Business Admin role
  - [ ] Access token: stored en Cloudflare, no en code

### Google Ads
- [ ] **MCC (Manager Account)**
  - [ ] Owner: Javier
  - [ ] Standard Access: NO (negado, OK)
  - [ ] Basic Access: SÍ (Diego o delegate)
  - [ ] Activity log: revisar cambios recientes

### Cloudflare
- [ ] **Account**
  - [ ] Owner: Javier
  - [ ] Admins: Tech Lead (si aplica)
  - [ ] Billing: Javier (2FA enabled)
- [ ] **Worker Secrets**
  - [ ] Acceso: Admin solo (no read in UI, encrypted)
  - [ ] Audit: activity log activo

---

## 10. INCIDENT RESPONSE & LOGGING

### Log Monitoring
- [ ] **Cloudflare Worker Logs**
  - [ ] Dashboard → Analytics → check errors daily
  - [ ] Alert on: 5xx errors, rate limit exceeds (429), auth failures (401)
  - [ ] Búsqueda: `payload=filtered` (veri que PII está masked)
- [ ] **GHL Activity Log**
  - [ ] Dashboard → Integrations → Activity log visible
  - [ ] Alert on: API token rotations, contact bulk deletes, workflow changes
- [ ] **Meta Ads Manager**
  - [ ] Change log: revisar cambios no autorizados
  - [ ] Alert: campaigns pausadas, budget changes
- [ ] **Shopify Admin**
  - [ ] Timeline: revisar cambios theme
  - [ ] Alert: staff account changes, API access

### Breach Response Plan
- [ ] **If API Token Exposed:**
  - [ ] Paso 1: Rotate token immediately (GHL, Meta, Google)
  - [ ] Paso 2: Review logs desde fecha exposición (buscar acceso malicioso)
  - [ ] Paso 3: Notificar equipo (Javier, Esneider)
  - [ ] Paso 4: Update documentation (MEMORY.md) con fecha rotación
- [ ] **If XSS/Injection Detectada:**
  - [ ] Paso 1: Take landing offline (set `robots: noindex`)
  - [ ] Paso 2: Identificar causa (form input, external script, etc.)
  - [ ] Paso 3: Fix + test en staging
  - [ ] Paso 4: Redeploy + verify
  - [ ] Paso 5: Root cause analysis + document
- [ ] **If Credential Leak:**
  - [ ] Paso 1: Revoke compromised credential
  - [ ] Paso 2: Change master password (Google Account, Shopify account)
  - [ ] Paso 3: Enable 2FA (si no activo)
  - [ ] Paso 4: Review recent logins (anomalías)

---

## Quick Checklist (10 min)

Use para cambios menores:

- [ ] Form NO ejecuta `<script>alert(1)</script>` (input testing)
- [ ] API token NO en git commits (`.gitignore` verificado)
- [ ] HTTPS en todas las URLs (DevTools → Security)
- [ ] Cookies tienen `Secure` flag (DevTools → Cookies)
- [ ] POST no echo sensitive data (Worker response sanitizado)
- [ ] 2FA en accounts críticos (Shopify, GHL, Meta, Google)
- [ ] Script terceros de origen conocido (no typosquatting)

---

## Compliance Checklist (si aplica)

### GDPR (EU users)
- [ ] Privacy policy menciona: cookies, tracking, retention
- [ ] Consent banner: (aunque CLI Colombia no lo requiere, best practice)
- [ ] Data deletion: policy + mechanism (request → GHL delete)
- [ ] DPA: si procesar datos UE → Data Processing Agreement con GHL

### Colombia LSCA (Ley Estatutaria)
- [ ] Política privacidad en español
- [ ] Consentimiento explícito (habitual WhatsApp directo, pero form mejor)
- [ ] No venta de datos a terceros (verificado: Meta, GHL, Google no venden Innovart data)
- [ ] Derecho a saber/acceder/eliminar/actualizar

### Shopify Terms
- [ ] Plugins usados (PageFly, GemPages) tienen ToS claros
- [ ] No violan Shopify App Store policy (tracking OK, ads OK)
- [ ] PCI compliance: no guardar tarjeta (Shopify lo maneja) ✅

---

## Testing Scripts

### Test XSS Payloads
```javascript
// En console de landing, intentar en form:
// Test 1: Script en nombre
"<script>alert('XSS')</script>"

// Test 2: Event handler en teléfono
"<img src=x onerror=alert(1)>"

// Test 3: URL parameter
?utm_source="><script>alert(1)</script>
?fbclid=<img src=x onerror=alert(1)>

// Test 4: localStorage injection
localStorage.fbclid = "test'; alert('XSS'); //";
```

### Test CSRF
```javascript
// Simular POST desde otro sitio:
// 1. Abrir landing en tab
// 2. Abrir otra URL (ej: google.com) en otra tab
// 3. Desde console en Google:
fetch('https://innovartmedical.com/webhook', {
  method: 'POST',
  body: JSON.stringify({...fake_data...})
})
// Esperado: rechazado (CORS o origin check)
```

### Test Rate Limiting
```bash
# Desde terminal:
for i in {1..101}; do
  curl -X POST https://innovart-capi-webhook-no-tocar.workers.dev \
    -H 'Content-Type: application/json' \
    -d '{...}'
done
# Esperado: primeros 100 = 200, el 101 = 429 Too Many Requests
```

---

## References

- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]] — Tech deep dive
- [[paso-a-paso-arreglo-formularios-2026-06-30]] — Form POST debugging
- [[filtro-capi-submitapplication-2026-06-22]] — CAPI validation logic
- [[protocolo-versionado-codigo-critico]] — Code versioning best practices
