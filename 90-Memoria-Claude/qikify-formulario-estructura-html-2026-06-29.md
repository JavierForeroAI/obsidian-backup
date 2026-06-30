---
name: qikify-formulario-estructura-html-critica
description: ⚠️ CRÍTICO — Estructura HTML correcta para Qikify en theme.pagefly.liquid. Problema: </body> faltante causa formulario oculto.
metadata:
  type: project
  status: RESUELTO
  fecha: 2026-06-29
  urgencia: ALTA
---

# ⚠️ CRÍTICO: Formulario Qikify — Estructura HTML theme.pagefly.liquid

## Problema Raíz (2026-06-29)

**Síntoma:** Formulario Qikify (`contactform-embed="483316"`) en el HTML pero **NO aparecía visualmente** en innovartmedical.com.

**Causa:** El archivo **theme.pagefly.liquid NO tenía `</body>` de cierre**. 
- `<body>` se abre en línea ~367
- Todo el contenido y scripts van dentro del body
- Pero **nunca se cierra** — pasaba directo a `</html>`
- Resultado: el elemento `<div contactform-embed="483316"></div>` quedaba fuera del body, no se renderizaba

**Impacto:** El formulario estaba en el DOM pero invisible. DevTools mostraba el elemento, pero PageFly no podía renderizarlo sin cierre de body.

---

## Solución: Estructura HTML Correcta

### Orden correcto en theme.pagefly.liquid (al final del archivo):

```html
<!-- End Innovart Qikify → GHL v3 (pagefly) -->
<div contactform-embed="483316"></div>
</body>
</html>
```

**NUNCA así (❌ INCORRECTO):**
```html
<!-- End Innovart Qikify → GHL v3 (pagefly) -->
<div contactform-embed="483316"></div>
</html>
<!-- FALTA </body> — el div queda fuera del body -->
```

### Verificación en Shopify

1. **Admin → Temas → "Dawn — GEO IA Innovart"**
2. **Editar código** (NO PageFly visual editor)
3. **Abre: `theme.pagefly.liquid`**
4. **Ctrl+F → busca: `</body>`** (debe encontrar 1 resultado)
5. **Verifica estructura:**
   - Línea X: `<div contactform-embed="483316"></div>`
   - Línea X+1: `</body>`
   - Línea X+2: `</html>`

---

## Código Completo Verificado (2026-06-29)

Las líneas finales de **theme.pagefly.liquid** deben ser:

```html
<!-- Innovart WA + Form UTM Enrichment -->
<script>
(function(){
  try{
    var p=new URLSearchParams(window.location.search);
    var src=p.get('utm_source')||'directo';
    var med=p.get('utm_medium')||'';
    // ... resto del script ...
  }catch(e){}
})();
</script>
<!-- End Innovart WA + Form UTM Enrichment -->

<!-- Innovart Qikify → GHL v3 (pagefly) -->
<script>
(function(){
  var W='https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead';
  function gu(){
    try{return JSON.parse(sessionStorage.getItem('inno_utms')||sessionStorage.getItem('landing_utms')||'{}')}catch(e){return{}}
  }
  function gf(){
    try{return localStorage.getItem('_fbclid')||''}catch(e){return''}
  }
  document.addEventListener('bcontact:beforeFormSubmitted',function(){
    // ... código de captura de datos ...
  });
})();
</script>
<!-- End Innovart Qikify → GHL v3 (pagefly) -->

<div contactform-embed="483316"></div>
</body>
</html>
```

---

## Archivo: theme.pagefly.liquid

| Propiedad | Valor |
|---|---|
| Ruta | `/themes/181331001645/assets/theme.pagefly.liquid` |
| Ubicación Shopify | **Temas → "Dawn — GEO IA Innovart" → Editar código → theme.pagefly.liquid** |
| Línea embed form | **Última línea antes de `</body>`** |
| ID Qikify | `483316` |
| Form ID HTML | `#bcontact-form-483316` |

---

## Checklist Futuro: Si el formulario desaparece

1. ✅ **Verifica que `</body>` existe** en theme.pagefly.liquid (Ctrl+F)
2. ✅ **Verifica que `<div contactform-embed="483316"></div>` está ANTES de `</body>`**
3. ✅ **Hard refresh:** Cmd+Shift+R (Mac) o Ctrl+Shift+F5 (Windows)
4. ✅ **DevTools → Elements → Busca `contactform-embed`** (debe encontrar 1+ resultado)
5. ✅ **Consola JavaScript:**
   ```javascript
   document.querySelector('[contactform-embed="483316"]')
   ```
   Debe devolver el elemento, no `null`

---

## ¿Por qué PageFly auto-generó sin `</body>`?

PageFly es un page builder visual que auto-genera `theme.pagefly.liquid` cada vez que se publica una página.

- **Si lo editas manualmente** en código → puede quedarse incompleto
- **Mejor práctica:** Editar en PageFly visual cuando sea posible
- **Código crítico** (scripts tracking, embed div) → editar en theme.liquid base o theme.pagefly.liquid a mano con cuidado

**Si vuelve a desaparecer el `</body>`:** Probablemente PageFly lo quitó al regenerar. Vuelve a agregarlo.

---

## Links y Referencias

- **Archivo:** [[plan-formulario-qikify-innovartmedical]] — flujo completo Qikify → Worker → GHL
- **Worker:** innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead
- **Evento disparador:** `bcontact:beforeFormSubmitted` (Qikify custom event)
- **Tracking:** fbclid + UTMs capturados → GHL custom fields

---

## Nota: Estructura PageFly vs theme.liquid

| Archivo | Propósito | Contiene `</body>` |
|---|---|---|
| **theme.liquid** | Tema base Shopify (generalmente) | ✅ Sí |
| **theme.pagefly.liquid** | Auto-generado por PageFly (puede faltar `</body>`) | ⚠️ Verificar siempre |
| **theme.gempages.*.liquid** | GemPages (diferente page builder) | ✅ Sí |

PageFly es especialmente propenso a generar HTML incompleto. **Siempre verifica `</body>` después de cambios en theme.pagefly.liquid.**
