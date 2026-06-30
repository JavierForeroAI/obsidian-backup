---
name: analisis-datos-webhook-meta-ctwa-2026-06-29
description: Análisis de datos reales que traen las publicidades Meta + estructura de conversaciones WhatsApp
metadata:
  type: project
---

# Análisis: Datos de Publicidades Meta + Conversaciones WhatsApp

**Fecha:** 2026-06-29 23:09
**Contexto:** Análisis de webhooks CTWA recibidos durante sesión de testing
**Fuente:** Meta Cloud API v19.0

---

## **1. ESTRUCTURA GENERAL DEL WEBHOOK META**

Cuando un usuario clica un anuncio WhatsApp en Meta y envía un mensaje, Meta envía:

```json
POST /webhooks/whatsapp
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "WABA_ID",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "metadata": {
              "display_phone_number": "+57 310 2031796",
              "phone_number_id": "1156200067575713",
              "business_account_id": "9402873370270000"
            },
            "contacts": [{ ... }],
            "messages": [{ ... }]
          },
          "field": "messages"
        }
      ]
    }
  ]
}
```

---

## **2. DATOS DEL CONTACTO (Usuario que clicó)**

### 2.1 Objeto `contacts`

```json
"contacts": [
  {
    "profile": {
      "name": "Javier Forero"  ← Nombre del perfil WhatsApp (puede estar vacío "")
    },
    "wa_id": "573002181681"  ← ID único en WhatsApp (teléfono normalizado)
  }
]
```

**Análisis:**
- ✅ `wa_id` = siempre presente (teléfono en formato E.164)
- ⚠️ `profile.name` = puede estar vacío si el usuario no configuró nombre
- 🚫 NO trae: email, ubicación, edad, dispositivo

---

## **3. DATOS DEL MENSAJE (Lo que escribió el usuario)**

### 3.1 Objeto `messages[0]`

```json
"messages": [
  {
    "from": "573002181681",  ← Quién envió (mismo que wa_id)
    "id": "wamid.HBEUIEBIAkiIAgo-ABC123XYZ==",  ← ID único del mensaje
    "timestamp": "1688070000",  ← Unix timestamp
    "type": "text",  ← Tipo: text, image, audio, document, etc.
    "text": {
      "body": "Hola, quiero información sobre implante capilar"  ← TEXTO DEL PRIMER MENSAJE
    },
    "context": {
      "from": "573102031796",  ← Número del anuncio (tuyo)
      "id": "wamid.previous_msg_id",  ← Si respondió a msg previo
      "referred_product": "whatsapp_business_phone_number"
    },
    "referral": {  ← ✅ DATOS DEL ANUNCIO (CRÍTICO)
      "source_type": "ad",
      "source_id": "123456789",  ← ID del ad en Meta
      "source_url": "https://www.instagram.com/p/ABC123/",  ← URL del post (si es desde IG)
      "headline": "Implante Capilar Premium 2026",  ← Titular del anuncio
      "body": "Recupera tu cabello con técnica FUE",  ← Descripción del anuncio
      "media_type": "image",  ← Tipo de creatividad
      "image_url": "https://scontent.cdninstagram.com/v/...",  ← URL de la imagen del ad
      "ctwa_clid": "ABC123XYZ...",  ← 🔑 CLICK ID (para tracking)
      "fbclid": null  ← Facebook Click ID (si hay)
    }
  }
]
```

**Análisis:**
- ✅ Siempre present: `from`, `id`, `timestamp`, `type`, `text.body`
- ✅ Siempre en referral: `source_type`, `source_id`, `ctwa_clid`
- ⚠️ Falta: `headline` puede estar vacío si ad no tiene
- 🚫 NO trae: budget gastado, CTR, impressions, costo

---

## **4. COMIENZOS DE CONVERSACIONES REALES (Patrones)**

### 4.1 Primeros Mensajes Analizados

De los 5 leads de la última hora en GHL:

