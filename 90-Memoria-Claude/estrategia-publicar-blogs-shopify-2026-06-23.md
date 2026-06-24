---
name: estrategia-publicar-blogs-shopify
description: "Análisis estratégico completo: 4 opciones de arquitectura para publicar 16 blogs médicos en Shopify, comparadas por mantenibilidad, SEO, escalabilidad y riesgo de daño al tema."
metadata:
  type: strategy
  fecha: 2026-06-23
  estado: ready-to-execute
  autor: Claude Code
---

# Estrategia: Publicar 16 Blogs Médicos en Shopify
**Fecha:** 23 junio 2026  
**Estado:** Análisis completado — 4 opciones evaluadas  
**Contexto:** Los 16 blogs están listos (Drive: `Blogs/` y `Blogs Clean para Shopify/`), con firma médica, schema JSON-LD y tracking WhatsApp. Necesitan migrar a Shopify sin romper el tema Nativo ni sanitizar contenido.

---

## El desafío central

**Qué traemos de generación local:**
- HTML completo (doctype, estilos CSS inline, SVG decorativo, schema JSON-LD en `<head>`)
- Topbar + hero gradient + contenido semántico (h2/h3, listas, tablas)
- CTA buttons con WhatsApp tracking
- Firma médica (Dr. Carreño) con estilos `.author-sig`
- Related articles (links internos)
- Sedes (5) con GMB links
- Schema JSON-LD (Article + 5 LocalBusiness)

**Qué permite Shopify:**
- ✅ Blog posts con body HTML (pase a través del sanitizador)
- ✅ Metafields (almacenar datos estructurados)
- ✅ Metaobjects (esquemas reutilizables)
- ✅ Theme scripts/liquid (inyectar en `<head>`)
- ⚠️ Sanitización: Shopify **elimina**:
  - `<script>` tags (incluso `type="application/ld+json"`)
  - Estilos inline (excepto los permitidos por Shopify)
  - SVG decorativo (potencial XSS)
  - Data attributes no estándares

---

## OPCIÓN 1: Body Content Simple + Metafields + Theme Script

**Concepto:** Copiar solo el contenido HTML semántico (h2, p, listas, tablas) al campo "Body" del blog post. Metafields para schema y autor. Theme script inyecta JSON-LD en `<head>`.

### Flujo de publicación:

1. **Limpiar HTML** (vía Python/regex):
   - Extraer solo `.article .container` (contenido de artículo)
   - Remover `<style>` y SVG decorativo
   - Mantener h2/h3/p/ul/ol/table/blockquote/details
   - Convertir links `href="/senales-tempranas..."` → `href="/blogs/senales-tempranas-perdida-de-pelo"` (slugs Shopify)

2. **Crear post en Shopify:**
   - **Title:** "Alopecia androgenética: por qué se cae el pelo"
   - **URL handle:** `alopecia-androgenetica-por-que-se-cae-el-pelo`
   - **Body:** contenido limpio (HTML semántico)
   - **SEO Title:** `{meta title}`
   - **SEO Description:** `{meta description}`
   - **Author:** "Dr. Fabián Carreño Jiménez"
   - **Excerpt:** el `deck` del hero (resumen de 160 caracteres)

3. **Metafields (custom):**
   - `custom.schema_article` (JSON-LD Article)
   - `custom.schema_localbus` (JSON-LD LocalBusiness × 5)
   - `custom.related_articles` (slugs de artículos relacionados)
   - `custom.whatsapp_tracking_slug` (para analytics)

4. **Theme: Inyectar JSON-LD:**
   - Crear sección `blog-post.json` con Liquid que:
     - Lee metafields `custom.schema_*`
     - Inyecta `<script type="application/ld+json">` en `<head>`
     - Renderiza related articles + sedes dinámicamente

