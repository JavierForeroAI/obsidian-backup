---
name: PENDIENTE-trigger-utm-wa-tracker
description: Tarea pausada — arreglar trigger Firebase en 5 workflows UTM WA Directo Tracker. Continuar después de educación sobre setup GHL.
metadata:
  type: project
  date: 2026-06-28
  status: PAUSADO
---

# PENDIENTE — Arreglar trigger UTM WA Directo Tracker (5 sub-cuentas)

## Por qué está pausado
Javier va a explicar primero el setup completo de GHL para tener contexto correcto antes de continuar.

## Qué falta hacer

### El problema
5 workflows tienen `triggersFilePath: null` → el trigger "Customer replied" existe en MongoDB pero NO en Firebase → GHL nunca los dispara.
- ✅ Bogotá `ec3d0cbb` — YA funciona (triggersFilePath correcto)
- ❌ Medellín `2fe984c3` — PENDIENTE (builder abierto en tab 863674560)
- ❌ Barranquilla `e1c8709e` — PENDIENTE
- ❌ Bucaramanga `d10dcfdc` — PENDIENTE
- ❌ Panamá `5722994e` — PENDIENTE
- ❌ Principal `cf7e99e5` — PENDIENTE

### La solución
Entrar al builder UI de GHL por cada workflow y guardar el trigger con el filtro correcto. Esto escribe a Firebase y activa el trigger.

### Filtro correcto (CRÍTICO — aprendido hoy)
Innovart tiene DOS líneas de WhatsApp:
- **Applevel WhatsApp** → aparece como **SMS** en GHL → filtrar `Reply channel = SMS`
- **API WhatsApp** (Meta Business) → aparece como **WhatsApp** en GHL → filtrar `Reply channel = WhatsApp`

**Decisión pendiente:** ¿un workflow con SMS solamente? ¿dos workflows (SMS + WhatsApp)? ¿sin filtro?

### Cómo entrar al builder sin pantalla en blanco
1. Ir a la LISTA de workflows de la sub-cuenta
2. Buscar "UTM - WA Directo Tracker"
3. Hacer clic en la fila del workflow (no en botones de acción)
4. El builder abre correctamente

### URLs de cada sub-cuenta
- Medellín: `https://app.gohighlevel.com/v2/location/h8DplQKVE6epDbbj5Kg8/automation/workflows`
- Barranquilla: `https://app.gohighlevel.com/v2/location/cXH8KbMaAPGzkmf3Z2pP/automation/workflows`
- Bucaramanga: `https://app.gohighlevel.com/v2/location/s40Wa8mXYBxlFCieKohO/automation/workflows`
- Panamá: `https://app.gohighlevel.com/v2/location/45SKYgIDgr4Eh6a6JcFz/automation/workflows`
- Principal: `https://app.gohighlevel.com/v2/location/NPhQTmLOHd6FbDtqLPnG/automation/workflows`

## Relacionado
- [[ghl-whatsapp-tipos-lineas]]
- [[feedback-whatsapp-applevel-sms]]
- [[BRIEF-whatsapp-directo-tracking]]
