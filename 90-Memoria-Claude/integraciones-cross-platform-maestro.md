---
name: "Integraciones Cross-Platform — Compilación Maestro"
description: "Guía completa de Shopify↔GHL, WordPress↔GHL, Qikify, Pixels unificados, UTM tracking, GDPR/Privacy. Documentación + código reutilizable + checklist."
metadata:
  type: "technical-reference"
  industry: "healthcare-aesthetics"
  company: "Innovart Medical"
  updated: "2026-06-30"
  status: "living-document"
  topics: ["integrations", "tracking", "gdpr", "crm", "marketing-automation", "compliance"]
  related-files: [
    "ctwa-sistema-100-operacional-2026-06-29.md",
    "utm-tracking-avance-general.md",
    "schema-arquitectura-logica-no-tocar.md",
    "tracking-setup-completa-2026-06-23.md"
  ]
---

# Integraciones Cross-Platform — Compilación Maestro

**Versión**: 1.0 | **Última actualización**: 30 junio 2026  
**Audiencia**: Equipo técnico Innovart, Esneider (tráfico), Diego (Google Ads), Javier (estrategia)  
**Propósito**: Documentar y hacer reutilizable toda arquitectura de integración multi-plataforma.

---

## RESUMEN EJECUTIVO

| Integración | Estado Innovart | Prioridad | Tiempo Setup | Complejidad |
|-------------|-----------------|-----------|--------------|-------------|
| **Shopify → GHL** | ✅ Funcional (webhooks) | P0 | 30 min | 🟢 Baja |
| **Shopify + CAPI Meta** | ⚠️ Bloqueado (sin permisos token) | P0 | 2 horas | 🟡 Media |
| **WordPress → GHL** | ❌ No implementado aún | P1 | 1 hora | 🟡 Media |
| **Qikify universal** | ✅ Funcional (Shopify + GHL) | P1 | 45 min | 🟢 Baja |
| **Pixel unificado Meta+Google** | ⚠️ Múltiples pixels dispersos | P0 | 3 horas | 🔴 Alta |
| **UTM tracking** | ⚠️ Parcial (landing sí, otros canales no) | P0 | 2 horas | 🟡 Media |
| **GDPR compliance** | ❌ No implementado | P1 | 2 horas | 🟡 Media |

**Recomendación**: Ejecutar P0 en semana 1-2 (CAPI + pixels + GDPR), P1 en semana 3-4 (WordPress si suma).

---

## 1. SHOPIFY ↔ GHL (Webhooks, CAPI, Lead Sync)

### 1.1 Métodos Nativos de Integración

#### **A) Webhooks Shopify + GHL API** (Innovart actual)

**Flujo**:
```
Shopify Event (form submit, order)
    ↓
Webhook HTTP POST a endpoint custom
    ↓
Validar y parsear payload
    ↓
GHL API: POST /contacts
    ↓
Contacto creado en GHL + triggers workflow
```

**Implementación mínima**:

```javascript
// En Cloudflare Worker o similar
export default {
  async fetch(request, env) {
    const body = await request.json();
    
    // Parsear payload Shopify
    const contact = {
      firstName: body.contact?.first_name || '',
      lastName: body.contact?.last_name || '',
      email: body.contact?.email || '',
      phone: body.contact?.phone || '',
      source: 'shopify_form',
      customField: {
        utm_source: new URL(request.url).searchParams.get('utm_source'),
        utm_campaign: new URL(request.url).searchParams.get('utm_campaign'),
        fbclid: new URL(request.url).searchParams.get('fbclid'),
      }
    };
    
    // Verificar existencia (evitar duplicados)
    const exists = await fetch(`https://api.gohighlevel.com/v1/contacts/search`, {
      method: 'POST',
      headers: {'Authorization': `Bearer ${env.GHL_TOKEN}`},
      body: JSON.stringify({query: contact.email})
    });
    
    if (exists.status === 200) {
      return new Response('Contact already exists', {status: 409});
    }
    
    // Crear contacto
    const response = await fetch('https://api.gohighlevel.com/v1/contacts', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.GHL_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contact)
    });
    
    return response;
  }
};
```

**Documentación oficial**:
- 📖 Shopify webhooks: https://shopify.dev/api/admin-rest/2024-10/resources/webhook
- 📖 GHL API docs: https://dev.gohighlevel.com/

**Checklist de setup**:
- [ ] Webhook endpoint creado (URL HTTPS + token verificación)
- [ ] GHL API key con permisos: `contacts:write`, `contacts:read`, `workflows:write`
- [ ] Mapeo de campos Shopify → GHL (email, phone, custom fields)
- [ ] Test E2E: formulario Shopify → GHL contacto en < 10s
- [ ] Logging/error handling en endpoint
- [ ] Rate limit: GHL permite ~100 requests/seg

---

#### **B) Lead Sync Automático (Variantes)**

**Caso 1: Formularios Shopify (PageFly, GemPages)**
- Form.submit → JS handler → webhook endpoint → GHL
- **Limitación**: Shopify no expone "form submit" como webhook nativo
- **Workaround**: Qikify o script custom con mutation observer

**Caso 2: Abandono de carrito**
```javascript
// Meta: cart_updated webhook
// Payload: customer, cart_total, items
// Acción: Tag en GHL "cart_abandoned" → trigger workflow SMS/WA
```

**Caso 3: Post-compra**
```javascript
// Meta: order_paid webhook
// Acción: Crear oportunidad en GHL tipo "Prospecto seguimiento"
// Workflow: enviar manual de post-operatorio + agendar cita
```

---

#### **C) Meta CAPI (Conversions API) desde Shopify**

**Problema que resuelve**: iOS privacy (iOS 14.5+) bloquea client-side tracking → CAPI evita.

**Flujo**:
```
User compra en Shopify
    ↓
