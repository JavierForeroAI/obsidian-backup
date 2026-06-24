---
name: shopify-blog-post-template-tecnico
description: "Especificación técnica completa: JSON schema de metafields, template Liquid blog-post.json, CSS, y mutations GraphQL para crear blog posts."
metadata:
  type: technical
  fecha: 2026-06-23
  stack: Shopify + Liquid + GraphQL
---

# Especificación Técnica: Blog Posts Médicos en Shopify

## 1. Metafield Definitions

### Crear vía Shopify Admin
`Settings > Custom data > Blogs > Metafields > Manage definitions`

O via CLI:
```bash
shopify app function run create-metafield --location blog-post
```

### JSON structure (para referencia / CLI)

```json
{
  "definitions": [
    {
      "namespace": "custom",
      "key": "hero_eyebrow",
      "name": "Hero Eyebrow",
      "description": "Etiqueta pequeña arriba del título (ej: 'Ciencia capilar')",
      "type": "single_line_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "hero_subtitle",
      "name": "Hero Subtitle",
      "description": "Texto descriptivo bajo el título (ej: 'No es un exceso de hormonas...')",
      "type": "rich_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "featured_image_url",
      "name": "Featured Image URL",
      "description": "URL de la imagen destacada del artículo (opcional)",
      "type": "url_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "schema_article",
      "name": "Schema Article JSON-LD",
      "description": "JSON-LD schema para Article (NO tocar manualmente; generado por script)",
      "type": "json_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "schema_localbusiness",
      "name": "Schema LocalBusiness JSON-LD",
      "description": "JSON-LD schema array para 5 LocalBusiness sedes (NO tocar manualmente)",
      "type": "json_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "related_articles",
      "name": "Related Articles",
      "description": "Array JSON de slugs de artículos relacionados (ej: ['slug1', 'slug2', 'slug3'])",
      "type": "json_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "author_name",
      "name": "Author Name",
      "description": "Nombre del autor (ej: 'Dr. Fabián Carreño Jiménez')",
      "type": "single_line_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "author_title",
      "name": "Author Title",
      "description": "Título profesional del autor (ej: 'Director Médico, Cirujano Plástico y Reconstructivo')",
      "type": "single_line_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "author_bio",
      "name": "Author Bio",
      "description": "Biografía corta del autor (opcional, rich text)",
      "type": "rich_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "cta_text",
      "name": "CTA Text",
      "description": "Texto del bloque CTA (Call-To-Action)",
      "type": "rich_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "cta_button_label",
      "name": "CTA Button Label",
      "description": "Texto del botón CTA (ej: 'Escríbenos al WhatsApp')",
      "type": "single_line_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "cta_button_url",
      "name": "CTA Button URL",
      "description": "URL del botón CTA (base, sin ?text=...)",
      "type": "url_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "whatsapp_tracking_slug",
      "name": "WhatsApp Tracking Slug",
      "description": "Slug para parámetro ?text= (ej: 'alopecia-androgenetica-por-que-se-cae-el-pelo')",
      "type": "single_line_text_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "sedes_enabled",
      "name": "Show Sedes Section",
      "description": "Mostrar sección de sedes (true/false)",
      "type": "boolean",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    },
    {
      "namespace": "custom",
      "key": "sedes_data",
      "name": "Sedes Data",
      "description": "Array JSON de sedes (OPCIONAL si usas globalData; NO tocar si es centralizado)",
      "type": "json_field",
      "owner_type": "ARTICLE",
      "access": {
        "admin": "MERCHANT_READ_WRITE"
      }
    }
  ]
}
```

---

## 2. Template Liquid — `blog-post.json` (o editar existente)

**Ubicación en theme:** `templates/blog-post.json` o `templates/article.json` (verificar cuál existe)

```liquid
{
  "sections": {
    "blog_hero": {
      "type": "blog-hero",
      "settings": {}
    },
    "blog_article": {
      "type": "blog-article",
      "settings": {}
    },
    "blog_author_sig": {
      "type": "blog-author-signature",
      "settings": {}
    },
    "blog_related": {
      "type": "blog-related-articles",
      "settings": {}
    },
    "blog_sedes": {
      "type": "blog-sedes",
      "settings": {}
    },
    "blog_cta": {
      "type": "blog-cta",
      "settings": {}
    },
    "blog_schema": {
      "type": "blog-schema-jsonld",
      "settings": {}
    }
  },
  "order": [
    "blog_hero",
    "blog_article",
    "blog_author_sig",
    "blog_related",
    "blog_sedes",
    "blog_cta",
    "blog_schema"
  ]
}
```

