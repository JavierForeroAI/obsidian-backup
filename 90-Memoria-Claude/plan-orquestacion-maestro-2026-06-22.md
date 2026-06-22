---
name: plan-orquestacion-maestro-2026-06-22
description: Plan maestro de orquestación — qué hacer después que terminan Terminal 1 (CRO) y Terminal 2 (Auditoría fbclid). Coordinación de 4 fases en paralelo/secuencial.
metadata:
  type: project
  estado: esperando-terminales
  fecha: 2026-06-22
---

# PLAN MAESTRO DE ORQUESTACIÓN — Innovart Tracking & CRO

## 🎯 ESTADO ACTUAL (22-JUN 9:50pm)

| Terminal | Tarea | ETA | Bloqueador |
|---|---|---|---|
| **#1** | CRO home4/home5 (Guardar + Publicar) | ~5 min | Ninguno |
| **#2** | Auditoría fbclid + Plan implementación | ~7 min | Ninguno |
| **#MAIN** | Orquestación | ⏳ ESPERA | Ambas tareas |

---

## 📊 DESPUÉS QUE TERMINEN AMBAS TERMINALES

### **FASE 1: SÍNTESIS (10 min)**

**Lugar:** Terminal MAIN (aquí)
**Tareas:**
```
[ ] 1. Leer output completo Terminal #1 (CRO finalizado)
[ ] 2. Leer output completo Terminal #2 (Plan fbclid)
[ ] 3. Integrar ambos resultados en 1 documento maestro
[ ] 4. Crear CHECKLIST DE VALIDACIÓN unificado
[ ] 5. Documentar en Obsidian Innovart
```

**Outcome:** Plan de ejecución de 4 fases, priorizado por impacto.

---

### **FASE 2: VALIDACIÓN TÉCNICA (15 min)**

**Lugar:** Terminal MAIN
**Tareas en PARALELO:**

**2a. Validar CRO home5 (5 min)**
```bash
# Verificar que home5 fue deployada correctamente
[ ] ✓ Home5 trackingCode v10 inyectado
[ ] ✓ bodyTrackingCode presente (sticky bar + CTA)
[ ] ✓ headTrackingCode preservado (Clarity, GA, etc.)
[ ] ✓ Form conectado a router ac1b818d
[ ] ✓ Tag lead_home5 dispara correctamente
```

**2b. Validar plan fbclid (5 min)**
```bash
# Verificar que el plan de inyección está listo
[ ] ✓ Script fbclid minificado y listo
[ ] ✓ Ubicación de inyección definida (headTrackingCode)
[ ] ✓ Campos GHL identificados (fbclid custom field)
[ ] ✓ Webhooks cableados correctamente
[ ] ✓ Impacto estimado: 600 eventos/mes recuperados
```

**2c. Validar CAPI Worker (5 min)**
```bash
# Confirmar que el worker está listo para recibir fbclid
[ ] ✓ Filter SubmitApplication vivo
[ ] ✓ Espera fbclid en user_data
[ ] ✓ Logs accesibles en Cloudflare
[ ] ✓ Backup de versión anterior guardado
```

---

### **FASE 3: IMPLEMENTACIÓN PARALELA (30 min)**

**Este es el CORAZÓN del orquestación. 4 tareas en paralelo:**

#### **3A. Inyección fbclid en home4 (10 min)**
```
[ ] Traer home4 completa vía MCP
[ ] Inyectar script fbclid en headTrackingCode
[ ] Preservar: Clarity tracking + headTrackingCode existente
[ ] Guardar cambios
[ ] Validar en DevTools (console + network)
```

#### **3B. Inyección fbclid en home5 (10 min)**
```
[ ] Traer home5 completa vía MCP
[ ] Inyectar script fbclid en headTrackingCode
[ ] Preservar: bodyTrackingCode v10 que ya está
[ ] Guardar cambios
[ ] Validar en DevTools (console + network)
```

#### **3C. Monitoreo CAPI Worker (10 min)**
```
[ ] Abrir Cloudflare dashboard
[ ] Ir a: innovart-capi-webhook-no-tocar
[ ] Leer logs de últimos 30 min
[ ] Buscar: eventos con fbclid (deben pasar)
[ ] Buscar: eventos sin fbclid (deben ser bloqueados)
[ ] Documentar: baseline de eventos bloqueados/día
```

#### **3D. Setup A/B Testing (10 min)**
```
[ ] Verificar que home4 + home5 tienen tags distintos
[ ] home4 → tag: lead_home4
[ ] home5 → tag: lead_home5
[ ] Crear smart list por tag en GHL
[ ] Preparar dashboard de comparación
```

**⚠️ IMPORTANTE:** Las 4 tareas pueden correr EN PARALELO. Cada una es independiente.

---

### **FASE 4: VALIDACIÓN E2E (20 min)**

**Lugar:** Simulación + DevTools

#### **4A. Test de captura fbclid**
```javascript
// En DevTools console de home4/home5:
console.log(document.cookie)  // Debe mostrar: inv_fbclid=IwAR0...
console.log(window.fbclid)     // Alternativa si está en memory
```

#### **4B. Test E2E completo**
```
1. Abrir home4 en navegador incognito
2. Agregar ?fbclid=TEST123 a la URL
3. Llenar form
4. Verificar GHL: ¿llegó fbclid en custom field?
5. Verificar CAPI worker logs: ¿fue aceptado?
6. Repetir con home5
```

