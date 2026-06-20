---
name: shopify-formulario-contacto-crm
description: Por qué los contactos del formulario web /pages/contact NUNCA llegan al CRM (GHL) — es el formulario NATIVO de Shopify (solo manda email), no está cableado. Causa raíz + cómo arreglarlo.
metadata:
  type: reference
---

# Formulario de contacto web (Shopify) NO conectado al CRM

**Fecha:** 2026-06-19. Diagnóstico pedido por Javier ("el contacto del formulario de la
página web tiene que llegar al CRM y no llega").

## Causa raíz (no hay nada "roto" — nunca estuvo conectado)
- La página `/pages/contact` tiene el **body vacío** y `templateSuffix = "contact"` → el
  formulario **no vive en el contenido de la página**, sino en la plantilla del theme
  `templates/page.contact.json` (theme MAIN **Dawn — GEO IA Innovart**).
- Esa plantilla usa la sección **`"type": "contact-form"`** = el **formulario NATIVO de
  Shopify** (`{% form 'contact' %}`).
- Ese formulario nativo: **solo envía un email** a `innovartmedicalips@gmail.com`,
  **NO crea customer** en Shopify y **NO tiene ninguna conexión con GHL**.
- → Por diseño, ese contacto **nunca puede llegar al CRM**.

## Cómo arreglarlo (pendiente)
- Reemplazar el formulario nativo por un **formulario de GHL** (embed/iframe de un form de
  la cuenta principal de Innovart) en `/pages/contact`, **o** cablear un webhook/flujo que
  postee los envíos a GHL (crear contacto + tag).
- Debe **capturar `fbclid` → `fb_click_id` y `ctwa_clid`** como toda landing de Innovart
  → ver [[feedback_fbclid_landing_pages]].
- ⚠️ Al operar GHL por MCP, la ubicación activa puede arrancar en **The Voice Digital**
  (cuenta ajena). Cambiar a **Innovart Medical IPS** (`NPhQTmLOHd6FbDtqLPnG`) antes de
  tocar nada → [[referencia-ghl-cuentas-innovart]].

Relacionado: [[shopify-ecosistema-mcp]] · [[shopify-playbook-capacidades-mcp]]