---

## 3. Secciones Liquid (en `sections/` directory)

### 3.1 `sections/blog-hero.liquid`

```liquid
<section class="hero hero-blog">
  {% if article.metafields.custom.featured_image_url.value %}
    <img src="{{ article.metafields.custom.featured_image_url.value }}" alt="{{ article.title }}" class="hero-bg">
  {% else %}
    <svg class="hsvg" viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#ffffff" stop-opacity=".9"/>
          <stop offset="1" stop-color="#C0A24E" stop-opacity=".7"/>
        </linearGradient>
      </defs>
      <g stroke="url(#g)" stroke-width="2" fill="none" stroke-linecap="round">
        <!-- SVG decorativo (mismo que local) -->
      </g>
    </svg>
  {% endif %}

  <div class="hwrap">
    {% if article.metafields.custom.hero_eyebrow.value %}
      <div class="eyebrow">{{ article.metafields.custom.hero_eyebrow.value }}</div>
    {% endif %}

    <h1>{{ article.title }}</h1>

    {% if article.metafields.custom.hero_subtitle.value %}
      <p class="deck">{{ article.metafields.custom.hero_subtitle.value }}</p>
    {% endif %}

    <div class="meta">
      {% if article.metafields.custom.author_name.value %}
        <span>
          <span class="pip"></span>
          Por <b>{{ article.metafields.custom.author_name.value }}</b>
        </span>
      {% endif %}

      <span>
        <span class="pip"></span>
        {% assign reading_time = article.content | strip_html | split: ' ' | size | divided_by: 200 | ceil %}
        {{ reading_time }} min de lectura
      </span>

      <span>
        <span class="pip"></span>
        {{ article.published_at | date: "%d de %B de %Y" | replace: 'January', 'enero' | replace: 'February', 'febrero' | replace: 'March', 'marzo' | replace: 'April', 'abril' | replace: 'May', 'mayo' | replace: 'June', 'junio' | replace: 'July', 'julio' | replace: 'August', 'agosto' | replace: 'September', 'septiembre' | replace: 'October', 'octubre' | replace: 'November', 'noviembre' | replace: 'December', 'diciembre' }}
      </span>
    </div>
  </div>
</section>

<style>
  .hero-blog {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0B232E 0%, #0E3A39 55%, #0F766E 130%);
    color: #fff;
  }
  .hero-bg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.3;
  }
  .hsvg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.16;
  }
  .hwrap {
    position: relative;
    max-width: 880px;
    margin: 0 auto;
    padding: 70px 24px 64px;
  }
  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #C0A24E;
    margin-bottom: 22px;
  }
  .eyebrow::before {
    content: "";
    width: 30px;
    height: 1px;
    background: #C0A24E;
  }
  .hero-blog h1 {
    font-size: clamp(33px, 5.2vw, 54px);
    line-height: 1.18;
    margin: 0 0 28px;
    max-width: 18ch;
    font-family: 'Fraunces', 'Georgia', serif;
    font-weight: 600;
  }
  .hero-blog .deck {
    font-size: clamp(18px, 2.4vw, 21px);
    line-height: 1.7;
    color: #D6E5E3;
    max-width: 62ch;
    margin: 0;
  }
  .meta {
    display: flex;
    flex-wrap: wrap;
    gap: 10px 26px;
    margin-top: 34px;
    font-size: 13.5px;
    color: #BFD3D1;
  }
  .meta span {
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .meta b {
    color: #fff;
    font-weight: 600;
  }
  .pip {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #C0A24E;
    display: inline-block;
  }
  @media (max-width: 620px) {
    .hwrap {
      padding: 50px 24px 40px;
    }
    .hero-blog h1 {
      font-size: 28px;
    }
    .hero-blog .deck {
      font-size: 16px;
    }
  }
</style>
```

