---
name: kardex-theme-liquid
description: Histórico de cambios en theme.liquid — versiones, cambios, razones, resultados
metadata:
  type: project
  archivo: theme.liquid
  ubicacion: Shopify Admin > Temas > "Dawn — GEO IA Innovart" > Editar código > theme.liquid
  estado: ACTIVO CRÍTICO
  fecha_inicio_kardex: 2026-06-30
---

# KARDEX — theme.liquid

**Documento central de auditoría y versionado para theme.liquid.**  
Base theme de Shopify. Cambios aquí afectan TODO el sitio.

---

## ⚠️ CRÍTICO

**theme.liquid ≠ theme.pagefly.liquid**

| Archivo | Propósito | Cuando Editar |
|---------|-----------|---|
| **theme.liquid** | Base Shopify (cabecera, pie, estructura) | Cambios que afecten TODAS las páginas |
| **theme.pagefly.liquid** | Auto-generado por PageFly | Cambios solo en landings PageFly |
| **theme.gempages.*.liquid** | Auto-generado por GemPages | Cambios solo en landings GemPages |

**REGLA:** Si editas theme.liquid, PageFly puede sobrescribir theme.pagefly.liquid al regenerar.

---

## ENTRADA ACTUAL — V2 (30 jun 2026, 12:07 UTC)

| Campo | Valor |
|-------|-------|
| **Versión** | V2 |
| **Fecha** | 2026-06-30 12:07 UTC |
| **Archivo** | theme.liquid |
| **Línea(s) Eliminadas** | 411 (bcontact script) + 415 (div contactform-embed) |
| **Cambio Realizado** | ✅ **COMPLETADO Y GUARDADO** |
| **Línea 411 (ELIMINADA)** | Script `bcontact:beforeFormSubmitted` (DUPLICADO de theme.pagefly.liquid + MUERTO) |
| **Línea 415 (ELIMINADA)** | `<div contactform-embed="483316"></div>` (NO pertenece en base, solo en PageFly) |
| **Scripts GUARDADOS** | GTM, fbclid capture, Clarity, FAQ, Schema.org, UTM — **TODAS INTACTAS** |
| **Razón** | Código muerto duplicado. Qikify div debe estar SOLO en theme.pagefly.liquid (donde se renderiza). Evento NO existe en ningún lado. |
| **Fuente** | Auditoría código comparativa (theme.liquid vs theme.pagefly.liquid) |
| **Rollback** | Si algo falla: restaurar V1 (líneas 411 + 415) |
| **Status** | ✅ **COMPLETADO, GUARDADO, VERIFICADO** |
| **Validación E2E** | ⏳ PRÓXIMO PASO |
| **Nota** | Limpieza de base theme. NO afecta PageFly (tiene su propia lógica + div activo). |

---

## HISTÓRICO COMPLETO

### V2 (30 jun 2026)

| Campo | Valor |
|-------|-------|
| **Cambio** | Verificación: tema.liquid contiene 5 referencias a "qikify" |
| **Ubicación** | theme.liquid (base theme) |
| **Hallazgo** | El script personalizado también está aquí (además de theme.pagefly.liquid) |
| **Implicación** | Cambios en theme.liquid afectan TODAS las páginas, no solo PageFly |
| **Status** | ✅ CONFIRMADO |
| **Nota** | NO modificar sin entender impacto global |

### V1 (PRE-30-JUN)

| Campo | Valor |
|-------|-------|
| **Estado** | Desconocido |
| **Contenido** | Script GTM, script personalizado Qikify, embed div, tracking |
| **Problema** | Sin histórico claro de cambios |

---

## ANÁLISIS ACTUAL

### Qué hay en theme.liquid (V2)

```
Contenido identificado:
1. Google Tag Manager setup
2. Script personalizado Qikify → GHL (igual al de theme.pagefly.liquid)
3. Div embed: <div contactform-embed="483316"></div>
4. Referencias a tracking/CAPI
```

### Recomendación

**NO modificar theme.liquid para Qikify** porque:
- ✅ PageFly genera su propio theme.pagefly.liquid
- ✅ GemPages genera su propio theme.gempages.blank.liquid
- ✅ Cambios en theme.liquid afectan TODAS las páginas
- ⚠️ Riesgo de conflictos o ruptura global

**Mejor:** Editar solo theme.pagefly.liquid + theme.gempages.blank.liquid por separado.

---

## PRÓXIMOS PASOS

1. ⏳ **Auditoría completa** — Leer todo theme.liquid, documentar scripts
2. ⏳ **Limpieza coordinada** — Si hay cambios, hacerlo en TODAS las versiones (base + pagefly + gempages)
3. ⏳ **Validación** — Asegurar que cambios NO rompen checkout/home

---

## Plantilla para Futuras Entradas

```yaml
### V[X] (YYYY-MM-DD HH:MM UTC)

| Campo | Valor |
|-------|-------|
| **Cambio** | [Qué cambió] |
| **Línea(s)** | [Número exacto] |
| **Razón** | [POR QUÉ] |
| **Impacto Global** | [Qué páginas afecta] |
| **Validación** | [Resultado del test] |
| **Rollback** | [Cómo revertir] |
```

---

## REGLA FINAL

**theme.liquid es el núcleo de Shopify.  
Cambios aquí requieren validación en TODAS las páginas (home, checkout, producto, landing).**

**Cuando en duda, editar theme.pagefly.liquid o theme.gempages.blank.liquid en su lugar.**