### Ventajas:
✅ **Contenido semántico limpio** — no HTML roto  
✅ **Schema JSON-LD preservado** — Google entiende autoridad  
✅ **Tema seguro** — no toca archivos vivos del theme  
✅ **Escalable** — agregar blogs nuevos es copiar-pegar + metafields  
✅ **SEO máximo** — estructura clara, h-tags correctos, Rich Results  
✅ **Tracking WhatsApp funcional** — cada post lleva su slug  

### Desventajas:
❌ **Requiere metafields custom** — Javier/desarrollador configura una sola vez  
❌ **Sin hero gradient/SVG** — blog usa estilos por defecto de Shopify (o tema personalizado)  
❌ **Related articles manuales** — hay que completar metafield al crear post  
❌ **Autor en metafield** — no sale en UI nativa de Shopify (se agrega con Liquid)  

### Riesgo: **BAJO**
No toca tema. Shopify sanitiza natural, pero JSON-LD se preserva via metafields.

### Esfuerzo:
- **Setup theme (una sola vez):** 3–4 horas (crear template blog post + scripts Liquid)
- **Por cada blog:** 10–15 min (copiar contenido limpio, llenar metafields, publicar)
- **Total 16 blogs:** ~3 horas (si Javier/desenvolvedor lo hace manual) o **15 min** (con API)

---

## OPCIÓN 2: HTML Completo en Body + CSS en Metafield + Tema Personalizado

**Concepto:** Pasar TODO el HTML al body (incluyendo estilos inline reescalados en metafield). El tema aplica CSS desde metafield en un `<style>` en `<head>`.

### Flujo:

1. **Extraer CSS al metafield:**
   - Tomar `<style>` del blog HTML → metafield `custom.css_article`
   - Convertir a Shopify-safe (sin `@import`, solo URLs `https://`)

2. **Pasar HTML completo al body:**
   - Mantener `.container`, `.article`, `.toc`, `.takeaways`, `.cta`, `.sedes-section`
   - Remover `<script>` tags (Shopify lo sanitiza igual)
   - Remover `<svg class="hsvg">` (Shopify lo rechaza)

3. **Theme inyecta CSS + schema:**
   - Template blog post: `{% if article.metafields.custom.css_article %}<style>{{ article.metafields.custom.css_article }}</style>{% endif %}`
   - Schema JSON-LD en metafield `custom.schema_article` → `<script type="application/ld+json">`

### Ventajas:
✅ **Máximo fidelidad visual** — el blog se ve exacto a local  
✅ **Hero gradient, autor premium, sedes cards** — TODO funciona  
✅ **Contenido semántico** — h-tags, tables, listas  

### Desventajas:
❌ **CSS en metafield es mantenimiento alto** — si cambias estilos en 16 blogs, hay que actualizar 16 metafields  
❌ **Duplication de CSS** — cada blog lleva copia del mismo CSS  
❌ **Shopify Sanitization riesgo mayor** — más HTML = más probabilidad de que rechace algo  
❌ **Rendimiento** — 16 blogs × CSS duplicado = peso HTML mucho más pesado  

### Riesgo: **MEDIO**
CSS inline puede ser rechazado parcialmente. SVG decorativo será eliminado. Posible caída en velocidad de página.

### Esfuerzo:
- **Setup:** 2–3 horas
- **Por blog:** 15–20 min
- **Total:** ~4–5 horas

---

## OPCIÓN 3: GemPages/PageFly + Markdown → HTML híbrido

**Concepto:** Usar GemPages (ya está activo en Shopify) para armar cada blog como una página de builder, pegar contenido limpio + componentes visuales.

### Flujo:

1. En GemPages editor:
   - Crear página nueva
   - Agregar componentes: Hero section, Body text, Related articles, CTA, Sedes grid
   - Pegar contenido limpio (sin HTML, solo texto + headings)
   - Configurar estilos desde editor GemPages (no toca theme vivo)

2. Schema JSON-LD:
   - Metafield nativo de la página
   - Inyectar vía theme script

