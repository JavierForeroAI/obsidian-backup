---
name: tag-landing-home
description: Tag correcto para /home landing form — landing_form_home (no landing_formulario_web)
metadata:
  type: reference
---

# Tag de /home Landing

**Nombre correcto:** `landing_form_home`

**NO usar:** `landing_formulario_web` (nombre anterior, incorrecto)

## Por qué importa
- El tag se asigna automáticamente cuando se envía el form en /home
- La búsqueda por tag en GHL MCP debe usar `landing_form_home` exactamente
- Test contact creado ayer (2026-06-22) confirmó que funciona: test@innovart.com

## Flujo confirmado ✅
1. Usuario rellena form en /home
2. Contacto se crea en GHL con email/teléfono
3. Tag `landing_form_home` se asigna automáticamente
4. Workflow `Web - Formulario Contacto Shopify` se activa
5. Oportunidad se crea con tag `oportunidad ventas frio`

## Testing protocol
Cuando verificar /home en el futuro:
1. Crear contacto TEST: `test[fecha]@innovart.com` (ej: test062326@innovart.com)
2. Buscar contacto por email en GHL
3. Confirmar que tiene tag `landing_form_home`
4. Verificar que oportunidad se creó en flujo correcto

**Última verificación:** 2026-06-23, contact test@innovart.com ✅ funciona
