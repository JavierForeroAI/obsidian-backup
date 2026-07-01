---
name: checklist-e2e-validation
description: Checklist de validación End-to-End para Shopify, PageFly, GemPages, GHL y tracking. Paso-a-paso verificación post-deploy.
metadata:
  type: checklist
  fecha: 2026-06-30
  status: ACTIVO
  version: 1.0
  aplica_a: Landings, blogs, integraciones, tracking, formularios
---

# Checklist E2E Validation — Innovart

## ANTES DE CADA DEPLOY

**Duración:** 10–15 min | **Responsable:** Javier o Dev | **Frecuencia:** SIEMPRE post-deploy

---

## SECCIÓN 1: Shopify + Meta Pixel

### 1.1 Meta Pixel — Instalación y Disparo

**Ambiente:** Chrome Incognito | **Herramienta:** DevTools Network

- [ ] Ir a `innovartmedical.com` (home)
- [ ] Abrir DevTools (F12) → Network tab
- [ ] Hard-refresh (Cmd+Shift+R)
- [ ] Buscar solicitud a `connect.facebook.net/...fbevents.js`
  - **Status:** 200 ✅
  - **Size:** >50 KB
- [ ] Buscar solicitud a `fbq` POST calls (pixel firing)
  - Debe haber al menos 1 `PageView`
  - **Status:** 200 ✅

**Si falla:**
- [ ] Verificar Meta App está instalada: Shopify Admin → Sales Channels → Facebook & Instagram
- [ ] Confirmar Pixel ID termina en `62`
- [ ] Esperar 24h para sincronización (Meta tarda)

---

### 1.2 Meta Pixel — Eventos Dinámicos

**Ambiente:** Incognito | **Herramienta:** DevTools Console

- [ ] Ir a una página de ciudad (ej. `/implante-capilar-bogota`)
- [ ] F12 → Console
- [ ] Buscar logs: `fbq event` o `fbq('track', ...)`
- [ ] Hacer clic en botón WhatsApp
- [ ] Verificar evento en Network: debe enviar a `fbq('track', 'Lead')` o similar
  - **Status:** 200 ✅

**Si falla:**
- [ ] Revisar theme.liquid `fbq` tracking code (línea ~300)
- [ ] Verificar `gtag.js` también dispara (Google Ads)
- [ ] Comprobar no hay errores JS en Console (rojo)

---

## SECCIÓN 2: fbclid Capture (Meta Click ID)

### 2.1 Captura en URL → localStorage

**Ambiente:** Incognito | **Herramienta:** DevTools Application

**URL de prueba:**
```
https://innovartmedical.com/implante-capilar-bogota?fbclid=IwAR0TEST123456789
```

- [ ] Copiar URL + agregar `?fbclid=IwAR0TEST123456789`
- [ ] Navegar a esa URL en Incognito
- [ ] F12 → Application (pestañal) → localStorage
- [ ] Buscar clave `fbclid` o `_fbclid`
  - **Valor esperado:** `IwAR0TEST123456789` ✅
- [ ] Si está en sessionStorage también: ✅

**Si no aparece:**
- [ ] Verificar theme.liquid tiene código de captura (líneas 50–100):
  ```javascript
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  if (fbclid) localStorage.setItem('_fbclid', fbclid);
  ```
- [ ] Hard-refresh (cache)
- [ ] Console: `localStorage.getItem('_fbclid')` — debe retornar algo

---

### 2.2 fbclid en GHL Custom Field

**Ambiente:** GHL Admin | **Herramienta:** Contact Editor

**Preparación:**
- [ ] Crear contacto test: `test_fbclid_[fecha]@innovart.com`
- [ ] Copiar email exacto para busca posterior

**Prueba E2E:**
- [ ] Ir a landing `/implante-capilar-bogota?fbclid=IwAR_TEST_ABC123`
- [ ] Rellenar formulario con email test
- [ ] Hacer clic "Enviar" / "Submit"
- [ ] Ir a GHL → Búsqueda contacto → email test
- [ ] Expandir contacto y mirar custom field `fb_click_id`
  - **Valor esperado:** `IwAR_TEST_ABC123` ✅
  - **Field ID (Bucaramanga):** FYVJpTGSmAPhiqoRwm97

**Si está vacío:**
- [ ] Verificar custom field existe en GHL: Settings → Custom Fields
- [ ] Revisar form en GHL: agregó field `fb_click_id` como invisible
- [ ] Revisar theme.liquid: código de captura localStorage + asignación a form
- [ ] Test directo en Console: `localStorage.getItem('_fbclid')`

