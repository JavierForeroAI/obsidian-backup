---
name: trabajo-geo-ia-refinements-2026-06-24
description: GEO/IA Refinements en progreso — Schema MedicalClinic por ciudad + Listicles + Video FAQ. Estado actual y plan de acción.
metadata:
  type: project
  status: FASE1_COMPLETADA
  date_started: 2026-06-24
  date_fase1_done: 2026-06-24
---

# GEO/IA Refinements — Trabajo en Progreso

**Sesión:** 2026-06-24  
**Estado:** Diagnóstico completo, listos para ejecutar Paso 1  
**Responsable:** Javier Forero (ejecución), Claude (guía)

---

## 📊 DIAGNÓSTICO ACTUAL — Schema por Página

| Página | URL | Schema Actual | Status | Acción |
|--------|-----|--------------|--------|--------|
| **HOME** | https://www.innovartmedical.com/ | ✅ MedicalClinic + priceRange + aggregateRating | DONE | ✅ Verificado 2026-06-24 |
| **Bogotá** | /pages/implante-capilar-bogota | ✓ FAQPage | SAFE | Complementar + MedicalClinic |
| **Medellín** | /pages/implante-capilar-medellin | ✓ FAQPage | SAFE | Complementar + MedicalClinic |
| **Barranquilla** | /pages/implante-capilar-barranquilla | ❌ NINGUNO | P0 | Agregar MedicalClinic |
| **Bucaramanga** | /pages/implante-capilar-bucaramanga | ❌ NINGUNO | P0 | Agregar MedicalClinic |
| **Panamá** | /pages/panama | ❌ NINGUNO | P0 | Agregar MedicalClinic |
| **Blog posts** | /blogs/articulos-medicos/* | ✓ Article + author | OK | Verificar en próximo paso |
| **Página de precios** | /pages/precios | ✓ PriceSpecification | OK | Verificar en próximo paso |

---

## 🎯 PLAN GEO/IA — 3 FASES

### **FASE 1 — Schema MedicalClinic (ESTA SEMANA)**

**Grupo A: Inyección SEGURA** (sin schema actual)
- ✅ HOME
- ✅ Barranquilla
- ✅ Bucaramanga
- ✅ Panamá

**Grupo B: Inyección COMPLEMENTARIA** (mantener FAQPage intacto)
- ✅ Bogotá (agregar MedicalClinic + mantener FAQPage)
- ✅ Medellín (agregar MedicalClinic + mantener FAQPage)

**JSON-LD Template (MedicalClinic) — para HOME y todas las ciudades:**
```json
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Innovart Medical IPS",
  "description": "Clínica especializada en implante capilar FUE con 1000+ casos exitosos",
  "telephone": "+573124565014",
  "address": [
    {"streetAddress": "Calle 119 #7-94, Bogotá", "addressLocality": "Bogotá"},
    {"streetAddress": "C.C. Oviedo, Medellín", "addressLocality": "Medellín"},
    {"streetAddress": "Calle 77 #57-103, Barranquilla", "addressLocality": "Barranquilla"},
    {"streetAddress": "Transversal 93, Bucaramanga", "addressLocality": "Bucaramanga"}
  ],
  "priceRange": "COP 8.000.000 – 11.000.000",
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.5", "reviewCount": "103+"},
  "url": "https://www.innovartmedical.com"
}
```

**Métodos disponibles:**
1. **Opción 1:** Agregar en snippet Shopify separado (cero riesgo, verificar PageFly primero)
2. **Opción 2:** Editar theme.liquid directo (rápido, requiere acceso Shopify Admin)
3. **Opción 3:** Via MCP Shopify (automatizado, sin tocar UI)

**DECISIÓN PENDIENTE:** ¿Cuál opción? ¿Acceso a Shopify Admin disponible?

---

### **FASE 2 — Listicles Competitivos ✅ PUBLICADOS EN SHOPIFY (2026-06-24)**

**Artículos VIVOS:**
1. ✅ **Top 5 Clínicas Bogotá** — https://www.innovartmedical.com/blogs/articulos-medicos/top-5-clinicas-implante-capilar-bogota-2026 (2,425 palabras | 154 estilos CSS inline)
2. ✅ **FUE vs DHI Comparativa** — https://www.innovartmedical.com/blogs/articulos-medicos/fue-vs-dhi-comparativa-definitiva-colombia-2026 (2,104 palabras | 132 estilos CSS inline)
3. ✅ **Guía por Ciudad** — https://www.innovartmedical.com/blogs/articulos-medicos/donde-hacerse-implante-capilar-colombia-guia-por-ciudad-2026 (2,781 palabras | 130 estilos CSS inline)

**Diseño:** Navy (#2C3E50) + Dorado (#c9a84c) + Teal (#f0f8f5) | Georgia serif | Ranking cards, tablas, pros/cons  
**Schema:** Article + ItemList/FAQPage | Dr. Fabián Carreño | Innovart primero en todo  
**Compliance:** ✅ Sin prohibidos, precios reales, competidores solo nombre, CTA box, FAQ  
**Impacto esperado:** GEO Score +5–8pts, E-E-A-T +10%, conversiones +10%

---

### **FASE 3 — Video FAQ (SEMANA 2-3)**

**Videos a grabar:**
1. "¿Cuánto cuesta el implante capilar?"
2. "FUE vs DHI: ¿Cuál técnica elegir?"
3. "¿Cuánto tarda la recuperación?"
4. "¿Es permanente el resultado?"
5. "¿Dónde operarse? Bogotá vs Medellín vs Barranquilla"

**Host:** YouTube  
**Schema:** `VideoObject` en blogs  
**Duración:** 3–5 min c/video  
**Tiempo:** 2–3 horas (grabación + edición)

---

## 📈 Impacto esperado

| Acción | GEO Score ↑ | E-E-A-T ↑ | Conversiones ↑ |
|--------|-----------|----------|----------------|
| Schema MedicalClinic | +8–12pts | +15% | +5% |
| Listicles | +5–8pts | +10% | +10% |
| Video FAQ | +3–5pts | +8% | +8% |
| **TOTAL** | **+18–25pts** | **+33%** | **+23%** |

(Baseline actual: GEO Score 38/100 → Target: 56–63/100)

---

## 🔗 Archivos relacionados

- [[proyecto-landing-cities-seo-geo-completo]] — Landings de ciudad (DONE)
- [[fase-2-upgrade-blogs-contenido-2026-06-22]] — Blogs (DONE)
- [[geo-auditoria-junio24-2026]] — Auditoría GEO (baseline)
- [[feedback-schema-codigo-completo]] — Regla: siempre código completo

---

## ✅ Checklist Ejecución

### Paso 1: Verificar acceso
- [x] Confirmar acceso a Shopify Admin
- [x] Opción 2 (theme.liquid directo)

### Paso 2: HOME Schema
- [x] MedicalClinic + priceRange + aggregateRating en HOME ✅ verificado 2026-06-24

### Paso 3: Ciudades Grupo A
- [x] Barranquilla: MedicalClinic ✅
- [x] Bucaramanga: MedicalClinic ✅
- [x] Panamá: MedicalClinic ✅

### Paso 4: Ciudades Grupo B
- [x] Bogotá: MedicalClinic ✅
- [x] Medellín: MedicalClinic ✅

### Paso 4b: /pages/precios
- [x] priceRange COP 8000000-11000000 ✅ verificado 2026-06-24
- [x] priceRange USD 3500-4500 ✅ verificado 2026-06-24
- [x] snippet en snippets/page-precios-schema.liquid
- [x] theme.liquid con guard `page.handle == 'precios'`

### Paso 5: Listicles + Video FAQ
- [ ] Crear 3 listicles (semana 2)
- [ ] Grabar 5 videos (semana 2-3)

---

## 🎬 Próximos pasos

**HILO A SEGUIR EN PRÓXIMO CHAT:**
1. Javier responde: ¿Opción 1, 2 o 3? ¿Acceso a Shopify Admin?
2. Ejecutar Paso 1 (HOME Schema) según opción elegida
3. Verificar en Rich Results Test
4. Replicar a 5 ciudades (Grupo A + B)
5. Continuar con Fases 2 y 3

---

**Última actualización:** 2026-06-24  
**Sesión anterior:** Landing pages SEO/GEO (COMPLETED)  
**Sesión siguiente:** Ejecutar GEO/IA Refinements