Event "Purchase" dispara
    ↓
Servidor (Cloudflare Worker) captura
    ↓
Hashes PII (email, phone) → SHA256
    ↓
Envía a Meta CAPI con fbclid/fbp
    ↓
Meta matchea con usuario original
```

**Setup CAPI Innovart** (BLOQUEANTE P0):

1. **Token Meta**: 
   - Ir a: https://business.facebook.com/ → Settings → Users and Permissions
   - Generar System User token con permisos:
     - `ads_read`, `ads_management`, `business_management`
   - O usar Access Token de app custom (Life time)

2. **Cloudflare Worker**:
```javascript
export default {
  async fetch(request, env) {
    const order = await request.json();
    
    // Hash email y phone
    const crypto = require('crypto');
    const hashSha256 = (str) => crypto.createHash('sha256').update(str).digest('hex');
    
    const event = {
      event_name: 'Purchase',
      event_source_url: `https://implantecapilarencolombia.com/?fbclid=${order.fbclid}`,
      event_source_id: env.META_PIXEL_ID,
      action_source: 'website',
      event_id: order.order_id, // Deduplicación
      user_data: {
        em: hashSha256(order.customer.email.toLowerCase()),
        ph: hashSha256(order.customer.phone.replace(/[^\d]/g, '')),
        fbclid: order.fbclid,
        fbp: order.fbp, // Extraer de cookie
        client_ip_address: request.headers.get('cf-connecting-ip'),
        client_user_agent: request.headers.get('user-agent'),
      },
      custom_data: {
        value: order.total_price,
        currency: 'COP',
        content_type: 'product_group',
        content_name: 'Implante capilar',
        content_ids: order.items.map(i => i.sku),
      }
    };
    
    const response = await fetch(
      `https://graph.facebook.com/v18.0/${env.META_PIXEL_ID}/events`,
      {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          data: [event],
          access_token: env.META_TOKEN,
          test_event_code: env.META_TEST_EVENT_CODE, // Para testing
        })
      }
    );
    
    return response;
  }
};
```

3. **Configurar en wrangler.toml**:
```toml
[env.production]
vars = { META_PIXEL_ID = "1642103999710262" }
secrets = ["META_TOKEN", "META_TEST_EVENT_CODE"]
```

4. **Verificar en Meta Events Manager**:
   - https://business.facebook.com/events_manager
   - Pixel ID: 1642103999710262
   - Test Event Code: dentro de 24h se empiezan a ver eventos

**Parámetros clave CAPI**:
| Parámetro | Ejemplo | Obligatorio | Nota |
|-----------|---------|------------|------|
| `event_name` | "Purchase", "ViewContent" | ✅ | 29 valores estándar |
| `event_id` | UUID único | ✅ | Deduplicación (cliente + servidor) |
| `event_source_url` | URL con fbclid | ✅ | Contexto del evento |
| `user_data.em` | hash(email) | ✅ SHA256 | Obligatorio para matcheo |
| `user_data.ph` | hash(phone) | ⚠️ | Recomendado; formatos: `1234567890` |
| `custom_data.value` | 500000 | ✅ Para Purchase | En cents (COP) |
| `custom_data.currency` | "COP" | ✅ | ISO 4217 |

**Documentación oficial**:
- 📖 Meta CAPI: https://developers.facebook.com/docs/marketing-api/conversions-api/overview
- 📖 Event specs: https://developers.facebook.com/docs/marketing-api/conversions-api/event-set-up

---

### 1.2 Caso Actual Innovart

**Estado**: 
- ✅ Webhook form → GHL operacional (desde Qikify)
- ⚠️ CAPI Meta **bloqueado**: token sin permisos `campaigns_read`, `catalog_read`
- ❌ Purchase tracking: $0 revenue vinculado en Meta (sin fbclid histórico)

**Impacto**: No sé si CAPI está funcionando o si Meta recibe eventos = no optimizar ROAS.

**Acción inmediata**:
1. Verificar token Meta en Secrets Cloudflare (`innovart-capi-webhook-no-tocar`)
2. Si token expirado/sin permisos → regenerar en https://developers.facebook.com/apps
3. Test: `curl -X POST "https://graph.facebook.com/v18.0/[PIXEL_ID]/events?access_token=[TOKEN]"` 
4. Habilitar test_event_code para ver en Events Manager

---

### 1.3 Checklist Completo Shopify ↔ GHL

**Setup inicial**:
- [ ] Webhook endpoint en Cloudflare (HTTPS, token secret)
- [ ] GHL token en Secrets Cloudflare
- [ ] Mapeo de campos Shopify → custom fields GHL
  - [ ] email → email
  - [ ] phone → phone
  - [ ] utm_source → custom "utm_source"
  - [ ] utm_campaign → custom "utm_campaign"
  - [ ] fbclid → custom "fbclid"
- [ ] Validación: no crear duplicados (buscar por email antes)
- [ ] Workflows trigger: tag "contacto_shopify" → 4.1 SMS al lead

**Testing**:
- [ ] Test contacto desde form Shopify
- [ ] Verificar en GHL: contacto + tags + campos custom within 10s
- [ ] Verificar en GHL: workflow 4.1 disparó (SMS enviado)
- [ ] Monitorear errores en Cloudflare logs

**Mantenimiento**:
- [ ] Revisar logs cada 24h (errors en POST a GHL)
- [ ] Rate limit: si > 100 req/seg, implementar queue (Redis, DurableObjects)
- [ ] Annual: rotar tokens (expire Meta tokens cada 60 días si son de usuario)

---

## 2. WORDPRESS ↔ GHL (Form Submissions, Tracking)

### 2.1 Opciones de Integración (Sin código custom vs Con código)

**Sin código** (Recomendado para rápido):
```
WordPress Form Plugin (Gravity Forms)
    ↓
