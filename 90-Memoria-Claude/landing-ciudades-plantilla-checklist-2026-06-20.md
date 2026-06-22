---
name: landing-ciudades-plantilla-checklist-2026-06-20
description: Plantilla maestra y checklist pre-publicación de las landings de ciudad (Bogotá primero → duplicar a Medellín, Barranquilla, Bucaramanga). Cubre SEO on-page, GEO/Schema, tracking de eventos (form, botones, WhatsApp) y estrategia de duplicación. Fase 1 del plan PURO SEO.
metadata:
  type: project
  fecha: 2026-06-20
  estado: en-progreso
---

# Landing de Ciudad — Plantilla Maestra + Checklist Pre-Publicación

Página piloto: **Implante Capilar en Bogotá** (`/pages/implante-capilar-bogota`,
`gid://shopify/Page/154843742509`, **borrador**, builder **PageFly Legacy**).
Estrategia: dejar Bogotá PERFECTA → duplicar a las otras 3 sedes cambiando solo los
"puntos variables". Parte de [[seo-puro-seo-cowork]] (Fase 1).

## ▶️ RETOMA AQUÍ (estado 2026-06-21 — 18:20)
**Plan vigente:** terminar Bogotá PERFECTA → duplicar a Medellín, Barranquilla, Bucaramanga.

### Hecho en sesión 2026-06-21 mañana
- Bloque título "Implante Capilar en Bogotá" → imagen de fondo + overlay azul `#0A2A5E`
- Párrafo descriptivo desktop → texto blanco, centrado, max-width 1150px
- Bloque sede Chicó Norte → fondo azul oscuro `rgb(13, 31, 92)`, texto blanco. NAP completo en texto visible
- Accordion FAQ con 5 preguntas/respuestas al final de la página ✅
- Bloque HTML/Liquid gtag resuelto ✅
- Página guardada ✅

### Hecho en sesión 2026-06-21 tarde
- ✅ Accordion FAQ movido a posición correcta en **móvil** (drag & drop completado)

### ⚠️ Hallazgo sesión tarde
- **Imagen de horarios en móvil** muestra teléfono `+57 318 8528481` → INCORRECTO. Debe ser `312 456 5014`. Reemplazar la imagen manualmente.
- Los **3 códigos HTML/Liquid** de la página existen pero sus contenidos exactos no están en el contexto actual (se perdieron en resumen de sesión). **Próxima sesión: pegar los 3 códigos aquí** para verificar fbclid y eventos.

