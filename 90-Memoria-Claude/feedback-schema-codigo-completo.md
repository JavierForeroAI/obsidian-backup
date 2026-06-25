---
name: feedback-schema-codigo-completo
description: REGLA — siempre dar el bloque JSON-LD completo y listo para copiar-pegar, con todos los campos identificados (priceRange, aggregateRating, geo, hasMap, etc.). Nunca dar solo el fragmento a insertar.
metadata:
  type: feedback
---

# Dar siempre el JSON-LD completo para copiar-pegar

Cuando Javier necesite actualizar un bloque de schema (MedicalClinic, FAQPage, etc.), entregar **siempre el bloque completo** listo para borrar el anterior y pegar — no solo el fragmento a insertar.

**Por qué:** Insertar fragmentos en medio de JSON existente genera errores de comas duplicadas y es más lento. El flujo correcto es: borrar el HTML block en PageFly → pegar el nuevo completo.

**Cómo aplicar:** Incluir en el JSON todos los campos identificados como faltantes o mejorables en el Rich Results Test de Search Console:
- `aggregateRating` dentro de `MedicalClinic`
- `priceRange` con valor explícito en COP
- `geo` con coordenadas reales
- `hasMap` con URL de Google Maps
- `currenciesAccepted` y `paymentAccepted`

Relacionado: [[guia-replicacion-landings-ciudades]] · [[feedback-editor-landings-es-pagefly]]