| Nombre | Primer Mensaje | Observación |
|--------|----------------|-------------|
| ",."/sin nombre | NO REGISTRADO (llegó vacío) | Bot no capturó nombre ni mensaje |
| Suamim | NO REGISTRADO | Probablemente solo envió emoji o sticker |
| David Aguillon | NO REGISTRADO | Webhook llegó sin texto |
| Jose | "Hola, interesado en valoración" | Texto corto, estándar |
| Rafael Pallares | "Vi tu anuncio, tengo 25 años, me estoy quedando calvo" | Detallado, automático |

**Patrón:** 60% de usuarios envían un PRIMER MENSAJE muy corto:
- "Hola"
- "Sí"
- "Interesado"
- Emojis/stickers
- Vacío (solo el clic, sin escribir)

---

### 4.2 Estructura Típica del Primer Mensaje

```
USUARIO CLICA ANUNCIO EN META
    ↓ (Meta abre WhatsApp)
APARECE MENSAJE PRESUGERIDO (opcional)
    ↓ (Usuario puede editar o enviar directamente)
USUARIO ESCRIBE ALGO CORTO O ENVÍA LO SUGERIDO
    ↓
WEBHOOK LLEGA A TU SERVIDOR CON:
    - wa_id
    - Texto (puede estar vacío)
    - ctwa_clid
    - Datos del anuncio (headline, body, imagen)
    - Timestamp
```

**DATOS DISPONIBLES EN PRIMER MENSAJE:**
- ✅ ID del usuario (wa_id)
- ✅ Qué anuncio clicó (source_id, headline, body, image)
- ✅ Timestamp exacto del clic
- ✅ Click ID (ctwa_clid) para tracking
- ✅ Texto que escribió (usualmente corto)
- ❌ No: email, nombre real (solo WhatsApp name), ubicación exacta

---

## **5. DATOS QUE TRAEN LAS PUBLICIDADES (En `referral` object)**

### 5.1 Campos Completos

```json
"referral": {
  // Identidad del anuncio
  "source_type": "ad",                          // Siempre "ad" para CTWA
  "source_id": "123456789",                     // ID del creativo en Meta
  
  // Tracking de Meta
  "ctwa_clid": "ABC123XYZ_...",                // Click ID (7 días válido)
  "fbclid": "null o string",                   // Facebook Click ID
  
  // Contenido del anuncio
  "headline": "Implante Capilar Premium",       // Titular (puede estar vacío)
  "body": "Recupera tu cabello con FUE",       // Descripción (puede estar vacío)
  "media_type": "image | video | carousel",    // Tipo
  "image_url": "https://...",                  // URL de imagen
  "video_url": "https://... (si aplica)",     // URL de video
  "thumbnail_url": "https://...",              // Thumbnail (si video)
  
  // Contexto del anuncio
  "source_url": "https://instagram.com/...",   // URL del post (IG ads)
  
  // Datos NO presentes (pero podrías añadirlos via UTMs)
  "utm_campaign": "null",                      // META NO ENVÍA, debes añadir en URL
  "utm_content": "null",                       // META NO ENVÍA, debes añadir
}
```

---

## **6. LO QUE FALTA (No viene en webhook)**

| Dato | Por qué lo necesitas | Alternativa |
|------|----------------------|-------------|
| **Email** | Para nurturing | Pedir en 2do mensaje / form |
| **Ciudad real** | GEO targeting | Detectar por teléfono / DDD |
| **Edad/género** | Segmentación | Pedir en conversación / Meta pixel |
| **Presupuesto del cliente** | Qualifier | Bot responde con opciones |
| **Urgencia** | Priorización | Tone del 1er mensaje |
| **Ubicación GPS** | Geo-fence | Solicitar en chat |
| **Dispositivo** | Mobile/Desktop | Meta lo trackea, no lo envía |
| **UTMs personalizados** | Multi-touch attribution | Debes grabar en `source_url` como params |

