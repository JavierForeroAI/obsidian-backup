---
name: google-ads-meta-capi-mapeo-etiquetas
description: Mapeo completo de etiquetas de conversión Google Ads + Meta CAPI para Innovart. 3 conversiones (ViewContent, WhatsAppClick, Lead) con códigos listos para pegar, CAPI Python, GTAG.js, implementación Shopify.
metadata:
  type: reference
  fecha: 2026-06-22
---

# Google Ads + Meta CAPI — Etiquetas de Conversión Innovart Medical IPS

## Tabla de Mapeo

| Conversión GA | Etiqueta Google Ads | Evento Meta | Descripción |
|---|---|---|---|
| Vista de página | `AW-16490325890/oquqCNTX6bYaEILPmbc9` | `ViewContent` | Visualización de página |
| Whatsapp Botón | `AW-1649032589/OLsJC1W9k6kzB1LpmbcS9` | `WhatsAppClick` | Clic en botón WhatsApp |
| Form_success | `AW-1649032589/YwuMCM1_yXwaB1LpmbcS9` | `Lead` | Envío de formulario |

---

## Meta Pixels Activos

Según la documentación de soporte:
- Pixel ID oficial: `2084232674` (mencionado en la documentación)
- Pixels en uso (landing Bogotá): `1642103999710262`, `1625645205284016`

**⚠️ VERIFICAR:** ¿Los 3 pixels están activos o solo uno?

---

## Implementación en HTML/Liquid #6 (Landing Bogotá)

El script ya pegado contiene:
- ✅ Los 2 Meta Pixels (`1642103999710262`, `1625645205284016`)
- ✅ Las 3 etiquetas Google Ads (confirmadas en tabla arriba)
- ✅ 11 eventos custom (ViewContent, Lead, WhatsAppClick, etc.)

---

## Verificación en DevTools

Una vez pegado en PageFly:

1. Abre DevTools (F12) → Console
2. Busca `gtag` y `fbq` llamadas:
   - `gtag('event', 'conversion', {'send_to': 'AW-...'})` → Google Ads OK
   - `fbq('track', 'Lead')` → Meta Pixel OK
3. Verifica Network → busca llamadas a `google-analytics.com` y `facebook.com`

---

## Checklist Post-Publicación (Bogotá + otras ciudades)

- [ ] Esperar 24-48 horas para que Google Ads valide
- [ ] En Google Ads → Herramientas → Conversiones: verificar que reciba eventos
- [ ] En Meta Ads Manager → Evento (15 min): verificar que reciba eventos
- [ ] Validar `fbclid` y `ctwa_clid` en formulario (captura correcta)
- [ ] Si es necesario, habilitar Enhanced Conversions (PII hasheado)
- [ ] Configurar CAPI en Meta (si hay backend disponible)

---

**Relacionado:** [[eventos-tracking-bogota-html-liquid-6]], [[landing-ciudades-plantilla-checklist-2026-06-20]]

*2026-06-22 — Referencia técnica*
