---
name: auditoria-fbclid-fase2-2026-06-21
description: Auditoría Fase 2 validación de fbclid en GHL — custom fields, head tracking code, brecha crítica y plan de fix P0 (25 minutos)
metadata:
  type: audit
  fecha: 2026-06-21
  criticidad: P0
---

# Auditoría Fase 2 — Validación fbclid en GHL (2026-06-21)

## 1. CUSTOM FIELD FBCLID

**Estado:** EXISTE ✓
**ID:** `ROjbROGU9919xi7GR9rO`
**Nombre exacto:** fbclid
**fieldKey:** contact.fbclid
**Tipo:** TEXT
**Creado:** 2026-06-11T01:53:26.015Z (10 días atrás)

### DATO CRÍTICO
Campo configurado pero **CERO contactos tienen valor**.
- Query en 163K+ contactos: 0 resultados
- Implica: **Ningún lead en los últimos 10 días capturó fbclid en home4**

### Campos relacionados (CONFUSIÓN NOMENCLATURA)
- `fbclid` (ID: `ROjbROGU9919xi7GR9rO`) — nuestro campo principal
- `fb_click_id` (ID: `wy6FYlxKsMDvtXljeC9O`) — "Facebook Click ID"
- `ctwa_clid` (ID: `pmfzBxCFdjeojgCLmEWu`) — "Click-to-WhatsApp Click ID"

⚠️ **Problema de arquitectura:** Tres campos para el mismo concepto. Unificar en UNO.

---

## 2. HEAD TRACKING CODE (HOME4)

**Página:** PaBAMA8f6ISzy4H3HHty (live home4 en implantecapilarencolombia.com/home4)

**Lo que EXISTE:**
- ✅ Meta Pixel IDs: 1642103999710262, 1625645205284016
- ✅ Clarity ID: x62cig8qug
- ✅ Inicialización de fbq y Clarity
- ❌ **CERO código JavaScript capturando fbclid del parámetro URL**

**Lo que FALTA:**
```javascript
// NO EXISTE en home4:
const params = new URLSearchParams(window.location.search);
const fbclid = params.get('fbclid');
if (fbclid) {
  localStorage.setItem('innovart_fbclid', fbclid);
  document.body.setAttribute('data-fbclid', fbclid);
}
```

**Tamaño actual:** ~4.8 KB de JS
**Ausencia:** fbclid capture = ~0.5 KB

---

## 3. BRECHA CRÍTICA IDENTIFICADA

### Causa Raíz

El formulario GHL de home4 es un **iframe cross-origin** (`api.leadconnectorhq.com/widget/form/...`). Problema:

1. **headTrackingCode corre en dominio PRINCIPAL** (implantecapilarencolombia.com)
2. **form vive en iframe GHL** (dominio ajeno, cross-origin)
3. **JS principal NO puede acceder al iframe** (CORS policy)
4. **Solución requerida:** JS capture fbclid → localStorage → form GHL lee desde localStorage

### Dato de Impacto

- **Leads/día (home4):** ~15-25 en Bogotá (promedio: 20)
- **% sin fbclid actualmente:** 100% (CERO contactos con valor)
- **Eventos CAPI bloqueados/día:** 20
- **Eventos/mes perdidos:** ~600
- **Impacto EMQ:** Fbclid = match quality → Meta no puede vincular "clic ad" → "lead"

### Event Match Quality Impact

- EMQ actual: 4.9/10
- Causa: email hasheado 10% + **fbclid 100% de web leads**
- Solución fbclid podría subir EMQ: 4.9 → 5.5+ (estimado)

---

## 4. ESTADO OTRAS LANDING PAGES

### qikify (Shopify)
- **Problema:** Form NO captura fbclid
- **Flujo:** qikify → Gmail → n8n → GHL
- **Solución:** Custom HTML oculto en qikify que lea fbclid
- **Estado:** Pendiente (Fase 2)

### home5 (prueba)
- **Página:** F6xTmSqYRLizoZ1SJmDg
- **bodyTrackingCode v10:** Listo (HOME5 CRO v10 deploy 2026-06-22)
- **Acción:** Verificar si v10 INCLUYE fbclid capture

### /pages/contact (Shopify)
- **Problema:** Form nativo Shopify → NO llega a GHL
- **Solución:** GHL embed (Contacto Web Innovart, ID: X4zQ4jv8SNtap08XU1rs)
- **Estado:** Listo, pendiente iframe en Liquid

---

## 5. PLAN DE FIX P0

### Acción 1: Inyectar fbclid capture en home4
**Ubicación:** headTrackingCode (page PaBAMA8f6ISzy4H3HHty)
**Tiempo:** 15 minutos
**Riesgo:** BAJO

```html
<script>
// Capture fbclid from URL and store for form
(function() {
  const params = new URLSearchParams(window.location.search);
  const fbclid = params.get('fbclid');
  if (fbclid) {
    localStorage.setItem('innovart_fbclid', fbclid);
    document.body.setAttribute('data-fbclid', fbclid);
  }
})();
</script>
```

### Acción 2: Configurar form GHL para LEER fbclid
**Dónde:** Form "Formulario Landing page Home4" (ID: 5TkRnl4xWOvZeoz9pGFf)
**Cómo:** Hidden field → custom field fbclid (ROjbROGU9919xi7GR9rO)
**Tiempo:** 10-30 minutos
**Riesgo:** BAJO

### Acción 3: Validación E2E
1. Clic en ad Meta con fbclid en URL (ej: `?fbclid=AjH2-J...`)
2. Landing home4 carga
3. Llenar form
4. Verificar: Campo fbclid tiene valor en contacto
**Tiempo:** 30 minutos (2-3 ciclos)

---

## 6. RESUMEN EJECUTIVO

| Aspecto | Estado |
|---|---|
| Campo fbclid existe | ✅ SÍ (ID: ROjbROGU9919xi7GR9rO) |
| Contactos con fbclid | ❌ 0 / 163K+ |
| JS de captura en home4 | ❌ NO |
| JS de captura en home5 | 🟡 A VERIFICAR |
| Impacto (leads/mes) | ~600 eventos CAPI bloqueados |
| Tiempo fix P0 | ~25 minutos |
| Efecto en EMQ | +0.5–0.7 puntos |

---

## 7. RECOMENDACIÓN FINAL

**Esta es la causa #1 de EMQ baja en web.** Ejecutar Acciones 1-2 HOY.

**Regla nueva:** fbclid es OBLIGATORIO en TODO form nuevo de Innovart, sin excepción. Ver [[feedback_fbclid_landing_pages]].

---

## Relacionados
- [[home4-no-trackea-clics-cro]] — diagnóstico Clarity
- [[feedback_fbclid_landing_pages]] — estándar de desarrollo
- [[flujo-leads-qikify-fbclid]] — qikify fbclid problem
- [[auditoria-capimetaghl-base]] — base de auditoría CAPI
