---
name: Qikify Forms & Webhooks — Guía Completa
description: Form embeds, webhooks, API, CRM sync, ejemplos para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Qikify Forms & Webhooks — Guía Completa

## 1. Introducción a Qikify

Qikify es una plataforma de chatbot/forms que se integra con Shopify y CRM. En Innovart:
- Formularios incrustados en landings (ID: 483316)
- Webhook → GHL para sincronización de leads
- Bot de conversación WhatsApp/Messenger

---

## 2. Embed Qikify Form en Sitio

### Código de embed básico

```html
<!-- Qikify Contact Form Embed -->
<div id="qikify-form-container">
  <div contactform-embed="483316"></div>
</div>

<!-- Script de Qikify (se carga automático cuando el div existe) -->
<script src="https://www.qikify.com/app/qikify.min.js"></script>
```

### Con inicialización manual

```html
<div id="qikify-form-container">
  <div contactform-embed="483316"></div>
</div>

<script src="https://www.qikify.com/app/qikify.min.js"></script>

<script>
  // Esperar a que Qikify cargue
  function initQikify() {
    if (typeof window.BContact !== 'undefined') {
      console.log('Qikify BContact loaded');
      // window.BContact contiene la API del form
    } else {
      // Reintentar después de 500ms
      setTimeout(initQikify, 500);
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQikify);
  } else {
    initQikify();
  }
</script>
```

---

## 3. Qikify API — window.BContact

**IMPORTANTE en Innovart:** `window.BContact` es la API principal de Qikify.

### Propiedades disponibles

```javascript
// Verificar que Qikify está listo
if (typeof window.BContact !== 'undefined') {
  // Obtener datos del formulario
  const formData = window.BContact.formData || {};
  console.log('Form data:', formData);
  
  // Obtener ID de sesión
  const sessionId = window.BContact.sessionId;
  console.log('Session ID:', sessionId);
  
  // Obtener configuración
  const config = window.BContact.config || {};
  console.log('Config:', config);
}
```

### Métodos disponibles

```javascript
// Enviar datos personalizados
if (typeof window.BContact !== 'undefined' && window.BContact.send) {
  window.BContact.send({
    name: 'John Doe',
    email: 'john@example.com',
    phone: '+573101234567',
    message: 'Custom message',
    source: 'landing_page',
    utm_source: 'google',
    utm_medium: 'cpc'
  });
}

// Establecer datos en el form
if (typeof window.BContact !== 'undefined' && window.BContact.setData) {
  window.BContact.setData({
    email: 'preloaded@example.com'
  });
}

// Disparar evento personalizado
if (typeof window.BContact !== 'undefined' && window.BContact.track) {
  window.BContact.track('custom_event', { foo: 'bar' });
}
```

---

## 4. Enriquecer Formulario Qikify con UTMs

**Caso de uso en Innovart:** Capturar UTMs de anuncio Meta y enviarlos con form.

```javascript
<script>
  // Esperar a que Qikify cargue
  function enrichQikifyWithUTMs() {
    // Capturar UTMs de URL
    const params = new URLSearchParams(window.location.search);
    const utm_data = {
      utm_source: params.get('utm_source') || 'direct',
      utm_medium: params.get('utm_medium') || '',
      utm_campaign: params.get('utm_campaign') || '',
      utm_content: params.get('utm_content') || '',
      utm_term: params.get('utm_term') || '',
      fbclid: params.get('fbclid') || '',
      gclid: params.get('gclid') || ''
    };
    
    // Almacenar en sessionStorage para ref futura
    Object.keys(utm_data).forEach(key => {
      if (utm_data[key]) {
        sessionStorage.setItem(key, utm_data[key]);
      }
    });
    
    // Inyectar en Qikify si está disponible
    if (typeof window.BContact !== 'undefined') {
      if (window.BContact.setData) {
        // Pre-llenar form con algunos datos
        window.BContact.setData({
          utm_source: utm_data.utm_source,
          utm_medium: utm_data.utm_medium,
          utm_campaign: utm_data.utm_campaign
        });
      }
      
      // Interceptar envío para agregar UTMs
      const originalSend = window.BContact.send;
      window.BContact.send = function(data) {
        // Agregar UTMs al payload
        const enrichedData = {
          ...data,
          ...utm_data,
          page_url: window.location.href,
          referrer: document.referrer,
          timestamp: new Date().toISOString()
        };
        
        console.log('Sending to Qikify with UTMs:', enrichedData);
        return originalSend(enrichedData);
      };
    } else {
      // Reintentar si Qikify no está listo
      setTimeout(enrichQikifyWithUTMs, 500);
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enrichQikifyWithUTMs);
  } else {
    enrichQikifyWithUTMs();
  }
</script>
```

---

## 5. Qikify Webhook — Configuración

**En Qikify Dashboard:**
```
Settings → Webhooks → Add Webhook
```

### URL del Webhook (reemplazar con tu Worker)

```
https://your-domain.com/api/qikify-webhook
```

### Datos que Qikify envía

