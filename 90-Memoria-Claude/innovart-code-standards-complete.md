---
name: Innovart Code Standards — Guía Completa
description: Versionado, fbclid protocol, CAPI filter, Qikify window.BContact, seguridad
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Innovart Code Standards — Guía Completa

## 1. REGLA ABSOLUTA — Versionado de Código Crítico

**Cambios en estos archivos REQUIEREN versionado:**
- `layout/theme.liquid`
- `theme.pagefly.liquid`
- `theme.gempages.blank.liquid`
- Cloudflare Workers (CAPI, webhooks)
- Tracking scripts
- GHL bodyTrackingCode

**Ubicación del versionado:** `/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/`

**Formato:**
```markdown
# versionado-[archivo-nombre].md

## V1 — Descripción (fecha)
- Cambios
- Motivo
- Verificación

## V2 — Descripción (fecha)
- Cambios
- Motivo
- Verificación
```

**Ejemplo real:**
```markdown
# versionado-theme-pagefly-liquid.md

## V1 — Base (2026-06-28)
- HTML estructura: head + body + styles
- Tracking: Meta Pixel + fbclid

## V2 — Qikify Integration (2026-06-29)
- CAMBIO: Agregado `<script src="https://www.qikify.com/app/qikify.min.js"></script>`
- MOTIVO: Sin esto, window.BContact no existía → formularios Qikify no disparaban POST
- VERIFICACIÓN: typeof window.BContact === "object" en console

## V3 — CAPI Filter (2026-06-30)
- CAMBIO: Cloudflare Worker ahora filtra SubmitApplication sin fbclid
- MOTIVO: Reducir ruido de eventos fantasma en CAPI
- VERIFICACIÓN: 0 SubmitApplication sin PII en logs
```

---

## 2. fbclid Protocol — Estándar Innovart

### Dónde se captura fbclid

**EN TODAS ESTAS UBICACIONES:**
1. Landing `/home` (GHL)
2. Landings de ciudad (PageFly)
3. Qikify forms
4. Cualquier página que reciba tráfico Meta

### Cómo capturarlo

```javascript
// Siempre en <head> o bodyTrackingCode temprano
function captureFbclid() {
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  
  if (fbclid) {
    // Guardar en sessionStorage (no persiste, solo esta sesión)
    sessionStorage.setItem('fbclid', fbclid);
    
    // Optional: guardar en localStorage (persiste)
    localStorage.setItem('fbclid_last', fbclid);
    
    console.log('✅ fbclid captured:', fbclid);
  }
}

// Ejecutar inmediatamente
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', captureFbclid);
} else {
  captureFbclid();
}
```

### Dónde propagarlo

**En todos los formularios:**
```javascript
function propagateFbclid() {
  const fbclid = sessionStorage.getItem('fbclid');
  
  if (!fbclid) return;
  
  document.querySelectorAll('form').forEach(form => {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'fbclid';
    input.value = fbclid;
    form.appendChild(input);
  });
}
```

**A GHL fields:**
```javascript
// Si forma GHL, llenar custom field 'fbclid'
if (typeof window.ghl !== 'undefined') {
  window.ghl.setFieldValue('fbclid', sessionStorage.getItem('fbclid'));
}
```

**A Qikify:**
```javascript
// Interceptar BContact.send
if (typeof window.BContact !== 'undefined') {
  const originalSend = window.BContact.send;
  window.BContact.send = function(data) {
    data.fbclid = sessionStorage.getItem('fbclid');
    return originalSend(data);
  };
}
```

---

## 3. window.BContact — Qikify API Protocol

**CRÍTICO en Innovart:** window.BContact es la API de Qikify.

### Verificación de Disponibilidad