Zapier (intermediario)
    ↓
GHL Create Contact
```

**Con código** (Recomendado para control + ahorro):
```
WordPress custom hook (gform_after_submission)
    ↓
PHP script → GHL API directo
```

### 2.2 Opción A: Gravity Forms + Zapier

**Pasos**:

1. **Instalar Gravity Forms** (https://www.gravityforms.com/)
   - Costo: $99/año (básico) - $399/año (todo)
   - Características: form builder, conditional logic, confirmation rules

2. **Crear formulario** en WordPress:
   - Campos: First Name, Last Name, Email, Phone, City, Message
   - Confirmación: "Gracias, nos comunicaremos pronto"
   - Notificación: no enviar (es job de GHL via Zapier)

3. **Conectar a Zapier**:
   - https://zapier.com/ → Create Zap
   - Trigger: Gravity Forms → Form Submission
   - Acción: GoHighLevel → Create Contact
   - Mapear campos:
     ```
     GF.First Name → GHL.firstName
     GF.Last Name → GHL.lastName
     GF.Email → GHL.email
     GF.Phone → GHL.phone
     GF.City → GHL.custom["city"]
     GF.utm_source (hidden field) → GHL.custom["utm_source"]
     ```

4. **Test**:
   - Llenar formulario en WordPress
   - Verificar en GHL dentro 30s (Zapier delay típico)

**Costo**: Gravity Forms ($99-399/año) + Zapier ($20-125/mes)

---

### 2.3 Opción B: Webhooks WordPress + PHP Custom

**Ventaja**: 0 intermediarios, control total, sin costo variable

```php
<?php
// En wp-content/plugins/ghl-integration/ghl-integration.php

defined('ABSPATH') or die('No script kiddies please!');

class GHL_Integration {
  private $ghl_token;
  private $ghl_api_url = 'https://api.gohighlevel.com/v1';
  
  public function __construct() {
    $this->ghl_token = get_option('ghl_api_token');
    add_action('gform_after_submission_1', [$this, 'send_to_ghl'], 10, 2);
  }
  
  public function send_to_ghl($entry, $form) {
    // Extraer datos del formulario
    $contact_data = [
      'firstName' => sanitize_text_field($entry[1]), // GF Field ID 1
      'lastName' => sanitize_text_field($entry[2]),
      'email' => sanitize_email($entry[3]),
      'phone' => sanitize_text_field($entry[4]),
      'source' => 'wordpress_form',
      'customField' => [
        'city' => sanitize_text_field($entry[5]),
        'utm_source' => sanitize_text_field($_GET['utm_source'] ?? ''),
        'utm_campaign' => sanitize_text_field($_GET['utm_campaign'] ?? ''),
        'fbclid' => sanitize_text_field($_GET['fbclid'] ?? ''),
      ]
    ];
    
    // Buscar si existe
    $search_response = wp_remote_post("{$this->ghl_api_url}/contacts/search", [
      'headers' => [
        'Authorization' => "Bearer {$this->ghl_token}",
        'Content-Type' => 'application/json',
      ],
      'body' => json_encode(['query' => $contact_data['email']]),
      'timeout' => 10,
    ]);
    
    if (is_wp_error($search_response)) {
      error_log('[GHL] Search error: ' . $search_response->get_error_message());
      return;
    }
    
    $search_body = json_decode(wp_remote_retrieve_body($search_response), true);
    
    // Si existe, actualizar; si no, crear
    $method = isset($search_body['contacts'][0]['id']) ? 'PUT' : 'POST';
    $endpoint = $method === 'PUT' 
      ? "{$this->ghl_api_url}/contacts/{$search_body['contacts'][0]['id']}"
      : "{$this->ghl_api_url}/contacts";
    
    // Enviar a GHL
    $response = wp_remote_request($endpoint, [
      'method' => $method,
      'headers' => [
        'Authorization' => "Bearer {$this->ghl_token}",
        'Content-Type' => 'application/json',
      ],
      'body' => json_encode($contact_data),
      'timeout' => 10,
    ]);
    
    if (is_wp_error($response)) {
      error_log('[GHL] Request error: ' . $response->get_error_message());
    } else {
      $body = json_decode(wp_remote_retrieve_body($response), true);
      error_log('[GHL] Contact ' . ($method === 'POST' ? 'created' : 'updated') . ': ' . ($body['id'] ?? 'unknown'));
    }
  }
  
  // Hook para salvar API token en admin
  public static function register_settings() {
    register_setting('ghl_settings', 'ghl_api_token');
    add_settings_section('ghl_section', 'GHL Integration', null, 'ghl_settings');
    add_settings_field('ghl_api_token', 'API Token', [self::class, 'token_field'], 'ghl_settings', 'ghl_section');
  }
  