### 3.2 `sections/blog-article.liquid`

```liquid
<main class="article">
  <div class="container">
    {% if article.content %}
      {{ article.content }}
    {% endif %}
  </div>
</main>

<style>
  .container {
    max-width: 760px;
    margin: 0 auto;
    padding: 0 24px;
  }
  .article {
    padding: 56px 0 30px;
  }
  /* Estilos del body: copiar de blog-post.css */
</style>
```

### 3.3 `sections/blog-author-signature.liquid`

```liquid
{% if article.metafields.custom.author_name.value %}
  <div class="author-sig">
    <div class="sig-title">{{ article.metafields.custom.author_name.value }}</div>
    <div class="sig-role">{{ article.metafields.custom.author_title.value }}</div>
    {% if article.metafields.custom.author_bio.value %}
      <div class="sig-bio">{{ article.metafields.custom.author_bio.value }}</div>
    {% endif %}
  </div>
{% endif %}

<style>
  .author-sig {
    background: #E9F3F1;
    border: 1px solid #D5E8E4;
    border-radius: 18px;
    padding: 24px 28px;
    margin: 46px 0 0;
    border-left: 4px solid #C0A24E;
    max-width: 760px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 30px;
  }
  .author-sig .sig-title {
    font-family: 'Fraunces', 'Georgia', serif;
    font-size: 18px;
    font-weight: 600;
    color: #0E2733;
    margin: 0 0 6px;
  }
  .author-sig .sig-role {
    font-size: 14px;
    color: #6B7B82;
    margin: 0;
  }
  .author-sig .sig-bio {
    font-size: 14px;
    color: #3A4D55;
    margin-top: 12px;
    line-height: 1.6;
  }
</style>
```

### 3.4 `sections/blog-related-articles.liquid`

```liquid
{% if article.metafields.custom.related_articles.value %}
  <div class="container">
    <div class="related-articles">
      <h4>📖 Lee también</h4>
      <ul class="rel-list">
        {% for slug in article.metafields.custom.related_articles.value %}
          {% assign related_article = blog.articles | where: 'handle', slug | first %}
          {% if related_article %}
            <li>
              <a href="{{ related_article.url }}">{{ related_article.title }}</a>
            </li>
          {% endif %}
        {% endfor %}
      </ul>
    </div>
  </div>
{% endif %}

<style>
  .related-articles {
    background: #E9F3F1;
    border: 1px solid #D5E8E4;
    border-radius: 18px;
    padding: 32px 28px;
    margin: 54px 0 40px;
    border-left: 4px solid #C0A24E;
  }
  .related-articles h4 {
    margin: 0 0 20px;
    font-size: 15px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #0B5A54;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .rel-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 14px;
  }
  .rel-list li {
    margin: 0;
    padding: 0;
  }
  .rel-list a {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 12px;
    background: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #D5E8E4;
    text-decoration: none;
    color: #0E2733;
    font-size: 14px;
    font-weight: 500;
    line-height: 1.4;
    transition: all 0.2s;
  }
  .rel-list a:hover {
    background: #fff;
    border-color: #0F766E;
    color: #0B5A54;
  }
  .rel-list a::before {
    content: "→";
    flex: 0 0 auto;
    color: #C0A24E;
    font-weight: 700;
  }
</style>
```

### 3.5 `sections/blog-sedes.liquid`