```javascript
function ensureQikifyReady(callback, maxAttempts = 10) {
  let attempts = 0;
  
  function check() {
    if (typeof window.BContact !== 'undefined') {
      console.log('✅ window.BContact ready');
      callback();
    } else if (attempts < maxAttempts) {
      attempts++;
      setTimeout(check, 500);
    } else {
      console.error('❌ Qikify failed to load after', maxAttempts * 500, 'ms');
    }
  }
  
  check();
}

// Uso
ensureQikifyReady(() => {
  console.log('Qikify is ready to use');
});
```

### Métodos Estándar

```javascript
// 1. Enviar formulario
if (typeof window.BContact !== 'undefined' && window.BContact.send) {
  window.BContact.send({
    name: 'John Doe',
    email: 'john@example.com',
    phone: '+573101234567',
    message: 'Custom message',
    utm_source: 'google',
    utm_medium: 'cpc',
    fbclid: 'fb_123456789'
  });
}

// 2. Pre-llenar campos
if (typeof window.BContact !== 'undefined' && window.BContact.setData) {
  window.BContact.setData({
    email: 'preloaded@example.com'
  });
}

// 3. Track evento personalizado
if (typeof window.BContact !== 'undefined' && window.BContact.track) {
  window.BContact.track('custom_event', { property: 'value' });
}
```

### Manejo de Errores

```javascript
// Interceptar y manejar errores de Qikify
function setupQikifyErrorHandling() {
  if (typeof window.BContact !== 'undefined') {
    const originalSend = window.BContact.send;
    
    window.BContact.send = function(data) {
      try {
        // Validar datos mínimos
        if (!data.email && !data.phone) {
          throw new Error('Email or phone is required');
        }
        
        // Enviar
        const result = originalSend(data);
        console.log('✅ Qikify sent successfully');
        return result;
        
      } catch (error) {
        console.error('❌ Qikify error:', error.message);
        alert('Error submitting form. Please try again.');
      }
    };
  }
}
```

---

## 4. CAPI Filter — Cloudflare Worker Pattern

**Ubicación:** Cloudflare Worker `innovart-capi-webhook-no-tocar`

**Propósito:** Bloquear eventos fantasma antes que lleguen a Meta.

### Lógica de Filtro

```javascript
// Cloudflare Worker

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('OK', { status: 200 });
    }
    
    try {
      const payload = await request.json();
      const event = payload.data?.[0];
      
      if (!event) return new Response(JSON.stringify({ ok: true }), { status: 200 });
      
      // ============================================
      // FILTRO 1: Bloquear SubmitApplication sin PII
      // ============================================
      if (event.event_name === 'SubmitApplication') {
        const userData = event.user_data || {};
        
        const hasEmail = userData.em || userData.email;
        const hasPhone = userData.ph || userData.phone;
        const hasExtId = userData.external_id;
        
        // Requiere al menos una PII
        if (!hasEmail && !hasPhone && !hasExtId) {
          console.log('❌ [FILTER] SubmitApplication sin PII → BLOCKED');
          return new Response(JSON.stringify({ skipped: true, reason: 'no_pii' }), { status: 200 });
        }
      }
      
      // ============================================
      // FILTRO 2: Bloquear eventos sin fbclid ni contacto
      // ============================================
      if (event.event_name === 'Lead') {
        const userData = event.user_data || {};
        const eventData = event.event_data || {};
        
        const hasFbclid = eventData.fbclid || userData.fbclid;
        const hasContact = userData.em || userData.ph;
        
        if (!hasFbclid && !hasContact) {
          console.log('❌ [FILTER] Lead sin fbclid ni contacto → BLOCKED');
          return new Response(JSON.stringify({ skipped: true, reason: 'no_fbclid_no_contact' }), { status: 200 });
        }
      }
      
      // ============================================
      // Si pasa filtros, enviar a Meta
      // ============================================
      const metaResponse = await fetch('https://graph.facebook.com/v18.0/...' , {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${env.META_TOKEN}` },
        body: JSON.stringify(payload)
      });
      
      console.log('✅ [PASSED] Event sent to Meta');
      return new Response(JSON.stringify({ success: true }), { status: 200 });
      
    } catch (error) {
      console.error('❌ Error:', error.message);
      return new Response(JSON.stringify({ error: error.message }), { status: 500 });
    }
  }
};
```

### Qué eventos filtrar

| Evento | Condición de Bloqueo |
|--------|---------------------|
| SubmitApplication | Sin email/phone/external_id |
| Lead | Sin fbclid y sin contacto |
| ViewContent | Sin content_id |
| Purchase | Sin value or currency |

---

## 5. Tracking Script Pattern — Estándar

```javascript
// Patrón universal para cualquier tracking script en Innovart

