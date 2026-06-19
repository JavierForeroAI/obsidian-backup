---
name: referencia-ghl-cuentas-innovart
description: IDs de las sub-cuentas GHL de Innovart + regla de verificar/cambiar ubicación antes de escribir
metadata:
  type: reference
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

⚠️ **REGLA DE ORO — verificar ubicación antes de CUALQUIER escritura.** La ubicación activa puede arrancar en **"The Voice Digital" (`lSXdqtEocvEgULrWoyJ5`)**, que es una cuenta **AJENA** a Innovart (su CRM de cotizaciones/demos). Siempre:
1. `get_current_location` para confirmar.
2. `switch_location <ID>` a la sede correcta (intercambia el PIT token registrado de esa sede).

Un token de una sede da **403** al consultar otra vía el parámetro `locationId` (ej. `get_workflows`); por eso hay que **switch_location**, no pasar locationId de otra cuenta. `list_registered_locations` muestra las 6 registradas.

Recordar: las cuentas de **Meta Ads** (BGTA, QUILLA, MEDELLIN, PANAMA, LANDING/INTERACCION DIEGO) NO mapean 1:1 a estas sedes GHL — ver [[feedback-cuentas-meta-no-son-sedes]]. Relacionado: [[referencia-ghl-workflows-mcp]], [[medicion-leads-blog-whatsapp]].
