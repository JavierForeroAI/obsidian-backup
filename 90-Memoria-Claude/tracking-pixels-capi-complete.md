---
name: Tracking Pixels & CAPI — Guía Completa
description: Meta Pixel, fbclid, CAPI, Google Ads, UTM, ejemplos para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Tracking Pixels & CAPI — Guía Completa

## 1. Meta Pixel — Setup Básico

### Instalar Meta Pixel en Shopify

En Shopify Admin → Settings → Customer events:
```
Apps and sales channels → Shopify sales channel → Manage → Customer events
```

O agregar manualmente en `theme.liquid`:

```html
<!-- Meta Pixel -->
<script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  
  // Reemplazar con tu Pixel ID
  fbq('init', '1642103999710262');
  fbq('track', 'PageView');
</script>

<noscript>
  <img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=1642103999710262&ev=PageView&noscript=1"
  />
</noscript>
```

**En Innovart:**
- Pixel ID: `1642103999710262` (principal en Shopify)
- Pixel GHL: `1625645205284016` (landing pages)

---

## 2. Meta Pixel Events

### Standard Events

```javascript
// PageView (automático, pero se puede triggerar manualmente)
fbq('track', 'PageView');

// ViewContent (ver producto)
fbq('track', 'ViewContent', {
  content_ids: ['123', '456'],
  content_type: 'product',
  content_name: 'Product Name',
  value: 99.99,
  currency: 'USD'
});

// AddToCart
fbq('track', 'AddToCart', {
  content_ids: ['123'],
  content_type: 'product',
  value: 99.99,
  currency: 'USD'
});

// Purchase
fbq('track', 'Purchase', {
  content_ids: ['123', '456'],
  content_type: 'product_group',
  value: 199.99,
  currency: 'USD'
});

// Lead (formulario submitido)
fbq('track', 'Lead', {
  content_name: 'Free Consultation',
  content_category: 'service',
  currency: 'USD',
  value: 0
});

// Contact (click en WhatsApp, phone, etc.)
fbq('track', 'Contact', {
  content_name: 'WhatsApp CTA',
  content_type: 'contact_method'
});

// Schedule (agendar cita)
fbq('track', 'Schedule', {
  content_name: 'Appointment Booked',
  content_type: 'appointment',
  value: 0,
  currency: 'USD'
});

// Custom Events
fbq('trackCustom', 'VideoPlay', {
  video_title: 'Before & After',
  duration: 120
});

fbq('trackCustom', 'SignUp', {
  user_type: 'newsletter_subscriber'
});
```

---

## 3. fbclid — Captura y Propagación

**fbclid = Facebook Click ID. Permite atribuir leads/ventas a anuncios Meta.**

### Capturar fbclid

```javascript
// Método 1: URLSearchParams
function captureFbclid() {
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  
  if (fbclid) {
    sessionStorage.setItem('fbclid', fbclid);
    console.log('fbclid captured:', fbclid);
  }
}

// Método 2: URL parsing
function getFbclidFromURL() {
  const url = new URL(window.location);
  return url.searchParams.get('fbclid');
}

// Ejecutar al cargar página
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', captureFbclid);
} else {
  captureFbclid();
}
```

### Propagar fbclid a formularios

```javascript
// Agregar hidden input a todos los forms con fbclid
function propagateFbclid() {
  const fbclid = sessionStorage.getItem('fbclid');
  
  if (!fbclid) return;
  
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    // Crear input oculto
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'fbclid';
    input.value = fbclid;
    
    form.appendChild(input);
  });
  
  console.log('fbclid propagated to', forms.length, 'forms');
}

document.addEventListener('DOMContentLoaded', propagateFbclid);
```

### Propagar fbclid a links

```javascript
function propagateFbclidToLinks() {
  const fbclid = sessionStorage.getItem('fbclid');
  
  if (!fbclid) return;
  
  const links = document.querySelectorAll('a[href]');
  
  links.forEach(link => {
    const url = new URL(link.href, window.location.origin);
    url.searchParams.set('fbclid', fbclid);
    link.href = url.toString();
  });
  
  console.log('fbclid propagated to', links.length, 'links');
}

document.addEventListener('DOMContentLoaded', propagateFbclidToLinks);
```

---

## 4. CAPI — Conversion API

**CAPI permite enviar eventos de servidor a Meta, sin depender de pixel.**

### Setup CAPI en Shopify

En Shopify → Settings → Customer events:
```
Shopify Sales Channel → Manage → Customer events → Meta
```

Conectar cuenta Meta y autorizar.

### CAPI Manual (Python)

