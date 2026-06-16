I have everything needed. GHL has been down for the **5th consecutive week** (same token expiry), the renewal deadline set for today (Mon Jun 15) has passed, and the only intermittently-readable account (Bogotá, briefly on Jun 12) is now also returning 401. Per the instructions, I'll output the report as pure markdown — no Write tool, no preamble, no code fences (the prior run corrupted its file by adding those).

---
tipo: reporte-semanal
semana: 24
periodo: "8 Jun – 14 Jun 2026"
generado: 2026-06-15
---

# Reporte Semanal — Semana 24 (8 Jun – 14 Jun 2026)

## Resumen ejecutivo
- 🚨 **GHL inaccesible por 5ª semana consecutiva.** Las 5 subcuentas devuelven 401/403 — el token del MCP de GHL sigue expirado/sin permisos. La fecha límite de renovación fijada para hoy (lunes 15 Jun) **se cumplió sin resolverse**. Operación de CRM completamente ciega.
- **Sin métrica de leads real:** ni vía API (token caído) ni vía Meta (ninguna de las 4 cuentas rastrea el evento `lead`). La única señal viva es Meta Ads, que muestra inversión y conversaciones WA iniciadas pero **no permite calcular CPL** (ver notas diarias 11–12 Jun).
- **Acción P0 escalada:** renovar el token GHL es ahora la prioridad absoluta — bloquea reporte de leads, won tracking y diagnóstico de las 4 alertas operativas heredadas (Bucaramanga sin bot, won roto, Medellín gastando sin tracking, Panamá sin objetivo Lead).

## Leads por ciudad

> ⚠️ **GHL no disponible — 5ª semana consecutiva (401/403).** Datos no obtenibles vía API. Bogotá fue legible puntualmente el 12 Jun (8 leads ese día, 7 FB/WA + 1 IG) pero el token está nuevamente caído para las 5 subcuentas. Verificar conteos manualmente en GHL filtrando por fecha de creación 8–14 Jun 2026.

| Ciudad | Leads | vs semana ant. | Tendencia |
|--------|-------|----------------|-----------|
| Bogotá | ⚠️ Sin datos (401) | — | — |
| Medellín | ⚠️ Sin datos (401) | — | — |
| Barranquilla | ⚠️ Sin datos (401) | — | — |
| Bucaramanga | ⚠️ Sin datos (401) | — | — |
| Panamá | ⚠️ Sin datos (401) | — | — |
| **TOTAL** | **⚠️ Sin datos** | **—** | |

Benchmark referencia Bogotá: 105–175 leads/semana (15–25/día).

## Alertas 🚨

- 🚨 **Token GHL expirado — 5ª semana / deadline incumplido:** ninguna subcuenta responde (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá). El agency token lista locations pero los tokens por subcuenta (PIT) están caídos → 401 "location not accessible". La renovación tenía fecha límite hoy (15 Jun) y no se hizo.
- 🚨 **Ninguna cuenta Meta rastrea el evento `lead`:** CPL formal no calculable en las 4 cuentas. Proxy actual = costo por conversación WA iniciada. Crítico en **Panamá** (sin objetivo Lead) y **Medellín**.
- 🚨 **Medellín — alta inversión sin leads rastreados:** $780.407 COP el 11 Jun, costo/conversación WA $9.517 COP (82 convs). Confirmar que los leads aterrizan en GHL.
- 🚨 **Bucaramanga sin bot IA — semana 4+:** bot nunca activado. Leads acumulados en `landing_formulario` sin seguimiento comercial.
- 🚨 **Won tracking roto (Bogotá, Medellín, Panamá):** sin métricas de cierre. Imposible calcular CPL real ni ROAS.
- ⚠️ **LANDING DIEGO — 0 conversaciones DM:** CTR 10,82% pero sin mensajería. Revisar objetivo de campaña y campañas 2025 aún activas.
- ⚠️ **BGTA — CTR 1,11% marginal:** apenas sobre el umbral del 1%. Monitorear; rotar creativos si baja.
- ⚠️ **Casos "asistió y no pagó" en Panamá:** sin confirmación de cierre desde semana 20.

## Pipeline GHL

> ⚠️ Sin datos — API no disponible (5ª semana). Última lectura válida en [[50-Reportes/2026/semana-22]].

| Etapa | Bogotá | Medellín | BQ | BGA | PTY |
|-------|--------|----------|----|-----|-----|
| Nuevos | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| Contactados | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| En seguimiento | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| Won | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |

## Observaciones del equipo
_Espacio para agregar notas manuales después de generar_

## Pendientes para esta semana
- [ ] **🔴 P0 — Renovar token GHL (5ª semana, deadline incumplido):** generar nuevo API key / PIT con acceso a las 5 subcuentas. Sin esto el reporte semanal seguirá ciego. Escalar al administrador de GHL hoy.
- [ ] Verificar manualmente leads 8–14 Jun 2026 en GHL (filtro: fecha de creación) por ciudad
- [ ] Configurar evento `lead` en las 4 cuentas Meta para habilitar CPL real (prioridad Panamá y Medellín)
- [ ] Confirmar recarga de presupuesto en campaña `CLIENTES POTENCIALES FASE 3` Medellín
- [ ] Cerrar casos "asistió y no pagó" en Panamá (pendiente desde semana 20)

## Pendientes arrastrados (sin completar la semana pasada)
- [ ] Resolver acceso 401 a subcuenta Bogotá en GHL — [[50-Reportes/2026/semana-24]]
- [ ] Diagnosticar y activar bot IA en Bucaramanga — [[50-Reportes/2026/semana-24]]
- [ ] Activar won tracking en Medellín y Panamá — [[50-Reportes/2026/semana-24]]
- [ ] Activar tracking de leads en PANAMÁ (objetivo campaña) — [[50-Reportes/2026/semana-23]]
- [ ] Revisar campañas 2025 activas en LANDING DIEGO — [[50-Reportes/2026/semana-23]]
- [ ] Definir benchmarks leads/semana por ciudad (BQ, BGA, PTY) — [[50-Reportes/2026/semana-22]]
- [ ] Monitorear frecuencia/CTR BGTA — rotar creativos si CTR baja del 1% — [[50-Reportes/2026/semana-23]]
- [ ] Verificar pixel Medellín — confirmar que los leads llegan a GHL — [[50-Reportes/2026/semana-23]]

---
_Generado automáticamente el 2026-06-15 a las 08:00_
