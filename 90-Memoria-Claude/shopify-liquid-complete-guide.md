---
name: Shopify Liquid — Guía Completa
description: Sintaxis, filtros, tags, bucles, condicionales con ejemplos copy-paste para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Shopify Liquid — Guía Completa

## Introducción a Liquid

Liquid es el lenguaje de plantillas de Shopify. Permite mezclar HTML estático con lógica dinámica.

**Tres tipos de sintaxis:**

```liquid
{{ variable }}        # Output: imprime valor
{% tag %}             # Logic: controla flujo
{% comment %}         # Comment: comentario (no se renderiza)
```

---

## 1. Variables y Output

### Output básico

```liquid
{{ product.title }}
{{ product.price }}
{{ customer.first_name }}
```

**Contexto:** Las variables están disponibles según la página/contexto:
- `/products/*` → `product`, `collections`
- `/cart` → `cart`
- `/account` → `customer`

### Output con formato

```liquid
{{ product.price | money }}                 # $12.99
{{ product.created_at | date: "%Y-%m-%d" }} # 2026-06-30
{{ string | upcase }}                       # HELLO WORLD
```

### Acceso a arrays/objetos

```liquid
{{ product.variants[0].title }}
{{ product.metafields.custom.section_name.value }}
```

---

## 2. Filtros (Filters)

Filtros transforman variables. Se encadenan con `|`.

### Filtros de string

```liquid
{{ "hello world" | upcase }}              # HELLO WORLD
{{ "HELLO" | downcase }}                  # hello
{{ "hello world" | capitalize }}          # Hello world
{{ "hello" | size }}                      # 5
{{ " hello " | strip }}                   # hello (sin espacios)
{{ "hello-world" | replace: "-", " " }}   # hello world
{{ "hello" | append: " world" }}          # hello world
{{ "prefix-" | prepend: "hello" }}        # hello-prefix
```

### Filtros numéricos

```liquid
{{ 4.6 | ceil }}              # 5
{{ 4.6 | floor }}             # 4
{{ 4.567 | round: 2 }}        # 4.57
{{ 100 | divided_by: 3 }}     # 33 (integer division)
{{ 100 | modulo: 3 }}         # 1
{{ -5 | abs }}                # 5
{{ -5 | times: 3 }}           # -15
{{ 5 | plus: 3 }}             # 8
{{ 5 | minus: 3 }}            # 2
```

### Filtros de array

```liquid
{% assign colors = "red,blue,green" | split: "," %}
{{ colors | join: " - " }}                    # red - blue - green
{{ colors | size }}                           # 3
{{ colors | first }}                          # red
{{ colors | last }}                           # green
{{ colors | map: "title" | join: ", " }}      # (para array de objetos)
{{ colors | reverse | join: ", " }}           # green, blue, red
```

### Filtros de dinero/fecha

```liquid
{{ 1234.5 | money }}                  # $1,234.50
{{ 1234.5 | money_with_currency }}    # $1,234.50 USD
{{ product.created_at | date: "%B %d, %Y" }}  # June 30, 2026
{{ "now" | date: "%s" }}              # Timestamp Unix
```

### Filtros de URL

```liquid
{{ "hello world" | url_encode }}      # hello%20world
{{ "hello world" | url_decode }}      # hello world
{{ url | url_param_escape }}          # Para URLs en href
```

### Filtro `where`

```liquid
{% assign highlighted = products | where: "published", true %}
{% for product in highlighted %}
  {{ product.title }}
{% endfor %}
```

---

## 3. Tags de Control (Control Flow)

### If / Elsif / Else

```liquid
{% if product.available %}
  <p>In stock</p>
{% elsif product.coming_soon %}
  <p>Coming soon</p>
{% else %}
  <p>Out of stock</p>
{% endif %}
```

**Operadores de comparación:**

```liquid
{% if price > 100 %}              # >
{% if price >= 100 %}             # >=
{% if price < 100 %}              # <
{% if price <= 100 %}             # <=
{% if price == 100 %}             # ==
{% if price != 100 %}             # !=
```

**Operadores lógicos:**

```liquid
{% if price > 50 and stock > 0 %}
  <p>Expensive and available</p>
{% endif %}

{% if color == "red" or color == "blue" %}
  <p>Primary color</p>
{% endif %}

{% unless product.available %}
  <p>Out of stock</p>
{% endunless %}
```

### Case / When

