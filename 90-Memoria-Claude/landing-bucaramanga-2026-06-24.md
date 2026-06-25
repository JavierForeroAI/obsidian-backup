---
name: landing-bucaramanga-2026-06-24
description: Landing "Implante Capilar en Bucaramanga" creada y publicada el 2026-06-24. Estado, datos de sede, fixes de handle PageFly y pendientes.
metadata:
  type: project
  fecha: 2026-06-24
  estado: publicada
---

# Landing Implante Capilar en Bucaramanga — 2026-06-24

**URL:** `https://www.innovartmedical.com/pages/implante-capilar-bucaramanga`
**Estado:** ✅ PUBLICADA (2026-06-24)
**Shopify Page ID (en vivo):** `gid://shopify/Page/154896073005`

## Datos de la sede Bucaramanga

| Campo | Valor |
|---|---|
| Dirección | Centro Internacional de Especialistas, Complejo Médico HIC, KM 7, Cons. 719N, Piso 7 |
| Zona | Cabecera del Llano |
| Landmark | Complejo Médico HIC |
| Coordenadas | 7.1193, -73.1227 |
| Depto | Santander |
| Teléfono | +57 312 456 5014 |
| Horario | Lun–Vie 11am–5pm · Sáb 11am–4pm |

## Qué se hizo

**Shopify Admin (MCP):**
- Página en vivo `154896073005`, handle `implante-capilar-bucaramanga` (limpio, matchea theme.liquid línea 302 → renderiza `faq-bucaramanga.liquid`)
- Meta title: "Implante Capilar FUE en Bucaramanga | Innovart Medical"
- Meta description: "Implante capilar FUE en Bucaramanga: especialistas certificados, valoración gratuita, 24 controles postoperatorios y garantía de folículos. Complejo Médico HIC, Cons. 719N."

**Shopify Theme (ya existía de la sesión BAQ):**
- Snippet `faq-bucaramanga.liquid` (FAQPage JSON-LD)
- `theme.liquid` línea 302 enruta el render para `/pages/implante-capilar-bucaramanga`

**PageFly:**
- Duplicada desde Bogotá. H1 desktop/móvil, párrafo intro (Cabecera del Llano + Complejo Médico HIC + Cons. 719N), NAP, FAQ 1 y 5 actualizados a Bucaramanga
- HTML #1/#2 Schema MedicalClinic insertado con datos BGA (geo 7.1193,-73.1227, addressRegion Santander)

## ⚠️ Aprendizaje clave — PageFly crea su propia página con handle "-✅"

Al publicar desde PageFly, **PageFly NO usó la página que se creó por MCP**: generó una página nueva con handle `implante-capilar-bucaramanga-✅` y título `…Innovart Medical ✅`. Esto rompía 2 cosas:
1. El handle con `-✅` NO matchea theme.liquid → el FAQPage del snippet no renderizaba.
2. El SEO (metafields) quedó en la página vacía, no en la publicada.

**Fix aplicado (MCP):** se borró/quedó huérfana la página vacía, se cambió el handle de la publicada a `implante-capilar-bucaramanga`, se corrigió el título y se seteó `title_tag`.
**Ojo:** PageFly sobreescribe el TÍTULO del admin (con `✅`) cada vez que se le da Publish. Solución estable: renombrar la página DENTRO de PageFly quitando el `✅` (hecho). Handle y metafields SEO NO los toca PageFly.

**Why:** evitar que las próximas ciudades repitan el handle `-✅` y pierdan el FAQPage + SEO.
**How to apply:** al replicar otra ciudad, tras publicar desde PageFly verificar SIEMPRE por MCP el handle real (`pages(query:"ciudad")`), corregirlo a la URL corta y renombrar la página interna de PageFly sin `✅`.

## Pendiente

- [ ] Rich Results Test de la URL → confirmar `FAQPage` + `MedicalClinic` (esperar unos min por caché)
- [ ] Borrar bloque oculto `-9999px` — Javier lo hará en un barrido conjunto de TODAS las ciudades, después de publicar (no antes)
- [ ] Eventos de tracking (Pixel Lead, Google Ads conv, WhatsApp click) — HTML #6 post-publicación
- [ ] aggregateRating: solo en MedicalClinic, NUNCA en FAQPage (lección Medellín)

## Referencias
- [[guia-replicacion-landings-ciudades]]
- [[landing-barranquilla-2026-06-24]]
- [[landing-medellin-pagefly-2026-06-23]]
- [[protocolo-validacion-landing-automatica]]
