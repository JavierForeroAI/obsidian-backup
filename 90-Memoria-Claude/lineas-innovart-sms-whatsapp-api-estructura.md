---
name: lineas-innovart-sms-whatsapp-api-estructura
description: Estructura completa de líneas SMS y WhatsApp API por sede — 2 líneas independientes por ciudad
metadata:
  type: reference
---

# Líneas Innovart — SMS vs WhatsApp API

**Última actualización:** 2026-06-29 17:15

---

## **REGLA FUNDAMENTAL**

Cada sede tiene **DOS LÍNEAS INDEPENDIENTES** con **DOS FLUJOS DIFERENTES**:

1. **SMS** — LeadConnector (GHL) — flujo SMS nativo
2. **WhatsApp API** — Meta Ads (CTWA) — flujo webhooks Meta → GHL

**NUNCA MEZCLAR.** Cada una tiene su propia configuración, field IDs, y workflow.

---

## **SMS — LeadConnector (GHL)**

**Reciben leads de:** Llamadas, SMS directo, formularios web, integraciones

| Sede | Número | GHL Alias | Status | Lead Capture | GHL LocationId | Flujo |
|---|---|---|---|---|---|---|
| **Medellín** | `573171224974` | Medellin | ✅ Online | ✅ ON | `h8DplQKVE6epDbbj5Kg8` | SMS independiente |
| **Bogotá** | `573208167253` | BOGOTA MAIN PRINCIPAL | ✅ Online | ✅ ON | `DgjjDzD9nkCKv8AGF1Qb` | SMS independiente |
| **Barranquilla** | `573213047786` | MAIN BARRANQUILLA | ✅ Online | ✅ ON | `cXH8KbMaAPGzkmf3Z2pP` | SMS independiente |
| **Panamá** | `50767731244` | MAIN PANAMA | ✅ Online | ✅ ON | `45SKYgIDgr4Eh6a6JcFz` | SMS independiente |
| **Principal (Bogotá)** | `312` | — | ✅ | — | `NPhQTmLOHd6FbDtqLPnG` | Recibe TODOS leads web innovartmedical.com |

---

## **WhatsApp API — Meta Ads (CTWA)**

**Reciben leads de:** Meta ads (Click-to-WhatsApp), usuario envía mensaje → Webhook Meta → GHL

| Sede | Número Meta | phone_number_id | Integración | Status | GHL LocationId | Flujo | ctwa_clid Field ID |
|---|---|---|---|---|---|---|---|
| **Bogotá** | `+57 310 2031796` | `1156200067575713` | WhatsApp Plugins (type 20) | ✅ Webhook configurado | `DgjjDzD9nkCKv8AGF1Qb` | WhatsApp API (CTWA) | `ebBHQovnCw3AgAij7BAA` |
| **Medellín** | `+57 317 1224977` | `611850088685930` | Cloud API Nativa (type 19) | ✅ Webhook configurado | `h8DplQKVE6epDbbj5Kg8` | WhatsApp API (CTWA) | `4V2IZiwCCkLdt0jTUI8K` |
| **Barranquilla** | `+57 313 2754191` | `625405087319822` | WhatsApp Plugins (type 20) | ✅ Webhook configurado | `cXH8KbMaAPGzkmf3Z2pP` | WhatsApp API (CTWA) | `lr9AYYbE3MKxcbMqGOew` |
| **Panamá** | `+507 650 76869` | `662014553651143` | WhatsApp Plugins (type 20) | ✅ Webhook configurado | `45SKYgIDgr4Eh6a6JcFz` | WhatsApp API (CTWA) | `Ckdb2494518FRWLHLb7n` |

---

## **Webhook Meta (Único para todos)**

**URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/wa-ctwa`

**Verify Token:** `innovart-ctwa-verify-2026`

**Mapeo interno (WA_PHONE_NUMBER_MAP):**
```json
{
  "1156200067575713": "bogota",
  "611850088685930": "medellin",
  "625405087319822": "barranquilla",
  "662014553651143": "panama"
}
```

**Routing:** El Worker detecta `phone_number_id` → obtiene la GHL location correcta → guarda `ctwa_clid` en el field ID correspondiente.

---

## **Flujos en GHL — DOS INDEPENDIENTES**

### **Flujo SMS**
- **Trigger:** Mensaje SMS entrante (línea 312, 573171224974, etc.)
- **Acción:** Crea contacto → Tag `fuente_sms_*` → Workflow SMS
- **Campos:** phone, email, nombre (nativos de SMS)

### **Flujo WhatsApp API (CTWA)**
- **Trigger:** Webhook de Meta con `ctwa_clid`
- **Acción:** Crea contacto → Tag `fuente_whatsapp_ads` → Guarda `ctwa_clid` → Workflow WhatsApp API
- **Campos:** phone, email, nombre + **`ctwa_clid`** (custom field) + utm_source/medium/campaign/content
- **Impacto:** Atribución de lead a anuncio específico en Meta

---

## **Custom Fields — ctwa_clid por GHL location**

Estos son los field IDs donde se guarda el identificador único del clic del anuncio:

| Sede | GHL Location | ctwa_clid Field ID |
|---|---|---|
| Bogotá | DgjjDzD9nkCKv8AGF1Qb | `ebBHQovnCw3AgAij7BAA` |
| Medellín | h8DplQKVE6epDbbj5Kg8 | `4V2IZiwCCkLdt0jTUI8K` |
| Barranquilla | cXH8KbMaAPGzkmf3Z2pP | `lr9AYYbE3MKxcbMqGOew` |
| Panamá | 45SKYgIDgr4Eh6a6JcFz | `Ckdb2494518FRWLHLb7n` |
| Principal (Bogotá) | NPhQTmLOHd6FbDtqLPnG | `ni4PMQh6l93hmoiyfEEY` (utm_term en esta location) |

---

## **Referencias técnicas**

- [[webhook-config-location-meta]] — Dónde está la configuración en Meta + pasos
- [[ctwa-tracking-whatsapp-ads]] — Sistema completo CTWA tracking
- [[plan-b-webhook-revert-bogota]] — Rollback si falla

---

## **CHECKLIST DE CONFIGURACIÓN — ✅ 100% COMPLETO**

- [x] SMS líneas creadas en GHL (4 ciudades + principal)
- [x] WhatsApp API números en Meta (4 ciudades)
- [x] Webhook global configurado en Meta (URL + Token)
- [x] Worker escrito con código CTWA
- [x] **WA_PHONE_NUMBER_MAP configurada en Cloudflare** (2026-06-29)
- [x] **WA_VERIFY_TOKEN configurado en Cloudflare** (2026-06-29)
- [x] **GHL_TOKEN_BOGOTA/MEDELLIN/BARRANQUILLA/PANAMA configurados** (2026-06-29)
- [x] **Documentación completada** (este archivo + MEMORY.md)
- ⏳ **Test E2E real** (próximo: usuario clica anuncio → aparece en GHL con ctwa_clid)

