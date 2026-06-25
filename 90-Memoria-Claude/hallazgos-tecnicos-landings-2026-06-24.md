---
name: hallazgos-tecnicos-landings-2026-06-24
description: Problemas técnicos detectados en 4 landings de ciudad (Bogotá/Medellín/Barranquilla/Bucaramanga) tras auditoría 24-jun — título basura, FAQPage duplicado, H1 incorrecto, falta meta description.
metadata:
  type: project
---

# Hallazgos Técnicos — Landings de Ciudad (2026-06-24)

**Auditoría realizada:** 24 de junio 2026 (en vivo con curl/Chrome)  
**Páginas:** `/implante-capilar-bogota`, `/implante-capilar-medellin`, `/implante-capilar-barranquilla`, `/implante-capilar-bucaramanga`

---

## Hallazgos por severidad

### 🔴 CRÍTICO — Bloquea ranking (las 4 páginas)

**C1: `<title>` Basura**
- **Problema:** Las tres renderizaciones en vivo sirven `<title>Ejemplo con .bcontact-field-help-text</title>` (×3 veces por página) en lugar del meta title real.
- **Causa:** Hay un bloque HTML/Liquid en PageFly que contiene un documento HTML **completo de ejemplo** (incluye `<!DOCTYPE html>`, `<html>`, `<head>`, `<title>` y `<style>` anidados dentro del `<body>`). Es HTML inválido.
- **Impacto:** Google toma ese `<title>` basura como el título de la página en SERP. El `og:title` SÍ es correcto.
- **Afecta:** Bogotá, Medellín, Barranquilla, Bucaramanga (se propagó al duplicar).
- **Fix:** En PageFly, encontrar el elemento **HTML/Liquid** que comienza con `<!DOCTYPE html>` y contiene `bcontact-field-help-text` → **Borrar el bloque completo.**
  - **Cómo validar tras arreglarlo:** En Chrome, clic derecho → "Ver código fuente" → Ctrl+F → `bcontact` (no debe encontrarse).

---

### 🔴 CRÍTICO — H1 de Escritorio (Bogotá, Medellín, Barranquilla, Bucaramanga)

**C2: H1 Incorrecto en Vista Escritorio**
- **Problema:** En vista de **escritorio**, el H1 sigue diciendo "Implante Capilar en **Bogotá**" incluso en Medellín/Barranquilla/Bucaramanga.
- **Causa:** PageFly edita escritorio y móvil por separado. El H1 móvil se cambió correctamente, pero el H1 de desktop quedó con la plantilla original de Bogotá.
- **Impacto:** Medium-High. El H1 es factor on-page importante; además, causa confusión.
- **Afecta:** Todas 4 ciudades (hecho en replicación).
- **Fix:** En PageFly, dentro del elemento de texto del H1 → cambiar "Bogotá" → nombre de ciudad correcta. Hacerlo en VISTA ESCRITORIO (click en ícono de monitor).

---

### 🟠 HIGH — FAQPage Duplicado (Medellín, Barranquilla)

**H1: FAQPage Duplicado — 2 Bloques**
- **Problema:** Medellín y Barranquilla tienen **2 bloques `FAQPage`** (uno incorrecto, uno correcto).
- **Causa:** El HTML #5 de PageFly renderiza un FAQPage JSON-LD manual; además, el snippet `faq-medellin.liquid` / `faq-barranquilla.liquid` inyecta otro FAQPage desde el theme. Resultado: Google indexa ambos → confusión de parser.
- **Impacto:** Medium. FAQPage sigue siendo válido en Google (aunque poco), pero la duplicación degrada calidad de datos estructurados.
- **Afecta:** Medellín, Barranquilla.
- **Fix:** En PageFly, dentro del **elemento HTML #5** de cada ciudad, **borrar el bloque `<script type="application/ld+json">` del FAQPage**. Dejar el HTML/Liquid vacío o eliminarlo. La fuente única queda en el snippet del theme.

---

### 🟠 HIGH — Meta Description Ausente (Medellín)

