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

## Capacidades clave

### 1. **Reportes en tiempo real** ✅
- Gasto por campaña/sede/día
- Leads y CPL
- Performance de creativos (CTR, CPC, CPM)
- Comparativas período vs período
- Detección automática de anomalías

### 2. **Generador de UTMs Inteligente** ✅ (2026-06-22)

**Tres modos:**

**MODO 1 — Analizar ad publicado → Sugerir UTMs** ⭐
Esneider envía nombre del ad/campaña:
```
"UTMs para el ad 'Testimonio Bogotá Video 01'"
"Dame parámetros para 'Implante Capilar TOFU'"
```
El bot:
1. Busca el ad en Meta en vivo
2. Obtiene: objetivo (Leads/Traffic/Conversions), plataforma (IG/FB), ciudad, creativo
3. Analiza tipo (TOFU/MOFU/BOFU) automáticamente
4. Devuelve sugerencia:
```
Basándome en tu campaña "Implante Capilar TOFU" (objetivo: Leads, Instagram, Bogotá):
https://implantecapilarencolombia.com/landing?utm_source=instagram&utm_medium=paid_social&utm_campaign=tofu_bogota_leads&utm_content=video_testimonio&utm_term=leads
```

**MODO 2 — Generar desde descripción**
```
"UTMs para TOFU Instagram Bogotá"
"Parámetros para campaña de ebook"
```
El bot pregunta detalles si falta info y devuelve URL lista.

**MODO 3 — Auditar UTMs existentes**
```
"Muéstrame los UTMs activos"
"Qué UTMs tienen mis ads"
```
Revisa todos los ads activos y detecta anomalías.

Estructura estándar:
- `utm_source`: instagram / facebook
- `utm_medium`: paid_social
- `utm_campaign`: tipo_ciudad_objetivo (ej: tofu_bogota_leads)
- `utm_content`: id_creativo (ej: video_testimonio)
- `utm_term`: objetivo (ej: leads, landing, pdf, schedule)

## Estado / pendientes
- ✅ Reportes en vivo (leads, CPL, creativos, UTMs)
- ✅ Generador automático de UTMs para nuevas campañas (2026-06-22)
- ✅ Usuario DEXTER1799 (Esneider) autorizado (2026-06-22)
- ⚠️ **Corre solo mientras la Mac/terminal esté encendida.** Pendiente convertirlo en
  servicio `launchd` para que corra 24/7.

Relacionado: [[meta-mcp-guia]] · [[feedback-cuentas-meta-no-son-sedes]] · [[reporte-diario-meta-automatico]]