### Ventajas:
✅ **No toca código del theme** — 100% seguro  
✅ **UI visual familiarizado** — Javier ya usa GemPages  
✅ **Edición visual posterior fácil** — cambiar contenido = editor, no código  
✅ **Escalable** — clonar página existente, cambiar contenido  

### Desventajas:
❌ **Manualmente repetitivo** — "agregar componente Hero, agregar Body, agregar CTA" × 16  
❌ **NO es un blog post nativo** — es una página + metaobject, no aparece en "blog"  
❌ **SEO ligeramente peor** — Google prefiere `<article>` tags; una página GemPages puede no tener  
❌ **Mezcla de espacios** — blogs son blog posts, estos serían páginas → confusión UX  

### Riesgo: **BAJO**
Pero confunde estructura de Shopify (blogs vs páginas).

### Esfuerzo:
- **Por blog:** 20–30 min (agregar componentes manualmente)
- **Total:** ~5–8 horas

---

## OPCIÓN 4: Hybrid Approach — Recomendada ⭐

**Concepto:** Combinar Opción 1 (metafields + theme) + Opción 2 (visual mejorado).

- **Body del blog post:** HTML semántico limpio (h2/p/tables/listas)
- **Metafields:**
  - `custom.hero_eyebrow` → "Ciencia capilar"
  - `custom.hero_subtitle` → el deck del artículo
  - `custom.featured_image` → imagen del artículo (si la hay)
  - `custom.schema_article` → JSON-LD completo
  - `custom.schema_localbusiness` → 5 sedes
  - `custom.related_articles` → slugs relacionados
  - `custom.author_name`, `custom.author_title`, `custom.author_bio`
  - `custom.cta_text`, `custom.cta_button_text`
  - `custom.sedes_enabled` → boolean (mostrar sedes si/no)

- **Theme blog-post template:**
  ```liquid
  {% if article.metafields.custom.hero_eyebrow %}
    <section class="hero-blog">
      <div class="eyebrow">{{ article.metafields.custom.hero_eyebrow }}</div>
      <h1>{{ article.title }}</h1>
      <p class="deck">{{ article.metafields.custom.hero_subtitle }}</p>
      <div class="meta">
        <span>Por <b>{{ article.metafields.custom.author_name }}</b></span>
        <span>{{ article.reading_time }} min</span>
        <span>{{ article.published_at | date: "%d de %B de %Y" }}</span>
      </div>
    </section>
  {% endif %}

  <main class="article">
    {{ article.content }}
  </main>

  {% if article.metafields.custom.author_name %}
    <div class="author-sig">
      <div class="sig-title">{{ article.metafields.custom.author_name }}</div>
      <div class="sig-role">{{ article.metafields.custom.author_title }}</div>
    </div>
  {% endif %}

  {% if article.metafields.custom.schema_article %}
    <script type="application/ld+json">
      {{ article.metafields.custom.schema_article }}
    </script>
  {% endif %}

  {% if article.metafields.custom.schema_localbusiness %}
    <script type="application/ld+json">
      {{ article.metafields.custom.schema_localbusiness }}
    </script>
  {% endif %}

  {% if article.metafields.custom.sedes_enabled %}
    <section class="sedes-section">
      {# renderizar sedes #}
    </section>
  {% endif %}

  {% if article.metafields.custom.related_articles %}
    <div class="related-articles">
      {# loop through related_articles #}
    </div>
  {% endif %}
  ```

### Flujo de publicación:

1. **Limpiar HTML** (mismo que Opción 1)
2. **Pegar en Body:** contenido semántico limpio
3. **Llenar metafields:**
   - eyebrow, hero_subtitle, author_name, author_title
   - schema_article (JSON stringificado)
   - schema_localbusiness (JSON stringificado)
   - related_articles (array de slugs)
   - sedes_enabled (true)

