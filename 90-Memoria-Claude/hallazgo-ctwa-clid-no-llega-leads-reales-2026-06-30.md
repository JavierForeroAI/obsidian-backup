---
name: hallazgo-ctwa-clid-no-llega-leads-reales-2026-06-30
description: 🚨 CRÍTICO — ctwa_clid NO se está poblando en leads reales de WhatsApp Ads (aunque test webhook pasó). 5 leads últimas 2h con fuente WhatsApp Ads pero sin ctwa_clid ni UTMs.
metadata:
  type: project
---

## Hallazgo

**Fecha:** 2026-06-30 · **Hora:** ~01:09 UTC (última verificación en GHL)

### Síntoma
Test webhook de ctwa_clid **SÍ funciona** (webhook llega a Worker, contacto se crea en GHL).
Pero leads **reales** de WhatsApp Ads en última 1h NO tienen ctwa_clid poblado:

| Sede | Contacto | Teléfono | Hora UTC | Origen | ctwa_clid | Acción |
|------|----------|----------|----------|--------|-----------|--------|
| Bogotá | ",."/sin nombre | +573112210215 | 02:06:32 | WhatsApp Ads | ❌ NO | [whatsapp]-lead capture |
| Bogotá | Suamim | +573187386729 | 01:42:48 | WhatsApp Ads | ❌ NO | [whatsapp]-lead capture |
| Bogotá | David Aguillon | +573124320661 | 01:32:34 | WhatsApp Ads | ❌ NO | [whatsapp]-lead capture |
| Barranquilla | 2 leads | — | 01:00–01:20 | Lead API | ❌ NO | lead de api |
| Medellín & Panamá | 0 | — | — | — | — | (sin leads última 1h) |

### Causa probable

1. **Meta webhook NO está disparándose** — clicks de WhatsApp Ads no envían webhook a `innovart-wa-redirect-320`
2. **O webhook llega pero va a location incorrecta** — campo ctwa_clid no se mapea bien por sede
3. **O Worker tiene bug silencioso** — recibe pero no guarda (aunque curl test OK)

### Crítico para

- **CAPI training:** Sin ctwa_clid, no podemos vincular "clic WhatsApp Ads → lead → conversión" en Meta
- **Attribution:** EMQ (Email Match Quality) sigue bajo (4.9) porque falta fbclid + ctwa_clid
- **Show Rate:** Conversión de ads clickeados a appointments sigue ciega

---

## Estado del Sistema (verificado 2026-06-30)

| Componente | Estado | Verificación |
|---|---|---|
| Worker Cloudflare | ✅ VIVO | `curl` test OK, crea contactos |
| Meta webhook config | ⚠️ NO VERIFICADO | ¿Está disparando? ¿A qué URL? |
| GHL field ctwa_clid | ✅ Existe | ID `—` (revisar MCP) |
| Líneas WhatsApp | ✅ Activas | 4 números (310/317/313, 507 650) en uso |
| Test manual webhook | ✅ OK | 4 contactos test 2026-06-29 sí llegaron |
| **Leads reales** | ❌ FALLA | 0/5 últimas 2h con ctwa_clid |

---

## Próximos pasos

**P0 (hoy):**
1. ¿Meta webhook está configurado? Verificar en Meta Business Manager → Webhooks → URL destino
2. ¿A cuál Worker/URL apunta la configuración?
3. ¿El Worker recibe POST o falla silenciosamente?

**P1 (mañana si no es webhook):**
1. Revisar logs Cloudflare de `innovart-wa-redirect-320` (últimas 2h)
2. Buscar errores o requests bloqueados
3. Confirmar que phone_number_ids por sede están correctos

**P2:**
1. Una vez identificada causa raíz, resetear training en Meta (EMQ debería subir)

---

**Why:** Sin ctwa_clid de leads reales, CAPI no puede aprender dónde vienen conversiones → show rate 40% sigue bloqueado.

**How to apply:** Resolver antes de escalar pauta WhatsApp Ads o hacer cambios en landing pages.
