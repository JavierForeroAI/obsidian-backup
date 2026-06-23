---
name: auditoria-home4-vs-home-integral-2026-06-23
description: "Auditoría INTEGRAL home4 (qué funciona) vs home (nueva URL) — Migración perfecta de fuentes, workflows, tracking y configuración"
metadata:
  type: audit
  severidad: P0_BLOQUEANTE
  date: 2026-06-23
---

# Auditoría INTEGRAL: home4 (LIVE) vs home (nueva) — Configuración Paralela

## Hallazgo Ejecutivo

**home4** (`implantecapilarencolombia.com/home4`) está **auditada, instrumentada y VIVA**. **home** (`implantecapilarencolombia.com/home`) **existe pero está DESCOORDINADA**: no se ha verificado su interior (formulario, tracking, workflows, tags). **Riesgo crítico:** leads podrían caer en el vacío o duplicarse.

---

## ESTADO ACTUAL POR CAPA

### CAPA 1: GHL — ORGANIZACIÓN DE ESTRUCTURAS

#### Funnel Principal (home4)
```
Landing 1 Home (funnel_id: 6gDZimr1JRoW9iQZZnRH)
├─ page home4 (PaBAMA8f6ISzy4H3HHty)
│  └─ URL: implantecapilarencolombia.com/home4
│  └─ Clarity: x62cig8qug
├─ page home5 (F6xTmSqYRLizoZ1SJmDg) ← A/B test
│  └─ URL: implantecapilarencolombia.com/home5
│  └─ Clarity: x62cig8qug (compartida)
└─ page home (¿?) ← DESCONOCIDA
   └─ URL: implantecapilarencolombia.com/home
   └─ Clarity: ¿?
```

#### Formularios GHL (Bogotá)

| Nombre | ID | Ubicación | Estado | Campos |
|---|---|---|---|---|
| **Diagnostico Capilar Bogota** | `6aGxlY1gdbBx3vQA7XR9` | home4 vivo | ACTIVO | nombre, email, teléfono, fbclid, utm_*, fbp |
| Diagnóstico Capilar — Home5 (A/B) | `RB4a58CCebT51AOpuyPd` | home5 vivo | ACTIVO | ídem |
| Formulario Landing page 1 | `huSVZkJqk19eAPi3Xg9E` | alternativo | ACTIVO pero no usar | ídem |
| **home form** | `¿?` | **home vivo** | **⛔ DESCONOCIDO** | ¿? |

**Crítica:** Si home usa un form_id distinto a estos, los routers NO dispararán.

#### Routers (Bogotá)

| Nombre | ID | Triggers | Acciones | Status |
|---|---|---|---|---|
| **Home4 - Landing page 1** | `fbd5387a` | form_submission (6aGxlY1g, huSVZkJqk19eAPi3Xg9E) | add_tag: landing_form_home4 + notify Sofia | ✅ PUBLICADO |
| **Home5 - Landing page** | `ac1b818d` | form_submission (RB4a58...) | add_tag: lead_home5 | ✅ PUBLICADO |
| **home router** | `¿?` | form_submission (**home_form_id**) | add_tag: **home_tag** | **⛔ DESCONOCIDO** |

#### Flujo Destino (4.1)

```
Workflow: 4.1 Recibir lead de Landing_formulario (d405fcaf)
├─ Triggers: 
│  ├─ tag: landing_formulario (original)
│  ├─ tag: landing_form_home4 (home4) ✅
│  └─ tag: lead_home5 (home5) ⚠️ Sin verificar en vivo
├─ Acciones (todos igual):
│  ├─ Crea oportunidad Ventas/Frio
│  ├─ Asigna: Sofia Forero (ajPncm2f7Yvjgle1kZwy)
│  └─ intentos_llamada = 1
└─ Status: ✅ PUBLICADO
```

**Problema:** Si home tiene nuevo tag, flujo 4.1 NO lo dispara.

#### Tags (Bogotá)

