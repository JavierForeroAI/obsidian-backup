---
name: referencia-tecnica-shopify-pagefly-whatsapp-tracking
description: Guía técnica definitiva — cómo funciona el tracking en Shopify+PageFly y cómo enriquecer links de WhatsApp con UTMs. Fuente de verdad para no improvisar.
metadata:
  type: reference
---

# Referencia Técnica — Shopify + PageFly + WhatsApp UTM Tracking

**Fecha:** 26 junio 2026  
**Por qué existe:** Tomó 4+ horas descubrir por qué los botones de WA no recibían el sufijo UTM. Todo lo documentado aquí fue validado en producción en `innovartmedical.com`.

---

## 1. Arquitectura de la landing (lo que tienes)

| Capa | Tecnología | Notas |
|------|-----------|-------|
| CMS | Shopify (tema Dawn — GEO IA Innovart, ID `181331001645`) | El tema tiene 2 scripts en `layout/theme.liquid` |
| Page builder | PageFly (React + Styled Components) | Renderiza botones DINÁMICAMENTE después del DOM ready |
| CRM | GoHighLevel (location `NPhQTmLOHd6FbDtqLPnG`) | Recibe leads por API REST |
| Tracking | Scripts propios en theme.liquid (no GTM) | GTM fue descartado — los scripts van directo en el tema |

---

## 2. Cómo funciona PageFly (crítico para entender el problema)

- PageFly es **React-based**. Monta componentes en el DOM después de que el HTML base se carga.
- Los botones de WhatsApp (`<a href="https://wa.me/...">`) **no existen en el HTML inicial** — PageFly los inyecta vía JavaScript.
- PageFly puede **re-renderizar** sus componentes, lo que reemplaza los nodos DOM existentes. Si modificaste un `href`, PageFly puede crearlo de nuevo sin tu modificación.
- Los botones tienen clase `pf-button-1`, `data-pf-type="Button2"`, y usan Styled Components (`sc-fbFjKN`).
- Los botones tienen **`target="_blank"`** — esto es crucial para el comportamiento en iOS (ver sección 4).

---

## 3. Variables globales vs window.location.search — NUNCA usar globals para UTMs

### ❌ Lo que NO funciona (y por qué)

```javascript
// MAL — window.LANDING_UTMS puede ser undefined en el contexto del click handler
var utms = window.LANDING_UTMS || JSON.parse(sessionStorage.getItem('landing_utms') || '{}');
var src = utms.utm_source || 'directo'; // Si LANDING_UTMS es undefined → src = 'directo'
var sfx = ...; // sfx queda vacío
if (!sfx) return; // Sale sin hacer nada
```

**Por qué falla:** En el in-app browser de Facebook/Instagram (WKWebView en iOS), la variable global `window.LANDING_UTMS` puede ser `undefined` cuando el click handler corre. `sessionStorage` también puede fallar. El resultado es un sufijo vacío y el handler no hace nada.

### ✅ Lo que SÍ funciona siempre

```javascript
// BIEN — window.location.search siempre tiene la URL actual
var p = new URLSearchParams(window.location.search);
var src = p.get('utm_source') || 'directo';
var cmp = p.get('utm_campaign') || '';
```

**Por qué funciona:** `window.location.search` es una propiedad del navegador garantizada en todos los contextos (FBIAB, WKWebView, Safari, Chrome, Android). `URLSearchParams` tiene soporte universal desde iOS 10 / Android 5.

**Regla absoluta:** En cualquier script de tracking en Shopify, leer UTMs SIEMPRE de `window.location.search`, nunca de variables globales.

---

## 4. El problema de `target="_blank"` en iOS con links de WhatsApp

### El comportamiento de iOS

Cuando un `<a href="https://wa.me/...">` tiene `target="_blank"`:
- iOS/WebKit **captura el href en el momento del toque** para pasarlo al sistema operativo
- Esta captura ocurre **antes o simultáneamente** con el disparo del evento `click` de JavaScript
- Si JavaScript modifica `el.href` en el click handler, iOS **ya tiene la URL original** y abre WhatsApp con ella

Este es el motivo por el que `el.href = newUrl` dentro de un click handler no funciona en iOS para links `wa.me` con `target="_blank"`.

### La solución: preventDefault + window.open

