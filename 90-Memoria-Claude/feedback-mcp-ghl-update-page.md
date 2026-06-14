---
name: feedback-mcp-ghl-update-page
description: El update_page_content del MCP ghl NO persiste cambios de página/funnel; editar contenido de páginas en el editor de GHL
metadata:
  type: feedback
---

# ⚠️ MCP ghl: `update_page_content` no persiste

Probado 2026-06-13 en la página `RSAIRRYLw6yLh6MZfkDd` (funnel FINANCIACIONBTA1, Bogotá): `mcp__ghl__update_page_content` devuelve `{"prebuiltSectionTemplates":[]}` sin error, pero **NO compromete el guardado** — la versión live no cambia (`version` no sube, el page-data en Firebase queda igual). Parece hacer solo el "broadcast" colaborativo, no el commit.

**Why:** se pierde tiempo reenviando el JSON completo de la página (~30KB) sin efecto, y hay riesgo de creer que se aplicó cuando no.

**How to apply:**
- Para cambios de **contenido de páginas/funnels** (texto, links, custom code): hacerlos en el **editor de GHL** (rápido y seguro), no por MCP. Dar al usuario instrucciones de buscar/reemplazar.
- El MCP **sí** sirve para leer páginas (`get_page_full` + `get_page_content`) y para **verificar** descargando el page-data de Firebase / la URL pública con `curl`.
- Los **workflows sí persisten** por MCP (`create_workflow`, `update_workflow_actions`, `publish_workflow`) — Firebase auth habilitado en la company de Innovart.
- ⚠️ **Pasos `custom_code` creados por MCP NO se ejecutan hasta "testearlos" en la UI.** GHL exige "Code must be tested before saving": hay que abrir el paso en el builder, correr el test una vez, Guardar y Publicar. No se puede hacer por MCP. Síntoma: el paso aparece con error rojo "Errors found. Click to resolve" aunque el workflow esté publicado. Los pasos anteriores sí corren; solo el custom_code queda inactivo hasta el test manual.
- 🔴🔴 **El `custom_code` de GHL NO puede hacer `fetch` ni llamadas HTTP** (corre en `isolated-vm`, sandbox sin red). Errores al testear: `ReferenceError: fetch is not defined`. Además `contact` NO existe en el panel "Test your code" (solo en ejecución real) → `ReferenceError: contact is not defined` (guardar con `const C=(typeof contact!=='undefined'&&contact)?contact:{}`). Y "Custom value will not be passed when you are testing" → `{{custom_values.x}}` va vacío en el test. **Conclusión: NO se puede mandar CAPI a Meta desde custom_code de GHL.** Por eso los 16 flujos CAPI armados por MCP nunca funcionaron (en Meta no hay canal `crm`). **Solución adoptada (2026-06-13): acción Webhook nativa de GHL → worker Cloudflare `innovart-capi-webhook-no-tocar`** que hashea PII + postea a los 2 píxeles. Ver [[integracion-ghl-meta-capi]]. El custom_code SOLO sirve para transformar datos, no para integraciones externas.

Relacionado: [[flujo-financiacion-bta-capi]] · [[feedback-ghl-fechas-manual]]
