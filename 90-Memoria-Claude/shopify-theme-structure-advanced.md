---
name: Shopify Theme — Estructura Avanzada
description: theme.liquid, sections, app extensions, CLI, deployment, workflow en Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Shopify Theme — Estructura Avanzada

## 1. Estructura de Carpetas Theme

```
my-theme/
├── assets/
│   ├── css/
│   │   └── theme.css
│   ├── js/
│   │   └── theme.js
│   └── images/
├── config/
│   └── settings_schema.json         # Schema de configuración
├── layout/
│   ├── theme.liquid                 # Layout principal
│   ├── password.liquid              # Página de contraseña
│   └── checkout.liquid              # Checkout (solo lectura en Shopify Plus)
├── sections/
│   ├── header.liquid
│   ├── footer.liquid
│   ├── product-template.liquid
│   └── collection-template.liquid
├── snippets/
│   ├── product-card.liquid
│   ├── image-with-text.liquid
│   └── breadcrumb.liquid
├── templates/
│   ├── index.json                   # Página de inicio (editor visual)
│   ├── product.json
│   ├── collection.json
│   ├── page.json
│   └── (otros templates)
└── package.json
```

---

## 2. theme.liquid — Layout Principal

`layout/theme.liquid` es el HTML wrapper de todas las páginas.

```liquid
<!DOCTYPE html>
<html lang="{{ shop.locale }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ page_title }}</title>
  
  <!-- SEO Meta Tags -->
  {% if page_description %}
    <meta name="description" content="{{ page_description | escape }}">
  {% endif %}
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="{{ 'favicon.svg' | asset_url }}">
  
  <!-- Stylesheets -->
  {{ 'theme.css' | asset_url | stylesheet_tag }}
  
  <!-- App Embeds Head (Shopify apps) -->
  {{ content_for_header }}
  
  <!-- Custom Head Code (desde settings_schema) -->
  {{ settings.custom_head }}
</head>
<body class="{{ template | replace: '.', ' ' }}">
  
  <!-- Accesibilidad: Skip to content -->
  <a href="#main-content" class="skip-to-content">Skip to content</a>
  
  <!-- Header -->
  {% section 'header' %}
  
  <!-- Main Content -->
  <main id="main-content">
    {{ content_for_layout }}
  </main>
  
  <!-- Footer -->
  {% section 'footer' %}
  
  <!-- JavaScript -->
  {{ 'theme.js' | asset_url | script_tag }}
  
  <!-- Custom Scripts -->
  {{ settings.custom_body }}
</body>
</html>
```

### Variables Disponibles en theme.liquid

```liquid
{{ page_title }}              # Título de la página
{{ page_description }}        # Descripción SEO
{{ template }}                # Nombre del template actual (e.g., "product", "collection")
{{ template | replace: '.', ' ' }}  # Clase CSS dinámica
{{ content_for_header }}      # Inyectado por Shopify (tracking, apps)
{{ content_for_layout }}      # Contenido de la página actual
{{ shop.name }}               # Nombre de la tienda
{{ shop.locale }}             # Idioma (es, en, etc.)
```

---

## 3. Sections — Bloques Reutilizables

Las sections son componentes reutilizables. Se definen en `sections/` y se incluyen en templates.

### Estructura básica de una section

```liquid
<!-- sections/hero-banner.liquid -->

{% schema
{
  "name": "Hero Banner",
  "settings": [
    {
      "type": "image_picker",
      "id": "image",
      "label": "Image"
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Welcome"
    },
    {
      "type": "text",
      "id": "button_text",
      "label": "Button Text",
      "default": "Shop Now"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Button Link"
    }
  ],
  "presets": [
    {
      "name": "Hero Banner",
      "settings": {}
    }
  ]
}
{% endschema %}

<div class="hero-banner" style="background-image: url('{{ section.settings.image | image_url: width: 1500 }}')">
  <h1>{{ section.settings.heading }}</h1>
  <a href="{{ section.settings.button_link }}" class="button">
    {{ section.settings.button_text }}
  </a>
</div>

{% stylesheet %}
  .hero-banner {
    background-size: cover;
    background-position: center;
    padding: 100px 20px;
    text-align: center;
    color: white;
  }
{% endstylesheet %}
```