```javascript
document.addEventListener('click', function(e) {
  var el = e.target.closest('a[href*="wa.me"]');
  if (!el) return;
  
  var p = new URLSearchParams(window.location.search);
  var src = p.get('utm_source') || 'directo';
  var cmp = p.get('utm_campaign') || '';
  var sfx = cmp ? ' ['+src+'/'+cmp+']' : (src !== 'directo' ? ' ['+src+']' : '');
  if (!sfx) return;
  
  try {
    var url = new URL(el.href);
    var txt = decodeURIComponent(url.searchParams.get('text') || '');
    if (txt.indexOf('[') === -1) {
      url.searchParams.set('text', txt + sfx);
      e.preventDefault();           // Cancela la navegación original
      e.stopImmediatePropagation(); // Evita que otros handlers interfieran
      window.open(url.toString(), '_blank'); // Abre con la URL modificada
    }
  } catch(ee) {}
}, true); // true = capture phase (corre ANTES de cualquier handler en el elemento)
```

**Por qué funciona:**
- `e.preventDefault()` cancela que el navegador siga el href original
- `window.open()` desde un click handler es considerado acción del usuario → no bloqueado como popup
- `capture: true` garantiza que nuestro handler corre antes que cualquier handler de PageFly

**Fallback si `window.open` falla:** cambiar por `window.location.href = url.toString()` — abre WhatsApp sin nueva ventana pero funciona igual.

---

## 5. MutationObserver con React/PageFly — limitaciones

MutationObserver detecta cambios en el DOM. Funciona bien para frameworks que **agregan** nodos. Pero con React:

- Cuando React re-renderiza, **reemplaza** nodos existentes (crea nuevos DOM nodes)
- El MutationObserver detecta los nuevos nodos y los enriquece
- React puede volver a re-renderizar y los nodos enriquecidos se pierden
- El resultado: race condition entre React y el MutationObserver

**Cuándo SÍ usar MutationObserver:** cuando el framework agrega elementos sin reemplazar los existentes (jQuery, vanilla JS).  
**Cuándo NO usar MutationObserver:** cuando hay React/Vue/Styled Components que hacen reconciliación de DOM.  
**Alternativa para React:** interceptar el click (ver sección 4).

---

## 6. Facebook in-app browser (FBIAB) — comportamiento especial

Cuando un usuario llega desde Meta Ads y hace clic en el anuncio, se abre el **in-app browser de Facebook/Instagram**, no Safari ni Chrome.

Características relevantes:
- En iOS: usa **WKWebView** (motor WebKit pero con restricciones extra)
- En Android: usa **Android WebView** (Chromium)
- Puede aislar variables globales entre scripts de diferentes `<script>` tags
- `sessionStorage` puede estar disponible pero con comportamiento inconsistente
- `window.location.search` **siempre funciona** — es parte del API del navegador garantizado
- `window.open()` desde click handler del usuario **generalmente funciona** (no es popup)

**Regla:** asumir siempre que el usuario llega en FBIAB. Diseñar los scripts para ese contexto primero.

---

## 7. Estructura de scripts en theme.liquid (configuración actual)

### Script 1 — UTM Capture (en `<head>`)
Ubicación: después de `<!-- End Google Tag Manager -->`

```html
<!-- Innovart UTM Capture -->
<script>(function(){try{var p=new URLSearchParams(window.location.search);window.LANDING_UTMS={utm_source:p.get('utm_source')||'directo',utm_medium:p.get('utm_medium')||'none',utm_campaign:p.get('utm_campaign')||'sin_campana',utm_content:p.get('utm_content')||'',utm_term:p.get('utm_term')||''};sessionStorage.setItem('landing_utms',JSON.stringify(window.LANDING_UTMS));}catch(e){}})();</script>
<!-- End Innovart UTM Capture -->
```

### Script 2 — WA + Form Enrichment (antes de `</body>`)
**VERSIÓN DEFINITIVA** (con todos los fixes aplicados):

