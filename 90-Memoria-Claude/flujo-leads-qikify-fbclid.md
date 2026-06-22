---
name: flujo-leads-qikify-fbclid
description: Flujo real de los leads del formulario qikify (Implante Capilar) y el problema de fbclid — investigado con prueba en vivo el 2026-06-21.
metadata:
  type: project
  fecha: 2026-06-21
---

# Flujo de leads — Formulario qikify + problema fbclid

Investigado el 2026-06-21 con un lead de prueba (PRUEBA / prueba@gmail.com / +573002181682 / Bogotá).

## Flujo confirmado

```
qikify form (Shopify) → correo a innovartmedicalips@gmail.com → n8n (IMAP) → GHL
```

- **qikify** envía un correo `no-reply@qikify.com` con asunto "You received a message from [nombre] via Implante Capilar form".
- **n8n** lo intercepta por IMAP y lo pasa a GHL (quien configuró la integración: la persona que hizo el setup de n8n).
- **GHL** recibe el contacto.

## Datos que captura qikify

Nombre, Email, Teléfono, Sede. **NO captura fbclid ni ctwa_clid.**

## Submit URL en el correo

El correo de qikify incluye un campo `Submit URL` que muestra la URL de la página donde se llenó el form. En la prueba mostró `https://www.innovartmedical.com/` — sin ningún parámetro `fbclid`.

## Limitaciones descubiertas en qikify

Formulario "Implante Capilar" revisado pestaña por pestaña (Fields / Display / Trigger Button / Style / Extra):

- **No existe opción de "Redirect URL" ni "Success Page"** en ninguna de las pestañas. qikify solo muestra un mensaje de éxito en la misma modal, NO redirige al usuario a otra página.
- **No hay campo oculto (hidden field)** nativo para capturar el `fbclid` de la URL.

## Implicación para CAPI

Sin fbclid en el lead:
- El evento `Lead` de CAPI no puede hacer match con el click de Meta.
- La EMQ (Event Match Quality) se mantiene baja en esos leads.

## Opciones contempladas

1. **Landing de gracias** (Opción A): imposible con qikify sin redirect.
2. **Campo HTML personalizado** en qikify → capturar fbclid vía JS (`URLSearchParams(location.search).get('fbclid')`). Posible con "Custom HTML" en Fields.
3. **API propia** que reciba el form con fbclid: evaluada y descartada por complejidad.
4. **Instrucción a n8n** (Fase 2): pedir a quien maneja n8n que agregue un campo custom `fb_click_id` en GHL con el fbclid que aparece en la Submit URL del correo.

**Estado al 2026-06-21:** solución pendiente. La más práctica a corto plazo es (2) agregar un Custom HTML oculto en qikify que lea el fbclid de la URL y lo incluya en el form, para que n8n lo lea del cuerpo del correo.

## Campo GHL para fbclid

ID: `FYVJpTGSmAPhiqoRwm97` (campo `fb_click_id`). Ver [[feedback_fbclid_landing_pages]].
