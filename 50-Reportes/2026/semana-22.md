---
tipo: reporte-semanal
semana: 21
periodo: "18 May – 24 May 2026"
generado: 2026-05-25
---

# Reporte Semanal — Semana 21 (18 May – 24 May 2026)

## Resumen ejecutivo
- Bogotá devolvió **401 Unauthorized** — subcuenta inaccesible por API esta semana; datos de la ciudad más importante ausentes.
- Bucaramanga acumula **dos semanas consecutivas sin bot activo**: todos los contactos permanecen en `landing_formulario` sin progresión de pipeline; el pendiente de la semana 20 no se resolvió.
- Panamá muestra el **pipeline más activo** de la red: ~55 leads en primer contacto vía Facebook Forms y 3 casos "asistió y no pagó" que siguen sin cierre.

## Leads por ciudad

> ⚠️ **Nota metodológica:** La API de GHL no filtra por fecha de creación. Los datos reflejan los últimos ~100 contactos del snapshot actual, **no** los generados exclusivamente en la semana 21. Para conteo exacto: filtrar en GHL por "Fecha de creación: 18–24 May 2026".

| Ciudad | Leads (snapshot) | vs semana ant. | Tendencia |
|--------|-----------------|----------------|-----------|
| Bogotá | ⚠️ Sin datos (401) | — | — |
| Medellín | ~100 recientes | Sin cambio visible | → |
| Barranquilla | ~100 recientes | Sin cambio visible | → |
| Bucaramanga | ~50 visibles | Sin cambio visible | → |
| Panamá | ~100 recientes | Sin cambio visible | → |
| **TOTAL** | **~350 (excl. Bogotá)** | **Sin comparativa** | |

## Alertas 🚨
- 🚨 **Bogotá inaccesible (401 Unauthorized):** La API rechaza el token para esta subcuenta. Verificar credenciales / token expirado en el MCP de GHL. Ciudad con benchmark 105–175 leads/semana queda sin monitoreo.
- 🚨 **Bucaramanga sin bot — semana 2:** Los ~50 contactos visibles tienen exclusivamente tag `landing_formulario` y ninguno tiene `ai_activado`. El diagnóstico pendiente de semana 20 no fue resuelto. Leads en limbo sin seguimiento comercial.
- 🚨 **Won tracking roto (Medellín, Panamá):** Zero oportunidades `won` detectables en estas subcuentas. Solo Barranquilla mantiene 1 won histórico (gerardo massi charris).
- ⚠️ **3 leads "asistió y no pagó" en Panamá sin cierre:** Tercer reporte consecutivo sin resolución de estos casos calientes.

## Pipeline GHL

_Derivado de análisis de tags en últimos 100 contactos por subcuenta. Aproximaciones — verificar en GHL para cifras exactas._

| Etapa | Bogotá | Medellín | BQ | BGA | PTY |
|-------|--------|----------|----|-----|-----|
| Nuevos / Primer contacto | ⚠️ N/D | ~38 | ~28 | 0 | ~55 |
| En seguimiento (frio) | ⚠️ N/D | ~48 | ~40 | 0 | ~20 |
| Agenda valoración | ⚠️ N/D | ~3 | ~15 | 0 | ~15 |
| Won | ⚠️ N/D | 0 | 1 | 0 | 0 |
| Asistió y no pagó | ⚠️ N/D | 0 | ~2 | 0 | ~3 |
| No asistió | ⚠️ N/D | 0 | ~4 | 0 | ~5 |
| Perdido / No apto | ⚠️ N/D | ~1 | ~4 | 0 | ~3 |
| Landing sin proceso | — | — | — | ~50 | — |

**Señales adicionales Medellín:** 1 lead con tag `asesor_urgente` (e. rivas). 2 leads con `ai_parar` en agenda valoración activa (paola G3h5, jesús osorio). Pipeline de seguimiento denso.

**Señales adicionales Barranquilla:** Pipeline de agenda valoración es el más proporcionalmente activo (~15% en etapa avanzada). Único won funcional en toda la red. 2 leads `asistió y no pagó` — cerrar esta semana.

**Señales adicionales Panamá:** Flujo form (Facebook Forms) muy activo con ~55 en primer contacto. Pipeline avanzado con leads en `agenda valoracion`, `no asistio` y `asistio y no pago`. 3 casos calientes pendientes de cierre desde semana 20.

**Bucaramanga:** 0 pipeline funcional. ~50 contactos detenidos en `landing_formulario`. Sin `ai_activado` en ninguno.

## Observaciones del equipo
_Espacio para agregar notas manuales después de generar_

## Pendientes para esta semana
- [ ] Resolver acceso 401 a subcuenta Bogotá — revisar token MCP GHL
- [ ] Diagnosticar y activar bot IA en Bucaramanga (pendiente semana 2)
- [ ] Cerrar los 3 casos "asistió y no pagó" en Panamá antes del viernes
- [ ] Cerrar los 2 casos "asistió y no pagó" en Barranquilla
- [ ] Activar won tracking en Medellín y Panamá
- [ ] Definir benchmarks de leads/semana por ciudad (BQ, BGA, PTY)

## Pendientes arrastrados (sin completar la semana pasada)
- [ ] Verificar conteos exactos de leads semana 20 en GHL (filtro: fecha de creación 11–17 May) — [[50-Reportes/2026/semana-21]]
- [ ] Diagnosticar Bucaramanga sin progresión de bot — ¿AI desactivado? — [[50-Reportes/2026/semana-21]]
- [ ] Priorizar corrección won tracking en Bogotá, Medellín y Panamá — [[50-Reportes/2026/semana-21]]
- [ ] Revisar y cerrar los 3 leads "asistió y no pagó" en Panamá — [[50-Reportes/2026/semana-21]]
- [ ] Definir benchmarks leads/semana por ciudad — [[50-Reportes/2026/semana-21]]

---
_Generado automáticamente el 2026-05-25 a las 08:00_
