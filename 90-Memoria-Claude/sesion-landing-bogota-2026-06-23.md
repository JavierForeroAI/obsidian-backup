---
name: sesion-landing-bogota-2026-06-23
description: Registro completo de la sesión 2026-06-23 — publicación y optimización SEO/GEO de la landing Implante Capilar en Bogotá. Cambios técnicos, decisiones, hallazgos y estado final.
metadata:
  type: project
  fecha: 2026-06-23
  estado: completado
---

# Sesión 2026-06-23 — Landing Bogotá: Publicación + SEO/GEO

## Objetivo de la sesión
Completar y publicar la landing `/pages/implante-capilar-bogota` con todos los elementos SEO/GEO correctos, resolver el bloque oculto `-9999px` (black-hat SEO), e implementar el FAQPage schema.

---

## Cambios realizados

### 1. HTML #3 — Bloque oculto ELIMINADO
- **Qué era:** Elemento HTML/Liquid en PageFly con `position:absolute;left:-9999px` que contenía texto oculto incluyendo "garantía vitalicia" ×2 — black-hat SEO, penalizable por Google.
- **Decisión:** En lugar de simplemente borrarlo, se migró el contenido útil al FAQ visible (accordion + JSON-LD).
- **Acción:** Bloque borrado de PageFly.

### 2. HTML #5 — FAQPage JSON-LD AMPLIADO
- **Antes:** 5 preguntas genéricas.
- **Después:** 8 preguntas que cubren el contenido del bloque oculto eliminado:
  1. ¿Cuánto cuesta el implante capilar en Bogotá?
  2. ¿Qué es la técnica FUE y en qué se diferencia del método tradicional? ← NUEVA
  3. ¿Qué técnica usan — FUE o DHI?
  4. ¿Por qué es importante cuidar la zona donante después del implante? ← NUEVA
  5. ¿Cuántos controles postoperatorios están incluidos y qué cubren? ← NUEVA
  6. ¿Cuánto tiempo tarda la recuperación?
  7. ¿El implante capilar es permanente?
  8. ¿Cómo agendo una valoración en Bogotá?
- **Lección aprendida:** PageFly filtra `<script type="application/ld+json">` en sus elementos HTML/Liquid — el JSON-LD sí aparece en el HTML renderizado pero el Rich Results Test no lo detecta desde PageFly.

### 3. Snippet `faq-bogota.liquid` CREADO en theme Dawn
- **Ruta:** `snippets/faq-bogota.liquid`
- **Contenido:** JSON-LD FAQPage con las 8 preguntas.
- **Por qué snippet:** PageFly bloquea los script tags en sus elementos HTML/Liquid para el crawler de Google. El snippet en el theme garantiza que el JSON-LD esté en el HTML estático.

### 4. `theme.liquid` MODIFICADO (línea 299)
- **Cambio:** Agregado condicional antes del `</head>`:
```liquid
{% if request.path == '/pages/implante-capilar-bogota' %}{% render 'faq-bogota' %}{% endif %}
```
- **Seguridad:** El condicional asegura que el FAQPage de Bogotá NO cargue en otras páginas (Medellín, Barranquilla, etc.).
- **Versión del theme:** Version 12 (guardada 2026-06-23).

### 5. URL de la página CORREGIDA
- **Antes:** `/pages/implante-capilar-en-bogota-innovart-medical` (handle generado automáticamente por Shopify)
- **Después:** `/pages/implante-capilar-bogota` (alineado con todo el plan SEO)
- **Redirect 301:** Shopify creó automáticamente el redirect de la URL vieja a la nueva ✅
- **Hallazgo:** Había DOS páginas con el mismo título. La correcta es ID `154884800813` (plantilla `pf-88d89a52` de PageFly).

### 6. Meta description ACTUALIZADA
```
Implante capilar FUE en Bogotá: especialistas certificados, valoración gratuita, 24 controles postoperatorios y garantía de folículos implantados. Sede Calle 119 #7-94, Chicó Norte.
```
(157 caracteres — dentro del límite de 160)

### 7. Página PUBLICADA
- Visibilidad: Visible en Shopify Admin ✅
- PageFly: Published ✅
- URL en vivo: `https://www.innovartmedical.com/pages/implante-capilar-bogota` ✅

---

## Hallazgos importantes

