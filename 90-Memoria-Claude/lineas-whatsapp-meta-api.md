---
name: lineas-whatsapp-meta-api
description: Números de WhatsApp API (Meta) y CRM AppLevel por sede — líneas activas para pautar y para CRM
metadata:
  type: reference
---

# Líneas activas Innovart — WhatsApp API y CRM

> Fuente: [Google Doc](https://docs.google.com/document/d/1TYX18EuxmSzemvnX5Ave7JLJZ7LA0ORuogxNX94vPJE/edit) — actualizado 2026-06-21

**"Celulares activos son líneas para pautar en Meta."**

## APIs (líneas para pauta en Meta)

| Sede | Número API |
|---|---|
| Barranquilla | 3132754191 |
| Bogotá | 3102031796 |
| Medellín | 317 1224977 |
| Panamá | +507 6507-6869 |

## WhatsApp Business — CRM AppLevel

| Sede / Cuenta | Número CRM |
|---|---|
| CRM Principal (AppLevel) | +57 312 456 5014 |
| CRM AppLevel Panamá | +507 6773-1244 |
| CRM AppLevel Barranquilla | 3213047786 |
| CRM AppLevel Medellín | 573171224974 |
| CRM AppLevel Bogotá | 573208167253 |

## Análisis de calidad por canal — Bogotá (2026-06-28)

| Canal | Número | Tipo | Recibe pauta Meta | Read receipts |
|---|---|---|---|---|
| BOGOTA MAIN PRINCIPAL | 573208167253 (CRM AppLevel) | WhatsApp Plugins (QR) | ✅ SÍ — llegan con Facebook Ad Data payload | ❌ Solo "delivered" |
| GHL Nativo | +57 310 2031796 | LC WhatsApp (API oficial) | ❌ No directamente | ✅ "read" (doble check azul) |

**Hallazgo clave (2026-06-28):** Todos los leads de click-to-DM de Meta Ads llegan al canal BOGOTA MAIN PRINCIPAL (AppLevel), pero ese canal no confirma si el lead leyó el mensaje. El canal nativo GHL (310 2031796) confirma lectura pero no recibe los leads de pauta.

**Recomendación pendiente:** Migrar el enlace de Meta Ads al número nativo +57 310 2031796 para obtener read receipts reales + compatibilidad CAPI + sin riesgo de ban (QR viola TdS de Meta).

⚠️ `BOGOTA MAIN PRINCIPAL` provider ID en GHL: `628f88b07cf43a7641c58089`

## Notas

- Las líneas API son las que se usan para pautar en Meta Ads (Click-to-WhatsApp).
- Las líneas CRM AppLevel son las que reciben y gestionan conversaciones en GHL.
- Ver [[referencia-ghl-cuentas-innovart]] para los IDs de subcuentas correspondientes.
- Ver [[whatsapp-templates-sistema]] para gestión de templates por línea.
- Ver [[feedback-whatsapp-applevel-sms]] para el comportamiento de AppLevel en GHL triggers.