```liquid
{% if article.metafields.custom.sedes_enabled.value == true %}
  <section class="sedes-section">
    <div class="container">
      <h3>Nuestras sedes en Colombia y Panamá</h3>
      <div class="sedes-grid">
        {%- assign sedes = article.metafields.custom.sedes_data.value -%}
        {% if sedes %}
          {%- for sede in sedes -%}
            <div class="sede-card">
              <h4>{{ sede.city }}</h4>
              <p class="addr">{{ sede.address }}</p>
              <a href="{{ sede.gmb_link }}" class="sede-link" target="_blank">📍 Ver en Maps</a>
            </div>
          {%- endfor -%}
        {% else %}
          {%- comment -%}
            Fallback: sedes centralizadas (desde settings o global metaobject)
            Descomentar si usas esta opción
          {%- endcomment -%}
          <div class="sede-card">
            <h4>Bogotá</h4>
            <p class="addr">Calle 116 #9-72</p>
            <a href="https://share.google/unA0jM58IDgsldKhl" class="sede-link" target="_blank">📍 Ver en Maps</a>
          </div>
          <div class="sede-card">
            <h4>Medellín</h4>
            <p class="addr">CC Oviedo, Piso 16</p>
            <a href="https://share.google/rtE6wmM6zx18dG2JA" class="sede-link" target="_blank">📍 Ver en Maps</a>
          </div>
          <div class="sede-card">
            <h4>Barranquilla</h4>
            <p class="addr">Green Tower, Piso 14</p>
            <a href="https://share.google/NlrnR03cCYoShIKqz" class="sede-link" target="_blank">📍 Ver en Maps</a>
          </div>
          <div class="sede-card">
            <h4>Bucaramanga</h4>
            <p class="addr">HIC Business Center</p>
            <a href="https://goo.gl/maps/innovart-bucaramanga" class="sede-link" target="_blank">📍 Ver en Maps</a>
          </div>
          <div class="sede-card">
            <h4>Ciudad de Panamá</h4>
            <p class="addr">Costa del Este</p>
            <a href="https://share.google/GrA5R5tOD5HLKLSpM" class="sede-link" target="_blank">📍 Ver en Maps</a>
          </div>
        {% endif %}
      </div>
    </div>
  </section>
{% endif %}

<style>
  .sedes-section {
    background: #FBFAF7;
    padding: 56px 24px;
    margin: 0;
  }
  .sedes-section h3 {
    text-align: center;
    font-family: 'Fraunces', 'Georgia', serif;
    font-size: 28px;
    color: #0E2733;
    margin: 0 0 40px;
    max-width: 60ch;
    margin-left: auto;
    margin-right: auto;
  }
  .sedes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    max-width: 1000px;
    margin: 0 auto;
  }
  .sede-card {
    background: #FFFFFF;
    border: 1px solid #E8E3D8;
    border-radius: 18px;
    padding: 28px 24px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(14, 39, 51, 0.08);
  }
  .sede-card:hover {
    border-color: #0F766E;
    box-shadow: 0 8px 24px rgba(15, 118, 110, 0.12);
    transform: translateY(-2px);
  }
  .sede-card h4 {
    font-family: 'Fraunces', 'Georgia', serif;
    font-size: 22px;
    color: #0B5A54;
    margin: 0 0 12px;
    font-weight: 600;
  }
  .sede-card .addr {
    font-size: 14px;
    color: #3A4D55;
    margin: 0 0 16px;
    line-height: 1.5;
    font-weight: 500;
  }
  .sede-link {
    display: inline-block;
    color: #0B5A54;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 12px;
    border: 1px solid #EFE7CF;
    border-radius: 8px;
    margin: 0 6px 8px 0;
    transition: all 0.2s;
  }
  .sede-link:hover {
    background: #EFE7CF;
    color: #23210F;
  }
  @media (max-width: 620px) {
    .sedes-grid {
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 14px;
    }
    .sede-card {
      padding: 20px 16px;
    }
  }
</style>
```

### 3.6 `sections/blog-cta.liquid`