### Tipos de settings en schema

```json
{
  "type": "text",
  "id": "title",
  "label": "Title"
}

{
  "type": "textarea",
  "id": "description",
  "label": "Description"
}

{
  "type": "number",
  "id": "width",
  "label": "Width",
  "default": 100
}

{
  "type": "range",
  "id": "columns",
  "min": 1,
  "max": 4,
  "label": "Columns",
  "default": 3
}

{
  "type": "image_picker",
  "id": "image",
  "label": "Image"
}

{
  "type": "collection",
  "id": "collection",
  "label": "Collection"
}

{
  "type": "product",
  "id": "product",
  "label": "Product"
}

{
  "type": "url",
  "id": "link",
  "label": "Link"
}

{
  "type": "select",
  "id": "alignment",
  "label": "Alignment",
  "options": [
    { "value": "left", "label": "Left" },
    { "value": "center", "label": "Center" },
    { "value": "right", "label": "Right" }
  ]
}

{
  "type": "checkbox",
  "id": "show_price",
  "label": "Show Price",
  "default": true
}

{
  "type": "color",
  "id": "background_color",
  "label": "Background Color",
  "default": "#ffffff"
}

{
  "type": "font",
  "id": "heading_font",
  "label": "Heading Font"
}
```

### Blocks dentro de sections (elementos dinámicos)

```liquid
{% schema
{
  "name": "Testimonials",
  "settings": [
    { "type": "text", "id": "title", "label": "Title" }
  ],
  "blocks": [
    {
      "type": "testimonial",
      "name": "Testimonial",
      "settings": [
        { "type": "text", "id": "quote", "label": "Quote" },
        { "type": "text", "id": "author", "label": "Author" }
      ]
    }
  ]
}
{% endschema %}

<div class="testimonials">
  <h2>{{ section.settings.title }}</h2>
  {% for block in section.blocks %}
    <div class="testimonial" {{ block.shopify_attributes }}>
      <p>"{{ block.settings.quote }}"</p>
      <p class="author">— {{ block.settings.author }}</p>
    </div>
  {% endfor %}
</div>
```

---

## 4. Templates JSON — Editor Visual

Los templates en `templates/` pueden ser JSON (editables en Shopify Theme Editor) o Liquid.

### index.json (Página de inicio)

```json
{
  "sections": {
    "hero": {
      "type": "hero-banner",
      "settings": {
        "heading": "Welcome to our store",
        "button_text": "Shop Now",
        "button_link": "/collections/all"
      }
    },
    "featured-products": {
      "type": "featured-products",
      "settings": {
        "title": "Featured Products",
        "limit": 4
      }
    },
    "newsletter": {
      "type": "newsletter",
      "settings": {
        "title": "Subscribe"
      }
    }
  },
  "order": ["hero", "featured-products", "newsletter"]
}
```

### product.json

```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "settings": {}
    },
    "related": {
      "type": "related-products",
      "settings": {
        "limit": 4
      }
    }
  },
  "order": ["main", "related"]
}
```

---

## 5. Snippets — Componentes Pequeños

Los snippets se incluyen con `{% render %}` (recomendado) o `{% include %}`.