```python
# Enviar evento CAPI a Meta Ads
import requests
import hashlib

def hash_pii(value):
    """Hash de PII (email, phone) para CAPI"""
    if not value:
        return None
    return hashlib.sha256(value.lower().encode()).hexdigest()

def send_capi_event(access_token, pixel_id, event_name, user_data, event_data):
    """
    Enviar evento a Meta Conversion API
    
    event_name: 'Lead', 'Purchase', 'ViewContent', etc.
    user_data: {'em': 'email', 'ph': 'phone', 'external_id': 'user_id'}
    event_data: {'value': 99.99, 'currency': 'USD', 'content_id': '123'}
    """
    
    url = f'https://graph.facebook.com/v18.0/{pixel_id}/events'
    
    # Hash PII
    hashed_user_data = {}
    if 'em' in user_data:
        hashed_user_data['em'] = hash_pii(user_data['em'])
    if 'ph' in user_data:
        hashed_user_data['ph'] = hash_pii(user_data['ph'])
    if 'external_id' in user_data:
        hashed_user_data['external_id'] = user_data['external_id']
    
    payload = {
        'data': [
            {
                'event_name': event_name,
                'event_time': int(time.time()),
                'event_id': f"{pixel_id}_{int(time.time())}",  # Dedup ID
                'user_data': hashed_user_data,
                'event_data': event_data,
                'custom_data': {
                    'value': event_data.get('value', 0),
                    'currency': event_data.get('currency', 'USD')
                }
            }
        ],
        'access_token': access_token
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Ejemplo de uso
send_capi_event(
    access_token='your_token',
    pixel_id='1642103999710262',
    event_name='Purchase',
    user_data={
        'em': 'customer@example.com',
        'ph': '+573101234567',
        'external_id': 'customer_123'
    },
    event_data={
        'value': 199.99,
        'currency': 'USD',
        'content_id': 'product_456'
    }
)
```

### CAPI vía JavaScript (usando fetch)

```javascript
async function sendCAPIEvent(eventName, userData, eventData) {
  const pixelId = '1642103999710262';
  const accessToken = 'your_access_token'; // Reemplazar
  
  const url = `https://graph.facebook.com/v18.0/${pixelId}/events`;
  
  function hashPII(value) {
    // Hash SHA-256 de PII
    return SHA256(value.toLowerCase()); // Requiere crypto-js
  }
  
  const payload = {
    data: [
      {
        event_name: eventName,
        event_time: Math.floor(Date.now() / 1000),
        event_id: `${pixelId}_${Date.now()}`,
        user_data: {
          em: userData.email ? hashPII(userData.email) : undefined,
          ph: userData.phone ? hashPII(userData.phone) : undefined,
          external_id: userData.external_id
        },
        event_data: eventData,
        custom_data: {
          value: eventData.value || 0,
          currency: eventData.currency || 'USD'
        }
      }
    ],
    access_token: accessToken
  };
  
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    
    const result = await response.json();
    console.log('CAPI event sent:', result);
    return result;
  } catch (error) {
    console.error('CAPI error:', error);
  }
}

// Usar
sendCAPIEvent('Lead', {
  email: 'user@example.com',
  phone: '+573101234567',
  external_id: 'user_123'
}, {
  value: 0,
  currency: 'USD',
  content_id: 'consultation'
});
```

---

## 5. UTM Tracking

### Capturar UTMs

```javascript
function captureUTMs() {
  const params = new URLSearchParams(window.location.search);
  
  const utms = {
    utm_source: params.get('utm_source') || 'direct',
    utm_medium: params.get('utm_medium') || 'direct',
    utm_campaign: params.get('utm_campaign') || '',
    utm_content: params.get('utm_content') || '',
    utm_term: params.get('utm_term') || '',
    gclid: params.get('gclid') || '',
    fbclid: params.get('fbclid') || ''
  };
  
  // Guardar en sessionStorage
  Object.keys(utms).forEach(key => {
    if (utms[key]) {
      sessionStorage.setItem(key, utms[key]);
    }
  });
  
  console.log('UTMs captured:', utms);
  return utms;
}

captureUTMs();
```

### Enviar UTMs con form

```javascript
function enrichFormWithUTMs() {
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    // Crear hidden inputs para cada UTM
    const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid'];
    
    utmKeys.forEach(key => {
      const value = sessionStorage.getItem(key);
      if (value) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value;
        form.appendChild(input);
      }
    });
  });
}

document.addEventListener('DOMContentLoaded', enrichFormWithUTMs);
```

---

## 6. Google Analytics 4 (gtag.js)

### Instalar GA4

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX'); // Reemplazar con tu ID
</script>
```

### Track Events en GA4

