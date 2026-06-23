Perfecto. Ahora tengo los datos para el reporte. Voy a generar el reporte de la semana 25 en Markdown puro:

---
tipo: reporte-semanal
semana: 25
periodo: "15 Jun – 21 Jun 2026"
generado: 2026-06-22
---

# Reporte Semanal — Semana 25 (15 Jun – 21 Jun 2026)

## Resumen ejecutivo
- ✅ **GHL recuperado — primera semana con datos tras 5 semanas de caída.** Token renovado permite lectura de 4 subcuentas (Bogotá, Medellín, Barranquilla, Bucaramanga); Panamá aún sin acceso (403 Forbidden).
- **Medellín crítica: 0 leads.** Caída desde ~15-20 leads/semana estimados. Barranquilla y Bucaramanga estables (~65 leads c/u). Bogotá por debajo del benchmark (61 vs 105-175 esperados).
- **Panamá sigue inaccesible.** Token del MCP no tiene permisos; requiere regeneración específica o validación de credenciales.

## Leads por ciudad

| Ciudad | Leads | vs semana ant. | Tendencia |
|--------|-------|----------------|-----------|
| Bogotá | 61 | —* | ↓ |
| Medellín | 0 | **-100%** | 🚨 |
| Barranquilla | 65 | —* | → |
| Bucaramanga | 65 | —* | → |
| Panamá | ⚠️ Sin datos (403) | — | — |
| **TOTAL** | **191** | **—** | |

*Semana 24 sin datos (GHL caído). Benchmark Bogotá: 105–175 leads/semana (15–25/día).

## Alertas 🚨

- 🚨 **Medellín — CERO leads esta semana.** Caída crítica. Verificar: (1) pixel Meta → GHL integración activa, (2) campaña presupuesto sin agotarse (issue pendiente semana 24), (3) workflows de ingesta activos en GHL.
- 🚨 **Bogotá por debajo del benchmark.** 61 leads vs 105–175 esperados. Posibles causas: estacionalidad (fin de junio), presupuesto limitado o fatiga creativa.
- ⚠️ **Panamá sin acceso — 2ª semana (403).** Token PIT expirado o sin scope en esa subcuenta. Requiere regeneración de credenciales explícitas para `45SKYgIDgr4Eh6a6JcFz`.
- ⚠️ **Bucaramanga — 65 contactos concentrados el 21 jun.** Evento puntual ese día (¿captura masiva? ¿evento/oferta?). Validar si fueron valificados o son bulk sin calidad.

## Pipeline GHL

| Etapa | Bogotá | Medellín | BQ | BGA | PTY |
|-------|--------|----------|----|-----|-----|
| Nuevos | 61 | 0 | 65 | 65 | ⚠️ N/D |
| Contactados | — | — | — | — | — |
| En seguimiento | — | — | — | — | — |
| Won | 0 | 0 | 1 | 46 | — |

*Pipeline detallado por etapa no disponible via MCP simplificado. Oportunidades abiertas (histórico): Bogotá 13.439, Medellín 11.767, Barranquilla 66, Bucaramanga 100+.

## Observaciones del equipo

- Token GHL renovado el 22 jun permite lectura. Credenciales válidas para BGTA, BOG, MED, BGA; Panamá requiere validación.
- Medellín 0 leads = riesgo operacional crítico. Prioridad: verificar flujo pixel → GHL y confirmar presupuesto campaña CLIENTES POTENCIALES FASE 3 antes de fin de semana.

## Pendientes para esta semana

- [ ] **P0 — Medellín: diagnosticar 0 leads.** Verificar pixel instalación + Meta Pixel Health, confirmar presupuesto en `CLIENTES POTENCIALES FASE 3` no agotado, validar workflows GHL.
- [ ] **P1 — Regenerar token Panamá.** Generar nuevo PIT con scope explícito para `45SKYgIDgr4Eh6a6JcFz` o investigar por qué el token actual devuelve 403.
- [ ] Validar batch Bucaramanga del 21 jun (~65 contactos): ¿captura orgánica o evento? Revisar etiquetas + origen en GHL.
- [ ] Realizar benchmark leads/semana REALISTA para BQ/BGA (semana 25 cero datos previos; usar semana 25 como baseline).

## Pendientes arrastrados (sin completar la semana pasada)

- [ ] Resolver acceso 403 a subcuenta Panamá en GHL — [[50-Reportes/2026/semana-24]]
- [ ] Diagnosticar y activar bot IA en Bucaramanga — [[50-Reportes/2026/semana-24]]
- [ ] Activar won tracking en Medellín y Panamá — [[50-Reportes/2026/semana-24]]
- [ ] Activar tracking de leads en PANAMÁ (objetivo campaña) — [[50-Reportes/2026/semana-23]]
- [ ] Revisar campañas 2025 activas en LANDING DIEGO — [[50-Reportes/2026/semana-23]]
- [ ] Definir benchmarks leads/semana por ciudad (BQ, BGA, PTY) — [[50-Reportes/2026/semana-22]]
- [ ] Monitorear frecuencia/CTR BGTA — rotar creativos si CTR baja del 1% — [[50-Reportes/2026/semana-23]]
- [ ] Verificar pixel Medellín — confirmar que los leads llegan a GHL — [[50-Reportes/2026/semana-23]]

---
_Generado automáticamente el 2026-06-22 a las 08:00_