  public static function token_field() {
    $value = get_option('ghl_api_token');
    echo "<input type='password' name='ghl_api_token' value='" . esc_attr($value) . "' />";
  }
}

// Registrar plugin hooks
add_action('admin_menu', function() {
  add_options_page('GHL Integration', 'GHL Settings', 'manage_options', 'ghl_settings', function() {
    ?>
    <div class="wrap">
      <h1>GHL Integration Settings</h1>
      <form method="post" action="options.php">
        <?php settings_fields('ghl_settings'); ?>
        <?php do_settings_sections('ghl_settings'); ?>
        <?php submit_button(); ?>
      </form>
    </div>
    <?php
  });
});

add_action('admin_init', ['GHL_Integration', 'register_settings']);

// Inicializar plugin
new GHL_Integration();
```

**Instalación**:
1. Crear carpeta `/wp-content/plugins/ghl-integration/`
2. Copiar código arriba en `ghl-integration.php`
3. En WP admin → Plugins → Activar "GHL Integration"
4. Ir a Settings → GHL Settings, pegar token GHL

**Costo**: 0 (solo Gravity Forms si no tienes)

---

### 2.4 Lead Capture Avanzada (WordPress)

#### **Comentarios de blog → GHL**

```php
add_action('comment_post', function($comment_id, $comment_approved) {
  if ($comment_approved === 1) { // Solo si es aprobado
    $comment = get_comment($comment_id);
    
    wp_remote_post('https://api.gohighlevel.com/v1/contacts', [
      'headers' => ['Authorization' => "Bearer " . get_option('ghl_api_token')],
      'body' => json_encode([
        'firstName' => sanitize_text_field($comment->comment_author),
        'email' => sanitize_email($comment->comment_author_email),
        'source' => 'blog_comment',
        'description' => $comment->comment_content,
        'tags' => ['blog_commentor'],
      ]),
    ]);
  }
}, 10, 2);
```

#### **Descargas de Lead Magnet → GHL**

(Usar plugin como Easy Digital Downloads + custom hook)

```php
add_action('edd_payment_complete', function($payment_id) {
  $payment = new EDD_Payment($payment_id);
  
  wp_remote_post('https://api.gohighlevel.com/v1/contacts', [
    'headers' => ['Authorization' => "Bearer " . get_option('ghl_api_token')],
    'body' => json_encode([
      'firstName' => $payment->first_name,
      'email' => $payment->email,
      'phone' => $payment->user_data['phone'] ?? '',
      'source' => 'lead_magnet_download',
      'description' => 'Descargó: ' . implode(', ', wp_list_pluck($payment->cart_details, 'name')),
      'tags' => ['lead_magnet'],
    ]),
  ]);
});
```

---

## 3. QIKIFY UNIVERSAL

### 3.1 Compatibilidad Multi-Plataforma

| Plataforma | Soporte | Método | Ejemplo |
|-----------|---------|--------|---------|
| **Shopify** | ✅ Nativo | Embed en theme.liquid | `<div contactform-embed="483316"></div>` |
| **WordPress** | ✅ Plugin + embed | Shortcode + JS | `[qikify id="123"]` |
| **GHL Pages** | ✅ Nativo | Embed en bodyTrackingCode | `<div contactform-embed="ID"></div>` |
| **Standalone** | ✅ iframe | URL direkta | `https://app.qikify.com/form/ID` |
| **Mailchimp** | ⚠️ Limitado | Script custom | Webhook sync |

### 3.2 Configuración Shopify (Innovart actual)

```html
<!-- En theme.liquid, antes de </body> -->

<!-- Qikify form embed -->
<div contactform-embed="483316"></div>

<!-- Cargar script Qikify (IMPORTANTE: después del div) -->
<script src="https://www.qikify.com/app/qikify.min.js"></script>

<!-- Nota: 2026-06-29 — Agregar </body> a cierre de theme -->
```

**Configuración en dashboard Qikify**:
1. Ir a https://app.qikify.com/ → Forms → "Innovart Landing"
2. Campos:
   - ✅ Nombre (required)
   - ✅ Email (required)
   - ✅ Teléfono (required)
   - ✅ Ciudad (dropdown: Bogotá, Medellín, Barranquilla, Panamá, Bucaramanga)
   - ✅ Consulta (textarea, optional)

3. Integraciones → Webhooks:
   - Endpoint: `https://innovart-qikify-webhook.workers.dev`
   - Headers: `Authorization: Bearer [SECRET_TOKEN]`
   - Payload: JSON (automático)

4. Success message: 
   ```
   "¡Gracias! Te contactaremos en las próximas 2 horas por WhatsApp."
   ```

**Webhook Payload típico** (Cloudflare Worker recibe):
```json
{
  "formId": "483316",
  "submissionId": "sub_abc123",
  "submission": {
    "name": "Carlos García",
    "email": "carlos@email.com",
    "phone": "+573101234567",
    "city": "Bogotá",
    "consult": "Tengo alopecia androgénica",
    "timestamp": "2026-06-30T15:45:22Z",
    "ipAddress": "203.0.113.42",
    "utmSource": "instagram",
    "utmCampaign": "implante_junio"
  }
}
```

### 3.3 WordPress (Si suma)