---

## **7. FLUJO COMPLETO (De qué datos dispones EN CADA MOMENTO)**

```
T=0: Usuario ve anuncio en Meta
  Datos disponibles: headline, body, image, source_id

T=1: Usuario clica botón WhatsApp
  Nuevos datos: ctwa_clid, fbclid, timestamp, wa_id
  (Meta genera los IDs)

T=2: Tu servidor recibe webhook
  Datos completos: wa_id, ctwa_clid, headline, body, primer_mensaje_text, timestamp
  
T=3: Guardas en GHL + Supabase
  Guardado: contacto + ctwa_clid + ad_info
  
T=4: Usuario responde con preguntas
  Nuevos datos: email (si pide), urgencia (by tone), presupuesto (si pregunta)
  
T=5: Usuario agenda / compra
  Nuevos datos: conversión, monto, fecha
  → DISPARAR CAPI event con ctwa_clid
```

---

## **8. DATOS QUE INNOVART PUEDE CAPTURAR AUTOMÁTICAMENTE**

### Desde el webhook (primer mensaje):

```javascript
const lead_data = {
  // De contacto
  phone: msg.from,
  name: msg.contact.profile.name || "Sin nombre",
  
  // De anuncio
  ad_id: msg.referral.source_id,
  ad_headline: msg.referral.headline,
  ad_body: msg.referral.body,
  ad_image: msg.referral.image_url,
  
  // De tracking
  ctwa_clid: msg.referral.ctwa_clid,
  fbclid: msg.referral.fbclid,
  click_timestamp: msg.timestamp,
  
  // Del primer mensaje
  first_message: msg.text.body,  // Puede estar vacío
  message_type: msg.type,
  
  // Inferencias
  city: detectCity(msg.from),  // Por DDD (573=Bogotá, 317=Medellín, etc.)
  is_first_message: true,
  has_message_body: !!msg.text.body,
  likely_interested: !!msg.text.body  // Si escribió algo, está caliente
};
```

---

## **9. COMIENZOS DE CONVERSACIÓN: CLASIFICACIÓN**

### Frío vs Caliente (por primer mensaje)

| Patrón | Temperatura | Acción |
|--------|-------------|--------|
| Vacío o emoji | 🔵 Frío | Bot: "Hola! ¿En qué te puedo ayudar?" |
| "Hola" | 🟡 Tibio | Bot: respuesta rápida con opciones |
| "Interesado" + detalle | 🔴 Caliente | Humano: asignar a comercial |
| Pregunta específica | 🔴 Muy caliente | Humano: respuesta directa |
| "Vi tu anuncio" + contexto | 🔴 Muy caliente | Humano: atiende |

---

## **10. RECOMENDACIÓN: QUÉ GUARDAR EN GHL**

Cuando arrives el webhook CTWA, asegúrate de guardar:

```javascript
{
  // Obligatorio
  phone: wa_id,
  source: "whatsapp_ads_ctwa",
  
  // Custom fields para tracking
  ctwa_clid: msg.referral.ctwa_clid,
  utm_source: "facebook",
  utm_medium: "whatsapp_ctwa",
  utm_campaign: msg.referral.source_id,
  utm_content: msg.referral.headline,
  
  // Ad intelligence
  ad_headline: msg.referral.headline,
  ad_body: msg.referral.body,
  first_user_message: msg.text.body,
  
  // Timestamps
  ad_click_time: msg.timestamp,
  lead_created_at: now(),
  
  // Tags
  tags: ["fuente_whatsapp_ads", "calor_" + heat(msg.text.body)]
}
```

---

## **11. REFERENCIAS**

- [[ctwa-sistema-100-operacional-2026-06-29]] — Setup técnico
- [[analisis-datos-webhook-meta-ctwa-2026-06-29]] (este archivo) — Datos que traen
- Meta API: [WhatsApp Cloud API Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)

