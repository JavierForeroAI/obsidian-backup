---
name: pagina-precios-expandida-2026-06-25
description: Página /pages/precios expandida con 6 bloques autónomos optimizados para AEO/GEO (FUE vs DHI, precios por ciudad, financiación, garantía, timeline 18 meses, FAQ). Implementado por MCP Shopify GraphQL.
metadata:
  type: project
  date: 2026-06-25
  company: Innovart
---

# /pages/precios Expandida — 6 Bloques + Schema JSON-LD (25 junio 2026)

## Cambios Implementados

**Página:** `gid://shopify/Page/154899317037` (`¿Cuánto cuesta el implante capilar? Precios FUE 2026`)  
**Handle:** `/pages/precios`  
**Estrategia:** Expandir para que LLMs citen directamente + mejorar GEO/AEO Score

## 6 Bloques Autónomos

### **Bloque 1: Tabla FUE vs DHI (Comparativa)**
- 8 criterios: técnica, duración, cicatrices, precio, recuperación, resultados, ideal para
- Copy introductorio sobre opciones disponibles en Innovart
- Visibilidad: LLMs citan directamente tablas comparativas

### **Bloque 2: Rangos de Precio por Ciudad**
- Grid de 5 sedes (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá)
- Precio FUE y DHI por sede en COP y USD
- Transparencia: "Precios desde... hasta"
- PriceRange schema: `minPrice: 8000000 COP` / `maxPrice: 11000000 COP` + USD

### **Bloque 3: Financiación**
- MeddiPay: hasta 90%, 12–36 meses
- Pago directo (contado)
- CTAs a landing `/financiacionbta` (y replicadas a otras sedes)

### **Bloque 4: Garantía de Resultado**
- Qué cubre: viabilidad de folículos, técnica, control
- Condiciones: 24 controles/18 meses incluidos
- ⚠️ Lenguaje PROHIBIDO: "Garantía Vitalicia" → usar "Garantía de resultado"

### **Bloque 5: Timeline 18 Meses**
- Costo real mes 1 vs mes 3 vs mes 6 vs mes 18
- Fases: implante → cicatrización → crecimiento visible → resultado final
- Impacto: usuario entiende que precio inicial ≠ costo total real

### **Bloque 6: FAQ Autónoma**
- 10 preguntas frecuentes (críticas para AEO)
- Ejemplos: "¿Qué define el costo?", "¿Hay descuentos?", "¿DHI vs FUE cuál es mejor?", "¿Financiación para extranjeros?"
- FAQPage schema: Google y ChatGPT pueden citar respuestas directamente

## Schema JSON-LD Inyectado

```json
{
  "MedicalClinic": {
    "priceRange": "COP 8,000,000 - 11,000,000 / USD 3,500 - 4,500"
  },
  "FAQPage": {
    "mainEntity": [
      { "question": "¿Cuál es el costo...", "acceptedAnswer": "..." },
      ...
    ]
  }
}
```

## Implementación

**Método:** MCP Shopify GraphQL  
**Mutation:** `pageUpdate` (ID `154899317037`)  
**HTML:** 387 líneas + schema inline  
**Estado:** ✅ PUBLICADO 2026-06-25

**Archivos temporales generados:**
- `/tmp/PAGINA-PRECIOS-CONSOLIDADA.html` (387 líneas)
- `/Users/javierforero/skills/user/PAGINA-PRECIOS-INNOVART-EXPANDIDA-2026-06-25.md` (documento de trabajo)

## Impacto Esperado

| Métrica | Baseline | Target |
|---------|----------|--------|
| **GEO Score** | 38/100 | 46–52/100 |
| **Citas en IA** | 0% | 15–25% |
| **Show rate preguntas de precio** | Bajo | Medio–Alto |

## Próximos Pasos

1. **Validar en Rich Results Test** — https://search.google.com/test/rich-results
   - FAQPage debe aparecer como "eligible"
   - PriceRange debe validar
2. **Monitorar CTR en GSC** — Búsquedas de precio después de 1-2 semanas
3. **Completar Fase 3 AEO** — Video FAQ (en plan maestro, 0% avance)

## Referencias

- [[PLAN-MAESTRO-SEO-GEO-AEO-2026-06-25]] — Plan maestro SEO/GEO/AEO; Bloque de precios es Línea D
- [[restricciones-lenguaje]] — Términos PROHIBIDOS (p.ej., "Garantía Vitalicia")
- [[adn-comunicacion-innovart]] — ADN de marca (premium, navy+dorado, no venta de cabello)