| Tag | ID | Used By | Status |
|---|---|---|---|
| landing_form_home4 | JGGnenesICFOCpT0Bc9H | home4 router | ✅ |
| lead_home5 | [¿?] | home5 router | ⚠️ Verificar en vivo |
| landing_formulario | [original] | 4.1 origen | ✅ |
| **landing_form_home** | **¿?** | **home router (si existe)** | **⛔ DESCONOCIDO** |

---

### CAPA 2: META — PÍXELES Y EVENTOS

#### Píxeles
- **GHL Home4/5:** `1625645205284016` (termina en 62, live)
- **Alternativo:** `1642103999710262`
- **Clarity:** `x62cig8qug` (compartida home4/home5)

#### Eventos Disparados (home4)

```javascript
// VIVO EN home4:
fbq('track', 'PageView', { fbclid: ... })           // ✅ cada página load
fbq('track', 'InitiateCheckout', {...})             // ✅ 4 CTAs (Hero, Qualify, Results, Testimonios)

// PROBLEMA:
fbq('track', 'Lead')  // ⚠️ INFLADO: se dispara con set-sticky-contacts + cada clic WA, NO con form envío
```

#### EMQ Scoring
- **Actual:** 4.9
- **Target:** ≥6
- **Bloqueante:** fbclid NUNCA llega → 600+/mes eventos perdidos

---

### CAPA 3: HOME (NUEVA URL) — INCÓGNITA

| Aspecto | home4 | home |
|---|---|---|
| **URL viva** | ✅ `implantecapilarencolombia.com/home4` | ✅ HTTP 200 |
| **Hosting** | PageFly (GHL) | PageFly (GHL) |
| **Formulario ID** | `6aGxlY1g` | **¿?** |
| **headTrackingCode** | Clarity + fbclid capture | **⛔ DESCONOCIDO** |
| **bodyTrackingCode** | Meta Pixel + eventos | **⛔ DESCONOCIDO** |
| **Router GHL** | fbd5387a | **⛔ DESCONOCIDO** |
| **Tag lead** | landing_form_home4 | **⛔ DESCONOCIDO** |
| **Flujo 4.1 trigger** | ✅ Sí (por tag) | **¿ Depende del tag** |
| **Email/SMS post** | ✅ Sí (flujo 4.1) | **¿ Depende de flujo 4.1** |

---

## RIESGOS CRÍTICOS (P0)

### R1: home no tiene formulario confirmado
**Impacto:** Leads caen al vacío (no crean contacto GHL).
**Causa:** home4 es la única landing auditada internamente.
**Fix:** Leer página viva home en GHL, extraer form_id.

### R2: fbclid capture desconocido en home
**Impacto:** EMQ seguiría siendo 4.9 en home (600+/mes perdidos).
**Causa:** No se verificó headTrackingCode exacto de home.
**Fix:** Comparar headTrackingCode home vs home4 (byte-exacto).

### R3: Router home no existe o está desconectado
**Impacto:** Form submit home → no dispara tag → flujo 4.1 no corre.
**Causa:** Router aún no creado o home usa form_id que nadie trackea.
**Fix:** Crear router o mapear form_id existente.

### R4: Flujo 4.1 podría no cubrir home tag
**Impacto:** Leads home crean contacto GHL pero no crean oportunidad.
**Causa:** Triggers en 4.1 aún no incluyen home_tag.
**Fix:** Verificar y actualizar 4.1 triggers si es necesario.

### R5: Migración A/B incompleta
**Impacto:** home4 sigue LIVE con tráfico viejo → test no limpio, datos contaminados.
**Causa:** home en construcción, home4 aún activo.
**Fix:** Dirigir tráfico a home paso a paso (50/50) o cortar home4 cuando home esté lista.

---

## COMPARATIVA DETALLADA: home4 vs home

### Formulario
**home4:** `6aGxlY1gdbBx3vQA7XR9` (Diagnostico Capilar Bogota)
- Campos: nombre, apellido, email, teléfono
- Custom fields capturados: fbclid, fb_click_id, utm_source/medium/campaign/content, utm_id, fbp
- Status: ACTIVO, histórico
- **Validación:** ✅ FUNCIONAL

