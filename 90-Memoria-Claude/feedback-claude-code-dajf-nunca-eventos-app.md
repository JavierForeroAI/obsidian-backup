---
name: feedback-claude-code-dajf-nunca-eventos-app
description: Regla absoluta — jamás seleccionar CLAUDE CODE DA-JF en el campo "Eventos de la app" en Meta Ads Manager
metadata:
  type: feedback
---

## REGLA: CLAUDE CODE DA-JF NUNCA va en "Eventos de la app"

Nunca seleccionar la app **CLAUDE CODE DA-JF** (`1698932398019234`) en el campo **"Eventos de la app"** dentro de cualquier ad o ad set en Meta Ads Manager.

**Why:** CLAUDE CODE DA-JF es una app de desarrollador de Meta Marketing API — sirve para gestionar campañas/ads por API (leer campañas, cargar UTMs, crear creativos). NO es un SDK de tracking instalado en ninguna app móvil de usuarios. Innovart no tiene app móvil. Al seleccionarla en ads:
- Genera error #1634005 "Falta el objeto de la consulta de acción" (en campañas de tráfico al perfil)
- O contamina los datos de seguimiento sin aportar nada útil (en campañas que sí lo aceptan técnicamente)
- Investigación confirmada 2026-06-26 contra la documentación oficial de Meta "Conversions API for App Events"

**How to apply:**
- Al revisar o crear ads: verificar que "Eventos de la app" NO tenga ninguna selección (dejar en blanco)
- Si ya está seleccionada: quitar antes de publicar
- El tracking real de leads va por: Pixel CRM (termina en `62`) + CAPI Cloudflare worker + fbclid + ctwa_clid

**Herramientas de tracking correctas:**

| Herramienta | Usar |
|---|---|
| Pixel CRM (`...62`) | ✅ Siempre |
| CAPI (Cloudflare worker `innovart-capi-webhook-no-tocar`) | ✅ Siempre |
| CLAUDE CODE DA-JF en ads | ❌ Nunca |
