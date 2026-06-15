---
name: reporte-auditoria-capimetaghl-automatico
description: "Monitor de SALUD del sistema CAPIMETAGHL (6 sedes GHL ↔ Meta) automatizado vía cron local — verifica que la comunicación GHL→Meta esté fluyendo, config por sede, alertas. Diario a Drive + correo semanal. v2 2026-06-14."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e59d124-363f-4666-9838-f5c75f5725c2
---

# Monitor de salud CAPIMETAGHL — automatización (v2, 2026-06-14)

Cron local en la Mac de Javier que cada mañana **verifica que el CAPI esté fluyendo GHL→Meta** (no es conteo de leads), revisa config por sede y alerta lo roto. Base/estándar: [[auditoria-capimetaghl-base]].

## Arquitectura
| Cuándo | Cron | Qué hace |
|---|---|---|
| Diario 7:30 | `30 7 * * *` | `audit-capimetaghl.py` → HTML a Drive |
| Lunes 7:45 | `45 7 * * 1` | `audit-capimetaghl.py --weekly` → HTML a Drive **+ correo** |

- **Script:** `~/.claude/scripts/audit-capimetaghl.py` (solo stdlib).
- **Salida local:** `~/.claude/reports/salud-capimetaghl-AAAA-MM-DD.html`
- **Drive destino:** `CONFIGURACIONAPICONVERSIONMETAGHL/REPORTES` id `1hpDYd5jVT9H8jakkcPcfopZA2EtkDpvx` (padre `CONFIGURACIONAPICONVERSIONMETAGHL` = `1tQlCpjlYRVN8c9rsiqef_h1h8DxcCMs5`). Sube por folder ID con rclone.
- **Logs:** `~/.claude/logs/capimetaghl.log` y `capimetaghl-weekly.log`.

## Qué mide (monitor de salud, NO leads del CRM)
1. **Comunicación GHL→Meta fluyendo:** manda 1 evento real **HealthCheck** por el worker `innovart-capi-webhook-no-tocar` y lee `events_received` por píxel (✅ si =1 en los 2). + worker `debug` (recibe/parsea).
2. **Eventos CAPI recibidos por Meta (48h):** lee `graph.facebook.com/v21.0/{pixel}/stats?aggregation=event` por píxel y muestra volumen por evento (Lead, Purchase, Schedule, etc.) → confirma qué está llegando.
3. **Config por sede:** lista workflows (API pública GHL `/workflows`) y verifica que los workflows CAPI esperados existan y estén `published` (IDs en `CAPI_WF` del script). + "en cirugía" (Operaciones›Programación) como Purchase esperados.
4. **Alertas** automáticas (worker caído, Lead/Purchase=0 en 48h, workflow no publicado).
5. **Checklist de landing nueva** + lista de mejoras abiertas (secciones fijas).

## Detalles técnicos clave
- **Tokens GHL:** registro fresco del MCP ghl en `~/Library/Application Support/elitedcs-ghl-mcp/.ghl-tokens.json` (`tokens[loc].apiKey`); fallback env `gohighlevel` en `~/.claude.json`.
- **Token Meta:** `~/.claude.json` → `mcpServers.meta-dajf.env.META_ACCESS_TOKEN`.
- ⚠ **Cloudflare Error 1010:** GHL y los workers banean el UA por defecto de urllib → el script manda User-Agent de navegador (incluido).
- El **HealthCheck** manda a Meta un evento llamado `HealthCheck` (no se usa para optimización, inofensivo) — es la prueba diaria end-to-end.
- Nota observada 2026-06-14: el píxel `1642…0262` muestra 0 en eventos server (Lead/Purchase) aunque events_received=1; el `1625…4016` sí los registra. Vigilar (posible config de 0262) — el reporte muestra ambas columnas.

## Correo semanal (PENDIENTE 1 paso de Javier)
- Lee `~/.claude/scripts/.capimetaghl-mail.json` → `{"user","app_password","to"}` (hay `.example`).
- Falta crear **App Password de Gmail** y pegarlo. Mientras tanto el lunes igual sube a Drive; el correo se omite con aviso en log.

## Caveats
- La Mac debe estar **encendida y despierta** a las 7:30/7:45 (cron no la despierta). Mitigación: `sudo pmset repeat wakeorpoweron MTWRFSU 07:28:00`.
- EMQ/calidad de match no se lee desde el cron (endpoint distinto) → revisar vía MCP `ads_get_dataset_quality` semanal (checklist C2 en [[auditoria-capimetaghl-base]]).

## Estado
- v2 validado en local 2026-06-14: Comunicación FLUYENDO (HealthCheck OK 2 píxeles), Meta 48h Lead 32 / Purchase 4 / Schedule 2, todos los workflows CAPI `published`, sin alertas. **No se subió informe el 2026-06-14 (a pedido). Primera corrida automática: 2026-06-15 7:30 → REPORTES.**

Relacionado: [[auditoria-capimetaghl-base]] · [[integracion-ghl-meta-capi]] · [[capi-webhook-worker]] · [[reporte-diario-meta-automatico]]
