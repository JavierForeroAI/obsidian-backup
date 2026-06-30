---
name: whatsapp-phone-numbers-meta-api
description: Números de teléfono WhatsApp de Meta API para las 4 sedes de Innovart Medical
metadata:
  type: reference
---

# WhatsApp Phone Numbers — Meta API

**Última actualización:** 2026-06-29

---

## Números de Teléfono WhatsApp (WABA Phone IDs)

| Ciudad | Número WhatsApp | phone_number_id Meta | Integración GHL | Estado |
|---|---|---|---|---|
| **Bogotá** | +57 310 2031796 | `1156200067575713` | WhatsApp Plugins (type 20) | ✅ Activo |
| **Medellín** | +57 317 1224977 | `611850088685930` | Cloud API Nativa (type 19) | ✅ Activo |
| **Barranquilla** | +57 313 2754191 | `625405087319822` | WhatsApp Plugins (type 20) | ✅ Activo |
| **Panamá** | +507 650 76869 | `662014553651143` | WhatsApp Plugins (type 20) | ✅ Activo |
| **Bucaramanga** | — | — | Sin WhatsApp aún | ⏸️ Pendiente |

---

## Webhook Actual (CTWA Tracking)

**URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/wa-ctwa`

**Verify Token:** `innovart-ctwa-verify-2026`

---

## Campos Personalizados GHL (ctwa_clid)

| Ciudad | ctwa_clid Field ID |
|---|---|
| Bogotá | `ebBHQovnCw3AgAij7BAA` |
| Medellín | `4V2IZiwCCkLdt0jTUI8K` |
| Barranquilla | `lr9AYYbE3MKxcbMqGOew` |
| Panamá | `Ckdb2494518FRWLHLb7n` |
| Bucaramanga | `UHB4VHlBQ2XnnZODeGRK` |

---

## API Endpoints (Graph API v20.0)

Formato: `/v20.0/{phone_number_id}/webhook_configuration`

**Ejemplos:**
- Bogotá: `/v20.0/1156200067575713/webhook_configuration`
- Medellín: `/v20.0/611850088685930/webhook_configuration`
- Barranquilla: `/v20.0/625405087319822/webhook_configuration`
- Panamá: `/v20.0/662014553651143/webhook_configuration`

---

## Estado de Cambios Webhook

| Ciudad | Cambio a CTWA | Fecha | Prueba E2E |
|---|---|---|---|
| Bogotá | ⏳ Pendiente | — | — |
| Medellín | ⏳ Pendiente | — | — |
| Barranquilla | ⏳ Pendiente | — | — |
| Panamá | ⏳ Pendiente | — | — |

---

## Notas Importantes

- **Medellín** recibe mensajes DIRECTO via Cloud API nativa — no necesita relay a WhatsApp Plugins
- **Bogotá, Barranquilla, Panamá** usan WhatsApp Plugins — necesitan relay para que GHL reciba conversaciones
- **Bucaramanga** aún no tiene línea de WhatsApp abierta en Meta

---

## Referencias Relacionadas

- [[ctwa-tracking-whatsapp-ads]] — Sistema completo de tracking
- [[plan-b-webhook-revert-bogota]] — Plan de reversión si falla
