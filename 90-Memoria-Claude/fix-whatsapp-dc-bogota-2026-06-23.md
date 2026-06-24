---
name: fix-whatsapp-dc-bogota-2026-06-23
description: Cambio de número WhatsApp en páginas dc1-bta y dc2-bta del funnel DC-BOGOTA — de línea 320 (dada de baja) a línea 310 (nueva Bogotá)
metadata:
  type: project
---

# Fix WhatsApp dc-bogota — 2026-06-23

**Why:** La línea +57 320 865 3730 fue dada de baja en Bogotá y reemplazada por +57 310 203 1796 (registrada en Meta API).

**How to apply:** Si se crean nuevas páginas en el funnel DC-BOGOTA, verificar siempre que el botón WhatsApp apunte a `wa.me/573102031796`.

## Cambio realizado

| Campo | Valor anterior | Valor nuevo |
|---|---|---|
| Número | +57 320 865 3730 | +57 310 203 1796 |
| URL WA | `wa.me/573208653730` | `wa.me/573102031796` |
| Texto predef. | `Si asistire` | sin cambio |

## Páginas actualizadas

- **dc1-bta** (page ID `Wqiefcabe64SGbRtEs04`) — cambiado y payload JSON preparado
- **dc2-bta** (page ID `JzVD6F6znAGbvhwyb0KV`) — cambiado y publicado vía MCP GHL

**Funnel:** DC-BOGOTA (`b0uikUkMLWlADpxoQW7M`)
**Location GHL:** Innovart Medical IPS Bogota (`DgjjDzD9nkCKv8AGF1Qb`)
**URL pública del funnel:** `https://implantecapilarencolombia.com/dc2-bta`

## Nota

El cambio de dc1-bta se preparó como JSON pero la publicación vía MCP `update_page_content` puede no persistir (ver [[feedback-mcp-ghl-update-page]]). Verificar en editor visual si dc1-bta quedó actualizado.

## Contexto de líneas

Ver [[lineas-whatsapp-meta-api]] para el mapa completo de líneas activas por sede.