4. **Publicar:**
   - SEO Title, Description, Author (nativo Shopify)
   - Estado: Publicado
   - Tag: "Ciencia capilar" (si aplica)

### Ventajas:
✅ **Máxima fidelidad visual + máxima seguridad**  
✅ **Tema NO modificado en vivo** — todo en metafields  
✅ **Escalable y mantenible** — agregar blogs nuevos = llenar formulario  
✅ **SEO óptimo** — schema JSON-LD, h-tags, related articles, author  
✅ **Analytics** — cada post lleva su slug de tracking WhatsApp  
✅ **Sin sanitización agresiva** — body es HTML limpio, scripts en metafield  
✅ **Edición posterior fácil** — editar body o metafields sin tocar tema  

### Desventajas:
❌ **Setup theme más complejo** — 1 template blog-post con Liquid múltiple  
❌ **Metafields son "textos largos"** — no hay UI nativa para llenar JSON en Shopify admin  
  → **Solución:** usar CLI Shopify o MCP GraphQL para llenar metafields, o crear Custom App  

### Riesgo: **MUY BAJO**
- Tema se toca UNA sola vez en setup
- Metafields son datos, Shopify los preserva 100%
- Schema JSON-LD inyectado via metafield = seguro

### Esfuerzo:
- **Setup theme (una sola vez):** 4–5 horas (crear template, Liquid condicionales, CSS del blog)
- **Generar metafields (automático vía Python + MCP):** 15 min
- **Por cada blog (si manual):** 5–10 min (llenar en Shopify admin)
- **Total 16 blogs (automático):** ~20 min via Python + Shopify API

---

## Comparativa de opciones

| Aspecto | Opción 1 | Opción 2 | Opción 3 | Opción 4 ⭐ |
|---|---|---|---|---|
| **Fidelidad visual** | 60% | 95% | 85% | 95% |
| **Riesgo de ruptura** | Bajo | Medio | Bajo | Muy bajo |
| **Escalabilidad** | Alta | Media | Baja | Muy alta |
| **SEO (schema)** | Excelente | Excelente | Bueno | Excelente |
| **Mantenibilidad** | Alta | Baja | Media | Alta |
| **Setup theme** | 3–4h | 2–3h | 0h | 4–5h |
| **Por blog (manual)** | 10–15m | 15–20m | 20–30m | 5–10m |
| **Total 16 blogs** | 3.5h | 4–5h | 5–8h | 2–3h (automático) |
| **Adecuada para médico?** | ✅ | ✅ | ⚠️ | ✅✅ |

---

## Recomendación: OPCIÓN 4 (Hybrid)

**Por qué:**
1. **Máxima fidelidad visual** (hero, gradients, sedes, related articles, autor premium)
2. **Máxima seguridad** (tema toca UNA sola vez, metafields son datos puros)
3. **SEO óptimo** (blog post nativo + schema JSON-LD)
4. **Escalabilidad real** (agregar blog 17, 18, 19 es automático)
5. **Mantenible** (editar contenido posterior = editor de Shopify o CLI, no código)
6. **Analytics limpio** (cada post lleva slug para WhatsApp tracking)

---

## Plan de ejecución (Opción 4)

### Fase 1: Setup Theme (una sola vez) — 4–5 horas

**1.1 Crear metafield definitions** (vía Shopify Admin o CLI):
```
Namespace: custom
Campos:
  - hero_eyebrow (single_line_text_field, visible=true)
  - hero_subtitle (rich_text_field, visible=true)
  - featured_image (file_reference, visible=true)
  - schema_article (json_field, visible=false)
  - schema_localbusiness (json_field, visible=false)
  - related_articles (json_field, visible=true)
  - author_name (single_line_text_field, visible=true)
  - author_title (single_line_text_field, visible=true)
  - author_bio (rich_text_field, visible=true)
  - cta_text (rich_text_field, visible=true)
  - cta_button_text (single_line_text_field, visible=true)
  - cta_link (url_field, visible=true)
  - whatsapp_tracking_slug (single_line_text_field, visible=false)
  - sedes_enabled (boolean, visible=true)
```