```html
<!-- En footer.php o shortcode [qikify] -->
<div id="qikify-form"></div>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const script = document.createElement('script');
    script.src = 'https://www.qikify.com/app/qikify.min.js';
    document.body.appendChild(script);
    
    // Inyectar con delay (esperar script cargar)
    setTimeout(() => {
      const form = document.createElement('div');
      form.setAttribute('contactform-embed', '483316');
      document.getElementById('qikify-form').appendChild(form);
    }, 500);
  });
</script>
```

### 3.4 Routing Condicional (Qikify API)

**Caso**: Enviar a webhook diferente según ciudad

```json
// En Qikify Settings → Advanced Routing
{
  "rules": [
    {
      "condition": "field_city === 'Bogotá'",
      "webhook": "https://innovart-bogota-webhook.workers.dev"
    },
    {
      "condition": "field_city === 'Medellín'",
      "webhook": "https://innovart-medellin-webhook.workers.dev"
    },
    {
      "default": true,
      "webhook": "https://innovart-default-webhook.workers.dev"
    }
  ]
}
```

---

## 4. PIXEL UNIFICADO (Meta + Google)

### 4.1 Arquitectura Recomendada

```
┌─────────────────────────────────────┐
│ Google Tag Manager (GTM) Container  │
│ ID: GTM-XXXXXX                      │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ↓          ↓          ↓
Meta Pixel   GA4 Tag   Custom Event
(client-side)(GA4)     (server-side)
    │          │          │
    └──────────┼──────────┘
               ↓
    ┌──────────────────────┐
    │ Cloudflare Worker    │
    │ (Deduplicador)       │
    └──────────┬───────────┘
               │
    ┌──────────┴───────────┐
    ↓                      ↓
Meta CAPI           Google Measurement
(server-side)       Protocol (server-side)
```

### 4.2 Instalación GTM

1. **Crear cuenta en Google Tag Manager**:
   - https://tagmanager.google.com/
   - Crear "Contenedor Web"
   - Copiar ID: `GTM-XXXXXX`

2. **Instalar snippet en Shopify**:
   - Theme Editor → Edit code → theme.liquid
   - Antes de `</head>`, agregar:
   ```html
   <!-- Google Tag Manager -->
   <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
   new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
   j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
   'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
   })(window,document,'script','dataLayer','GTM-XXXXXX');</script>
   <!-- End Google Tag Manager -->
   ```

   - Después de `<body>` opening tag:
   ```html
   <!-- Google Tag Manager (noscript) -->
   <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXX"
   height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
   <!-- End Google Tag Manager (noscript) -->
   ```

### 4.3 Configurar Tags en GTM

#### **Tag 1: Meta Pixel (Page View)**

- **Name**: Meta Pixel - Page View
- **Type**: Conversion Pixel
- **Pixel ID**: 1642103999710262
- **Trigger**: All Pages
- **Advanced Settings**:
  ```
  Event Parameter: 'PageView'
  Value: 1
  Currency: 'COP'
  ```

#### **Tag 2: GA4 (Page View + Events)**

- **Name**: GA4 - All Pages
- **Type**: Google Analytics: GA4 Configuration
- **Measurement ID**: G-XXXXXXXXXX (obtener de Google Analytics)
- **Trigger**: All Pages
- **Custom Events**:
  - `form_submit`: cuando usuario envía formulario
  - `whatsapp_click`: cuando hace click en botón WA
  - `add_to_cart`: cuando agrega algo

#### **Tag 3: Custom Event (Form Submit)**

- **Name**: Form Submit Event
- **Type**: Custom HTML
- **HTML**:
  ```javascript
  <script>
    document.addEventListener('submit', function(e) {
      if (e.target.tagName === 'FORM') {
        window.dataLayer.push({
          event: 'form_submit',
          form_id: e.target.id,
          form_name: e.target.name || 'unknown',
          form_method: e.target.method
        });
      }
    });
  </script>
  ```
- **Trigger**: Page View (All Pages)

### 4.4 Variables GTM

**Setup de variables para capturar parámetros**:

| Variable | Tipo | Valor | Usar en... |
|----------|------|-------|-----------|
| `utm_source` | Query Param | `utm_source` | All tags |
| `utm_campaign` | Query Param | `utm_campaign` | All tags |
| `fbclid` | Query Param | `fbclid` | Meta Pixel + CAPI |
| `form_name` | Data Layer | `form_name` | Form Event |
| `page_title` | DOM Element | `document.title` | GA4 |
| `client_id` | Cookie | `_ga` | GA4 dedup |

### 4.5 Deduplicación de Eventos

**Problema**: Mismo evento enviado 2 veces (client-side JS + server-side CAPI) = Meta cuenta doble = ROAS falso

**Solución A: Event ID único** (Recomendado)

```javascript
// En tag GTM Custom HTML (head)
<script>
  // Generar evento ID único
  const eventId = 'evt_' + Date.now() + '_' + Math.floor(Math.random() * 10000);
  
  // Guardar en sessionStorage para server-side
  sessionStorage.setItem('lastEventId', eventId);
  
  // Inyectar en data layer
  window.dataLayer.push({
    event: 'page_view',
    event_id: eventId
  });
</script>
```

**En Cloudflare Worker** (server-side):
```javascript
// Recibir mismo event_id del cliente
const event_id = request.url.searchParams.get('event_id') || body.event_id;

// Enviar a Meta con deduplicación
await fetch('https://graph.facebook.com/v18.0/[PIXEL_ID]/events', {
  method: 'POST',
  body: JSON.stringify({
    data: [{
      event_name: 'Purchase',
      event_id: event_id, // CLAVE: Meta deduplicará automáticamente
      // ... resto de parámetros
    }],
    access_token: env.META_TOKEN
  })
});
```