```json
{
  "event": "form_submitted",
  "timestamp": "2026-06-30T14:30:00Z",
  "contact": {
    "id": "qikify_contact_123",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+573101234567",
    "message": "I'm interested in your service"
  },
  "form": {
    "id": "483316",
    "name": "Contact Form",
    "source": "landing_page"
  },
  "metadata": {
    "utm_source": "google",
    "utm_medium": "cpc",
    "utm_campaign": "landing_v1",
    "fbclid": "fb_123456789",
    "page_url": "https://example.com/landing"
  }
}
```

---

## 6. Qikify → Cloudflare Worker → GHL

**Flujo en Innovart:**

```
Qikify Form Submit → Webhook → Cloudflare Worker → GHL API
```

### Cloudflare Worker Handler

```javascript
// worker-qikify.js (Cloudflare)

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    try {
      const payload = await request.json();
      
      console.log('Qikify webhook received:', payload);
      
      // Validar payload
      if (!payload.contact || !payload.contact.email) {
        return new Response('Invalid payload', { status: 400 });
      }
      
      // Preparar datos para GHL
      const ghlData = {
        firstName: payload.contact.name?.split(' ')[0] || 'Lead',
        lastName: payload.contact.name?.split(' ')[1] || '',
        email: payload.contact.email,
        phone: payload.contact.phone,
        message: payload.contact.message,
        source: 'qikify',
        // Tags para GHL
        tags: ['qikify', 'web_form', payload.metadata?.utm_source || ''].filter(Boolean),
        // Tracking
        fbclid: payload.metadata?.fbclid || '',
        utm_source: payload.metadata?.utm_source || '',
        utm_medium: payload.metadata?.utm_medium || '',
        utm_campaign: payload.metadata?.utm_campaign || '',
        customData: {
          qikify_contact_id: payload.contact.id,
          page_url: payload.metadata?.page_url,
          referrer: payload.metadata?.referrer
        }
      };
      
      // Enviar a GHL
      const ghlResponse = await sendToGHL(ghlData, env.GHL_API_KEY, env.GHL_LOCATION_ID);
      
      console.log('GHL response:', ghlResponse);
      
      return new Response(JSON.stringify({ success: true }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
      
    } catch (error) {
      console.error('Error processing webhook:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};

async function sendToGHL(data, apiKey, locationId) {
  const url = `https://rest.gohighlevel.com/v1/contacts/`;
  
  const payload = {
    firstName: data.firstName,
    lastName: data.lastName,
    email: data.email,
    phone: data.phone,
    tags: data.tags,
    // Custom fields (reemplazar con tus field IDs)
    customFields: {
      'utm_source': data.utm_source,
      'utm_medium': data.utm_medium,
      'utm_campaign': data.utm_campaign,
      'fbclid': data.fbclid,
      'source': data.source
    }
  };
  
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  
  if (!response.ok) {
    throw new Error(`GHL API error: ${response.status} ${response.statusText}`);
  }
  
  return response.json();
}
```

---

## 7. Validación y Sanitización en Qikify

```javascript
<script>
  // Interceptar y validar datos antes de enviar a Qikify
  function validateQikifyData() {
    if (typeof window.BContact !== 'undefined') {
      const originalSend = window.BContact.send;
      
      window.BContact.send = function(data) {
        // Validar email
        if (data.email && !isValidEmail(data.email)) {
          console.error('Invalid email:', data.email);
          alert('Please enter a valid email');
          return false;
        }
        
        // Validar teléfono (mínimo 10 dígitos)
        if (data.phone) {
          const phoneDigits = data.phone.replace(/\D/g, '');
          if (phoneDigits.length < 10) {
            console.error('Invalid phone:', data.phone);
            alert('Please enter a valid phone number');
            return false;
          }
        }
        
        // Sanitizar texto
        data.message = data.message?.trim().substring(0, 1000) || '';
        
        // Enviar validado
        console.log('Sending validated data to Qikify');
        return originalSend(data);
      };
    }
  }
  
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
  
  document.addEventListener('DOMContentLoaded', validateQikifyData);
</script>
```

---

## 8. Track Events en Qikify

```javascript
<script>
  // Rastrear eventos de formulario en Meta Pixel
  function setupQikifyTracking() {
    if (typeof window.BContact === 'undefined') {
      setTimeout(setupQikifyTracking, 500);
      return;
    }
    
    const originalSend = window.BContact.send;
    
    window.BContact.send = function(data) {
      // Track en Meta Pixel cuando form es enviado
      if (typeof fbq !== 'undefined') {
        fbq('track', 'Lead', {
          content_name: 'Qikify Form',
          value: 0,
          currency: 'USD',
          content_type: 'product'
        });
      }
      
      // Track en Google Analytics
      if (typeof gtag !== 'undefined') {
        gtag('event', 'form_submission', {
          form_name: 'qikify_contact',
          form_id: '483316'
        });
      }
      
      console.log('Qikify form tracked');
      
      return originalSend(data);
    };
  }
  
  document.addEventListener('DOMContentLoaded', setupQikifyTracking);
