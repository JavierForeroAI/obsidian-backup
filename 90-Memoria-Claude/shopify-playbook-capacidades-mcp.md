---
name: shopify-playbook-capacidades-mcp
description: Playbook maestro de TODO lo que se puede hacer en la tienda Shopify de Innovart desde el MCP (tools + GraphQL Admin API), qué está bloqueado, y recetas para PageFly/GemPages/SEO/themes
metadata:
  type: reference
---

# Shopify Innovart — Playbook maestro de capacidades (MCP)

**Verificado 2026-06-19** contra el MCP `claude.ai Shopify` + doc oficial shopify.dev. Contexto de la tienda: [[shopify-ecosistema-mcp]]. Caso alt text: [[shopify-alt-text-home-panama]].

## A) Tools nativas del MCP cargadas (atajos con widget)
**Productos:** `search_products`, `get-product`, `create-product`, `update-product`, `bulk-update-product-status`.
**Colecciones:** `search_collections`, `get-collection`, `create-collection`, `update-collection`, `add-to-collection`.
**Inventario:** `get-inventory-levels`, `set-inventory` (usa `compareQuantity` para update seguro).
**Pedidos/Clientes:** `list-orders`, `get-order`, `list-customers`.
**Analítica:** `run-analytics-query` (ShopifyQL: ventas, sesiones, conversión, productos, referrers).
**Descuentos:** `create-discount` (% con scope colección, mínimos, fechas, segmentos).
**Tienda:** `get-shop-info`, `switch-shop`.
**Dev/GraphQL:** `graphql_query`, `graphql_mutation`, `graphql_schema`, `search_docs_chunks`, `validate_graphql_codeblocks`.
**Creación de tienda nueva (NO aplica, ya existe):** `get-new-store-previews`, etc.

> Flujo GraphQL correcto: `graphql_schema`/`search_docs_chunks` → construir → **`validate_graphql_codeblocks`** → `graphql_query`/`graphql_mutation`. Resultados >~30KB el MCP los vuelca a disco → analizar con `jq`/`grep` en Bash.

## B) Poder real vía GraphQL Admin API (lo que SÍ se puede ejecutar)
| Área | Mutations clave | Uso para Innovart |
|---|---|---|
| **Páginas nativas** | `pageCreate` · `pageUpdate` · `pageDelete` | crear/editar páginas (body HTML, handle, template, publish) |
| **Blog** | `blogCreate/Update` · `articleCreate/Update/Delete` | publicar los 13+ artículos médicos por API |
| **SEO meta** | `metafieldsSet` con `title_tag` y `description_tag` (namespace `global`, `single_line_text_field`) | controlar meta title/description de **producto, página, colección, blog, artículo** |
| **Metafields/Metaobjects** | `metafieldsSet`, `metaobjectDefinitionCreate`, `metaobjectCreate` | datos estructurados / schema / contenido reutilizable |
| **Redirects 301** | `urlRedirectCreate/Update/Delete` + bulk | SEO al borrar/mover URLs |
| **Navegación** | menús vía Admin (menu mutations) | cambiar menús |
| **Traducciones/Markets** | `translationsRegister` (TranslatableResourceType incluye PAGE, ARTICLE) | versión multi-idioma |
| **Archivos/CDN** | `fileUpdate` (alt de MediaImage), `stagedUploadsCreate` | alt de imágenes de Files (ver caveat PageFly abajo) |
| **Themes** | `themeDuplicate` (API 2025-10) · `themeCreate` (desde URL/staged) · `themeUpdate` (nombre) · `themeFilesCopy` · `themeFilesUpsert` · `themeFilesDelete` | staging/backup de theme |

## C) ⛔ Bloqueado / limitado (verificado)
- **Escribir archivos del theme LIVE/MAIN** → el MCP lo **bloquea**. Solo themes **unpublished**.
- **`themePublish`** → bloqueado por el MCP → publicar **manual en admin**.
- **`themeDelete`** → bloqueado.
- **Caveat doc oficial:** `themeFilesUpsert`/`themeFilesCopy` requieren `write_themes` **+ una "exemption" de Shopify**. El MCP first-party la tiene para unpublished; un token propio podría no tenerla.
- **`appInstallations`** → bloqueado (token sin scope `read_apps`) → apps se detectan por templates, no por API.
- Refunds, gift cards (write), staff management → bloqueados.

