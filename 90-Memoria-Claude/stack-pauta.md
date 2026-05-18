---
name: stack-pauta-innovart
description: Stack técnico, canal de pauta principal y estructura de CRM de Innovart
metadata:
  type: project
---

# Stack de pauta y tecnología — Innovart

## Canal de adquisición primario
**Meta Ads → WhatsApp** (confirmado vía tags GHL: "[whatsapp] - fb ads", "lead de facebook forms [ciudad]")

- Formato: Facebook Lead Forms por ciudad
- Destino: WhatsApp Business (integrado con GHL)
- Placement dominante: Instagram
- Estructurado como cold traffic / warm traffic separados por ciudad
- Naming: `data-[cold/warm]-traffic-standard-[ciudad]-[objetivo]-abo-[fecha]`

## AI bot
GHL AI activado por defecto en ~73% de leads nuevos. Se pausa (~38% "ai_parar") cuando el agente humano toma el caso.

## CRM
GoHighLevel con 6 subcuentas:
- NPhQTmLOHd6FbDtqLPnG — Cuenta Raíz
- DgjjDzD9nkCKv8AGF1Qb — Bogotá
- h8DplQKVE6epDbbj5Kg8 — Medellín
- cXH8KbMaAPGzkmf3Z2pP — Barranquilla
- 45SKYgIDgr4Eh6a6JcFz — Panamá
- s40Wa8mXYBxlFCieKohO — Bucaramanga (nueva, 0 oportunidades)

## Otros componentes
- Shopify (web) — 5-6 páginas indexadas, bajo SEO
- Google Sheets en Drive — calendarios de valoraciones manuales
- Google Drive — fotos de pacientes (proceso manual)
- MeddiPay — financiación (integrado como etapa en pipeline)

## Gaps de tracking
- Pixel Meta: no confirmado
- CAPI: no confirmado
- GA4: no confirmado
- Google Ads: no hay evidencia de uso activo

**Why:** Observado 2026-05-18 vía GHL MCP + Drive + Web.
**How to apply:** Asumir Meta Ads como canal único confirmado. No asumir tracking web correcto sin confirmar con cliente. GHL es la fuente de verdad de leads.
