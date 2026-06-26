---
name: innovart-landing-utm-ghl
description: Custom fields UTM + Workflow Landing creados en GHL Innovart el 26 jun 2026
metadata: 
  node_type: memory
  type: project
  originSessionId: d61993d3-9bfb-445c-a0bc-2dd5e1d4bae4
---

# GHL Innovart — Landing UTM Integration (26 jun 2026)

**Por qué:** Los leads de landing.com llegan sin UTMs. No se sabe qué campaña/ciudad genera cada lead. Meta EMQ bajo (4.9).
**Cómo aplicar:** Al crear nuevos workflows de otras fuentes, reusar estos mismos custom field IDs.

## Custom Fields UTM creados (location NPhQTmLOHd6FbDtqLPnG)

| Campo | ID | fieldKey |
|-------|----|----------|
| utm_source | `ffBWPx4Qlhxb6D6toNWO` | `contact.utm_source` |
| utm_medium | `46qWfYJubx8IAOhyFlgT` | `contact.utm_medium` |
| utm_campaign | `lPfZB842vcw2a7iD3tOD` | `contact.utm_campaign` |
| utm_content | `hFUkJs1bRuGskcA6X5TA` | `contact.utm_content` |
| utm_term | `ni4PMQh6l93hmoiyfEEY` | `contact.utm_term` |

## Workflow publicado

- **Nombre:** `LANDING - Procesar UTMs y Asignar Lead`
- **ID:** `abcee3aa-0676-40a7-b3f3-9e65430a90b8`
- **Trigger:** tag `fuente_landing` agregado
- **Acciones:** actualiza Lead Source, agrega tags `fuente_landing_wpp` y `utm_pendiente`, nota interna
- **Status:** `published`

## Pendiente (Javier debe hacer)

JS en innovartmedical.com para capturar UTMs de URL y enviarlos a GHL API al click de WhatsApp.
Script completo en: `/Users/javierforero/.claude/workflows/landing-utm-EJECUTADO.md`

## Próximas fuentes a configurar
DM Instagram, DM Facebook, WhatsApp directo, Typeform, Lead Forms Meta — ver [[embudo-completo-crm-innovart]]
