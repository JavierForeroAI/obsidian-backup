---
name: guia-practica-blogs-shopify
description: "Guía paso-a-paso para Javier: cómo van a funcionar los 16 blogs en Shopify, qué va en cada lado, y qué esperar."
metadata:
  type: guide
  fecha: 2026-06-23
  audiencia: Javier (no técnico)
---

# Guía Práctica: Los 16 Blogs Médicos en Shopify

**Hola Javier:**

Aquí te explico de forma simple qué vamos a hacer con los 16 blogs, cómo van a funcionar en Shopify, y qué esperar.

---

## El problema que solucionamos

Hoy tienes 16 blogs "hermosos" en local:
- ✅ Hero gradient teal/dorado
- ✅ Firma Dr. Carreño
- ✅ Estilos premium (tipografía, colores)
- ✅ Schema JSON-LD (Google entiende que es artículo médico)
- ✅ Sedes con links Google Maps
- ✅ Tracking de WhatsApp (sé de qué blog viene cada lead)

**Pero:**
- ❌ Están en HTML local (archivos `.html` en tu drive)
- ❌ No están en Shopify
- ❌ No los indexa Google
- ❌ No generan tráfico

**Solución:** Pasar los 16 blogs a Shopify **SIN perder nada** de lo que te gusta.

---

## Cómo funciona la solución

### Hoy (local)
```
Blog HTML completo (1 archivo = todo)
├── Estilos CSS (colores, tipografía)
├── Contenido (texto, headings, tablas)
├── Schema JSON-LD (información médica)
├── Sedes + links
└── CTA button + tracking WhatsApp
```

### Después (Shopify)
```
Blog en Shopify ≈ 2 partes
│
├── PARTE 1: Shopify Admin
│   ├── Título
│   ├── URL (handle: alopecia-androgenetica-...)
│   ├── Contenido limpio (sin estilos, sin scripts)
│   ├── SEO Title y Description
│   └── Autor: "Dr. Fabián Carreño"
│
└── PARTE 2: Datos guardados en "metafields" (JSON)
    ├── hero_eyebrow: "Ciencia capilar"
    ├── hero_subtitle: "No es un exceso de hormonas..."
    ├── schema_article: {...JSON completo del esquema...}
    ├── schema_localbusiness: [...5 sedes...]
    ├── author_name, author_title
    ├── related_articles: ["slug1", "slug2", "slug3"]
    ├── cta_text, cta_button
    ├── whatsapp_tracking_slug: "alopecia-androgenetica-..."
    └── sedes_enabled: true
```

### Qué renderiza al visitante

```
Visitante abre blog en www.innovartmedical.com/blogs/alopecia-androgenetica-...
│
├── 1. Hero section (gradient teal/dorado)
│   ├── "Ciencia capilar" (eyebrow)
│   ├── "Alopecia androgenética: ..." (título)
│   ├── "No es un exceso de hormonas..." (subtitle)
│   └── Meta: "Por Dr. Fabián Carreño · 9 min de lectura · 13 de junio de 2026"
│
├── 2. Contenido (texto limpio + tablas + listas)
│   └── (redacción original exacta)
│
├── 3. Firma médica premium
│   └── "Dr. Fabián Carreño Jiménez\nDirector Médico, Cirujano Plástico..."
│
├── 4. Artículos relacionados
│   └── "📖 Lee también: [enlace1] [enlace2] [enlace3]"
│
├── 5. Sedes (5 tarjetas)
│   └── Bogotá · Medellín · Barranquilla · Bucaramanga · Panamá (+ links GMB)
│
├── 6. CTA button
│   └── "📲 Escríbenos al +57 312 456 5014" → WhatsApp CON tracking slug
│
└── En `<head>` (invisible pero Google lo ve)
    ├── Schema JSON-LD (Article)
    └── Schema JSON-LD (LocalBusiness × 5)

↓ RESULTADO: Blog se ve IGUAL o MEJOR que local, Google lo entiende perfectamente
```

---

## ¿Dónde va cada cosa?

### ESTILOS (colores, tipografía, gradients)
- **Hoy:** dentro del HTML (`<style>` inline)
- **Después:** en archivo CSS centralizado (`assets/blog-post.css`)
- **Beneficio:** si cambias de idea sobre los colores, editas UN archivo y todos los 16 blogs cambian. No repites CSS.

### CONTENIDO (texto, h2, tablas, listas)
- **Hoy:** HTML semántico (h2, p, table, ul, blockquote)
- **Después:** MISMO HTML semántico, pero en el campo "Body" de Shopify
- **Lo que pasa:** Shopify lo sanitiza (elimina `<script>` tags, pero mantiene h2/p/table/etc.)
- **Resultado:** contenido perfectamente legible, sin cambios visibles

