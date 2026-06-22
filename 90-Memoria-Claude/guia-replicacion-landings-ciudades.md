---
name: guia-replicacion-landings-ciudades
description: Guía paso a paso completa para crear/replicar landings de ciudad en PageFly (Bogotá como plantilla). Incluye lecciones aprendidas, errores a evitar, códigos listos y checklist de publicación. Usar para Medellín → Barranquilla → Bucaramanga.
metadata:
  type: project
  fecha: 2026-06-21
  estado: activo
---

# Guía de Replicación — Landings de Ciudad Innovart
*Bogotá = plantilla maestra. Replicar cambiando solo los "puntos variables".*

---

## 0. ANTES DE EMPEZAR — cargar contexto

1. Leer [[landing-ciudades-plantilla-checklist-2026-06-20]] — estado actual de Bogotá
2. Leer [[restricciones-lenguaje]] — términos prohibidos
3. Leer [[adn-comunicacion-innovart]] — tono y oferta
4. Confirmar que Bogotá esté 100% publicada antes de duplicar

---

## 1. DATOS POR CIUDAD (puntos variables)

| Campo | Bogotá | Medellín | Barranquilla | Bucaramanga |
|---|---|---|---|---|
| H1 | Implante Capilar en Bogotá | Implante Capilar en Medellín | Implante Capilar en Barranquilla | Implante Capilar en Bucaramanga |
| URL handle | `implante-capilar-bogota` | `implante-capilar-medellin` | `implante-capilar-barranquilla` | `implante-capilar-bucaramanga` |
| Dirección | Calle 119 #7-94, diagonal a la Clínica Santa Fe | C.C. Oviedo, Torre Médica Oviedo, Cons. 678 | Edificio Green Tower (Centro Empresarial), Calle 77B #57-103, Torre 2, Piso 7, Cons. 706 | Centro Internacional de Especialistas, Complejo Médico HIC, KM 7, Cons. 719N, Piso 7 |
| Barrio/zona | Chicó Norte, Usaquén | El Poblado / Oviedo | Norte, Centro Empresarial | Cabecera del Llano |
| Referencia landmark | Diagonal a la Clínica Santa Fe | C.C. Oviedo | Centro Empresarial Green Tower | Complejo Médico HIC |
| Meta title | `Implante Capilar FUE en Bogotá \| Innovart Medical` | `Implante Capilar FUE en Medellín \| Innovart Medical` | `Implante Capilar FUE en Barranquilla \| Innovart Medical` | `Implante Capilar FUE en Bucaramanga \| Innovart Medical` |
| Tel | +57 312 456 5014 | +57 312 456 5014 | +57 312 456 5014 | +57 312 456 5014 |
| Horarios | Lun–Vie 11am–5pm · Sáb 11am–4pm | Lun–Vie 11am–5pm · Sáb 11am–4pm | Lun–Vie 11am–5pm · Sáb 11am–4pm | Lun–Vie 11am–5pm · Sáb 11am–4pm |
| Schema `geo` coords | Bogotá: 4.6971, -74.0489 | Medellín: 6.2087, -75.5674 | Barranquilla: 11.0041, -74.8069 | Bucaramanga: 7.1193, -73.1227 |

---

## 2. PASOS EN SHOPIFY ADMIN (MCP — antes de abrir PageFly)

Hacer via MCP Shopify o desde el admin. Cambiar por ciudad.

### 2a. Crear la página en Shopify
```
Título: Implante Capilar en [CIUDAD] | Innovart Medical
Handle: implante-capilar-[ciudad]
Visibilidad: Oculta (publicar al final)
Plantilla: page (predeterminada)
```

### 2b. Poner meta SEO (MCP graphql_mutation)
```graphql
mutation {
  metafieldsSet(metafields: [
    {
      ownerId: "gid://shopify/Page/[ID]"
      namespace: "global"
      key: "title_tag"
      value: "Implante Capilar FUE en [CIUDAD] | Innovart Medical"
      type: "single_line_text_field"
    },
    {
      ownerId: "gid://shopify/Page/[ID]"
      namespace: "global"
      key: "description_tag"
      value: "Implante capilar FUE en [CIUDAD]: especialistas certificados, valoración gratuita, 24 controles y garantía de folículos implantados. Sede [DIRECCIÓN CORTA]."
      type: "single_line_text_field"
    }
  ]) {
    metafields { key value }
    userErrors { field message }
  }
}
```

---

## 3. PASOS EN PAGEFLY (editor visual)

