---
name: shopify-alt-text-home-panama
description: Inspección de alt text de las imágenes del Home (PageFly) y Panamá (GemPages) — dónde viven, si se pueden editar por MCP, y deck de alt corregidos para el Home
metadata:
  type: project
---

# Alt text — Home + Panamá (inspección Fase 2)

**Fecha:** 2026-06-19. Base técnica: [[shopify-ecosistema-mcp]].

## Dónde vive cada alt
- **HOME** = PageFly. HTML horneado en `sections/pagefly-home.liquid` (~72KB, theme MAIN). **30 `<img>`**, todas en `cdn.shopify.com`, el `alt` es **texto literal** dentro del `<img>`. 29 con alt, **1 vacío**, varios **corruptos**.
- **PANAMÁ** = GemPages. JSON `page.gp-template-553417332983071906.json` referencia **14 secciones** `sections/gp-section-<id>.liquid`. El `alt` NO es literal: es variable Liquid `{{ section.settings.ggXXXX_alt }}`. **Los VALORES (19) están guardados como settings dentro del template JSON**, todos llenos y bien optimizados (SEO + Panamá-específico). Imágenes en mix `cdn.shopify.com` + `assets.gemcommerce.com` + `ucarecdn.com` + video Wistia.

## ⚠️ Veredicto: ¿puedo cambiar los alt por MCP? → NO automáticamente
Dos bloqueos REALES y verificados:
1. Ambos archivos viven en el theme **MAIN/live** → el MCP **bloquea `themeFilesUpsert` al theme publicado** (sólo unpublished).
2. PageFly y GemPages **sobrescriben** esos archivos al publicar desde su editor (auto-generated).
3. Bonus: en el Home las imágenes son `cdn.shopify.com`, pero PageFly renderiza su PROPIO `alt` literal (no el del `MediaImage`), así que `fileUpdate` sobre el File NO cambiaría lo que se ve. Ruta inútil para alt renderizado.

**Rutas que SÍ funcionan:**
- Home → editor **PageFly** (campo Alt por imagen).
- Panamá → editor **GemPages** (campo Alt por imagen = un setting `ggXXX_alt`). ⚠️ Los 19 settings están llenos, PERO la página **en vivo** tiene **20 `<img>` sin alt** (de 39 totales) → ver "Estado Panamá" abajo.
- (Opcional avanzado) duplicar a theme unpublished, editar, publicar desde admin — frágil porque la app lo regenera.

## Estado Home (lo que urge corregir) — 7 alt rotos/vacíos
| # | Archivo | Alt actual (roto) | Alt corregido propuesto |
|---|---|---|---|
| 1 | VideodeWhatsApp...gif-to-webp.webp | `VideodeWhatsApp2025-05-28...webp__PID:48b3...` | Animación de resultados de implante capilar FUE — Innovart Medical Colombia |
| 3 | (misma webp) | idem nombre de archivo crudo | Animación de resultados de implante capilar FUE — Innovart Medical Colombia |
| 5 | (misma webp) | idem nombre de archivo crudo | Animación de resultados de implante capilar FUE — Innovart Medical Colombia |
| 6 | 01_LANDING-CAPILAR-_01-min.webp | (vacío) | Implante capilar en Colombia - Antes y después - Innovart Medical IPS |
| 13 | Imagen_4_Innovart_Desplazable.webp | `ClínicServicio de implante...IPSa de implante...` (empalme) | Clínica de implante capilar en Colombia — Innovart Medical IPS |
| 23 | implante_capilar_en_colombia.webp | `implante capResultados...Medicalilar en colombia .webp__PID...` (empalme) | Resultados reales de implante capilar FUE en Colombia - Innovart Medical |
| 26 | Ultima_imagen_Innovart-min.webp | `Ultima imagen Innovart-min.webp__PID:d815...` | Sedes y horarios de atención — Innovart Medical Colombia y Panamá |

Las otras ~23 imágenes del Home ya tienen alt aceptable (descriptivo + marca + ubicación). Patrón a mantener: `<qué muestra> + implante capilar FUE/DHI + Colombia/Panamá + Innovart Medical`.

