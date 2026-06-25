---
name: landing-barranquilla-2026-06-24
description: Landing "Implante Capilar en Barranquilla" creada y publicada el 2026-06-24. Shopify + PageFly + theme.liquid completos.
metadata:
  type: project
---

# Landing Implante Capilar en Barranquilla — 2026-06-24

**URL:** `https://www.innovartmedical.com/pages/implante-capilar-barranquilla`

**Estado:** ✅ PUBLICADA (2026-06-24)

## Datos de la sede BAQ

| Campo | Valor |
|---|---|
| Dirección | Calle 77B #57-103, Torre 2, Piso 7, Cons. 706 |
| Edificio | Green Tower |
| Zona | Norte — Barranquilla |
| Coordenadas | 11.0041, -74.8069 |
| Teléfono | +57 312 456 5014 |
| Horario | Lun–Vie 11am–5pm · Sáb 11am–4pm |

## Qué se hizo

**Fase 1 — Shopify Admin (MCP):**
- Página creada: `gid://shopify/Page/154887422253`
- Handle: `implante-capilar-barranquilla`
- Meta title: "Implante Capilar FUE en Barranquilla | Innovart Medical"
- Meta description: "Implante capilar FUE en Barranquilla: especialistas certificados, valoración gratuita, 24 controles postoperatorios y garantía de folículos. Edificio Green Tower, Torre 2, Piso 7, Cons. 706."
- Visibilidad inicial: Oculta

**Fase 2 — Shopify Theme:**
- Snippet `faq-barranquilla.liquid` creado en `snippets/` (FAQPage JSON-LD, 8 preguntas con datos BAQ)
- Snippet `faq-bucaramanga.liquid` creado también (para uso futuro)
- `theme.liquid` línea 301: `{% if request.path == '/pages/implante-capilar-barranquilla' %}{% render 'faq-barranquilla' %}{% endif %}`
- `theme.liquid` línea 302: `{% if request.path == '/pages/implante-capilar-bucaramanga' %}{% render 'faq-bucaramanga' %}{% endif %}`

**Fase 3 — PageFly:**
- Duplicada desde landing Bogotá
- H1 Desktop y Móvil → "Implante Capilar en Barranquilla"
- Párrafo intro actualizado (Green Tower, Calle 77B, El Poblado → Norte)
- NAP actualizado con dirección Green Tower
- FAQ preguntas 1 y 5 actualizadas para Barranquilla
- Schema MedicalClinic (HTML #2) reemplazado completo con datos BAQ
- Publicada

**Verificación post-deploy:** H1 ✅, dirección Green Tower ✅, teléfono ✅, sin referencias a Bogotá ✅. fbclid/JSON-LD/MedicalClinic no visibles para fetcher estático (renderizados por JS/browser — normal).

## Notas técnicas

- `aggregateRating` NO incluido en `faq-barranquilla.liquid` (aprendizaje de Medellín: no va en FAQPage sino en MedicalClinic de PageFly)
- PageFly limita fetcher estático para JS — verificar schema siempre via "Ver código fuente" en Chrome, buscar `FAQPage`

## Pendiente

- Bucaramanga: snippet `faq-bucaramanga.liquid` ya listo; falta crear página Shopify + PageFly + publicar
- Agregar reseñas de Google (widget/app Shopify) cuando se definan (ver [[datos-sedes-y-schemas-ciudades]])

## Referencias

- [[guia-replicacion-landings-ciudades]]
- [[sesion-landing-bogota-2026-06-23]]
- [[landing-medellin-pagefly-2026-06-23]]
- [[feedback-pagefly-url-stability]]
