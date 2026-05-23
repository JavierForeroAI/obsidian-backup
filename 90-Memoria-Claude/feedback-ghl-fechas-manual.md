---
name: feedback-ghl-fechas-manual
description: Cómo analizar conversaciones GHL por fecha manualmente — limitaciones reales del API y metodología paso a paso
metadata:
  type: feedback
---

## Regla

Cuando el usuario pida cualquier análisis por fechas en GHL (tasas de respuesta, conversaciones de un mes, actividad semanal, tiempos de respuesta, etc.), **hacerlo manualmente leyendo timestamps de conversaciones**.

**Por qué:** El endpoint `/calendars/events/appointments` devuelve 404 sin importar el formato de fecha o los parámetros. Las herramientas que SÍ funcionan son `ghl_get_contacts` y `ghl_get_conversations`, y sus respuestas incluyen timestamps Unix en ms.

---

## Limitación real del API

`ghl_get_contacts` devuelve **máximo 100 contactos** y **no tiene parámetro de paginación** (no existe `offset` ni `page`). Con 160K+ contactos en el CRM, solo puedo ver una muestra. Para maximizar cobertura:

- Usar `limit: 100` siempre (trae los más recientes)
- Complementar con `query` por nombre/teléfono para buscar contactos específicos
- Especificar `locationId` por sede para análisis por ciudad
- Siempre advertir al usuario que el resultado es una muestra, no el universo completo

---

## Metodología paso a paso

1. Llamar `ghl_get_contacts` con `limit: 100` para la sede solicitada
2. Tomar **todos los IDs** y llamar `ghl_get_conversations` en paralelo (tandas de 10)
3. Extraer los campos clave de cada conversación:
   - `lastMessageDate` → cuándo fue el último mensaje
   - `lastInboundWhatsappMessageDate` → cuándo escribió el lead
   - `lastManualMessageDate` → cuándo respondió el asesor
   - `lastMessageDirection` → `inbound` o `outbound`
   - `lastOutboundMessageAction` → `automated` o `manual`
   - `assignedTo` → qué asesor
4. Convertir timestamps de ms Unix a hora Colombia (UTC-5):
   - `datetime.fromtimestamp(ts_ms/1000, tz=timezone(timedelta(hours=-5)))`
5. Filtrar los que caen en el rango de fecha solicitado
6. Calcular métricas: tiempo de respuesta = `lastManualMessageDate - lastInboundWhatsappMessageDate`

---

## Campos de timestamp importantes en conversaciones GHL

| Campo | Qué indica |
|-------|-----------|
| `dateAdded` | Cuándo se creó la conversación en GHL |
| `lastMessageDate` | Último mensaje (inbound o outbound) |
| `lastInboundWhatsappMessageDate` | Última vez que el lead escribió por WhatsApp |
| `lastManualMessageDate` | Última respuesta del asesor (manual o automatizada) |
| `lastOutboundMessageAction` | `automated` = bot/flujo, `manual` = asesor humano |
| `unreadCount` | Mensajes sin leer (> 0 = sin responder aún) |

---

## Ejemplo aplicado (Bogotá, 20 mayo 2026)

De 100 contactos revisados (~50 con conversaciones analizadas):

**Inbound May 20:**
- Juan Pablo Prada: escribió 4:00 AM → respuesta 9:05 AM → **5h 04m**
- Emid Sanchez: escribió 11:44 AM → respuesta 3:23 PM → **3h 39m**
- Ambos atendidos por Isabel. Ambos ya agendados (leads en etapa valoración).

**Outbound proactivo May 20:**
- Mariana Prada: lote de 4 leads a las 14:24 COL con script "Dra. Gloris" → 0 respuestas

**Conclusión:** Tasa de respuesta 100% (2/2 respondidos), tiempo promedio ~4h 22m — lento para horario laboral. El bot de IA no estaba activo en estas conversaciones (ai_parar).

---

**How to apply:** Cada vez que el usuario pida "analiza el día X" o "cómo estuvieron las conversaciones de [período]", seguir esta metodología. Siempre advertir que cubre los 100 contactos más recientes y puede no ser el universo completo.
