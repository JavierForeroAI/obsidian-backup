---
name: landing-home-nueva-url
description: Landing /home reemplaza home4/home5 — nueva URL base con fbclid confirmado funcional (2026-06-23)
metadata:
  type: project
---

## Landing `/home` — Nueva URL Base (2026-06-23)

**Estado:** LIVE, reemplazando home4/home5 eliminadas

**Configuración técnica confirmada:**
- **URL:** `implantecapilarencolombia.com/home` (cambio de URL no afecta fbclid capture)
- **Pixel Meta:** `1625645205284016` (instalado ✅)
- **fbclid Capture:** Script funcional ✅ — test confirmó `[FbclidCapture] Captured: IwAR_TEST_123456`
- **Router GHL:** `fbd5387a` (activo, publica tags, dispara flujos)
- **Formulario:** Requiere auditoría (leads reales sin email — solo teléfono)

**Problemas identificados (Clarity 2026-06-22):**
- Bounce rate móvil: 98.76% 🚨
- Scroll depth promedio: 14.39% (form enterrado al fondo)
- Errores JS Android: 86
- Sesiones sin interacción: 86%

**Próximos pasos:**
1. Verificar si formulario tiene campo email (leads actuales 0% con email, solo teléfono)
2. Auditoría lado a lado: `/home` vs histórico home4 (tracking, flujos, tags)
3. Rerun Clarity post-fixes (target: bounce <70%, scroll >30%)

**Nota:** fbclid **FUNCIONA CORRECTAMENTE** en `/home`. El cuello de botella es EMAIL = 0 en leads reales (bloquea EMQ).

**Links relacionados:** 
- [[fbclid-home-implementacion-exitosa-2026-06-22]]
- [[Informe-Clarity-home4-2026-06-18.html]]
- [[protocolo-validacion-landing-automatica]]