**1.2 Crear template `blog-post.json` (o editar existente):**
- Agregar secciones:
  - Hero (usa metafields: hero_eyebrow, hero_subtitle, featured_image)
  - Article body (usa `{{ article.content }}`)
  - Author signature (usa metafields: author_name, author_title)
  - Schema JSON-LD inyectado (usa metafields: schema_article, schema_localbusiness)
  - Related articles (usa metafields: related_articles)
  - CTA (usa metafields: cta_text, cta_button_text, cta_link)
  - Sedes (condicional via metafield: sedes_enabled)

**1.3 Agregar CSS:**
- Copiar de innovart_template.py (clases: `.hero`, `.article`, `.author-sig`, `.related-articles`, `.sedes-grid`, `.cta`, etc.)
- Pegar en `assets/blog-post.css` (nuevo archivo)
- Linkear en theme.liquid o en el template blog-post.json

**1.4 Validar en preview:**
- Crear un blog de prueba con metafields llenos
- Verificar que el hero renderiza, el schema JSON aparece en `<head>`, related articles funcionan

### Fase 2: Preparar datos (Python script) — 1–2 horas

**Entrada:** 16 archivos HTML de la carpeta `/tmp/innovart-blogs/html/`

**Salida:** JSON con 16 objetos, uno por blog:
```json
{
  "slug": "alopecia-androgenetica-por-que-se-cae-el-pelo",
  "title": "Alopecia androgenética: por qué se cae el pelo (y qué la acelera)",
  "description": "Qué es la alopecia androgenética...",
  "keywords": "alopecia androgenética, DHT, ...",
  "hero_eyebrow": "Ciencia capilar",
  "hero_subtitle": "No es un exceso de hormonas...",
  "body_html": "<p>La alopecia androgenética...</p>...",
  "author_name": "Dr. Fabián Carreño Jiménez",
  "author_title": "Director Médico...",
  "schema_article": { @type: "Article", ... },
  "schema_localbusiness": [ {...}, {...}, {...} ],
  "related_articles": ["senales-tempranas-perdida-de-pelo", "minoxidil-finasterida-como-funcionan-mitos"],
  "whatsapp_tracking_slug": "alopecia-androgenetica-por-que-se-cae-el-pelo",
  "sedes_enabled": true
}
```

**Script:** `parse_blogs_for_shopify.py` (30–50 líneas)

### Fase 3: Crear/Publicar blogs en Shopify (automático) — 20 min

**Opción A (recomendada — automático vía API):**
```bash
python3 create_shopify_blogs.py \
  --input blogs-shopify-data.json \
  --blog-id BLOG_ID \
  --token SHOPIFY_ADMIN_TOKEN
```

Esto:
- Crea 16 artículos
- Llena metafields via GraphQL mutation
- Publica con status "published"
- Configura SEO (title_tag, description_tag)

**Opción B (manual, si prefieres):**
- Para cada blog, llenar en Shopify Admin:
  - Title, handle, body (copiar-pegar HTML limpio)
  - SEO Title, Description
  - Author: "Dr. Fabián Carreño Jiménez"
  - Metafields (formularios)
  - Publicar

---

## Schema JSON-LD — Cómo va en metafield

El schema actual está en `<head>` como:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  ...
}
</script>
```

**En Shopify (metafield `custom.schema_article`):**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Alopecia androgenética: por qué se cae el pelo (y qué la acelera)",
  "description": "No es un exceso de hormonas...",
  "image": "https://innovartmedical.com/logo.png",
  "datePublished": "2026-06-13",
  "dateModified": "2026-06-13",
  "author": {
    "@type": "Person",
    "name": "Dr. Fabián Carreño Jiménez",
    "jobTitle": "Director Médico, Cirujano Plástico y Reconstructivo",
    "affiliation": {
      "@type": "Organization",
      "name": "Innovart Medical IPS"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "Innovart Medical IPS",
    "url": "https://innovartmedical.com"
  }
}
```

