---
name: Shopify-GHL Integration — Guía Completa
description: Webhooks, CAPI, lead sync, order data, field mapping, ejemplos
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Shopify-GHL Integration — Guía Completa

## 1. Introducción a Shopify-GHL

**Integración:** Shopify (ecommerce) → GHL (CRM).

**Flujos:**
- Customer signup → crear contacto en GHL
- Form submission → crear oportunidad de venta
- Order placed → actualizar contacto con datos de compra
- Lead info entra → GHL → workflow automático

---

## 2. GHL Shopify App

### Instalar App en Shopify

```
Shopify Admin → Apps and Sales Channels → App Store 
→ Buscar "GoHighLevel" → Instalar
```

### Conectar con GHL Account

1. Después de instalar, click "Add app"
2. Autorizar que Shopify acceda a GHL
3. Seleccionar GHL Account y Location
4. Confirmar

---

## 3. Webhook Setup — Shopify → GHL

### Crear Webhook en Shopify

```
Shopify Admin → Settings → Notifications → Webhooks
```

**Crear webhook para Customer Created:**

```
Topic: customer/created
Format: JSON
URL: https://webhook.gohighlevel.com/incoming-webhook/your-secret
```

**Crear webhook para Order Created:**

```
Topic: order/created
Format: JSON
URL: https://webhook.gohighlevel.com/incoming-webhook/your-secret
```

### Estructura de Payload — Customer

```json
{
  "customer": {
    "id": 123456,
    "email": "customer@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1234567890",
    "tags": ["vip", "email-subscriber"],
    "addresses": [
      {
        "address1": "123 Main St",
        "city": "Bogotá",
        "province": "Cundinamarca",
        "zip": "110111",
        "country": "CO"
      }
    ],
    "created_at": "2026-06-30T10:00:00-05:00",
    "updated_at": "2026-06-30T10:00:00-05:00"
  }
}
```

### Estructura de Payload — Order

```json
{
  "order": {
    "id": 987654,
    "email": "customer@example.com",
    "customer": {
      "id": 123456,
      "email": "customer@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": "+1234567890"
    },
    "line_items": [
      {
        "id": 1,
        "variant_id": 456,
        "title": "Product Name",
        "quantity": 2,
        "price": "99.99",
        "total": "199.98"
      }
    ],
    "total_price": "199.98",
    "currency": "USD",
    "financial_status": "paid",
    "fulfillment_status": "unshipped",
    "created_at": "2026-06-30T10:30:00-05:00"
  }
}
```

---

## 4. Manual Integration — Webhook Receiver en GHL

### GHL Webhook Receiver

En GHL → Webhooks → Crear webhook receptor:

```
API Endpoint: https://your-ghl-instance.gohighlevel.com/webhooks/incoming
Secret: your_webhook_secret
```

---

## 5. Field Mapping — Shopify → GHL

**Mapping automático de campos:**

| Shopify | GHL Custom Field | Tipo |
|---------|------------------|------|
| `customer.email` | `email` | Email |
| `customer.phone` | `phone_number` | Phone |
| `customer.first_name` | `firstName` | Text |
| `customer.last_name` | `lastName` | Text |
| `customer.created_at` | `date_created` | Date |
| `order.total_price` | `ltv` (Lifetime Value) | Number |
| `order.id` | `last_order_id` | Text |

### Custom Field IDs en Innovart

```json
{
  "email": "email",
  "phone_number": "phone",
  "firstName": "first_name",
  "lastName": "last_name",
  "source": "c_source",
  "utm_source": "utm_source",
  "utm_medium": "utm_medium",
  "utm_campaign": "utm_campaign",
  "fbclid": "fbclid",
  "order_id": "last_order_id",
  "ltv": "lifetime_value",
  "last_purchase_date": "last_purchase_date",
  "product_purchased": "product_purchased"
}
```

---

## 6. Cloudflare Worker — Webhook Processor

**Procesar webhook de Shopify y enviar a GHL:**

