---
name: shopify-ecosistema-mcp
description: Inventario verificado de la tienda Shopify de Innovart + qué se puede y qué NO se puede editar desde el MCP de Shopify (themes, PageFly, GemPages, páginas)
metadata:
  type: reference
---

# Shopify Innovart — Ecosistema + capacidades reales del MCP

**Fecha de verificación:** 2026-06-19 (vía MCP `claude.ai Shopify`, acceso operativo).

> 🇪🇸 **Idioma:** el panel de Shopify de Javier está en **español**. Cualquier instrucción de Shopify (navegación, secciones, botones) va con las etiquetas en español: Tienda online · Temas · Personalizar · Agregar sección · Liquid personalizado · Ocultar sección · Guardar · Páginas · "Formulario de contacto". Detalle y glosario en [[feedback-idioma-espanol-ghl]].

## Tienda
| Campo | Valor |
|---|---|
| Nombre | Innovart Medical |
| Dominio público | www.innovartmedical.com |
| `.myshopify` | `qr6t9m-bz.myshopify.com` |
| Shop GID | `gid://shopify/Shop/90100105517` |
| Plan | **Basic** · Moneda **COP** · TZ −05 |

## Themes
| Theme | Rol | ID (GID `OnlineStoreTheme/...`) |
|---|---|---|
| **Dawn — GEO IA Innovart** | 🟢 MAIN (live) | `181331001645` |
| Dawn | ⚪ Unpublished (respaldo) | `172204491053` |

## Page builders activos — HAY DOS (detectados por `templateSuffix` + archivos del theme)
- 🟣 **GemPages** → `templateSuffix = gp-template-<id>`, contenido en `sections/gp-section-<id>.liquid` (auto-generado).
- 🔵 **PageFly** → `templateSuffix = pf-<hash>`, contenido horneado en `sections/<pf>.liquid` (auto-generado).
- ⚪ **Nativo Shopify** → `templateSuffix = page` / `contact` / vacío.

### Páginas (13)
| Página | Handle | Builder | Template |
|---|---|---|---|
| Home (index) | `/` | 🔵 PageFly | secciones nativas DESACTIVADAS + `pagefly-home`; layout `theme.pagefly` |
| Financiación | `financiacion` | 🟣 GemPages | `page.gp-template-548457161085158307.json` |
| Barbería | `barberia` | 🟣 GemPages | `page.gp-template-550626686639539022.json` |
| Panamá | `panama` | 🟣 GemPages | `page.gp-template-553417332983071906.json` |
| Valoración Clientes | `valoracion` | 🔵 PageFly | `page.pf-43ea6386.json` |
| Implante de Cejas | `implantedecejas` | 🔵 PageFly | `page.pf-8501d84d.json` |
| Implante de Barba | `implantedebarba` | 🔵 PageFly | `page.pf-7ac9ee97.json` |
| Valoraciones Panamá | `valoraciones-panama` | 🔵 PageFly | `page.pf-0eba0939.json` |
| Sobre Innovart | `sobre-innovart-medical` | ⚪ Nativo | `page` |
| Cancelaciones/Devoluciones | `politicas-de-cancelaciones-...` | ⚪ Nativo | `page` |
| Privacidad/Datos | `politica-de-tratamientos-de-datos` | ⚪ Nativo | default |
| Repoblamiento Complementario | `politica-repoblamiento-...` | ⚪ Nativo | default |
| llms.txt | `llms-txt` | ⚪ Nativo | `page.llms-txt.liquid` |
| Contact | `contact` | ⚪ Nativo | `page.contact.json` |

**2 templates GemPages huérfanos** (sin página asignada): `gp-template-549495758164853862` y `gp-template-582843351703749593` → candidatos a limpieza.

Blog único: **"Artículos Médicos"** (`articulos-medicos`, 13 artículos). 0 metaobjects definidos.

## ⚠️ Matriz de capacidad REAL del MCP (verificada, no asumida)
| Acción | Estado | Nota |
|---|---|---|
| Leer cualquier template/sección (PageFly/GemPages/nativo) | ✅ | `theme.files(filenames:[...])`; archivos grandes (>~30KB) el MCP los vuelca a disco → analizar con `jq`/`grep` |
| Editar **página nativa** (título, body HTML, SEO, handle, publicar, template) | ✅ | mutation `pageUpdate` |
| Editar SEO/título/handle/estado de páginas PageFly/GemPages | ✅ | el registro `Page` es nativo; sólo el render es de la app |
| Productos, colecciones, blog/artículos, redirects, metafields, descuentos, markets | ✅ | tools dedicadas + GraphQL |
| **Escribir archivos del theme LIVE/MAIN** (`themeFilesUpsert`/`themeFilesCopy`) | ❌ | **El MCP bloquea escritura al theme publicado.** Sólo permite escribir a themes **unpublished**. |
| Publicar theme / refunds / gift cards / staff / borrar theme | ❌ | Bloqueado por seguridad del MCP (se hace en admin) |
| Enumerar apps instaladas (`appInstallations`) | ❌ | Token MCP **sin scope `read_apps`** → detectar apps por templates, no por API |

**Implicación clave:** todo el contenido visual de PageFly y GemPages vive en archivos del theme **MAIN (live)** → **no se puede modificar por MCP**. Además ambas apps **regeneran/sobrescriben** esos archivos al publicar desde su editor ("auto-generated, do not edit directly"). Para cambiar contenido visual: editor de PageFly/GemPages, o escribir a un theme unpublished y publicar desde admin.

Relacionado: [[shopify-alt-text-home-panama]] · [[feedback-mcp-ghl-update-page]] · [[seo-plan-shopify-2026-05]]