```liquid
{% if article.metafields.custom.cta_button_url.value %}
  <div class="cta">
    <div class="inner">
      <h3>Da el primer paso: agenda tu valoración capilar</h3>
      {% if article.metafields.custom.cta_text.value %}
        <p>{{ article.metafields.custom.cta_text.value }}</p>
      {% else %}
        <p>En Innovart Medical estudiamos tu caso con dermatoscopia y un plan personalizado. La primera valoración es sin costo y sin compromiso, presencial en nuestras sedes o por videollamada.</p>
      {% endif %}

      {% assign tracking_slug = article.metafields.custom.whatsapp_tracking_slug.value | default: article.handle %}
      {% assign wa_url = article.metafields.custom.cta_button_url.value | append: "?text=Hola,%20vengo%20del%20blog%20'" | append: tracking_slug | append: "'%20y%20me%20interesa%20saber%20m%C3%A1s" %}

      <a class="btn" href="{{ wa_url }}" target="_blank">
        📲 {{ article.metafields.custom.cta_button_label.value | default: "Escríbenos al +57 312 456 5014" }}
      </a>
      <a class="btn ghost" href="https://innovartmedical.com?utm_source=blog&utm_content={{ tracking_slug }}">
        Agenda tu valoración gratuita →
      </a>
    </div>
  </div>
{% endif %}

<style>
  .cta {
    margin: 54px auto 10px;
    max-width: 760px;
    padding: 0 24px;
    border-radius: 22px;
    overflow: hidden;
    background: linear-gradient(135deg, #0B232E, #0F766E);
    color: #fff;
    box-shadow: 0 18px 48px -24px rgba(14, 39, 51, 0.45);
  }
  .cta .inner {
    padding: 48px 44px;
    display: flex;
    flex-direction: column;
  }
  .cta h3 {
    color: #fff;
    font-size: 27px;
    margin: 0 0 14px;
    max-width: 22ch;
    font-family: 'Fraunces', 'Georgia', serif;
    font-weight: 600;
  }
  .cta p {
    color: #CFE2E0;
    font-size: 16px;
    margin: 0 0 28px;
    max-width: 54ch;
  }
  .cta .btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #C0A24E;
    color: #23210F;
    font-weight: 700;
    font-size: 15.5px;
    letter-spacing: 0.01em;
    text-decoration: none;
    padding: 15px 28px;
    border-radius: 999px;
    width: fit-content;
    margin-bottom: 12px;
    transition: all 0.2s;
  }
  .cta .btn:hover {
    background: #EFE7CF;
    color: #0E2733;
  }
  .cta .btn.ghost {
    background: transparent;
    color: #fff;
    border: 1.5px solid rgba(255, 255, 255, 0.45);
    margin-bottom: 16px;
  }
  .cta .btn.ghost:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.8);
  }
  @media (max-width: 620px) {
    .cta .inner {
      padding: 40px 30px;
    }
    .cta h3 {
      font-size: 22px;
    }
    .cta .btn.ghost {
      margin-bottom: 16px;
    }
  }
</style>
```

### 3.7 `sections/blog-schema-jsonld.liquid`

```liquid
{%- if article.metafields.custom.schema_article.value -%}
  <script type="application/ld+json">
    {{- article.metafields.custom.schema_article.value -}}
  </script>
{%- endif -%}

{%- if article.metafields.custom.schema_localbusiness.value -%}
  <script type="application/ld+json">
    {{- article.metafields.custom.schema_localbusiness.value -}}
  </script>
{%- endif -%}
```

---

## 4. CSS Centralizado — `assets/blog-post.css`

(Copiar de innovart_template.py `<style>` section, líneas 19–184 del HTML local)

