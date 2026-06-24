---
name: auditoria-fbclid-critica-2026-06-22
description: Auditoría crítica fbclid — causa raíz de bajo show rate y EMQ 4.9
metadata:
  type: project
---

# AUDITORÍA CRÍTICA: fbclid Capture — Show Rate y EMQ Root Cause

**Fecha:** 2026-06-22  
**Estado:** 🔴 BLOQUEANTE — Root cause identificada  
**Impacto:** 600+ eventos/mes perdidos | 20 leads/día sin atribución  
**Urgencia:** P0 — Implementar HOY  

---

## TL;DR — El Problema

| Aspecto | Realidad |
|---|---|
| **Campo fbclid en GHL** | ✅ Existe (ID: `ROjbROGU9919xi7GR9rO`) |
| **Contactos con fbclid** | ❌ CERO de 163K+ en 10 días |
| **Causa** | ❌ NO hay código JS capturando fbclid en landing |
| **Síntoma** | CAPI bloquea eventos → show rate ~40% |
| **Solución** | Inyectar 1.2 KB de JS en headTrackingCode |
| **Tiempo** | 25 min implementación + 30 min E2E |
| **ROI** | EMQ 4.9 → 5.5+, 600 eventos/mes recuperados |

---

## Fase 1: Auditoría (COMPLETADA)

### V1: ¿Llega fbclid a URL?
✅ **SÍ** — Meta Ad incluye `?fbclid=IwAR0...` en landing

### V2: ¿JavaScript lo CAPTURA?
❌ **NO** — BRECHA CRÍTICA ENCONTRADA
- home4 (live): 0% fbclid capture
- home5 (test): 0% fbclid capture
- Código de captura: NO EXISTE

### V3: ¿GHL tiene campo fbclid?
✅ **SÍ** — Campo creado 2026-06-11
- ID: `ROjbROGU9919xi7GR9rO`
- Tipo: TEXT
- Estado: **VACÍO** (nunca fue poblado)

### V4: ¿Webhook GHL→CAPI funciona?
✅ **SÍ** — Worker `innovart-capi-webhook-no-tocar` envía eventos a Meta

### V5: ¿CAPI Filter funciona?
✅ **SÍ** — Bloquea SubmitApplication sin fbclid **correctamente**

**Conclusión:** El filtro CAPI **NO es el problema**. El problema es la cascada:

```
Meta envía fbclid ✅ → JS NO lo captura ❌ → GHL no recibe ❌ → CAPI bloquea correctamente ✅
```

---

## Fase 2: Validación Técnica (COMPLETADA)

### Audit de Custom Fields

**Campos encontrados:**
1. `fbclid` (ROjbROGU9919xi7GR9rO) — **CORRECTO**, pero vacío
2. `fb_click_id` (wy6FYlxKsMDvtXljeC9O) — "Facebook Click ID" (redundante)
3. `ctwa_clid` (pmfzBxCFdjeojgCLmEWu) — "Click-to-WhatsApp Click ID"

**Recomendación:** Consolidar en UN campo (`fbclid`), deprecar los otros.

### Audit de headTrackingCode (home4)

**Ubicación:** PaBAMA8f6ISzy4H3HHty  
**Tamaño:** ~2.5 KB  
**Contiene:**
- ✅ Meta Pixel ×2 (init + tracking)
- ✅ Clarity tracking (x62cig8qug)
- ❌ JavaScript capturando fbclid — **FALTA**

**Código faltante (~0.5 KB):**
```javascript
const url = new URLSearchParams(window.location.search);
const fbclid = url.get('fbclid');
if (fbclid) {
  window.fbclid = fbclid;
  sessionStorage.setItem('fbclid', fbclid);
  // Pasar a form GHL
}
```

### Estado de Otras Landings

| Landing | Formulario | fbclid Capture | Status |
|---|---|---|---|
| home4 | GHL iframe | ❌ NO | LIVE — P0 FIX |
| home5 | GHL iframe | ❌ NO | TEST — P0 FIX |
| qikify | Shopify nativo | ❌ NO | LIVE — P1 FIX |
| /pages/contact | Shopify nativo | ❌ NO | LIVE — P1 FIX |

---

## Fase 3: Solución (LISTO PARA IMPLEMENTAR)

### Código a Inyectar (1.2 KB minificado)

**Archivo:** `/tmp/fbclid-capture-minified.js`

**Funcionalidad:**
1. Lee `?fbclid=...` del URL
2. Guarda en `window.fbclid` (memory)
3. Guarda en `sessionStorage` (persiste sesión)
4. Intercepta `fetch()` para inyectar en form submission
5. Hookea GHL internals si disponible

**Logs esperados:**
```javascript
[FbclidCapture] Captured fbclid: IwAR0... {stored: true}
[FbclidCapture] Init complete {fbclid: true, fbp: false}
```

### Ubicación de Inyección

**headTrackingCode de home4 page (`PaBAMA8f6ISzy4H3HHty`):**

```html
<!-- PRESERVAR: Clarity -->
<!-- Clarity x62cig8qug -->
<script async="true" src="https://www.clarity.ms/tag/x62cig8qug"></script>

<!-- AGREGAR: fbclid capture (NUEVO) -->
<script>
[1.2 KB CÓDIGO MINIFICADO]
</script>

<!-- PRESERVAR: Meta Pixel y resto -->
<!-- ... -->
```

**REGLA CRÍTICA:** Si actualizar en GHL, SIEMPRE enviar `headTrackingCode` + `bodyTrackingCode` juntos. Si omites body, se borra la tracking v10.

### Plan de Implementación

**Duración total:** 25 min crítico + 30 min E2E