**home:** ¿?
- **Validación:** ⛔ BLOQUEANTE

**Fix requerido:** home debe usar MISMO form_id o clon byte-equivalente

---

### Tracking — headTrackingCode (Clarity + fbclid)
**home4:** 
```html
<!-- Clarity x62cig8qug -->
<script>
  const fbclid = params.get('fbclid');
  if (fbclid) {
    window.fbclid = fbclid;
    sessionStorage.setItem('fbclid', fbclid);
    console.log('[FbclidCapture] Captured:', fbclid);
    window.fbq('track', 'PageView', { fbclid: fbclid });
  }
</script>
```
- **Clarity ID:** x62cig8qug
- **fbclid capture:** sí, básico
- **Status:** ✅ FUNCIONAL

**home:** ¿?
- **Validación:** ⛔ BLOQUEANTE

**Fix requerido:** home debe tener MISMO headTrackingCode o equivalente (misma Clarity ID)

---

### Tracking — bodyTrackingCode (Meta Pixel + eventos)
**home4:**
```javascript
// Meta Pixel 1625645205284016
fbq('init', '1625645205284016');
fbq('track', 'PageView', {...});
fbq('track', 'InitiateCheckout', {...});  // 4 CTAs

// Sticky WhatsApp
fbq('track', 'WhatsAppClick', {...});
```
- **Píxeles:** 1625645205284016
- **Eventos:** PageView, InitiateCheckout, WhatsAppClick
- **Status:** ✅ FUNCIONAL

**home:** ¿?
- **Validación:** ⛔ BLOQUEANTE

**Fix requerido:** home debe tener MISMO bodyTrackingCode o equivalente (mismo pixel ID + eventos)

---

### Routing GHL (form → tag → flujo)
**home4:**
```
form_submission (6aGxlY1g)
  ↓ router fbd5387a
  ↓ add_tag: landing_form_home4
  ↓ notify Sofia
  ↓ trigger flujo 4.1 (tag: landing_form_home4)
  ↓ create oppty + assign Sofia + intentos_llamada=1
  ↓ SMS + email
```
- **Router:** fbd5387a ✅
- **Tag:** landing_form_home4 ✅
- **Flujo destino:** 4.1 ✅
- **Status:** ✅ FUNCIONAL

**home:**
```
form_submission (¿?)
  ↓ router (¿?)
  ↓ tag (¿?)
  ↓ trigger flujo 4.1?
  ↓ ???
```
- **Validación:** ⛔ BLOQUEANTE

**Fix requerido:** 
1. Crear router si no existe
2. Mapear form_id exacto
3. Crear tag home_tag si no existe
4. Verificar flujo 4.1 cubre el tag

---

### Email/SMS Post-Formulario
**home4:** vía flujo 4.1
- SMS automático (3 intentos)
- Email de confirmación
- Oportunidad Ventas/Frio
- Asignación automática a Sofia
- **Status:** ✅ FUNCIONAL

**home:** depende de flujo 4.1 trigger
- **Validación:** ⛔ BLOQUEANTE si 4.1 no se dispara

---

### Campos Custom Mapeados
**home4:**
| Campo | GHL ID (Bogotá) | Carátula | Status |
|---|---|---|---|
| fbclid | `DnKbVMv2xH3kNEksDV5h` | fb_click_id | ✅ |
| utm_source | `bRG4YVkotWP9YjicYhnA` | utm_source | ✅ |
| utm_medium | `GYiGihp4RIr2kVk34C2i` | utm_medium | ✅ |
| utm_campaign | `MBNCUu8uyZbQassuPs6r` | utm_campaign | ✅ |
| utm_content | `ZZOmsPTSRhnKhUvSGgVu` | utm_content | ✅ |
| utm_id | `JOd9jgxiWgfTxiyHWGTJ` | utm_id | ✅ |
| fbp | `xqGgBJ8iteGTBGOzRYeY` | fbp (vacío) | ⚠️ |

