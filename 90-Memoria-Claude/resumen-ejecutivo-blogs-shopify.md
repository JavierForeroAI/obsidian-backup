---
name: resumen-ejecutivo-blogs-shopify
description: "Resumen ejecutivo de 1 página: qué opción elegir, por qué, y paso-a-paso. Para Javier."
metadata:
  type: decision
  fecha: 2026-06-23
---

# Resumen Ejecutivo: 16 Blogs a Shopify

## La pregunta
¿Cómo pasar 16 blogs médicos (con hero gradient, firma Dr. Carreño, schema JSON-LD, sedes, tracking WhatsApp) a Shopify **sin romper nada ni sanitizar contenido**?

## La respuesta: OPCIÓN 4 — Hybrid Approach

### Qué es
- **Body del blog:** HTML limpio (h2/p/tablas/listas, SIN estilos ni scripts)
- **Estilos + Datos:** Guardados en metafields Shopify (JSON seguro)
- **Theme:** Renderiza metafields en blog template (Liquid condicionales)

### Por qué funciona
| Aspecto | Resultado |
|---------|-----------|
| ✅ Fidelidad visual | 95% (hero, gradients, sedes, autor premium) |
| ✅ Seguridad | 100% (tema toca UNA sola vez, datos son datos) |
| ✅ SEO | Excelente (schema JSON-LD, h-tags, related articles) |
| ✅ Escalabilidad | Perfecta (agregar blog 17/18/19 = automático) |
| ✅ Mantenibilidad | Alta (editar contenido = admin Shopify, no código) |
| ✅ Tiempo | 5–6h setup + 20 min para 16 blogs |

### Qué pasa con cada elemento

| Elemento | Dónde va | Cómo se renderiza |
|----------|----------|-------------------|
| **Hero gradient + eyebrow** | Metafield `hero_eyebrow` | Theme template (Liquid) |
| **Contenido semántico** (h2/p/listas/tablas) | Body del blog post | Shopify nativo |
| **Schema JSON-LD** (Article + LocalBusiness) | Metafield `schema_*` | `<script type="application/ld+json">` en `<head>` |
| **Firma Dr. Carreño** | Metafields `author_*` | Theme template (Liquid) |
| **Sedes + GMB links** | Metafield `sedes_locales` o centralizado | Theme template (grid Liquid) |
| **Related articles** | Metafield `related_articles` (array slugs) | Theme template (loop Liquid) |
| **Tracking WhatsApp** | Metafield `whatsapp_tracking_slug` | URL params en CTA button |
| **Estilos CSS** | Asset `blog-post.css` | `<link>` en theme.liquid |

### Plan de ejecución

#### Fase 1: Setup (una sola vez) — 4–5 horas
1. **Crear metafield definitions** en Shopify (via Admin o CLI)
   - `hero_eyebrow`, `hero_subtitle`, `schema_article`, `schema_localbusiness`, `related_articles`, `author_*`, `sedes_*`, `whatsapp_tracking_slug`, etc.

2. **Editar/Crear template `blog-post.json`** en el theme
   - Agregar Liquid que renderiza:
     - Hero (usa metafields)
     - Article body (Shopify nativo)
     - Author signature (usa metafields)
     - Schema JSON-LD inyectado (usa metafields)
     - Related articles (usa metafields)
     - Sedes grid (usa metafields o global)
     - CTA con tracking (usa metafields)

3. **Agregar CSS** (`assets/blog-post.css`)
   - Copiar estilos de innovart_template.py
   - Pegar en archivo nuevo
   - Linkear en theme

4. **Validar en preview** con un blog de prueba

#### Fase 2: Automatizar datos (1–2 horas)
- Python script `parse_blogs_for_shopify.py`: Lee 16 HTML locales → extrae contenido limpio + metafields → JSON
- Output: `blogs-shopify-data.json` (16 objetos con todo lo necesario)

#### Fase 3: Publicar (20 minutos automático)
- Python script `create_shopify_blogs.py`: Lee JSON → crea 16 artículos en Shopify via API Shopify Admin
- Cada artículo:
  - Title, handle, body (limpio)
  - SEO title/description
  - Author (Dr. Fabián Carreño)
  - Metafields (todos llenos)
  - Status: published