**H2: Medellín Sin Meta Description**
- **Problema:** `<meta name="description">` NO se renderiza en la página de Medellín (línea 104 en curl).
- **Causa:** El metafield `description_tag` estaba en `null` en Shopify (no fue configurado en el MCP GraphQL).
- **Impacto:** High. Google usa el meta desc como snippet en SERP; sin él, toma las primeras líneas del contenido (puede ser un párrafo incompleto).
- **Afecta:** Medellín.
- **Status:** ✅ **CORREGIDO el 24-jun** — Aplicado por MCP: `metafieldsSet` con valor `"Implante capilar FUE en Medellín: especialistas certificados, valoración gratuita, 24 controles postoperatorios y garantía de folículos. C.C. Oviedo."` (155 caracteres).

---

### 🟡 MEDIUM — aggregateRating Inconsistente

**M1: aggregateRating en Lugar Incorrecto**
- **Problema:** En Medellín y Barranquilla, el `aggregateRating` está dentro del FAQPage JSON-LD (inválido). Debería estar dentro del MedicalClinic schema o como campo aparte en la página.
- **Impacto:** Low-Medium. Google puede ignorar el rating si está mal ubicado.
- **Afecta:** Medellín, Barranquilla.
- **Fix:** Mover `aggregateRating` al metafield del MedicalClinic schema o asegurarse que esté al nivel correcto en el FAQPage (Google FAQ schema no soporta aggregateRating; solo Article, LocalBusiness, etc.).
- **Status:** Documentado; no ejecutado.

---

## Resumen Ejecución

| Ciudad | Título Basura | H1 Desktop | FAQPage Dup. | Meta Desc | aggregateRating |
|--------|---|---|---|---|---|
| Bogotá | 🔴 | 🔴 | ✅ | ✅ | ⚠️ |
| Medellín | 🔴 | 🔴 | 🔴 | ✅ (fijo) | 🔴 |
| Barranquilla | 🔴 | 🔴 | 🔴 | ✅ | 🔴 |
| Bucaramanga | 🔴 | 🔴 | ✅ | ✅ | ✅ |

---

## Plan de Corrección (Paso a Paso)

**Paso 1: Borrar `<title>` basura en las 4 ciudades**
1. Abrir cada landing en PageFly
2. Buscar el elemento que contiene `<!DOCTYPE html>` (usa Vista Previa / Inspector de elementos)
3. Borrar el bloque completo
4. Publicar

**Paso 2: Fijar H1 en escritorio (las 4 ciudades)**
1. En PageFly, cambiar vista a **Escritorio** (ícono de monitor)
2. Editar el H1 → cambiar "Bogotá" → ciudad correcta
3. Publicar

**Paso 3: Borrar FAQPage duplicado (Medellín, Barranquilla)**
1. En PageFly, buscar HTML #5
2. Dentro, localizar `<script type="application/ld+json">` del FAQPage
3. Borrar ese bloque
4. Publicar

**Paso 4: Validar**
- Ejecutar en terminal: `curl -s https://www.innovartmedical.com/pages/implante-capilar-[ciudad] | grep -i "title\|description\|faqpage" | head -20`
- Validar en [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## Aplicación a Futuras Ciudades

Cuando se creen nuevas landings de ciudad:
1. ✅ Usar PageFly como editor (confirmado, NO GemPages)
2. ✅ Borrar bloque HTML de ejemplo ANTES de publicar
3. ✅ Cambiar H1 en AMBAS vistas (desktop + móvil)
4. ✅ No duplicar FAQPage (una sola fuente: theme snippet)
5. ✅ Verificar meta description en Shopify Admin

---

## Referencias
- [[trabajo-geo-ia-refinements-2026-06-24]] — Fase 1-2 GEO/IA schema (MedicalClinic inyectado)
- [[guia-replicacion-landings-ciudades]] — Plantilla original
- [[landing-ciudades-plantilla-checklist-2026-06-20]] — Checklist pre-publicación (necesita actualizar con estos fixes)
