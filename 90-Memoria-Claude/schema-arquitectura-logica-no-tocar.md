---
name: schema-arquitectura-logica-no-tocar
description: Arquitectura completa del sistema Schema.org en Innovart Medical Shopify. LEER ANTES de tocar cualquier schema. Reglas, lógica y estado por sede.
metadata:
  type: project
  status: COMPLETADO_ESTABLE
  date_completado: 2026-06-24
  advertencia: NO MODIFICAR sin entender esta lógica completa
---

# ⚠️ SCHEMA.ORG — LEER ANTES DE TOCAR NADA

**Estado:** 4 sedes en 0 ERRORES, 0 ADVERTENCIAS  
**Fecha estabilizado:** 2026-06-24

---

## 🏗️ Arquitectura del sistema

### Dos archivos de layout — distintos para distintas páginas

| Archivo | Páginas que lo usan | Cómo renderiza snippets |
|---------|--------------------|-----------------------|
| `layout/theme.liquid` | Bogotá, Barranquilla, Bucaramanga | Tiene `{% if page.handle == '...' %}{% render 'faq-xxx' %}{% endif %}` |
| `layout/theme.pagefly.liquid` | Medellín | Tiene `{% if page.handle == 'implante-capilar-medellin' %}{% render 'faq-medellin' %}{% endif %}` |

**CRÍTICO:** Si una página usa `theme.pagefly.liquid` y el snippet no está referenciado ahí, NO se renderiza aunque exista en `snippets/`.

---

## 📁 Snippets FAQ por sede

| Snippet | Contenido | Layout que lo carga |
|---------|-----------|-------------------|
| `snippets/faq-bogota.liquid` | FAQPage JSON-LD | theme.liquid |
| `snippets/faq-medellin.liquid` | FAQPage JSON-LD | theme.pagefly.liquid |
| `snippets/faq-barranquilla.liquid` | FAQPage JSON-LD | theme.liquid |
| `snippets/faq-bucaramanga.liquid` | FAQPage JSON-LD | theme.liquid |

Cada snippet contiene SOLO el `FAQPage` schema — nada más.

---

## 📄 Bloques HTML/Liquid en PageFly (por ciudad)

Cada landing page tiene bloques HTML/Liquid embebidos en PageFly con el `@graph` principal:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "MedicalClinic", ... },
    { "@type": "MedicalProcedure", ... },
    { "@type": "BreadcrumbList", ... }
  ]
}
```

**REGLA ABSOLUTA — MedicalProcedure:**  
`medicalSpecialty` NO es una propiedad válida de `MedicalProcedure`.  
Solo es válida en `MedicalClinic` / `MedicalOrganization`.  
Si se agrega a MedicalProcedure → 1 ADVERTENCIA en validator.schema.org.

---

## ✅ Estado validado por sede (validator.schema.org)

| Sede | URL | Errores | Advertencias | Schemas detectados |
|------|-----|---------|-------------|-------------------|
| **Bogotá** | /implante-capilar-bogota | 0 | 0 | MedicalProcedure, MedicalOrganization, Organization, BreadcrumbList, MedicalClinic, FAQPage |
| **Medellín** | /implante-capilar-medellin | 0 | 0 | MedicalProcedure, MedicalOrganization, Organization, BreadcrumbList, MedicalClinic, FAQPage |
| **Barranquilla** | /implante-capilar-barranquilla | 0 | 0 | MedicalProcedure, MedicalOrganization, Organization, BreadcrumbList, MedicalClinic, FAQPage |
| **Bucaramanga** | /implante-capilar-bucaramanga | 0 | 0 | MedicalProcedure, MedicalOrganization, Organization, BreadcrumbList, MedicalClinic, FAQPage |

---

## 🚫 Reglas que NO se pueden romper

1. **No agregar `medicalSpecialty` a MedicalProcedure** — causa ADVERTENCIA inmediata
2. **`medicalSpecialty` en MedicalClinic debe usar URL:** `"https://schema.org/Dermatology"` (no texto plano `"Dermatology"`)
3. **`procedureType` debe usar:** `"http://schema.org/PercutaneousProcedure"` (no SurgicalProcedure)
4. **Los snippets FAQ solo contienen FAQPage** — el @graph va en el bloque PageFly, no en el snippet
5. **Si se agrega una nueva sede con PageFly:** hay que agregar el `{% render %}` en `theme.pagefly.liquid` (no en theme.liquid)
6. **Si se agrega una nueva sede sin PageFly:** hay que agregar el `{% render %}` en `theme.liquid`

---

## 📍 Dónde están los render tags actuales

### En `theme.liquid` (cerca del cierre de `</head>`):
```liquid
{% if page.handle == 'implante-capilar-bogota' %}{% render 'faq-bogota' %}{% endif %}
{% if page.handle == 'implante-capilar-medellin' %}{% render 'faq-medellin' %}{% endif %}
{% if page.handle == 'implante-capilar-barranquilla' %}{% render 'faq-barranquilla' %}{% endif %}
{% if page.handle == 'implante-capilar-bucaramanga' %}{% render 'faq-bucaramanga' %}{% endif %}
```

### En `theme.pagefly.liquid` (antes de `{% include 'pagefly-app-header' %}</head>`):
```liquid
{% if page.handle == 'implante-capilar-medellin' %}{% render 'faq-medellin' %}{% endif %}
```

---

## 🔧 Cómo agregar una nueva sede correctamente

1. Crear `snippets/faq-[ciudad].liquid` con solo FAQPage
2. Determinar si la página usa PageFly o theme estándar
3. Agregar el `{% render %}` en el layout correcto (theme.liquid o theme.pagefly.liquid)
4. En el bloque HTML/Liquid de PageFly: agregar @graph con MedicalClinic + MedicalProcedure (sin medicalSpecialty en MedicalProcedure) + BreadcrumbList
5. Validar en validator.schema.org → debe dar 0 ERRORES, 0 ADVERTENCIAS

---

## 🔗 Referencias

- [[schema-medicalclinic-fase1-ejecutado-2026-06-24]] — Inyección metafields MedicalClinic por ciudad
- [[trabajo-geo-ia-refinements-2026-06-24]] — Plan GEO/IA completo Fases 1-3
