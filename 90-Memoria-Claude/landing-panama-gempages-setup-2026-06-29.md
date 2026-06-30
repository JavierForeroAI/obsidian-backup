---
name: landing-panama-gempages-setup-2026-06-29
description: Landing de Panamá en GemPages — arquitectura, formulario, tracking a GHL y estado de implementación al 29 jun 2026
metadata:
  type: project
  fecha: 2026-06-29
  status: EN_PRUEBA
---

# Landing Panamá — GemPages (29 jun 2026)

## Datos clave

| Campo | Valor |
|---|---|
| URL live | `https://www.innovartmedical.com/pages/panama` |
| Handle Shopify | `panama` (ID `gid://shopify/Page/143699149101`) |
| Editor | **GemPages 7** (NO PageFly — diferente a las otras ciudades) |
| Layout | `theme.liquid` de Dawn — GEO IA Innovart |
| Publicado | Sí (desde 2025-02-12) |

## Formulario GemPages

- ID del form: `contact_form_gU9LTW4B_d`
- Clase: `gp-form-gU9LTW4B_d`
- Action: `/contact#contact_form_gU9LTW4B_d` → Shopify nativo
- Campos: `contact[name]`, `contact[email]`, `contact[phone]`, `contact[ciudad]` (texto libre)
- Botón envío: `<button type="submit" class="gI4m7LT0PX gp-button-base...">Agendar cita</button>`

## Número WhatsApp en la página

`+50765076869` — número de Panamá (diferente al `+573124565014` de Colombia)

## Problema original (antes del fix)

El formulario GemPages enviaba solo a Shopify (`/contact`) → llegaba email de notificación a `innovartmedicalips@gmail.com` pero NO creaba contacto en GHL Panamá. Leads perdidos.

Ejemplo: lead **Leidy** (martinez240792@gmail.com, tel 69596499) — llegó por email el 29 jun 2026, 12:39 AM pero nunca entró a GHL. **Creada manualmente** en GHL Panamá el 29 jun 2026 (contactId `KwELucAHDfGJmR1JcpCj`).

## Fix implementado — Formulario (29 jun 2026)

**Elemento "Código Personalizado"** añadido en GemPages editor → pestaña **HTML/Liquid**:

```html
<script>
(function(){
  document.addEventListener('click',function(e){
    var btn=e.target.closest('button[type="submit"]');
    if(!btn)return;
    var form=btn.closest('form[class*="gp-form"]');
    if(!form)return;
    var d=new FormData(form);
    var ss=window.sessionStorage||{};
    fetch('https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        sede:'Panama',
        name:d.get('contact[name]')||'',
        email:d.get('contact[email]')||'',
        phone:d.get('contact[phone]')||'',
        utm_source:ss.getItem?ss.getItem('utm_source')||'':'',
        utm_medium:ss.getItem?ss.getItem('utm_medium')||'':'',
        utm_campaign:ss.getItem?ss.getItem('utm_campaign')||'':'',
        utm_content:ss.getItem?ss.getItem('utm_content')||'':'',
        fbclid:ss.getItem?ss.getItem('fbclid')||'':''
      })
    }).catch(function(){});
  },true);
})();
</script>
```

**Por qué `click` con `capture:true`:** GemPages intercepta el evento `submit` y llama `stopPropagation`. El listener en `submit` nunca se dispara. Usando `click` en fase de captura (`true`), el handler corre antes que los handlers de GemPages.

## Pipeline verificado

```
Clic en "Agendar cita"
  → click capture listener lee FormData + sessionStorage UTMs
  → POST a Cloudflare Worker /qikify-lead
  → Worker normaliza teléfono (+507 prefix) + rutea sede="Panama"
  → GHL Panamá (45SKYgIDgr4Eh6a6JcFz) crea contacto
  → Tags: fuente_web_qikify + landing_formulariov2
  → Workflow 4.1 activa pipeline Ventas/Frío
```

## Estado de pruebas

| Prueba | Resultado | Fecha |
|---|---|---|
| Fetch manual desde consola → Worker → GHL | ✅ ok (contactId creado, tags correctos, país PA) | 29 jun |
| Click sintético desde browser tool | ❌ no dispara (evento no-trusted, GemPages lo bloquea) | 29 jun |
| Click real de usuario (nuevo lead post-fix) | ✅ COMPLETADO — lead entra a GHL con UTMs | 29 jun |
| WA button con UTM [fb/rtg] | ✅ FUNCIONAL — sufijo se añade correctamente al href | 29 jun, 13:41 p.m. |

## Ventana de 24h — Verificación mañana (30 jun)

⏳ **Pendiente revisar:** Leads reales que lleguen entre 29 jun 13:45 - 30 jun 13:45
- [ ] Al menos 1 lead nuevo desde formulario QikIfy
- [ ] Verificar que contacto en GHL tiene tags `fuente_web_qikify` + `landing_formulariov2`
- [ ] Verificar que contacto tiene campos UTM rellenos
- [ ] Verificar que workflow 4.1 se disparó (oportunidad + SMS al lead)
- [ ] Confirmar WA messages enviados con [fb/rtg] en el texto