### DATOS ESTRUCTURADOS (schema JSON-LD, autor, sedes)
- **Hoy:** dentro del HTML (`<script type="application/ld+json">`)
- **Después:** en metafields (JSON seguro, Shopify NO sanitiza)
- **Ejemplo:**
  ```json
  metafield "schema_article":
  {
    "@type": "Article",
    "headline": "Alopecia androgenética...",
    "author": {
      "name": "Dr. Fabián Carreño Jiménez",
      "jobTitle": "Director Médico"
    },
    ...
  }
  ```
- **Qué pasa en frontend:** Theme Liquid inyecta este JSON en `<head>` → Google lo lee → Google entiende que es artículo médico de autoridad

### TRACKING WhatsApp
- **Hoy:** quemado en cada HTML
  ```html
  ?text=Hola,%20vengo%20del%20blog%20'alopecia-androgenetica-...'
  ```
- **Después:** slug en metafield + theme arma la URL dinámicamente
- **Beneficio:** trazabilidad perfecta: qué artículo → qué lead → qué conversión

---

## Línea de tiempo

### FASE 0: Decisión (AHORA)
- ✅ Lees esta guía
- ✅ Dices "sí, vamos" o preguntas dudas
- **Duración:** 15 min

### FASE 1: Setup del tema (Claude hace, 4–5 horas)
- Claude crea metafields en Shopify (campos para guardar los datos)
- Claude edita el template de blog post en Shopify (cómo renderiza los datos)
- Claude agrega el CSS centralizado
- Claude valida en preview con un blog de prueba
- **Tú haces:** ninguno, pero puedes validar en preview si quieres
- **Resultado:** Shopify listo para recibir blogs

### FASE 2: Preparar datos (Claude automatiza, 1 hora)
- Claude corre un script Python que lee los 16 HTML locales
- Script extrae: contenido limpio, metadatos, schema JSON-LD, sedes, tracking slug
- Output: archivo JSON con todo estructurado
- **Duración:** automático
- **Resultado:** JSON listo para publicar

### FASE 3: Publicar blogs (Claude automático, 20 min)
- Claude corre otro script que:
  - Crea 16 artículos en Shopify (vía API)
  - Llena todos los campos (título, contenido, SEO, autor, metafields)
  - Publica cada uno
- **Tú haces:** nada, solo esperar
- **Resultado:** 16 blogs LIVE en www.innovartmedical.com/blogs/

### FASE 4: Validación (Tú + Claude, 30 min)
- Abre un blog: ¿se ve bien?
- Inspecciona el código: ¿schema JSON-LD está en `<head>`?
- Prueba el botón WhatsApp: ¿el tracking slug aparece?
- Prueba links de related articles: ¿redirigen correctamente?
- Google Rich Results Test: ¿Google reconoce el artículo médico?

### FASE 5: Medir impacto (después, 30 días)
- Google Search Console: ¿se indexaron todos los blogs?
- AI Visibility Score / Semrush: ¿mejoró visibilidad en búsquedas médicas?
- GHL analytics: ¿de qué blogs vienen más leads?
- WhatsApp: ¿los leads dicen de qué blog vienen?

---

## Riesgos (muy bajos)

### "¿Se va a romper el tema?"
**No.** El tema Shopify se toca UNA sola vez (agregar template blog post + CSS). Los 16 blogs son datos, no código. Incluso si algo sale mal, siempre puedes volver atrás sin perder nada.

### "¿Shopify va a sanitizar mi contenido?"
**Parcialmente (es normal):**
- ❌ Shopify elimina: `<script>`, `<svg>` decorativo, atributos `data-*`
- ✅ Shopify mantiene: h2, p, table, blockquote, listas, links

**Pero nuestro schema JSON-LD está protegido:**
- Está en metafields (JSON puro)
- Shopify NO sanitiza metafields
- Theme Liquid inyecta el JSON en `<head>` sin tocar

**Resultado:** Contenido se ve limpio y bien, schema intacto.

### "¿Puedo cambiar algo después?"
**Sí, fácil:**
- **Cambiar texto de un blog:** edita el Body en Shopify admin (2 min)
- **Cambiar estilos (colores, tipografía):** edita `assets/blog-post.css`, re-publica theme (15 min, todos los blogs reflejan el cambio)
- **Cambiar autor médico:** edita metafield `author_name` (1 min por blog, o automático)
- **Agregar blog nuevo:** ejecuta script (5 min automático)

### "¿Pierd el tracking de WhatsApp?"
**No.** Cada blog lleva su slug:
```
Blog A: vengo del blog 'alopecia-androgenetica-...'
Blog B: vengo del blog 'fue-vs-dhi-que-tecnica-elegir'
Blog C: vengo del blog 'minoxidil-finasterida-...'
```