**Solución B: Routing por tipo de evento**

- **Cliente (JS)**: ViewContent + InitiateCheckout solamente
- **Servidor (CAPI)**: Purchase solamente (conversión real)
- **Resultado**: No hay overlap

**Solución C: Cloudflare Deduplicador** (KV store)

```javascript
export default {
  async fetch(request, env) {
    const body = await request.json();
    const eventId = body.event_id;
    
    // Verificar en KV si ya procesado
    const cached = await env.DEDUP_EVENTS.get(`event:${eventId}`);
    if (cached) {
      return new Response('Already processed', {status: 409});
    }
    
    // Guardar en KV por 24h (Meta window de deduplicación)
    await env.DEDUP_EVENTS.put(`event:${eventId}`, '1', {expirationTtl: 86400});
    
    // Enviar a Meta (1 sola vez)
    // ...
  }
};
```

---

## 5. UTM TRACKING CROSS-PLATFORM

### 5.1 Parámetros Estándar + Custom Innovart

```
URL base: https://implantecapilarencolombia.com/home

Con UTM: https://implantecapilarencolombia.com/home?utm_source=instagram&utm_medium=cpc&utm_campaign=implante_mayo_2026&utm_content=video_hero&fbclid=EAIaIQobChMIpq7...
```

| Parámetro | Ejemplo | Requerido | Fuente |
|-----------|---------|-----------|--------|
| `utm_source` | instagram, whatsapp, google_ads, organic | ✅ | Plataforma origen |
| `utm_medium` | cpc, cpm, paid_social, organic | ✅ | Tipo de canal |
| `utm_campaign` | implante_mayo_2026, whatsapp_leads | ✅ | Nombre campaña |
| `utm_content` | video_hero, button_green, image_carousel | ⚠️ | A/B test identifier |
| `utm_term` | "implante capilar" | ⚠️ | Keyword (Google Ads) |
| `fbclid` | EAIaIQobChMIpq7U... | ✅ Meta | Meta click ID |
| `gclid` | CjwKCAj... | ✅ Google | Google click ID |

### 5.2 Captura y Persistencia

#### **Opción A: localStorage** (Innovart actual)

```javascript
// Ejecutar al cargar página (en <head> o theme.liquid)
(function() {
  const params = new URLSearchParams(window.location.search);
  
  // Extraer UTM + fbclid
  const utm = {
    source: params.get('utm_source') || 'direct',
    medium: params.get('utm_medium') || 'direct',
    campaign: params.get('utm_campaign') || '',
    content: params.get('utm_content') || '',
    term: params.get('utm_term') || '',
    fbclid: params.get('fbclid') || '',
    gclid: params.get('gclid') || '',
    timestamp: Date.now(),
  };
  
  // Guardar en localStorage (persiste mientras no borren cache)
  localStorage.setItem('utm_data', JSON.stringify(utm));
  
  // Inyectar en data layer GTM
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: 'utm_captured',
    ...utm
  });
})();
```

**Ventajas**: Simple, cross-domain (mismo origen), sin cookie consent requerido  
**Limitaciones**: Se borra al limpiar cache, max ~90 días efectivos

#### **Opción B: First-Party Cookie** (Recomendado)

```javascript
// Guardar por 90 días (LSPDP Colombia-compatible si informado en política)
function setUtmCookie(name, value) {
  const date = new Date();
  date.setTime(date.getTime() + (90 * 24 * 60 * 60 * 1000));
  
  // SameSite=Lax: permite cross-domain si es navegación natural
  document.cookie = `utm_${name}=${encodeURIComponent(value)}; expires=${date.toUTCString()}; path=/; SameSite=Lax`;
}

const params = new URLSearchParams(window.location.search);
params.forEach((value, key) => {
  if (key.startsWith('utm_') || key === 'fbclid' || key === 'gclid') {
    setUtmCookie(key, value);
  }
});
```

**Ventajas**: Persiste 90 días, respeta privacy moderna  
**Limitaciones**: Requiere informar en política de cookies

#### **Opción C: Server-Side (Cloudflare KV)** (Máxima privacidad)

```javascript
// En Cloudflare Worker
export default {
  async fetch(request, env) {
    // Generar fingerprint del usuario (sin PII)
    const ip = request.headers.get('cf-connecting-ip');
    const ua = request.headers.get('user-agent');
    const fingerprint = await crypto.subtle.digest('SHA-256', 
      new TextEncoder().encode(ip + ua)
    );
    
    const url = new URL(request.url);
    const utm = {
      source: url.searchParams.get('utm_source') || 'direct',
      medium: url.searchParams.get('utm_medium') || 'direct',
      campaign: url.searchParams.get('utm_campaign') || '',
      fbclid: url.searchParams.get('fbclid') || '',
      timestamp: Date.now(),
    };
    
    // Guardar en KV por 90 días
    await env.UTM_KV.put(
      `utm:${fingerprint}`,
      JSON.stringify(utm),
      {expirationTtl: 7776000} // 90 días
    );
    
    // Pasar UTM al cliente via header o cookie
    const response = new Response(/* ... */);
    response.headers.set('X-UTM-Stored', 'true');
    return response;
  }
};
```

**Ventajas**: 0 cookies en cliente, máxima privacidad GDPR  
**Limitaciones**: Requiere Cloudflare, latencia de KV lookup