```liquid
<!-- snippets/product-card.liquid -->
<div class="product-card">
  {% if product.featured_image %}
    <img src="{{ product.featured_image | image_url: width: 300 }}" alt="{{ product.featured_image.alt }}">
  {% endif %}
  
  <h3>{{ product.title }}</h3>
  <p class="price">{{ product.price | money }}</p>
  
  {% if product.available %}
    <a href="{{ product.url }}" class="button">View Product</a>
  {% else %}
    <p class="out-of-stock">Out of Stock</p>
  {% endif %}
</div>

{% stylesheet %}
  .product-card {
    border: 1px solid #e0e0e0;
    padding: 16px;
    text-align: center;
  }
  .product-card img {
    max-width: 100%;
  }
  .price {
    font-size: 1.5rem;
    font-weight: bold;
  }
{% endstylesheet %}
```

Llamar snippet:

```liquid
<!-- En una section o template -->
{% render 'product-card', product: product %}

<!-- Con múltiples variables -->
{% render 'product-card', product: product, show_stock: true %}
```

---

## 6. App Extensions (Bloques de Apps)

Las apps de Shopify pueden inyectar bloques dentro de sections.

```json
{
  "blocks": [
    {
      "type": "@app",
      "name": "App Block",
      "settings": []
    }
  ]
}
```

**En theme.liquid**, los app blocks se insertan automáticamente si están en el schema.

---

## 7. Assets — CSS y JavaScript

### CSS

```liquid
<!-- En theme.liquid o en <stylesheet> dentro de sections -->
{{ 'theme.css' | asset_url | stylesheet_tag }}
```

En `assets/css/theme.css`:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  color: #333;
  background: #fff;
}

header {
  background: #f5f5f5;
  padding: 20px;
}

.product-card {
  border: 1px solid #e0e0e0;
  padding: 16px;
  transition: box-shadow 0.3s ease;
}

.product-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

### JavaScript

```liquid
{{ 'theme.js' | asset_url | script_tag }}
```

En `assets/js/theme.js`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  console.log('Theme loaded');
  
  // Ejemplo: agregar clase a enlaces activos
  const currentPath = window.location.pathname;
  document.querySelectorAll('nav a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });
});

// Ejemplo: Carrito
function addToCart(variantId, quantity) {
  fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      items: [{ id: variantId, quantity: quantity }]
    })
  })
  .then(res => res.json())
  .then(cart => console.log('Added to cart:', cart))
  .catch(err => console.error('Error:', err));
}
```

---

## 8. Configuración de Theme (settings_schema.json)

```json
{
  "sections": [
    {
      "name": "Colors",
      "settings": [
        {
          "type": "color",
          "id": "primary_color",
          "label": "Primary Color",
          "default": "#000000"
        },
        {
          "type": "color",
          "id": "secondary_color",
          "label": "Secondary Color",
          "default": "#ffffff"
        }
      ]
    },
    {
      "name": "Typography",
      "settings": [
        {
          "type": "font",
          "id": "heading_font",
          "label": "Heading Font"
        }
      ]
    }
  ]
}
```

Acceder en Liquid:

```liquid
<style>
  :root {
    --primary-color: {{ settings.primary_color }};
    --secondary-color: {{ settings.secondary_color }};
  }
</style>
```

---

## 9. Shopify Theme CLI

### Instalación

```bash
npm install -g @shopify/cli @shopify/theme
```

### Comandos básicos

```bash
# Crear un nuevo theme
shopify theme init

# Conectar a una tienda
shopify theme dev --store=mystore.myshopify.com

# Uploads cambios
shopify theme push

# Publicar un draft theme
shopify theme publish

# Listar themes
shopify theme list

# Eliminar theme
shopify theme delete --theme-id=123456789
```

### Workflow en Innovart

```bash
# 1. Conectar a la tienda
cd ~/innovart-theme
shopify theme dev --store=innovartmedical.myshopify.com

# 2. El CLI abre un servidor local en http://localhost:9292
# Editar archivos localmente, cambios se sincronizan en vivo

# 3. Una vez completado, hacer push
shopify theme push

# 4. Si listo, publicar
shopify theme publish
```

---

## 10. Versionado de theme.liquid (PROTOCOLO INNOVART)

**REGLA ABSOLUTA:** Cada cambio en `layout/theme.liquid` requiere versionado.

```markdown
# /Obsidian-Innovart/versionado-theme-liquid.md

