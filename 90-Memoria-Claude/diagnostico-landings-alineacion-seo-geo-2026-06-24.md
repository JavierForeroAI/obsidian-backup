---
name: diagnostico-landings-alineacion-seo-geo-2026-06-24
description: Auditoría completa Bogotá/Medellín/Barranquilla/Bucaramanga — alineación con flujo SEO/GEO, qué está bien, qué está mal, paso-a-paso remediación con fundamentos técnicos.
metadata:
  type: project
---

# Diagnóstico — Alineación SEO/GEO Landings de Ciudad (2026-06-24)

**Objetivo:** Validar que las 4 landings de ciudad cumplan estándar SEO/GEO esperado y detectar qué las saca del flujo  
**Auditoría:** En vivo + crawl Apify (24-jun)  
**Impacto:** GEO Score 38/100 → regresión observable en recuperación IA (invisible no-branded)

---

## Estado General

| Check | Bogotá | Medellín | Barranquilla | Bucaramanga | Expect. |
|---|---|---|---|---|---|
| HTTP 200 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Canonical | ✅ | ✅ | ✅ | ✅ | ✅ |
| `<title>` | 🔴 | 🔴 | 🔴 | 🔴 | ✅ |
| Meta description | ✅ | ✅ (ahora) | ✅ | ✅ | ✅ |
| H1 | 🔴 (desktop) | 🔴 (desktop) | 🔴 (desktop) | 🔴 (desktop) | ✅ |
| Schema MedicalClinic | ✅ | ✅ | ✅ | ✅ | ✅ |
| FAQPage | ✅ | 🔴 (dup) | 🔴 (dup) | ✅ | ✅ |
| aggregateRating | 🔴 (absent) | 🔴 (bad loc) | ✅ | ✅ | ✅ |
| Compliance | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Diagnóstico por Hallazgo

### 🔴 P0 — `<title>` Basura (todas 4)

**Qué es:** Cada página renderiza `<title>Ejemplo con .bcontact-field-help-text</title>` (×3) en lugar de meta title real.

**Por qué es crítico:**
- `<title>` es la **señal on-page #1** para ranking en Google y el texto que aparece en SERP como título de resultado
- Hoy le estás diciendo a Google que la página se titula "Ejemplo..." en lugar de "Implante Capilar FUE en [Ciudad]"
- Además, ese bloque HTML de ejemplo mete `<!DOCTYPE>`, `<html>`, `<head>`, `<style>` anidados en el `<body>` → **HTML inválido** que degrada parsing del crawler
- El `og:title` SÍ está correcto, pero ese solo sirve para previews de redes sociales, no para ranking

**Cómo arreglarlo:**
1. En PageFly, encontrar el elemento que contiene `<!DOCTYPE html>` (usa Inspector o Vista Previa)
2. **Borrar el bloque completo**
3. Publicar en Shopify
4. Validar: `curl -s https://www.innovartmedical.com/pages/implante-capilar-[ciudad] | grep '<title>'` — debe mostrar SOLO UNA línea con el título real

**Impacto esperado:** +5-10 posiciones en SERP para keywords de ciudad (si todo lo demás está OK)

---

### 🔴 P0 — H1 Incorrecto en Escritorio (todas 4)

**Qué es:** En vista escritorio, el H1 sigue diciendo "Implante Capilar en Bogotá" incluso en Medellín/Barranquilla/Bucaramanga.

**Por qué es crítico:**
- H1 es el **segundo factor on-page** después del `<title>` para Google
- Además, causa confusión para el usuario (llega a landing de Medellín y ve "Bogotá" en el H1)
- Riesgo de contenido duplicado percibido (4 páginas con H1 "Bogotá")

**Causa raíz:**
- PageFly edita **escritorio y móvil por separado**
- El H1 móvil FUE cambiado correctamente en Medellín/Barranquilla/Bucaramanga
- El H1 de desktop quedó sin cambiar → sigue plantilla original

**Cómo arreglarlo:**
1. En PageFly, abrir la landing de la ciudad
2. **Cambiar vista a Escritorio** (ícono de monitor, no móvil)
3. Editar el elemento de texto H1 → cambiar "Bogotá" → nombre de ciudad
4. Publicar
5. Validar en vivo y en vista escritorio (F12 Inspector, cambiar UA a desktop)

**Impacto esperado:** Pequeño directo (+1-2%), pero crítico para user experience y para no perder "fresh content" signal (Google ve cambios)

---

### 🟠 P1 — FAQPage Duplicado (Medellín, Barranquilla)

**Qué es:** Dos bloques `FAQPage` JSON-LD en la misma página.

**Por qué es problema:**
- Google puede ignorar o malinterpretar datos estructurados duplicados
- Aumenta "noise" en el parsing del schema
- Cada FAQPage agrega latencia de parseo

**Causa raíz:**
- El HTML #5 de PageFly renderiza un FAQPage JSON-LD manual
- El snippet `faq-medellin.liquid` / `faq-barranquilla.liquid` (theme.liquid) inyecta otro FAQPage
- Resultado: 2 bloques `"@type": "FAQPage"` en la página

**Cómo arreglarlo:**
1. En PageFly, abrir elemento HTML #5
2. Buscar `<script type="application/ld+json">` dentro
3. Borrar TODO lo que está adentro de ese `<script>` (o eliminar el script completo si está vacío)
4. Dejar la fuente única en el theme snippet
5. Publicar

**Impacto esperado:** +1-2% en claridad de schema para Google (Rich Results mejor)

---

### 🟠 P1 — aggregateRating Inconsistente (Medellín, Barranquilla)

