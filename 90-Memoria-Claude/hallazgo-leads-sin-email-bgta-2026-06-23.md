---
name: hallazgo-leads-sin-email-bgta
description: Hallazgo crítico — leads reales en BGT sin email (0% cobertura), solo teléfono — cuello de botella para EMQ 4.9 (2026-06-23)
metadata:
  type: feedback
---

## Hallazgo Crítico: Leads sin Email en BGTA — Cuello de Botella EMQ

**Descubrimiento:** 2026-06-23, auditoría de nuevos leads post-fbclid

**El problema:**
4 leads reales hoy (ramiro, david motos, francisco, david martinez):
- ❌ **CERO tienen email** (0% cobertura)
- ✅ Todos tienen teléfono
- ✅ fbclid capture funciona correctamente

**Causa identificada:**
Muchos usuarios **entran por WhatsApp directo**, no por formulario web. WhatsApp no solicita email → el contacto llega a GHL sin él.

**Impacto en Meta CAPI:**
- EMQ actual: **4.9 (bajo)** → target 5.5+
- Meta no puede matchear sin email → No audience matching
- Evento Lead en Meta: **EMQ 5.2** (más bajo aún)
- Evento Schedule: **EMQ 4.8** (casi sin señal)
- Evento PageView: **EMQ 6.1** (tiene fbclid en 42%)

**Root cause del EMQ bajo = NO es fbclid (funciona OK), es EMAIL**

| Evento | EMQ | Email Coverage | Phone | Problema |
|---|---|---|---|---|
| Lead | 5.2 | 20% | 100% | Sin email = Meta no matchea |
| Schedule | 4.8 | 0% | 100% | Peor aún |
| PageView | 6.1 | — | — | Tiene fbclid 42% |

**Why:**
El funnel actual mezcla dos canales: formulario web (email) + WhatsApp directo (sin email). Pero Javier indica que "muchos entran por WhatsApp" = el volumen vivo es principalmente WhatsApp, que NO captura email.

**How to apply:**
Para subir EMQ, necesitamos una estrategia de captura de email:

1. **Opción A: Solicitar email en WhatsApp** — workflow GHL que pregunta "¿Cuál es tu email?" antes de oferta (friction, puede perder leads)

2. **Opción B: Usar teléfono como ID temporal + matching por PII** — CAPI acepta phone + pais, puede matchear (menos confiable que email)

3. **Opción C: Email como soft-requirement en form web** — si alguien intenta contactar sin email, llevar a formulario web (re-targeting)

4. **Opción D: Mezclar email + teléfono en CAPI** — Meta puede entrenar con PII mixta (email es más fuerte, phone de backup)

**Siguiente paso:** Preguntar a Javier cuál es la estrategia preferida. Mientras tanto, sigue siendo VERDAD que fbclid capture funciona bien.

**Nota para el futuro:**
Cuando se audite nuevo landing o form, preguntar SIEMPRE:
- ¿El form solicita email? ¿Es requerido?
- ¿Hay leads por canal alternativo (WhatsApp, otros) que no capturan email?
- EMQ bajo = revisar cobertura de email PRIMERO, no fbclid.

**Referencias:**
- [[landing-home-nueva-url-2026-06-23]]
- [[fbclid-home-implementacion-exitosa-2026-06-22]]
- [[auditoria-fbclid-critica-2026-06-22]]
- [[filtro-capi-submitapplication-2026-06-22]]
