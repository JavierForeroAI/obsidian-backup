---
name: fbclid-landing-pages-obligatorio
description: Todo formulario/landing page de GHL o web desarrollado para Innovart debe incluir siempre el campo oculto fbclid → fb_click_id
metadata:
  type: feedback
---

En cualquier landing page o formulario que se desarrolle para Innovart (GHL funnels, HTML, o cualquier plataforma), incluir SIEMPRE un campo oculto que capture el `fbclid` de la URL y lo guarde en el campo personalizado `fb_click_id` de GHL.

**Por qué:** El Worker de Cloudflare lee `fb_click_id` del contacto en GHL y lo envía a Meta CAPI como `fbc = fb.1.{timestamp}.{fbclid}`. Sin este campo, los leads de anuncios web no tienen atribución de clic en Meta y el EMQ baja.

**Campo GHL:** `fb_click_id` (ID: `FYVJpTGSmAPhiqoRwm97`, fieldKey: `contact.fb_click_id`)

**Cómo aplicar:**

Para formularios GHL:
- Agregar campo tipo "Hidden Field"
- Nombre: `fb_click_id`
- Parameter Name: `fbclid`
- Activar "Auto-populate from URL"

Para HTML/formulario web:
```html
<input type="hidden" name="fb_click_id" id="fb_click_id">
<script>
  const params = new URLSearchParams(window.location.search);
  if (params.get('fbclid')) {
    document.getElementById('fb_click_id').value = params.get('fbclid');
  }
</script>
```

**También incluir siempre `ctwa_clid`** para leads de WhatsApp — ver [[ctwa-clid-campo-ghl]].

**How to apply:** Aplicar en TODA landing page nueva sin excepción, sin esperar a que Javier lo solicite. Es parte del estándar de desarrollo de Innovart.
