---
name: home5-capa-optimizacion-cro
description: Capa de optimización CRO de la landing /home5 (Bogotá Ads) inyectada por bodyTrackingCode del funnel. Tema claro médico + copy compliant + tracking + Lead suprimido en navegador. Incluye el GOTCHA de update_funnel (no mergea).
metadata:
  type: project
---

# Landing /home5 — capa de optimización CRO (2026-06-20)

Página de PRUEBA para A/B vs `/home4` (live). Todo se aplica por una **capa runtime** inyectada en el `bodyTrackingCode` del funnel, **scopeada con guard a `/home5`** (la `home4` live no se afecta).

## IDs
- **Subcuenta:** Innovart Medical IPS Bogota `DgjjDzD9nkCKv8AGF1Qb`
- **Funnel:** "Landing 1 Home " `6gDZimr1JRoW9iQZZnRH` (dominio implantecapilarencolombia.com)
- **Páginas:** home4 (LIVE) `PaBAMA8f6ISzy4H3HHty` · **home5 (prueba)** `F6xTmSqYRLizoZ1SJmDg`
- **Clarity ID:** `x62cig8qug` · **Pixels:** 1625645205284016 + 1642103999710262

## ⚠️ GOTCHA CRÍTICO — `update_funnel` (MCP ghl) NO mergea
`update_funnel` **borra** cualquier campo de tracking que NO le pases en la llamada. Pasar solo `bodyTrackingCode` **borró el `headTrackingCode`** (el script de Clarity + captura fbclid) → tumbó Clarity en home4 (live) y home5. Pasó 2 veces.
**Regla:** SIEMPRE enviar `headTrackingCode` **Y** `bodyTrackingCode` **juntos** en cada `update_funnel`. El head a conservar = captura fbclid + tag Clarity `x62cig8qug`. Relacionado: [[feedback-mcp-ghl-update-page]].

## Qué hace la capa (v7, vía equipo de 5 agentes + supervisor)
- **Tema claro-médico** (de la landing de referencia en Obsidian): marfil `#F9FAFB`, navy `#1A2E4A`, **CTA azul `#3470A6`** (AA), dorado `#C9963D` de acento, títulos serif Playfair. Hero conserva foto; **video pesado oculto en móvil**.
- **25 reemplazos de texto** en runtime (conversión + compliant): H1 dice el servicio, CTAs alineados a "te llaman en 10 min/agendar", claims de riesgo suavizados ("permanente/para siempre", "garantía vitalicia", "no duele", "únicos", "oferta/congelar precio", "100% seguros").
- **Limpiezas:** garantías de testimonios/FAQ suavizadas, "+200 esta semana" neutralizado, typo "clinica SantaFe"→"Clínica Santa Fe".
- **CRO:** franja de confianza (4.9★ · +6.000 procedimientos · 24 controles · 5 sedes) + microcopy bajo CTA. Antes/después legible 1:1.
- **Tracking:** ViewForm + ScrollDepth + WhatsApp como evento custom; inyecta lead_event_id/fbp/fbclid al hook leadconnector.

## Lead / CAPI (Plan B, supervisado 2026-06-20)
- **NO se construyó workflow nuevo de Lead** (habría duplicado: el `contact_created` ya cubre home5).
- En home5 se **SUPRIMEN `Lead` y `Contact` del píxel del navegador** (return temprano en el wrapper de fbq) → **el server CAPI es la fuente única** (workflow `CAPI Lead WhatsApp/Ads Bogota (NO TOCAR)` `fd50246d` + worker `innovart-capi-webhook-no-tocar`, deduplicado por contactId). Mata la inflación (los Lead fantasma de set-sticky-contacts y WhatsApp).
- Worker SÍ reenvía fbp/fbc si llegan en payload; hoy match por em/ph/fn/ln/external_id (EMQ alto). Enriquecer fbp/fbc = backlog (tocaría el workflow NO TOCAR). Ver [[capi-webhook-worker]] · [[integracion-ghl-meta-capi]].

## Atribución A/B real (2026-06-20) — form independiente + router
Para medir de verdad home4 vs home5 se creó un **formulario propio para home5** (clon byte-equivalente del de home4) y un **router** que lo engancha al mismo handler de leads, marcándolo aparte.