---

## SECCIÓN 3: Qikify Formulario → GHL

### 3.1 Qikify Carga (window.BContact)

**Ambiente:** Incognito | **Herramienta:** DevTools Console

**Test en cualquier landing con Qikify:**

- [ ] Navegar a `/implante-capilar-bogota` (o ciudad)
- [ ] F12 → Console
- [ ] Ejecutar: `typeof window.BContact`
  - **Valor esperado:** `"object"` ✅
  - **Si retorna:** `"undefined"` ❌

**Si es undefined:**
- [ ] Ir a theme.pagefly.liquid
- [ ] Buscar línea: `<script src="https://app.qikify.com/embed.js" async></script>`
  - Nota: URL debe ser `https://app.qikify.com/embed.js`, NO `https://www.qikify.com/...`
- [ ] Verificar está ANTES de comentario `<!-- Innovart Qikify → GHL v3 -->`
- [ ] Hard-refresh y reintentar

**Post-fix test:**
- [ ] Console nuevamente: `typeof window.BContact`
  - Debe retornar `"object"` ✅
- [ ] Formulario debe ser visible en página (no desaparece)

---

### 3.2 Formulario Visible + Funcional

**Ambiente:** Incognito | **Herramienta:** Viewport visual

- [ ] Página `/implante-capilar-bogota` carga
- [ ] Formulario Qikify visible en la página (div con `contactform-embed="483316"`)
- [ ] Campos presentes:
  - [ ] Nombre
  - [ ] Email
  - [ ] Teléfono
  - [ ] Ciudad (selector)
- [ ] Botón "Enviar" visible y clickeable

**Si formulario no aparece:**
- [ ] Abrir DevTools → check para errores JS (rojo)
- [ ] Verificar theme.pagefly.liquid tiene `</body>` antes de `</html>`
- [ ] Revisar: `<div contactform-embed="483316"></div>` está presente
- [ ] Nota: Sin `</body>`, el DOM no se completa y Qikify no renderiza

---

### 3.3 Formulario Submit → Worker POST

**Ambiente:** Incognito | **Herramienta:** DevTools Network + Console

**Preparación:**
- [ ] F12 → Network tab (grabar)
- [ ] F12 → Console (watch para logs)

**Pasos:**
- [ ] Rellenar formulario:
  - Nombre: `Test QikifyE2E`
  - Email: `test_qikify_[timestamp]@innovart.com`
  - Teléfono: `3104567890`
  - Ciudad: Bogotá
- [ ] Hacer clic "Enviar"
- [ ] En Network tab, buscar POST a:
  - URL contiene: `innovart-capi-webhook-no-tocar`
  - Endpoint: `/qikify-lead`
  - **Status:** 200 ✅

**Payload esperado (Network → Request body):**
```json
{
  "name": "Test QikifyE2E",
  "email": "test_qikify_[timestamp]@innovart.com",
  "phone": "3104567890",
  "city": "Bogotá",
  "fbclid": "...",
  "utm_source": "...",
  "utm_campaign": "...",
  "timestamp": "2026-06-30T..."
}
```

**En Console, buscar log:**
```
[Qikify Event] Form submitted
[Worker] Event received
```

**Si POST no se envía:**
- [ ] Console: `typeof window.BContact` debe ser `"object"`
- [ ] Revisar theme.pagefly.liquid: listener `bcontact:beforeFormSubmitted` presente
- [ ] Verificar Worker URL: `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead`
- [ ] Probar en Chrome vs Safari (browser compatibility)

---

### 3.4 Worker Respuesta + GHL Creación

**Ambiente:** GHL Admin + Incognito lado-a-lado

**Verificación GHL:**
- [ ] Esperar 2–3 segundos (async)
- [ ] Ir a GHL → Search Contacts → email test (`test_qikify_[timestamp]@innovart.com`)
- [ ] Contacto encontrado: ✅
- [ ] Verificar tags:
  - [ ] `fuente_web_qikify`
  - [ ] `landing_formulariov2`
  - [ ] `oportunidad ventas frio`
- [ ] Verificar custom fields:
  - [ ] Email: correcto ✅
  - [ ] Teléfono: correcto ✅
  - [ ] Ciudad: Bogotá ✅
  - [ ] fbclid: capturado (si fue en URL) ✅
