---
name: feedback-pagefly-url-stability
description: Regla crítica para evitar que PageFly cambie la URL de las landings de ciudad al publicar. Causa raíz identificada y fix definitivo.
metadata:
  type: feedback
---

# Regla: URL estable en PageFly — NO tocar el "Page title"

Antes de cada **Publish en PageFly**, verificar que el campo **"Page URL"** en **Page Settings (⚙️)** diga exactamente el handle correcto (ej. `implante-capilar-barranquilla`). Si no coincide, corregirlo ANTES de publicar.

**Why:** Javier reportó que las URLs cambiaban solas cada vez que publicaba. Causa raíz: cuando se edita el campo **"Page title"** en Page Settings, PageFly/Shopify regenera automáticamente el "Page URL" a partir del título nuevo. Esto pierde el handle fijado y rompe anuncios y el snippet de `theme.liquid`.

**How to apply:**
1. Nunca editar el "Page title" en Page Settings después de fijar el handle.
2. Si hay que cambiar el SEO title visible, hacerlo en el campo `title_tag` de Shopify Admin (sección "Optimización para motores de búsqueda"), no en el Page title de PageFly.
3. Antes de cada Publish: abrir el ⚙️ de la página en PageFly → verificar campo "Page URL" → si está correcto, publicar; si no, corregir y luego publicar.
4. Shopify y PageFly tienen el handle en dos lugares distintos — si difieren, PageFly impone el suyo al publicar.

## Handles definitivos de las landings de ciudad

| Ciudad | Handle |
|---|---|
| Bogotá | `implante-capilar-bogota` |
| Medellín | `implante-capilar-medellin` |
| Barranquilla | `implante-capilar-barranquilla` |
| Bucaramanga | `implante-capilar-bucaramanga` (pendiente crear) |

Descubierto 2026-06-24 — [[landing-barranquilla-2026-06-24]] · [[landing-medellin-pagefly-2026-06-23]]
