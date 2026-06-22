---
name: home5-cro-v10-deploy-2026-06-22
description: Deploy home5 bodyTrackingCode v10 — sticky bar + CTA color + video optimización + copy compliant
metadata:
  type: project
---

# Deploy Home5 CRO v10 — 2026-06-22

## Estado Ejecutivo

**Home5** (`F6xTmSqYRLizoZ1SJmDg`) está lista para optimización CRO completa. Se inyecta **bodyTrackingCode v10** vía MCP sin afectar home4 (guard `/home5`).

**Todos los P0 implementados:**
- ✅ Sticky bar 88px fijo (WhatsApp + "Ver si Califico")
- ✅ CTA color #3D7EBF (azul) + gradiente + halo dorado
- ✅ Video oculto en móvil (@media max-width 768px)
- ✅ Copy suavizada (sin "garantía vitalicia", claims compliant)
- ✅ Tracking events (ViewForm, ScrollDepth, WhatsAppClick)
- ✅ Lead/Contact suprimido (CAPI webhook fuente única)
- ✅ Clarity x62cig8qug preservada

## bodyTrackingCode v10 — Especificación

### Alcance
- **Ubicación:** GHL funnel "Landing 1 Home" (`6gDZimr1JRoW9iQZZnRH`), page home5 (`F6xTmSqYRLizoZ1SJmDg`)
- **Campo:** `bodyTrackingCode` (NO tocar `headTrackingCode` — contiene Clarity)
- **Tamaño:** 4.8 KB (minificado)
- **Guard:** `if (!location.pathname.includes('/home5')) return;` → SOLO ejecuta en /home5

### Componentes

#### 1. Sticky Bar (CSS fixed)
```
Altura: 88px
Posición: bottom 0, z-index 9999
Botones:
  - 📱 WhatsApp: verde #25D366, link +57 312 456 5014
  - ✓ Ver si Califico: azul #3D7EBF, scroll a #formulario
Shadow: 0 -2px 8px rgba(0,0,0,0.1)
Mobile: visible en <768px
Desktop: visible en >768px
```

#### 2. CSS Tema Claro
- Body: fondo #F9FAFB, text #1A2E4A (navy)
- H1/H2: #1A2E4A
- CTA buttons: #3D7EBF + gradiente linear 135deg + shadow dorado
- Textos secundarios: #b0b0b0 (WCAG AA)
- Video hero: `@media (max-width: 768px) { display: none !important; }`

#### 3. Copy Reemplazos (find/replace)
| Original | Nuevo | Razón |
|----------|-------|-------|
| "garantía vitalicia" | (removido) | Prohibido en Colombia |
| "no sientes dolor" | "con anestesia local" | Claim no verificable |
| "para siempre / permanente" | "duradero + respaldo médico" | Suavizar promesa |
| "ÚNICOS EN COLOMBIA" | "18+ años liderando implantes capilares" | Verificable, sin exclusiva |

#### 4. Eventos Custom
```javascript
ViewForm           // page load (si visible)
ScrollDepth_25     // usuario llega 25%
ScrollDepth_50     // usuario llega 50%
ScrollDepth_75     // usuario llega 75%
WhatsAppClick      // clic en botón WhatsApp
```

#### 5. Supresión CAPI
```javascript
Lead    ✗ SUPRIMIDO (GHL webhook → Meta)
Contact ✗ SUPRIMIDO (GHL webhook → Meta)
```

## Instalación (GHL MCP)

**Método:** `mcp__ghl__update_funnel`

```json
{
  "locationId": "DgjjDzD9nkCKv8AGF1Qb",
  "funnelId": "6gDZimr1JRoW9iQZZnRH",
  "body": {
    "headTrackingCode": "[PRESERVAR EXACTO — incluye Clarity x62cig8qug + captura fbclid]",
    "bodyTrackingCode": "[CÓDIGO v10 COMPLETO]"
  }
}
```

**REGLA CRÍTICA:** Enviar `headTrackingCode` + `bodyTrackingCode` **JUNTOS**. Si omites head, borra Clarity.

## Validación Post-Deploy

### Verificación Visual (48h después)
- Sticky bar visible en móvil (88px fijo)
- Video oculto en móvil
- Botones WhatsApp + "Ver si Califico" clickables
- CTA color azul (no teal de marca)

