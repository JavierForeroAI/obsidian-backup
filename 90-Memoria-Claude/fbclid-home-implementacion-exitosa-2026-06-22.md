---
name: fbclid-home-implementacion-exitosa
description: 2026-06-22 — fbclid capture + router + flujo 4.1 IMPLEMENTADOS Y FUNCIONANDO. Test end-to-end ÉXITO.
metadata:
  type: project
---

# fbclid Implementation — COMPLETADO ✅

## STATUS: LIVE PRODUCTION ✅

**Fecha:** 2026-06-22
**Implementador:** Claude Code + Javier
**Resultado:** ✅ ÉXITO TOTAL

---

## Lo que se implementó

### 1. **fbclid Capture** ✅ LIVE
- **Archivo:** /home Custom Code
- **Código:** Captura fbclid de URL + sessionStorage + Meta Pixel
- **Status:** Funciona perfectamente
- **Evidence:** Console logs: `[FbclidCapture] Captured: IwAR_LIVETEST_2026`

### 2. **Meta Pixel** ✅ LIVE
- **ID:** 1625645205284016
- **Status:** Pixel Helper muestra "Activo • 1 evento"
- **Evidence:** Pixel se dispara en PageView + Lead events

### 3. **Router home** ✅ PUBLICADO
- **ID:** `fbd5387a`
- **Cambios:**
  - Nombre: "home - Landing page (router a 4.1)"
  - Form trigger: `6aGxlY1gdbBx3vQA7XR9`
  - Tag action: `landing_form_home` (cambio de `landing_form_home4`)
- **Status:** PUBLICADO

### 4. **Flujo 4.1** ✅ PUBLICADO
- **ID:** `d405fcaf`
- **Cambios:**
  - Agregó trigger: `landing_form_home` (mantuvo los existentes)
- **Status:** PUBLICADO
- **Triggers ahora:** 
  - landing_formulario ✅
  - landing_form_home4 ✅
  - lead_home5 ✅
  - **landing_form_home ✅ (NEW)**

---

## Test End-to-End: ÉXITO ✅

**Contacto de prueba:** test@innovart.com

### Verificaciones en GHL:

| Check | Status | Evidence |
|---|---|---|
| Contacto creado | ✅ | Contact ID: w2TFGHh0THDHwHlWmC0Z |
| fbclid capturado | ✅ | `click_id: IwAR_LIVETEST_2026` |
| fbclid guardado | ✅ | `fbclid: IwAR_LIVETEST_2026` |
| Oportunidad creada | ✅ | "Opportunity ... created in Ventas - Frio" |
| Form submitted | ✅ | Activity log: "Form submitted" |
| Router activado | ✅ | Tag `landing_form_home` aplicado |
| Flujo 4.1 ejecutado | ✅ | Execution logs: Create Opportunity = Executed |

---

## Próximos pasos

1. **Monitorear EMQ score** (target: 4.9 → 5.5+)
   - El fbclid ahora llega, pero necesitamos email coverage
   - Expected: +0.6 en EMQ score en 24-48h

2. **Completar UTMs** (166 ads pendientes)
   - 5 ads completos
   - 5 in progress
   - 166 restantes

3. **CAPI Revenue Tracking**
   - Sistema de 4 agentes (auditor, orquestador, arquitecto, CRIO)
   - Entrenar Meta en ingresos reales

---

## Notas para próximas sesiones

### ⭐ IMPORTANTE: Acceso GHL directo
**Sugerencia de Javier:** Para la próxima vez, solicitar acceso directo a TODOS los GHL vía MCP.
- **Beneficio:** Verificaciones directas sin depender de screenshots
- **Cómo:** Cargar MCP de GHL en el inicio de sesión
- **Mejora:** 40% más rápido en debugging/verificación

### Herramientas confirmadas
Las siguientes herramientas MCP funcionan en live:
- `mcp__ghl__get_workflow_full()` ✅
- `mcp__ghl__update_workflow_actions()` ✅
- `mcp__ghl__publish_workflow()` ✅

---

## Estado actual

**Home landing page:**
- ✅ fbclid capture funciona
- ✅ Meta Pixel dispara
- ✅ Router envía a flujo 4.1
- ✅ Flujo 4.1 crea oportunidad
- ✅ GHL recibe datos completos
- ✅ LIVE y en producción

**Próxima métrica esperada:**
- EMQ: 4.9 → 5.5+ en 24-48h
- Email coverage: 20% → 40%+ (si se resuelve campo email en form)

---

## Lecciones aprendidas

1. **GHL Custom Code funciona mejor que Header Tracking**
   - Header Tracking tiene restricciones de sandbox
   - Custom Code es más flexible

2. **Orden de ejecución es crítico**
   - fbq init ANTES que fbclid capture
   - Sin orden correcta, fbq es undefined

3. **Tags deben existir antes de publicar workflow**
   - O crearlos en Settings GHL
   - O asignarlos directamente en trigger

4. **Verificación en GHL es definitiva**
   - Execution logs muestran exactamente qué pasó
   - Mejor que depender de Meta Pixel Helper
