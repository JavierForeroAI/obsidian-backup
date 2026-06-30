---
name: versionado-theme-pagefly-liquid
description: Historial de versiones de theme.pagefly.liquid — cambios críticos, changelog y rollback reference
metadata:
  type: project
  fecha: 2026-06-30
  archivo: layout/theme.pagefly.liquid
  status: ACTIVO
---

# Versionado — theme.pagefly.liquid

## VERSIÓN 4 (2026-06-30 23:42 UTC)

### Cambio
✅ Reemplazada URL del script de carga de Qikify (CDN endpoint)

### Por qué
La URL anterior (`https://www.qikify.com/app/qikify.min.js`) devolvía **301 Moved Permanently → 404 Not Found**. Esto impedía que la librería de Qikify se cargara, lo que significaba:
- `window.BContact` nunca se inicializaba
- El evento `bcontact:beforeFormSubmitted` nunca se disparaba
- El script personalizado (que intercepta ese evento) nunca se ejecutaba
- **Los formularios NO funcionaban completamente**

**Síntomas (30 jun):**
- ❌ Red: GET `https://www.qikify.com/app/qikify.min.js` → 301 → 404
- ❌ `typeof window.BContact` devolvía `"undefined"`
- ❌ Formulario Qikify no se renderizaba/funcionaba

### Código Original (INCORRECTO)
```html
<script src="https://www.qikify.com/app/qikify.min.js" defer></script>
```

### Código Nuevo (CORRECTO)
```html
<script src="https://app.qikify.com/embed.js" async></script>
```

### Ubicación en el archivo
- **Línea:** ~467 (después de `<!-- Innovart WA + Form UTM Enrichment -->`)
- **ANTES de:** `<!-- Innovart Qikify → GHL v3 (pagefly) -->`

### Estructura Completa (después del cambio V4)

```html
<!-- Innovart WA + Form UTM Enrichment -->
<script>
(function(){
  // ... script de WA enrichment ...
})();
</script>

<script src="https://app.qikify.com/embed.js" async></script>

<!-- Innovart Qikify → GHL v3 (pagefly) -->
<script>
(function(){
  var W='https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead';
  // ... script personalizado ...
})();
</script>

<div contactform-embed="483316"></div>
</body>
```

### Verificación Post-Deploy

```javascript
// En la consola del navegador, después de hard-refresh (Cmd+Shift+R):
typeof window.BContact
// Debe devolver: "object" (NO "undefined")
```

### Impacto Esperado (V4)
- ✅ Qikify CDN se carga correctamente
- ✅ `window.BContact` existe
- ✅ Evento `bcontact:beforeFormSubmitted` se dispara
- ✅ Script personalizado se ejecuta
- ✅ POST al Worker se envía
- ✅ Contactos llegan a GHL con tags + UTMs
- ✅ Workflow 4.1 se dispara automáticamente

---

## VERSIÓN 3 (2026-06-30 13:25 UTC)

### Cambio
✅ Agregado script de carga de Qikify desde CDN

### Por qué
El formulario Qikify no se inicializaba porque faltaba el script de carga de la librería de Qikify (window.BContact). Sin esto:
- El div `<div contactform-embed="483316"></div>` quedaba vacío
- El evento `bcontact:beforeFormSubmitted` nunca se disparaba
- El script personalizado de Qikify → Worker nunca se ejecutaba
- Los formularios NO enviaban datos a GHL
- **Impacto:** Leads se perdían completamente en todas las landings PageFly

**Síntomas diagnosticados (30 jun):**
- ❌ `typeof window.BContact` devolvía `"undefined"`
- ❌ No había POST al Worker
- ❌ Contactos no llegaban a GHL

### Código Agregado

```html
<script src="https://www.qikify.com/app/qikify.min.js" defer></script>
```

### Ubicación en el archivo
- **Línea:** ~467 (después de `<!-- End Innovart WA + Form UTM Enrichment -->`)
- **ANTES de:** `<!-- Innovart Qikify → GHL v3 (pagefly) -->`

### Estructura Completa (después del cambio)

```html
<!-- End Innovart WA + Form UTM Enrichment -->

<script src="https://www.qikify.com/app/qikify.min.js" defer></script>

<!-- Innovart Qikify → GHL v3 (pagefly) -->
<script>
(function(){
  var W='https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead';
  // ... resto del script personalizado ...
})();
</script>
<!-- End Innovart Qikify → GHL v3 (pagefly) -->

<div contactform-embed="483316"></div>
</body>
</html>
```

### Verificación Post-Deploy

```javascript
// En la consola del navegador, después de hard-refresh (Cmd+Shift+R):
typeof window.BContact
// Debe devolver: "object" (NO "undefined")
```

### Impacto Esperado
- ✅ Qikify se inicializa correctamente
- ✅ Evento `bcontact:beforeFormSubmitted` se dispara
- ✅ Script personalizado se ejecuta
- ✅ POST al Worker se envía
- ✅ Contactos llegan a GHL con tags + UTMs
- ✅ Workflow 4.1 se dispara automáticamente

---

## VERSIÓN 2 (2026-06-29 ~20:00 UTC)

### Cambio
✅ Agregado script personalizado Qikify → GHL con listener `bcontact:beforeFormSubmitted`

### Por qué
Para capturar datos del formulario Qikify y enviarlos directamente al Worker de Cloudflare, que luego los envía a GHL en la sub-cuenta correcta según la sede seleccionada.

### Código Agregado

```html
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
    // Captura datos del formulario
    // Envía POST al Worker
  });
})();
</script>
<!-- End Innovart Qikify → GHL v3 (pagefly) -->
```

### Ubicación
Antes de `<div contactform-embed="483316"></div>`

---

## VERSIÓN 1 (pre-29-jun)

### Estado
- ❌ Script personalizado NO existía
- ❌ Sin conexión a Worker
- ❌ Sin enrutamiento automático por sede
- ❌ Leads se perdían

---

## Rollback Reference

Si algo falla con V3, revertir a:
1. **Eliminar** la línea: `<script src="https://www.qikify.com/app/qikify.min.js" defer></script>`
2. **Contactar** a Javier para diagnóstico

---

## Checksum / Validation

### V3 Debe contener:
- ✅ `https://www.qikify.com/app/qikify.min.js` (loader)
- ✅ `bcontact:beforeFormSubmitted` (event listener)
- ✅ `qikify-lead` (Worker endpoint)
- ✅ `<div contactform-embed="483316"></div>` (embed div)
- ✅ `</body>` (cierre de body)

### V3 Debe NO contener:
- ❌ BContact hardcoded
- ❌ Llamadas diretas a GHL API desde cliente
- ❌ Tokens de GHL expuestos en client-side

---

## Próximas Ciudades

Repetir V3 en:
- [ ] **Medellín** — theme.pagefly.liquid (igual script, solo cambiar `sede` en listener si es necesario)
- [ ] **Barranquilla** — theme.pagefly.liquid
- [ ] **Bucaramanga** — theme.pagefly.liquid
- [ ] **Panamá** — theme.gempages.blank.liquid (script diferente, usar click listener)

---

## Relacionados

- [[paso-a-paso-arreglo-formularios-2026-06-30]] — Guía paso-a-paso
- [[qikify-formulario-estructura-html-2026-06-29]] — Estructura HTML crítica
- [[flujo-crm-qikify-verificado-2026-06-29]] — Flujo completo verificado

