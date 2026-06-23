---
name: tracking-pixels-config
description: Configuración de pixels de tracking — Shopify vs GHL (CRÍTICO, consultar siempre)
metadata:
  type: reference
---

# Configuración de Pixels de Tracking — Innovart

**REGLA ABSOLUTA:** Estos IDs son únicos y no cambian. Usarlos siempre para verificación de tracking.

## Pixel de Shopify (innovartmedical.com)

| Propiedad | Valor |
|-----------|-------|
| **Plataforma** | Shopify (innovartmedical.com) |
| **Identificador clave** | Termina en **`62`** |
| **ID completo** | `[XXXXXXXXXXXXX]62` |
| **Uso** | Página de productos, home, landings nativas de Shopify |

**Verificación:** Cuando busques el pixel de Shopify, confirma que el ID termina en `62`.

---

## Pixel de GHL (home4 y home5)

| Propiedad | Valor |
|-----------|-------|
| **Plataforma** | GHL (landing pages) |
| **Landing pages** | `/home4` y `/home5` |
| **Identificador clave** | **`1625645205284016`** |
| **ID completo** | `1625645205284016` (exacto) |
| **Uso** | Tracking de eventos en landings GHL (fbclid, CAPI, conversiones) |

**Verificación:** Cuando revises el tracking de home4/home5, confirma que el pixel es `1625645205284016`.

---

## Cómo Usar Esta Información

1. **Auditoría de tracking:** Busca estos IDs en el código de la página
2. **Verificación de eventos:** Confirma que los eventos llegan desde estos pixels
3. **Troubleshooting:** Si el tracking falla, valida que los IDs estén presentes y activos
4. **Cambios futuros:** Si se reemplaza un pixel, UPDATE este archivo inmediatamente

**NO preguntes nuevamente** — estos IDs están aquí como referencia de verdad.

---

## Relación con otros sistemas

- [[auditoria-fbclid-critica-2026-06-22]] — fbclid capture en home5
- [[home5-v11-codigo-completo]] — código final de home5 con pixels
- [[metodo-carga-utms-api-meta]] — UTMs cargados con estos pixels

