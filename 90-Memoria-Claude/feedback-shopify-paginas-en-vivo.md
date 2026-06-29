---
name: feedback-shopify-paginas-en-vivo
description: Regla de oro Shopify — nunca ofrecer editar via MCP páginas o código en producción sin que Javier lo pida explícitamente
metadata:
  type: feedback
---

No ofrecer aplicar cambios vía MCP de Shopify en páginas o archivos de tema que ya están en producción (live/publicados). Siempre entregar los pasos manuales para que Javier los aplique. Solo usar el MCP para escribir si Javier lo pide explícitamente en ese mensaje.

**Why:** Shopify no permite editar el contenido de páginas PageFly en vivo vía API. Y aunque los archivos de tema sí son editables por API, tocar código en producción sin confirmación explícita es un riesgo. Javier se cansa de que se le pregunte lo mismo cada sesión.

**How to apply:** Cuando el trabajo es en Shopify y hay código que cambiar — theme.liquid, theme.pagefly.liquid, PageFly pages, snippets — dar los pasos detallados con el texto exacto a buscar, borrar y pegar. Cerrar ahí. No agregar "¿quieres que lo haga yo vía MCP?".