```html
<!-- Innovart WA + Form UTM Enrichment -->
<script>(function(){try{var GHL_TOKEN='[ver GHL Private Integrations → Landing UTM Tracker]';var GHL_LOCATION='NPhQTmLOHd6FbDtqLPnG';document.addEventListener('click',function(e){var el=e.target.closest('a[href*="wa.me"]');if(!el)return;var p=new URLSearchParams(window.location.search);var src=p.get('utm_source')||'directo';var cmp=p.get('utm_campaign')||'';var sfx=cmp?' ['+src+'/'+cmp+']':(src!=='directo'?' ['+src+']':'');if(!sfx)return;try{var url=new URL(el.href);var txt=decodeURIComponent(url.searchParams.get('text')||'');if(txt.indexOf('[')===-1){url.searchParams.set('text',txt+sfx);e.preventDefault();e.stopImmediatePropagation();window.open(url.toString(),'_blank');}}catch(ee){}},true);var form=document.querySelector('#bcontact-form-483316');if(!form)return;form.addEventListener('submit',function(){try{var p2=new URLSearchParams(window.location.search);var utms={utm_source:p2.get('utm_source')||'directo',utm_medium:p2.get('utm_medium')||'none',utm_campaign:p2.get('utm_campaign')||'sin_campana',utm_content:p2.get('utm_content')||'',utm_term:p2.get('utm_term')||''};var rawPhone=((document.querySelector('[name="contact[Número de Celular]"]')||{}).value||'').replace(/\D/g,'');var email=((document.querySelector('[name="contact[email]"]')||{}).value||'').trim();var fullName=((document.querySelector('[name="contact[name]"]')||{}).value||'').trim();var sede=((document.querySelector('[name="contact[Sedes principales]"]')||{}).value||'').trim();if(!rawPhone&&!email)return;var phone=rawPhone.length===10?'+57'+rawPhone:(rawPhone.startsWith('57')&&rawPhone.length===12)?'+'+rawPhone:'+57'+rawPhone;var body={locationId:GHL_LOCATION,tags:['fuente_landing','landing_formulario'],customFields:[{id:'ffBWPx4Qlhxb6D6toNWO',value:utms.utm_source},{id:'46qWfYJubx8IAOhyFlgT',value:utms.utm_medium},{id:'lPfZB842vcw2a7iD3tOD',value:utms.utm_campaign},{id:'hFUkJs1bRuGskcA6X5TA',value:utms.utm_content},{id:'ni4PMQh6l93hmoiyfEEY',value:utms.utm_term}]};if(phone)body.phone=phone;if(email)body.email=email;if(fullName)body.firstName=fullName.split(' ')[0];if(fullName)body.lastName=fullName.split(' ').slice(1).join(' ');if(sede)body.city=sede;fetch('https://services.leadconnectorhq.com/contacts/',{method:'POST',keepalive:true,headers:{'Authorization':'Bearer '+GHL_TOKEN,'Content-Type':'application/json','Version':'2021-07-28'},body:JSON.stringify(body)}).catch(function(){});}catch(e){}});}catch(e){}})();</script>
<!-- End Innovart WA + Form UTM Enrichment -->
```

---

## 8. Checklist de debugging para problemas de tracking en Shopify

Cuando algo no funciona:

1. **¿El script está guardado?** Verificar que el archivo theme.liquid tiene los cambios (el punto azul en la pestaña indica sin guardar)
2. **¿El token tiene corchetes?** El token debe ser `'pit-xxx'` no `'[pit-xxx]'`  
3. **¿El token tiene salto de línea?** Pegar y guardar en una sola línea
4. **¿Las variables globales funcionan?** Usar `new URLSearchParams(window.location.search)` en vez de `window.LANDING_UTMS`
5. **¿El link tiene `target="_blank"`?** Si sí → usar `preventDefault()` + `window.open()`
6. **¿El framework es React?** Si sí → no usar MutationObserver, usar click interceptor
7. **¿El browser de prueba es el in-app de Facebook?** Probar en Safari nativo también para aislar el problema

---

## 9. Cómo identificar el mensaje de WhatsApp en GHL

El mensaje que llega cuando el lead hace clic en el botón de la landing es:
```
Hola, vi este anuncio en la web y quiero más información de implantes capilares. [meta/MEDELLIN_FUE]
```

- GHL agrega automáticamente al final: `\n\nReceived on 📱[Ppal Pagina y Google]`
- El sufijo `[meta/MEDELLIN_FUE]` identifica fuente y campaña
- Buscar en GHL por el texto exacto del mensaje para rastrear leads de la landing

---

---

## 10. Formato del sufijo WhatsApp — decisiones y aprendizajes (26 jun 2026)

### Por qué el sufijo es el único tracking para leads de WA
- Al hacer clic en un botón de WhatsApp, el navegador abre `wa.me` directamente
- No hay evento de submit, no hay llamada API a GHL en ese momento
- El contacto se crea en GHL solo cuando el lead ENVÍA el mensaje
- En ese momento ya no hay forma de saber qué campaña generó el clic
- **Conclusión:** el sufijo en el texto del mensaje ES el único identificador para WA leads

