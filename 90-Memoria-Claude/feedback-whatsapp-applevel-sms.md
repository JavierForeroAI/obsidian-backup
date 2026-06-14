---
name: feedback-whatsapp-applevel-sms
description: REGLA CRÍTICA — el WhatsApp de Innovart se maneja por applevel y entra a GHL como SMS (type 20 / TYPE_CUSTOM_SMS), no como WhatsApp
metadata:
  type: feedback
---

# ⚠️ REGLA PERMANENTE: WhatsApp de Innovart entra a GHL como SMS (applevel)

El WhatsApp de Innovart se gestiona con un proveedor **applevel** (marketplace **"WhatsApp Plugins"**, `conversationProviderId: 628f88b07cf43a7641c58089`) que **convierte los mensajes ENTRANTES en SMS dentro de GHL**. Los inbound llegan como **`type: 20` / `messageType: "TYPE_CUSTOM_SMS"`**, NO como WhatsApp.

**Why:** un trigger que filtre por canal WhatsApp NUNCA se dispara, porque GHL ve los mensajes como SMS. Esto rompió silenciosamente el primer build del flujo de financiación (trigger con Reply channel = WhatsApp / `message.type == 19` → no enrolaba). Aplica a **TODOS los desarrollos, pasados y futuros**.

**How to apply (en cualquier trigger `customer_reply` / "Customer Replied"):**
- **Reply channel = SMS** → en el JSON del trigger: `{"operator":"==","field":"message.type","value":2,"title":"Reply channel","type":"select"}`. (WhatsApp = 19 ❌; **SMS = 2 ✅**.)
- Filtro de cuerpo (forma que guarda la UI): `{"operator":"string-contains-any-of","field":"message.body","value":["<texto>"],"title":"Contains phrase","type":"string"}`.
- Para **responder** al lead sí se usa la acción `send_whatsapp_message` / `whatsapp_v2` con `from_phone_number` = WABA de la sede (eso sale por WhatsApp).
- Verificar un inbound real: en los mensajes, `type:20` + `messageType:"TYPE_CUSTOM_SMS"` = vino por applevel.

Nota: contactos ligados a un usuario (p.ej. el número de Javier `+573002181681`) no aparecen en `search_contacts` por número (quirk), pero sí vía `search_conversations`.

Relacionado: [[flujo-financiacion-bta-capi]] · [[feedback-mcp-ghl-update-page]] · [[stack-pauta]]