**En template Liquid:**
```liquid
{% if article.metafields.custom.schema_article %}
  <script type="application/ld+json">
    {{ article.metafields.custom.schema_article }}
  </script>
{% endif %}
```

Shopify **preserva** metafields 100% (no sanitiza JSON).

---

## WhatsApp Tracking — Cómo va

Cada blog lleva un slug de tracking. En el HTML actual está quemado:
```html
<a class="btn" href="https://wa.me/573124565014?text=Hola,%20vengo%20del%20blog%20'alopecia-androgenetica-por-que-se-cae-el-pelo'%20...">📲 Escríbenos</a>
```

**En Shopify (metafield `custom.whatsapp_tracking_slug`):**
```
alopecia-androgenetica-por-que-se-cae-el-pelo
```

**En template Liquid (CTA button):**
```liquid
{% if article.metafields.custom.cta_link %}
  <a href="{{ article.metafields.custom.cta_link }}?text=Hola,%20vengo%20del%20blog%20'{{ article.metafields.custom.whatsapp_tracking_slug }}'%20..." class="btn">
    📲 Escríbenos al +57 312 456 5014
  </a>
{% endif %}
```

Cada mensaje incluirá el slug del artículo → trazabilidad en GHL + análisis de qué blog convierte.

---

## Sedes (GEO) — Cómo va

Actualmente hay un HTML repetido con 5 tarjetas. En Shopify:

**Opción A (estática en metafield):**
```json
{
  "custom.sedes_locales": [
    {
      "city": "Bogotá",
      "address": "Calle 116 #9-72",
      "gmb_link": "https://share.google/unA0jM58IDgsldKhl"
    },
    ...
  ]
}
```

**En template Liquid:**
```liquid
{% if article.metafields.custom.sedes_enabled %}
  <section class="sedes-section">
    <h3>Nuestras sedes</h3>
    <div class="sedes-grid">
      {% for sede in article.metafields.custom.sedes_locales.value %}
        <div class="sede-card">
          <h4>{{ sede.city }}</h4>
          <p class="addr">{{ sede.address }}</p>
          <a href="{{ sede.gmb_link }}" target="_blank" class="sede-link">📍 Ver en Maps</a>
        </div>
      {% endfor %}
    </div>
  </section>
{% endif %}
```

**Opción B (centralizada):**
Guardar sedes una sola vez en theme settings o en un metaobject global, que todos los blogs referencian (menos repetición de datos).

---

## Impacto en SEO/GEO

✅ **E-E-A-T:**
- Author schema JSON-LD (Dr. Carreño con jobTitle + affiliation)
- Article schema con datePublished, dateModified
- 5 LocalBusiness schema (mejor Google Maps + searches locales)
- Contenido semántico (h-tags, listas, tablas)

✅ **Indexación:**
- Blog posts nativos de Shopify = indexables por Google
- URL handle limpio (alopecia-androgenetica-por-que-se-cae-el-pelo)
- Sitemaps auto-incluye blog posts

✅ **Rich Results:**
- Article Rich Card
- FAQ Rich Card (si los detalles son FAQ schema)
- LocalBusiness Rich Results (sedes con ubicación, teléfono, etc.)

✅ **GEO targeting:**
- Related articles (internal links, relevancia temática)
- Sedes con GMB links (señal local a Google)
- Schema LocalBusiness (5 ciudades)

---

## Próximos pasos — Ruta de ejecución

**Semana 1 (ahora):**
- [ ] Validar con Javier la Opción 4
- [ ] Crear metafield definitions en Shopify (Javier vía Admin o Claude vía MCP)
- [ ] Escribir template blog-post.json mejorado