#### **4C. Validar diferencia home4 vs home5 (A/B)**
```
home4 (CONTROL): 
  - Sin fbclid capturado previamente
  - SubmitApplication → BLOQUEADO por CAPI
  - Events: Lead solo (no Schedule)

home5 (TRATAMIENTO):
  - Con fbclid capturado
  - SubmitApplication → ACEPTADO por CAPI (con fbclid)
  - Events: Lead + fbclid en CAPI
```

---

### **FASE 5: REPORTE & DOCUMENTACIÓN (15 min)**

**Lugar:** Terminal MAIN (Obsidian)

#### **5A. Crear reporte de implementación**
```markdown
# Implementación fbclid Capture — 2026-06-22

## Cambios realizados
- home4: inyectado script fbclid en headTrackingCode
- home5: inyectado script fbclid en headTrackingCode
- CAPI filter: verificado + logs baseline

## Validación E2E
- ✓ fbclid se captura en cookies
- ✓ Se envía a GHL en custom field
- ✓ CAPI lo recibe y lo envía a Meta
- ✓ Eventos con fbclid: ACEPTADOS
- ✓ Eventos sin fbclid: BLOQUEADOS (correcto)

## Métrica de éxito
- Baseline: 0 eventos/mes con fbclid
- Meta: 600+ eventos/mes con fbclid
- Timeline: medir en 7 días
```

#### **5B. Actualizar memoria Innovart**
```
[ ] Crear: implementacion-fbclid-capture-2026-06-22.md
[ ] Actualizar: MEMORY.md con link
[ ] Grabar: logs de Cloudflare (baseline)
[ ] Documentar: A/B testing setup
```

#### **5C. Crear dashboard de monitoreo**
```
[ ] Configurar alertas Cloudflare (eventos bloqueados/día)
[ ] Crear smart list GHL: contacts con fbclid vs sin fbclid
[ ] Crear query Meta Ads Manager: Schedule events con fbclid
[ ] Timeline: revisar resultados en 7 días
```

---

## 🗓️ TIMELINE TOTAL

```
AHORA (22-JUN 9:50pm)
  ├─ Terminal #1 finaliza CRO (5 min) → 10:00pm
  ├─ Terminal #2 finaliza fbclid plan (7 min) → 10:07pm
  └─ Espera a ambas completar
         ↓
FASE 1: Síntesis (10 min) → 10:17pm
  ├─ Leer outputs
  └─ Integrar en plan maestro
         ↓
FASE 2: Validación técnica (15 min) → 10:32pm
  ├─ Verificar CRO
  ├─ Verificar plan fbclid
  └─ Verificar CAPI worker
         ↓
FASE 3: Implementación PARALELA (30 min) → 11:02pm
  ├─ 3A: fbclid home4
  ├─ 3B: fbclid home5
  ├─ 3C: monitoreo CAPI
  └─ 3D: A/B testing setup
         ↓
FASE 4: Validación E2E (20 min) → 11:22pm
  ├─ Test captura fbclid
  ├─ Test E2E completo
  └─ Validar A/B (home4 vs home5)
         ↓
FASE 5: Reporte & docs (15 min) → 11:37pm

TOTAL: 90 min desde aquí (asumo ambas terminales terminan a las 10:10pm)
FIN: 11:40pm (hoy 2026-06-22)
```

---

## 📋 CHECKLIST MAESTRO

```
PREPARACIÓN (mientras esperamos terminales):
[ ] Leer esta lista completa
[ ] Tener Obsidian abierto en otra ventana
[ ] Tener Cloudflare dashboard listo
[ ] Tener DevTools abierto (para test E2E)

DESPUÉS TERMINALES:
[ ] Fase 1: Síntesis (leer + integrar)
[ ] Fase 2: Validación (3 sub-tareas)
[ ] Fase 3: Implementación (4 tareas en paralelo)
[ ] Fase 4: E2E testing
[ ] Fase 5: Documentación + dashboard

SEMANA 1 (DESPUÉS DE ESTO):
[ ] Monitorear CAPI logs (eventos bloqueados/día)
[ ] Comparar home4 vs home5 (tag lead_home4 vs lead_home5)
[ ] Revisar show rate (debería mejorar con fbclid valido)
[ ] Ajustar si es necesario
```

---

## ⚡ DECISIONES CRÍTICAS (decide ahora)

**P1: ¿A/B Testing o rollout directo?**
- [ ] Opción A: A/B (home4 vs home5, 50/50 split) — más lento pero seguro
- [ ] Opción B: Rollout directo a ambas (home4 + home5) — más rápido, mayor riesgo

**P2: ¿Cuándo empezar monitoreo?**
- [ ] Hoy mismo (22-JUN) → baseline de 0 eventos con fbclid
- [ ] Mañana (23-JUN) → esperar 24h antes de medir

**P3: ¿Notificar a equipo?**
- [ ] Sí, enviar resumen a Esneider + Diego
- [ ] No, esperar a validación completa

---

## 🎯 OBJETIVO FINAL

**Después de esta sesión:**
- ✅ fbclid se captura en home4 + home5
- ✅ CAPI worker lo recibe y lo procesa
- ✅ Meta recibe Schedule eventos CON fbclid (identidad válida)
- ✅ Show rate debería mejorar (menos eventos bloqueados)
- ✅ A/B test activo (home4 vs home5)
- ✅ Dashboard de monitoreo listo

---

**Actualizado:** 2026-06-22 9:50pm
**Status:** Esperando terminales #1 y #2
**Próximo:** Confirma decisiones críticas (P1, P2, P3) mientras esperas
