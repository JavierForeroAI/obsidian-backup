---
name: proyecto-5-landings-homeinnovart
description: Proyecto ejecutar 5 landings HomeInnovart1-5 con A/B testing — 5 ángulos creativos, 9/10+ conversión (2026-06-23)
metadata:
  type: project
---

## Proyecto: 5 Landings HomeInnovart1-5 — A/B Testing Masivo (2026-06-23)

**Estado:** ✅ WORKFLOW COMPLETADO (2026-06-23 ~19:00) — Parcialmente desplegado en GHL

**Resultado del workflow:** 21 agentes · 1,324,409 tokens subagente · 30 min · Todas las 5 landings: score 9+/10

**Estado de despliegue en GHL (location Bogotá `DgjjDzD9nkCKv8AGF1Qb`, funnel `lbcmC7s6MV3eZIzZLzcD`):**
- HomeInnovart3 (Garantía): **PUBLICADA** — page ID `7XEARfp2qZwShMLVmQm5`
- HomeInnovart5 (Comunidad): **PUBLICADA** — page ID `tCIJkENhzssc7gTT74ja`
- HomeInnovart1, 2, 4: usuario interrumpió inyección (página en builder sin contenido HTML real en GHL)
- HTMLs fuente disponibles en Desktop: `/Users/javierforero/Desktop/HomeInnovart1.html` … `HomeInnovart5.html`

**Pendiente para completar despliegue:**
- Inyectar HTML en HomeInnovart1, 2, 4 vía MCP (payloads disponibles en la siguiente sesión)
- Enviar correo a Esneider con instrucciones Meta Ads

**Objetivo:** Crear 5 variantes de landing basadas en `/home`, cada una con ángulo creativo distinto, todas 9/10+ en rubros clave (conversión, tracking, design, copy, compliance).

**Los 5 Ángulos Creativos:**

1. **HomeInnovart1** — AUTORIDAD MÉDICA
   - Hero: Dr. Carreño como autoridad
   - Copy: Protocolo FUE/DHI, certificaciones, ciencia comprobada
   - Social proof: Credenciales médicas, publicaciones

2. **HomeInnovart2** — TRANSFORMACIÓN VISUAL
   - Hero: Antes/después épicos (galería impactante)
   - Copy: "Mira lo que es posible"
   - Social proof: Casos de éxito con fotos

3. **HomeInnovart3** — GARANTÍA + CERO RIESGO
   - Hero: Protección total, dinero-atrás, satisfacción 100%
   - Copy: "Sin compromiso, sin riesgo"
   - Social proof: Testimonio de persona quien recibió garantía

4. **HomeInnovart4** — URGENCIA + ESCASEZ
   - Hero: "Solo 20 valoraciones/mes" (cupo limitado)
   - Copy: Countdown, FOMO controlado
   - Social proof: "Sólo 3 espacios disponibles"

5. **HomeInnovart5** — COMUNIDAD + SOCIAL PROOF
   - Hero: Testimonios reales, casos de éxito
   - Copy: "Ellos lo hicieron, tú también"
   - Social proof: Reseñas Google, comunidad, video testimonios

**Requisitos Técnicos (TODAS):**
- ✅ 9/10+ en: conversión, tracking, design, copy, compliance
- ✅ Pixel Meta `1625645205284016` instalado
- ✅ fbclid capture script + router `fbd5387a`
- ✅ Formulario con campo email (requerido)
- ✅ Schema JSON-LD + E-E-A-T (Dr. Carreño)
- ✅ Sticky CTA + WhatsApp +57 312 456 5014
- ✅ Mobile-first responsive
- ✅ Clarity integrado para tracking

**Arquitectura de Agentes (18 especialistas):**

**TIER 1 — Análisis (3 agentes)**
- `creative-strategist` → estrategia avatares, M4 funnel
- `/market audit` → análisis prospección, positioning
- `meta-medical-auditor` → compliance médica, tracking

**TIER 2 — Diseño (5 agentes)**
- `/ui-ux-pro-max` → UI/UX visual, responsiveness
- `visual-designer` → assets gráficos, palettes
- `format-adapter` → validación specs imágenes
- `Explore` → investigación referencias (Dharma Hair, Ileanovo, DHI)
- `Plan` → arquitecto HTML/Liquid/PageFly

**TIER 3 — Copy (4 agentes)**
- `/copy-writer` → headlines, CTAs, compliance
- `creative-strategist` (2ª pasada) → objeciones por avatar
- `medical-compliance-copy` → restricciones de lenguaje
- `/market copy` → A/B copy variants

**TIER 4 — Conversión (3 agentes)**
- Form friction audit → placement, conversión funnel
- `audit-tracking` → fbclid, CAPI, UTMs, Google Ads
- `capi-revenue-orchestrator` → CAPI training, EMQ

**Entregables esperados:**
- 5 HTML completos (prototipo + listo Shopify/PageFly)
- 5 conjuntos de assets gráficos + brand guidelines
- 5 planes A/B testing con hipótesis
- Correo a Esneider con instrucciones Meta Ads
- Reportes de QA por landing

**Correo a Esneider:**
- Enviar a: `esneidervc17@gmail.com` (confirmar si es correcta)
- Contenido: instrucciones Meta Ads completas para las 5 landings
- Timeline: Mañana 6-8 AM (2026-06-24)

**Próximos pasos:**
1. Confirmar email Esneider (¿esneider@innovartmedical.com o esneidervc17@gmail.com?)
2. Lanzar workflow de 18 agentes en paralelo
3. Monitorear en `/workflows`

**Notas:**
- Meta Pixel y fbclid = se reutilizan de `/home` (MISMO código en todas)
- UTMs: aplicar la plantilla estándar `[[metodo-carga-utms-api-meta]]`
- Compliance: verificar contra `[[restricciones-lenguaje]]` + `[[adn-comunicacion-innovart]]`

**Referencias:**
- [[landing-home-nueva-url-2026-06-23]]
- [[Informe-Clarity-home4-2026-06-18.html]]
- [[adn-comunicacion-innovart]]
- [[restricciones-lenguaje]]