### Validación (checklist)
```
□ Blog post visible en Shopify admin
□ Body HTML no tiene <script> (Shopify sanitizó; ✅ es normal)
□ Metafields llenos en Shopify admin
□ Frontend: hero renderiza con eyebrow + subtitle
□ Frontend: schema JSON-LD en <head> (DevTools)
□ Frontend: related articles funcionan
□ Frontend: CTA button + slug tracking WhatsApp
□ Frontend: sedes grid visible (5 tarjetas + GMB links)
□ Google Rich Results Test: Article + LocalBusiness ✅
□ Slug tracking: mensaje WhatsApp incluye nombre del blog
```

### Después (mantenimiento futuro)

**Agregar blog nuevo:**
1. Generar HTML local
2. Ejecutar parse script
3. Ejecutar create script
4. ✅ Listo

**Cambiar estilos/color/tipografía:**
1. Editar `blog-post.css`
2. Re-publish theme
3. Todos los blogs reflejan el cambio (DRY)

**Cambiar autor médico:**
1. Editar metafield `author_name` en todas las páginas (o centralizado si es global)

---

## Comparación rápida (3 opciones descartadas)

| Opción | Ventaja | Desventaja | Veredicto |
|--------|---------|-----------|----------|
| **Opción 1: Solo metafields** | Simplicidad | 60% visual (sin hero/gradients) | ❌ Básica |
| **Opción 2: CSS en metafield** | Fidelidad visual 95% | Mantenimiento alto, CSS duplicado | ❌ Pesada |
| **Opción 3: GemPages** | Visual editor | NO es blog nativo, confunde UX | ❌ Confusa |
| **Opción 4: Hybrid** ⭐ | TODO: visual + seguridad + escalable | Setup más inicial | ✅ **GANADORA** |

---

## Preguntas frecuentes

**¿Se va a romper algo?**
No. El tema se toca UNA sola vez (agregar template blog-post.json + CSS). Los datos están en metafields (Shopify los preserva 100%). Cero riesgo de ruptura.

**¿Shopify va a sanitizar el schema JSON-LD?**
No. Los metafields son datos puros; Shopify no sanitiza. El JSON-LD se inyecta en `<head>` via Liquid `<script type="application/ld+json">` (seguro).

**¿Cuánto tiempo toma agregar blog 17?**
~5 minutos (si es automático via script). Manual = 10 min.

**¿Dónde aparecen los blogs en Shopify?**
En `Online Store > Blog posts > Artículos Médicos`. Son blog posts nativos (no páginas GemPages).

**¿Google va a indexarlos?**
Sí. Blog posts nativos de Shopify son indexables. Schema JSON-LD está en `<head>` → Google entiende Article + LocalBusiness + Author.

**¿Y si cambio de idea sobre los estilos?**
Editas `blog-post.css` (1 archivo) y re-publicas el theme. Todos los 16 blogs + futuros reflejan el cambio automáticamente (DRY).

---

## Siguientes pasos (para Javier)

1. **Validar la estrategia** ← (tú aquí, ahora)
   - ¿Te parece bien la Opción 4?
   - ¿Hay algo que quieras cambiar?

2. **Autorizar Fase 1** (setup theme)
   - Claude hace metafield definitions + template blog-post.json + CSS
   - ~4–5 horas

3. **Autorizar Fase 2–3** (datos + publicar)
   - Claude genera Python scripts
   - Ejecuta scripts automático
   - 20 minutos

4. **Validar en frontend** (tú + Claude)
   - Verificar que se ve bien
   - Medir impacto SEO en 30 días

---

## Riesgos mitigados

| Riesgo | Mitigation |
|--------|-----------|
| Shopify sanitiza HTML | ✅ Body está limpio (sin `<script>`, sin SVG); metafields son seguros |
| Ruptura del tema | ✅ Toca template UNA sola vez; metafields son datos, no código |
| Sanitización de schema | ✅ Schema está en metafield (JSON seguro); Shopify NO sanitiza |
| Pérdida de tracking | ✅ Slug de tracking está en metafield; CTA rearma URL con slug |
| Duplication de CSS | ✅ CSS centralizado en `assets/blog-post.css`; todos los blogs comparten |

---

**Documento:** Resumen Ejecutivo — Blogs a Shopify  
**Fecha:** 23 de junio de 2026  
**Decisión:** Opción 4 (Hybrid Approach)  
**Próximo checkpoint:** Validación con Javier + autorización para Fase 1

Ver también: [[estrategia-publicar-blogs-shopify-2026-06-23]] (análisis completo)