```liquid
{% case product.type %}
  {% when "Shirt" %}
    <p>This is a shirt</p>
  {% when "Pants" %}
    <p>This is pants</p>
  {% else %}
    <p>Unknown product</p>
{% endcase %}
```

---

## 4. Bucles (Loops)

### For loop básico

```liquid
{% for product in collection.products %}
  <h2>{{ product.title }}</h2>
  <p>${{ product.price | divided_by: 100 }}</p>
{% endfor %}
```

### For loop con índice

```liquid
{% for product in collection.products %}
  <p>Product #{{ forloop.index }}: {{ product.title }}</p>
  <!-- forloop.index empieza en 1 -->
  <!-- forloop.index0 empieza en 0 -->
{% endfor %}
```

### Propiedades de forloop

```liquid
{% for item in collection.products %}
  {{ forloop.index }}       # 1, 2, 3...
  {{ forloop.index0 }}      # 0, 1, 2...
  {{ forloop.first }}       # true si es el primer item
  {{ forloop.last }}        # true si es el último
  {{ forloop.length }}      # Total de items
  {{ forloop.rindex }}      # Índice inverso (3, 2, 1...)
  {{ forloop.rindex0 }}     # Índice inverso (2, 1, 0...)
{% endfor %}
```

### Break y Continue

```liquid
{% for i in (1..10) %}
  {% if i == 5 %}
    {% break %}  <!-- salir del loop -->
  {% endif %}
  {{ i }}
{% endfor %}

{% for i in (1..10) %}
  {% if i == 5 %}
    {% continue %}  <!-- ir al siguiente -->
  {% endif %}
  {{ i }}
{% endfor %}
```

### Limitar/Offset

```liquid
{% for product in collection.products limit: 5 %}
  {{ product.title }}
{% endfor %}

{% for product in collection.products offset: 10 %}
  {{ product.title }}
{% endfor %}
```

### Reverse

```liquid
{% for product in collection.products reversed %}
  {{ product.title }}
{% endfor %}
```

---

## 5. Variables Locales (Assign / Capture)

### Assign

```liquid
{% assign product_name = product.title %}
<h1>{{ product_name }}</h1>

{% assign price_in_dollars = product.price | divided_by: 100 %}
<p>${{ price_in_dollars }}</p>

{% assign is_available = product.available %}
```

### Capture (múltiples líneas)

```liquid
{% capture my_html %}
  <div class="product">
    <h2>{{ product.title }}</h2>
    <p>${{ product.price | divided_by: 100 }}</p>
  </div>
{% endcapture %}

{{ my_html }}
```

### Increment / Decrement

```liquid
{% increment counter %}  # 1
{% increment counter %}  # 2
{% increment counter %}  # 3

{% decrement counter %}  # -1
```

---

## 6. Condicionales Avanzados

### Contains

```liquid
{% if product.title contains "Red" %}
  <p>This is a red product</p>
{% endif %}
```

### Múltiples condiciones

```liquid
{% if product.type == "Shirt" and product.available and product.price < 5000 %}
  <p>Cheap shirt in stock</p>
{% endif %}
```

### Nil / Empty

```liquid
{% if product.description == nil %}
  <p>No description</p>
{% endif %}

{% if product.variants == empty %}
  <p>No variants</p>
{% endif %}

{% if product.variants != blank %}
  <p>Has variants</p>
{% endif %}
```

---

## 7. Iteración sobre Metafields

```liquid
<!-- Acceso a metafield -->
{{ product.metafields.namespace.key.value }}

<!-- Ejemplo real -->
{{ product.metafields.custom.highlights.value }}

<!-- Loop en metafields lista -->
{% for item in product.metafields.custom.faq.value %}
  <h3>{{ item.question }}</h3>
  <p>{{ item.answer }}</p>
{% endfor %}
```

---

## 8. Condicionales con Filtros

```liquid
{% if product.variants | size > 1 %}
  <p>Multiple variants available</p>
{% endif %}

{% assign highlighted = products | where: "published", true %}
{% if highlighted | size > 0 %}
  <p>{{ highlighted | size }} highlighted products</p>
{% endif %}
```

---

## 9. Include y Render (Reutilización)

### Include (comparte scope)

```liquid
{% include 'product-card' %}  <!-- reutiliza variables actuales -->
```

### Render (scope aislado, más rápido)

```liquid
{% render 'product-card', product: product %}

<!-- Pasar múltiples variables -->
{% render 'product-details', 
    product: product,
    show_price: true,
    collection: collection
%}
```

