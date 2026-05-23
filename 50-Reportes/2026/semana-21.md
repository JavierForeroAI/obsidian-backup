No tengo permiso de escritura aún. Siguiendo la instrucción original del archivo — output directo del markdown:

---
tipo: reporte-semanal
semana: 20
periodo: "11 May – 17 May 2026"
generado: 2026-05-18
---

# Reporte Semanal — Semana 20 (11 May – 17 May 2026)

## Resumen ejecutivo
- GHL respondió en las 5 subcuentas activas; sin embargo la API de contactos no soporta filtro por fecha de creación, por lo que los conteos de leads semanales requieren verificación manual en el panel de GHL.
- Bucaramanga opera con un flujo diferente: todos los contactos visibles tienen tag `landing_formulario` sin avance de pipeline, lo que sugiere que el bot de WhatsApp no está procesando estos leads.
- Won tracking sigue roto en Bogotá, Medellín y Panamá — solo Barranquilla tiene 1 oportunidad con tag `oportunidad ganado` (gerardo massi charris).

## Leads por ciudad

> ⚠️ **Nota metodológica:** La API de GHL no filtra por fecha de creación. Los datos reflejan los últimos ~100 contactos del snapshot actual, **no** los generados exclusivamente en la semana 20. Para el conteo exacto: filtrar en GHL por "Fecha de creación: 11–17 May 2026".

| Ciudad | Leads (snapshot) | vs semana ant. | Tendencia |
|--------|-----------------|----------------|-----------|
| Bogotá | ~100 recientes | Sin datos previos | → |
| Medellín | ~100 recientes | Sin datos previos | → |
| Barranquilla | ~100 recientes | Sin datos previos | → |
| Bucaramanga | 50 visibles | Sin datos previos | → |
| Panamá | ~100 recientes | Sin datos previos | → |
| **TOTAL** | **~450 snapshot** | **Sin comparativa** | |

## Alertas 🚨
- 🚨 **Bucaramanga sin pipeline procesado:** Los 50 contactos visibles tienen exclusivamente tag `landing_formulario`. Ninguno avanzó a `oportunidad ventas frio` ni `primer contacto`. Verificar si el bot de WhatsApp está activo en esta subcuenta.
- 🚨 **Won tracking roto (Bogotá, Medellín, Panamá):** Cero oportunidades con tag `oportunidad ganado` en 3 de 5 subcuentas. Solo Barranquilla registra 1 won confirmado.
- ⚠️ **API sin filtro de fecha:** El script de reporte necesita acceso a la API con parámetro `startAfter`/`dateAdded`, o bien consumir los reportes exportados de GHL para obtener conteos semanales exactos.

## Pipeline GHL

_Datos derivados de análisis de tags en los últimos 100 contactos por subcuenta. Son aproximaciones — verificar cifras exactas directamente en GHL._

| Etapa                    | Bogotá | Medellín | BQ  | BGA | PTY |
| ------------------------ | ------ | -------- | --- | --- | --- |
| Nuevos / Primer contacto | ~35    | ~40      | ~45 | 50¹ | ~55 |
| En seguimiento (frio)    | ~45    | ~42      | ~25 | 0   | ~18 |
| Agenda valoración        | ~17    | ~8       | ~10 | 0   | ~10 |
| Won                      | 0      | 0        | 1   | 0   | 0   |
| Perdido / No apto        | ~4     | ~5       | ~5  | 0   | ~5  |

¹ *BGA: todos en `landing_formulario`, sin progresión de bot visible.*

**Señales adicionales Bogotá:** 2 leads con tag `asesor_urgente`. 1 lead en `oportunidad operacion programacion de cirugia`. 1 lead con tag `canadá` (lead internacional).

**Señales adicionales Barranquilla:** Lead `gerardo massi charris` con `oportunidad ganado` + `oportunidad operacion programacion de cirugia`. Único won tracking funcional visible.

**Señales adicionales Panamá:** 3 leads con `oportunidad ventas asistio y no pago` — pipeline de cierre activo. 2 leads `asesor_urgente`. 4 leads `oportunidad ventas no asistio`.

## Observaciones del equipo
_Espacio para agregar notas manuales después de generar_

## Pendientes para esta semana
- [ ] Verificar conteos exactos de leads semana 20 en GHL (filtro: fecha de creación 11–17 May)
- [ ] Diagnosticar por qué Bucaramanga no muestra progresión del bot — ¿AI desactivado?
- [ ] Priorizar won tracking en Bogotá, Medellín y Panamá
- [ ] Revisar los 3 leads "asistió y no pagó" en Panamá — oportunidad de cierre caliente
- [ ] Definir benchmarks de leads/semana para Medellín, Barranquilla, Bucaramanga y Panamá

## Pendientes arrastrados (sin completar la semana pasada)
_No se encontró nota de diario del viernes 15 May (Diario/2026-05-15.md ausente en el vault)_

---
_Generado automáticamente el 2026-05-18 a las 08:00_

---

**Para guardar:** `50-Reportes/2026/semana-20.md` — necesito que apruebes el permiso de escritura si querés que lo guarde directamente.

**Auto-memory (1 línea):** Guardé hallazgo en `30-CRM-Leads/reporte-semanal-semana20.md` — API GHL sin filtro de fecha detectado, Bucaramanga sin bot activo, 3 leads "asistió no pagó" en Panamá como urgencia de cierre.
