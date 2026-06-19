---
name: referencia-ghl-workflows-mcp
description: Cómo construir workflows GHL por el MCP (triggers, if/else por cuerpo de mensaje, publicar, probar)
metadata:
  type: reference
---

Recetas verificadas para construir workflows GHL vía MCP `ghl` (probado 2026-06-18, ver [[medicion-leads-blog-whatsapp]]).

**Flujo de construcción:**
1. `create_workflow` → nace en `draft`.
2. `update_workflow_actions` con `triggers` + `actions` (+ `allowMultiple`, `removeContactFromLastStep`). **REEMPLAZA** todas las acciones: enviar el array COMPLETO cada vez.
3. `validate_workflow` → debe dar `status: ok` (atrapa el bug de "acción corrupta" que salta pasos).
4. `publish_workflow` → pasa a `published` **y activa los triggers** (en draft el trigger sale `active:false`; tras publicar queda `active:true` — verificar releyendo).

**Disparador Customer Replied (`type:"customer_reply"`):** admite condiciones (AND) sobre `message.type`, `message.body` (operador `contains`) y `contact.tags`. En Innovart el **WhatsApp applevel entra como SMS = `message.type == 2`** (ver [[feedback-whatsapp-applevel-sms]]). El flujo maestro de entrada es `0.1 SMS GPT` (`428a4568-...`), que dispara con type 2 sin filtro de texto y hace AI + oportunidad + asignación.

**If/Else por CUERPO DE MENSAJE (no por tag):** la utilidad `build_if_else_branch` solo cubre `field:'tags'`. Para ramificar por texto del mensaje se arma a mano un trío de nodos replicando la forma de un workflow real (`get_workflow_full`):
- **condition-node**: `nodeType:"condition-node"`, `cat:"conditions"`, `next:[yesId,noId]`, `attributes.branches[].segments[].conditions[]` con `{conditionType:"contact_reply", conditionSubType:"message.body", conditionOperator:"contains", conditionValue:"texto"}`. Operadores vistos: `contains`, `==`, `!=`, `has_no_value`.
- **branch-yes**: `nodeType:"branch-yes"`, `parent/parentKey:condId`, `next: <acción>`.
- **branch-no**: `nodeType:"branch-no"`, `parent/parentKey:condId`, `attributes:{else:true}`.
- **Encadenar varios if/else en secuencia (patrón nativo GHL = anidado):** el SIGUIENTE check va en el `next` de la rama **NO** (su `parent/parentKey` = ese no-node). La rama **SÍ** corre su acción y termina. Así el orden de evaluación queda forzado (útil: evaluar `(Ref: FUE-DHI)` antes que `(Ref: FUE)`; además matchear el token completo con paréntesis de cierre evita solapes).
- Las acciones lineales sí auto-encadenan por orden del array; los nodos if/else necesitan `parent/parentKey/next/sibling` explícitos. Conviene asignar `id` propios a todos los nodos para controlar el linkeo.

**Tags:** GHL guarda los nombres en **minúsculas**; usar el nombre exacto guardado en los `add_contact_tag` para que el dropdown renderice. Re-agregar un tag existente no duplica.

**Probar (limitación):** `add_inbound_message` necesita `conversationId` + `conversationProviderId`. En esta cuenta TODO el WhatsApp va por el provider del app applevel `628f88b07cf43a7641c58089`, al que el token del MCP da **401** (no autorizado); y no hay números LC Phone. → **No se puede simular un entrante real por API**; la prueba válida es un **WhatsApp real**. `add_contact_to_workflow` corre las acciones pero el if/else por `message.body` no ve cuerpo (queda solo la 1ª etiqueta incondicional).

**Lecturas grandes:** `list_workflows_full`, `get_location_tags`, `get_workflow_full` suelen exceder el límite y se guardan a archivo → procesar con `jq`.

**Carpetas de workflows (limitación + skill):** el MCP **NO** gestiona carpetas de workflows (no hay list/create/move-folder; el campo `parentId` del workflow es lineaje de clon, no carpeta, y no es editable). GHL las maneja por su **API interna no documentada**. Para cubrirlo se creó la skill **`ghl-carpetas-workflows`** (`~/.claude/skills/ghl-carpetas-workflows/`, script `scripts/ghl_folders.py`): `audit` ya opera (API pública v2 con PIT en env `GHL_TOKEN`); `list-folders`/`create-folder`/`move` están listos pero **pendientes de cablear** el bloque `FOLDER_API` con el endpoint real (capturar en DevTools: "New Folder" + arrastrar workflow → método/URL/body/headers). Seguridad: token por env (no lee `.ghl-tokens.json`), dry-run por defecto, solo organiza (no cambia estado/triggers/acciones).
