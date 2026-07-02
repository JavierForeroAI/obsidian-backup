---
name: analisis-pixel-1-sin-permisos-capi-2026-06-29
description: Pixel 1 Shopify (1642103999710262) solo recibe PageView/ViewContent — CAPI worker no tiene permisos de escritura
metadata:
  type: project
  fecha: 2026-06-29
  estado: hallazgo-bloqueante
---

# Análisis: Pixel 1 — Ausencia de permisos CAPI

**Fecha:** 2026-06-29 16:03 UTC (sesión e94ce2a3)

## Resumen ejecutivo

El **Pixel Shopify ("Pixel CRM" `1642103999710262`)** recibe tráfico (27K visitas/semana) pero **CERO eventos de conversión**:
- ❌ 0 Lead eventos
- ❌ 0 Purchase eventos
- ❌ 0 Schedule eventos
- ✅ 27K PageView (Shopify CAPI automático)
- ✅ 105 ViewContent (esporádico)

El **CAPI worker** (`innovart-capi-webhook-no-tocar`) tiene este pixel en su lista `DEFAULT_PIXELS`, pero **no escribe eventos ahí**. Causa probable: **token CAPI sin permisos** sobre el pixel Shopify.

## Datos de Meta

**Pixel ID:** `1642103999710262` ("Pixel CRM")  
**Creado:** 2024-11-05 (8 meses)  
**Última vez activo:** 2026-06-29 08:58  
**Business Manager:** `940287337027000` (Implante Innovart Medical)  
**EMQ (Email Match Quality):** 6.1 (baja — solo 2.1% email)  

## Flujos observados

| Fuente | Volumen 7d | % | Eventos enviados |
|--------|-----------|---|------------------|
| SERVER (Shopify CAPI) | 14,846 | 54.2% | **Solo PageView** |
| BROWSER (Pixel JS) | 12,534 | 45.8% | PageView + ViewContent |
| **Total** | **27,380** | 100% | **2 tipos únicamente** |

**Conclusión:** Shopify CAPI automático funciona (solo PageView), pero el **CAPI worker de Cloudflare no escribe conversiones** a este pixel.

## El problema en el worker

En `innovart-capi-webhook-no-tocar/src/index.js` línea ~40:

```javascript
const DEFAULT_PIXELS = ['1642103999710262', '1625645205284016'];
```

El worker envía `Lead`, `Purchase`, `Schedule` al pixel `1625645205284016` (GHL) ✅  
Pero intenta enviar también al pixel `262` ❌ sin permisos.

## Impacto

**Alto.**
- El Pixel Shopify debería ser la **fuente de verdad de conversiones** para e-commerce (Purchase)
- Ahora está "ciego" para el negocio
- Los reports de Meta sobre "Pixel Shopify CRM" no reflejan ingresos reales
- Attribution no cierra

## Opciones

### Opción 1: Agregar permisos al token CAPI (Recomendado)
1. En Meta: Business Settings → Data Sources → Conversions API
2. Verificar que el token tenga permiso en pixel `1642103999710262`
3. Re-generar token si es necesario
4. Probar worker con un evento de prueba

**Riesgo:** Requiere acceso Meta Business

### Opción 2: Eliminar pixel 262 del worker
```javascript
const DEFAULT_PIXELS = ['1625645205284016'];  // Solo GHL
```
- Worker envía conversiones solo a pixel GHL
- Pixel Shopify deja de recibir eventos del worker (solo Shopify CAPI automático)
- Más simple pero menos data en Meta

**Riesgo:** Menos redundancia

## Próximos pasos

- [ ] **Verificar permisos:** Acceso Meta → Business Settings → Conversions API → token sobre `1642103999710262`
- [ ] **Test E2E:** Generar un evento Purchase desde worker, confirmar que llega al pixel en Meta Events Manager
- [ ] **Decisión:** ¿Usar dual-pixel (si permisos OK) o single-pixel GHL?

---

## Actualización 2026-07-01 — Confirmado en vivo: el Pixel base SÍ carga

Verificación en vivo en `innovartmedical.com` (no vía GTM, como se sospechaba antes): el Pixel `1642103999710262` carga por el **canal nativo "Shopify Web Pixel"** (integración oficial de Shopify, no un tag de GTM) y dispara `PageView` correctamente. `fbq` existe y está cargado.

**Implicación:** los eventos custom (`Contact`, `Lead`, `ViewContent`) en `theme.pagefly.liquid` están envueltos en `if(typeof fbq !== 'undefined')` — como el Pixel base sí carga, ese guard no es la causa de que fallen; el problema de fondo sigue siendo el de este documento (permisos CAPI) + los bugs de selección/nomenclatura de eventos ya documentados en [[diagnostico-eventos-tracking-rotos-pixel1-2026-06-30]].

**Referencia:** [[tracking-pixels-config]], [[flujo-crm-qikify-verificado-2026-06-29]]
