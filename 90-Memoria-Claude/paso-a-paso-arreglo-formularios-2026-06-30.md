---
name: paso-a-paso-arreglo-formularios-todos-sedes
description: Guía paso-a-paso exacto para arreglar formularios en TODAS las 5 sedes (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá). Verificado con curl directo al Worker.
metadata:
  type: project
  fecha: 2026-06-30
  status: EN_PROGRESO
  urgencia: P0
---

# Arreglo de Formularios — Guía Paso-a-Paso (5 Ciudades)

## Estado Verificado (30 jun 2026)

✅ **Worker backend**: Funciona perfectamente (curl test exitoso)  
✅ **GHL integration**: Contactos llegan con todos los campos correctos  
❌ **Frontend forms**: No disparan POST al Worker (script falta o no se ejecuta)

Problema raíz: El script que intercepta el submit del formulario y POST al Worker **NO está instalado** en las landings.

---

## PASO 1: Bogotá (PageFly)

### 1a. Ir al editor
```
Shopify Admin
  → Temas
  → "Dawn — GEO IA Innovart"
  → "Editar código" (botón arriba a la derecha)
  → Buscar archivo: theme.pagefly.liquid
```

### 1b. Verificar que existe el código de Qikify
**Ctrl+F en theme.pagefly.liquid** y busca: `Innovart Qikify → GHL`

**Si lo encuentras:** ✅ El script está instalado. Continúa a paso 2.

**Si NO lo encuentras:** Necesitas instalarlo.

### 1c. Instalar el script (solo si falta)

1. En theme.pagefly.liquid, ve al **final del archivo**
2. Busca la línea `</body>` (debe estar cerca del final)
3. **ANTES de `</body>`**, pega este código exacto:

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
  document.addEventListener('bcontact:beforeFormSubmitted',function(e){
    if(!e.detail||!e.detail.contact)return;
    var c=e.detail.contact;
    var utms=gu();
    var data={
      sede:c.ciudad||'bogota',
      name:c.firstName+' '+(c.lastName||''),
      email:c.email||'',
      phone:c.phone||'',
      fbclid:gf()||utms.fbclid||'',
      utm_source:utms.utm_source||'',
      utm_medium:utms.utm_medium||'',
      utm_campaign:utms.utm_campaign||'',
      utm_content:utms.utm_content||''
    };
    fetch(W,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).catch(function(){});
  });
})();
</script>
<!-- End Innovart Qikify → GHL v3 (pagefly) -->

<div contactform-embed="483316"></div>
</body>
</html>
```

4. Haz clic en **"Guardar"**

### 1d. Verificar que funcionó

Abre en navegador (incógnito para evitar cache):
```
https://www.innovartmedical.com/pages/implante-capilar-bogota
```

Llena el formulario con datos de prueba:
- Nombre: Test Bogotá 30jun
- Email: test-bogota-30jun@gmail.com
- Teléfono: 3105551234
- Sede: **Sede - Bogota**
- Click en "Agendar Cita"

Espera 5-10 segundos y luego verifica en GHL:
```
GHL Bogotá → Contactos → Busca: test-bogota-30jun@gmail.com
```

Debe existir con tags: `fuente_web_qikify` + `landing_formulariov2`

---

## PASO 2: Medellín (PageFly)

Repite el mismo proceso que Bogotá, pero:
- Archivo: **theme.pagefly.liquid** (igual)
- En el script, cambia solo esta línea de `sede:`:

```javascript
sede:'medellin',  // ← Cambiar de 'bogota' a 'medellin'
```

Test:
```
https://www.innovartmedical.com/pages/implante-capilar-medellin
```

Busca en GHL Medellín (switch location).

---

## PASO 3: Barranquilla (PageFly)

Mismo proceso:
- Archivo: **theme.pagefly.liquid**
- Script con: `sede:'barranquilla',`

Test:
```
https://www.innovartmedical.com/pages/implante-capilar-barranquilla
```

---

## PASO 4: Bucaramanga (PageFly)

Mismo proceso:
- Archivo: **theme.pagefly.liquid**
- Script con: `sede:'bucaramanga',`

Test:
```
https://www.innovartmedical.com/pages/implante-capilar-bucaramanga
```

---

## PASO 5: Panamá (GemPages — DIFERENTE)

Panamá usa **GemPages**, no PageFly. El archivo y proceso es diferente.

### 5a. Ir al editor
```
Shopify Admin
  → Temas
  → "Dawn — GEO IA Innovart"
  → "Editar código"
  → Buscar archivo: theme.gempages.blank.liquid
