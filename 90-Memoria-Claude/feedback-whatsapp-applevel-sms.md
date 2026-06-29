---
name: feedback-whatsapp-applevel-sms
description: REGLA CRÍTICA — Innovart tiene DOS líneas de WhatsApp. La de Applevel entra como SMS (type 2/type 20). La de API (Meta Business) es WhatsApp nativo. Ambas reciben pauta.
metadata:
  type: feedback
---

# ⚠️ REGLA PERMANENTE: Dos líneas de WhatsApp — comportamiento diferente en GHL

## Las dos líneas (confirmado 2026-06-28)

| Nombre interno | Conexión | Mensaje en GHL | Trigger filter correcto |
|---|---|---|---|
| **WhatsApp de API** | Meta Business API oficial | WhatsApp nativo (type 19 en trigger) | `Reply channel = WhatsApp` |
| **WhatsApp Business de Applevel** | Applevel ("WhatsApp Plugins") | **SMS** (type 20 / TYPE_CUSTOM_SMS en API; type 2 en trigger) | `Reply channel = SMS` |

**Ambas líneas reciben tráfico de pauta.** Para capturar leads de AMBAS, se necesitan triggers o filtros para los DOS tipos.

## Detalle Applevel

El WhatsApp de Applevel usa proveedor `conversationProviderId: 628f88b07cf43a7641c58089`. Los inbound llegan como **`type: 20` / `messageType: "TYPE_CUSTOM_SMS"`** en la API, pero el trigger filter usa **`message.type == 2` (SMS)**.

**Why:** un trigger que filtre solo por canal WhatsApp (type 19) NUNCA captura los mensajes Applevel. Esto rompió silenciosamente el primer build del flujo de financiación. Aplica a **TODOS los desarrollos, pasados y futuros**.

**How to apply (en cualquier trigger `customer_reply` / "Customer Replied"):**
- **Reply channel = SMS** → en el JSON del trigger: `{"operator":"==","field":"message.type","value":2,"title":"Reply channel","type":"select"}`. (WhatsApp = 19 ❌; **SMS = 2 ✅**.)
- Filtro de cuerpo (forma que guarda la UI): `{"operator":"string-contains-any-of","field":"message.body","value":["<texto>"],"title":"Contains phrase","type":"string"}`.
- Para **responder** al lead sí se usa la acción `send_whatsapp_message` / `whatsapp_v2` con `from_phone_number` = WABA de la sede (eso sale por WhatsApp).
- Verificar un inbound real: en los mensajes, `type:20` + `messageType:"TYPE_CUSTOM_SMS"` = vino por applevel.

Nota: contactos ligados a un usuario (p.ej. el número de Javier `+573002181681`) no aparecen en `search_contacts` por número (quirk), pero sí vía `search_conversations`.

Relacionado: [[flujo-financiacion-bta-capi]] · [[feedback-mcp-ghl-update-page]] · [[stack-pauta]]