```javascript
// /shopify-ghl-webhook (Cloudflare Worker)

export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('OK', { status: 200 });
    }
    
    try {
      // Verificar signature
      const signature = request.headers.get('X-Shopify-Hmac-SHA256');
      if (!verifyShopifySignature(request, env.SHOPIFY_SECRET, signature)) {
        console.warn('❌ Invalid Shopify signature');
        return new Response('Unauthorized', { status: 401 });
      }
      
      const payload = await request.json();
      const topic = request.headers.get('X-Shopify-Topic');
      
      console.log(`Processing ${topic}:`, payload);
      
      let ghlData = {};
      
      // Procesar según topic
      if (topic === 'customer/created') {
        ghlData = mapCustomerToGHL(payload.customer);
      } else if (topic === 'order/created') {
        ghlData = mapOrderToGHL(payload.order);
      } else if (topic === 'customer/updated') {
        ghlData = mapCustomerToGHL(payload.customer);
      }
      
      // Enviar a GHL
      const ghlResponse = await sendToGHL(ghlData, env);
      
      console.log('✅ GHL response:', ghlResponse);
      
      return new Response(JSON.stringify({ success: true }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
      
    } catch (error) {
      console.error('❌ Error:', error);
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500
      });
    }
  }
};

// Mapear customer de Shopify a GHL
function mapCustomerToGHL(customer) {
  const address = customer.addresses?.[0] || {};
  
  return {
    firstName: customer.first_name || 'Lead',
    lastName: customer.last_name || '',
    email: customer.email,
    phone: customer.phone || '',
    address: address.address1,
    city: address.city,
    state: address.province,
    postalCode: address.zip,
    country: address.country,
    tags: ['shopify_customer', ...customer.tags],
    customFields: {
      'shopify_customer_id': customer.id?.toString(),
      'shopify_created': customer.created_at,
      'source': 'shopify'
    }
  };
}

// Mapear order de Shopify a GHL
function mapOrderToGHL(order) {
  const customer = order.customer || {};
  
  return {
    firstName: customer.first_name || 'Lead',
    lastName: customer.last_name || '',
    email: customer.email || order.email,
    phone: customer.phone || '',
    tags: ['shopify_customer', 'shopify_buyer'],
    customFields: {
      'shopify_customer_id': customer.id?.toString(),
      'last_order_id': order.id?.toString(),
      'last_order_total': order.total_price,
      'last_order_status': order.financial_status,
      'last_order_date': order.created_at,
      'source': 'shopify_order'
    }
  };
}

// Enviar a GHL
async function sendToGHL(data, env) {
  const url = `https://rest.gohighlevel.com/v1/contacts/upsert`;
  
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.GHL_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      ...data,
      locationId: env.GHL_LOCATION_ID
    })
  });
  
  if (!response.ok) {
    throw new Error(`GHL error: ${response.status}`);
  }
  
  return response.json();
}

// Verificar firma de Shopify
function verifyShopifySignature(request, secret, signature) {
  const crypto = require('crypto');
  const body = request.body;
  const hash = crypto.createHmac('sha256', secret).update(body).digest('base64');
  return hash === signature;
}
```

---

## 7. GHL API — Crear/Actualizar Contactos

### REST API — Crear Contacto

```bash
curl -X POST https://rest.gohighlevel.com/v1/contacts/ \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "phone": "+573101234567",
    "locationId": "YOUR_LOCATION_ID",
    "tags": ["shopify", "web_lead"],
    "customFields": {
      "utm_source": "google",
      "utm_medium": "cpc",
      "utm_campaign": "summer_sale"
    }
  }'
```

### Python SDK

```python
import requests

def create_ghl_contact(data, api_key, location_id):
    """Crear contacto en GHL"""
    
    url = "https://rest.gohighlevel.com/v1/contacts/"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "firstName": data.get('firstName', 'Lead'),
        "lastName": data.get('lastName', ''),
        "email": data.get('email', ''),
        "phone": data.get('phone', ''),
        "locationId": location_id,
        "tags": data.get('tags', ['web_lead']),
        "customFields": data.get('customFields', {})
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 201:
        raise Exception(f"GHL error: {response.status_code} {response.text}")
    
    return response.json()

# Uso
contact = create_ghl_contact(
    data={
        'firstName': 'John',
        'lastName': 'Doe',
        'email': 'john@example.com',
        'phone': '+573101234567',
        'tags': ['shopify', 'buyer'],
        'customFields': {
            'order_id': '123456',
            'ltv': '299.99'
        }
    },
    api_key='YOUR_API_KEY',
    location_id='YOUR_LOCATION_ID'
)

print(contact)
```

---

## 8. Sincronización de Órdenes

### Crear Opportunity al Completar Orden

```javascript
// En GHL Workflow

Trigger: Webhook from Shopify (order/created)

Action 1: Create Contact (si no existe)
  - Email: {{ order.email }}
  - Phone: {{ order.customer.phone }}
  - Tags: ['shopify_buyer']