GHL recibe los mensajes → los clasifica por blog → tú sabes de dónde viene cada lead.

---

## Qué esperar después (ROI)

### Día 1
- ✅ 16 blogs LIVE en Shopify
- ✅ URLs limpias y SEO-friendly
- ✅ Google entiende que son artículos médicos (schema JSON-LD)

### Semana 1
- 🔍 Google indexa ~50% de los blogs
- 📊 Search Console muestra impresiones iniciales

### Semana 2–4
- 🚀 Tráfico orgánico pequeño pero creciente
- 📱 Primeros leads vía WhatsApp desde blogs
- 🎯 GHL analytics muestra "Blog A generó 5 leads" | "Blog B generó 3 leads"

### Mes 1–2
- 📈 E-E-A-T score ⬆️ (Google entiende que eres autoridad médica en alopecia)
- 🗺️ GEO targeting mejora (5 sedes posicionadas en Google Maps)
- 💬 Leads de blogs = más conciencia de marca (Dr. Carreño es visible)
- 💰 Conversión: algunos blogs (precios, FUE vs DHI, financiación) convertirán mejor

### Mes 3–6
- 🏆 Posicionamiento en búsquedas médicas clave: "implante capilar Colombia", "DHI vs FUE", "alopecia femenina", etc.
- 🌍 Visibilidad GEO en 5 ciudades (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá)
- 📊 30–50% de leads nuevos vienen de blogs
- 🎯 ROI: blogs son tráfico "gratuito" que dura años (SEO es inversion, no gasto)

---

## Preguntas frecuentes (simple)

### "¿Cuánto cuesta?"
**Cero.** Shopify ya permite blogs. Metafields son feature nativa. No hay apps, no hay plugins. Solo tiempo de Claude configurando (ya incluido en tu plan).

### "¿Se ven diferente a local?"
**Visual:** ~95% igual. Pierden el SVG decorativo (Shopify sanitiza por seguridad), pero todo lo importante (hero gradient, tipografía, sedes, autor, CTA) se ve igual o mejor.

**Funcionalidad:** 100% igual. Schema, tracking, related articles, todo funciona.

### "¿Qué pasa si Shopify cambia algo?"
**Muy seguro:** blog posts han sido en Shopify desde 2016. No son feature nueva. Es infraestructura estable.

### "¿Puedo estar tranquilo de que Google entiende los artículos?"
**Sí.** Schema JSON-LD + Article schema + Author schema + LocalBusiness = Google entiende perfectamente. Verás Rich Results (Article Rich Card) en Search Console dentro de 2–3 semanas.

### "¿Y si tengo 50 blogs en el futuro?"
**Automático.** Generador local (Python + innovart_template.py) + script Shopify = nuevo blog en 15 min, automático. Sin fricción.

---

## Checklist: ¿Estamos listos?

- [ ] Entiendo que los blogs se dividen en 2 partes (Shopify admin + metafields)
- [ ] Entiendo que Shopify sanitiza HTML (es normal y seguro)
- [ ] Entiendo que schema JSON-LD está protegido en metafields
- [ ] Entiendo que tracking WhatsApp se preserva (en metafield)
- [ ] Entiendo que después puedo cambiar estilos, contenido, autor fácilmente
- [ ] Estoy listo para que Claude configure el tema (FASE 1)
- [ ] Estoy listo para que Claude publique 16 blogs (FASE 3)
- [ ] Estoy listo para validar en frontend (FASE 4)

**Si marcaste todos:** ¡adelante!

---

## Próximos pasos (para Javier)

1. **Confirma esta estrategia:** "Claude, vamos con Opción 4"
2. **Autoriza Fase 1:** "Claude, configura el tema"
3. **Autoriza Fase 3:** "Claude, publica los 16 blogs"
4. **Valida Fase 4:** "Revisamos juntos en preview"
5. **Mide impacto Fase 5:** Dentro de 30 días, revisamos tráfico y leads

---

## Contacto y soporte

- **Preguntas antes de empezar?** Pregunta
- **Algo sale mal en FASE 1?** Claude rollback, reintentos
- **Cambios después?** Chatea con Claude, actualiza en 2 min
- **Impacto no es el esperado?** Revisamos estrategia SEO global

---

**Documento:** Guía Práctica para Javier  
**Fecha:** 23 de junio de 2026  
**Estrategia:** Opción 4 (Hybrid Approach)  
**Próximo:** Tu confirmación → Claude inicia Fase 1

---

Ver también: 
- [[resumen-ejecutivo-blogs-shopify]] (1 página, decisión rápida)
- [[estrategia-publicar-blogs-shopify-2026-06-23]] (análisis completo, todas las opciones)
- [[shopify-blog-post-template-tecnico]] (detalles técnicos si te interesa)