**Qué es:** El `aggregateRating` (calificación 4.8/37, 5.0/25) está DENTRO del FAQPage JSON-LD (donde no debe estar).

**Por qué es problema:**
- FAQPage schema NO soporta `aggregateRating` como propiedad válida
- Google puede ignorar el rating o marcarlo como "propiedades no esperadas"
- Además, el agregateRating es del MedicalClinic (la clínica completa), no de una FAQ

**Cómo arreglarlo:**
- Mover `aggregateRating` al nivel correcto: **dentro del MedicalClinic schema** (que SÍ está en la página)
- O crear un bloque aparte para el rating si no forma parte de MedicalClinic
- Validar que Bogotá y Bucaramanga tengan el rating en el lugar correcto (revisa su JSON)

**Impacto esperado:** +2-5% en Rich Results (Google mostrará la calificación en SERP si está correcta)

---

### 🟡 P2 — Meta Description Ausente (Medellín)

**Qué es:** La página de Medellín no tenía `<meta name="description">` renderizada.

**Status:** ✅ **CORREGIDO el 24-jun por MCP GraphQL** — metafield `description_tag` poblado con descripción médica de 155 caracteres.

**Impacto:** Ya resuelto.

---

## Resumen Ejecutivo

### Qué está BIEN
- ✅ HTTP 200 en todas
- ✅ Canonical correcto
- ✅ Meta descriptions presentes (ahora)
- ✅ MedicalClinic schema inyectado
- ✅ FAQPage en Bogotá y Bucaramanga (no duplicado)
- ✅ aggregateRating en Bogotá y Bucaramanga (ubicación correcta)
- ✅ Compliance: sin "garantía vitalicia", sin "resultado garantizado"
- ✅ Direcc iones locales correctas + teléfonos locales

### Qué está MAL (Orden de Urgencia)
1. **`<title>` basura (todas 4)** — P0, bloquea ranking
2. **H1 desktop incorrecto (todas 4)** — P0, user experience + fresh signal
3. **FAQPage duplicado (Medellín, Barranquilla)** — P1, degrada schema clarity
4. **aggregateRating mal ubicado (Medellín, Barranquilla)** — P1, pierde Rich Results

---

## Plan de Corrección (Ejecución Step-by-Step)

### LOTE 1: Bogotá (la plantilla)
**Duración:** ~20 min

1. Abrir `/implante-capilar-bogota` en PageFly editor
2. Encontrar el bloque HTML con `<!DOCTYPE html>` → **Borrar**
3. Cambiar vista a Escritorio
4. Verificar H1 dice "Implante Capilar en Bogotá" (debe estar OK)
5. Publicar
6. Validar: `curl -s https://www.innovartmedical.com/pages/implante-capilar-bogota | grep '<title>' | wc -l` → debe retornar 1 línea

### LOTE 2: Medellín (duplicada de Bogotá, más fixes)
**Duración:** ~25 min

1. Abrir `/implante-capilar-medellin` en PageFly
2. Borrar bloque HTML con `<!DOCTYPE html>`
3. Cambiar vista a Escritorio → cambiar H1 "Bogotá" → "Medellín"
4. Ir a HTML #5 → borrar FAQPage JSON-LD adentro
5. Validar aggregateRating está en MedicalClinic schema (no en FAQPage)
6. Publicar
7. Validar

### LOTE 3: Barranquilla (igual que Medellín)
**Duración:** ~25 min

1. Abrir `/implante-capilar-barranquilla` en PageFly
2. Mismo proceso que Medellín

### LOTE 4: Bucaramanga (casi OK, solo `<title>` + H1)
**Duración:** ~15 min

1. Abrir `/implante-capilar-bucaramanga` en PageFly
2. Borrar bloque HTML
3. Cambiar vista Escritorio → H1 debe decir "Implante Capilar en Bucaramanga" (es nueva, debería estar OK)
4. Publicar

---

## Validación Post-Fix

Ejecutar en terminal después de cada ciudad:

```bash
url="https://www.innovartmedical.com/pages/implante-capilar-[ciudad]"
echo "=== $url ==="
echo "Titles:"
curl -s "$url" | grep '<title>' | wc -l
echo "—— (debe ser 1)"
echo "Meta description:"
curl -s "$url" | grep -o '<meta name="description"[^>]*>' | head -1
echo "—— (debe estar presente)"
echo "FAQPage count:"
curl -s "$url" | grep -o '"@type":"FAQPage"' | wc -l
echo "—— (debe ser 1)"
```

---

## Impacto Esperado en GEO Score

Hoy: **38/100** (invisible no-branded)

Esperado post-fixes:
- `<title>` correcto: +3-5 puntos
- H1 correcto: +2-3 puntos
- Schema limpio (FAQPage): +1-2 puntos
- Total esperado: **44-49/100** (aún no suficiente para ser citado por IA, pero mejora significativa)

Esto sigue siendo bloqueado por:
- **Doctoralia 0** (sin credibilidad médica verificada)
- **Listicles 0** (sin menciones de terceros)
- **Google Maps <10 reseñas** (sin social proof)

Pero el schema limpio sí te pone en posición para que cuando esos bloqueantes se resuelvan, el Knowledge Graph ya esté listo.

---

## Referencias

- [[hallazgos-tecnicos-landings-2026-06-24]] — Especificaciones técnicas completas de cada hallazgo
- [[proyecto-landing-cities-seo-geo-completo]] — Antecedente: Fase 1 completada
- [[guia-replicacion-landings-ciudades]] — Plantilla de replicación
- [[geo-auditoria-junio24-2026]] — Contexto GEO Score 38/100
