---
name: flujo-4-1-sms-lead-habilitado-2026-06-29
description: SMS/WA al lead en workflow 4.1 habilitado en 4 sedes (Bogotá, Medellín, Barranquilla, Panamá). Estado por sede, IDs de workflow y pendiente Bucaramanga.
metadata:
  type: project
  fecha: 2026-06-29
  status: PARCIALMENTE_COMPLETO
---

# Workflow 4.1 — Paso SMS/WA al lead habilitado (29 jun 2026)

## Problema encontrado

El paso final del workflow `4.1 Recibir lead de Landing_formulario` (mensaje al lead con saludo + Reel 3) estaba **deshabilitado en TODAS las sedes**. Los leads entraban al CRM, se creaba la oportunidad y se notificaba al asesor, pero el lead nunca recibía ningún mensaje automático → conversación nunca iniciaba.

## Fix aplicado

Se cambió `advanceCanvasMeta.isDisabled: true → false` en el paso SMS/WA al lead de cada sede via `update_workflow_actions`.

## Estado por sede

| Sede | Workflow ID | Versión antes → después | Paso al lead | Estado |
|---|---|---|---|---|
| Panamá | `93a0ecb1-c0ce-4159-b531-0f3f6ba9c059` | v17 → v18 | SMS + video | ✅ habilitado |
| Bogotá | `d405fcaf-adc7-4281-b36c-f647f8707f17` | v30 → v31 | SMS + video | ✅ habilitado |
| Medellín | `fbe353c5-7b84-45a4-8b09-0137235e72d0` | v24 → v25 | SMS + video | ✅ habilitado |
| Barranquilla | `a15f77f1-8c1c-46cd-97e6-1d93517eb4c2` | v35 → v36 | WhatsApp template v2 (imagen) | ✅ habilitado |
| Bucaramanga | `2efd5f03-79f8-45fe-bc82-a5bee8bdfddf` | v4 (sin cambio) | **NO EXISTE** | ⚠️ pendiente |

## Flujo completo del 4.1 (Bogotá/Medellín/Panamá)

```
Tag landing_formulariov2 dispara 4.1
  1. Crea oportunidad Ventas / Frío
  2. Asigna asesor
  3. Espera horario hábil (lun–sáb 7am–8pm)
  4. Actualiza intentos_llamada = 1
  5. SMS interno al asesor (notificación)
  6. Webhook dapta.ai (DISABLED — no tocar)
  7. ✅ SMS al lead: saludo + Reel 3 (1).mp4
  8. (Notificación final — DISABLED, incompleteData)
```

## Flujo 4.1 Barranquilla (diferente)

```
  1. Crea oportunidad
  2. Asigna asesor
  3. Espera horario hábil
  4. SMS interno al asesor
  5. Update intentos_llamada = 1
  6. Webhook dapta.ai (DISABLED)
  7. ✅ WhatsApp template v2 al lead (template_id: 737563909409886, imagen incluida)
```

## Bucaramanga — 4.1 simplificado (PENDIENTE)

El 4.1 de Bucaramanga fue creado el 2026-06-28 y es más simple:
```
  1. Crear oportunidad Ventas/Frío (pipeline r6twTNR4DbLvYrtXCIHR)
  2. Asignar asesor (Y1Lj2tAjeawnEoUwHy3B)
  3. Update intentos_llamada = 1
  4. SMS al asesor (interno)
  — SIN PASO AL LEAD —
```
**Pendiente:** añadir paso de SMS/WA al lead igual que las demás sedes.

## Regla crítica para update_workflow_actions

Al usar `update_workflow_actions` se deben enviar **TODOS los pasos** del workflow en el array `actions`. Si se envían solo los modificados, los demás pasos se borran.

## Lead Leidy (Panamá) recuperada

- contactId: `KwELucAHDfGJmR1JcpCj`
- Añadida manualmente al workflow 4.1 Panamá el 29 jun 2026
- Lead que llegó por formulario GemPages antes del fix (29 jun, 12:39 AM)

## Archivos relacionados

- [[landing-panama-gempages-setup-2026-06-29]] — fix formulario GemPages → Worker → GHL Panamá
- [[flujo-crm-qikify-verificado-2026-06-29]] — flujo completo Qikify → GHL