</script>
```

---

## 9. Multi-Language Forms en Qikify

```html
<!-- Form con selector de idioma -->
<div id="language-selector" style="margin-bottom: 20px;">
  <select id="form-language">
    <option value="es">Español</option>
    <option value="en">English</option>
  </select>
</div>

<div id="qikify-form-es" style="display: block;">
  <div contactform-embed="483316"></div>
</div>

<div id="qikify-form-en" style="display: none;">
  <div contactform-embed="483317"></div>
</div>

<script src="https://www.qikify.com/app/qikify.min.js"></script>

<script>
  document.getElementById('form-language').addEventListener('change', function(e) {
    const lang = e.target.value;
    
    // Ocultar todos
    document.getElementById('qikify-form-es').style.display = 'none';
    document.getElementById('qikify-form-en').style.display = 'none';
    
    // Mostrar seleccionado
    if (lang === 'es') {
      document.getElementById('qikify-form-es').style.display = 'block';
    } else {
      document.getElementById('qikify-form-en').style.display = 'block';
    }
  });
</script>
```

---

## 10. Qikify Con Conditional Logic

```javascript
<script>
  // Mostrar/ocultar campos basado en respuesta anterior
  function setupQikifyConditional() {
    if (typeof window.BContact === 'undefined') {
      setTimeout(setupQikifyConditional, 500);
      return;
    }
    
    // Observar cambios en el form
    const observer = new MutationObserver(() => {
      const inputs = document.querySelectorAll('input, select, textarea');
      
      inputs.forEach(input => {
        input.addEventListener('change', function() {
          // Si user selecciona "Urgent", mostrar campo adicional
          if (this.name === 'urgency' && this.value === 'urgent') {
            document.getElementById('urgent-message').style.display = 'block';
          }
        });
      });
    });
    
    const container = document.querySelector('[contactform-embed]');
    if (container) {
      observer.observe(container, { childList: true, subtree: true });
    }
  }
  
  document.addEventListener('DOMContentLoaded', setupQikifyConditional);
</script>
```

---

## 11. Gotchas en Qikify

### Problema: window.BContact no definido

**Causa:** Script de Qikify no se cargó o no esperamos a que cargue.

**Solución:**

```javascript
// Implementar retry loop
function waitForQikify(callback, maxAttempts = 10) {
  let attempts = 0;
  
  function check() {
    if (typeof window.BContact !== 'undefined') {
      callback();
    } else if (attempts < maxAttempts) {
      attempts++;
      setTimeout(check, 500);
    } else {
      console.error('Qikify failed to load');
    }
  }
  
  check();
}

waitForQikify(() => {
  console.log('Qikify ready!');
});
```

### Problema: Form no se renderiza

**Causa:** Elemento `<div contactform-embed>` falta o ID incorrecto.

**Solución:** Verificar que el ID (483316) coincida en Qikify dashboard.

### Problema: Webhook no recibe datos

**Causa:** URL de webhook incorrecta o Qikify deshabilitado en config.

**Solución:**
1. Verificar URL en Qikify Dashboard
2. Confirmar que el servidor responde 200 OK
3. Revisar logs de Qikify

---

## 12. Testing Qikify

```javascript
// Test script — copiar en consola del navegador
(function() {
  console.log('=== Qikify Test Suite ===');
  
  // Test 1: Qikify cargado
  if (typeof window.BContact !== 'undefined') {
    console.log('✅ Qikify loaded');
  } else {
    console.log('❌ Qikify NOT loaded');
  }
  
  // Test 2: UTMs capturados
  const utm_source = sessionStorage.getItem('utm_source');
  console.log('✅ UTM source:', utm_source || 'Not captured');
  
  // Test 3: Meta Pixel
  if (typeof fbq !== 'undefined') {
    console.log('✅ Meta Pixel loaded');
  } else {
    console.log('❌ Meta Pixel NOT loaded');
  }
  
  // Test 4: Enviar test
  if (typeof window.BContact !== 'undefined' && window.BContact.send) {
    console.log('✅ BContact.send available');
    console.log('Test data:', {
      name: 'Test User',
      email: 'test@example.com',
      phone: '+573101234567'
    });
  }
})();
```

---

## 13. Qikify vs Typeform vs Google Forms

| Aspecto | Qikify | Typeform | Google Forms |
|---------|--------|----------|--------------|
| Embed en sitio | ✅ | ✅ | ✅ |
| Webhook | ✅ | ✅ | ⚠️ Scripts |
| CRM Integration | ✅ | ⭐⭐⭐ | Manual |
| Conversational | ✅ Bot | ✅ | ❌ |
| Costo | $ | $$ | Free |

**En Innovart:** Qikify es la mejor opción para landing forms + webhook.

---

## 14. Recursos Oficiales

- [Qikify Docs](https://help.qikify.com/)
- [Qikify Embed Guide](https://help.qikify.com/article/embed-form)
- [Qikify Webhook Setup](https://help.qikify.com/article/webhooks)
- [GHL Integration](https://help.qikify.com/article/ghl-integration)

