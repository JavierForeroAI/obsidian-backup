---
name: plan-exportacion-leads-principal
description: Plan maestro de exportación de leads desde CRM Principal a sedes — inventario, estado actual, gaps y wishlist
metadata:
  type: project
  última_actualización: 2026-06-28
---

# 🚀 Plan Maestro — Exportación de Leads Principal → Sedes

**Última actualización:** 2026-06-28  
**Estado:** EN INVESTIGACIÓN

---

## 🏗️ CONTEXTO

El CRM Principal (`NPhQTmLOHd6FbDtqLPnG`) es el hub de captación. Todos los leads entran aquí primero. La exportación a sedes (Bogotá, Medellín, Barranquilla, Panamá, Bucaramanga) es el paso crítico para que el comercial de cada ciudad vea y trabaje su lead.

**Regla absoluta:** Solo exportamos leads que son EXCLUSIVOS de la Principal — los que entran directamente a subcuentas de sede NO deben exportarse (ya están donde tienen que estar).

---

## ✅ LO QUE YA EXPORTAMOS HOY

### Flujos confirmados activos:

| # | Tipo de Lead | Canal | Identificador |
|---|---|---|---|
| 1 | **IG DM** | Instagram Direct | Workflow "3. Recibir msj IG" → bot califica → exporta |
| 2 | **FB DM** | Facebook Direct | Workflow "2. Recibir msj FB" → bot califica → exporta |
| 3 | **WA Principal** | WhatsApp línea principal | Workflow WA GPT (0.1 SMS GPT / 0.1.1 API WA GPT FJF) |
| 4 | **WA 312 orgánico** | WhatsApp 312 desde landing innovartmedical.com | Mismo flujo WA |
| 5 | **Landing /home** | Shopify innovartmedical.com → form | Workflow "6. Poner Tag Landing" → exporta |
| 6 | **API Principal** | Webhook externo (programas, integraciones) | Webhook inbound |

### Webhooks de exportación a sedes:
*(IDs parciales — pendiente confirmar UUIDs completos)*
- Bogotá: `a4c61322-xxxx`
- Medellín: `432fbde6-xxxx`
- Barranquilla: `b999bf38-xxxx`
- Panamá: `2fd76cc1-xxxx`
- **Bucaramanga: ¿Existe?** — No aparece en registros anteriores

---

## ⚠️ LO QUE FALTA EXPORTAR

### Tipos de lead captados en Principal SIN exportación confirmada:

| # | Tipo | Canal | Estado |
|---|---|---|---|
| 1 | **IG DM nativo** (orgánico sin ciudad en msj) | IG DM | ⚠️ Caso A — en trabajo |
| 2 | **Lead Forms FB** | Facebook Lead Ads | 4 workflows en DRAFT (Bogotá, Medellín, Barranquilla, Panamá) — ¿activos? |
| 3 | **Form web /pages/contact** | Shopify contact form | Implementado 2026-06-19 → ¿exporta? |
| 4 | **Form Qikify** | innovartmedical.com Qikify popup | N8N roto, arquitectura nueva pendiente |
| 5 | **Blog leads WA** | WhatsApp desde blog | Workflow `ddc39bd2` activo pero ¿exporta a sede? |

---

## 🎯 LO QUE QUEREMOS TENER (WISHLIST)

### Datos en el payload de exportación (hoy vs. futuro):

| Campo | Hoy | Futuro ideal |
|---|---|---|
| Nombre | ✅ | ✅ |
| Teléfono | ✅ | ✅ |
| Email | ✅ (si existe) | ✅ |
| Ciudad | ✅ (por utm_term) | ✅ |
| utm_source | ⚠️ A veces | ✅ Siempre |
| utm_medium | ⚠️ A veces | ✅ Siempre |
| utm_term | ✅ (nuevo) | ✅ |
| utm_campaign | ❌ | ✅ |
| Tags al momento de exportar | ❌ | ✅ para trazabilidad |
| Último mensaje del bot | ❌ | ✅ (contexto comercial) |
| Resumen de conversación | ❌ | ✅ wishlist — GHL no nativo |
| Score de calificación del bot | ❌ | ✅ wishlist |
| fbclid | ✅ (si hay) | ✅ |
| Fecha primer contacto | ✅ | ✅ |

### Limitación técnica conocida:
> GHL **no permite exportar historial de conversación** entre subcuentas. Lo que SÍ podemos enviar en el webhook es un campo de texto con un **resumen generado por IA** de la conversación (el bot ya tiene el contexto), o enviar las últimas N notas del contacto como texto plano en el payload. Esto le da al comercial trazabilidad sin necesitar acceso a la cuenta principal.

---

## 📋 GAPS IDENTIFICADOS

### P0 — Crítico
- [ ] **Confirmar UUIDs completos** de los 4 webhooks "Enviar contacto a Sede"
- [ ] **Verificar si existe webhook para Bucaramanga** (sede activa sin webhook confirmado)
- [ ] **Lead Forms FB** — 4 workflows en DRAFT, ¿se activan o están obsoletos?

### P1 — Importante  
- [ ] **Form Qikify** — arquitectura nueva pendiente (~45min) [[plan-formulario-qikify-innovartmedical]]
- [ ] **Agregar UTMs al payload** de los 4 webhooks de exportación (FASE 2 pendiente)
- [ ] **Verificar Blog leads** — ¿el workflow `ddc39bd2` exporta a sede o solo queda en Principal?

### P2 — Wishlist
- [ ] **Resumen de conversación** en el payload (texto generado por bot)
- [ ] **Tags al exportar** — snapshot de tags en momento de exportación
- [ ] **Score de calificación** del lead antes de exportar

---

## 🔗 Referencias

- Workflows de ciudad IG DM: `f3c21f45` (Bogotá), `06a7435d` (Medellín), `3cae2544` (Barranquilla), `186016c6` (Panamá), `2fc70935` (Bucaramanga)
- Custom fields UTM: utm_source `ffBWPx4Qlhxb6D6toNWO`, utm_medium `46qWfYJubx8IAOhyFlgT`, utm_term `ni4PMQh6l93hmoiyfEEY`
- [[utm-tracking-avance-general]]
- [[stack-pauta]]
- [[plan-formulario-qikify-innovartmedical]]
