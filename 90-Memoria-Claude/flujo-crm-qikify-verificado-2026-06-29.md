---
name: flujo-crm-qikify-verificado-2026-06-29
description: Flujo completo verificado E2E — lead entra por formulario Qikify → GHL. Tags, campos UTM, pipeline y workflows que se activan. Verificado con contacto real en producción.
metadata:
  type: project
  fecha: 2026-06-29
  status: COMPLETADO
---

# Flujo CRM — Lead Qikify → GHL (verificado 29 jun 2026)

## Resultado: Todo el stack funciona

| Componente | Estado |
|---|---|
| Botones WA en landings (5 páginas) | ✅ sufijo `[fb/rtg]` en mensaje |
| Formulario Qikify → Cloudflare Worker → GHL | ✅ contacto creado con UTMs |
| Tags en GHL | ✅ `fuente_web_qikify` + `landing_formulariov2` + `oportunidad ventas frio` |
| Campos UTM | ✅ utm_source / utm_medium / utm_campaign / utm_content / fbclid |
| Workflow activado | ✅ `4.1 Recibir lead de Landing_formulario` (`d405fcaf`) |
| Oportunidad creada | ✅ Pipeline Ventas, etapa Frío |

---

## Flujo paso a paso

```
Lead llena formulario Qikify en innovartmedical.com/pages/implante-capilar-[ciudad]
        ↓
bcontact:beforeFormSubmitted dispara (antes del AJAX de Qikify)
        ↓
JS interceptor en theme.pagefly.liquid / theme.liquid lée UTMs + fbclid de la URL
        ↓
POST a Cloudflare Worker https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead
        ↓
Worker mapea sede → GHL sub-cuenta correcta (por campo dropdown del formulario):
  - "Bogotá"       → GHL Bogotá       (DgjjDzD9nkCKv8AGF1Qb)
  - "Medellin"     → GHL Medellín     (h8DplQKVE6epDbbj5Kg8)
  - "Barranquilla" → GHL Barranquilla (cXH8KbMaAPGzkmf3Z2pP)
  - "Bucaramanga"  → GHL Bucaramanga  (s40Wa8mXYBxlFCieKohO)
  - "Panama"       → GHL Panamá       (45SKYgIDgr4Eh6a6JcFz)
        ↓
Worker crea contacto en sub-cuenta correspondiente con:
  Tags:   fuente_web_qikify  +  landing_formulariov2
  Campos: utm_source, utm_medium, utm_campaign, utm_content, fbclid
  Fuente en GHL: INTEGRATION / OAUTH (aparece así en historial del contacto)
        ↓
GHL detecta tag landing_formulariov2 → dispara workflow:
  "4.1 Recibir lead de Landing_formulario" (ID d405fcaf) — v30, PUBLISHED
        ↓
Workflow hace:
  1. Agrega tag "oportunidad ventas frio"
  2. Crea oportunidad en Pipeline Ventas, etapa Frío
  3. Asigna lead a asesor
```

---

## Tags finales en el contacto

| Tag | Quién lo pone | Momento |
|---|---|---|
| `fuente_web_qikify` | Cloudflare Worker | Al enviar formulario |
| `landing_formulariov2` | Cloudflare Worker | Al enviar formulario |
| `oportunidad ventas frio` | Workflow `4.1 Recibir lead de Landing_formulario` | Automático tras trigger |

---

## Campos UTM en GHL (verificados con datos reales)

| Campo GHL | Valor de prueba | Confirmado |
|---|---|---|
| utm_source | `facebook` | ✅ |
| utm_medium | `paid_social` | ✅ |
| utm_campaign | `test_e2e_bogota_0628` | ✅ |
| utm_content | `video_v1` | ✅ |
| fbclid | `IwARtest_e2e_bogota_0628` | ✅ |

---

## Workflows publicados que pueden activarse

| Workflow | ID | Trigger | Rol |
|---|---|---|---|
| `4.1 Recibir lead de Landing_formulario` | `d405fcaf` | tag `landing_formulariov2` | Crea oportunidad Frío + asigna asesor |
| `Etiqueta Frio` | `f71fe211` | tag `oportunidad ventas frio` | Motor de seguimiento Frío |
| `UTM - WA Directo Tracker` (Bogotá) | `ec3d0cbb` | `customer_reply` + `message.type == 3` | Si el lead responde por WA |
| `CAPI Lead WhatsApp/Ads Bogota` | (en Bogotá) | trigger CAPI | Dispara evento CAPI a Meta |

---

## Notas técnicas

- El contacto aparece con `createdBy.source = "INTEGRATION"` en GHL — correcto, viene del Cloudflare Worker
- `lastMessageType: TYPE_NO_SHOW` en conversación — normal para leads de formulario (no hay mensaje WA aún)
- Conversación tipo `TYPE_PHONE` — GHL crea la conversación por defecto como canal de teléfono hasta que el lead escriba
- ⚠️ Bucaramanga: campos UTM pendientes de crear en esa sub-cuenta (hoy solo llega fbclid)

---

## Archivos relacionados

- [[wa-botones-landings-ciudad-verificado-2026-06-29]] — verificación botones WA
- [[utm-tracking-avance-general]] — estado tracking por fuente
- [[plan-formulario-qikify-innovartmedical]] — arquitectura técnica del Worker