## Estado Panamá (inspección EN VIVO 2026-06-19)
La página de Panamá renderiza **39 `<img>`**: 19 con alt + **20 con `alt=""`** (verificado en vivo por `curl` + cruce de hashes 2026-06-19).

**Conteo según reporte SEO (3 niveles):**
- **Crudo (lo que marca un crawler tipo Screaming Frog/Ahrefs):** **20 imágenes** con alt faltante.
- **Identidades únicas detrás de esas 20:** 14 (el resto son repeticiones). De ellas → **3 son duplicados responsive** que YA tienen alt en otro breakpoint (`610d956e`, `16846378`, `01d30060`), **1 es un SVG decorativo** repetido 4× (alt vacío es lo correcto), y **1 es un placeholder de `ucarecdn` repetido 4×** (imagen ajena a Innovart → reemplazar, no poner alt).
- **Accionable real (fotos de contenido sin alt en ningún lado):** **~10 imágenes únicas** flageadas; de éstas, por revisión visual ~**6 son fotos reales** que necesitan alt descriptivo (las otras parecen gráficos de plantilla/decorativos — confirmar viéndolas).

Detalle del split contenido/decorativo (requiere ver las imágenes):

**🟢 Las 6 fotos que SÍ necesitan alt (texto en español, compliant, listo para pegar en GemPages):**
| Qué es | Alt |
|---|---|
| Banner arriba: médico + 2 pacientes | `Médico y pacientes de Innovart Medical tras un implante capilar con técnica FUE en Panamá` |
| Banner "¡Recupera tu confianza!" (valoración) | `Valoración gratis de implante capilar en Panamá — Innovart Medical` |
| Antes/después paciente 1 | `Antes y después de un implante capilar FUE en Innovart Medical Panamá` |
| Antes/después paciente con tapabocas | `Resultado de implante capilar FUE — paciente antes y después, Innovart Medical Panamá` |
| Antes/después paciente 3 | `Recuperación de densidad capilar con técnica FUE — antes y después, Innovart Medical` |
| Antes/después paciente 4 | `Antes y después de trasplante capilar en hombre — Innovart Medical Panamá` |

**🔴 Hallazgo importante — 4 fotos de BOLSOS de cuero (no es alt, es un error a corregir):** en la sección de beneficios (GARANTÍA / TERAPIAS / RESULTADOS EN 6 MESES…) hay una foto stock de **bolsos de cuero repetida 4×**, placeholder que quedó de la plantilla GemPages y nunca se reemplazó. En una clínica capilar es un **problema de credibilidad** → **reemplazar o quitar**, no ponerle alt.

**⚪ 10 imágenes decorativas → alt vacío es lo CORRECTO (no tocar):** 6 = números de los pasos (1-5) + 4 = pin de ubicación de sedes. Ponerles alt con keywords sería spam.

> Panamá ya tiene **H1 bueno** ("Llegaste a la mejor clínica de implante capilar en Panamá") y **no usa "garantía vitalicia"** → compliant. (En cambio el Home SÍ tiene "garantía vitalicia" 2× → corregir al tocar el texto, [[restricciones-lenguaje]].)

## Causa raíz probable
Los alt corruptos (texto empalmado dentro de otro, p.ej. "Clínic"+frase+"a de...") son de **ediciones manuales previas en PageFly** mal pegadas. Revisar el editor con cuidado al corregir.

## Pendiente / próximo paso
- [ ] Aplicar los 7 alt corregidos del Home en el editor de PageFly.
- [ ] (Bajo) Confirmar 1 `<img>` del Home sin alt distinto al #6 si aparece.
- [ ] Panamá: pegar los **6 alt** (tabla arriba) en GemPages.
- [ ] Panamá: **reemplazar/quitar las 4 fotos de bolsos** de la sección de beneficios (credibilidad).
- [ ] Home: quitar "garantía vitalicia" (2×) al editar el texto.

Relacionado: [[shopify-ecosistema-mcp]] · [[seo-plan-shopify-2026-05]] · [[restricciones-lenguaje]] (compliance médico al redactar alt)
