---
name: reporte-diario-meta-automatico
description: Sistema automático de reporte diario Meta Ads (HTML→PDF→Drive) vía 2 crons locales en la Mac
metadata:
  type: project
---

# Reporte diario Meta Ads — automatización (montado 2026-06-13)

Sistema de **2 crons locales** en la Mac de Javier que genera y entrega cada mañana
un reporte detallado por campaña de las 6 cuentas Meta de Innovart, como PDF en Drive.

## Arquitectura

| Hora | Cron | Script | Qué hace |
|------|------|--------|----------|
| 8:00am | `0 8 * * *` | `~/.claude/scripts/generate-meta-report.py` | Consulta API Graph Meta (datos de AYER, nivel campaña), genera HTML email-safe, sube a Drive |
| 8:25am | `25 8 * * *` | `~/.claude/scripts/convert-meta-report.sh` | Baja el HTML, lo pasa a PDF con Chrome headless, sube el PDF a Drive |

- **Destino Drive:** carpeta **`Informesdiariosmeta`** dentro de `3.MERCADEO/CLAUDE/TRAFICO ESN DIEGO JAVIER/`. **Folder ID `1XFEluaAao-mpp8rnDMKL2JirHp2WlWNl`** (cuenta innovartmedicalips@gmail.com). Los scripts suben **por ID** con `rclone ... "gdrive,root_folder_id=1XFEluaAao-mpp8rnDMKL2JirHp2WlWNl:"`, NO por ruta `gdrive:informesdiariosmeta` (esa creaba una carpeta suelta en la raíz del remote — error corregido 2026-06-13).
- **Logs:** `~/.claude/logs/meta-gen.log` y `~/.claude/logs/meta-pdf.log`.
- **Nombre archivos:** `auditoria-meta-AAAA-MM-DD.html` / `.pdf` (fecha = día de ejecución; contenido = día anterior).

## Detalles técnicos clave

- **Token Meta:** el script lo lee **dinámicamente** de `~/.claude.json` (env `META_ACCESS_TOKEN` del MCP `meta-dajf`). No está hardcodeado → si el token rota en el MCP, el reporte sigue funcionando. Si el token expira y nadie lo renueva, ambos crons fallan (revisar logs).
- **Solo stdlib de Python** (`urllib`, `json`, `subprocess`) → corre con `/usr/bin/python3`, sin pip.
- **Métrica "Resultado"** = `onsite_conversion.messaging_conversation_started_7d` (conversaciones WhatsApp), con fallback a leads de pixel/form según objetivo de cada cuenta.
- **Monedas separadas:** USD (BGTA, QUILLA, PANAMA) y COP (Interacción, Landing, Medellín). Nunca se suman entre sí.
- **Comparativo:** cada cuenta muestra variación ▲/▼ vs el día anterior.
- Formato HTML email-safe (tablas + inline styles), cumple [[feedback-email-formato]].

## Cuentas y un hallazgo importante

`account_status 9` NO es "desactivada" → es **PERÍODO DE GRACIA** (problema de facturación, la cuenta SIGUE gastando pero en riesgo de corte).
- **MEDELLIN** (status 9) es la **mayor inversión** (~$900K COP/día, ~97 resultados) y **PANAMA** (status 9) también gasta. El reporte las marca con chip ámbar "⚠ PERÍODO DE GRACIA". **Acción pendiente: resolver facturación de MEDELLIN y PANAMA para evitar corte.**

## Acción a demanda (tiempo real) — agregado 2026-06-13

Además del cron, hay una **acción manual** para sacar el reporte al instante cuando Javier lo pida
(frase disparadora: *"Generar un reporte de Metaadsinnovart"*, registrada en el CLAUDE.md global):

```
~/.claude/scripts/reporte-meta-ondemand.sh <preset>
```
- Default `today` (hoy en vivo, parcial). Presets: `today yesterday last_3d last_7d last_14d last_30d this_month last_month`.
- Genera HTML + PDF (nombre `metaadsinnovart-ondemand-...`, NO pisa el del cron), sube ambos a Drive e imprime un `=== RESUMEN ===` en texto para relayear en chat.
- También disponible como slash command **`/reporte-meta [preset]`** (`~/.claude/commands/reporte-meta.md`).
- El motor `generate-meta-report.py` ahora acepta `--preset` / `--since`/`--until` / `--tag` / `--no-upload`. Sin args = modo cron (ayer, `auditoria-meta-HOY.html`). `convert-meta-report.sh` acepta un nombre de HTML como 1er argumento (sin arg = el del cron).

## Caveats de confiabilidad

1. **La Mac debe estar encendida y despierta** a las 8:00 y 8:25. macOS `cron` no despierta la máquina dormida. Si falla seguido, migrar a `launchd` o programar wake con `pmset`.
2. Primer corrida real automática: **2026-06-14 8:00am**. Validado manualmente el 2026-06-13 (HTML + PDF generados y subidos OK).

## Historial

- Montaje original (11-12 jun): quedó a medias y roto — faltaba el generador 8am, carpeta `~/.claude/logs/` inexistente (cron nunca corría), ruta rclone equivocada (`/usr/local/bin` en vez de `/opt/homebrew/bin`).
- 2026-06-13: diagnosticado y reparado por completo; construido el generador determinista; validado end-to-end.
- 2026-06-13 (tarde): corregido destino Drive. El `rclone mkdir gdrive:informesdiariosmeta` había creado una carpeta SUELTA en la raíz del remote (Shared Drive), no dentro de TRAFICO ESN DIEGO JAVIER. La carpeta correcta `Informesdiariosmeta` (id `1XFEluaAao...`) ya existía anidada bien desde el inicio. Se movieron los archivos a la correcta, se borró la suelta, y los scripts ahora direccionan por **folder ID**.

Relacionado: [[meta-mcp-guia]] · [[stack-pauta]] · [[feedback-informes-drive]]