### Verificación Técnica (Console F12)
```
[BodyTrackingCode v10] Initialized for /home5
[Tracking] ViewForm { source: 'page-load', visible: true }
[ScrollDepth] 25% reached
```

### Verificación Analytics (30 min después en Clarity)
- Click map visible (no ciego como home4)
- Eventos custom en `fbq()` llamadas
- Lead/Contact NO aparecen en fbq (solo por webhook)

## Comparativa home4 vs home5

| Métrica | home4 (LIVE) | home5 (A/B) |
|---------|--------------|------------|
| **Scroll a form** | 3.6% (enterrado) | ↑ (sticky bar rescata) |
| **CTA color** | Teal marca (blind) | Azul único (#3D7EBF) |
| **Video móvil** | 217 MB autoplay (mata) | Oculto (@media) |
| **Copy** | "garantía vitalicia" | Suavizada |
| **Tracking** | Lead fantasma | Lead por CAPI clean |
| **Clarity** | Ciego (iframe) | Iframe igual pero eventos custom |
| **Form** | `6aGxlY1g` (Diagnostico Capilar Bogota) | `RB4a58…` A/B (por swap nativo) |
| **Tag lead** | `landing_form_home4` | `lead_home5` (router ac1b818d) |

## Roadmap Ejecución

### Fase 1: Deploy bodyTrackingCode (HOY)
- [ ] Update funnel vía MCP (headTrackingCode + bodyTrackingCode)
- [ ] Validar visual sticky bar + CTA color
- [ ] Revisar Console no hay errores JS

### Fase 2: Swap Form Nativo (Tomorrow)
- [ ] GHL editor → home5 → click elemento formulario → cambiar a "Diagnóstico Capilar — Home5 (A/B)" (RB4a58…)
- [ ] Router ac1b818d auto-dispara tag `lead_home5`
- [ ] Verificar leads caen como A/B

### Fase 3: Optimización Video (1 semana, Dev)
- [ ] Comprimir hero 217 MB → 1.5-3 MB (ffmpeg)
- [ ] Subir CDN Shopify/Cloudinary
- [ ] Cambiar URL en GHL (update_funnel)

### Fase 4: A/B Test (Weeks 2-4)
- [ ] Smart list por tag: `lead_home4` vs `lead_home5`
- [ ] KPIs: conversion rate, scroll depth, eventos tracking
- [ ] Ganador reemplaza home4

## Notas Técnicas

**GOTCHA headTrackingCode:**
- `update_funnel` NO mergea automáticamente
- Si pasas solo `bodyTrackingCode`, **borra `headTrackingCode`** → tumbó Clarity 2 veces
- Solución: extraer `headTrackingCode` exacto (incluye `<!-- Clarity x62cig8qug -->`) + enviar junto con body

**Video Compresión (Fase 3):**
- Actual: 227.6 MB, autoplay en móvil mata performance
- Target: 1.5-3 MB, lazy-load (load on interaction)
- Herramienta: ffmpeg, HandBrake o ffmpeg.wasm

**Form A/B:**
- home4 form: `6aGxlY1gdbBx3vQA7XR9` (Diagnostico Capilar Bogota)
- home5 form: `RB4a58CCebT51AOpuyPd` (Diagnóstico Capilar — Home5 (A/B)) ← clon byte-equivalente
- Router home5: `ac1b818d` → tag `lead_home5` + dispara flujo 4.1

**Clarity Limitación:**
- Form vive en iframe cross-origin (`api.leadconnectorhq.com/widget/form/…`) → Clarity ciego a clics
- Workaround: medir form events en GHL nativo (clic Enviar + conversiones) + eventos custom en fbq

## Archivos Relacionados

- `home4-no-trackea-clics-cro.md` — diagnóstico original (Clarity ciego, sticky vacío)
- `home5-capa-optimizacion-cro.md` — versiones v8/v9 + GOTCHA update_funnel
- `landing-home4-routing.md` — formularios, routers, hidden fields
- `/tmp/bodyTrackingCode-v10-COPIAR.js` — código minificado (4.8 KB) para pegar en GHL

---

**Versión:** v10 | **Fecha:** 2026-06-22 | **Estado:** READY FOR DEPLOY | **Propietario:** Javier Forero | **Cliente:** Innovart Medical IPS
