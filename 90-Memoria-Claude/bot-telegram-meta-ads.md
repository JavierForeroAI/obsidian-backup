---
name: bot-telegram-meta-ads
description: Bot de Telegram (@Innovart_meta_bot) que es un agente Claude sobre Telegram — el trafficker pide reportes Meta Ads en lenguaje natural y el bot llama los MCPs de Meta en vivo
metadata:
  type: project
---

# Bot de Telegram — Meta Ads Innovart (@Innovart_meta_bot)

**Fecha:** 2026-06-20. Sistema nuevo, construido y probado en vivo el mismo día.

## Qué es
Un **agente Claude sobre Telegram**: el trafficker escribe en lenguaje libre (español)
como si estuviera en la terminal, y el bot llama los **MCPs de Meta Ads en tiempo real**
y responde en el chat (~20–40 s por consulta). No es un menú de comandos fijos: entiende
preguntas abiertas sobre leads, CPL, gasto, campañas, creativos, UTMs, comparativas y
alertas de las 6 cuentas / 5 sedes. También puede disparar el reporte completo
("genera un reporte de Metaadsinnovart" → HTML+PDF a Drive).

## Arquitectura
- **Carpeta:** `/Users/javierforero/meta-ads-telegram-bot/` (`bot.py`, `requirements.txt`,
  `.env`, `start.sh`).
- **Cómo funciona:** `bot.py` (python-telegram-bot 21.6, `python3.12`) escucha los mensajes y
  por cada uno invoca el **CLI de `claude` en modo headless** (`CLAUDE_BIN=/opt/homebrew/bin/claude`)
  que consulta los MCPs de Meta y devuelve la respuesta al chat.
- **Config en `.env`** (fuente de verdad, no copiar el token a memoria):
  `TELEGRAM_BOT_TOKEN`, `ALLOWED_USERS` (hoy vacío = TODOS autorizados ⚠️), `CLAUDE_BIN`.
- **Bot:** username **@Innovart_meta_bot** — "Innovart Meta Ads Reports".
- **Arranque:** `bash /Users/javierforero/meta-ads-telegram-bot/start.sh` (o
  `nohup python3.12 bot.py`). Log en `/tmp/meta-ads-bot.log`. Solo una instancia a la vez
  (dos instancias → conflicto de polling de Telegram).

## Estado / pendientes
- ✅ Probado de punta a punta: el bot conecta y responde consultas reales
  (p.ej. "gasto del día", "mejor creativo de todas las cuentas").
- ⚠️ **Corre solo mientras la Mac/terminal esté encendida.** Pendiente convertirlo en
  servicio `launchd` para que corra 24/7.
- ⚠️ **`ALLOWED_USERS` vacío = cualquiera puede usarlo.** Restringir a usernames del equipo
  (trafficker + Javier) antes de compartirlo ampliamente.

Relacionado: [[meta-mcp-guia]] · [[feedback-cuentas-meta-no-son-sedes]] · [[reporte-diario-meta-automatico]]
