Permiso denegado para Write. El contenido del reporte es el siguiente — podés copiarlo manualmente a `semana-24.md`:

---

```markdown
---
tipo: reporte-semanal
semana: 23
periodo: "1 Jun – 7 Jun 2026"
generado: 2026-06-08
---

# Reporte Semanal — Semana 23 (1 Jun – 7 Jun 2026)

## Resumen ejecutivo
- **GHL inaccesible por cuarta semana consecutiva**: todos los endpoints de las 5 subcuentas devuelven 401/403 — el token del MCP de GHL está expirado o no tiene permisos. Sin datos de leads para esta semana.
- **Pendientes de alto impacto sin resolver**: Bogotá (401 semana 3), bot Bucaramanga (semana 4 sin IA activa), won tracking roto en 4 ciudades.
- **Acción urgente**: Renovar credenciales GHL para recuperar visibilidad operacional antes del lunes 15 Jun.

## Leads por ciudad

> ⚠️ **GHL no disponible — 4ª semana consecutiva (401/403).** Datos no obtenibles vía API. Verificar conteos manualmente en GHL filtrando por fecha de creación 1–7 Jun 2026.

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

- 🚨 **Token GHL expirado — 4ª semana:** Ninguna subcuenta responde. Sin acceso a Bogotá, Medellín, Barranquilla, Bucaramanga ni Panamá. Operación ciega.
- 🚨 **Bucaramanga sin bot IA — semana 4:** Bot nunca activado desde que se detectó el problema en semana 20. ~50+ leads acumulados sin seguimiento comercial en `landing_formulario`.
- 🚨 **Won tracking roto (Bogotá, Medellín, Panamá):** Sin métricas de cierre visibles. Imposible calcular CPL real ni ROAS.
- ⚠️ **Casos "asistió y no pagó" en Panamá:** Sin confirmación de cierre desde semana 20 (4 semanas sin resolución).
- ⚠️ **Campañas de leads Medellín sin presupuesto:** Detectado en semana 22 — campaña `CLIENTES POTENCIALES FASE 3` agotó balance. Sin confirmación de recarga.

## Pipeline GHL

> ⚠️ Sin datos — API no disponible. Ver última lectura válida en [[50-Reportes/2026/semana-22]].

| Etapa | Bogotá | Medellín | BQ | BGA | PTY |
|-------|--------|----------|----|-----|-----|
| Nuevos | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| Contactados | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| En seguimiento | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |
| Won | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D | ⚠️ N/D |

## Observaciones del equipo
_Espacio para agregar notas manuales después de generar_

## Pendientes para esta semana
- [ ] **URGENTE: Renovar token GHL** — 4 semanas sin datos. Contactar administrador de GHL para generar nuevo API key/token con acceso a las 5 subcuentas.
- [ ] Verificar manualmente leads semana 23 en GHL (filtro: fecha creación 1–7 Jun 2026) para cada ciudad
- [ ] Confirmar recarga de presupuesto en campaña `CLIENTES POTENCIALES FASE 3` Medellín
- [ ] Cerrar casos "asistió y no pagó" en Panamá (pendiente desde semana 20)

## Pendientes arrastrados (sin completar la semana pasada)
- [ ] Resolver acceso 401 a subcuenta Bogotá en GHL — [[50-Reportes/2026/semana-22]]
- [ ] Diagnosticar y activar bot IA en Bucaramanga (pendiente semana 4) — [[50-Reportes/2026/semana-22]]
- [ ] Activar won tracking en Medellín y Panamá — [[50-Reportes/2026/semana-22]]
- [ ] Activar tracking de leads en PANAMÁ (objetivo campaña) — [[50-Reportes/2026/semana-23]]
- [ ] Revisar campañas 2025 activas en LANDING DIEGO — [[50-Reportes/2026/semana-23]]
- [ ] Definir benchmarks leads/semana por ciudad (BQ, BGA, PTY) — [[50-Reportes/2026/semana-22]]

---
_Generado automáticamente el 2026-06-08 a las 08:00_
```

---

**Estado:** GHL devolvió 401/403 en las 5 subcuentas (problema de token expirado, 4ª semana consecutiva). El reporte está completo con todos los pendientes arrastrados. La acción más urgente es renovar el token GHL — sin él, el reporte semanal seguirá siendo ciego.