- [ ] Verificar workflow disparó:
  - [ ] Workflow 4.1 activó (check conversación para SMS/WA que debería llegar)
  - [ ] Oportunidad creada (Ventas > Frío)

**Si contacto no aparece:**
- [ ] Worker devolvió error (Network → Response body)
  - Buscar `error` key en JSON
- [ ] GHL sub-cuenta incorrecta (verificar location routing)
- [ ] Worker secrets incompletos (revisar Cloudflare dashboard)

**Si contacto existe pero sin tags:**
- [ ] Revisar Worker code: debe hacer `addTag` en GHL API
- [ ] Verificar GHL API token en Cloudflare secrets (validad)
- [ ] Revisar logs Worker: Cloudflare dashboard → Worker → Logs

---

## SECCIÓN 4: Landing Pages — Técnico

### 4.1 Schema.org Validation

**Herramienta:** Google Rich Results Test

- [ ] Abrir https://search.google.com/test/rich-results
- [ ] Pegar URL: `https://innovartmedical.com/implante-capilar-bogota`
- [ ] Esperar análisis
- [ ] Verificar resultados:
  - [ ] **Errors:** 0 ✅
  - [ ] **Warnings:** 0 ✅
  - [ ] **Eligibility:** ✅ (debe mostrar "Eligible for Rich Snippets")
- [ ] Expandir "MedicalClinic" → verificar propiedades:
  - [ ] name: Innovart Medical IPS
  - [ ] address: [Dirección correcta de la sede]
  - [ ] telephone: [Teléfono correcto]
  - [ ] aggregateRating: [Rating presente]