```css
:root {
  --ink: #0E2733;
  --ink-soft: #3A4D55;
  --muted: #6B7B82;
  --teal: #0F766E;
  --teal-deep: #0B5A54;
  --teal-tint: #E9F3F1;
  --gold: #C0A24E;
  --gold-soft: #EFE7CF;
  --bg: #FBFAF7;
  --surface: #FFFFFF;
  --line: #E8E3D8;
  --shadow: 0 18px 48px -24px rgba(14, 39, 51, 0.45);
  --radius: 18px;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  font-size: 18px;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, .brandmark {
  font-family: 'Fraunces', 'Georgia', serif;
  font-weight: 600;
  letter-spacing: -0.01em;
}

img {
  max-width: 100%;
}

a {
  color: var(--teal-deep);
}

/* ---- Article content ---- */
.article h2 {
  font-size: 29px;
  margin: 52px 0 8px;
  padding-top: 14px;
  position: relative;
}

.article h2::after {
  content: "";
  display: block;
  width: 54px;
  height: 3px;
  background: var(--gold);
  border-radius: 3px;
  margin-top: 14px;
}

.article h3 {
  font-size: 21px;
  margin: 34px 0 6px;
  color: var(--teal-deep);
}

.article p {
  margin: 0 0 22px;
}

.article ul, .article ol {
  margin: 0 0 24px;
  padding-left: 1.25em;
}

.article li {
  margin: 0 0 10px;
}

.article strong {
  color: var(--ink);
}

.article table {
  width: 100%;
  border-collapse: collapse;
  margin: 30px 0;
  font-size: 15.5px;
  font-family: 'Inter', sans-serif;
}

.article table th,
.article table td {
  text-align: left;
  padding: 13px 16px;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
}

.article table th {
  background: var(--ink);
  color: #fff;
  font-weight: 600;
  font-size: 13px;
  letter-spacing: 0.04em;
}

.article table tr:nth-child(even) td {
  background: #F6F4EE;
}

.article blockquote {
  margin: 42px 0;
  padding: 6px 0 6px 30px;
  border-left: 4px solid var(--gold);
  font-family: 'Fraunces', serif;
  font-size: 25px;
  line-height: 1.4;
  color: var(--ink);
  font-style: italic;
}

.article blockquote cite {
  display: block;
  margin-top: 12px;
  font-family: 'Inter', sans-serif;
  font-style: normal;
  font-size: 14px;
  letter-spacing: 0.04em;
  color: var(--muted);
}

/* ---- Details (Accordion) ---- */
.article details {
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 6px 20px;
  margin: 0 0 12px;
  background: var(--surface);
}

.article details summary {
  cursor: pointer;
  font-family: 'Fraunces', serif;
  font-size: 18px;
  padding: 12px 0;
  color: var(--ink);
}

.article details summary:hover {
  color: var(--teal-deep);
}

.article details > * + * {
  margin-top: 12px;
}

/* ---- Key takeaways ---- */
.takeaways {
  background: var(--teal-tint);
  border-radius: var(--radius);
  padding: 28px 30px;
  margin: 36px 0;
  border: 1px solid #D5E8E4;
}

.takeaways h4 {
  margin: 0 0 14px;
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--teal-deep);
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 9px;
}

.takeaways ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.takeaways li {
  position: relative;
  padding-left: 30px;
  margin: 0 0 12px;
  font-size: 16.5px;
  line-height: 1.6;
}

.takeaways li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 9px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--teal);
  box-shadow: 0 0 0 4px rgba(15, 118, 110, 0.16);
}

.takeaways li:last-child {
  margin-bottom: 0;
}

/* ---- Note / disclaimer ---- */
.note {
  background: #FBF7EC;
  border: 1px solid var(--gold-soft);
  border-radius: 14px;
  padding: 20px 24px;
  margin: 34px 0;
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--ink-soft);
}

.note b {
  color: var(--ink);
}

@media (max-width: 620px) {
  .article h2 {
    font-size: 24px;
  }
  .article h3 {
    font-size: 18px;
  }
}
```

---

## 5. GraphQL Mutations — Crear Blog Posts

### 5.1 Crear blog post base (nombre, contenido, SEO)

```graphql
mutation CreateArticle(
  $blogId: ID!
  $title: String!
  $bodyHtml: String!
  $handle: String!
  $authorV3: String!
  $seo: SEOInput!
) {
  articleCreate(
    blogId: $blogId
    input: {
      title: $title
      bodyHtml: $bodyHtml
      handle: $handle
      authorV3: $authorV3
      publishedAt: "2026-06-23T00:00:00Z"
      seo: $seo
    }
  ) {
    article {
      id
      handle
      title
    }
    userErrors {
      field
      message
    }
  }
}

# Variables
{
  "blogId": "gid://shopify/Blog/BLOG_ID",
  "title": "Alopecia androgenética: por qué se cae el pelo (y qué la acelera)",
  "bodyHtml": "<p>La alopecia androgenética...</p>...",
  "handle": "alopecia-androgenetica-por-que-se-cae-el-pelo",
  "authorV3": "Dr. Fabián Carreño Jiménez",
  "seo": {
    "title": "Alopecia androgenética: por qué se cae el pelo | Innovart Medical",
    "description": "Qué es la alopecia androgenética, el papel de la DHT..."
  }
}
```

### 5.2 Llenar metafields (después de crear el artículo)