- **Form home5 (A/B):** `Diagnóstico Capilar — Home5 (A/B)` `RB4a58CCebT51AOpuyPd` (clon de `Diagnostico Capilar Bogota` `6aGxlY1gdbBx3vQA7XR9`: mismos 14 campos — Nombre/Apellido/Teléfono/Email + ocultos UTM/fbclid/fb_click_id/fbp/campaign_id + T&C + botón; mismo pixel `1625645205284016`).
- **⚠️ Swap del iframe en caliente (capa v9) = MALO, REVERTIDO.** `swapForm()` renombraba el iframe `inline-6aGxlY1g…` → `inline-RB4a58…`. **Rompió el form** (no dejaba escribir): la página tiene un **config estático** que inicializa `form_embed.js` con `formId:'6aGxlY1g'` y guarda una referencia `T={iframe,id}` ligada a `inline-6aGxlY1g`; al renombrar, `T.iframe` queda null → `Uncaught Error: iFrame (inline-6aGxlY1gdbBx3vQA7XR9) does not exist` (form_embed.js, función `We()`) + iframe colapsado. **NO renombrar/mutar el iframe del form en runtime.** Se revirtió a v8 (byte-perfect) y el form quedó usable de nuevo.
- **Forma correcta de poner el form A/B en home5 = swap NATIVO en el constructor de GHL** (no por capa, no por `update_page_content` que se trunca a ~94KB): abrir home5 en el page-builder → click en el elemento de formulario → cambiar el form seleccionado de `Diagnostico Capilar Bogota` a `Diagnóstico Capilar — Home5 (A/B)` (`RB4a58CCebT51AOpuyPd`) → Guardar/Publicar. Así la página embebe el form nuevo nativamente (config + form_embed correctos), el router `ac1b818d` dispara y el A/B queda limpio. La capa v8 (sin swap) convive sin problema.
- **INTERINO:** mientras no se haga el swap nativo, home5 usa el form compartido `6aGxlY1g` → sus leads caen como `landing_form_home4` (mal atribuidos). Hacer el swap nativo cuanto antes.
- **Router:** workflow `Home5 - Landing page (router a 4.1) [A/B]` `ac1b818d-70fa-4446-b575-9c8c76b9accb` (published). Trigger = form_submission de `RB4a58…` → tag **`lead_home5`** (marca A/B limpia) + **`landing_formulario`** (dispara el 4.1 `d405fcaf`: oportunidad pipeline `RpC0O3mYkxyKV1jvMqm6` + asignación Sofía `ajPncm2f7Yvjgle1kZwy` + SMS) + aviso interno "HOME5 (A/B)" a Sofía. **No se editó el 4.1** (su nodo create_opportunity es delicado).
- **Lectura del experimento:** home4 → tag `landing_form_home4`; home5 → tag `lead_home5`. Comparar conteos por tag (smart list / form submissions). Caveat: `landing_formulario` es genérico (lo usan otros leads de landing); el marcador A/B fiel de home5 es **`lead_home5`**.
- **update_funnel mergeó OK esta vez:** se envió head+body juntos igual; head (Clarity `x62cig8qug` + fbclid) verificado IDÉNTICO tras el deploy. Capa v9 desplegada byte-perfecto (diff contra `/tmp/home5-layer-v9.html`).

## Pendiente
- **Paste del `<head>` (#4):** archivo `/tmp/home5_custom_fixed.html` (quita "Garantía vitalicia" de metas, suaviza JSON-LD "no duele"/garantía, **elimina aggregateRating de 6.000 reseñas falsas** — son 6.000 CLIENTES, no reseñas, y borra código muerto). `update_page_content` no es viable (~94KB se trunca) → pegar en el editor de GHL (Cmd+A → pegar).
- Cuando home5 reemplace a home4: "hornear" tema+copy+head en el fuente para no depender de la capa.

**Why:** centraliza el estado del experimento home5 y evita re-romper Clarity. **How to apply:** para editar la capa, regenerar el bodyTrackingCode completo y enviarlo con el head Clarity en el mismo `update_funnel`. Verificar siempre por curl de `/home5` + `node --check` del JS servido.

Relacionado: [[home4-no-trackea-clics-cro]] · [[landing-home4-routing]] · [[capi-webhook-worker]] · [[feedback-mcp-ghl-update-page]]
