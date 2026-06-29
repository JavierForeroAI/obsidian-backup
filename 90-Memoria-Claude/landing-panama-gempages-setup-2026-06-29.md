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

## Fix implementado (29 jun 2026)

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

| Prueba | Resultado |
|---|---|
| Fetch manual desde consola → Worker → GHL | ✅ ok (contactId creado, tags correctos, país PA) |
| Click sintético desde browser tool | ❌ no dispara (evento no-trusted, GemPages lo bloquea) |
| Click real de usuario | ⏳ PENDIENTE — Javier debe probar manualmente |

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
