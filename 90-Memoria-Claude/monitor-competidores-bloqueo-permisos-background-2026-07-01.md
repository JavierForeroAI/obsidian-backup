---
name: monitor-competidores-bloqueo-permisos-background
description: El monitor semanal de competidores falla en agentes background/async — Playwright inspection, WebFetch y curl están denegados por permisos en ese entorno
metadata:
  type: project
---

# Monitor de Competidores — bloqueo de infraestructura (semana 27, 2026-07-01)

La automatización semanal (miércoles 9am, ver `20-Pauta/Competidores/_instrucciones-monitor.md`)
lanza 4 agentes en paralelo (uno por competidor: Mediarte, HERO Institute, DHI Colombia,
Rogans Care) para navegar sitios y Meta Ads Library con Playwright.

En la corrida de la semana 27, **los 4 agentes fallaron en obtener contenido real**:
- `mcp__playwright__browser_navigate` sí funcionó (las URLs cargaron).
- `browser_snapshot`, `browser_evaluate`, `browser_take_screenshot`, `browser_console_messages`
  fueron **denegados por permisos** en el entorno de ejecución en background.
- `WebFetch` también fue denegado.
- `Bash`/`curl` también fue denegado.
- Resultado: el reporte `20-Pauta/Competidores/2026/semana-27.md` quedó con casi todos los
  campos "no verificable esta semana" — no debe tomarse como base para decisiones.

**Hallazgo real que sí se detectó pese al bloqueo:** el dominio `heroinstitute.com.co` no
resolvió DNS (`ERR_NAME_NOT_RESOLVED`) en ninguna variante — posible caída del sitio o
cambio de dominio de HERO Institute. Pendiente de verificación manual.

**Why:** los agentes lanzados en background (vía `Agent`/subagentes async, no la sesión
interactiva principal) parecen heredar un set de permisos más restrictivo que no incluye
las herramientas de lectura de Playwright ni `WebFetch`/`Bash` para este entorno. Esto no
es un problema del contenido/prompt de la automatización, sino de permisos del entorno.

**How to apply:** antes de la próxima corrida (semana 28, miércoles 2026-07-08), verificar
si se puede habilitar `mcp__playwright__browser_snapshot` (o `browser_evaluate`/`WebFetch`)
como allowlist permanente para agentes background en este proyecto, o rediseñar el monitor
para correr en la sesión interactiva en vez de agentes async. Si no se resuelve, la
automatización semanal seguirá produciendo reportes vacíos.