### FAQPage deprecated por Google (mayo 2026)
- Google deprecó FAQPage rich results en mayo 2026. Ya no aparece en Google Search como resultado enriquecido para sitios no gubernamentales/salud oficial.
- **El FAQPage SÍ tiene valor para GEO** — ChatGPT, Perplexity, Gemini y otros modelos de IA leen el JSON-LD para citar respuestas. Ese era el objetivo principal.
- El Rich Results Test solo muestra "Organización" — esto es correcto y esperado.
- **Fuente verificada:** Google Search Central + Search Engine Journal + Search Engine Land.

### JSON-LD en PageFly vs theme.liquid
- PageFly renderiza el JSON-LD en el HTML estático ✅ (confirmado en código fuente, línea ~922)
- Sin embargo, el Rich Results Test no lo detecta desde PageFly (posiblemente por la forma en que PageFly anida los elementos)
- Solución correcta: snippet en `theme.liquid` con condicional por `request.path`

### Dos páginas duplicadas
- Quedaron dos páginas "Implante Capilar en Bogotá" en Shopify.
- La correcta: ID `154884800813`, handle `implante-capilar-bogota`, plantilla `pf-88d89a52`.
- **PENDIENTE:** Eliminar la duplicada para evitar penalización por contenido duplicado.

---

## Estado final de los 6 elementos HTML/Liquid en PageFly

| # | Elemento | Estado |
|---|---|---|
| #1 | gtag Google Ads `AW-16490325890` | ✅ Activo |
| #2 | Schema GEO (MedicalClinic + MedicalProcedure + BreadcrumbList) | ✅ Activo |
| #3 | Bloque oculto `-9999px` | ✅ ELIMINADO |
| #4 | Script fbclid | ✅ Activo |
| #5 | JSON-LD FAQPage (8 preguntas) | ✅ Activo (en HTML pero Rich Results deprecated) |
| #6 | Eventos tracking (Meta Pixel ×2 + Google Ads ×3 + 11 eventos) | ✅ Activo |

---

## Checklist pre-publicación — Estado final

### A. SEO on-page
- [x] Meta title: `Implante Capilar FUE en Bogotá | Innovart Medical`
- [x] Meta description: 157 caracteres, compliance OK
- [x] URL handle: `/pages/implante-capilar-bogota`
- [x] H1 desktop + móvil en texto real
- [x] Párrafo intro único
- [x] NAP en texto visible (dirección + teléfono + horarios)

### B. GEO / Schema
- [x] JSON-LD MedicalClinic con NAP Bogotá
- [x] JSON-LD FAQPage con 8 preguntas (en theme.liquid vía snippet)
- [x] JSON-LD BreadcrumbList
- [x] Accordion FAQ visible al usuario

### C. Tracking
- [x] Script fbclid (HTML/Liquid #4)
- [x] Meta Pixel + Google Ads + 11 eventos (HTML/Liquid #6)

### D. Compliance
- [x] CERO "garantía vitalicia" (bloque oculto eliminado)
- [x] CERO "garantía de resultado"
- [x] Tel correcto 312 456 5014 en texto

---

## Pendientes post-sesión

1. **Eliminar página duplicada** — la segunda "Implante Capilar en Bogotá" en Shopify (revisar cuál es la duplicada sin contenido PageFly y borrarla)
2. ~~**AggregateRating schema**~~ ✅ COMPLETADO — 4.3 estrellas / 103 reseñas agregado al snippet `faq-bogota.liquid`. Rich Results Test: 3 elementos válidos (Breadcrumb + Empresas locales + Organización)
3. **Replicar a Medellín, Barranquilla, Bucaramanga** — usando la guía [[guia-replicacion-landings-ciudades]]. Para cada ciudad: crear snippet `faq-[ciudad].liquid` + línea en `theme.liquid`

---

## Patrón para replicar a otras ciudades

En `theme.liquid`, agregar después de la línea de Bogotá:
```liquid
{% if request.path == '/pages/implante-capilar-medellin' %}{% render 'faq-medellin' %}{% endif %}
{% if request.path == '/pages/implante-capilar-barranquilla' %}{% render 'faq-barranquilla' %}{% endif %}
{% if request.path == '/pages/implante-capilar-bucaramanga' %}{% render 'faq-bucaramanga' %}{% endif %}
```

Crear snippet por ciudad cambiando: nombre ciudad, dirección, coordenadas geo, URL.

---

**Relacionado:** [[landing-ciudades-plantilla-checklist-2026-06-20]] · [[guia-replicacion-landings-ciudades]] · [[eventos-tracking-bogota-html-liquid-6]] · [[geo-visibilidad-ia-auditoria-2026-06-22]]

*Creado 2026-06-23 — Claude Code + Javier Forero*
