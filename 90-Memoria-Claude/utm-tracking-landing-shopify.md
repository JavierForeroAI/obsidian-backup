---
name: utm-tracking-landing-shopify
description: Scripts UTM instalados en theme.liquid de Shopify — NO tocar en ediciones futuras
metadata:
  type: project
---

# UTM Tracking Landing — Innovart Medical IPS
**Fecha implementación:** 26 junio 2026

## Estado actual
- ✅ **FUNCIONANDO EN PRODUCCIÓN** — 26 junio 2026
- Probado en celular: mensaje llega con `[fb/rtg]` ✅ (formato final — fuente corta + medio corto)
- Formato sufijo: `[{src_corto}/{medium_corto}]` → facebook→fb, instagram→ig, retargeting→rtg, paid_social→paid
- ⚠️ Error conocido: si el token GHL se pega con salto de línea al final → script falla silenciosamente. Token debe estar en una sola línea.
- Ver estado completo de todas las fuentes: [[utm-tracking-avance-general]]

## 🚨 LECCIÓN CRÍTICA — Archivo correcto

La landing (`/`) usa **`theme.pagefly.liquid`**, NO `theme.liquid`. Los scripts deben estar en `theme.pagefly.liquid`. Pusimos los scripts en `theme.liquid` primero y no funcionaron — 4 horas perdidas. Ver: [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]]

## ⚠️ NO TOCAR ESTOS BLOQUES EN FUTURAS EDICIONES DEL TEMA

Se instalaron 2 scripts en el archivo `layout/theme.liquid` del tema activo **"Dawn — GEO IA Innovart"** (ID: `181331001645`).

**Por qué:** Los leads de la landing llegaban sin UTMs a GHL. No se sabía de qué campaña venía cada lead. Esto resuelve el tracking completo.

---

## Script 1 — UTM Capture (en `<head>`)

**Ubicación:** Líneas 18-20, justo después de `<!-- End Google Tag Manager -->`

```html
<!-- Innovart UTM Capture -->
<script>(function(){try{var p=new URLSearchParams(window.location.search);window.LANDING_UTMS={utm_source:p.get('utm_source')||'directo',utm_medium:p.get('utm_medium')||'none',utm_campaign:p.get('utm_campaign')||'sin_campana',utm_content:p.get('utm_content')||'',utm_term:p.get('utm_term')||''};sessionStorage.setItem('landing_utms',JSON.stringify(window.LANDING_UTMS));}catch(e){}})();</script>
<!-- End Innovart UTM Capture -->
```

**Qué hace:** Lee los parámetros UTM de la URL y los guarda en `sessionStorage` + `window.LANDING_UTMS`.

---

## Script 2 — WA + Form Enrichment (antes de `</body>`)

**Ubicación:** Justo antes del cierre `</body>` al final del archivo.

```html
<!-- Innovart WA + Form UTM Enrichment -->
<script>(function(){...GHL_TOKEN='pit-...'...})();</script>
<!-- End Innovart WA + Form UTM Enrichment -->
```

**Qué hace:**
- Modifica los 9 botones WhatsApp para añadir `[meta/MEDELLIN_FUE]` al mensaje
- Al enviar el formulario "Agendar Cita" (`#bcontact-form-483316`), envía nombre + teléfono + email + UTMs directo a GHL API

---

## Token GHL usado

- **Nombre en GHL:** `Landing UTM Tracker`
- **Tipo:** Private Integration — scope `contacts.write`
- **Dónde verlo:** GHL → Settings → Private Integrations → Landing UTM Tracker
- **No expira** a menos que se rote manualmente
- **Si se rota:** actualizar `var GHL_TOKEN='...'` en el Script 2 del theme.liquid

---

## Custom Fields GHL (NO crear duplicados)

| Campo | ID |
|-------|----|
| utm_source | `ffBWPx4Qlhxb6D6toNWO` |
| utm_medium | `46qWfYJubx8IAOhyFlgT` |
| utm_campaign | `lPfZB842vcw2a7iD3tOD` |
| utm_content | `hFUkJs1bRuGskcA6X5TA` |
| utm_term | `ni4PMQh6l93hmoiyfEEY` |

---

## Workflow GHL activo

- **Nombre:** `LANDING - Procesar UTMs y Asignar Lead`
- **ID:** `abcee3aa-0676-40a7-b3f3-9e65430a90b8`
- **Trigger:** tag `fuente_landing` agregado
- **Status:** published ✅

---

**How to apply:** Antes de cualquier edición al theme.liquid, verificar que los bloques `<!-- Innovart UTM Capture -->` y `<!-- Innovart WA + Form UTM Enrichment -->` están intactos. No eliminarlos ni moverlos.
