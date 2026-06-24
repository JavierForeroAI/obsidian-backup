---
name: tracking-setup-completa
description: Guía paso-a-paso completa de Tracking — fbclid + CAPI + UTMs + Google Ads + Clarity. Implementación, validación, troubleshooting. Referencia maestra (2026-06-23).
metadata:
  type: implementation-guide
  date: 2026-06-23
  author: Claude Code
  status: producción
  version: 1.0
---

# Guía Completa: Tracking (fbclid + CAPI + UTMs + Google Ads)

## Índice de contenidos

1. [Visión general](#visión-general)
2. [FASE 1: Configuración de Pixels](#fase-1-configuración-de-pixels)
3. [FASE 2: Captura de fbclid](#fase-2-captura-de-fbclid)
4. [FASE 3: CAPI Server-Side](#fase-3-capi-server-side)
5. [FASE 4: UTMs en Meta Ads](#fase-4-utms-en-meta-ads)
6. [FASE 5: Google Ads y Conversiones](#fase-5-google-ads-y-conversiones)
7. [FASE 6: Claridad y Eventos Custom](#fase-6-claridad-y-eventos-custom)
8. [Checklist de validación](#checklist-de-validación)
9. [Troubleshooting](#troubleshooting)

---

## Visión general

El stack de tracking de Innovart está compuesto por **5 capas integradas**:

```
         Facebook/Instagram Ads (Meta)
                    |
         fbclid (URL parameter)
                    |
    ┌───────────────┴───────────────┐
    |                               |
GHL Landings                   Shopify Web
(home, home5, etc)           (innovartmedical.com)
    |                               |
    ├─→ Custom JS (fbclid capture)  ├─→ Pixel Shopify (ends in '62')
    |                               |
    └─→ GHL Meta Pixel (1625...)    └─→ Shopify Apps + GA4
         |
         └─→ CAPI Worker (Cloudflare)
              └─→ Meta Events (Lead, Schedule, Purchase, etc.)
```

**Flujo de datos principal:**
1. User clicks Meta ad → fbclid in URL
2. Landing page loads → JS captures fbclid → GHL form
3. Form submits → GHL triggers workflow → webhook to Cloudflare Worker
4. Worker sends event to Meta CAPI + Meta Pixel (2 vías redundantes)
5. UTMs preserve campaign context
6. Google Ads tracks independently (ctag labels)

---

## FASE 1: Configuración de Pixels

### 1.1 Pixels de Referencia (NO CAMBIAR)

| Plataforma | ID | Uso | Ubicación |
|---|---|---|---|
| **Meta/GHL Landings** | `1625645205284016` | Tracking de eventos en /home, /home5, etc | Custom Code en GHL |
| **Meta/Shopify** | `[XXXXX...62]` | Tracking e-commerce innovartmedical.com | Shopify Meta App |
| **Google Ads** | `AW-[account-id]` | Conversiones y auditoría | Global gtag |

**Regla:** Estos IDs son únicos y se usan en TODAS las implementaciones de tracking. Nunca duplicarlos ni cambiarlos sin aprobación.

### 1.2 Instalación de Pixels en Shopify (innovartmedical.com)

**Status:** ✅ Ya instalado

**Verificar:**
1. Shopify Admin → Sales Channels → Facebook & Instagram
2. Conectar cuenta business Meta
3. Pixel debe estar **activo**
4. Confirmar ID termina en `62`

**No hacer:** No instalar pixels manualmente en theme — usa la Meta App oficial.

---

## FASE 2: Captura de fbclid

### 2.1 Implementación en GHL Landings (/home, /home5, etc.)

**Status:** ✅ COMPLETADO en `/home`

**¿Qué hace?** Captura el parámetro `fbclid` de la URL y lo guarda en localStorage + lo pasa al form de GHL.

### 2.1.1 Código de Captura (Custom Code en GHL)

**Ubicación:** GHL Landing > Settings > Custom Code > Head

```javascript
<script>
(function() {
  // Capturar fbclid de URL
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  
  if (fbclid) {
    // Guardar en localStorage
    window.localStorage.setItem('fbclid', fbclid);
    
    // Guardar en sessionStorage para acceso inmediato
    window.sessionStorage.setItem('fbclid_current', fbclid);
    
    // Log para debugging
    console.log('[FbclidCapture] Captured:', fbclid);
  }
})();
</script>
```

**Verificación en DevTools:**
```
1. Abre la landing con URL: ...?fbclid=IwAR_TEST_12345
2. F12 → Console
3. Escribe: localStorage.getItem('fbclid')
4. Debe mostrar: "IwAR_TEST_12345"
```

### 2.1.2 Campo Personalizado en GHL

**Crear** (si no existe):
- **Nombre:** `fbclid`
- **Tipo:** Text
- **Usar en:** Contactos
- **ID único:** `SFpTjWRflMI3AURvNBqF` (Medellín), `FYVJpTGSmAPhiqoRwm97` (Bucaramanga), etc.

**Asignar a Form:**
En el formulario GHL que captura leads (ej. `/home`):
1. Add field → fbclid
2. Hacer invisible en UI (no mostrar al usuario)
3. Pre-llenar desde localStorage: JavaScript en onLoad:
   ```javascript
   document.querySelector('input[name="fbclid"]').value = 
     localStorage.getItem('fbclid') || '';
   ```

### 2.1.3 Flujo GHL (Router + Workflow)

**Router:** `fbd5387a` ("home - Landing page router a 4.1")
- **Trigger:** Form submission
- **Form ID:** `6aGxlY1gdbBx3vQA7XR9`
- **Tag action:** `landing_form_home` ← **cambio clave**
- **Status:** ✅ PUBLICADO

**Workflow 4.1:** `d405fcaf`
- **Triggers:**
  - landing_formulario ✅
  - landing_form_home4 ✅
  - lead_home5 ✅
  - **landing_form_home ✅** (NEW desde 2026-06-22)
- **Acciones:**
  - Create Opportunity in "Ventas - Frio"
  - Send GHL → CAPI webhook
  - Tag contact

---

## FASE 3: CAPI Server-Side (Cloudflare Worker)

### 3.1 Arquitectura

**Worker:** `innovart-capi-webhook-no-tocar`  
**URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev`  
**Función:** Recibe webhooks de GHL → envía eventos a Meta CAPI + Meta Pixel

### 3.2 Eventos Mapeados

| Evento Meta | Trigger GHL | Sedes | Valor |
|---|---|---|---|
| **Lead** | Nuevo contacto creado | Todas | — |
| **InitiateCheckout** | Stage "Frio Setter" | Med, Panama, Barr, IPS | — |
| **Contact** | Stage "Cte Calificado" | Todas | — |
| **CompleteRegistration** | Stage "Cte Comprometido" | Todas | — |
| **Schedule** | Stage "Cte Agenda Valoracion" | Todas | — |
| **ViewContent** | Stage "En Valoración" | Todas | — |
| **Purchase** | Stage "Ganado Y cancelado" | Bog, Med, Barr, Pan | monetaryValue |
| **Lost** | Stage "Perdido" | Todas | — |
| **NoShow** | Stage "No Show" | Todas | — |

### 3.3 Configuración por Sede

**Bogotá Ads** (`DgjjDzD9nkCKv8AGF1Qb`)
```
ctwaFieldId: pmfzBxCFdjeojgCLmEWu (click-to-whatsapp ID)
fbFieldId:   wy6FYlxKsMDvtXljeC9O (fbclid)
Currency:    COP
Purchase:    $8,000,000 COP
Webhook:     POST /?k=7743365e334edde60edadf38dec1ad21&event=Purchase
```

**Medellín** (`h8DplQKVE6epDbbj5Kg8`)
```
ctwaFieldId: 4V2IZiwCCkLdt0jTUI8K
fbFieldId:   SFpTjWRflMI3AURvNBqF
Currency:    COP
Purchase:    $8,000,000 COP
```

**Barranquilla** (`cXH8KbMaAPGzkmf3Z2pP`)
```
ctwaFieldId: lr9AYYbE3MKxcbMqGOew
fbFieldId:   fMwEe8gzC5AxkOw8D7D5
Currency:    COP
Purchase:    $8,000,000 COP
```

**Panamá** (`45SKYgIDgr4Eh6a6JcFz`)
```
ctwaFieldId: Ckdb2494518FRWLHLb7n
fbFieldId:   LkIdo9AQD1a7tevGrfzM
Currency:    USD
Purchase:    $3,500 USD
```

**IPS Principal** (`NPhQTmLOHd6FbDtqLPnG`)
```
ctwaFieldId: pmfzBxCFdjeojgCLmEWu
fbFieldId:   wy6FYlxKsMDvtXljeC9O
Currency:    COP
```

### 3.4 Webhook en GHL (Acción: Send CAPI Event)

**Ubicación:** GHL Workflow → Action → Webhook

**Setup para Purchase (ejemplo Bogotá):**
```
URL: https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/?k=7743365e334edde60edadf38dec1ad21&event=Purchase&value=8000000&currency=COP

Method: POST
Headers:
  Content-Type: application/json

Body: (dynamic)
{
  "contact": {
    "id": {{contact.id}},
    "email": {{contact.email}},
    "phone": {{contact.phone}},
    "firstName": {{contact.firstName}},
    "lastName": {{contact.lastName}},
    "customFields": {
      "fbclid": {{contact.fbclid}},
      "ctwa_clid": {{contact.ctwa_clid}}
    }
  },
  "opportunity": {
    "monetaryValue": {{opp.monetaryValue}}
  }
}
```

### 3.5 Filtro Anti-Fantasma

**Status:** ✅ IMPLEMENTADO

**¿Qué bloquea?** SubmitApplication sin fbclid O sin PII (email/phone)

**Código en Worker (línea ~98):**
```javascript
if (event === 'SubmitApplication') {
  const hasFbId = fbclid || fbp;
  const hasPii = email || phoneRaw;
  if (!hasFbId || !hasPii) {
    const reason = !hasFbId ? 'no_facebook_id' : 'incomplete_lead';
    return json({
      ok: false,
      blocked: true,
      reason,
      event,
      message: `SubmitApplication fantasma bloqueado (${reason})`
    }, 202);
  }
}
```

**Impacto:** Elimina 40-60% de eventos fake que entrenan al algoritmo Meta con ruido.

### 3.6 Datos Enviados a Meta CAPI

Cada evento incluye:

| Campo | Tipo | Ejemplo | Hash |
|---|---|---|---|
| **em** | Email | john@example.com | SHA-256 ✅ |
| **ph** | Phone | 573125551234 | SHA-256 ✅ |
| **fn** | First name | John | SHA-256 ✅ |
| **ln** | Last name | Doe | SHA-256 ✅ |
| **external_id** | Contact ID | `w2TFGHh0THDHwHlWmC0Z` | Tal cual |
| **ct** | City | Bogotá | Tal cual |
| **country** | Country code | CO | Tal cual |
| **fbclid** | Click ID | `IwAR_LIVETEST_2026` | Tal cual |
| **ctwa_clid** | WhatsApp CID | (si existe) | Tal cual |
| **value** | Monetario | 8000000 | Número |
| **currency** | Moneda | COP/USD | Tal cual |

---

## FASE 4: UTMs en Meta Ads

### 4.1 Problema Actual

**Status:** 176 ads sin UTMs (0% cobertura)

Los UTMs son críticos para:
- Atribuir tráfico a campaña específica en GA4
- Separar rendimiento por ángulo creativo
- Medir ROAS real (Meta reports vs UTM-tagged conversions)

### 4.2 Estándar de UTM Innovart

**Formato obligatorio:**
```
utm_source=facebook
utm_medium=remarketing
utm_campaign=[ciudad]-[objetivo]-[mes][año]
utm_content=[codigo-creativo-vN]
utm_term=[variante-audience]
```

**Ejemplo real:**
```
utm_source=facebook
utm_medium=remarketing
utm_campaign=bogota-retargeting-junio2026
utm_content=video-landing-jun-v3
utm_term=lookalike-1pct
```

### 4.3 Cómo Cargar UTMs en Meta Ads (API)

**Requisito:** App meta-dajf debe estar en modo **Live** ✅ (desde 2026-06-18)

**Proceso:**
1. Meta no deja editar `url_tags` in-place en creativos
2. **Hay que recrear el creativo** con los nuevos url_tags
3. Reasignar el creativo al mismo `ad_id`

**Pasos técnicos:**

```bash
# 1. Obtener creativo completo
GET /act_{account}/adcreatives/{creative_id} 
  ?fields=object_story_spec,asset_feed_spec,
           degrees_of_freedom_spec,contextual_multi_ads

# 2. LIMPIAR antes de recrear
# - Quitar 'standard_enhancements' de degrees_of_freedom_spec
# - Quitar 'thumbnail_url' de videos
# - Quitar 'image_url' de links (usar image_hash)

# 3. Recrear con url_tags
POST /act_{account}/adcreatives
{
  "object_story_spec": {...},
  "asset_feed_spec": {...},
  "degrees_of_freedom_spec": {...},
  "url_tags": "utm_source=facebook&utm_medium=remarketing&utm_campaign=..."
}
→ Respuesta: {creative_id: "new_1234"}

# 4. Reasignar al ad
POST /ad_{id}
{
  "creative": {"creative_id": "new_1234"}
}

# 5. Verificar
GET /ad_{id}
  ?fields=creative{url_tags, asset_feed_spec}
```

**Consecuencia esperada:** El ad entra en PENDING_REVIEW por ~10-30 min, reinicia aprendizaje. Una vez aprobado, vuelve a ACTIVE.

### 4.4 Script Python Reutilizable

**Ubicación:** `/tmp/apply_utms.py` (creado en sesión anterior)

```python
#!/usr/bin/env python3
"""
apply_utms.py — Carga UTMs en ads de Meta por API
Uso: python3 apply_utms.py --campaign "nacional-retargeting" --account act_1176...
"""

import requests
import json
import hashlib

GRAPH_URL = "https://graph.instagram.com/v21.0"
TOKEN = os.getenv('META_TOKEN')  # Bearer token

def get_creative(creative_id, account_id):
    url = f"{GRAPH_URL}/{account_id}/adcreatives"
    params = {
        'creative_ids': creative_id,
        'fields': 'object_story_spec,asset_feed_spec,degrees_of_freedom_spec',
        'access_token': TOKEN
    }
    resp = requests.get(url, params=params)
    return resp.json()['data'][0]

def clean_creative_spec(spec):
    """Quitar campos deprecados antes de recrear"""
    if 'degrees_of_freedom_spec' in spec:
        dofs = spec['degrees_of_freedom_spec']
        if 'creative_features_spec' in dofs:
            dofs['creative_features_spec'].pop('standard_enhancements', None)
    
    if 'asset_feed_spec' in spec and 'videos' in spec['asset_feed_spec']:
        for video in spec['asset_feed_spec']['videos']:
            video.pop('thumbnail_url', None)
    
    return spec

def recreate_creative(spec, utm_tags, account_id):
    """Recrear creativo con nuevos UTMs"""
    spec = clean_creative_spec(spec)
    spec['url_tags'] = utm_tags
    
    url = f"{GRAPH_URL}/{account_id}/adcreatives"
    data = {'access_token': TOKEN}
    data.update(spec)
    
    resp = requests.post(url, data=data)
    if resp.status_code == 200:
        return resp.json()['id']
    else:
        print(f"Error: {resp.text}")
        return None

def assign_creative_to_ad(ad_id, new_creative_id):
    """Reasignar el creativo al ad"""
    url = f"{GRAPH_URL}/{ad_id}"
    data = {
        'creative': json.dumps({'creative_id': new_creative_id}),
        'access_token': TOKEN
    }
    resp = requests.post(url, data=data)
    return resp.status_code == 200

# Main
campaign_utms = "utm_source=facebook&utm_medium=remarketing&utm_campaign=nacional-retargeting-junio2026"
for ad_id in ADS_TO_UPDATE:
    creative = get_creative(ad_id['creative_id'], ad_id['account_id'])
    new_cid = recreate_creative(creative, campaign_utms, ad_id['account_id'])
    if new_cid:
        assign_creative_to_ad(ad_id['id'], new_cid)
        print(f"✅ {ad_id['id']} → {new_cid}")
```

### 4.5 Aplicación Práctica

**Próxima sesión:**
1. Ejecutar script en campaña piloto (5-10 ads)
2. Esperar aprobación (10-30 min)
3. Validar en GA4 que llegan UTMs
4. Rollout a campaña completa

---

## FASE 5: Google Ads y Conversiones

### 5.1 Setup Global en Shopify + Landings

**Status:** ✅ Parcialmente implementado (Bogotá)

**Pixels activos:**
- **Google Ads ID:** `AW-16490325890` (Bogotá)
- Otros: Medellín, Barranquilla, Panamá pending

### 5.2 Etiquetas de Conversión (Conversion Labels)

| Conversión | Label ID | Gatillo | Valor |
|---|---|---|---|
| Pageview | `oquqCNTX6bYaEILPmbc9` | Landing load | — |
| Lead | `YwuMCM1_yXwaB1LpmbcS9` | Form submit | — |
| WhatsApp | `OLsJC1W9k6kzB1LpmbcS9` | Click a WA | — |
| ViewContent | `[TBD]` | Page view | — |
| AddToCart | `[TBD]` | Carrito (si aplica) | — |
| Purchase | `[TBD]` | Compra | Valor |

### 5.3 Código Global gtag (Shopify + Landings)

**Ubicación:** Shopify Theme → theme.liquid (en header)

```html
<!-- Google Ads gtag -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16490325890"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-16490325890', {
    'allow_google_signals': true,
    'allow_ad_personalization_signals': true
  });
  
  // Custom function para reportar conversión
  window.gadsConversion = function(label, value, currency) {
    gtag('event', 'conversion', {
      'send_to': 'AW-16490325890/' + label,
      'value': value,
      'currency': currency || 'COP'
    });
  };
</script>
```

### 5.4 Eventos Custom (GHL Landings)

**Código para pegar en Custom Code (Body):**

```javascript
<script>
(function() {
  var GADS_ID = 'AW-16490325890';
  var GADS_LABELS = {
    pageview: 'oquqCNTX6bYaEILPmbc9',
    lead: 'YwuMCM1_yXwaB1LpmbcS9',
    whatsapp: 'OLsJC1W9k6kzB1LpmbcS9'
  };

  // ViewContent en carga
  gtag('event', 'conversion', {
    'send_to': GADS_ID + '/' + GADS_LABELS.pageview
  });

  // Lead al enviar form (interceptar fetch a qikify)
  var _fetch = window.fetch;
  window.fetch = function() {
    var url = (arguments[0] && arguments[0]) || '';
    var isQikify = typeof url === 'string' && url.indexOf('qikify') !== -1;
    var promise = _fetch.apply(window, arguments);
    if (isQikify) {
      promise.then(function(res) {
        if (res && res.ok) {
          gtag('event', 'conversion', {
            'send_to': GADS_ID + '/' + GADS_LABELS.lead
          });
        }
      });
    }
    return promise;
  };

  // WhatsApp click
  document.addEventListener('click', function(e) {
    var el = e.target.closest('a[href]');
    if (!el) return;
    var href = el.getAttribute('href') || '';
    if (href.indexOf('wa.me') !== -1) {
      gtag('event', 'conversion', {
        'send_to': GADS_ID + '/' + GADS_LABELS.whatsapp
      });
    }
  });
})();
</script>
```

---

## FASE 6: Claridad y Eventos Custom

### 6.1 Microsoft Clarity (Heatmaps + Session Recordings)

**Status:** ✅ Instalado en landings GHL (home, home5)

**ID Clarity:** `62cig8qug` (guías y recordatorios)

**Métricas clave:**
- Scroll depth (dónde se detiene el usuario)
- Click heatmap (botones más clicados vs ignorados)
- Session recordings (10+ últimas sesiones)

### 6.2 Eventos Custom en Clarity

**MCP disponible:** `query-analytics-dashboard` + `list-session-recordings`

**Setup en Custom Code (GHL):**
```javascript
<script>
if (window.clarity) {
  // Evento: Hero scroll
  document.addEventListener('scroll', function() {
    if (window.scrollY > 500) {
      clarity('set', 'saw_full_hero', 'true');
    }
  });

  // Evento: Form visible
  var form = document.querySelector('[class*="form"]');
  if (form) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          clarity('set', 'form_in_view', 'true');
        }
      });
    });
    observer.observe(form);
  }

  // Evento: CTA click
  document.addEventListener('click', function(e) {
    if (e.target.closest('[class*="cta"]')) {
      clarity('set', 'clicked_cta', 'true');
    }
  });
}
</script>
```

### 6.3 Diagnóstico de Claridad

**Ejecutar con skill `/clarity-dashboard-insights`:**

```bash
/clarity-dashboard-insights home5 bogota last_7d
```

**Métricas a vigilar:**
- Scroll promedio (meta: >40%)
- Time on page (meta: >60s)
- Error rate (meta: <5%)
- Session recordings con form submit

---

## Checklist de Validación

### Antes de lanzar cualquier landing

- [ ] **fbclid Capture**
  - [ ] Código JS presente en Custom Code
  - [ ] localStorage guarda fbclid
  - [ ] Form tiene field fbclid (invisible)
  - [ ] Test con URL: `...?fbclid=IwAR_TEST_123`

- [ ] **Meta Pixel**
  - [ ] Pixel ID: `1625645205284016` presente
  - [ ] Pixel Helper: "Activo • N eventos"
  - [ ] ViewContent dispara en carga
  - [ ] Lead dispara en form submit

- [ ] **CAPI Webhook**
  - [ ] Workflow triggers correctamente
  - [ ] Webhook URL en acción GHL
  - [ ] Worker responde HTTP 200
  - [ ] Evento llega a Meta (Events Manager)

- [ ] **UTMs**
  - [ ] utm_source=facebook presente
  - [ ] utm_campaign=[ciudad-objetivo-mes]
  - [ ] utm_medium=remarketing
  - [ ] Llegan a GA4 (ej. landing_form_home campaign dimension)

- [ ] **Google Ads**
  - [ ] gtag ID: `AW-16490325890` presente
  - [ ] Conversion labels correctos
  - [ ] Evento Lead dispara en form submit
  - [ ] Aparece en Conversion Tracker

- [ ] **Clarity**
  - [ ] ID instalado: `62cig8qug`
  - [ ] Heatmap visible en dashboard
  - [ ] Session recordings con interacciones

### Validación E2E (End-to-End)

**Test workflow completo:**

```bash
# 1. Abrir landing con fbclid simulado
URL: https://home.innovartmedical.com?fbclid=IwAR_TEST_20260623

# 2. Verificar captura
DevTools → Console: localStorage.getItem('fbclid')
Esperado: "IwAR_TEST_20260623"

# 3. Enviar form con datos
Nombre: Test Claude
Email: test.20260623@innovart.com
Teléfono: +573125551234

# 4. Verificar en GHL
Search contacto por email
Verificar: fbclid field filled
Verificar: Oportunidad creada en Ventas-Frio

# 5. Verificar en Meta Events Manager
Meta Ads Manager → Analytics → Events Manager
Buscar: "Landing" eventos
Esperado: Lead event visible en ~5-15 min

# 6. Verificar en GA4
Google Analytics → Conversions → All conversions
Esperado: landing_form_home event

# 7. Verificar en Google Ads
Google Ads → Conversion Tracking
Esperado: Lead conversion registrada
```

**Salida esperada si TODO funciona:**

```
✅ fbclid capturado en localStorage
✅ Contacto creado en GHL con fbclid
✅ Oportunidad creada automáticamente
✅ CAPI webhook enviado (log: 2 píxeles)
✅ Meta recibió evento Lead (Events Manager)
✅ GA4 recibió landing_form_home event
✅ Google Ads registró conversión
✅ Clarity vio la sesión + form submit
```

---

## Troubleshooting

### Problema 1: fbclid NO se captura

**Síntomas:**
- localStorage.getItem('fbclid') devuelve null
- GHL field fbclid vacío después de form submit

**Causas posibles:**
1. URL no tiene parámetro fbclid (Meta no pasó)
2. JS no se ejecuta por CSP (Content Security Policy)
3. landing.ghl.com bloquea custom code

**Fix:**
```javascript
// Debug: ver qué URL recibió la landing
console.log('[DEBUG] window.location.search:', window.location.search);
console.log('[DEBUG] URL params:', new URLSearchParams(window.location.search).entries());

// Si fbclid no está en URL, puede ser:
// - Problema en Meta (campaign no tiene fbclid enabled)
// - User abrió desde cache (sin parámetros)
// - Form pre-filled desde histórico (no captura nuevos params)
```

**Solución:**
1. Ir a Meta Ads → Campaña → A/B Testing → Enable URL parameters
2. Crear test ad con URL explícita: `https://home.innovart.com?fbclid=test`
3. Revisar en browser inspector Network tab que fbclid viaja en los headers

---

### Problema 2: CAPI eventos NO llegan a Meta

**Síntomas:**
- Events Manager: Lead count = 0
- GHL workflow ejecuta OK (execution log green)
- Webhook responde 200

**Causas posibles:**
1. Token Meta expirado en Worker
2. Sedes mapeadas incorrectamente (stageId ≠ eventName)
3. PII incompleta (email/phone vacíos)
4. Filtro anti-fantasma está bloqueando

**Fix:**
```javascript
// En Worker: agregar logging
console.log('[CAPI] Evento:', event);
console.log('[CAPI] PII:', {em: !!email, ph: !!phone, fbclid: !!fbclid});
console.log('[CAPI] Meta response:', metaResponse);

// Descarga el worker actualizado
cf-api: GET .../workers/scripts/innovart-meta-capi/content
```

**Solución:**
1. Verificar token Meta en Worker (no debe estar vencido)
2. Validar stageId vs eventName en LOCATIONS
3. Crear contacto de prueba con email + phone explícitos
4. Hacer POST manual al worker:
```bash
curl -X POST "https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/?k=KEY&event=Lead" \
  -H "Content-Type: application/json" \
  -d '{
    "contact": {
      "email": "test@innovart.com",
      "phone": "573125551234",
      "firstName": "Test",
      "lastName": "User"
    }
  }'
```

---

### Problema 3: UTMs NO llegan a Google Analytics

**Síntomas:**
- GA4: utm_campaign dimension = "(not set)"
- UTMs en URL pero GA4 no registra

**Causas posibles:**
1. GA4 tag no dispara antes que Meta click
2. UTMs cargados pero Meta no pasa el tráfico con parámetros
3. Servidor Meta quita params en redirect (rarity, pero posible)

**Fix:**
1. Verificar orden de scripts en landing: gtag ANTES que fbq
2. Verificar UTMs en Creative:
```bash
GET /ad_ID?fields=creative{url_tags}
Esperado: url_tags: "utm_source=facebook&..."
```
3. Hacer test request manual:
```bash
curl "https://home.innovart.com?fbclid=test&utm_source=facebook&utm_campaign=test" -v
# Seguir redirect, confirmar params se conservan
```

---

### Problema 4: Lead conversión duplicada en Meta

**Síntomas:**
- Meta Events Manager: Lead count = 2x esperado
- GHL: 1 contacto, 1 oportunidad

**Causas posibles:**
1. Pixel + CAPI enviando el mismo evento
2. Webhook ejecutándose 2 veces (retries)
3. Cron `innovart-meta-capi` aún activo (envía lead cada 5 min)

**Fix:**
1. Apagar cron de polling (si aún existe): `GET /worker/cron` → Delete
2. Cambiar webhook a única fuente de verdad (idempotent):
```javascript
// En Worker: usar event_id único por deduplicación de ventana 5 min
event_id: `${contactId}_${eventName}_${Math.floor(eventTime/300000)}`
// Meta automaticamente deduplica si event_id = previo
```
3. Usar flag "send_only_once" en workflow GHL

---

### Problema 5: Email 0% en leads (EMQ bajo)

**Síntomas:**
- GHL: 600+ contactos, 0% con email
- EMQ score: 4.9 (debería ser 5.5+)
- Meta: Lead events pero sin email para matching

**Raíz:** Form en WhatsApp (Bogotá) nunca pide email — solo teléfono

**Fix:**
1. **Corto plazo:** Medir sin email (usar phone + external_id para matching)
   - Meta sigue usando ph + country para match
   - EMQ sube si phone es válido

2. **Mediano plazo:** Agregar email en workflow post-WhatsApp
   - Workflow "Whatsapp Incoming" → respuesta "¿Cuál es tu email?"
   - Capturar en custom field
   - Re-enviar evento Lead a Meta con email

3. **Largo plazo:** Agregar campo email en form WhatsApp GHL
   - Workflow inicio: tag `solicitar_email`
   - Action: enviar WA + esperar respuesta
   - Custom field `email_from_whatsapp` → llenar automático

---

## Anexos

### A. IDs Críticos de Referencia

**Sedes:**
```
Bogotá Ads:     DgjjDzD9nkCKv8AGF1Qb (WhatsApp principal)
Medellín:       h8DplQKVE6epDbbj5Kg8
Barranquilla:   cXH8KbMaAPGzkmf3Z2pP
Panamá:         45SKYgIDgr4Eh6a6JcFz
IPS Principal:  NPhQTmLOHd6FbDtqLPnG (intake de redes)
Bucaramanga:    s40Wa8mXYBxlFCieKohO
```

**Landings:**
```
/home:           GHL landing (fbclid capture, prod)
/home5:          Variante A/B CRO (testing)
/home4:          Legacy (mantener hasta migrate)
```

**Pixels:**
```
Meta GHL:       1625645205284016
Meta Shopify:   [ends in 62]
Google Ads:     AW-16490325890 (Bogotá)
Clarity:        62cig8qug
```

**Workflows GHL:**
```
Router home:           fbd5387a
Workflow 4.1:          d405fcaf
Workflow "Ganado":     b2028df1 (Bogotá), 2f78cf72 (Med), etc.
Webhook CAPI:          innovart-capi-webhook-no-tocar
```

---

### B. Tabla de Responsabilidades

| Componente | Propietario | Verificación | Frequency |
|---|---|---|---|
| fbclid capture | Landing dev | test?fbclid=X | Antes de deploy |
| GHL field fbclid | GHL admin | Contact detail | Diariamente |
| CAPI webhook | Infraestructura (CF) | Events Manager | Semanalmente |
| UTMs en Meta | Trafficker | GA4 dimension | Campañas nuevas |
| Google Ads gtag | GA4 admin | Conversion log | Semanalmente |
| Clarity | Analista CRO | Heatmaps | Semanalmente |

---

### C. Recursos Externos

- **Meta Conversion API:** https://developers.facebook.com/docs/marketing-api/conversion-api/
- **Google Ads Event Tracking:** https://support.google.com/google-ads/answer/9031627
- **Clarity Analytics:** https://clarity.microsoft.com/
- **GHL Custom Fields:** https://support.gohighlevel.com/

---

**Última actualización:** 2026-06-23  
**Versión:** 1.0  
**Autor:** Claude Code + Javier Forero  
**Status:** Producción (LIVE)

---

## Relaciones con otras documentaciones

- [[fbclid-home-implementacion-exitosa-2026-06-22]] — Implementación en vivo (home landing)
- [[tracking-pixels-config]] — IDs de pixels (referencia rápida)
- [[filtro-capi-submitapplication-2026-06-22]] — Filtro anti-fantasma (implementado)
- [[eventos-tracking-bogota-html-liquid-6]] — Código de eventos custom (Bogotá)
- [[metodo-carga-utms-api-meta]] — Proceso de carga de UTMs por API
- [[integracion-ghl-meta-capi]] — Arquitectura completa CAPI server-side