**Si hay errores:**
- [ ] Nota el error exacto (ej. "missing property name")
- [ ] Revisar theme.pagefly.liquid o landing HTML → JSON-LD block
- [ ] Validar sintaxis JSON (usar https://jsonlint.com)
- [ ] Re-publicar landing y reintentar Rich Results Test

---

### 4.2 Alt Text en Imágenes

**Herramienta:** DevTools Inspector

- [ ] Abrir `/implante-capilar-bogota` en Incognito
- [ ] Hacer Right-click en cada imagen → Inspect
- [ ] Verificar atributo `alt`:
  ```html
  <img src="..." alt="Implante capilar FUE en Bogotá" />
  ```
  - Alt text NO vacío ✅
  - Alt text descriptivo (keywords locales) ✅
  - Alt text NOT solo nombre archivo ❌

**Checklist por sección:**
- [ ] Hero image: alt descriptivo
- [ ] Procedimiento images (x3–5): alt con keywords
- [ ] Testimonios: alt con nombre/resultado
- [ ] Doctores: alt con nombre + especialidad
- [ ] Ubicación/mapa: alt "Ubicación Innovart Bogotá"

**Si alt vacío:**
- [ ] Landing en PageFly: Editar image → Settings → Alt Text
- [ ] Landing en GemPages: Editar template → Settings image
- [ ] Landing en Shopify nativa: Editar producto/página → Image → Alt

---

### 4.3 Performance — Móvil

**Herramienta:** PageSpeed Insights

- [ ] Abrir https://pagespeed.web.dev
- [ ] Pegar URL: `https://innovartmedical.com/implante-capilar-bogota`
- [ ] Ver scores:
  - [ ] Performance: >50 (meta: >70) ⚠️
  - [ ] Accessibility: >80 ✅
  - [ ] Best Practices: >80 ✅
  - [ ] SEO: >90 ✅
- [ ] Expandir "Opportunities" y mirar top issues:
  - [ ] Images not optimized? → Comprimir
  - [ ] Render-blocking JS? → Defer o async
  - [ ] Cumulative Layout Shift alto? → Fix CSS

**No bloquea deploy si Score >50**, pero reportar a Javier para mejora.

---

## SECCIÓN 5: WhatsApp + CTWA Tracking

### 5.1 WhatsApp Button Visible

**Ambiente:** Incognito (móvil viewport recomendado)

- [ ] Ir a `/implante-capilar-bogota`
- [ ] Viewport: 375×667 (iPhone SE)
- [ ] Buscar botón WhatsApp verde:
  - [ ] Visible en hero o sticky ✅
  - [ ] Clickeable ✅
  - [ ] Texro: "Obtén Valoración Gratis" o similar
- [ ] Hacer clic y verificar:
  - [ ] Abre conversación WhatsApp (si app instalada)
  - [ ] O redirige a WhatsApp Web (si no app)
  - [ ] Número correcto por ciudad (Bogotá: 310, etc.)

**Si no se abre WhatsApp:**
- [ ] Revisar href del botón: `https://wa.me/57310XXXXXXX?text=...`
- [ ] Verificar número teléfono SIN `+` (ej: `573101234567`)
- [ ] Probar en móvil real + simulador

---

### 5.2 ctwa_clid en GHL (WhatsApp Ads)

**Aplicable si:** Landing recibe tráfico desde Meta Ads con objetivo "Mensajes de WhatsApp"

**Herramienta:** GHL Contact search

- [ ] Crear anuncio Meta: Objetivo = "Mensajes de WhatsApp", CTA = "Enviar mensaje"
- [ ] Hacer clic en anuncio (own account, testing)
- [ ] Llenar formulario en landing
- [ ] Buscar contacto en GHL
- [ ] Verificar custom field:
  - [ ] `ctwa_clid`: presente + no vacío ✅
  - [ ] Format: Long string (Meta CTWA ID)
- [ ] Workflow debe incluir utms de WhatsApp Ads

**Si ctwa_clid vacío:**
- [ ] Revisar Meta webhook → Cloudflare Worker logs
- [ ] Endpoint: `/wa-ctwa` debe recibir eventos
- [ ] Verificar Cloudflare secrets: Meta access token, business account ID

---

## SECCIÓN 6: UTM Tracking

### 6.1 UTMs en URL → Persistencia

**Ambiente:** Incognito | **Herramienta:** DevTools Application

**URL de prueba:**
```
https://innovartmedical.com/implante-capilar-bogota?utm_source=instagram&utm_medium=feed&utm_campaign=implante_feb_2026
```

- [ ] Navegar a URL con UTMs
- [ ] F12 → Application → localStorage
- [ ] Buscar clave `inno_utms` o `landing_utms`
  - **Valor esperado:** JSON con utm_source, utm_medium, utm_campaign ✅

**Si no persiste:**
- [ ] Revisar theme.liquid: código UTM capture (línea ~80)
- [ ] Console: `JSON.parse(localStorage.getItem('inno_utms'))`
  - Debe retornar objeto con keys `utm_*`

---

### 6.2 UTMs en Form Submit → GHL Field

**Continuación del test anterior:**

- [ ] Después de rellenar form (mismo navegador)
- [ ] Buscar contacto en GHL
- [ ] Verificar custom fields:
  - [ ] `utm_source`: instagram ✅
  - [ ] `utm_medium`: feed ✅
  - [ ] `utm_campaign`: implante_feb_2026 ✅
  - [ ] Todos presentes en tag + opportunity ✅

**Si UTMs no llegan a GHL:**
- [ ] Revisar Worker: debe enviar UTMs en payload a GHL
- [ ] GHL custom field IDs: verificar están correctos
- [ ] sessionStorage vs localStorage: código debe leer ambos

---

## SECCIÓN 7: GHL Workflow Integration

### 7.1 Workflow 4.1 Dispara Automáticamente

**Preparación:**
- [ ] Test de landing (Sección 3.4) completado con contacto creado

**Verificación:**
- [ ] GHL → el contacto test
- [ ] Expandir conversación (chat area)
- [ ] Buscar mensaje SMS o WhatsApp entrante:
  - [ ] "Hola [nombre], gracias por tu interés..."
  - [ ] Mensaje llega en <10 segundos ✅
  - [ ] Mensaje usa número correcto por sede

**Si mensaje NO llega:**
- [ ] Workflow 4.1 publicado? (check mark ✅)
- [ ] Trigger correcto? (form submission o tag?)
- [ ] SMS/WhatsApp step habilitado? (no gris)
- [ ] Número teléfono configurado? (no vacío)
- [ ] Nota: Bucaramanga aún sin step — skip para esa ciudad

---

### 7.2 Oportunidad Creada

**Verificación:**
- [ ] Contacto test → pestaña "Opportunities" (o similar)
- [ ] Oportunidad presente:
  - [ ] Pipeline: Ventas ✅
  - [ ] Stage: Frío ✅
  - [ ] Titulo: "Lead del formulario [landing]"
- [ ] Tags en oportunidad:
  - [ ] `fuente_web_qikify`
  - [ ] `landing_formulariov2`

**Si oportunidad no existe:**
- [ ] Revisar Router: debe crear oportunidad + asignar tags
- [ ] Verificar Pipeline ID y Stage ID en GHL (settings)
- [ ] Workflow action: "Create Opportunity" configurado

---

## SECCIÓN 8: Integraciones Cross-Platform

### 8.1 Shopify → GHL

**Aplicable:** Si hay productos en `/pages/precios`

- [ ] Comprar un producto en Shopify (test con tarjeta Stripe test)
- [ ] Esperar 5 segundos
- [ ] GHL → Búsqueda por email usado en compra
- [ ] Verificar:
  - [ ] Contacto creado automáticamente ✅
  - [ ] Tag: `shopify_purchase` o similar ✅
  - [ ] Oportunidad: "Purchase" o "Cliente"

**Si contacto/oportunidad no sincroniza:**
- [ ] Shopify → Settings → Apps and Integrations → GHL integration
- [ ] Verificar webhook activo (debe tener ✅)
- [ ] Re-probar compra

---

### 8.2 Google Ads Integration

**Aplicable:** Si landings se promocionan en Google Ads

- [ ] Crear campaña Search (prueba) que apunta a `/implante-capilar-bogota?gclid=[auto]`
- [ ] Hacer clic en anuncio
- [ ] Verificar URL contiene `gclid=[valor]` (Google auto-tagging)
- [ ] Rellenar form en landing
- [ ] GHL → Contacto search
- [ ] Custom field `gclid` (si existe) debe tener valor ✅

**Si gclid no llega:**
- [ ] Verificar Google Ads auto-tagging enabled: Account → Settings → Auto-tagging ✅
- [ ] Landing form debe capturar `gclid` en custom field
- [ ] Revisar theme.liquid: URL params capture

---

## SECCIÓN 9: Post-Deploy Cleanup

### 9.1 Test Data Deletion

- [ ] Ir a GHL
- [ ] Buscar todos contactos con email `test_*@innovart.com` o similar
- [ ] Eliminar cada uno (o marcar con tag `_test` para filtrar después)
- [ ] Nota: No dejes datos de testing en producción

---

### 9.2 Browser Cache + Hard-Refresh

- [ ] Todos los tests hicieron Cmd+Shift+R (hard-refresh)?
  - [ ] Si no → **repetir hard-refresh y retest**
- [ ] Limpiar localStorage si es necesario:
  ```javascript
  localStorage.clear(); // En Console
  ```

---

### 9.3 Email de Confirmación

**Enviar a Javier + Esneider (Media):**

```
Subject: ✅ E2E Validation Completado — [Landing/Feature Name]

Checklist Status:
✅ Pixel Meta dispara
✅ fbclid capturado
✅ Qikify form funciona
✅ GHL integration OK
✅ Workflow 4.1 dispara
✅ UTMs persistentes
✅ Schema válido
✅ Performance aceptable
⚠️ [Cualquier issue encontrado]

Fecha: 2026-06-30
URL: https://innovartmedical.com/implante-capilar-bogota
Validated by: [Tu nombre]

Próximos pasos: [Si aplica]
```

---

## Troubleshooting Rápido

| Síntoma | Causa Probable | Fix |
|---|---|---|
| fbclid no se captura | URL params no parseados | theme.liquid URLSearchParams |
| Qikify form no aparece | window.BContact undefined | theme.pagefly.liquid: Qikify script URL |
| Form submit no llega a GHL | Worker falla / no ejecuta POST | DevTools Network: verificar status 200 |
| Workflow no dispara | Trigger incorrecto o deshabilitado | GHL Workflow: revisar trigger + estado publish |
| Schema errors | JSON syntax o properties faltantes | jsonlint.com + Rich Results Test |
| UTMs no persisten | sessionStorage/localStorage no guardado | Console: verificar getItem() retorna algo |

---

## Frecuencia de Validación

| Evento | Checklist Aplicar |
|---|---|
| Deploy landing nueva | ✅ TODAS secciones (1-9) |
| Cambio schema/tracking | ✅ Secciones 2, 4, 6–7 |
| Update micro (copy/imagen) | ✅ Sección 4 (alt text, schema) |
| Deploy tracking script | ✅ Secciones 1–3, 5–6 |
| Post-launch semanal | ✅ Sección 7–8 (workflows, integraciones) |

---

**Última actualización:** 2026-06-30
**Versión:** 1.0
**Aprobado por:** Innovart Dev Standards
