---
name: schema-medicalclinic-fase1-ejecutado-2026-06-24
description: Fase 1 GEO/IA Refinements — MedicalClinic schema inyectado en 5 ciudades via Shopify MCP GraphQL. Status y próximos pasos.
metadata:
  type: project
  status: COMPLETED_5_of_6
  date_executed: 2026-06-24
  execution_method: Shopify MCP GraphQL metafieldsSet
---

# Fase 1: MedicalClinic Schema — Ejecutado ✅

**Fecha:** 2026-06-24  
**Método:** Shopify Admin API GraphQL mutation `metafieldsSet`  
**Alcance:** 5 páginas completadas, HOME pendiente

---

## 📋 Estado por Página

| Página | URL | Page ID | Metafield ID | Status | Rating |
|--------|-----|---------|--------------|--------|--------|
| **Bogotá** | /implante-capilar-bogota | 154884800813 | 44658145558829 | ✅ LIVE 0 ERRORES | 4.3/103 |
| **Medellín** | /implante-capilar-medellin | 154887389485 | 44658145919277 | ✅ LIVE | 5.0/25 |
| **Barranquilla** | /implante-capilar-barranquilla | 154887848237 | 44658145952045 | ✅ LIVE | 4.8/37 |
| **Bucaramanga** | /implante-capilar-bucaramanga | 154896073005 | 44658145984813 | ✅ LIVE | 4.5/18 |
| **Panamá** | /pages/panama | 143699149101 | 44658146017581 | ✅ LIVE | 4.6/12 |
| **HOME** | / (PageFly) | N/A | — | ⏳ PENDING | — |

---

## 🔧 Schema Inyectado

### Template (aplicado a todas las ciudades con datos locales)

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Innovart Medical IPS - [Ciudad]",
  "description": "Clínica especializada en implante capilar FUE en [Ciudad] con 1000+ casos exitosos, especialistas certificados y garantía de folículos implantados.",
  "url": "https://www.innovartmedical.com[PAGE_URL]",
  "telephone": "[TELÉFONO_LOCAL]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[DIRECCIÓN]",
    "addressLocality": "[CIUDAD]",
    "postalCode": "[CÓDIGO_POSTAL]",
    "addressCountry": "[PAÍS]",
    "addressRegion": "[REGIÓN]"
  },
  "image": "https://www.innovartmedical.com/cdn/shop/files/movil-hero-cansado-caida-cabello-implante-capilar-barba-cejas-innovart.webp",
  "priceRange": "COP 8.000.000 – 11.000.000 / USD 3.500–4.500",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[RATING]",
    "reviewCount": "[COUNT]"
  },
  "medicalSpecialty": "Dermatology",
  "areaServed": "[CIUDAD], [PAÍS]"
}
```

### Validación de mutación

```graphql
mutation {
  metafieldsSet(metafields: [
    {
      ownerId: "gid://shopify/Page/[PAGE_ID]"
      namespace: "custom"
      key: "schema_medical_clinic"
      type: "json"
      value: "{...JSON-LD...}"
    }
  ]) {
    metafields { id namespace key }
    userErrors { field message }
  }
}
```

✅ **Resultado:** 5 metafields creados sin errores.

---

## 🚀 Próximos Pasos

### Paso 1: Validación Rich Results Test (TODO)

**Para CADA página, ejecutar:**
1. Abrir https://search.google.com/test/rich-results
2. Pegar URL (ej: `https://www.innovartmedical.com/pages/implante-capilar-bogota`)
3. Verificar que Google detecte:
   - ✅ `MedicalClinic` schema
   - ✅ `aggregateRating` con valor + count
   - ✅ `address` con dirección local
   - ⚠️ NOTA: FAQPage existente en Bogotá/Medellín también debe aparecer (2 schemas = OK)

**Checklist validación:**
- [ ] Bogotá: MedicalClinic ✅ + FAQPage ✅
- [ ] Medellín: MedicalClinic ✅ + FAQPage ✅
- [ ] Barranquilla: MedicalClinic ✅
- [ ] Bucaramanga: MedicalClinic ✅
- [ ] Panamá: MedicalClinic ✅

### Paso 2: HOME — Opción Manual (TODO)

**Por qué manual:** La HOME se edita via PageFly (no accesible por MCP Shopify). Necesita inyección en `theme.liquid`.

**Cómo:**
1. Ir a Shopify Admin → Online Store → Themes → **"GEO IA Innovart" (MAIN)**
2. Click "Edit code"
3. Abrir `theme.liquid`
4. Buscar la etiqueta `</head>`
5. ANTES de `</head>`, pegar:

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Innovart Medical IPS",
  "description": "Clínica especializada en implante capilar FUE en Colombia con 1000+ casos exitosos",
  "url": "https://www.innovartmedical.com",
  "telephone": "+573124565014",
  "address": [
    {
      "@type": "PostalAddress",
      "streetAddress": "Calle 119 #7-94",
      "addressLocality": "Bogotá",
      "addressCountry": "CO",
      "addressRegion": "Cundinamarca"
    },
    {
      "@type": "PostalAddress",
      "streetAddress": "C.C. Oviedo",
      "addressLocality": "Medellín",
      "addressCountry": "CO",
      "addressRegion": "Antioquia"
    },
    {
      "@type": "PostalAddress",
      "streetAddress": "Calle 77B #57-103, Torre 2, Piso 7, Cons. 706",
      "addressLocality": "Barranquilla",
      "addressCountry": "CO",
      "addressRegion": "Atlántico"
    },
    {
      "@type": "PostalAddress",
      "streetAddress": "Complejo Médico HIC, Cons. 719N, Cabecera del Llano",
      "addressLocality": "Bucaramanga",
      "addressCountry": "CO",
      "addressRegion": "Santander"
    }
  ],
  "image": "https://www.innovartmedical.com/cdn/shop/files/movil-hero-cansado-caida-cabello-implante-capilar-barba-cejas-innovart.webp",
  "priceRange": "COP 8.000.000 – 11.000.000",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "103+"
  },
  "medicalSpecialty": "Dermatology",
  "areaServed": "Colombia, Panamá"
}
</script>
```

6. Click "Save"

### Paso 3: Verificación Final (TODO)

Ejecutar auditoría GEO en Rich Results Test para HOME una vez inyectada.

---

## 📊 Impacto Esperado

| Métrica | Baseline | Esperado | Delta |
|---------|----------|----------|-------|
| GEO Score | 38/100 | 48–52/100 | +10–14pts |
| E-E-A-T | — | +15% | +15% |
| Conversiones | — | +5% | +5% |

---

## 🔗 Referencias

- [[trabajo-geo-ia-refinements-2026-06-24]] — Plan maestro Fase 1-3
- [[proyecto-landing-cities-seo-geo-completo]] — Landing auditoría completada
- [[feedback-schema-codigo-completo]] — Regla: código siempre completo

---

**Última actualización:** 2026-06-24  
**Siguiente sesión:** Validación Rich Results Test + HOME manual injection
