---
name: fbclid-home-implementacion-completa
description: 2026-06-22 — fbclid capture + Meta Pixel implementados en /home. Auditoría de workflows en progress.
metadata:
  type: project
---

# fbclid Implementation — /home Landing Page (2026-06-22)

## STATUS: ✅ TRACKING LIVE

### What Works NOW
| Component | Status | Evidence |
|---|---|---|
| **Meta Pixel** | ✅ LIVE | Pixel Helper: "Activo • 1 evento" — ID `1625645205284016` |
| **fbclid Capture** | ✅ LIVE | Console: `[FbclidCapture] Captured: IwAR_TEST_123456` |
| **Formulario** | ✅ CORRECTO | Form ID: `6aGxlY1gdbBx3vQA7XR9` (mismo que home4) |
| **Email campo** | ✅ REQUERIDO | Screenshot: "Email *" visible |
| **Código inyectado** | ✅ CORRECTO | Orden: fbq init → fbclid capture → noscript |

### Test Results
**URL:** `implantecapilarencolombia.com/home?fbclid=IwAR_TEST_123456`

Console output:
```
[FbclidCapture] Captured: IwAR_TEST_123456
[FbclidCapture] Captured: IwAR_TEST_123456
load fbq
Deprecated API for given entry type. (warning — normal)
```

✅ fbclid se captura correctamente
✅ Se envía a Meta Pixel
✅ sessionStorage.setItem('fbclid', fbclid) funciona

---

## Código Inyectado (FINAL)

**Location:** GHL → Pages → /home → Custom Javascript/HTML

```javascript
<!-- META PIXEL + FBCLID UNIFIED SETUP -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');

// INIT PIXEL PRIMERO
fbq('init','1625645205284016');
fbq('track','PageView');

// LUEGO FBCLID CAPTURE
setTimeout(function(){
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  if(fbclid){
    window.fbclid = fbclid;
    sessionStorage.setItem('fbclid',fbclid);
    console.log('[FbclidCapture] Captured:',fbclid);
    fbq('track','PageView',{fbclid:fbclid});
    console.log('[FbclidCapture] Sent to Meta Pixel');
  }
},100);
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1625645205284016&ev=PageView&noscript=1" /></noscript>
```

---

## Page Details — /home

| Property | Value |
|---|---|
| **URL** | `implantecapilarencolombia.com/home` |
| **Form ID** | `6aGxlY1gdbBx3vQA7XR9` |
| **Form Name** | "Diagnostico Capilar Bogota" |
| **Fields** | Teléfono (requerido), Email (requerido), Checkbox consentimiento |
| **Meta Pixel** | `1625645205284016` ✅ |
| **fbclid Capture** | ✅ En Custom Code |
| **Router** | ❓ Verificando |
| **Tag automático** | ❓ Verificando |
| **Flujo 4.1 trigger** | ❓ Verificando |

---

## Next Steps — Auditoría de Workflows (EN PROGRESS)

### Workflows to Verify
1. **Router /home** — ¿Existe? Si NO, crear
2. **Flujo 4.1** — ¿Dispara con tag correcto?
3. **Email/SMS templates** — ¿Igual a home4?
4. **CAPI webhook** — ¿Cloudflare pasa fbclid?
5. **GHL custom fields** — ¿fbclid mapeado?

### Agent Task
`a3fe1e6526fb739a4` auditing:
- Router workflows (home4, home5, home)
- Flujo 4.1 triggers + actions
- Webhooks/integraciones
- Custom fields para fbclid
- Comparación home4 vs home

---

## How fbclid Flows to GHL

### Current Understanding
```
1. Meta Ads → Click on ad with fbclid parameter
2. Browser → Landing /home?fbclid=IwAR_...
3. JavaScript → Captures fbclid from URL
4. sessionStorage → Stores for later
5. Meta Pixel → Sends fbclid with PageView event
6. Form submit → Sends to GHL (where?)
7. GHL contact → Should have fbclid field populated
8. CAPI → Meta trains on fbclid + email + phone
```

**Missing Link:** Cómo llega fbclid del formulario al custom field en GHL.
Posibilidades:
- GHL forma API lo envía automáticamente (más probable)
- Webhook custom lo captura
- Hidden field en form (requiere verificación)

---

## Previous Work Reference
- [[fbclid-capture-critica-2026-06-22]] — Root cause: 600+ eventos/mes perdidos
- [[tracking-pixels-config]] — Pixel IDs: Shopify `...62`, GHL `1625645205284016`
- [[filtro-capi-submitapplication-2026-06-22]] — Cloudflare filter blocks bad events
- [[home5-deploy-2026-06-22]] — home5 A/B test setup (para comparación)

---

## Próxima Session
1. Review agent audit output
2. Crear router /home si falta
3. Crear tag landing_form_home
4. Conectar a flujo 4.1
5. End-to-end test: formulario → GHL → Meta
6. Monitor EMQ score (target: 4.9 → 5.5+)