```graphql
mutation SetMetafields(
  $ownerId: ID!
  $metafields: [MetafieldsSetInput!]!
) {
  metafieldsSet(ownerId: $ownerId, metafields: $metafields) {
    metafields {
      id
      namespace
      key
    }
    userErrors {
      field
      message
    }
  }
}

# Variables
{
  "ownerId": "gid://shopify/Article/ARTICLE_ID",
  "metafields": [
    {
      "namespace": "custom",
      "key": "hero_eyebrow",
      "type": "single_line_text_field",
      "value": "Ciencia capilar"
    },
    {
      "namespace": "custom",
      "key": "hero_subtitle",
      "type": "rich_text_field",
      "value": "No es un exceso de hormonas: es la sensibilidad genética de tu folículo a la DHT..."
    },
    {
      "namespace": "custom",
      "key": "schema_article",
      "type": "json_field",
      "value": "{\"@context\":\"https://schema.org\",\"@type\":\"Article\",\"headline\":\"...\"}"
    },
    {
      "namespace": "custom",
      "key": "schema_localbusiness",
      "type": "json_field",
      "value": "[{\"@type\":\"LocalBusiness\",...}]"
    },
    {
      "namespace": "custom",
      "key": "related_articles",
      "type": "json_field",
      "value": "[\"slug1\",\"slug2\",\"slug3\"]"
    },
    {
      "namespace": "custom",
      "key": "author_name",
      "type": "single_line_text_field",
      "value": "Dr. Fabián Carreño Jiménez"
    },
    {
      "namespace": "custom",
      "key": "author_title",
      "type": "single_line_text_field",
      "value": "Director Médico, Cirujano Plástico y Reconstructivo especializado en Restauración Capilar"
    },
    {
      "namespace": "custom",
      "key": "cta_text",
      "type": "rich_text_field",
      "value": "<p>En Innovart Medical estudiamos tu caso...</p>"
    },
    {
      "namespace": "custom",
      "key": "cta_button_label",
      "type": "single_line_text_field",
      "value": "📲 Escríbenos al +57 312 456 5014"
    },
    {
      "namespace": "custom",
      "key": "cta_button_url",
      "type": "url_field",
      "value": "https://wa.me/573124565014"
    },
    {
      "namespace": "custom",
      "key": "whatsapp_tracking_slug",
      "type": "single_line_text_field",
      "value": "alopecia-androgenetica-por-que-se-cae-el-pelo"
    },
    {
      "namespace": "custom",
      "key": "sedes_enabled",
      "type": "boolean",
      "value": "true"
    },
    {
      "namespace": "custom",
      "key": "sedes_data",
      "type": "json_field",
      "value": "[{\"city\":\"Bogotá\",\"address\":\"Calle 116 #9-72\",\"gmb_link\":\"https://share.google/...\"}]"
    }
  ]
}
```

---

## 6. Python Script — Automatizar publicación

### `create_shopify_blogs.py`

