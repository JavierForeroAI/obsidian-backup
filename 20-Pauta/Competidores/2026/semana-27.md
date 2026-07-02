---
tipo: monitor-competidores
semana: 27
fecha: 2026-07-01
---

# Monitor Competidores — Semana 27

## Resumen ejecutivo
- ⚠️ **Bloqueo de infraestructura esta semana:** todas las herramientas de lectura web (Playwright snapshot/evaluate/screenshot, WebFetch, curl vía Bash) fueron denegadas por permisos en este entorno automatizado — solo se pudo confirmar que las URLs cargan, sin poder leer contenido real. El monitoreo de esta semana es **incompleto y no debe tomarse como base para decisiones**.
- 🚨 **Hallazgo real detectado pese al bloqueo:** el dominio `heroinstitute.com.co` (sitio de HERO Institute) no resolvió DNS en ninguna variante (`ERR_NAME_NOT_RESOLVED`) — posible caída del sitio o cambio de dominio. Vale la pena verificar manualmente.
- Acción recomendada: habilitar permisos permanentes de `WebFetch` y/o Playwright (`browser_snapshot`, `browser_evaluate`) para la automatización semanal de este monitor, para que los próximos reportes traigan datos reales.

## Mediarte

### Sitio web
- Cambios detectados: no verificable esta semana (bloqueo de permisos)
- CTA hero: no verificable esta semana
- Promociones: no verificable esta semana
- Nota: la URL cargó correctamente (título de pestaña "Implante capilar Bogotá | Resultados naturales – Mediarte"), pero no se pudo leer contenido.

### Meta Ads
- Anuncios activos: no verificable esta semana
- Formatos: no verificable esta semana
- Ángulo dominante: no verificable esta semana
- Novedades vs semana anterior: no verificable esta semana

### Google Maps
- Rating: no verificable esta semana
- Tendencia reviews: no verificable esta semana

---

## HERO Institute

### Sitio web
- 🚨 `heroinstitute.com.co` no resolvió DNS (raíz ni `www.`) — el sitio parece caído o cambió de dominio. Requiere verificación manual urgente.
- CTA hero: no verificable
- Promociones: no verificable

### Meta Ads
- Anuncios activos: no verificable esta semana (bloqueo de permisos)
- Ángulo dominante: no verificable esta semana
- Novedades: no verificable esta semana

### Google Maps
- Rating: no verificable esta semana
- Tendencia reviews: no verificable esta semana

---

## DHI Colombia

### Meta Ads
- Anuncios activos: no verificable esta semana (bloqueo de permisos)

### Google Maps
- Rating: no verificable esta semana
- Tendencia reviews: no verificable esta semana

---

## Rogans Care

### Sitio web (https://rogansya.com/implantes-capilares/)
- Cambios en headline/CTA: no verificable esta semana (bloqueo de permisos)
- Cambios en precios o garantía: no verificable esta semana
- Nuevas secciones o testimonios: no verificable esta semana
- Nota: la URL cargó correctamente (título de pestaña "Implantes Capilares ROGANS CARE"), pero no se pudo leer contenido.

### Meta Ads
- Anuncios activos: no verificable esta semana
- Formatos: no verificable esta semana
- Ángulo dominante: no verificable esta semana
- Novedades vs semana anterior: no verificable esta semana

### Google Ads
- ¿Aparece en búsqueda "implante capilar colombia"?: no verificable esta semana
- Copy del anuncio detectado: no verificable esta semana

### Google Maps
- Rating: no verificable esta semana
- Tendencia reviews: no verificable esta semana

---

## Alertas y oportunidades 🚨

- **P0 — Infraestructura del monitor rota:** el reporte automático de esta semana no pudo capturar ningún dato real porque las herramientas de lectura web (Playwright snapshot/evaluate, WebFetch, curl) están denegadas por permisos en el entorno donde corre este cron. Hay que revisar la configuración de permisos (`settings.json` / allowlist de herramientas) para que las próximas ejecuciones automáticas de `monitor-competidores` puedan leer contenido, no solo navegar.
- **Verificar manualmente:** ¿`heroinstitute.com.co` sigue siendo el dominio correcto de HERO Institute? El DNS no resolvió en el intento automático.
- Sin datos frescos esta semana, no hay base para detectar movimientos reales de precio, creativos o reviews vs. semana 26 — el próximo reporte (semana 28) debería traer doble ventana de comparación una vez resuelto el bloqueo.

## Recomendaciones para Innovart
1. Arreglar el acceso de herramientas del monitor (habilitar WebFetch/Playwright con permisos persistentes) antes del próximo miércoles, para no perder otra semana de inteligencia competitiva.
2. Verificar manualmente si HERO Institute cambió de dominio o está caído — si es caída prolongada, es una ventana de oportunidad para captar búsquedas de su marca.
3. Retomar el monitoreo completo de Mediarte y Rogans Care la próxima semana en cuanto se resuelva el bloqueo, dado que ambos venían con actividad relevante en semanas anteriores (Rogans con campaña activa en Google Ads, Mediarte con presencia fuerte en Meta).

---
_Monitor generado automáticamente el 2026-07-01 a las 09:00_
