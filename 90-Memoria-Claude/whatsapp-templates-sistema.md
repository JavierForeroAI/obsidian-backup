---
name: whatsapp-templates-sistema
description: Sistema de gestión de plantillas WhatsApp por API (Meta) en las líneas de Innovart — mapa de líneas, por qué la analítica de aperturas no sale de Meta, proxy de ubicuidad, y copia Tier 1 a Bogotá nueva (2026-06-19)
metadata:
  type: project
  fecha: 2026-06-19
---

# WhatsApp Templates — gestión por API y consolidación de Bogotá nueva (2026-06-19)

Gestión de plantillas de WhatsApp de las líneas Innovart vía **Meta WhatsApp Business API**
(leer / sugerir / crear con dedupe / mandar a aprobación). Skill: **`whatsapp-templates-ghl`**
(alias interno `API_Whatsapp_Tem_GHL`). Config + token en `~/.claude/scripts/.wa-templates.json`
(⚠️ token Meta dentro; NO copiarlo a memoria).

## Panorama (85 días, junio 2026)
- **7 líneas API activas** · **614 templates** en total · 13 WABA vacías.
- **Bogotá tiene 2 líneas:** la **anterior (320)**, WABA `1183841487216235`… *(ver abajo)*,
  prácticamente **retirada** (solo 3 envíos en 85 días → su analítica no sirve para decidir);
  y la **nueva (310)**, WABA `1183841487216235`, que estaba casi vacía (12 templates) con
  **165 plantillas faltantes** frente a las demás sedes.

## ⚠️ La analítica de aperturas NO se puede sacar de Meta
`template_analytics` de Meta devuelve **todo en 0** porque `product_type: cloud_api` y **los
envíos de Innovart NO pasan por Cloud API** — salen por **LeadConnector/applevel** (el mismo
motivo por el que el WhatsApp entra a GHL como SMS, ver [[feedback-whatsapp-applevel-sms]]).
`is_enabled_for_insights` está en `true`, pero igual reporta 0. **Las aperturas reales por
plantilla viven en GHL** (botón *"View reports"* junto a cada template), no en la API de Meta.

## Proxy data-driven que sí funciona: "ubicuidad por sede"
Como no hay aperturas vía Meta, se rankean los faltantes por **en cuántas sedes activas
(MDE+BAQ+PAN) existe la misma plantilla** (si está en las 3, el equipo claramente la usa):
- **44** en las 3 sedes → núcleo probado.
- 21 en 2 sedes · 25 en 1 sede (dudosos).
- **75 solo en la Bogotá vieja** → one-offs de temporada (`11_frio`, `halloween_octubre`,
  `reserva_abril`…) → **NO copiar**.

## Ejecutado: copia Tier 1 a Bogotá nueva (310)
- **22 plantillas TEXT copiadas** (con dedupe, sin tocar lo existente) → Bogotá nueva pasó de
  **12 → 35 templates**. Todas quedaron en estado **PENDING** (Meta revisando).
  - 8 UTILITY del journey: `1er/2do/3er/4to/5to_mensaje_cirugia`, `1er/3er/4to_mensaje_valoracion`.
  - 14 MARKETING TEXT operativas: `2do_mensaje_valoracion`, `bienvenida_cp`, `bienvenida_cp2`,
    `karla_rv`, `no_asistio_1`, `no_contesta_llamada_ofi`, `no_me_he_olvidado`, `opc_msj`,
    `opc2_msj`, `opc3_msj`, `opc4_msj`, `reimpacto_con_pagina`, `reimpacto_val_virtual`,
    `valoracion_confirma_3_api_vr1`.
- Prueba previa OK: `6to_mensaje_cirugia` quedó **APPROVED** (UTILITY) en minutos.
- **Tier 2 pendiente:** ~21 plantillas que están en 3/3 sedes con **IMAGE/VIDEO** — Meta no deja
  clonar el medio copiando solo el texto, hay que **re-subir imagen/video** en una 2ª pasada.

## ⚠️ Compliance — quitar `video_garantia_vitalicia`
Existe el template `video_garantia_vitalicia` en **5 líneas**. "Garantía vitalicia" es **término
prohibido** ([[restricciones-lenguaje]], [[angulos-creativos]]) → **reemplazarlo en las 5 líneas**
(no copiarlo a la nueva).

## Entregable
- Reporte **`Inventario-Plantillas-WhatsApp-Innovart-2026-06-18.html`** (KPIs, inventario de las
  7 líneas con WABA IDs/conteos/idiomas/calidad, hallazgos, proxy de ubicuidad, plan por tiers).
- En **Drive** (carpeta auditoría GHL [[feedback-carpeta-auditoria-ghl]]), file id
  `1-lj3-60bfl0r0wxCSiqebu8gTVkvA7Q2`, y copia en `~/Downloads/`.

## Pendientes
1. Revisar aprobación de las 22 (APPROVED?).
2. Tier 2: re-subir medios y copiar las ~21 con imagen/video.
3. Compliance: reemplazar `video_garantia_vitalicia` en las 5 líneas.

**Relacionado:** [[feedback-whatsapp-applevel-sms]] · [[restricciones-lenguaje]] · [[stack-pauta]]
