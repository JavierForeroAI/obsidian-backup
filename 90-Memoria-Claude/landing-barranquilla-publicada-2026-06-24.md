---
name: landing-barranquilla-publicada-2026-06-24
description: Landing "Implante Capilar en Barranquilla" publicada el 2026-06-24 — estado completo, schema validado, AggregateRating 4.8/37
metadata:
  type: project
  fecha: 2026-06-24
  estado: completado
---

# Landing Implante Capilar en Barranquilla — PUBLICADA ✅

**URL en vivo:** `https://www.innovartmedical.com/pages/implante-capilar-barranquilla`

**Fecha publicación:** 2026-06-24

---

## Qué se hizo

### Fase 1 — Shopify Admin (MCP)
- Página creada: `Implante Capilar en Barranquilla | Innovart Medical`
- Handle: `implante-capilar-barranquilla`
- Meta title: `Implante Capilar FUE en Barranquilla | Innovart Medical` (55 chars)
- Meta description: `...Edificio Green Tower, Torre 2, Piso 7, Cons. 706.` (168 chars)

### Fase 2 — PageFly (duplicada de Bogotá)
- H1 Desktop + Móvil: `Implante Capilar en Barranquilla`
- Párrafo intro: Norte de la ciudad, Edificio Green Tower, Calle 77B #57-103
- NAP: Calle 77B #57-103, Torre 2, Piso 7, Cons. 706 · Edificio Green Tower
- FAQ preguntas 1 y 5 actualizadas con Barranquilla
- Bloque `-9999px` eliminado ✅

### Fase 3 — Theme Shopify
- Snippet `faq-barranquilla.liquid` creado con:
  - MedicalClinic schema + coordenadas 11.0041, -74.8069
  - AggregateRating: 4.8 estrellas / 37 reseñas (Google Maps verificado)
  - FAQPage: 8 preguntas
- `theme.liquid` línea 301: `{% if request.path == '/pages/implante-capilar-barranquilla' %}{% render 'faq-barranquilla' %}{% endif %}`

---

## Validación Google Rich Results Test

- ✅ 3 elementos válidos detectados
- ✅ Empresas locales (MedicalClinic + AggregateRating)
- ✅ Organización
- ✅ Rastreado correctamente 23 jun 2026, 20:58

---

## Datos de la sede

| Campo | Valor |
|---|---|
| Dirección | Calle 77B #57-103, Torre 2, Piso 7, Cons. 706 |
| Referencia | Edificio Green Tower |
| Zona | Norte, Barranquilla |
| Coords | 11.0041, -74.8069 |
| Tel | +57 312 456 5014 |
| Google Maps | 4.8 ⭐ / 37 reseñas |

---

## Pendientes post-publicación

- [ ] Monitorear indexación en Google Search Console (48-72h)
- [ ] Agregar AggregateRating a Medellín cuando se publique

**Relacionado:** [[guia-replicacion-landings-ciudades]] · [[landing-medellin-pagefly-2026-06-23]] · [[sesion-landing-bogota-2026-06-23]]
