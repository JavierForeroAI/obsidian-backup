---
name: filtro-capi-submitapplication
description: Filtro CAPI para bloquear eventos SubmitApplication fantasma en home4/home5 — implementado 2026-06-22
metadata:
  type: project
---

# Filtro CAPI — SubmitApplication Fantasma (2026-06-22)

## Problema Resuelto

**Raíz:** Home4 y home5 en GHL disparan `SubmitApplication` **automáticamente** en páginas `optin_funnel_page`, sin participación real del usuario.

**Impacto anterior:**
- Eventos fantasma llegan a Meta sin `fbclid` ni PII válida
- Entrenan al algoritmo Meta con conversiones falsas
- Reportes de Meta incluyen ruido (no refleja show rate real ~40%)
- El evento `Lead` de Meta es poco confiable (dispara con cada clic, no con form)

## Solución Implementada

**Dónde:** Worker Cloudflare `innovart-capi-webhook-no-tocar` (CAPI lado servidor)

**Lógica:** Bloquea `SubmitApplication` si:
1. NO tiene `fbclid` o `fbp` (sin identidad Meta)
2. NO tiene `email` o `phone` (lead incompleto)

**Código inyectado (línea ~98):**
```javascript
if (event === 'SubmitApplication') {
  const hasFbId = fbclid || fbp;
  const hasPii = email || phoneRaw;
  if (!hasFbId || !hasPii) {
    const reason = !hasFbId ? 'no_facebook_id' : 'incomplete_lead';
    return json({
      ok: false,
      blocked: true,
      reason,
      event,
      message: `SubmitApplication fantasma bloqueado (${reason})`
    }, 202);
  }
}
```

## Validación (E2E)

✅ **Test 1:** SubmitApplication sin fbclid → **BLOQUEADO** (reason: `no_facebook_id`)
✅ **Test 2:** SubmitApplication con fbclid + email → **ACEPTADO** (enviado a Meta CAPI, 2 píxeles)
✅ **Test 3:** Lead sin fbclid → **ACEPTADO** (eventos Lead no requieren fbclid)

**Deploy:** 2026-06-22 18:54 UTC
- Version ID: `9ca49de3-b6be-41f1-97e6-278da9166481`
- URL: https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev

## Pendientes (Roadmap Fase 2)

### CRO — Home4 y Home5
- [ ] Subir captura del hero (video 217MB autoarranca mata conversión)
- [ ] Llenar sticky-bar vacío (88px sin CTA)
- [ ] Cambiar color CTA (teal marca → banner blindness)
- [ ] Mover form o sticky (3.6% alcanza hoy)

### Tracking — Validaciones
- [ ] Verificar fbclid se captura antes de SubmitApplication
- [ ] Validar evento Lead dispara correctamente
- [ ] Monitorear logs del worker (cuántos eventos/día se bloquean)

### Reporting
- [ ] Dashboard de eventos bloqueados vs aceptados
- [ ] Impacto en ROAS y show rate (antes/después)

## Archivos Modificados

**Ruta:** `/Users/javierforero/innovart-capi-webhook-no-tocar/src/index.js`
**Cambio:** ~20 líneas de filtro inyectadas post-línea 99
**Backup:** En git (commit automático al deploy)

## Referencias

- [[auditoria-capimetaghl-base]] — Matriz de eventos y validación
- [[home4-no-trackea-clics-cro]] — Diagnóstico original (scroll/form al 100%)
- [[flujo-leads-qikify-fbclid]] — Cómo fbclid llega a GHL

## Status

**Live:** ✅ 2026-06-22 18:54 UTC
**Bloqueadores:** Ninguno (filtro independiente)
**Próximo paso:** CRO de home4/home5
