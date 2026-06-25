---
name: schema-precios-theme-liquid-2026-06-24
description: JSON-LD MedicalOrganization con priceRange inyectado en /pages/precios vía theme.liquid (línea 304-306). Solución final tras intentos fallidos con page.liquid/page.json.
metadata:
  type: project
  fecha: 2026-06-24
  estado: pendiente-guardar-y-verificar
---

# Schema /pages/precios — Inyección en theme.liquid

## Qué se hizo

El snippet `page-precios-schema.liquid` (en `snippets/`) contiene el JSON-LD de tipo
`MedicalOrganization` con dos `Offer` objects:

- **Colombia:** `priceRange: "COP 8000000-11000000"`, `minPrice: 8000000`, `maxPrice: 11000000`
- **Panamá:** `priceRange: "USD 3500-4500"`, `minPrice: 3500`, `maxPrice: 4500`

El snippet se inyecta condicionalmente en `theme.liquid` (tema **Dawn — GEO IA Innovart**,
ID `181331001645`) en las **líneas 304-306**, justo antes de `</head>` (línea 307):

```liquid
{% if page.url == '/pages/precios' %}
  {% render 'page-precios-schema' %}
{% endif %}
```

## Por qué theme.liquid y no page.liquid

Shopify requiere que los templates JSON (`page.json`) existan junto al `.liquid`.
Intentamos crear `page.liquid` + `page.json` en `templates/`, pero:
- `page.json` conflictuaba con el default existente
- Shopify no permite templates con nombres custom (e.g., `page-precios.liquid`)
- La solución más limpia y robusta: inyectar en `theme.liquid` con guard por `page.url`

## Estado al guardar esta memoria

- ✅ Snippet `page-precios-schema.liquid` existe en `snippets/` con priceRange correcto
- ✅ Código inyectado en `theme.liquid` líneas 304-306 con `page.handle == 'precios'`
- ✅ **VERIFICADO** — curl confirma ambos priceRange en el HTML renderizado
- ✅ **COMPLETADO 2026-06-24**

## Verificación post-guardado

```bash
curl -s https://innovartmedical.com/pages/precios | grep -i priceRange
```

Debe devolver:
```
"priceRange": "COP 8000000-11000000"
"priceRange": "USD 3500-4500"
```

## Archivos involucrados (Code Editor Shopify)

| Archivo | Carpeta | Estado |
|---|---|---|
| `page-precios-schema.liquid` | `snippets/` | ✅ Con priceRange |
| `theme.liquid` | `layout/` | ⚠️ Pendiente guardar |
| `page.liquid` | `templates/customers/` | ✅ Sin tocar (customers) |
| `page.json` | `templates/` | ✅ Existe (default) |

## Relacionado

- [[geo-visibilidad-ia-diagnostico-2026-06-19]] — diagnóstico original, /pages/precios era P1
- [[fase-2-upgrade-blogs-contenido-2026-06-22]] — precios Colombia/Panamá definidos aquí
- [[schema-arquitectura-logica-no-tocar]] — reglas schema generales del tema