### 5.3 Inyección en Formularios

#### **Shopify + Qikify**
```html
<!-- Qikify captura automáticamente parámetros URL -->
<!-- No requiere setup adicional -->
<div contactform-embed="483316"></div>
```

#### **Formularios custom (WordPress, HTML)**
```html
<form method="POST" action="/submit-lead">
  <input type="email" name="email" required>
  
  <!-- Hidden fields para UTM (se llenan por JS) -->
  <input type="hidden" name="utm_source" id="utm_source">
  <input type="hidden" name="utm_medium" id="utm_medium">
  <input type="hidden" name="utm_campaign" id="utm_campaign">
  <input type="hidden" name="fbclid" id="fbclid">
  
  <button type="submit">Enviar</button>
</form>

<script>
  // Llenar campos hidden con data guardada
  document.addEventListener('DOMContentLoaded', () => {
    const utm = JSON.parse(localStorage.getItem('utm_data') || '{}');
    
    document.getElementById('utm_source').value = utm.source || '';
    document.getElementById('utm_medium').value = utm.medium || '';
    document.getElementById('utm_campaign').value = utm.campaign || '';
    document.getElementById('fbclid').value = utm.fbclid || '';
  });
</script>
```

### 5.4 Validación y Limpieza

```javascript
function validateAndCleanUTM(utm) {
  // Whitelist de valores permitidos
  const VALID_SOURCES = new Set([
    'whatsapp', 'instagram', 'facebook', 'google_ads', 
    'google_organic', 'organic', 'direct', 'referral',
    'email', 'affiliate'
  ]);
  
  const VALID_MEDIUMS = new Set([
    'cpc', 'cpm', 'cpv', 'organic', 'paid_social',
    'email', 'direct', 'affiliate'
  ]);
  
  // Validar source
  if (utm.source && !VALID_SOURCES.has(utm.source)) {
    console.warn(`Invalid utm_source: ${utm.source} (using 'direct')`);
    utm.source = 'direct';
  }
  
  // Validar medium
  if (utm.medium && !VALID_MEDIUMS.has(utm.medium)) {
    console.warn(`Invalid utm_medium: ${utm.medium} (using 'direct')`);
    utm.medium = 'direct';
  }
  
  // Limitar largo (XSS prevention)
  const MAX_LENGTH = 200;
  Object.keys(utm).forEach(key => {
    if (typeof utm[key] === 'string' && utm[key].length > MAX_LENGTH) {
      utm[key] = utm[key].substring(0, MAX_LENGTH);
    }
  });
  
  // Remover valores vacíos
  Object.keys(utm).forEach(key => {
    if (!utm[key]) delete utm[key];
  });
  
  return utm;
}
```

---

## 6. GDPR / PRIVACY CROSS-PLATFORM

### 6.1 Requerimientos Legales Innovart

#### **Colombia (Ley 1581/2012 - LSPDP)**

- ✅ **Consentimiento previo** para procesar datos personales (formularios, tracking)
- ✅ **Derecho a conocer**, actualizar, rectificar datos
- ✅ **Derecho al olvido** (erasure) — borrar perfil + datos asociados
- ✅ **Política de privacidad** obligatoria (publicada, accesible)
- ✅ **Identificación del responsable**: Innovart Medical IPS
- ✅ **Contacto privacidad** público: innovartmedicalips@gmail.com

**Penalidades**: COP $50M-$300M por violación

#### **Panamá (Ley 81/2013 - Derecho a la Privacidad)**

- ✅ Consentimiento informado
- ✅ Notificación en caso de breach (within 5 days)
- ⚠️ Más flexible que GDPR
- ✅ Derechos de acceso y rectificación

#### **GDPR (Si tráfico EU)**

- ✅ Consentimiento granular (analytics, marketing, etc.)
- ✅ Cookie banners
- ✅ Data Processing Agreement (DPA)
- ✅ Derecho al olvido

### 6.2 Herramientas Consent Management

#### **Comparativa**

| Herramienta | Soporte LSPDP | Costo | API | Recomendado |
|---|---|---|---|---|
| **Consentio** | ✅ Nativo | Freemium + $5-15/mes | ✅ | ⭐ INNOVART |
| **Cookiebot** | ✅ | €50-400/año | ✅ | ✅ Alternativa |
| **Termly** | ✅ | $99-499/año | ✅ | ✅ |
| **OneTrust** | ✅ | Enterprise | ✅ | Para grandes |

**Recomendación Innovart**: **Consentio**
- Gratis hasta 50K eventos/mes
- Equipo latam, soporte en español
- 1-click integración Shopify
- LSPDP-compliant

### 6.3 Setup Consentio

1. **Registrar**:
   - https://consentio.app/es
   - Email: innovartmedicalips@gmail.com
   - Configurar para: Colombia + Panamá

2. **Crear política de privacidad**:
   - Responde cuestionario del asistente Consentio
   - Publica URL en footer

3. **Instalar snippet** en Shopify:
   - Theme Editor → Edit code → theme.liquid
   - Antes de `</head>`:
   ```html
   <script async src="https://cdn.consentio.app/v2/consent.js"></script>
   <script>
     window.consentioConfig = {
       siteKey: "YOUR_SITE_KEY",
       lang: "es",
       position: "bottom-left",
       categories: {
         necessary: {
           label: "Necesarias",
           description: "Requeridas para funcionamiento",
           required: true
         },
         analytics: {
           label: "Analítica",
           description: "Google Analytics 4, Microsoft Clarity",
           scripts: ["Google Analytics", "Clarity"]
         },
         marketing: {
           label: "Marketing",
           description: "Meta Pixel, retargeting",
           scripts: ["Meta Pixel", "Google Ads"]
         }
       }
     };
   </script>
   ```