### 3a. Duplicar la página de Bogotá
1. PageFly → Pages → hover sobre "Implante Capilar en Bogotá"
2. Clic en el ícono de duplicar
3. Renombrar la copia con el nombre de la nueva ciudad

### 3b. Cambios de texto en PageFly (manual)
Cambiar SOLO estos elementos — todo lo demás es igual:

| Elemento | Cómo editarlo |
|---|---|
| H1 desktop | Clic doble sobre el Heading → editar texto |
| H1 móvil | Cambiar a vista móvil → mismo proceso |
| Párrafo intro | Clic doble sobre el Paragraph → editar |
| Bloque NAP (sede) | Clic doble → editar dirección, barrio, referencia |
| FAQ preguntas locales | Cada header del Accordion → editar si alguna pregunta es ciudad-específica |

**Textos a cambiar en intro (sustituir ciudad y dirección):**
> *En Innovart Medical **[CIUDAD]** realizamos implante capilar con técnica FUE… en nuestra sede del **[ZONA]** de la ciudad… **[DIRECCIÓN]**, **[REFERENCIA LANDMARK]**.*

### 3c. Actualizar los 3 elementos HTML/Liquid

**Elemento 1 — gtag Google Ads:** NO tocar (es el mismo para todas las ciudades)

**Elemento 2 — Schema GEO:** actualizar estas líneas por ciudad:
```json
"name": "Innovart Medical [CIUDAD]",
"address": {
  "streetAddress": "[DIRECCIÓN]",
  "addressLocality": "[CIUDAD]",
  "addressRegion": "[DEPARTAMENTO]"
},
"geo": {
  "latitude": [LAT],
  "longitude": [LNG]
},
"url": "https://www.innovartmedical.com/pages/implante-capilar-[ciudad]",
"sameAs": ["https://www.instagram.com/innovartmedicalips/"]
```

**Elemento 3 — BORRAR** (bloque oculto `-9999px` — black-hat SEO, está en TODAS las páginas duplicadas de PageFly)

**Elemento 4 (nuevo) — Script fbclid:** pegar este código (igual para todas las ciudades):
```html
<script>(function(){try{var url=new URL(location.href);var fb=url.searchParams.get('fbclid');function setC(n,v){if(v)document.cookie=n+'='+encodeURIComponent(v)+';path=/;max-age=7776000';}function getC(n){var m=document.cookie.match('(?:^|; )'+n+'=([^;]+)');return m?decodeURIComponent(m[1]):'';}if(fb)setC('inv_fbclid',fb);if(url.searchParams.get('ctwa_clid'))setC('inv_ctwa',url.searchParams.get('ctwa_clid'));var s=fb||getC('inv_fbclid');if(s&&!fb){url.searchParams.set('fbclid',s);history.replaceState(null,'',url.toString());}}catch(e){}})();</script>
```