```javascript
// PageView (automático)
gtag('event', 'page_view');

// Track específico
gtag('event', 'view_item', {
  items: [
    {
      item_id: '123',
      item_name: 'Product Name',
      item_variant: 'color:red',
      price: 99.99,
      quantity: 1
    }
  ]
});

// Form submission
gtag('event', 'form_submit', {
  form_name: 'contact_form',
  form_id: 'contact_form_1'
});

// Lead
gtag('event', 'generate_lead', {
  currency: 'USD',
  value: 0
});

// Custom event
gtag('event', 'custom_event', {
  param1: 'value1',
  param2: 'value2'
});
```

---

## 7. Google Ads Conversion Tracking

### Instalar Google Ads Tag

```html
<!-- Google Ads Conversion Tracking -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-XXXXXXXXXX'); // Reemplazar
</script>
```

### Track Conversions

```javascript
// Lead conversion
gtag('event', 'conversion', {
  'send_to': 'AW-XXXXXXXXXX/LeadConversion',
  'value': 0,
  'currency': 'USD'
});

// Purchase conversion
gtag('event', 'purchase', {
  'send_to': 'AW-XXXXXXXXXX/PurchaseConversion',
  'value': 199.99,
  'currency': 'USD',
  'transaction_id': 'order_123'
});

// View conversion
gtag('event', 'page_view', {
  'send_to': 'AW-XXXXXXXXXX'
});
```

---

## 8. CAPI Filter — Bloquear Eventos Fantasma

**En Innovart:** Filtro en Cloudflare Worker para bloquear SubmitApplication sin fbclid/email/phone.

```javascript
// /innovart-capi-webhook-no-tocar (Cloudflare Worker)

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('OK', { status: 200 });
    }
    
    try {
      const payload = await request.json();
      
      // Filtro: Bloquear SubmitApplication sin PII o fbclid
      if (payload.data?.[0]?.event_name === 'SubmitApplication') {
        const userData = payload.data[0].user_data || {};
        const eventData = payload.data[0].event_data || {};
        
        const hasEmail = userData.em || userData.email;
        const hasPhone = userData.ph || userData.phone;
        const hasFbclid = eventData.fbclid || userData.fbclid;
        
        if (!hasEmail && !hasPhone && !hasFbclid) {
          console.log('❌ SubmitApplication blocked: No PII or fbclid');
          return new Response(JSON.stringify({ skipped: true }), { status: 200 });
        }
      }
      
      // Si pasa filtro, enviar a Meta
      const response = await fetch('https://graph.facebook.com/v18.0/...');
      
      return new Response(JSON.stringify({ success: true }), { status: 200 });
      
    } catch (error) {
      console.error('Error:', error);
      return new Response(JSON.stringify({ error: error.message }), { status: 500 });
    }
  }
};
```

---

## 9. Troubleshooting Tracking

### Problema: Pixel no tracks eventos

**Solución:**
```javascript
// Verificar que Pixel está cargado
if (typeof fbq !== 'undefined') {
  console.log('✅ Meta Pixel loaded');
} else {
  console.log('❌ Meta Pixel NOT loaded');
}

// Verificar eventos en Meta Pixel Helper (Chrome extension)
// O abrir DevTools → Network y filtrar por "facebook.com"
```

### Problema: fbclid no se propaga

**Solución:**
```javascript
// Verificar sessionStorage
console.log('fbclid:', sessionStorage.getItem('fbclid'));

// Verificar URL
const url = new URL(window.location);
console.log('fbclid from URL:', url.searchParams.get('fbclid'));
```

### Problema: CAPI retorna error

**Solución:**
```javascript
// Verificar token
// Verificar formato de payload
// Verificar que PII esté hasheado
// Ver logs en Meta Ads Manager → Events Manager
```

---

## 10. Resumen de IDs en Innovart

| Plataforma | ID | Tipo |
|------------|-----|------|
| Meta Pixel (Shopify) | `1642103999710262` | Pixel Principal |
| Meta Pixel (GHL) | `1625645205284016` | GHL Landing |
| Google Ads | `AW-XXXXXXXXXX` | Google Conversion |
| Google Analytics 4 | `G-XXXXXXXXXX` | GA4 Stream |
| Clarity | `x62cig8qug` | Session Replay |

---

## 11. Recursos Oficiales

- [Meta Pixel Docs](https://developers.facebook.com/docs/facebook-pixel/)
- [Meta CAPI Docs](https://developers.facebook.com/docs/marketing-api/conversions-api/)
- [GA4 Events](https://developers.google.com/analytics/devguides/collection/ga4/events)
- [Google Ads Conversion Tracking](https://support.google.com/google-ads/answer/1722054)