### 🔴 PENDIENTES PARA PUBLICAR (en orden)
1. ✅ ~~Mover accordion FAQ en móvil~~
2. ✅ ~~Script fbclid~~ — pegado en HTML/Liquid #4
3. ✅ ~~JSON-LD FAQPage~~ — pegado en HTML/Liquid #5
4. **Borrar bloque oculto `-9999px`** (HTML/Liquid #3) — con persona de Google mañana
5. **Reemplazar imagen horarios móvil** — teléfono malo `318 8528481` → correcto `312 456 5014`
6. **Publicar**

### Página tiene ahora 6 elementos HTML/Liquid:
- #1: gtag Google Ads `AW-16490325890` ✅
- #2: Schema GEO (MedicalClinic + MedicalProcedure + BreadcrumbList) ✅
- #3: ⚠️ BLOQUE OCULTO `-9999px` — BORRAR (tiene "garantía vitalicia" ×2)
- #4: ✅ Script fbclid (captura fbclid → cookie → qikify Submit URL)
- #5: ✅ JSON-LD FAQPage (5 preguntas — Rich Results + GEO)
- #6: ✅ Eventos completo (Meta Pixel ×2 + Google Ads ×3 + 11 eventos) — [[eventos-tracking-bogota-html-liquid-6]]

### ⚡ Al arrancar la próxima sesión
1. En PageFly, clic en cada uno de los 3 HTML/Liquid → copiar código aquí
2. Con esos códigos verificamos fbclid + eventos + bloque oculto de una sola vez

**Bogotá tiene 3 elementos HTML/Liquid:** (1) gtag Google Ads `AW-16490325890`, (2) Schema GEO (MedicalClinic+MedicalProcedure+Breadcrumb), (3) ⚠️ **BLOQUE OCULTO a borrar**.

## ✅ Ya hecho (Bogotá)
- URL limpia: `/pages/implante-capilar-bogota`
- Meta title (MCP): `Implante Capilar FUE en Bogotá | Innovart Medical`
- Meta description (MCP): `Implante capilar FUE en Bogotá: especialistas certificados, valoración gratuita, 24 controles y garantía de folículos implantados. Sede Calle 119 #7-94.`
- ⚠️ Corregido: el meta decía "garantía de resultado" (riesgo compliance) → cambiado a
  "garantía de folículos implantados" (lenguaje aprobado, ver [[restricciones-lenguaje]]).
- Imágenes: 22 PC + 10 móvil (`movil-`) subidas a Files con alt text. Reemplazo en PageFly = manual del usuario.

## 🔢 Puntos VARIABLES por ciudad (lo único que cambia al duplicar)
| Elemento | Bogotá |
|---|---|
| H1 | Implante Capilar en Bogotá |
| Dirección sede | Calle 119 #7-94, diagonal a la Clínica Santa Fe |
| Meta title | Implante Capilar FUE en Bogotá \| Innovart Medical |
| URL handle | implante-capilar-bogota |
| Schema NAP | dirección + geo + horarios Bogotá |
| Alt text imágenes locales | "...en Bogotá" |

### Datos de sedes (para duplicar)
- **Medellín:** C.C. Oviedo, Torre Médica Oviedo, Consultorio 678
- **Barranquilla:** Edificio Green Tower (Centro Empresarial), Calle 77B #57-103, Torre 2, Piso 7, Cons. 706
- **Bucaramanga:** Centro Internacional de Especialistas, Complejo Médico HIC, KM 7, Cons. 719 N, Piso 7
- **Bogotá:** Calle 119 #7-94, diagonal a la Clínica Santa Fe
- **Panamá:** C.C. Town Center, Torre Arboleda, Cons. 7030, Costa del Este
- **Tel correcto (todas):** +57 312 456 5014 (NO el 318)
- **Horarios COL:** Lun–Vie 11:00–17:00 · Sáb 11:00–16:00

## 📋 CHECKLIST PRE-PUBLICACIÓN

### A. SEO on-page
- [x] Meta title + description (MCP)
- [x] URL handle limpio
- [x] **H1 de texto real** — agregado en PageFly. Escritorio (Inicio PC, 36px navy centrado) + **Móvil (Inicio Celular, 18px)**. Ambos tag H1, color `#0A1A3C`. Truco aprendido: en móvil soltar el Heading sobre el hero (no en el header/menú); el header bloquea drop.
- [x] Párrafo de intro ÚNICO — en escritorio (Inicio PC), centrado, drop-cap off. En móvil se decidió NO ponerlo (ya está en el DOM vía escritorio → Google lo lee igual). Texto: "En Innovart Medical Bogotá recuperamos tu cabello con implante capilar de técnica FUE…".
- [ ] Texto local Bogotá (zona/barrio, referencia clínica Santa Fe)
- [ ] Alt text en cada imagen reemplazada (las nuevas ya lo traen)
- [ ] Enlaces internos (→ /sobre-innovart, blog, otras sedes)

### B. GEO / Schema (Diagnóstico AI Visibility 37/100 — [[geo-visibilidad-ia-diagnostico-2026-06-19]])
- [x] JSON-LD `MedicalClinic` con NAP de Bogotá (nombre, dir Calle 119 #7-94, tel +573124565014, horarios, areaServed, sameAs Instagram) — pegado en elemento HTML/Liquid de PageFly.
- [x] JSON-LD `MedicalProcedure` (implante capilar FUE, SurgicalProcedure, 24 controles, provider→clínica)
- [x] JSON-LD `BreadcrumbList`
- [ ] JSON-LD `FAQPage` (la FAQ hoy está en imagen → pasar a texto + schema; pendiente para no violar reglas de Google)
- [ ] **Validar con Google Rich Results Test al publicar** (ahora no se puede, página en borrador). Falta `geo` (coords) — opcional.
- Inyección: elemento **HTML/Liquid** dentro del body de PageFly (el `<head>` lo sobrescribe Shopify/PageFly; Google lee el JSON-LD igual en el body).

### C. Tracking / Eventos (URGENTE) — **SOLUCIÓN DEFINIDA, falta implementar**
Objetivo: atribuir los leads del form a Meta (CAPI) con el `fbclid`.

**FLUJO REAL CONFIRMADO (prueba en vivo 2026-06-20):**
`qikify form (Implante Capilar, id 483316) → correo innovartmedicalips@gmail.com (remite no-reply@qikify.com) → n8n (IMAP lee el correo) → GHL → worker CAPI → Meta`
- El correo trae: Form Name, Nombre, Email, Teléfono, Sede, **Submit URL**. NO trae fbclid (aún).
- Leads se distribuyen por ciudad MANUALMENTE desde el correo (campo "Sedes principales").

**❌ LECCIÓN CLAVE: qikify Custom HTML NO acepta `<script>`** → meter JS ahí ROMPE el form (deja el `qcfData` como texto suelto en la página). Restaurar = dejar SOLO el CSS original:
`<style>.bcontact-field-help-text{color:#001a64}.bcontact-content{padding:6px 15px}</style>`

**✅ PLAN B (definitivo, SIN tocar qikify):**
⚠️ NO hay contenedor GTM (solo etiquetas gtag: GA4 `G-KHYS59RXJ7`, Google Ads `AW-16490325890`). El script va en **PageFly (elemento HTML/Liquid)**, NO en GTM ni en qikify (qikify ROMPE con `<script>` → deja `qcfData` como texto; restaurar = solo el CSS `.bcontact-field-help-text{color:#001a64}.bcontact-content{padding:6px 15px}`).
1. **PageFly HTML/Liquid** (cada landing, empezando por home en vivo + plantilla Bogotá) — captura `fbclid` → cookie y lo **repone en la URL** vía `history.replaceState`. Así qikify lo guarda en "Submit URL" del correo. CÓDIGO:
```html
<script>(function(){try{var url=new URL(location.href);var fb=url.searchParams.get('fbclid');function setC(n,v){if(v)document.cookie=n+'='+encodeURIComponent(v)+';path=/;max-age=7776000';}function getC(n){var m=document.cookie.match('(?:^|; )'+n+'=([^;]+)');return m?decodeURIComponent(m[1]):'';}if(fb)setC('inv_fbclid',fb);if(url.searchParams.get('ctwa_clid'))setC('inv_ctwa',url.searchParams.get('ctwa_clid'));var s=fb||getC('inv_fbclid');if(s&&!fb){url.searchParams.set('fbclid',s);history.replaceState(null,'',url.toString());}}catch(e){}})();</script>
```
2. **n8n** — leer el `fbclid` del "Submit URL" del correo → custom field `fbclid` en GHL (lo hace la persona que montó n8n).
3. **Worker CAPI** — usar ese `fbclid` (→ `fbc`) al enviar Lead a Meta.

**FLUJO FORM CONFIRMADO:** qikify (form id 483316) → correo innovartmedicalips@gmail.com (remite no-reply@qikify.com, trae "Submit URL") → n8n IMAP → GHL → CAPI. Leads se reparten por ciudad manual desde el correo.

- [ ] Pegar script fbclid en PageFly Bogotá (plantilla) + home en vivo
- [ ] n8n: parsear fbclid del Submit URL → GHL custom field (persona n8n)
- [ ] Crear custom field `fbclid` en GHL
- [ ] Probar con `?fbclid=PRUEBA_ABC123` → revisar correo
- **Google Ads:** mismo problema (form no rastrea). Opción ideal = Conversiones Mejoradas para Leads (usa email, no necesita gclid). Pendiente, después de Meta.

**Nota Bogotá (al publicar):** ya tiene HTML/Liquid con dataLayer events (whatsapp_click, cta_click, lead_form_submit), pero el form es el mismo qikify → aplica el mismo Plan B.

### D. Compliance final
- [ ] Cero "garantía vitalicia" (imágenes 08 + horarios pendientes — las arregla el usuario)
- [x] Cero "garantía de resultado" (meta corregido)
- [ ] No citar Dr. Óscar Muñoz / Carlos Muñoz / Escuela de Alopecia
- [ ] Tel correcto 312 456 5014 en toda la página

### E. Estrategia de duplicación
1. Dejar Bogotá 100% lista (estructura + secciones + schema + tracking como plantilla).
2. Duplicar en PageFly para cada ciudad.
3. Cambiar SOLO los "puntos variables" (tabla arriba): MCP hace meta+URL+schema; PageFly (manual o browser) hace H1+intro+dirección.

## 🖱️ Pasos PageFly — agregar H1 + intro + dirección (manual)
1. Vista **"All devices"** 🖥️ (siempre).
2. Panel izquierdo → icono de **Elements** (elementos arrastrables).
3. Arrastra **"Heading"** al inicio de la página → suéltalo en la zona azul (drop zone).
4. Doble-clic → escribe `Implante Capilar en Bogotá`.
5. Panel derecho → campo **"Tag"** → selecciona **H1**.
6. Arrastra **"Paragraph"** debajo → pega el párrafo de intro.
7. Arrastra otro **"Paragraph"** (o cerca de sedes) → pega el bloque de dirección.
8. Guarda.

## 🔍 AUDITORÍA SITIO COMPLETO (2026-06-20) — ⏸️ PENDIENTE post-Bogotá
Fetch+grep de páginas en vivo (`curl | grep`). Hallazgos sistémicos (mismo patrón que tenía Bogotá):
- **Texto OCULTO (`position:absolute;left:-9999px`, spam SEO + black-hat)** en 5 PageFly: **HOME**, valoracion, implantedecejas, implantedebarba, valoraciones-panama. *(financiacion=12 y panama=8 ocurrencias `-9999px` → probablemente interno de GemPages, verificar.)*
- **"garantía vitalicia"** (prohibido) en 6: HOME, barberia, valoracion, cejas, barba, valoraciones-panama. En 5 está DENTRO del bloque oculto → se elimina al borrarlo. **barberia** la tiene VISIBLE (GemPages) → fix aparte.
- **CERO schema JSON-LD** en TODAS las páginas de conversión (HOME, valoracion, cejas, barba, panama, financiacion, barberia). Solo `sobre-innovart-medical` (2) y el blog tienen. ← gran gap GEO.
- **H1:** financiacion y barberia = 0 H1. HOME + PageFly = 1 (probablemente el del bloque oculto → al borrarlo quedan SIN H1, poner uno visible como en Bogotá).
- Teléfono en TEXTO correcto en todas (el 318 malo solo en imágenes, no en texto).
- **Plan post-Bogotá:** P0 HOME (borrar oculto + schema + H1) → P1 las 4 PageFly → P2 GemPages (barberia/financiacion/panama). Reusar la plantilla Bogotá ya limpia.

**Relacionado:** [[seo-puro-seo-cowork]] · [[geo-visibilidad-ia-diagnostico-2026-06-19]] · [[reporte-alt-text-completado-2026-06-19]] · [[restricciones-lenguaje]]

*Creado 2026-06-20 — Claude Code + Javier Forero*
