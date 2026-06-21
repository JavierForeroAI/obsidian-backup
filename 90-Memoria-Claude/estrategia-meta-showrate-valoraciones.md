---
name: estrategia-meta-showrate-valoraciones
description: Estrategia Meta Ads (multiagente) para subir el show rate de valoraciones de ~40% — 5 propuestas + embudo médico, con verificación en vivo de las 6 cuentas
metadata:
  type: project
---

# Estrategia Meta Ads para subir el show rate de valoraciones — Innovart (2026-06-20)

Estrategia **exclusivamente de Meta Ads** (+ cableado de señal) para atacar el no-show: se agendan ~25 valoraciones pero solo asiste ~40%. Hecha con **análisis multiagente** (13 agentes: 5 lentes proponen → debate cruzado → síntesis → auditoría adversarial que **verificó en vivo las 6 cuentas Meta** y corrigió supuestos falsos). Destinatarios: Esneider y Diego.

## Insight central
Las campañas optimizan por el **lead/conversación más barato** → Meta trae al que abre chat fácil (curioso), no al que asiste. **Meta nunca ha visto quién sí asiste** (no existe el evento "Valoración Asistida"). Palanca real: optimizar por **`Schedule` calificado**, no por lead.

## Hechos verificados en vivo (correcciones clave)
- **DM WAP MED** y **DM WAP BRQ** corren en la cuenta **BGTA (USD)**, NO en MEDELLIN (cuenta ≠ sede → ver [[feedback-cuentas-meta-no-son-sedes]]).
- **Monedas mixtas:** BGTA/QUILLA/PANAMA = USD; MEDELLIN/LANDING/INTERACCION = COP → **CBO entre cuentas imposible** (consolidar DENTRO de cada cuenta).
- **Dataset:** MEDELLIN (`1625645205284016`) **ya recibe `Schedule`**; el que solo tiene `PageView` es **BGTA** (`1642103999710262`) → piloto arranca en Medellín; cablear BGTA.
- **EMQ del Lead = 4.9** (< gate 6) → arreglar payload CAPI antes de optimizar.
- **Volumen:** Lead ~80-100/sem, Schedule ~6/sem, ValoraciónAsistida ~2-3/sem → ValoraciónAsistida **inutilizable como goal a 90 días** (solo lectura/value).
- Show rate **no auditable hoy** (endpoint de citas 404 → calcular manual en GHL, ver [[feedback-ghl-fechas-manual]]).

## Las 5 propuestas
1. **Re-señalización:** optimizar por `Schedule` calificado vía CAPI (regla objetiva: cita futura + tel validado + ciudad/modalidad), CBO dentro de cada cuenta. Gate EMQ ≥6. *Columna vertebral.*
2. **Lookalike de "Asistió/Operados"** (días 30-60, si la semilla supera el mínimo de match).
3. **Calificación primer toque** (quick win): reframe "valoración = consulta médica" + Ice Breaker de 1 pregunta + avatares en el creativo + acople anuncio↔bot.
4. **Anti-no-show:** recordatorio WhatsApp con "responde SÍ" (principal) + refuerzo Meta 3 actos del Dr. Carreño (condicionado a tamaño de audiencia).
5. **Cerrar el loop:** definir fuente de verdad del show rate + marcar "Asistió" obligatorio para comisión (piloto 1 sede). *Habilitador.*

## Dónde vive
- **Drive (maestro, HTML):** https://drive.google.com/file/d/1pnRYReTfzqgkhrvVEcEy1cyFEJtZ3taf/view — carpeta AUDITORIA COMUNICACION GHL Y MEJORAS (`1LCzzvFFQgz-SHm_5raj2DTBOoJYsli3A`). ⚠️ Privado: compartir con esneidervc17@gmail.com y diegosilvacdigital@gmail.com.
- **Local:** `~/Downloads/Estrategia-Meta-ShowRate-Innovart-2026-06-20.html`
- **Correo:** borrador en Gmail de Javier (resumen + link) para Esneider + Diego — el conector solo crea borradores, se envía manual.

## Pendiente / próximos pasos
- Compartir el Drive con el equipo (o adjuntar HTML al correo) y enviar.
- Quick wins semana 1: fuente de verdad del show rate · reframe copy + Ice Breaker · recordatorio WhatsApp · cablear evento asistencia BGTA + EMQ ≥6 · North Star = costo por asistido (no CPL).

Relacionado: [[diagnostico-ai-prospeccion-2026-06-12]] (show rate <40%) · [[auditoria-capimetaghl-base]] (datasets/EMQ/CAPI) · [[capi-webhook-worker]] · [[stack-pauta]] · [[adn-comunicacion-innovart]] (avatares/funnel M4) · [[restricciones-lenguaje]] (compliance copy).