**home:** ¿?
- **Validación:** ⛔ BLOQUEANTE

**Fix requerido:** home debe mapear los MISMOS custom fields (IDs iguales en Bogotá)

---

## PLAN DE IGUALACIÓN (HOME → HOME4)

### Fase 0: Auditoría Internal (HOY)
**Tarea T1:** Leer página viva home en GHL

```
GHL Bogota (DgjjDzD9nkCKv8AGF1Qb)
→ Funnel 6gDZimr1JRoW9iQZZnRH
→ Pages
→ Buscar "home" (no solo home4/home5)
→ Si existe: abrirla
→ Extraer:
   - page_id (ej. PaBAMA8f6ISzy4H3HHty)
   - form_id incrustado
   - headTrackingCode (Clarity ID, fbclid capture)
   - bodyTrackingCode (Meta Pixel, eventos)
```

**Responsable:** Claude (MCP GHL)
**Duración:** 10 min
**Bloqueante:** Datos de home

---

### Fase 1: Igualar Estructura (Day 1)

**Tarea T2:** Si home form ≠ 6aGxlY1g → clonar form home4

```
Opción A: home usa 6aGxlY1g (mismo que home4)
  → No hace nada

Opción B: home usa form_id distinto
  → Clone 6aGxlY1g → nuevo ID
  → Mapear custom fields igual
  → Embeber en home

Opción C: home NO tiene form
  → Crear form nuevo
  → Clonar 6aGxlY1g como plantilla
  → Embeber en home
```

**Responsable:** Claude (MCP) o Esneider (dev manual)
**Duración:** 30-45 min
**Resultado:** home.form_id ∈ {6aGxlY1g, RB4a58, home_clone_id}

---

**Tarea T3:** Inyectar tracking code home = home4

```
Si home.headTrackingCode ≠ home4.headTrackingCode:
  → Extraer home4.headTrackingCode exacto (incluye Clarity x62cig8qug + fbclid)
  → Inyectar en home.headTrackingCode
  → Validar Clarity ID = x62cig8qug en ambas
  
Si home.bodyTrackingCode ≠ home4.bodyTrackingCode:
  → Extraer home4.bodyTrackingCode exacto (Meta Pixel + eventos)
  → Inyectar en home.bodyTrackingCode
  → Validar Meta Pixel = 1625645205284016 en ambas
```

**Responsable:** Claude (MCP GHL)
**Duración:** 20-30 min
**Validación:** Console F12 en home = Console en home4 (sin errores JS)

---

### Fase 2: Routing & Workflows (Day 1-2)

**Tarea T4:** Crear router para home si no existe

```
Si router (home) ≠ existe:
  → Crear workflow router
  → Name: "Home - Landing page (router a 4.1)"
  → Trigger: form_submission (home.form_id)
  → Action: add_contact_tag (landing_form_home)
  → Action: notify_internal (Sofia)
  → Publish
```

**Responsable:** Claude (MCP GHL)
**Duración:** 15 min
**Bloqueante:** home.form_id debe estar confirmado (T1)

---

**Tarea T5:** Crear tag landing_form_home si no existe

```
Si tag landing_form_home ≠ existe:
  → Create tag
  → Name: landing_form_home
  → Color: (mismo que landing_form_home4)
  → Use in router home
```

**Responsable:** Claude (MCP GHL)
**Duración:** 5 min

---

**Tarea T6:** Actualizar flujo 4.1 triggers para cubrir home

```
Workflow 4.1 (d405fcaf)
├─ Trigger 1: tag: landing_formulario ✅
├─ Trigger 2: tag: landing_form_home4 ✅
├─ Trigger 3: tag: lead_home5 ✅
└─ Trigger 4: tag: landing_form_home ← AGREGAR

Acciones: mantener igual (crean oppty, asignan Sofia, etc.)
Publish
```

**Responsable:** Claude (MCP GHL)
**Duración:** 10 min
**Validación:** Verificar triggers en vivo

---

### Fase 3: A/B Test (Week 1)