1. **Backup** (2 min): Guardar headTrackingCode actual
2. **Inyección** (10 min): Pegar código via MCP o GHL UI
3. **Validación inmediata** (5 min): Console logs
4. **E2E Testing** (30 min): 5 tests (URL, localStorage, form, GHL contact, CAPI)

**Ver:** [[fbclid-home-implementacion-completa-2026-06-22]] para detalles paso a paso.

---

## Impacto Cuantificable

### Hoy (Sin fbclid)
```
Leads/día (home4):        20
Leads/semana:            140
Leads/mes:               600

Eventos sin fbclid:    100%
Eventos bloqueados CAPI: ~95% (ruido de eventos fantasma)
EMQ:                   4.9 (noche oscura)
Show rate:             ~40% (causa secundaria)
```

### Después de Fix (Con fbclid)
```
Leads/día (home4):        20
Leads/semana:            140
Leads/mes:               600

Eventos con fbclid:    100% (esperado)
Eventos aceptados CAPI:  ~95%
EMQ:                   5.5+ (estimado)
Show rate:             41-45%? (secundario, pero Meta aprende mejor)
```

**Nota:** fbclid NO es la panacea para show rate. El show rate depende del scheduling correcto, copywriting, y emparejamiento médico. Pero fbclid SÍ es crítico para que Meta entienda el funnel completo.

---

## Archivos Generados en Esta Auditoría

| Archivo | Propósito | Ubicación |
|---|---|---|
| auditoria-fbclid-fase1-hallazgos.md | Findings Fase 1 | `/Users/javierforero/` |
| [[fbclid-home-implementacion-completa-2026-06-22]] | Plan Fase 3 (copiar/pegar) + implementación completa | 2026-06-22 |
| fbclid-capture-solution.js | Código sin minificar (~5 KB) | `/tmp/` |
| fbclid-capture-minified.js | Código minificado (~1.2 KB) | `/tmp/` |
| check-ghl-fbclid.sh | Script validación Fase 2 | `/tmp/` |

---

## Estado de Implementación

- [ ] Fase 1 (Audit): ✅ COMPLETADA
- [ ] Fase 2 (Validación técnica): ✅ COMPLETADA
- [ ] Fase 3 (Implementación): ⏳ LISTO (por hacer HOY)
- [ ] Fase 4 (E2E validation): ⏳ POR HACER
- [ ] Fase 5 (Replicación a otras landings): 🔮 DESPUÉS

---

## Relación con Otras Iniciativas

### Estrategia de show rate (~40%)
- [[estrategia-meta-showrate-valoraciones]] menciona "optimizar por `Schedule` calificado vía CAPI"
- **fbclid es el prerequisito**: CAPI NO PUEDE entrenar sin fbclid
- **Impacto:** Este fix es tabla rasa para que Meta aprenda mejor

### Home5 CRO v10
- [[home5-cro-v10-deploy-2026-06-22]] tiene tracking events pero SIN fbclid
- **Recomendación:** Aplicar este fix a home5 también, para A/B test limpio

### Filtro CAPI
- [[filtro-capi-submitapplication-2026-06-22]] bloquea correctamente
- **Después del fix:** Filtro seguirá funcionando, pero bloqueará MENOS (porque fbclid llegará)

---

## Reglas para el Futuro

### 📋 Nueva Standard: Toda landing DEBE capturar fbclid

**Aplicar a:**
1. Cualquier form nuevo en innovartmedical.com
2. Cualquier page builder (PageFly, GemPages)
3. Cualquier landing externa (Shopify pages, etc)

**Checklist pre-publicación:**
- [ ] headTrackingCode contiene fbclid capture JS
- [ ] GHL form mapea field fbclid
- [ ] Test E2E con ?fbclid=TEST
- [ ] Verificar GHL contact tiene valor

**Documento:** [[feedback_fbclid_landing_pages]] (crear)

---

## FAQ

**P: ¿Por qué no se capturó fbclid antes?**
R: Código nunca fue escrito. El campo se creó 2026-06-11 pero no se completó la implementación.

**P: ¿Esto sube el show rate?**
R: Indirectamente. Show rate depende del copywriting y scheduling. Pero fbclid permite Meta atribuir mejor → EMQ sube → algoritmo mejora.

**P: ¿Qué pasa si el lead NO viene de Meta Ad?**
R: fbclid será nulo. Es OK. CAPI solo usa fbclid si está disponible; no es requerido.

**P: ¿Esto afecta home4 live?**
R: Sí. Si implementas hoy, nuevos leads desde mañana tendrán fbclid. Sin break.

**P: ¿Cuánto tiempo tarda en verlo en Meta?**
R: Meta CAPI recibe evento en ~5 min. EMQ se recalcula cada 24h. Verás cambio en ~1 semana.

---

## Próximos Pasos

### HOY (2026-06-22)
1. ✅ Leer este documento
2. 🔧 Implementar Fase 3 (25 min)
3. ✅ Validar E2E (30 min)
4. 📊 Monitorear logs CAPI worker

### Mañana (2026-06-23)
1. 📈 Revisar: ¿nuevos leads tienen fbclid?
2. 🔄 Replicar fix a home5 (A/B clean)
3. 📝 Documentar learnings

### Semana que viene (2026-06-28)
1. 📊 Ver EMQ (¿4.9 → 5.5+?)
2. 🔄 Replicar a qikify + /pages/contact
3. 📋 Crear standard "fbclid para toda landing"

---

**Versión:** 2.0 Auditoria Completa | **Fecha:** 2026-06-22 | **Estado:** ✅ LISTO PARA FIX | **Propietario:** Javier Forero | **Cliente:** Innovart Medical IPS
