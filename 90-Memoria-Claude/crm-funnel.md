---
name: crm-funnel-innovart
description: Volumen de CRM, estado del funnel y problemas de tracking de conversiones
metadata:
  type: project
---

# CRM y funnel — Innovart

## Volumen total (2026-05-18)

| Sede         | Oportunidades totales |
| ------------ | --------------------- |
| Cuenta Raíz  | 103,463               |
| Bogotá       | 25,241                |
| Barranquilla | 13,112                |
| Medellín     | 11,049                |
| Panamá       | 7,231                 |
| Bucaramanga  | 0 (recién creada)     |

## Velocidad de entrada (estimada)
- Bogotá: ~15-25 leads/día
- Panamá: ~1-5 leads/día

## Estructura del pipeline "Ventas" (igual en todas las ciudades)
Frío → Primer contacto → Tibio → Agenda Valoración → Val Virtual → Asistió/No → Ganado → Perdido

### Etapas de fricción identificadas (deducidas del CRM):
1. "Consultar con esposa" — decisión en pareja
2. "A la espera de vacaciones" — recuperación sin trabajar
3. "Paciente MeddiPay" — necesita crédito
4. "Cancelado – Reagendamiento pendiente" — cancela pero recuperable

## Problema crítico: won status roto
GHL Bogotá: **solo 2 oportunidades marcadas "won"** de 25,241 totales. El cierre real de ventas no se registra en GHL — los pacientes se mueven al pipeline "Operaciones" pero el status en "Ventas" queda en "open". Las métricas de conversión del CRM son inútiles para análisis.

**Why:** Observado 2026-05-18 vía API GHL.
**How to apply:** No calcular tasas de conversión desde GHL sin primero revisar el pipeline "Operaciones". El número real de cirugías es un gap que solo el cliente puede responder. [[stack-pauta-innovart]]