## V1 — Original (2026-06-28)
- Estructura base: `<head>` + `<body>` + sections
- Scripts: tracking-basic.js

## V2 — Qikify Integration (2026-06-29)
- Agregado: `<script src="https://www.qikify.com/app/qikify.min.js"></script>`
- Motivo: Sin esto, window.BContact no existía → formularios no disparaban POST
- Verificado: `typeof window.BContact === "object"`

## V3 — CAPI Pixel + fbclid (2026-06-30)
- Agregado: Meta Pixel `fbq('track', 'PageView')`
- Agregado: fbclid capture script en <head>
- Motivo: EMQ 4.9 → 5.5+, recuperar eventos de conversión

[...changelog...]
```

---

## 11. PageFly vs GemPages en theme.liquid

**REGLA CRÍTICA:** Innovart usa **PageFly para landings de ciudad**, **GemPages para home5 (Panamá)**.

```liquid
<!-- En theme.liquid -->

<!-- PageFly -->
{{ settings.pagefly_head_content }}

<!-- GemPages -->
{{ settings.gempages_head }}

<!-- Distintos porque inyectan JavaScript diferente -->
<!-- NUNCA quitar ninguno -->
```

---

## 12. Metafields en theme.liquid

```liquid
<!-- Acceder a metafields en product -->
{{ product.metafields.custom.highlights.value }}

<!-- Registrar en theme.liquid (sólo lectura) -->
<!-- Los metafields se cargan automáticamente -->
```

---

## 13. Gotchas Comunes

### Problema: theme.liquid sin </body>

Si `theme.liquid` no termina con `</body>`, ciertos scripts (como Qikify) no se cargan.

**Solución:**

```liquid
  <!-- Contenido -->
  
  </body>  <!-- NUNCA olvidar -->
</html>
```

### Problema: CSS no carga

```liquid
<!-- INCORRECTO -->
<link rel="stylesheet" href="/assets/theme.css">

<!-- CORRECTO -->
{{ 'theme.css' | asset_url | stylesheet_tag }}
```

### Problema: JavaScript conflictua con jQuery

```javascript
// Si jQuery está presente (algunas apps la inyectan)
if (typeof jQuery !== 'undefined') {
  jQuery(document).ready(function($) {
    // Código seguro
  });
}
```

---

## 14. Performance — Mejores Prácticas

### Lazy Load Images

```liquid
<img 
  src="{{ product.featured_image | image_url: width: 100 }}"
  srcset="{{ product.featured_image | image_url: width: 200 }} 200w, {{ product.featured_image | image_url: width: 400 }} 400w"
  loading="lazy"
  alt="{{ product.featured_image.alt }}"
>
```

### Preload Critical Resources

```liquid
{% if template == 'product' %}
  <link rel="preload" as="script" href="{{ 'product-picker.js' | asset_url }}">
{% endif %}
```

### Defer Non-Critical JS

```liquid
{{ 'analytics.js' | asset_url | script_tag: defer: true }}
```

---

## 15. Deployment Checklist (Innovart)

- [ ] Verificar `</body>` en theme.liquid
- [ ] Confirmar scripts (Qikify, Meta Pixel, fbclid)
- [ ] Test E2E en móvil (iOS/Android)
- [ ] Verificar Clarity tracking
- [ ] Probar formularios (POST a Worker)
- [ ] Guardar v++ en Obsidian con changelog
- [ ] Rollback script ready en caso de error

---

## 16. Recursos Oficiales

- [Shopify Theme Docs](https://shopify.dev/themes)
- [Shopify Liquid Reference](https://shopify.dev/api/liquid)
- [Shopify Theme CLI](https://shopify.dev/tools/theme-kit)
- [Shopify App Blocks](https://shopify.dev/apps/blocks)