### Variables en partials

```liquid
<!-- En partial: product-card.liquid -->
<div class="card">
  <h3>{{ product.title }}</h3>
  <p>${{ product.price | divided_by: 100 }}</p>
</div>
```

---

## 10. Casos de Uso Comunes en Innovart

### Mostrar precio con formato

```liquid
<span class="price">
  {{ product.price | money }}
</span>
```

### Listar variantes seleccionables

```liquid
<select name="variant">
  {% for variant in product.variants %}
    <option value="{{ variant.id }}">
      {{ variant.title }} - ${{ variant.price | money }}
    </option>
  {% endfor %}
</select>
```

### Mostrar descripción truncada

```liquid
{{ product.description | strip_html | truncatewords: 20 }}
```

### Loop con números (rango)

```liquid
{% for i in (1..5) %}
  <p>Item {{ i }}</p>
{% endfor %}
```

### Validar si producto está en colección

```liquid
{% if collection.products | where: "id", product.id | size > 0 %}
  <p>This product is in the collection</p>
{% endif %}
```

### Mostrar primero/último producto

```liquid
{% assign first_product = collection.products | first %}
<h3>{{ first_product.title }}</h3>

{% assign last_product = collection.products | last %}
<h3>{{ last_product.title }}</h3>
```

---

## 11. Objeto `request` (URL, Parámetros)

```liquid
{{ request.path }}           # /products/my-product
{{ request.host }}           # example.com
{{ request.page_type }}      # product, collection, cart...

{% if request.page_type == "product" %}
  <p>This is a product page</p>
{% endif %}

<!-- Parámetro de query string -->
{{ request.query_string }}   # color=red&size=large

<!-- Acceder a un parámetro específico vía JavaScript -->
```

---

## 12. Contexto Global en Innovart

### Variables disponibles según página

**Página de producto:**
```liquid
{{ product.title }}
{{ product.description }}
{{ product.price }}
{{ product.available }}
{{ product.variants }}
{{ product.collections }}
{{ product.featured_image.src }}
```

**Página de carrito:**
```liquid
{{ cart.item_count }}
{{ cart.total_price }}
{% for item in cart.items %}
  {{ item.product.title }}
  {{ item.quantity }}
  {{ item.price }}
{% endfor %}
```

**Customer (si está logueado):**
```liquid
{% if customer %}
  <p>Welcome {{ customer.first_name }}!</p>
{% endif %}
```

---

## 13. Debugging en Liquid

### Usar comment para ocultar

```liquid
{% comment %}
  Este código no se renderiza
  {{ product.title }}
{% endcomment %}
```

### Usar inspect para ver estructura

```liquid
{{ product | inspect }}  <!-- Imprime toda la estructura -->
```

### Log en Shopify Theme Editor

```liquid
{% assign debug = "Valor: " | append: product.price %}
<!-- Abre la consola de desarrollador para ver logs -->
```

---

## 14. Gotchas Comunes

### Espacios en blanco

```liquid
{%- if true -%}  # - elimina espacios en blanco
  <p>Hello</p>
{%- endif -%}
```

### División entera

```liquid
{{ 10 | divided_by: 3 }}    # 3 (no 3.33)
{{ 10.0 | divided_by: 3 }}  # 3.33 (convierte a float)
```

### For loop vacío

```liquid
{% for item in empty_array %}
  <p>{{ item }}</p>
{% else %}
  <p>No items</p>
{% endfor %}
```

### Nil vs False

```liquid
{% if nil %}           # falso
{% if false %}         # falso
{% if 0 %}             # verdadero (0 no es nil/false)
{% if "" %}            # verdadero (string vacío no es nil)
```

---

## 15. Recursos Oficiales

- [Shopify Liquid Docs](https://shopify.dev/api/liquid)
- [Shopify Theme Academy](https://shopify.dev/themes)
- [Liquid Tags Reference](https://shopify.dev/api/liquid/tags)
- [Liquid Filters Reference](https://shopify.dev/api/liquid/filters)

---

## Resumen Rápido

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| Output | `{{ variable }}` | `{{ product.title }}` |
| Filter | `{{ var \| filter }}` | `{{ price \| money }}` |
| If | `{% if condition %}` | `{% if product.available %}` |
| Loop | `{% for item in array %}` | `{% for p in products %}` |
| Assign | `{% assign var = value %}` | `{% assign name = product.title %}` |
| Include | `{% include 'partial' %}` | `{% render 'card', product: product %}` |