### Evolución del formato
1. Versión inicial: `[meta/MEDELLIN_FUE]` — usando utm_source/utm_campaign completo
2. Problema: nombre de campaña largo ("Trafico a web RM (Fase 2)") → sufijo demasiado largo
3. Versión final: `[fb/rtg]` — usando fuente corta + medio corto

### Código final del sufijo (en Script 2)
```javascript
var src=p.get('utm_source')||'directo';
var med=p.get('utm_medium')||'';
var srcS=src==='facebook'?'fb':src==='instagram'?'ig':src;
var medS=med==='retargeting'?'rtg':med==='paid_social'?'paid':med==='instagram_dm'?'ig-dm':med==='facebook_dm'?'fb-dm':med;
var sfx=(src!=='directo')?' ['+srcS+(medS?'/'+medS:'')+']':'';
```

### Bug crítico: token con salto de línea
- **Síntoma:** script no hace nada — sin sufijo, sin API call, silencio total
- **Causa:** el token GHL pegado con un salto de línea al final rompe la sintaxis JS
  ```javascript
  var GHL_TOKEN='pit-xxxxx\n';  ← \n real dentro de comillas simples = syntax error
  ```
- **Fix:** asegurarse de que el token esté en una sola línea sin ningún carácter después
- **Cómo detectarlo:** en Shopify ver el contenido del archivo via GraphQL API — el `\n` aparece en el valor

### Tipos de anuncios Meta que van a la landing vs. directo a WA
| Tipo | Destino | Tracking |
|------|---------|----------|
| Click-to-WhatsApp | WA directo (sin landing) | ctwa_clid en GHL |
| Tráfico a landing | innovartmedical.com → botón WA | sufijo en mensaje |
| Lead Ads | Formulario nativo Meta | workflow GHL |

- **Cómo distinguirlos:** el URL del clic — si abre `api.whatsapp.com` directamente es click-to-WA; si abre `innovartmedical.com` es landing

### Creativos viejos sin UTMs
- En cuenta LANDING DIEGO existen creativos de 2025 que van a `innovartmedical.com` sin url_tags
- Los clicks desde esos creativos llegan a la landing sin UTMs → sin sufijo → lead anónimo
- Identificados por `call_to_action.value.link = "https://www.innovartmedical.com/"` sin parámetros
- **Pendiente:** aplicar UTMs a esos creativos

---

## 11. Fuentes de información para resolver problemas de tracking

### Para entender comportamiento de Meta Ads
- **Meta API via MCP `mcp__meta-dajf__*`** — ver campañas activas, ads, creativos y sus url_tags
- Herramienta clave: `list_ads` → da creative_id → `list_creatives` → da URL destino y url_tags
- **Ads Manager UI** → campo "Parámetros de URL" en edición de ad muestra los UTMs configurados
- "Valores establecidos anteriormente" = Meta confirma que ya tiene los valores dinámicos guardados

### Para leer/verificar código en Shopify
- **GraphQL query `theme { files { nodes { body { content } } } }`** — lee el archivo liquid actual sin abrir UI
- Tema activo: ID `181331001645` ("Dawn — GEO IA Innovart")
- Archivo crítico: `layout/theme.pagefly.liquid`

### Para verificar leads en GHL
- **`mcp__ghl__search_conversations`** — busca por texto del mensaje o por fecha
- **`mcp__ghl__get_contact`** — ver campos UTM del contacto (customFields por ID)
- Los campos UTM tienen IDs fijos: utm_source=`ffBWPx4Qlhxb6D6toNWO`, utm_medium=`46qWfYJubx8IAOhyFlgT`, utm_campaign=`lPfZB842vcw2a7iD3tOD`

### Para probar el tracking sin esperar un click real
- Construir URL de prueba con UTMs reales de la campaña activa:
  `https://www.innovartmedical.com/?utm_source=facebook&utm_medium=retargeting`
- Abrir en celular en modo incógnito (evita caché)
- Hacer clic en botón WA → verificar sufijo en mensaje

---

**How to apply:** Antes de cualquier trabajo en scripts de Shopify, tema liquid, o botones de WhatsApp — leer primero la sección 3 (UTMs), 4 (target blank) y 2 (PageFly). Para debugging usar sección 8 + herramientas de sección 11. Evita 2-4 horas de debugging.