**Elemento 5 (nuevo) — JSON-LD FAQPage:** pegar (cambiar ciudad en la última pregunta):
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type":"Question","name":"¿Cuánto cuesta el implante capilar en [CIUDAD]?","acceptedAnswer":{"@type":"Answer","text":"El costo varía según el número de folículos y el área a cubrir. Ofrecemos valoración gratuita con el médico especialista. Financiación hasta el 90 % con MeddiPay. Teléfono: +57 312 456 5014."}},
    {"@type":"Question","name":"¿Qué técnica usan — FUE o DHI?","acceptedAnswer":{"@type":"Answer","text":"Usamos la técnica FUE: extracción folicular individual sin bisturí, sin cicatriz lineal y sin puntos. Compatible con corte corto desde la semana 6."}},
    {"@type":"Question","name":"¿Cuánto tiempo tarda la recuperación?","acceptedAnswer":{"@type":"Answer","text":"La mayoría de pacientes retoman actividades entre 3 y 7 días. Primeros resultados visibles entre el mes 3 y 4. Resultado final entre los 12 y 18 meses."}},
    {"@type":"Question","name":"¿El implante capilar es permanente?","acceptedAnswer":{"@type":"Answer","text":"Sí. Los folículos trasplantados con FUE provienen de zonas resistentes a la alopecia. Resultado permanente. Incluye 24 controles médicos en 18 meses."}},
    {"@type":"Question","name":"¿Cómo agendo una valoración en [CIUDAD]?","acceptedAnswer":{"@type":"Answer","text":"Valoración gratuita presencial en [DIRECCIÓN], [CIUDAD], o virtual. Llama al +57 312 456 5014. La atiende el médico especialista, no un asesor comercial."}}
  ]
}
</script>
```

---

## 4. CHECKLIST PRE-PUBLICACIÓN (ciudad por ciudad)

### A. SEO on-page
- [ ] Meta title con ciudad (MCP)
- [ ] Meta description con ciudad y dirección (MCP)
- [ ] URL handle limpio `/implante-capilar-[ciudad]`
- [ ] H1 desktop con ciudad (tag H1, visible)
- [ ] H1 móvil con ciudad (tag H1, visible)
- [ ] Párrafo intro con ciudad, zona, dirección y landmark
- [ ] NAP en texto real (no imagen): dirección + horarios + teléfono
- [ ] Teléfono correcto `312 456 5014` en TODO (no el 318)

### B. GEO / Schema
- [ ] JSON-LD MedicalClinic con NAP de la ciudad
- [ ] JSON-LD FAQPage con ciudad en preguntas 1 y 5
- [ ] Accordion FAQ visible al final de la página
- [ ] Validar con Google Rich Results Test al publicar

### C. Tracking
- [ ] Script fbclid pegado en HTML/Liquid
- [ ] Probar con `?fbclid=PRUEBA_ABC123` → verificar que aparece en Submit URL del correo

### D. Compliance
- [ ] CERO "garantía vitalicia" (texto visible + oculto)
- [ ] CERO "garantía de resultado"
- [ ] No citar Dr. Óscar Muñoz / Carlos Muñoz
- [ ] Teléfono 312 456 5014 (no 318)

### E. Limpieza PageFly
- [ ] Borrar bloque oculto `-9999px` (Elemento HTML/Liquid con `position:absolute;left:-9999px`)
- [ ] Accordion FAQ en posición correcta en móvil
- [ ] Guardar antes de publicar

### F. Publicación
- [ ] Guardar en PageFly
- [ ] Cambiar visibilidad a "Visible" en Shopify Admin
- [ ] Verificar URL en vivo: `https://www.innovartmedical.com/pages/implante-capilar-[ciudad]`
- [ ] Validar Rich Results: `https://search.google.com/test/rich-results`

---

## 5. LECCIONES APRENDIDAS (no repetir errores)

| Error | Solución |
|---|---|
| Texto oculto `-9999px` en PageFly | Borrar siempre ese bloque — es black-hat SEO, Google penaliza |
| qikify Custom HTML NO acepta `<script>` | El script fbclid va en elemento HTML/Liquid de PageFly, NUNCA en qikify (rompe el formulario) |
| FAQ en imagen = invisible para Google/IA | Siempre poner Accordion en texto + JSON-LD FAQPage |
| "garantía vitalicia" prohibida | Usar "garantía de folículos implantados" — ver [[restricciones-lenguaje]] |
| Teléfono 318 en algunas imágenes | El correcto es 312 456 5014 — imágenes las corrige el usuario |
| NAP solo en imágenes | Siempre poner dirección+teléfono+horarios en texto real visible |
| Meta con "garantía de resultado" | Prohibido también — solo "garantía de folículos implantados" |
| FAQ en móvil quedó muy arriba | Verificar posición en vista móvil después de agregar el Accordion |

---

## 5b. EVENTOS — Estado actual y pendiente post-publicación

**Estado actual (2026-06-21):** CERO eventos de tracking en la landing de Bogotá.

| Código | Eventos |
|---|---|
| #1 gtag Google Ads | Solo pageview — sin conversiones |
| #2 Schema GEO | Ninguno (es SEO, no tracking) |
| #4 fbclid | Captura parámetro, no dispara eventos |
| #5 FAQPage | Ninguno (es SEO, no tracking) |

**Pendiente post-publicación (no bloquea publicar):**
- Meta Pixel base code + evento `Lead` cuando form se envía
- Google Ads: conversión cuando form se envía
- WhatsApp click event

Estos se agregan en un **HTML/Liquid #6** después de publicar cada ciudad.

## 6. ESTADO DE AVANCE POR CIUDAD

| Ciudad | Página creada | Meta SEO | Contenido PageFly | FAQ | fbclid | Schema | Publicada |
|---|---|---|---|---|---|---|---|
| **Bogotá** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔴 2 pendientes** |
| **Medellín** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Barranquilla** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Bucaramanga** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

## 7. PRÓXIMO PASO INMEDIATO

**Bogotá primero → terminar y publicar → luego Medellín.**

Retoma en [[landing-ciudades-plantilla-checklist-2026-06-20]] sección "PENDIENTES PARA PUBLICAR".

*Actualizado 2026-06-21 — Claude Code + Javier Forero*
