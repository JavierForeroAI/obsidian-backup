---
name: geo-auditoria-junio24-2026
description: Auditoría GEO completa 2026-06-24. Score 38/100. Innovart ausente en 100% consultas no-branded. Roadmap P0-P3 + 90/180 días.
metadata:
  type: project
---

# Auditoría GEO — Innovart Medical IPS
**Fecha:** 2026-06-24
**Score anterior (2026-06-22):** 42/100
**Score actual:** 38/100 ⚠️ (regresión leve — landings de ciudad publicadas pero home sigue sin schema)

**Why:** Las 4 landings de ciudad se publicaron (Bogotá, Medellín, Barranquilla, Bucaramanga) con FAQPage, lo que es positivo, pero la home sigue sin JSON-LD y la citabilidad no-branded sigue en 0. El trigger de esta auditoría fue que ChatGPT mostró a Innovart como `chatgpt://generic-entity?number=7` en un análisis competitivo enviado por Diego Silva (Bee Comunicaciones) el 24/06/26.

**How to apply:** Usar este informe como base de priorización. Ejecutar P0 (schema home) antes de cualquier otro trabajo GEO.

---

## AI Visibility Score: 38/100

| Subscore | Puntaje | Evidencia |
|---|---|---|
| Entity Authority | 40/100 | Top Doctors ✅, YouTube ✅, IG ✅ — sin Wikipedia, sin Wikidata, sin Doctoralia verificado |
| GEO Readiness | 28/100 | Home = 0 schema JSON-LD ⚠️. FAQPage en 4 landings pero AggregateRating mal ubicado |
| AI Citability | 12/100 | Ausente en 3/3 consultas no-branded verificadas en vivo |
| Knowledge Graph | 35/100 | Blog tiene schema. Home no. Sin MedicalClinic + Physician + AggregateRating en money pages |
| Trust Signals | 32/100 | Sin menciones en listicles de medios orgánicos. Sin Doctoralia activo |
| Medical Authority | 45/100 | Dr. Carreño en Top Doctors, YouTube, TikTok — bien. Falta RAIS/credenciales en web |
| Semantic Coverage | 22/100 | Sin página de precio. Sin comparativa. Sin listicle. Sin claims de volumen en texto crawleable |
| Brand Consistency | 55/100 | NAP semi-consistente. "IPS" aparece/desaparece. Colisión con "Clinica Innovart" España |

---

## Hallazgos críticos (evidencia en vivo 2026-06-24)

### 1. Invisible en 100% de consultas no-branded
Búsquedas ejecutadas y resultado:
- "mejor clínica implante capilar Bogotá Colombia 2026" → Rogans, Mediarte, HERO, Capilix, Ileanovo — **Innovart ausente**
- "cuánto cuesta implante capilar Colombia 2026" → Rogans, Sin Calvicie, Mediarte, La República — **Innovart ausente**
- "mejores clínicas trasplante capilar Colombia ranking" → Capilclinic, Mediarte, HERO, Total Hair, Rogans — **Innovart ausente**

### 2. Rogans domina con listicle propio
URL: `rogansya.com/implante-capilar-en-bogota/` — página dedicada "mejores clínicas de implante capilar en Bogotá". Los LLMs la citan directamente. Innovart no tiene nada equivalente.

### 3. Home sin schema (igual que baseline junio-19)
0 JSON-LD detectado en home. El blog tiene MedicalOrganization/MedicalProcedure/Person. Las landings tienen FAQPage parcial. La página más importante para crawlers IA está vacía estructuralmente.

### 4. Sin página de precio
Rogans, Sin Calvicie y Mediarte tienen páginas dedicadas a precios. Los LLMs las citan para consultas de costo. Innovart no tiene ninguna.

### 5. Claims de autoridad no crawleables
"33.000+ pacientes" probablemente está en imagen PageFly (la IA no la lee). No aparece en texto HTML visible.

### 6. AggregateRating mal ubicado
Identificado en landings de Medellín y posiblemente Barranquilla/Bucaramanga: AggregateRating dentro de FAQPage (inválido). Debe estar dentro de MedicalClinic.

---

## Roadmap priorizado

### P0 — Ahora (< 1 hora, máximo impacto)
**Schema MedicalClinic en home**
```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Innovart Medical IPS",
  "description": "Clínica especializada en implante capilar FUE y DHI en Colombia. Más de 33.000 pacientes. Sedes en Bogotá, Medellín, Barranquilla, Bucaramanga y Panamá.",
  "medicalSpecialty": "PlasticSurgery",
  "url": "https://www.innovartmedical.com",
  "telephone": "+573124565014",
  "priceRange": "$8.000.000 - $11.000.000 COP",
  "physician": {
    "@type": "Physician",
    "name": "Fabián Carreño Jiménez"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "[VERIFICAR]"
  },
  "address": [
    {"@type": "PostalAddress", "addressLocality": "Bogotá", "addressCountry": "CO"},
    {"@type": "PostalAddress", "addressLocality": "Medellín", "addressCountry": "CO"},
    {"@type": "PostalAddress", "addressLocality": "Barranquilla", "addressCountry": "CO"},
    {"@type": "PostalAddress", "addressLocality": "Bucaramanga", "addressCountry": "CO"}
  ]
}
```

### P1 — Esta semana
**Página de precios** (`/pages/precio-implante-capilar`)
- Rango por folículos, tabla por caso (entradas / densificación / completo)
- Diferencia FUE vs DHI, qué incluye
- Bloques de ~150 palabras autónomos (cada sección responde una pregunta completa)
- Precios: $8M–$11M COP Colombia, $3,500–$4,500 USD Panamá

### P2 — Esta semana
**Corregir AggregateRating en landings de ciudad**
- Mover de FAQPage → MedicalClinic en Medellín, Barranquilla y Bucaramanga
- Bogotá: verificar si también aplica

### P3 — Esta semana
**Claims de autoridad en texto crawleable en home**
- Agregar en HTML visible: "33.000+ pacientes", "Dr. Fabián Carreño Jiménez", "FUE y DHI", las 5 sedes
- No solo en imágenes PageFly

### 90 días
- Página listicle propia: `/pages/mejores-clinicas-implante-capilar-colombia-2026`
- Perfil Doctoralia activo con reseñas por sede
- Gestionar inclusión en artículos de ranking existentes (El Espectador, Vanguardia, miclinicacapilar.com)
- Página del Dr. Fabián Carreño con schema Physician completo + certificaciones

### 180 días
- Wikidata entity para "Innovart Medical IPS"
- Google My Business unificado y verificado por sede con reseñas automatizadas post-cirugía
- RAIS visible en el sitio
- Contenido multimodal en páginas de tratamiento (video + imágenes + schema)

---

## Competidores que bloquean a Innovart

| Competidor | Por qué gana en IA |
|---|---|
| Rogans | Listicle propio "mejores clínicas Bogotá" + página de precios |
| Mediarte | Escala (12 ciudades), 20.000+ implantes citables, 98% recomendación |
| HERO Institute | "Primera clínica en Colombia" + tecnología robótica (claims únicos) |
| DHI Colombia | "250.000 pacientes", "50 años", "97% tasa de éxito" |

## Próxima acción concreta
Ejecutar P0: inyectar schema MedicalClinic en home via Shopify theme (`theme.liquid` o snippet dedicado `schema-home.liquid`).

**Vinculado a:** [[geo-visibilidad-ia-diagnostico-2026-06-19]] · [[geo-visibilidad-ia-auditoria-2026-06-22]] · [[landing-ciudades-plantilla-checklist-2026-06-20]] · [[seo-puro-seo-cowork]]
