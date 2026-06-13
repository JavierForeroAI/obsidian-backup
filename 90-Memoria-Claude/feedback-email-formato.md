---
name: feedback-email-formato
description: Informes por correo — siempre usar HTML email-safe con tablas e inline styles, nunca CSS Grid/Flex
metadata:
  type: feedback
---

# Formato obligatorio para informes enviados por correo

Cuando se genere cualquier informe, reporte o documento para enviar por email (Gmail u otro cliente), usar siempre **HTML email-safe**:

- Estructura con `<table>` para todo el layout — nunca `display:flex` ni `display:grid`
- Todos los estilos en **inline style=""** en cada elemento
- Fuentes web-safe: `Arial, Helvetica, sans-serif` — nunca Google Fonts por `<link>`
- Ancho máximo de 600px centrado
- Sin `<style>` blocks complejos — Gmail los ignora o los aplica parcialmente
- Usar `bgcolor` y atributos de tabla (`cellpadding`, `cellspacing`, `border`)
- Colores de fondo en tarjetas, headers y alertas mediante `background-color` inline
- Íconos: emojis Unicode (&#128226;, &#10003;, &#9888;) — no SVG

**Why:** El primer intento con CSS moderno (Grid, Flexbox, Google Fonts) resultó en un correo que solo mostraba texto plano sin formato. Gmail y la mayoría de clientes de correo no soportan estas propiedades.

**How to apply:** Antes de crear el draft de Gmail con `create_draft`, construir el HTML con esta arquitectura. Aplica a cualquier reporte, diagnóstico, brief o documento enviado por correo — no solo UTM reports.