## D) PageFly / GemPages — qué es alcanzable (NO hay MCP/API propio de esas apps)
La única superficie expuesta es lo que las apps escriben en el theme + el registro nativo de la página:
- ✅ **Leer** todo su output: `pagefly-home.liquid`, `gp-section-*.liquid`, `page.gp-template-*.json` (settings incl. `ggXXX_alt`).
- ✅ **Editar metadatos de la página** (título, handle, SEO `title_tag`/`description_tag`, template, publish) por `pageUpdate`/`metafieldsSet`.
- ⚠️ **Editar su contenido visual** (texto, imágenes, alt): vive en archivos del theme **MAIN** → no escribible por MCP; y **la app lo regenera al publicar**. → Hacerlo en el **editor de PageFly/GemPages** (durable, queda en la BD de la app).
- ❌ No hay endpoint para empujar cambios a la BD de PageFly/GemPages.

## E) Recetas verificadas
1. **SEO meta (title/description) de cualquier recurso** → `metafieldsSet` con `{ownerId, namespace:"global", key:"title_tag"|"description_tag", type:"single_line_text_field", value}`. Funciona aun en páginas PageFly/GemPages (el meta es nativo).
2. **Redirect 301** → `urlRedirectCreate(urlRedirect:{path, target})`.
3. **Staging de theme (cambios de CÓDIGO, no apps):** `themeDuplicate(id: live)` → `themeFilesUpsert(themeId: copia, ...)` → revisar en preview → **publicar en admin** (`themePublish` bloqueado por MCP). Riesgos SEO/medición: ver [[shopify-alt-text-home-panama]] (revertir schema/pixeles; apps sobrescriben).
4. **Backup de un template antes de tocar** → `themeFilesCopy(srcFilename → dstFilename .bak)` en theme unpublished.
5. **Alt de imágenes nativas (no PageFly):** `fileUpdate` sobre el `MediaImage`. (No sirve para PageFly: pinta su propio alt.)

## F) Roadmap acordado con Javier (2026-06-19) — orden FIJO
Secuencia decidida por Javier. **No saltarse fases.**
1. **Alt text** (en curso) — 7 alt rotos del Home en editor PageFly. Ver [[shopify-alt-text-home-panama]].
2. **SEO + GEO** (siguiente bloque) — completar antes de tocar optimización. Skills: `seo`, `seo-technical`, `seo-schema`, `seo-page`, **`seo-geo`** (AI Overviews/ChatGPT/Perplexity + `llms.txt` — el theme se llama "Dawn — GEO IA Innovart"). SEO meta (`title_tag`/`description_tag`) de las 13 páginas + productos por `metafieldsSet`.
3. **Optimización de páginas PageFly/GemPages** — recién cuando SEO+GEO esté listo. **Orden FIJO: Carga → Diseño → Seguridad.** Alcance (qué páginas) se define al llegar.

### Stack de skills ARMADO para la fase 3 (page builders)
| Pilar (en orden) | Skill | Foco |
|---|---|---|
| 🚀 **Carga** (punta de lanza) | `seo` (técnico) | Core Web Vitals/INP, peso HTML/CSS inline, fonts.gstatic, Wistia, `<source>`, lazy-load, formato/sizing de imágenes. Mayor dolor de los builders. |
| 🎨 **Diseño** | `page-cro` + `ui-ux-pro-max` | Jerarquía visual, above-the-fold, mobile, conversión → spec para editor |
| 🔒 **Seguridad** | `security-review` | Scripts terceros, CSP/headers, PII, pixeles/CAPI, scopes de apps |

⚠️ Recordatorio de ejecución: contenido visual de PageFly/GemPages NO se escribe por MCP → entregables = auditoría + cambios theme-level vía staging (`themeDuplicate`→`themeFilesUpsert`→publicar en admin) + spec exacto para el editor de la app.

### Otras oportunidades (backlog, sin fase asignada)
- [ ] 2 templates GemPages huérfanos (`...549495758164853862`, `...582843351703749593`) → limpiar.
- [ ] Conectar productos Shopify ↔ catálogo Meta (tools `ads_catalog_*`) para DPA/Advantage+.

Relacionado: [[shopify-ecosistema-mcp]] · [[shopify-alt-text-home-panama]] · [[seo-plan-shopify-2026-05]] · [[feedback-mcp-ghl-update-page]]
