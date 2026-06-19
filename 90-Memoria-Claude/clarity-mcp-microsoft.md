---
name: clarity-mcp-microsoft
description: MCP oficial de Microsoft Clarity para análisis de heatmaps/navegabilidad de landings + token Data Export y límites de la API
metadata:
  type: reference
---

# Microsoft Clarity — MCP oficial + token Data Export

Herramienta elegida para análisis de navegabilidad / comportamiento de las landings
(heatmaps, rage clicks, dead clicks, scroll, grabaciones). Verificada como la opción
**más segura y más usada de la industria** (2026-06-18).

## La herramienta: `@microsoft/clarity-mcp-server`
- Repo first-party Microsoft: https://github.com/microsoft/clarity-mcp-server (MIT, 88★/32 forks)
- npm: `@microsoft/clarity-mcp-server` v2.0.1 — ~16.6K descargas/mes
- Publicado por el pipeline seguro de Microsoft (`microsoft1es`, `microsoft-oss-releases`)
- `npm audit`: **0 vulnerabilidades**; solo 2 deps (`zod`, `@modelcontextprotocol/sdk`); firmas npm presentes
- Docs: https://learn.microsoft.com/en-us/clarity/third-party-integrations/clarity-mcp-server
- Tools que expone: `query-analytics-dashboard`, `list-session-recordings`, `query-documentation-resources`

## ⚠️ TOKEN Data Export (guardado por pedido explícito de Javier — texto plano)
> Javier pidió guardarlo aquí pese a la advertencia. **Está expuesto en el chat → REGENERAR**
> en Clarity (Settings → Data Export → Generate new API token) y reemplazar abajo.
> Scope: `Data.Export`. Proyecto (sub): `3368589194891752`.

```
eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ4M0FCMDhFNUYwRDMxNjdEOTRFMTQ3M0FEQTk2RTcyRDkwRUYwRkYiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI2MjM0NTkwNy1lYmExLTQwMTAtOTZlMy1jZGQwNTk1MWU3ZWEiLCJzdWIiOiIzMzY4NTg5MTk0ODkxNzUyIiwic2NvcGUiOiJEYXRhLkV4cG9ydCIsIm5iZiI6MTc4MTc5NTgwOSwiZXhwIjo0OTM1Mzk1ODA5LCJpYXQiOjE3ODE3OTU4MDksImlzcyI6ImNsYXJpdHkiLCJhdWQiOiJjbGFyaXR5LmRhdGEtZXhwb3J0ZXIifQ.XkfLVn3xyU4Xh_GQpUxpVwsw_q-9YiFCQ0o9Z5sWyUBdTs_cn3qayo3Ys6S9Cfo6D9Ur98FKwMZhkCFgV0X5q5DA7f1R4aENSf4y0ad_gwIbex21rcz_rS7RzKrjgzpoh78rO-Ym8kSctXfmn92f_zcShTj9U0OpQkaXQ8Zmj5tNZmeqvrOrRd16USs0WMAuoOJodiAdSBRSC2NHilr13RN_WnvYl2a4Fkw6BusMjP6Ch4QD22c-3mN7YckIa380DAG6zpGOlV8ju4szSaiBK3Eqv0cCAQHoBQgaXgWrasNwN55LGUPEUA3jyTr1X-wBWDaZzBqMuxnY6Do7n5b05A
```

## Cómo conectarlo (Claude Code)
```
claude mcp add clarity -- npx -y @microsoft/clarity-mcp-server --clarity_api_token=<TOKEN>
```
Requiere **reiniciar Claude Code** para que el MCP cargue en la sesión.

## API directa (sirve YA, sin reiniciar)
```
GET https://www.clarity.ms/export-data/api/v1/project-live-insights?numOfDays=3&dimension1=Device
Header: Authorization: Bearer <TOKEN>
```

## ⛔ LÍMITES DUROS (clave para análisis multi-agente)
- **10 llamadas/día por proyecto** · **máx 3 días** hacia atrás · **máx 3 dimensiones** por request.
- Por eso NO fan-out de agentes contra la API: **pull 1 vez → cachear local → varios agentes analizan el caché**.
- Heatmaps visuales y grabaciones NO salen por API (solo UI) → esos se pegan como captura.

Relacionado: [[stack-pauta]] · análisis CRO de landing (skills page-cro / ads-landing).