(function() {
  'use strict';
  
  // ============================================
  // STEP 1: Verificar que no se ejecute dos veces
  // ============================================
  if (window.innovartTrackerLoaded) {
    console.warn('Innovart Tracker already loaded');
    return;
  }
  window.innovartTrackerLoaded = true;
  
  // ============================================
  // STEP 2: Esperar a que DOM esté listo
  // ============================================
  function init() {
    console.log('Innovart Tracker initialized');
    
    // ============================================
    // STEP 3: Capturar parámetros de URL
    // ============================================
    const params = new URLSearchParams(window.location.search);
    const tracking = {
      fbclid: params.get('fbclid') || sessionStorage.getItem('fbclid'),
      utm_source: params.get('utm_source') || 'direct',
      utm_medium: params.get('utm_medium') || 'direct',
      utm_campaign: params.get('utm_campaign') || '',
      page_url: window.location.href,
      referrer: document.referrer,
      timestamp: new Date().toISOString()
    };
    
    // ============================================
    // STEP 4: Guardar en sessionStorage
    // ============================================
    Object.keys(tracking).forEach(key => {
      if (tracking[key]) {
        sessionStorage.setItem(key, tracking[key]);
      }
    });
    
    // ============================================
    // STEP 5: Propagar a formas/links
    // ============================================
    propagateTracking(tracking);
    
    // ============================================
    // STEP 6: Track en Meta Pixel
    // ============================================
    if (typeof fbq !== 'undefined') {
      fbq('track', 'PageView', tracking);
    }
    
    // ============================================
    // STEP 7: Log para debugging
    // ============================================
    if (window.innovartDebug) {
      console.log('Innovart Tracking:', tracking);
    }
  }
  
  function propagateTracking(tracking) {
    // A formularios
    document.querySelectorAll('form').forEach(form => {
      Object.keys(tracking).forEach(key => {
        let input = form.querySelector(`input[name="${key}"]`);
        if (!input && tracking[key]) {
          input = document.createElement('input');
          input.type = 'hidden';
          input.name = key;
          form.appendChild(input);
        }
        if (input) input.value = tracking[key];
      });
    });
    
    // A links
    document.querySelectorAll('a[href]').forEach(link => {
      try {
        const url = new URL(link.href, window.location.origin);
        Object.keys(tracking).forEach(key => {
          if (tracking[key]) {
            url.searchParams.set(key, tracking[key]);
          }
        });
        link.href = url.toString();
      } catch (e) {
        // Skip invalid URLs
      }
    });
  }
  
  // Ejecutar cuando DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
```

---

## 6. Testing Checklist — Pre-Deployment

**ANTES de publicar cualquier cambio, verificar:**

```javascript
// Copiar en console del navegador

(function() {
  console.log('=== INNOVART DEPLOYMENT CHECKLIST ===\n');
  
  let passes = 0;
  let total = 0;
  
  function test(name, condition) {
    total++;
    if (condition) {
      console.log('✅', name);
      passes++;
    } else {
      console.log('❌', name);
    }
  }
  
  // Verificaciones
  test('Meta Pixel loaded', typeof fbq !== 'undefined');
  test('fbclid captured', sessionStorage.getItem('fbclid') !== null);
  test('Clarity loaded', typeof clarity !== 'undefined');
  test('Qikify ready', typeof window.BContact !== 'undefined');
  test('Forms exist', document.querySelectorAll('form').length > 0);
  test('URL params propagated', new URL(document.querySelector('a')?.href).searchParams.get('fbclid') !== null);
  
  console.log(`\n${passes}/${total} tests passed`);
  
  if (passes === total) {
    console.log('✅ READY FOR DEPLOYMENT');
  } else {
    console.log('❌ FIX ISSUES BEFORE DEPLOYING');
  }
})();
```

---

## 7. Rollback Protocol

**Si algo falla POST-deployment:**

1. Identificar el archivo problemático
2. Revertir a versión anterior en Obsidian
3. Copiar código V[n-1] y publicar
4. Documentar en versionado:

```markdown
## V3 (ROLLED BACK)
- Issue: fbclid not propagating
- Rollback reason: Caused 45% form abandonment
- Reverted to V2 on 2026-06-30 14:30 UTC
```

---

## 8. Seguridad — Principios Clave

### NO hacer

```javascript
// ❌ NUNCA exponer tokens en cliente
const apiKey = 'sk_test_xxxxx'; // EXPOSICIÓN!

// ❌ NUNCA hacer upsert directo a Meta
fetch('https://graph.facebook.com/...', {
  body: JSON.stringify(userData) // El cliente puede modificar
});

// ❌ NUNCA confiar en datos de usuario
const fbclid = prompt('Enter your fbclid');

// ❌ NUNCA loguear PII
console.log(userData.phone); // A cualquiera que abra DevTools
```

### SÍ hacer

```javascript
// ✅ Guardar tokens en servidor (Cloudflare Worker secret)
const token = env.META_TOKEN; // Seguro

// ✅ Validar en servidor
// Worker valida signature, filtra, luego envía a Meta

// ✅ Capturar parámetros de URL legítimos
const fbclid = new URL(window.location).searchParams.get('fbclid');

// ✅ Hash de PII en cliente antes de enviar
const hashedEmail = sha256(email.toLowerCase());
```

---

## 9. Documentación de Cambios

**Cuando hagas un cambio, documenta:**

1. **QUÉ cambió** (archivo, línea, código viejo vs nuevo)
2. **POR QUÉ** (problema que soluciona, business case)
3. **CÓMO verificar** (test, métrica, log)
4. **ROLLBACK plan** (cómo revertir en 5 minutos)

Ejemplo:

```markdown
# Cambio: fbclid Capture Fix en /home (2026-06-30)

## Archivo
`/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/paso-a-paso-arreglo-formularios-2026-06-30.md`

## Cambio
Añadir script de captura en GHL bodyTrackingCode (antes de form rendering):

```javascript
function captureFbclid() {
  const fbclid = new URL(window.location).searchParams.get('fbclid');
  if (fbclid) sessionStorage.setItem('fbclid', fbclid);
}
captureFbclid();
```

## Por qué
EMQ 4.9 → 5.5+ (600 eventos/mes recuperados). Sin fbclid, Meta no matchea leads.

## Verificación
- Abrir DevTools → Application → Session Storage
- Copiar URL con ?fbclid=abc123
- Verificar que fbclid está en sessionStorage
- Enviar form y ver en GHL que fbclid field se rellena

## Rollback
Revertir a V2 en versionado-home-cro-2026-06-30.md
```

---

## 10. Checklist Final — Innovart Standards

- [ ] Código en español cuando sea posible (vars, comentarios)
- [ ] Versionado en Obsidian actualizado
- [ ] fbclid capturado en todas las páginas Meta traffic
- [ ] window.BContact verification en Qikify
- [ ] CAPI filter configurado en Worker
- [ ] Testing checklist ejecutado y pasado
- [ ] Rollback plan documentado
- [ ] Cambios comunicados al equipo
- [ ] Monitorear KPIs post-deployment