Action 2: Create Opportunity
  - Name: "Order #{{ order.id }}"
  - Value: {{ order.total_price }}
  - Stage: "Won"
  - Custom Fields:
    - order_id: {{ order.id }}
    - product_names: {{ order.line_items[0].title }}
    - order_status: {{ order.financial_status }}

Action 3: Send Email
  - Template: "Order Confirmation"
  - To: {{ order.email }}

Action 4: Create Task
  - Title: "Follow up order #{{ order.id }}"
  - Assign to: [Sales Owner]
  - Due date: +7 days
```

---

## 9. Sincronización de Leads vía Form

**Flujo: Shopify Form → Qikify/GHL Form → Webhook → GHL Contact + Workflow**

```javascript
// En Qikify (custom code)

document.addEventListener('DOMContentLoaded', function() {
  if (typeof window.BContact !== 'undefined') {
    const originalSend = window.BContact.send;
    
    window.BContact.send = function(data) {
      // Enriquecer con UTMs
      const params = new URLSearchParams(window.location.search);
      
      const enrichedData = {
        ...data,
        utm_source: params.get('utm_source') || '',
        utm_medium: params.get('utm_medium') || '',
        utm_campaign: params.get('utm_campaign') || '',
        fbclid: sessionStorage.getItem('fbclid') || '',
        page_url: window.location.href
      };
      
      // Enviar webhook a GHL
      fetch('/api/qikify-webhook', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(enrichedData)
      });
      
      return originalSend(enrichedData);
    };
  }
});
```

---

## 10. Tag Propagation — Shopify → GHL

```javascript
// Mapear tags de Shopify a GHL

const tagMapping = {
  'vip': 'vip_customer',
  'returning-customer': 'returning_customer',
  'abandoned-cart': 'cart_abandoned',
  'pre-order': 'pre_order',
  'sale': 'sale_customer'
};

function mapTags(shopifyTags) {
  return shopifyTags.map(tag => tagMapping[tag] || tag);
}

// Uso
const ghlTags = mapTags(['vip', 'returning-customer']);
// ['vip_customer', 'returning_customer']
```

---

## 11. Troubleshooting Shopify-GHL Integration

### Problema: Webhook no llega a GHL

**Solución:**
1. Verificar URL del webhook en Shopify
2. Verificar que el servidor responde 200 OK
3. Revisar logs en Shopify → Notifications → Webhooks

### Problema: Custom fields no se syncan

**Solución:**
1. Verificar que los custom fields existen en GHL
2. Verificar mapping de field IDs
3. Revisar logs en GHL API responses

### Problema: Duplicados de contactos

**Solución:**
```javascript
// Usar upsert en lugar de create
// Upsert busca por email y actualiza si existe

const response = await fetch('https://rest.gohighlevel.com/v1/contacts/upsert', {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${api_key}` },
  body: JSON.stringify({
    email: 'john@example.com',  // Clave de búsqueda
    firstName: 'John',
    lastName: 'Doe'
    // Si email existe, actualiza. Si no, crea.
  })
});
```

---

## 12. Resumen de Flujos en Innovart

```
FLUJO 1: Customer Registration
  Shopify (customer/created) 
    → Webhook 
    → Cloudflare Worker 
    → GHL (create contact)
    → Workflow: Send welcome email

FLUJO 2: Order Purchase
  Shopify (order/created)
    → Webhook
    → Cloudflare Worker
    → GHL (create opportunity)
    → Workflow: Send receipt + follow-up

FLUJO 3: Web Lead (Landing)
  Qikify Form Submit
    → Webhook
    → Cloudflare Worker
    → GHL (create contact + opportunity)
    → Workflow: Sales pipeline initiation
```

---

## 13. GHL Webhook Secret Management

```javascript
// En Cloudflare Worker environment

[env.secrets]
GHL_API_KEY = "sk_test_xxxxx"
GHL_LOCATION_ID = "xxxxx"
SHOPIFY_WEBHOOK_SECRET = "xxxxx"
```

---

## 14. Recursos Oficiales

- [GHL REST API Docs](https://docs.gohighlevel.com/api/)
- [GHL Contacts Endpoint](https://docs.gohighlevel.com/api/#contacts)
- [Shopify Webhooks](https://shopify.dev/api/admin-rest/2024-01/resources/webhook)
- [GHL Integrations](https://help.gohighlevel.com/article/integrations)

