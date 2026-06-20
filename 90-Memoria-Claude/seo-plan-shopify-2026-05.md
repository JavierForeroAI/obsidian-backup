---
name: seo-plan-shopify-2026-05
description: Plan completo de mejoras SEO para innovartmedical.com en Shopify — auditoría Mayo 2026, 17 acciones automáticas + 8 parciales + 5 manuales
metadata:
  type: project
  fecha: 2026-05-27
  fuente: Auditoría SEO Mayo 2026
  estado: pendiente-ejecucion
---

# Plan de Mejoras SEO — Innovart Medical Shopify
**Sitio:** [www.innovartmedical.com](https://www.innovartmedical.com)
**Fecha auditoría:** Mayo 2026
**Problema central:** Solo 5-6 páginas indexadas en Google. Competidores tienen 50-200+.

> ⚠️ **DESACTUALIZADO (compliance):** varias meta descriptions y títulos de abajo usan
> **"garantía vitalicia"**, hoy **término prohibido** ([[restricciones-lenguaje]], [[angulos-creativos]]).
> Reemplazar por "garantía de resultado" antes de ejecutar. Versión más ambiciosa y al día:
> [[seo-puro-seo-cowork]] (proyecto "PURO SEO" de COWORK).

## Contexto del problema
- Cero páginas de ciudad indexadas (Bogotá, Medellín, Barranquilla, Bucaramanga)
- Títulos SEO genéricos en páginas existentes ("/pages/barberia" → título solo "Barberia")
- Meta descriptions duplicadas en múltiples páginas (copia exacta del homepage)
- Sin blog → cero tráfico informacional
- Sin schema markup → sin rich snippets en Google
- Sin Google Search Console configurado

---

## CLASIFICACIÓN DE ACCIONES

| Tipo | Cantidad | Descripción |
|------|----------|-------------|
| AUTOMATICO | 17 | Claude las ejecuta vía API Shopify sin intervención |
| PARCIAL | 8 | Claude genera contenido/código, Javier lo inserta |
| MANUAL | 5 | Equipo o desarrollador de Innovart las hace |

---

## 1. CORRECCIONES ON-PAGE (páginas existentes)

### /pages/barberia
- **Título actual:** "Barberia"
- **Título nuevo:** `Implante Capilar desde tu Barberia | Innovart Medical Colombia`
- **Meta description nueva:** `Tu barbero de confianza puede ser el primer paso hacia recuperar tu cabello. Innovart Medical ofrece implante capilar FUE con garantia vitalicia y 24 controles. Valoracion gratis. Sedes en Bogota, Medellin, Barranquilla, Bucaramanga y Panama.`
- **Tipo:** AUTOMATICO | Impacto: ALTO

### /pages/panama
- **Título nuevo:** `Implante Capilar en Panama | Innovart Medical - Tecnica FUE Garantia Vitalicia`
- **Meta description nueva:** `La mejor clinica de implante capilar en Panama. Tecnica FUE foliculo a foliculo, valoracion gratis, garantia vitalicia y 24 controles postoperatorios incluidos. Costa del Este, Ciudad de Panama. Agenda tu cita hoy.`
- **Tipo:** AUTOMATICO | Impacto: ALTO

### /pages/financiacion
- **Título nuevo:** `Financiacion para Implante Capilar en Colombia | Innovart Medical`
- **Meta description nueva:** `Financia tu implante capilar con Innovart Medical. Aprobacion en menos de 5 minutos, hasta el 90% del costo financiado y tasas mas bajas que tarjeta de credito. Recupera tu cabello sin preocuparte por el presupuesto.`
- **Tipo:** AUTOMATICO | Impacto: ALTO

### Duplicado política de cancelación
- Dos URLs distintas generan contenido duplicado
- Identificar URL correcta (Claude) → redirect 301 en Shopify Admin (Javier)
- **Tipo:** PARCIAL | Impacto: MEDIO

---

## 2. NUEVAS LANDING PAGES DE CIUDAD

Estructura estándar de cada landing page:
1. H1: "Implante Capilar en [Ciudad]: Técnica FUE con Garantía Vitalicia"
2. Introducción: Por qué Innovart es la mejor opción en [Ciudad]
3. Qué incluye el procedimiento (FUE, zona donante, 24 controles)
4. Información de sede local: dirección, horarios, mapa
5. Por qué elegir Innovart vs. otras clínicas
6. 3-5 testimonios de pacientes de esa ciudad
7. Preguntas frecuentes específicas de esa ciudad
8. CTA: Botón WhatsApp + Formulario valoración gratuita

| URL | Sede | Tipo | Impacto |
|-----|------|------|---------|
| `/pages/implante-capilar-bogota` | Sede Bogotá | AUTOMATICO | MUY ALTO |
| `/pages/implante-capilar-medellin` | CC Oviedo | AUTOMATICO | MUY ALTO |
| `/pages/implante-capilar-barranquilla` | Green Tower | AUTOMATICO | ALTO |
| `/pages/implante-capilar-bucaramanga` | HIC | AUTOMATICO | ALTO |

---

## 3. NUEVAS PÁGINAS DE SERVICIO

| URL | Keyword objetivo | Tipo | Impacto |
|-----|-----------------|------|---------|
| `/pages/implante-de-barba` | "implante de barba Colombia" | AUTOMATICO | ALTO |
| `/pages/implante-de-cejas` | "implante de cejas Colombia" | AUTOMATICO | ALTO |
| `/pages/terapias-capilares` | "terapias capilares Bogota/Colombia" | AUTOMATICO | MEDIO |
| `/pages/precios` | "cuanto cuesta implante capilar Colombia" | AUTOMATICO | MUY ALTO |
| `/pages/resultados` | Google Imágenes tráfico estético | PARCIAL (Javier sube fotos) | ALTO |

---

## 4. BLOG — ARTÍCULOS SEO

Blog a crear: **"Guía Capilar"**

| Artículo | Keyword | Tipo | Impacto |
|----------|---------|------|---------|
| Cuánto cuesta implante capilar en Colombia 2026 | "cuanto cuesta implante capilar Colombia" | AUTOMATICO | MUY ALTO |
| Implante capilar FUE vs DHI: ¿Cuál es mejor para ti? | "FUE vs DHI Colombia" | AUTOMATICO | ALTO |
| Por qué la garantía vitalicia marca la diferencia | "garantia vitalicia implante capilar" | AUTOMATICO | ALTO |
| Cuidados postoperatorios del implante capilar | "cuidados despues de implante capilar" | AUTOMATICO | ALTO |
| Implante capilar para mujeres en Colombia | "implante capilar mujeres Colombia" | AUTOMATICO | MEDIO |
| Resultados del implante capilar: qué esperar mes a mes | "evolucion implante capilar Colombia" | AUTOMATICO | MEDIO |

---

## 5. SCHEMA MARKUP (requiere inserción en tema)

| Schema | Beneficio | Tipo | Impacto |
|--------|-----------|------|---------|
| FAQ Schema | Rich snippets en SERP (ocupa más espacio) | PARCIAL | ALTO |
| LocalBusiness (6 sedes) | Google Maps y búsquedas locales | PARCIAL | ALTO |
| MedicalClinic | Knowledge Panel de Google | PARCIAL | ALTO |
| BreadcrumbList | Mejora CTR en resultados | PARCIAL | MEDIO |

**Opciones de inserción:**
- **App (recomendada):** "JSON-LD for SEO" o "Smart SEO" (~$10-20 USD/mes). Claude genera datos, Javier configura.
- **Manual:** Claude genera JSON-LD completo, Javier o desarrollador lo pega en `theme.liquid`.

---

## 6. MEJORAS TÉCNICAS (acción de Javier/equipo)

| Problema | Solución | Quién | Prioridad |
|----------|----------|-------|-----------|
| Redirect 301 duplicado cancelación | Admin > Navigation > URL Redirects | MANUAL | MEDIO |
| Alt text imágenes homepage | Admin > editor de página, agregar alt text | PARCIAL (Claude prepara lista) | ALTO |
| Nombres de archivos imágenes (1.jpg, 2.jpg) | Renombrar al subir nuevas imágenes | MANUAL | MEDIO |
| Velocidad de carga — imágenes pesadas | ShortPixel o Crush.pics (apps Shopify) | MANUAL | ALTO |
| Sitemap.xml — envío a Google | Google Search Console > Sitemaps | MANUAL | ALTO |
| Google Search Console — configuración | Verificar dominio vía DNS o HTML tag | PARCIAL (Claude genera HTML tag) | MUY ALTO |
| Robots.txt — verificación | Confirmar que no bloquea /pages/* ni /blogs/* | MANUAL | MEDIO |

---

## ORDEN DE EJECUCIÓN RECOMENDADO

| Paso | Acción | Tipo | Timeline esperado |
|------|--------|------|-------------------|
| 1 | Corregir títulos y meta de /barberia, /panama, /financiacion | AUTO | Indexación mejorada en 1-2 semanas |
| 2 | Crear /pages/implante-capilar-bogota | AUTO | Tráfico local en 4-8 semanas |
| 3 | Crear /pages/implante-capilar-medellin | AUTO | Tráfico local en 4-8 semanas |
| 4 | Crear /pages/implante-capilar-barranquilla | AUTO | Tráfico local en 4-8 semanas |
| 5 | Crear /pages/implante-capilar-bucaramanga | AUTO | Tráfico local en 4-8 semanas |
| 6 | Crear /pages/precios | AUTO | Tráfico comercial en 4-8 semanas |
| 7 | Crear páginas de servicio (barba, cejas, terapias) | AUTO | Tráfico de nicho en 6-10 semanas |
| 8 | Crear blog + 6 artículos SEO | AUTO | Tráfico informacional en 8-16 semanas |
| 9 | Instalar app Schema Markup e insertar JSON-LD | PARCIAL | Rich snippets en 2-4 semanas |
| 10 | Enviar sitemap en Google Search Console | MANUAL | Indexación acelerada |

---

## ESTADO DE EJECUCIÓN

- [ ] Paso 1: Corregir on-page /barberia, /panama, /financiacion
- [ ] Paso 2-5: Landing pages de ciudad (4 páginas)
- [ ] Paso 6: Página de precios
- [ ] Paso 7: Páginas de servicio (barba, cejas, terapias)
- [ ] Paso 8: Blog "Guía Capilar" + 6 artículos
- [ ] Paso 9: Schema markup (pendiente app o acceso al tema)
- [ ] Paso 10: Google Search Console configurado y sitemap enviado

---

## NOTAS DE TRABAJO
- Javier debe proporcionar testimonios de pacientes por ciudad para las landing pages
- Javier debe subir fotos antes/después reales para /pages/resultados
- Google Search Console es prioritario para medir impacto de todas las mejoras

**Relacionado:** [[perfil-cliente]] | [[stack-pauta]] | [[notebooklm/geminnovart]]