```python
#!/usr/bin/env python3
import json
import os
from shopify import ShopifyResource
from shopify.session import Session
from shopify.shop import Shop

# Configuración
SHOP_NAME = "qr6t9m-bz"  # Reemplazar con tu tienda
ACCESS_TOKEN = os.getenv("SHOPIFY_ADMIN_TOKEN")  # Exportar desde .env
BLOG_HANDLE = "articulos-medicos"
BLOG_ID = "gid://shopify/Blog/BLOG_ID"  # Reemplazar

# Init session
session = Session(
    shop=SHOP_NAME,
    is_private_app=True,
    access_token=ACCESS_TOKEN,
)
ShopifyResource.activate_session(session)

# Leer datos
with open("blogs-shopify-data.json", "r", encoding="utf-8") as f:
    blogs_data = json.load(f)

# Crear blog posts
for blog in blogs_data:
    print(f"Creando: {blog['title']}")
    
    # GraphQL mutation 1: crear artículo
    query_create = """
    mutation CreateArticle(
      $blogId: ID!
      $title: String!
      $bodyHtml: String!
      $handle: String!
      $authorV3: String!
      $seo: SEOInput!
    ) {
      articleCreate(
        blogId: $blogId
        input: {
          title: $title
          bodyHtml: $bodyHtml
          handle: $handle
          authorV3: $authorV3
          publishedAt: "2026-06-23T00:00:00Z"
          seo: $seo
        }
      ) {
        article {
          id
          handle
        }
        userErrors {
          field
          message
        }
      }
    }
    """
    
    variables_create = {
        "blogId": BLOG_ID,
        "title": blog["title"],
        "bodyHtml": blog["body_html"],
        "handle": blog["slug"],
        "authorV3": blog["author_name"],
        "seo": {
            "title": blog["description"],
            "description": blog["keywords"]
        }
    }
    
    # Ejecutar mutation
    result = ShopifyResource.post(
        "/graphql.json",
        body=json.dumps({
            "query": query_create,
            "variables": variables_create
        })
    )
    
    if result.json()["data"]["articleCreate"]["userErrors"]:
        print(f"  ❌ Error: {result.json()['data']['articleCreate']['userErrors']}")
        continue
    
    article_id = result.json()["data"]["articleCreate"]["article"]["id"]
    print(f"  ✅ Artículo creado: {article_id}")
    
    # GraphQL mutation 2: llenar metafields
    query_metafields = """
    mutation SetMetafields(
      $ownerId: ID!
      $metafields: [MetafieldsSetInput!]!
    ) {
      metafieldsSet(ownerId: $ownerId, metafields: $metafields) {
        metafields {
          id
          namespace
          key
        }
        userErrors {
          field
          message
        }
      }
    }
    """
    
    variables_metafields = {
        "ownerId": article_id,
        "metafields": [
            {"namespace": "custom", "key": "hero_eyebrow", "type": "single_line_text_field", "value": blog["hero_eyebrow"]},
            {"namespace": "custom", "key": "hero_subtitle", "type": "rich_text_field", "value": blog["hero_subtitle"]},
            {"namespace": "custom", "key": "schema_article", "type": "json_field", "value": json.dumps(blog["schema_article"])},
            {"namespace": "custom", "key": "schema_localbusiness", "type": "json_field", "value": json.dumps(blog["schema_localbusiness"])},
            {"namespace": "custom", "key": "related_articles", "type": "json_field", "value": json.dumps(blog["related_articles"])},
            {"namespace": "custom", "key": "author_name", "type": "single_line_text_field", "value": blog["author_name"]},
            {"namespace": "custom", "key": "author_title", "type": "single_line_text_field", "value": blog["author_title"]},
            {"namespace": "custom", "key": "cta_text", "type": "rich_text_field", "value": blog["cta_text"]},
            {"namespace": "custom", "key": "cta_button_label", "type": "single_line_text_field", "value": "📲 Escríbenos al +57 312 456 5014"},
            {"namespace": "custom", "key": "cta_button_url", "type": "url_field", "value": "https://wa.me/573124565014"},
            {"namespace": "custom", "key": "whatsapp_tracking_slug", "type": "single_line_text_field", "value": blog["slug"]},
            {"namespace": "custom", "key": "sedes_enabled", "type": "boolean", "value": "true"},
        ]
    }
    
    result = ShopifyResource.post(
        "/graphql.json",
        body=json.dumps({
            "query": query_metafields,
            "variables": variables_metafields
        })
    )
    
    if result.json()["data"]["metafieldsSet"]["userErrors"]:
        print(f"  ⚠️  Error en metafields: {result.json()['data']['metafieldsSet']['userErrors']}")
    else:
        print(f"  ✅ Metafields llenos")

print("\n✅ Todos los blogs creados exitosamente")
```

---

## 7. Checklist de validación

- [ ] Metafield definitions creadas en Shopify Admin
- [ ] Template `blog-post.json` agregado al theme
- [ ] Secciones Liquid (`blog-hero.liquid`, etc.) en `sections/`
- [ ] CSS `blog-post.css` en `assets/`
- [ ] CSS linkeado en theme.liquid: `{{ 'blog-post.css' | asset_url | stylesheet_tag }}`
- [ ] Blog de prueba creado con metafields llenos
- [ ] Frontend: hero renderiza correctamente
- [ ] Frontend: schema JSON-LD en `<head>` (inspeccionar)
- [ ] Frontend: related articles funcionales
- [ ] Frontend: CTA button con tracking slug
- [ ] Frontend: sedes grid visible
- [ ] Google Rich Results Test: Article reconocido

---

**Última actualización:** 23 de junio de 2026  
**Responsable:** Claude Code  
**Próximo:** Ejecutar Fase 1 (setup theme) tras validación de Javier
