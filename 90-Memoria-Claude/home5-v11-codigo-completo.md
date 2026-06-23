---
name: home5-v11-codigo-completo
description: Código completo HOME5 v11 — HTML + CSS tema claro + JS tracking. Versión FINAL verificada en vivo (2026-06-21).
metadata:
  type: reference
---

# HOME5 v11 — Código Completo Verificado

**Estado:** ✅ EN VIVO en implantecapilarencolombia.com/home5  
**Fecha:** 2026-06-21  
**Pegado en:** GHL Custom Code (elemento de home5)  
**Resultado:** Render perfecto (localhost → GHL sin cambios)

## Componentes

- **HTML base:** estructura completa de la landing (hero, PASO 1/2/3, precios, form, footer)
- **CSS tema claro:** marfil #F9FAFB bg, navy #1A2E4A títulos, azul #3470A6 CTA, dorado #C9963D accento
- **JS tracking:** fbclid captura, Clarity, scroll depth, ViewForm, WhatsApp clicks, suavizaciones de claims
- **Form A/B:** `RB4a58CCebT51AOpuyPd` (nativo, no swap en caliente)
- **WhatsApp:** 310 (`573102031796`) en toda la página
- **Claims suavizadas:** "garantía vitalicia"→"garantía de resultado", "no duele"→"con anestesia local", etc.

## Guardado en Portapapeles

El código está almacenado en `/tmp/HOME5_COMPLETO_CON_CAPA.html` y fue pegado directamente en GHL.

**Para recuperar:**
```bash
cat /tmp/HOME5_COMPLETO_CON_CAPA.html | pbcopy
```

O leer desde `/tmp/HOME5_COMPLETO_CON_CAPA.html` si necesita inspeccionar.

## Cambios respecto a v10 (roto)

| Aspecto | v10 (roto) | v11 (OK) |
|---|---|---|
| Tema | Oscuro | Claro médico ✅ |
| Form | 6aGxlY1g (compartido) | RB4a58 (A/B) ✅ |
| WhatsApp | 573124565014 (equivocado) | 573102031796 (310 correcto) ✅ |
| Claims | Sin suavizar | Compliance ✅ |
| Colores | Negro | Marfil/navy/azul ✅ |

## Verificación (audit)

✅ 4.9★ + 6.000 procedimientos + 24 controles + 5 sedes  
✅ PASO 1/2/3 completos  
✅ Testimonios + before/after + FAQ  
✅ Precios ($8-11M)  
✅ Form fields (Nombre/Apellido/Teléfono/Email)  
✅ CTA principal + sticky bar  
✅ Pixel 1625645205284016 + Clarity x62cig8qug + CAPI Lead  
✅ Router ac1b818d → tags `lead_home5` + `landing_formulario` → 4.1 (Sofía)

## Próximos pasos

1. **Monitorear métricas:** lead_home5 vs landing_form_home4 por GHL tags
2. **Lanzar pauta A/B:** home5 vs home4 en Meta (mismos criterios)
3. **Comparar conversiones:** por 7-14 días → determinar ganador
4. **Opcional:** horneado final (CSS claro en fuente, no por capa) cuando home5 reemplace a home4

## Relacionado

[[home5-capa-optimizacion-cro]] (diseño/architecture)  
[[landing-home4-routing]] (form A/B setup)  
[[capi-webhook-worker]] (Lead server-side)