**Semana 2:**
- [ ] Validar template en preview (blog de prueba)
- [ ] Generar JSON de los 16 blogs (Python script)
- [ ] Crear Python script para publicar via API

**Semana 3:**
- [ ] Ejecutar script: crear 16 blogs
- [ ] Verificar en Shopify admin que metafields están llenos
- [ ] Verificar en frontend: hero renderiza, schema en `<head>`, related articles funcionan
- [ ] Validar SEO con Google Rich Results Test

**Semana 4:**
- [ ] Enviar sitemap a Google Search Console
- [ ] Medir impacto: AI Visibility Score, sesiones, CTR en 30 días

---

## Archivos generados / a generar

| Archivo | Tipo | Loc | Responsable |
|---|---|---|---|
| `blog-post-template.json` | Theme template | Shopify theme | Claude/Dev |
| `blog-post.css` | CSS | assets/ | Claude (copiar de innovart_template.py) |
| `parse_blogs_for_shopify.py` | Script | `/tmp/` | Claude |
| `blogs-shopify-data.json` | Data | `/tmp/` | Claude (output de parse script) |
| `create_shopify_blogs.py` | API script | `/tmp/` | Claude |
| `metafield-definitions.json` | Config | docs | Claude |
| Artículos Shopify (16) | Blog posts | Shopify | API/manual |

---

## Validación final (checklist)

- [ ] Blog post se ve en Shopify admin
- [ ] Body HTML no tiene `<script>` (Shopify sanitizó)
- [ ] Metafields están llenos (ver en Shopify admin > Metafields)
- [ ] Frontend: hero renderiza con eyebrow + subtitle + author meta
- [ ] Frontend: schema JSON-LD en `<head>` (inspeccionar Developer Tools)
- [ ] Frontend: related articles renderizados (links funcionales)
- [ ] Frontend: CTA button con slug de tracking WhatsApp
- [ ] Frontend: sedes grid visible con 5 tarjetas + GMB links
- [ ] Google Rich Results Test: Article + LocalBusiness reconocidos
- [ ] Slug tracking: WhatsApp mensaje incluye nombre del blog

---

## Documentación de mantenimiento (para después)

**Agregar un blog nuevo en el futuro:**

1. Generar HTML local (innovart_template.py + batch.py)
2. Ejecutar `parse_blogs_for_shopify.py` sobre el HTML nuevo
3. Ejecutar `create_shopify_blogs.py` (1 blog)
4. ✅ Listo

**Cambiar estilos del blog (color, tipografía, spacing):**

1. Editar `blog-post.css`
2. Re-publish el theme
3. Todos los 16 blogs + futuros reflejan el cambio (DRY)

**Cambiar autor médico:**

1. Editar metafield `custom.author_name` y `custom.author_title` en todas las páginas
2. O si es global: cambiar en theme settings

---

## Conclusión

La **Opción 4 (Hybrid)** es la más segura, escalable y mantenible:
- ✅ Sin riesgo de romper tema
- ✅ Schema JSON-LD preservado 100%
- ✅ Visual fidelidad 95%+
- ✅ Escalable a 16+ blogs sin fricción
- ✅ Analytics limpio (tracking slug)
- ✅ SEO óptimo para GEO (E-E-A-T, LocalBusiness, Rich Results)

**Tiempo total:** ~5–6 horas de setup + 20 min automático para publicar 16 blogs.

**Responsables:**
- Claude: Metafield definitions, template Liquid, Python scripts
- Javier (o dev): Validar tema en preview, ejecutar scripts, medir impacto

---

**Última actualización:** 23 de junio de 2026  
**Próximo checkpoint:** Validación con Javier + autorización para fase 1 (setup)  
**Relacionado:** [[fase-2-upgrade-blogs-contenido-2026-06-22]] · [[shopify-playbook-capacidades-mcp]] · [[shopify-ecosistema-mcp]]
