---
name: bucaramanga-lista-espera-launch
description: Lista de espera Bucaramanga — todo lo que hay que hacer cuando abra la sede y tengan línea WhatsApp. Listo para ejecutar en un clic.
metadata:
  type: project
  fecha: 2026-06-29
  status: EN_ESPERA
---

# Bucaramanga — Lista de espera (no tocar hasta abrir sede)

> ⏸️ **PAUSADO** — La sede aún no está operativa. No gastar tiempo aquí hasta tener la línea de WhatsApp y la sede lista.
> Cuando Javier diga "abre Bucaramanga", ejecutar esta lista en orden.

---

## Datos de la sub-cuenta

| Campo | Valor |
|---|---|
| GHL Location ID | `s40Wa8mXYBxlFCieKohO` |
| Nombre | Innovart Medical IPS - Bucaramanga |
| API key | `pit-083c9e3c...` |
| Workflow 4.1 ID | `2efd5f03-79f8-45fe-bc82-a5bee8bdfddf` |
| Landing | `innovartmedical.com/pages/implante-capilar-bucaramanga` |

---

## Checklist de lanzamiento — ejecutar en orden

### 1. Línea WhatsApp / número de teléfono
- [ ] Conectar número de teléfono de Bucaramanga a GHL
- [ ] Verificar que el canal WhatsApp quede como canal por defecto en la sub-cuenta

### 2. Añadir paso SMS/WA al lead en workflow 4.1
El workflow actual (`2efd5f03`, v4) solo notifica al asesor. Falta el paso al lead.

**Pasos a ejecutar via MCP:**
```
switch_location → s40Wa8mXYBxlFCieKohO
update_workflow_actions → 2efd5f03-79f8-45fe-bc82-a5bee8bdfddf
Añadir después del paso "SMS al asesor":
  - type: sms
  - body: "Hola {{contact.first_name}} 👋 Soy tu asesor de Innovart Medical IPS Bucaramanga.
    Gracias por dejarnos tus datos 🙌 Estoy aquí para acompañarte y resolver cualquier duda
    sobre el procedimiento, resultados, cuidados o costos.
    Lo ideal siempre es una valoración presencial, pero antes podemos hablar con calma 😊
    ¿Hay algo específico que te gustaría saber primero?"
  - adjuntar Reel 3 (subir a GHL Bucaramanga primero)
```

### 3. Crear campos UTM en GHL Bucaramanga
Los campos UTM no están creados en esta sub-cuenta. El Worker ya envía los datos pero no tienen dónde guardarse.

**Campos a crear** (via MCP `create_custom_field`):
- `utm_source` (texto)
- `utm_medium` (texto)
- `utm_campaign` (texto)
- `utm_content` (texto)

> Nota: `fbclid` verificar si ya existe. En las otras sedes sí existía.

### 4. Verificar landing E2E
```
Ir a innovartmedical.com/pages/implante-capilar-bucaramanga
→ Llenar formulario Qikify
→ Confirmar contacto en GHL Bucaramanga con:
   - Tag: fuente_web_qikify ✅
   - Tag: landing_formulariov2 ✅
   - Campos UTM rellenos ✅
   - Oportunidad en Pipeline Ventas/Frío ✅
   - Lead recibe SMS de bienvenida ✅
```

### 5. Configurar asesores en el 4.1
El workflow actual asigna al usuario `Y1Lj2tAjeawnEoUwHy3B`. Confirmar que ese usuario es el asesor correcto de Bucaramanga cuando abra.

### 6. Verificar botones WhatsApp en landing
Los botones WA de la landing de Bucaramanga deben tener el número correcto de Bucaramanga (no el número Colombia genérico `573124565014` si van a tener número local).

### 7. Prueba E2E final antes de activar campañas
Usar [[protocolo-validacion-landing-automatica]] completo.

---

## Estado actual del stack Bucaramanga (al 29 jun 2026)

| Componente | Estado |
|---|---|
| Landing PageFly (`/pages/implante-capilar-bucaramanga`) | ✅ existe |
| Qikify → Worker → GHL | ✅ ruteo funcionando |
| Workflow 4.1 trigger | ✅ activo (tag `landing_formulariov2`) |
| 4.1 paso al lead | ❌ no existe |
| Campos UTM en GHL | ❌ no creados |
| Línea WhatsApp | ❌ sin línea |
| Asesor asignado | ⚠️ `Y1Lj2tAjeawnEoUwHy3B` — confirmar |
| Campaña Meta activa | ❌ (no hay campañas hasta abrir sede) |

---

## Archivos relacionados

- [[flujo-4-1-sms-lead-habilitado-2026-06-29]] — cómo se habilitó el paso en las otras sedes (misma lógica a aplicar aquí)
- [[flujo-crm-qikify-verificado-2026-06-29]] — flujo completo Qikify → GHL
- [[protocolo-validacion-landing-automatica]] — checklist post-deploy
