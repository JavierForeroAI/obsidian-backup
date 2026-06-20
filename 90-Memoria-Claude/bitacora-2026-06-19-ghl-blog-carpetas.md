---
name: bitacora-2026-06-19-ghl-blog-carpetas
description: Bitácora de la sesión 2026-06-18/19 — sistema de medición de leads del blog + organización de workflows en carpetas en las 6 sedes GHL
metadata:
  type: project
---

# Bitácora sesión 2026-06-18/19 — GHL: Blog + Carpetas de Workflows

Registro de TODO lo construido / cambiado / mejorado. Notas de detalle enlazadas.

## 🟢 CONSTRUIDO

### 1. Sistema de medición de leads del Blog por WhatsApp → [[medicion-leads-blog-whatsapp]]
- **Cuenta principal** `NPhQTmLOHd6FbDtqLPnG`.
- **14 tags** creados (GHL los guarda en minúsculas): `lead del blog` + `lead del blog <codigo>` por artículo (fue-dhi, fue, dhi, candidato, recuperacion, resultados, barba, alopecia-mujeres, faq, clinica, dr-carreno, dra-morales, info-ia).
- **Workflow** `Leads del Blog (WhatsApp)` (ID `ddc39bd2-37fd-4db1-85e9-3dde52da613c`) PUBLICADO: disparador Customer Replied `message.type==2` + `message.body` contains "vengo del blog de Innovart"; 1ª acción tag general; 13 ramas If/Else anidadas por `(Ref: ...)` (orden FUE-DHI→FUE, token con paréntesis = sin solape). Entrega AUTO a `0.1 SMS GPT` (oportunidad + asignación + IA), sin tocar 0.1.
- **Verificado E2E** con WhatsApp real → tags + oportunidad + IA OK.
- **Pendiente**: equipo del blog pone botón WhatsApp por artículo con texto `Hola, vengo del blog de Innovart (Ref: <CODIGO>)`.

### 2. Skill `ghl-carpetas-workflows` → [[referencia-ghl-workflows-mcp]]
- `~/.claude/skills/ghl-carpetas-workflows/` (SKILL.md + `scripts/ghl_folders.py`).
- Cubre lo que el MCP NO hace: crear/listar/mover carpetas de workflows. `audit`/`list-folders`/`create-folder`/`move`. Dry-run por defecto, token por env, solo organiza, ya con User-Agent (fix Cloudflare 1010). **Verificada y usada en producción.**

### 3. Carpeta "FLUJOS CREADOS POR MCP CLAUDE" en las 6 sedes → [[referencia-ghl-cuentas-innovart]]
Folder IDs: Principal `f81eb9b9…` · Bogotá `02d7d81c…` · Medellín `aef15d02…` · Panamá `8212bc9c…` · Barranquilla `3fd26e6c…` · Bucaramanga `081b82d5…`.

## 🔧 CAMBIADO / ORGANIZADO

### 4. 23 workflows "nuestros" movidos a su carpeta por sede (estado `published` intacto)
**Inventario de nuestro footprint GHL** (lo movido):
- **Principal (4):** Leads del Blog (`ddc39bd2`), Web-Formulario Shopify landing_formulario_web (`4bd84e2f`), CAPI Frio Stale (`667b1ad1`), TEST CAPI Diagnostico Meta (`66144492`).
- **Bogotá (5):** Home4 router→4.1 (`fbd5387a`), LP Financiación BTA (`20eb73fb`), CAPI Lead WhatsApp/Ads "NO TOCAR" (`fd50246d`), CAPI Frio Stale (`700d8ed4`), webhook CP WEB (`9102785c` — ⚠️ dudoso si es nuestro; reversible).
- **Medellín (2):** LP Financiación MDE (`c3572764`), CAPI Frio Stale (`5fba3220`).
- **Panamá (8):** CAPI Frio Stale (`7c6b7271`) + 7 `Etiqueta… - CAPI` (Agenda Valoracion `f2ba50a4`, Asistio No Pago `41364b40`, Frio `4cacad3a`, Ganado `aa67d560`, No Asistio `b5a5a0b8`, Perdido `0771f115`, Primer Contacto `8d9b3d64`).
- **Barranquilla (2):** LP Financiación BAQ (`2f258215`), CAPI Frio Stale (`64594369`).
- **Bucaramanga (2):** CAPI Frio Stale `80de1e6b` y `d49857ee` (duplicado — revisar si borrar uno).
> Excluidos por pre-existentes (NO nuestros): `4.1 Recibir lead de Landing_formulario`, `Recipe - List Reactivation`.

## 🧠 MEJORAS DE PROCESO (referencias reutilizables)
- [[feedback-idioma-espanol-ghl]] — hablar SIEMPRE en español en todo lo de GHL.
- [[referencia-ghl-cuentas-innovart]] — IDs de las 6 sedes + regla de verificar `get_current_location`/`switch_location` (la activa puede arrancar en The Voice Digital, ajena).
- [[referencia-ghl-workflows-mcp]] — recetas para construir workflows por MCP, if/else por `message.body`, endpoints de carpetas verificados, limitación de probar inbound por API, y el bug Cloudflare 1010 (User-Agent obligatorio en `backend.leadconnectorhq.com`).

## ⏳ PENDIENTES
- Borrar carpetas de prueba vacías en la UI: `ZZZ PRUEBA BORRAR`, `ZZZ PRUEBA 2`.
- Confirmar si `webhook CP WEB` es nuestro; si no, sacarlo de la carpeta (mover a raíz, `parentId:null`).
- **Largo plazo (clave):** agregar al MCP las 3 tools de carpetas (`list/create/move`) usando su auth Firebase ya existente → elimina la fricción del token web de ~1h. Prompt para el dev guardado en [[referencia-ghl-workflows-mcp]].
- ✅ ~~Blog: botones WhatsApp por artículo~~ — VERIFICADO 2026-06-19: los 13 artículos YA los tienen correctos (`wa.me/573124565014` + Ref por tema + frase). Nada que hacer.

## 🔐 Nota de seguridad
La gestión de carpetas usó un **JWT de sesión web** (capturado de DevTools, expira ~1h). **No se guardó en disco**; se usó transitoriamente por env. Auth de largo plazo = Firebase del MCP.
