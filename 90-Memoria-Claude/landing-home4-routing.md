---
name: landing-home4-routing
description: "Cómo entran y se rutean los leads del landing /home4 (implantecapilarencolombia.com) en GHL Bogotá — formulario, router, tag y flujo 4.1"
metadata: 
  node_type: memory
  type: project
  originSessionId: c263fcc0-8f6d-4ee8-a919-3378689b69d6
---

# Landing /home4 → ruteo de leads (GHL Bogotá)

Montaje verificado en vivo el **2026-06-13**. Todo vive en la subcuenta **Innovart Medical IPS Bogota** (`DgjjDzD9nkCKv8AGF1Qb`). La landing `https://implantecapilarencolombia.com/home4` es el paso **"Home4"** del funnel **"Landing 1 Home"** (`6gDZimr1JRoW9iQZZnRH`, pageId `PaBAMA8f6ISzy4H3HHty`, dominio `Rk0eHbUsLpB9uQuPG27S`).

## Recorrido del lead
```
Form en /home4  →  Router pone tag landing_form_home4 + avisa a Sofia
                →  el tag dispara el flujo 4.1  →  oportunidad + asigna a Sofia + intentos_llamada=1
```

## Piezas (IDs)
- **Formulario en vivo en /home4:** `6aGxlY1gdbBx3vQA7XR9` ("Diagnostico Capilar Bogota"). La página lo embebe por un bloque de **Código personalizado** (iframe + script). El **2026-06-13 le apliqué el diseño nuevo** (Nombre/Apellido/Teléfono/Email + consentimiento, **sin** las fotos antiguas, botón "Agendar mi valoración"). Conserva sus submissions históricas.
  - **Tracking de atribución (2026-06-13):** antes solo capturaba `fbclid`, por eso los leads (ej. Johan `DbEXWSgD3UYRLLzhkKFP`) llegaban con UTMs/fb_click_id/campaña vacíos. Le agregué **8 hidden fields** (queryKey → campo de Bogotá): `fbclid`→`DnKbVMv2xH3kNEksDV5h`, `fbclid`→`fb_click_id` `1hdDWOfia3IljwbLwqNC` (el que lee el CAPI), `utm_source`→`bRG4YVkotWP9YjicYhnA`, `utm_medium`→`GYiGihp4RIr2kVk34C2i`, `utm_campaign`→`MBNCUu8uyZbQassuPs6r`, `utm_content`→`ZZOmsPTSRhnKhUvSGgVu`, `utm_id`→`Campaign Id` `JOd9jgxiWgfTxiyHWGTJ`, `fbp`→`xqGgBJ8iteGTBGOzRYeY`. Los UTMs + utm_id + fbclid se llenan solos desde la URL; **`fbp` queda como slot vacío** hasta que la landing inyecte la cookie `_fbp` (pendiente dev). Aplica a leads nuevos; los previos NO se rellenan solos.
- **Formulario nuevo dedicado (clon en Bogotá):** `huSVZkJqk19eAPi3Xg9E` ("Formulario Landing page 1"). Mismo diseño. Si algún día swapean el embed de la página a este ID, también funciona (el router lo cubre). ⚠ Su gemelo `akg7psKDdPd3yE9uvD91` vive en la cuenta **principal** (`NPhQTmLOHd6FbDtqLPnG`) — **NO usar ese en la página**: sus leads caerían en la cuenta principal, no en Bogotá.
- **Router** `fbd5387a-4311-4ce4-a067-e61717fa98fe` ("Home4 - Landing page 1 (router a 4.1)"): 2 triggers `form_submission` (forms `6aGxlY1g` **y** `huSVZkJqk19eAPi3Xg9E`) → acción `add_contact_tag` `landing_form_home4` → notificación interna a Sofia ("🔔 Nuevo Lead — Landing Form Home4 Bogotá").
- **Flujo de nurture** `4.1 Recibir lead de Landing_formulario` (`d405fcaf-adc7-4281-b36c-f647f8707f17`): se le agregó un **2º trigger por tag** `landing_form_home4` (sin tocar sus 8 pasos ni el trigger original `landing_formulario`). Crea oportunidad en pipeline `RpC0O3mYkxyKV1jvMqm6`, asigna a **Sofia Forero** (`ajPncm2f7Yvjgle1kZwy`), pone `intentos_llamada=1` (campo `hvOu2jmDIXZLwWHsTmD9`).
- **Tag** `landing_form_home4` (`JGGnenesICFOCpT0Bc9H`).

## Notas / caveats
- **`4.1` es compartido** con la landing de **Barranquilla** (trigger `landing_formulario`). Por eso el aviso "Home4 Bogotá" se puso en el **router** (exclusivo de home4) y NO se tocó el SMS interno de `4.1` (que dice "Barranquilla") para no mal-etiquetar a Barranquilla. Consecuencia: un lead de home4 recibe AMBOS avisos. Limpiarlo requeriría ramificar (GHL no fusiona ramas).
- GHL **no fusiona ramas** y **no mueve formularios entre subcuentas** (por eso se clonó/repurpuso en Bogotá).
- `update_workflow_actions` **conserva las acciones** si solo mandas `triggers` (probado). Para cambiar un paso hay que reenviar todo el array de acciones.
- Cumple [[feedback_fbclid_landing_pages]] (el form captura `fbclid` + `fb_click_id`).
- **Form solo existe en Bogotá; aún NO duplicado a otras sedes** (Medellín/BAQ/Panamá/Bucaramanga). Plan: dejar el de Bogotá "perfecto" y luego duplicar. ⚠ Al duplicar, **los IDs de campo personalizado son distintos por subcuenta** — hay que remapear cada hidden field al ID local (ej. Medellín: fb_click_id `SFpTjWRflMI3AURvNBqF`, utm_source `kLMdTD6z21PLsxOVccGh`, utm_medium `LBRvQTYSAxKyWSATOvOG`, utm_campaign `EYtlSV5Zo5bIFMWrt7zd`, utm_content `fkLu6dW4S2Qq61NlM20J`, fbp via campo a crear). Medellín hoy NO tiene form home4; sus forms son otros (cirugía/control/agenda).
- **Pendiente dev (Esneider) — no se arregla por MCP:** (1) la URL del home4 viene **duplicada** (params 2 veces → dos `fbclid` distintos; el del form ≠ el de la atribución) → corregir para que cada param salga 1 vez; (2) inyectar cookie `_fbp` al form (`fbp` sigue vacío); (3) plantilla UTM de Meta mal mapeada (`utm_medium` trae campaign.id, no adset.id) — correcto: `utm_campaign={{campaign.id}}` `utm_medium={{adset.id}}` `utm_content={{ad.id}}` `utm_id={{campaign.id}}`.

Relacionado: [[stack-pauta]] · [[crm-funnel]] · [[integracion-ghl-meta-capi]] · [[meta-mcp-guia]]
