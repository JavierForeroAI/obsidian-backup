---
name: diagnostico-eventos-tracking-rotos-pixel1-2026-06-30
description: Diagnóstico específico de por qué 3 de 4 eventos custom de tracking en innovartmedical.com (Pixel 1) no disparan — causas exactas por evento + decisión de nomenclatura custom vs eventos estándar Meta
metadata:
  type: project
  fecha: 2026-06-30
  estado: diagnosticado-pendiente-fix
---

# Diagnóstico — Eventos de tracking rotos en innovartmedical.com (Pixel 1)

**Fecha:** 2026-06-30 (sesión e94ce2a3). Complementa (no reemplaza) [[analisis-pixel-1-sin-permisos-capi-2026-06-29]] — ese análisis explica por qué el pixel no recibe conversiones desde el CAPI worker; este documento explica por qué los eventos JS del lado cliente tampoco disparan.

## Estado de los 4 eventos objetivo

| Evento | Estado | Causa raíz exacta |
|---|---|---|
| **Contact (WhatsApp)** | ⚠️ Roto/parcial | El listener de click se agrega ANTES de que PageFly renderice sus elementos dinámicos. Botón flotante WhatsApp es un `<div id="chat-bubble">` (no `<a>`), y el botón real "¿Quiero contactarme con un asesor?" sí es `<a href="https://api.whatsapp.com/...">` pero el listener no queda enganchado a elementos creados después del load. |
| **Diligencia Formulario (Lead)** | ❌ Roto — nunca dispara | El código busca `txt.indexOf('Agendar Cita') > -1`, pero el botón real de la página dice **"¿Quiero contactarme con un asesor?"**. Nunca coincide. |
| **ViewContent (Implante)** | ❌ Roto — nunca dispara | El código busca `txt.indexOf('Implante Capilar')`, pero el texto real en la card es **"Implante capilar"** (minúscula en "capilar"). `.indexOf()` es case-sensitive → nunca coincide. |
| **Scroll Depth (25/50/75%)** | ✅ Funciona 100% | Usa `window.addEventListener('scroll')` global, no depende de que existan elementos específicos del DOM — por eso es el único que sobrevive al render tardío de PageFly. |

**Diagnóstico agregado:** de los 8 eventos que necesitaría `/meta-ads-intel` para optimizar bien las campañas (PageView, Contact, Lead, ViewContent, Scroll Depth, Schedule, Purchase, AddToCart), Innovart solo tiene **1.5/8 funcionales** (PageView + Scroll Depth; Contact parcial). Sin Lead/Schedule/Purchase reales, Meta no puede optimizar por conversión de negocio — solo ve tráfico.

## Fix pendiente (no ejecutado aún, sesión interrumpida)

1. Contact: enganchar el listener con delegación de eventos sobre `document` (no sobre el elemento directo) para que capture nodos añadidos dinámicamente por PageFly.
2. Lead: cambiar el string de match de `'Agendar Cita'` a `'¿Quiero contactarme con un asesor?'` (o un substring estable de ese texto).
3. ViewContent: cambiar el match a case-insensitive (`.toLowerCase()` antes de comparar) o usar el texto exacto `'Implante capilar'`.

Ver también kardex de código crítico: [[kardex-theme-pagefly-liquid]] — cualquier fix a estos matches debe registrarse ahí antes de tocar el archivo (protocolo en [[protocolo-modificaciones-criticas]]).

## Decisión: nomenclatura de eventos custom vs eventos estándar Meta

Javier preguntó si podía renombrar eventos custom (ej. que "Contact" se llame "B.whatsapp", o que los eventos de scroll no se llamen "ViewContent"). Se evaluaron 3 opciones:

- **Opción 1 (eventos 100% custom, ej. `fbq('track','B.whatsapp')`)**: Meta pierde el reconocimiento como evento estándar → no optimiza ni atribuye correctamente. Descartada.
- **Opción 2 (disparar ambos: estándar + custom)**: funciona pero duplica eventos, Meta cuenta 2x. No recomendada.
- **Opción 3 (RECOMENDADA — la que se adoptó):** mantener los eventos **estándar** de Meta (`Contact`, `ViewContent`, etc.) para que Meta siga optimizando y atribuyendo bien, pero usar los parámetros `content_name` y `content_category` para llevar la nomenclatura custom que Javier quiere ver en Meta Pixel Helper / reportes. Ejemplo:
  ```javascript
  fbq('track', 'Contact', { content_name: 'B.whatsapp', content_category: 'WhatsApp Click' });
  fbq('track', 'ViewContent', { content_name: 'scroll_25', content_category: 'Engagement' });
  ```
  Ventaja: Meta optimiza normal, Javier ve sus nombres custom en los parámetros, y `/meta-ads-intel` sigue entendiendo los eventos estándar sin confusión.

**Esta decisión aplica a futuras implementaciones de tracking** — no renombrar eventos estándar de Meta, usar `content_name`/`content_category` para la nomenclatura interna deseada.

---
Referencias: [[analisis-pixel-1-sin-permisos-capi-2026-06-29]], [[eventos-tracking-bogota-html-liquid-6]], [[kardex-theme-pagefly-liquid]], [[protocolo-modificaciones-criticas]]
