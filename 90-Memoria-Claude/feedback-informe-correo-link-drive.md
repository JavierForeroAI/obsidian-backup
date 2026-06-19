---
name: feedback-informe-correo-link-drive
description: Regla permanente — todo informe que se envíe por correo debe ir COMPLETO en Drive y el correo solo lleva el resumen + link al Drive para profundizar.
metadata:
  type: feedback
  updated: 2026-06-18
---

# Informe + correo → versión extensa SIEMPRE en Drive, link dentro del correo

Cuando se genere un informe/reporte/auditoría/diagnóstico **y se vaya a enviar por correo**, es OBLIGATORIO:

1. Subir la versión **completa y extensa** del informe a Google Drive (HTML/PDF/doc detallado).
2. En el cuerpo del correo incluir el **resumen ejecutivo** + un **link al archivo en Drive** para que el lector pueda profundizar en el informe completo.
3. Nunca enviar todo el contenido extenso embebido en el correo: el correo es la puerta de entrada, el detalle vive en Drive.

**Why:** Javier quiere que el lector siempre tenga la opción de profundizar en el informe completo desde el correo, manteniendo el email corto/legible. Centraliza además el documento extenso en Drive (consistente con [[feedback-informes-drive]]).

**How to apply:**
- Antes de crear el draft de Gmail (`create_draft`), subir primero el informe completo a Drive — ligero por MCP Drive, pesado por `rclone` (ver [[feedback-informes-drive]] para carpetas/IDs y la regla de decisión por tamaño).
- Obtener el link compartible del archivo en Drive e insertarlo en el correo (botón/enlace visible: "Ver informe completo en Drive").
- El correo se construye en HTML email-safe (tablas + inline styles, sin Grid/Flex) según [[feedback-email-formato]].
- Aplica a TODO informe enviado por correo, sin excepción: reportes Meta, auditorías CAPI/GHL, diagnósticos, briefs, planes, etc.

**Checklist al enviar cualquier informe por correo:**
- [ ] Informe completo subido a Drive (carpeta correcta según el tipo).
- [ ] Link de Drive obtenido y pegado en el correo.
- [ ] Correo = resumen ejecutivo + CTA al link, no el documento entero.
- [ ] HTML email-safe.