4. **Cargar scripts condicionalmente**:
   ```javascript
   // En GTM o tema
   if (typeof consentio !== 'undefined') {
     consentio.onConsent(['marketing'], () => {
       // Cargar Meta Pixel
       !function(f,b,e,v,n,t,s){/* Facebook Pixel code */}(window,window,document,window,"fbq");
     });
   }
   ```

### 6.4 Right-to-Be-Forgotten Workflow

#### **En GHL**:

1. **Crear workflow "GDPR - Delete Contact"**:
   - Trigger: Tag agregado = "gdpr_delete_request"
   - Paso 1: Send email confirmación
   - Paso 2: Wait 72h (tiempo para cancelar)
   - Paso 3: Conditional — Si tag "gdpr_cancel" NO está:
     - Log: "GDPR delete: [nombre] [email]"
     - Delete contact + oportunidades asociadas

2. **Proceso manual**:
   - Cliente email: `innovartmedicalips@gmail.com`
   - Solicitud: "Quiero que borren mis datos"
   - Innovart verifica (últimos 4 dígitos teléfono, etc.)
   - Admin aplica tag "gdpr_delete_request"
   - Workflow ejecuta delete automáticamente después 72h

#### **Script de auditoría**:

```python
#!/usr/bin/env python3
# ghl_audit_deletions.py

import requests
import json
from datetime import datetime

GHL_TOKEN = "YOUR_TOKEN"
HEADER = {"Authorization": f"Bearer {GHL_TOKEN}"}

# Buscar contactos con tag gdpr_delete_request
response = requests.post(
  "https://api.gohighlevel.com/v1/contacts/search",
  headers=HEADER,
  json={"query": "tag:gdpr_delete_request"}
)

contacts = response.json().get("contacts", [])

log = {
  "timestamp": datetime.now().isoformat(),
  "gdpr_deletions": []
}

for contact in contacts:
  log["gdpr_deletions"].append({
    "id": contact["id"],
    "email": contact["email"],
    "name": f"{contact.get('firstName', '')} {contact.get('lastName', '')}",
    "status": "Pending" if contact.get("tag") == "gdpr_delete_request" else "Processed"
  })

print(json.dumps(log, indent=2, ensure_ascii=False))
```

### 6.5 Data Processing Agreement (DPA)

**Checklist si Innovart es responsable de datos**:

- [ ] GHL firma DPA: https://www.gohighlevel.com/terms/dpa
- [ ] Meta firma DPA (vía Business Tools)
- [ ] Google firma DPA (vía Google Ads policies)
- [ ] Cloudflare firma DPA (Data Processing Addendum)
- [ ] Comunicar a equipo: "Procesadores de datos autorizados"

---

## CHECKLIST RÁPIDO DE IMPLEMENTACIÓN

### Fase 1: Foundation (Semana 1)
- [ ] **CAPI Meta**: Verificar token + permisos
- [ ] **Pixels**: GTM instalado (1 contenedor)
- [ ] **UTM**: Captura en landing (localStorage)
- [ ] **GDPR**: Consentio instalado + política publicada

### Fase 2: Integración (Semana 2)
- [ ] **Shopify ↔ GHL**: Webhook + validación E2E
- [ ] **Qikify**: Ruteado a webhook (si no está)
- [ ] **Tracking**: fbclid + gclid capturados
- [ ] **Workflow 4.1**: SMS al lead habilitado en todas sedes

### Fase 3: Optimización (Semana 3-4)
- [ ] **WordPress** (si suma): Gravity Forms + Zapier
- [ ] **GDPR**: Workflow delete automático
- [ ] **Auditoría**: UTM en 100% de ads (Google Ads API)
- [ ] **Testing**: Cross-device, conversión end-to-end

---

## RECURSOS Y LINKS VERIFICADOS

### Documentación Oficial
- 📖 **Shopify Webhooks**: https://shopify.dev/api/admin-rest/2024-10/resources/webhook
- 📖 **GHL API**: https://dev.gohighlevel.com/
- 📖 **Meta CAPI**: https://developers.facebook.com/docs/marketing-api/conversions-api/overview
- 📖 **Google Tag Manager**: https://support.google.com/tagmanager
- 📖 **Qikify Docs**: https://docs.qikify.com/
- 📖 **Consentio**: https://consentio.app/es

### Legislación
- ⚖️ **LSPDP Colombia**: https://www.funcionpublica.gov.co/eva/gestornormativo/
- ⚖️ **Ley 81 Panamá**: https://www.asamblea.gob.pa/
- ⚖️ **GDPR**: https://gdpr-info.eu/

---

## PRÓXIMOS PASOS INMEDIATOS INNOVART

1. ✅ **Hoy**: Verificar token CAPI Meta (curl test)
2. ✅ **Hoy**: Publicar política privacidad + instalar Consentio
3. ✅ **Mañana**: GTM en Shopify (1 contenedor, todos los pixels)
4. ✅ **Semana 1**: Completar audit UTM (APIs Google Ads)
5. ✅ **Semana 2**: WordPress si suma nuevas landings

---

*Documento vivo — actualizar con nuevas integraciones, cambios de legislación, o feedback del equipo.*

