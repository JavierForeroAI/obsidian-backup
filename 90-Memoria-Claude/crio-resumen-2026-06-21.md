---
name: crio-resumen-2026-06-21
description: Diagnóstico inicial CRIO — estado completo del sistema Meta+GHL+CAPI con datos en vivo. Dashboard ejecutivo, top problemas, top oportunidades, roadmap 30/90/180 días. 2026-06-21.
metadata:
  type: project
---

# CRIO — Diagnóstico Inicial del Sistema · 2026-06-21

## Resumen ejecutivo

El sistema tiene tráfico barato (~$3 USD/lead) pero Meta aprende el perfil equivocado: el curioso que abre WhatsApp, no el paciente que opera. 61% del presupuesto va a DM WAP con 0 señal de revenue. Purchase activo hace 7 días con solo 2 eventos. EMQ 5.0 (bajo el gate de 6). 4 cuentas en Grace Period (riesgo de suspensión).

## Hallazgos críticos confirmados en vivo

- **Facturación:** BGTA, PANAMA, MEDELLIN, LANDING DIEGO = status 9 (Grace Period) → riesgo suspensión
- **Purchase:** 2 eventos en 7 días (activado Jun-14). Meta no puede aprender con esto.
- **Schedule:** 6 eventos/7 días, solo Medellín. BGTA sin Schedule.
- **Lead EMQ:** 5.0 — email 7.1%, apellido 57.1% (todos los leads entran sin email por WhatsApp)
- **Píxel 1642103999710262:** solo PageView. CERO conversiones.
- **DM WAP:** $2,122 USD/mes (61% presupuesto BGTA) optimizando para "abre chat", no para operar
- **CRM Bogotá:** 25,717 opps, valor monetario $0 en todas. Sin email en contactos.
- **Matriz:** 105,275 leads dormidos sin enrutar

## Acciones P1 (próximas 48h)

1. Verificar facturación 4 cuentas (Javier — HOY)
2. Auditoría Purchase webhook (Auditor — HOY)
3. Cablear Schedule BGTA (Orquestador — mañana)
4. Email en bot GHL → EMQ ≥7 (Claude — mañana)
5. Reunión con traffickers: cambiar North Star a Costo por Asistido

## KPIs correctos

- CPL → Costo por Asistido
- Leads/día → Show Rate %
- Conversaciones WA → Schedule calificado
- CTR → Purchase/semana

## Links del diagnóstico completo

- Diagnóstico generado en sesión Claude Code 2026-06-21
- Datos en vivo: Meta API + GHL MCP

Relacionado: [[auditoria-capimetaghl-base]] · [[estrategia-meta-showrate-valoraciones]] · [[plan-agencia-internacional]]
