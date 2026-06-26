---
name: bloqueantes-show-rate-43percent-junio2026
description: 3 bloqueantes críticos que mantienen show rate en 43% en lugar de 70%+ — EMQ 4.9, falta de reminders, desacoplamiento avatar-bot. Junio 2026.
metadata:
  type: project
  date: 2026-06-24
---

# 3 Bloqueantes — Show Rate 43% (Junio 2026)

## Panorama

**Hoy:** 43% de leads agendados asisten a valoración.  
**Target:** 70%+ (realista en 30–90 días).  
**Gap:** 27 puntos porcentuales = $16–24K USD/mes en revenue perdido.

## 🚨 Bloqueante #1 — EMQ = 4.9 (Objetivo: ≥6)

**Qué es:** Event Match Quality (Meta Pixel + CAPI) — capacidad de Meta para matchear eventos con usuarios reales.

**Estado actual:**
- EMQ 4.9 = Meta tiene poca visibilidad
- **Causa raíz:** Leads en BGTA llegan 100% por WhatsApp (teléfono), 0% email
- Formulario web NO solicita email → cero PII de calidad
- Email capturado = 0% cobertura

**Impacto:**
- Meta no puede train algoritmos (falta datos de revenue)
- CAPI recibe eventos pero sin matching: ~600 eventos/mes se pierden
- Atribución rota: "¿Este Schedule vino de qué anuncio?" → Meta no sabe

**Solución (30 min):**
1. Bot WhatsApp pregunta: **"¿Cuál es tu email?"** (antes de agendar)
   - Recolecta email en campo GHL `email`
   - Captura automáticamente en CAPI
2. Meta verifica email contra su base → Match rate ↑

**Impacto esperado:** EMQ 4.9 → 5.5+ (indirecto: +2% show rate por mejor targeting)

---

## 🚨 Bloqueante #2 — Arquitectura de Reminders Ausente

**Estado actual:**
- Confirmación en **Día 1** solamente
- Reminders planificados (-2d, -24h, -2h) existen en **DRAFT** pero NO activos
- Workaround: reintento manual

**Impacto:**
- ~40–50% de leads olvidan o cambian de opinión entre agendamiento y cita
- Sin touchpoint de -2 días: dejan de pensar en la valoración
- Sin SMS -2h: no se preparan ni confirman asistencia

**Solución (1.5 horas):**

1. **Activar workflow "Etiqueta Agenda Valoracion"** (ID: `3fbd8ccd-f311-4eea...`)
2. **Crear 3 branches automáticas:**
   ```
   Branch 1: -48h trigger → SMS + WhatsApp
     "Hola [Name], tu cita es en 2 días. ¿Confirmas presencia?"
   
   Branch 2: -24h trigger → SMS + WhatsApp
     "Última confirmación: mañana a las [hora]. Lugar: [dirección]"
   
   Branch 3: -2h trigger → SMS + WhatsApp
     "¡Ya casi! Tu cita es en 2 horas. Ven con cédula + receta EPS"
   ```

3. **Validar triggers GHL:**
   - `scheduled_appointment_reminder_before`
   - Offset: `-2d`, `-1d`, `-2h`

**Impacto esperado:** **+15–20% show rate** ⭐

---

## 🚨 Bloqueante #3 — Desacoplamiento Avatar-Bot

**Problema:**
- Usuario ve creativo: **"Profesional Premium, 45 años, implante superior"** (avatar específico)
- Recibe bot: **"Confirmamos tu cita"** (mensaje genérico)
- Contexto emocional se pierde → abandono

**Ejemplo real:**
```
Anuncio visto: "Recupera tu presencia ejecutiva en 3 meses"
            → Cliente es ejecutivo, 48 años, buscaba eso
Mensaje recibido: "Hola, confirmamos tu consulta. ¡Gracias!"
            → Genérico, no conecta con por qué el cliente clickeó
```

**Solución (1 hora):**

1. **Crear custom field GHL:** `creative_angle_seen`
   - Valores: `ejecutivo_premium`, `militar`, `gay_premium`, `emprendedor`, `gubernamental`
   - Capturado en landing → inyectado vía UTM o parámetro oculto

2. **Personalizar mensaje de reminder:**
   ```
   IF creative_angle_seen = "ejecutivo_premium":
     "Tu imagen ejecutiva te espera. Cita en 2h."
   
   IF creative_angle_seen = "gay_premium":
     "Tu comunidad te apoya. Confirma tu cita en 2h."
   
   IF creative_angle_seen = "militar":
     "Honor + resultados. Cita confirmada en 2h."
   ```

3. **Resultado:** Usuario siente continuidad narrativa → +commitment

**Impacto esperado:** **+10–15% show rate** ⭐

---

## Roadmap — Impacto Acumulativo

| Semana | Acción | Esfuerzo | Show Rate | Revenue Impact |
|--------|--------|----------|-----------|----------------|
| **SEM 1** | P0.1: Email capture bot | 30 min | +2% (43%→45%) | +$800 USD |
| **SEM 1** | P0.2: CAPI Schedule cleanup | 20 min | +3% (→48%) | +$1,200 |
| **SEM 1–2** | P1.1: Reminders (-2d/-24h/-2h) | 1.5h | +18% (→66%) | **+$7,200** ⭐ |
| **SEM 1–2** | P1.2: Avatar personalization | 1h | +12% (→78%) | **+$4,800** ⭐ |
| **SEM 2–3** | P1.3: Email/SMS channels | 30 min | +2% (→80%) | +$800 |
| **SEM 2–3** | P1.4: No-show recovery | 1h | +5% (→85%) | +$2,000 |
| **SEM 3–4** | P2.1: Close loop (CAPI Purchase) | 2h | +15% (→100%, teórico 70–75% real) | **+$6,000+** |

**Total Semana 1–2 (P0+P1):** 43% → **55–60%** ✅  
**Total Semana 3–4 (P2 incluido):** 43% → **70–75%** 🚀

---

## Implementación Inmediata (Esta Semana)

### Orden de ejecución:

1. **HOY (30 min):** Email capture bot WhatsApp
   - Test con 3 leads
   - Verificar captura en GHL

2. **MAÑANA (20 min):** CAPI Schedule cleanup
   - Revalidar workflow `Schedule`
   - Confirmar evento llega a Meta

3. **MIÉRCOLES–VIERNES (2.5h):** Reminders + Avatar
   - Publicar 3 branches de reminder
   - Custom field + workflow de personalización
   - Test E2E con 5 citas

---

## Métricas de Seguimiento

**Medir cada semana:**
- Show rate real (citas asistidas / citas agendadas)
- EMQ Meta (Dashboard → Pixel → EMQ)
- Email capture rate (% leads con email >= 1 semana)
- SMS abiertos (GHL analytics)
- Reminder engagement (clics, respuestas)

**Target esperado:**
- Semana 1: 43% → 45%
- Semana 2: 45% → 55%
- Semana 3: 55% → 65%
- Semana 4: 65% → 70%+

---

**Referencia:**
- [[estrategia-meta-showrate-valoraciones]] (análisis multiagente original)
- [[auditoria-meta-4-ciudades-junio2026]] (hallazgos por ciudad)
