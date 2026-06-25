---
name: landing-medellin-pagefly-2026-06-23
description: Landing "Implante Capilar en Medellín" creada en PageFly el 2026-06-23, publicada el 2026-06-24. URL definitiva /pages/implante-capilar-medellin.
metadata:
  type: project
---

# Landing Implante Capilar en Medellín — Estado al 2026-06-24

**URL definitiva:** `https://www.innovartmedical.com/pages/implante-capilar-medellin`

**Estado:** ✅ PUBLICADA (2026-06-24). El handle corto `implante-capilar-medellin` está activo y el snippet `faq-medellin.liquid` lo detecta correctamente (theme.liquid línea 300 usa URL corta).

## Qué se hizo

Duplicada desde la landing de Bogotá en PageFly y editada completamente para Medellín.

**Cambios aplicados:**

| Elemento | Valor Medellín |
|---|---|
| H1 Desktop | Implante Capilar en Medellín |
| H1 Móvil | Implante Capilar en Medellín |
| Párrafo intro PC | Bogotá → Medellín, Calle 119 → C.C. Oviedo Torre Médica Oviedo, Chicó Norte → El Poblado |
| NAP PC y Móvil | C.C. Oviedo, Torre Médica Oviedo, Consultorio 678 · El Poblado, Medellín |
| FAQ 1 | "...en Medellín?" |
| FAQ 5 pregunta | ¿Cómo agendo una valoración en Medellín? |
| FAQ 5 respuesta | Incluye C.C. Oviedo + +57 312 456 5014 |
| HTML #2 (Schema MedicalClinic) | Reemplazado completo con datos Medellín |
| HTML #3 (bloque oculto -9999px) | **BORRADO** (era copia de Bogotá, black-hat SEO) |
| HTML #5 (FAQPage) | Actualizado con Medellín |
| HTML #6 (Event tracking) | Actualizado referencias Bogotá → Medellín |

**SEO en Shopify Admin (configurado por MCP):**
- Título: `Implante Capilar en Medellín | Innovart Medical` (47/70 chars ✅)
- Metadescripción: `Implante capilar FUE en Medellín: especialistas certificados, valoración gratuita, 24 controles postoperatorios y garantía de folículos. C.C. Oviedo` (148/160 ✅)
- URL slug: `implante-capilar-en-medellin-innovart-medical`
- Redirect 301 activado

## ✅ Issue resuelto — aggregateRating en FAQPage (2026-06-24)

El snippet `faq-medellin.liquid` tenía un bloque `aggregateRating` dentro del tipo `FAQPage`. Google Rich Results Test lo marcaba como error "Elemento sin nombre" porque `aggregateRating` solo es válido dentro de `LocalBusiness`, `MedicalClinic` o `Product` — **nunca dentro de `FAQPage`**. **Solución aplicada:** se eliminó el bloque `aggregateRating` del snippet (reemplazo completo del archivo dejándolo solo con FAQPage + 8 preguntas). El rating válido ya vive en el schema `MedicalClinic` de PageFly (HTML #2) y, además, Google Maps muestra 25 reseñas reales (5.0★) para la sede.

**Resultado final Rich Results Test:** ✅ 4 elementos válidos (Breadcrumb, MedicalClinic/Empresas locales, Organización ×2). El "problema no crítico" en Organización es un campo opcional y NO bloquea rich results. Sin error de reseñas.

### Lecciones clave de la sesión
- **Caché del test:** correr el Rich Results Test inmediatamente tras guardar muestra la versión vieja. Esperar unos minutos y re-correr — eso resolvió el "falso fallo" persistente.
- **aggregateRating NUNCA va dentro de FAQPage.** Aplica también a `faq-bogota.liquid` y demás snippets de ciudad (tienen el mismo bloque pero no rendían porque su URL no matcheaba; conviene limpiarlos igual).
- **Arquitectura tema:** `theme.liquid` tiene una línea `{% if request.path == '/pages/<slug>' %}{% render 'faq-<ciudad>' %}{% endif %}` por ciudad (Bogotá 299, Medellín 300, Barranquilla 301, Bucaramanga 302). Cada ciudad = 1 snippet `faq-<ciudad>.liquid` + 1 línea en theme.liquid.
- **Slug:** Medellín usa la URL corta `implante-capilar-medellin` (la que matchea theme.liquid línea 300), NO la larga.
- Cuidado al duplicar en PageFly: el **HTML #3 oculto (left:-9999px)** se copia desde Bogotá y debe borrarse en cada ciudad.

## Pendiente

1. ~~Publicar en PageFly~~ ✅ HECHO
2. ~~Eliminar `aggregateRating` de `faq-medellin.liquid`~~ ✅ HECHO (2026-06-24)
3. ~~Validar Rich Results Test~~ ✅ HECHO — 4 elementos válidos
4. Limpiar `aggregateRating` también en `faq-bogota.liquid` (preventivo)
5. Validar Rich Results de Barranquilla y Bucaramanga (creadas en la misma sesión)

## Referencia técnica

- Plantilla fuente: [[guia-replicacion-landings-ciudades]]
- Checklist: [[landing-ciudades-plantilla-checklist-2026-06-20]]
- Próximas ciudades: Barranquilla → Bucaramanga