```

### 5b. Verificar que existe el código
**Ctrl+F** y busca: `Innovart Qikify → GHL`

**Si NO lo encuentras:** Necesitas instalarlo.

### 5c. Instalar el script (solo si falta)

En theme.gempages.blank.liquid, ve al **final del archivo**. Busca `</body>` y pega **ANTES de `</body>`**:

```html
<!-- Innovart Qikify → GHL v3 (gempages) -->
<script>
(function(){
  var W='https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead';
  function gu(){
    try{return JSON.parse(sessionStorage.getItem('inno_utms')||sessionStorage.getItem('landing_utms')||'{}')}catch(e){return{}}
  }
  function gf(){
    try{return localStorage.getItem('_fbclid')||''}catch(e){return''}
  }
  document.addEventListener('click',function(e){
    var btn=e.target.closest('button[type="submit"]');
    if(!btn)return;
    var form=btn.closest('form[class*="gp-form"]');
    if(!form)return;
    var d=new FormData(form);
    var utms=gu();
    var data={
      sede:'panama',
      name:d.get('contact[name]')||'',
      email:d.get('contact[email]')||'',
      phone:d.get('contact[phone]')||'',
      fbclid:gf()||utms.fbclid||'',
      utm_source:utms.utm_source||'',
      utm_medium:utms.utm_medium||'',
      utm_campaign:utms.utm_campaign||'',
      utm_content:utms.utm_content||''
    };
    fetch(W,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).catch(function(){});
  },true);
})();
</script>
<!-- End Innovart Qikify → GHL v3 (gempages) -->

</body>
</html>
```

4. Haz clic en **"Guardar"**

### 5d. Verificar que funcionó

Test:
```
https://www.innovartmedical.com/pages/panama
```

Llena el formulario:
- Nombre: Test Panamá 30jun
- Email: test-panama-30jun@gmail.com
- Teléfono: 65551234
- Ciudad: (dejá en blanco o escribe "Panamá")
- Click en "Agendar cita"

Verifica en GHL Panamá (switch location).

---

## CHECKLIST POST-ARREGLO

Después de instalar los 5 scripts, prueba cada landing:

| Ciudad | URL | Email de prueba | Verificar en GHL |
|--------|-----|-----------------|-----------------|
| Bogotá | `/implante-capilar-bogota` | test-bgta-30jun@gmail.com | GHL Bogotá |
| Medellín | `/implante-capilar-medellin` | test-med-30jun@gmail.com | GHL Medellín |
| Barranquilla | `/implante-capilar-barranquilla` | test-brq-30jun@gmail.com | GHL Barranquilla |
| Bucaramanga | `/implante-capilar-bucaramanga` | test-buc-30jun@gmail.com | GHL Bucaramanga |
| Panamá | `/panama` | test-pan-30jun@gmail.com | GHL Panamá |

Para cada test:
1. ✅ Llena formulario
2. ✅ Submit
3. ✅ Verifica que contacto aparece en GHL correcto
4. ✅ Verifica tags: `fuente_web_qikify` + `landing_formulariov2`
5. ✅ Verifica campos UTM llenados

---

## Notas técnicas

**¿Por qué dos scripts diferentes?**
- **PageFly** (Bogotá, Med, BRQ, Buc): Usa evento `bcontact:beforeFormSubmitted` de Qikify
- **GemPages** (Panamá): Intercepta `click` en el botón submit porque GemPages bloquea eventos `submit`

**¿Por qué PostMessage no funciona?**
- El formulario está en un iframe cross-origin (Qikify para PageFly, GemPages para Panamá)
- No podemos acceder al DOM del iframe desde el documento principal
- Solución: El evento `bcontact:beforeFormSubmitted` llega al document principal (permite cross-iframe)

---

## Archivos relacionados

- [[landing-panama-gempages-setup-2026-06-29]] — detalles de Panamá
- [[qikify-formulario-estructura-html-critica]] — validación de `</body>`
- [[guia-replicacion-landings-ciudades]] — estado de las landings

