---
name: referencia-ghl-cuentas-innovart
description: IDs de las sub-cuentas GHL de Innovart + regla de verificar/cambiar ubicación antes de escribir
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9c6a236f-2d91-4059-bb1b-2c2d280a4304
---

Sub-cuentas (locations) de Innovart en el MCP `ghl`. companyId **`PVgPUFTrR2rn75Ph8b21`** (Firebase habilitado → workflow builder funciona).

| Sede | Location ID |
|---|---|
| **Principal** (Innovart Medical IPS) | `NPhQTmLOHd6FbDtqLPnG` |
| Bogotá | `DgjjDzD9nkCKv8AGF1Qb` |
| Medellín | `h8DplQKVE6epDbbj5Kg8` |
| Panamá | `45SKYgIDgr4Eh6a6JcFz` |
| Barranquilla | `cXH8KbMaAPGzkmf3Z2pP` |
| Bucaramanga | `s40Wa8mXYBxlFCieKohO` |

⚠️ **REGLA DE ORO — verificar ubicación antes de CUALQUIER escritura.** Siempre:
1. `get_current_location` para confirmar.
2. `switch_location <ID>` a la sede correcta (intercambia el PIT token registrado de esa sede).

**2026-06-19: arranque por defecto cambiado a Innovart Principal.** En `~/Library/Application Support/elitedcs-ghl-mcp/credentials.json` se cambió `ghl_location_id` de `lSXdqtEocvEgULrWoyJ5` (The Voice Digital) → `NPhQTmLOHd6FbDtqLPnG` (Principal) y `ghl_api_key` al PIT de Principal (`pit-0a14244b…`). Motivo: Javier pidió "quitar a Voice Digital siempre". Valores originales para rollback: location `lSXdqtEocvEgULrWoyJ5`, key `pit-28aeafe6…`. ⚠️ Si el MCP re-sincroniza ese archivo desde su licencia, puede revertir → en ese caso **igual hay que `switch_location` fuera de The Voice Digital** apenas inicie. The Voice Digital es una cuenta **AJENA** a Innovart (CRM de cotizaciones/demos) y NO debe usarse para nada de Innovart.

Un token de una sede da **403** al consultar otra vía el parámetro `locationId` (ej. `get_workflows`); por eso hay que **switch_location**, no pasar locationId de otra cuenta. `list_registered_locations` muestra las 6 registradas.

**Carpeta de workflows `FLUJOS CREADOS POR MCP CLAUDE`** (creada 2026-06-18 vía API interna, ver [[referencia-ghl-workflows-mcp]]). Folder IDs por sede:
| Sede | Folder ID |
|---|---|
| Principal | `f81eb9b9-e626-4cac-b0b9-9a779e63a595` |
| Bogotá | `02d7d81c-9c8f-4b4d-b84c-288ce7626b9d` |
| Medellín | `aef15d02-7b5c-4779-a75a-ab61181627e7` |
| Panamá | `8212bc9c-b64c-463f-9e6e-4b07fa971503` |
| Barranquilla | `3fd26e6c-7653-4d84-8b5e-f82fa55869fc` |
| Bucaramanga | `081b82d5-e338-490b-ae01-ec078e659d78` |
⚠️ Cloudflare exige **User-Agent de navegador** (sin él → error 1010) en `backend.leadconnectorhq.com`.
**2026-06-18: 23 flujos "nuestros" movidos a esa carpeta en las 6 sedes (4 Principal, 5 Bogotá, 2 MDE, 8 Panamá, 2 BAQ, 2 BUC), todos conservaron estado `published`.** Auth = JWT de sesión web (DevTools), expira ~1h; el largo plazo es agregar las tools al MCP (que ya tiene auth Firebase) — ver [[referencia-ghl-workflows-mcp]].

Recordar: las cuentas de **Meta Ads** (BGTA, QUILLA, MEDELLIN, PANAMA, LANDING/INTERACCION DIEGO) NO mapean 1:1 a estas sedes GHL — ver [[feedback-cuentas-meta-no-son-sedes]]. Relacionado: [[referencia-ghl-workflows-mcp]], [[medicion-leads-blog-whatsapp]].