## Fix implementado — WA Button tracking (29 jun 2026)

**Problema:** Botones WA de Panamá no llevaban sufijo de rastreo `[fb/rtg]` como sí lo hacían las páginas de Colombia (PageFly).

**Raíz:** Panamá usa `theme.gempages.blank.liquid`, no `theme.liquid`. El script de tracking solo estaba en `theme.liquid`.

**Solución:** Modificador de href en `theme.gempages.blank.liquid` (líneas 312-314):
- Script modifica el `href` del botón WA directamente en el DOM cuando carga la página
- Usa `MutationObserver` para detectar nuevos botones agregados dinámicamente
- Inserta sufijo `[fb/rtg]` si hay UTMs `utm_source=facebook&utm_medium=retargeting`

```javascript
(function(){
  var p = new URLSearchParams(window.location.search);
  var src = p.get('utm_source') || 'directo';
  if (src === 'directo') return;
  var med = p.get('utm_medium') || '';
  var srcS = src === 'facebook' ? 'fb' : src === 'instagram' ? 'ig' : src;
  var medS = med === 'retargeting' ? 'rtg' : med === 'paid_social' ? 'paid' : med;
  var sfx = ' [' + srcS + (medS ? '/' + medS : '') + ']';
  
  function enrich() {
    document.querySelectorAll('a[href*="wa.me"]').forEach(function(el) {
      try {
        var url = new URL(el.getAttribute('href'));
        var txt = url.searchParams.get('text') || '';
        if (txt.indexOf('[') === -1) {
          url.searchParams.set('text', txt + sfx);
          el.setAttribute('href', url.toString());
        }
      } catch(e) {}
    });
  }
  
  enrich();
  setTimeout(enrich, 800);
  setTimeout(enrich, 2000);
  new MutationObserver(enrich).observe(document.documentElement, { childList: true, subtree: true });
})();
```

**Verificado:** 29 jun 2026, 13:41 p.m. Mensaje WA contiene `[fb/rtg]` correctamente.

## Leads pre-fix recuperados (29 jun 2026)

Los 6 leads reales que llegaron por email Shopify entre 16–26 jun (antes del fix) fueron creados manualmente en GHL Panama y añadidos al workflow 4.1.

| Nombre | Fecha email | Email | Teléfono | contactId GHL |
|---|---|---|---|---|
| Jorge Alberto Navarro | 16 jun | rojorgealberto@gmail.com | +50761803940 | `7OwO9wPreaXDWSfvJRGQ` |
| Jomar | 17 jun | castanedayomar111@gmail.com | +50769594127 | `22QTMxe0T0E4vqpXKz1g` |
| Irina | 20 jun | irinasanchez2023@gmail.com | +50760703508 | `RkG2dQp67TFhDv7qIQvN` |
| Ady | 25 jun | adyrangel05@gmail.com | +525523389834 | `e69W6HOR0Ki55PvAkeP5` |
| Erika | 26 jun | erikac2782@gmail.com | +50766798962 | `y8u5xKDSLNuimSOJOnVr` |
| Agustin Zambrano | 26 jun | zambranoagustin28@gmail.com | +50768107824 | `V1jWI7zvcNeh2ALykQJH` |
| Leidy | 29 jun | martinez240792@gmail.com | 69596499 | `KwELucAHDfGJmR1JcpCj` |

⚠️ **Ady** puso ciudad "CDMX" — posible turismo médico desde México. El asesor debe saberlo.
⚠️ Pruebas descartadas: "PRUEBA D" (aadf@gmail.com) y "PRUEBA PARA SABER A DONDE LLEGA" (f@gmail.co, x2).

## Notas técnicas importantes

- GemPages usa `theme.liquid` (NO `theme.pagefly.liquid`) → los scripts de UTM capture de `theme.liquid` SÍ cargan en esta página
- UTMs se almacenan en `sessionStorage` con las claves: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `fbclid`
- El Worker normaliza el teléfono para Panamá: añade prefijo `+507` si no lo tiene
- El `Código Personalizado` está en el elemento al fondo de la página en GemPages

## Leads no sincronizados (previos al fix)

Los leads que llegaron por el formulario GemPages antes del 29 jun 2026 solo existen en el email de Shopify (`innovartmedicalips@gmail.com`). Para recuperarlos hay que buscar en Gmail con asunto "Nuevo mensaje de cliente" y crear manualmente en GHL Panamá.

⚠️ El MCP de Gmail está conectado a `francisco2javierforero@gmail.com`, NO a `innovartmedicalips@gmail.com` — las notificaciones de Shopify van a la segunda cuenta.

## Archivos relacionados

- [[flujo-crm-qikify-verificado-2026-06-29]] — flujo GHL general verificado
- [[utm-tracking-avance-general]] — estado tracking por fuente
- [[regla-sedes-definitivas]] — Panamá es sede real