**Tarea T7:** Routing de tráfico 50/50 home vs home4

```
Meta Ads (Esneider):
  → 50% tráfico → implantecapilarencolombia.com/home
  → 50% tráfico → implantecapilarencolombia.com/home4
  
GHL Smart Lists:
  → List: leads_home (filter by tag: landing_form_home)
  → List: leads_home4 (filter by tag: landing_form_home4)
  
KPIs por 7 días:
  - form_submission rate
  - lead_quality (fbclid captured %)
  - EMQ home vs home4
  - show_rate
  - conversion_rate
```

**Responsable:** Esneider (Media Buyer) + Claude (Analytics)
**Duración:** 7 días
**Decisión:** Ganador avanza 100%, perdedor retírase

---

## CHECKLIST DE IGUALACIÓN

```
[] 1. Auditoria T1 — home page_id extraído
[] 2. T1 — home form_id confirmado
[] 3. T1 — home headTrackingCode copiado
[] 4. T1 — home bodyTrackingCode copiado
[] 5. T2 — home formulario clonado o verificado = home4
[] 6. T3 — headTrackingCode inyectado (Clarity x62cig8qug)
[] 7. T3 — bodyTrackingCode inyectado (Pixel 1625645205284016)
[] 8. T4 — Router home creado (fbd5387a clonado)
[] 9. T5 — Tag landing_form_home creado
[] 10. T6 — Flujo 4.1 triggers actualizados (+landing_form_home)
[] 11. T6 — Flujo 4.1 publicado
[] 12. T7 — Tráfico routed 50/50
[] 13. T7 — KPIs medidos (7 días)
[] 14. Decisión — ganador seleccionado
[] 15. Retiro perdedor (si aplica)
```

---

## CONFIGURACIÓN FINAL (JSON)

```json
{
  "account": "Innovart Medical IPS Bogota",
  "account_id": "DgjjDzD9nkCKv8AGF1Qb",
  "funnel": {
    "name": "Landing 1 Home",
    "id": "6gDZimr1JRoW9iQZZnRH"
  },
  "pages": {
    "home4": {
      "page_id": "PaBAMA8f6ISzy4H3HHty",
      "url": "implantecapilarencolombia.com/home4",
      "form_id": "6aGxlY1gdbBx3vQA7XR9",
      "router_id": "fbd5387a",
      "tag": "landing_form_home4",
      "clarity_id": "x62cig8qug"
    },
    "home5": {
      "page_id": "F6xTmSqYRLizoZ1SJmDg",
      "url": "implantecapilarencolombia.com/home5",
      "form_id": "RB4a58CCebT51AOpuyPd",
      "router_id": "ac1b818d",
      "tag": "lead_home5",
      "clarity_id": "x62cig8qug"
    },
    "home": {
      "page_id": "[VERIFICAR T1]",
      "url": "implantecapilarencolombia.com/home",
      "form_id": "[VERIFICAR T1]",
      "router_id": "[CREAR T4]",
      "tag": "landing_form_home",
      "clarity_id": "x62cig8qug"
    }
  },
  "workflow_destino": {
    "id": "d405fcaf",
    "name": "4.1 Recibir lead de Landing_formulario",
    "triggers": [
      "tag: landing_formulario",
      "tag: landing_form_home4",
      "tag: lead_home5",
      "tag: landing_form_home"
    ]
  },
  "pixel": {
    "ghl": "1625645205284016"
  }
}
```

---

## REFERENCIAS RELACIONADAS

- [[home4-no-trackea-clics-cro]] — diagnosis Clarity + fixes P0
- [[home5-cro-v10-deploy-2026-06-22]] — A/B test home5
- [[landing-home4-routing]] — ruteo home4 en GHL
- [[auditoria-fbclid-critica-2026-06-22]] — root cause EMQ 4.9
- [[feedback_fbclid_landing_pages]] — regla fbclid obligatorio

---

**Versión:** 1.0 | **Fecha:** 2026-06-23 | **Propietario:** Javier Forero | **Severidad:** P0_BLOQUEANTE
