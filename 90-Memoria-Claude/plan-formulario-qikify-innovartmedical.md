---
name: plan-formulario-qikify-innovartmedical
description: ✅ COMPLETADO 2026-06-29 — Formulario Qikify conectado al CRM por Javier.
metadata:
  type: project
  status: COMPLETADO
  fecha_completado: 2026-06-29
  fecha: 2026-06-27
---

# Plan: Formulario Qikify innovartmedical.com

**Contexto:** El formulario "Implante Capilar" de Qikify vive en innovartmedical.com. Cuando alguien lo llena, Qikify envía un email a innovartmedicalips@gmail.com. Se supone que N8N lee ese email y crea el contacto en el GHL correcto según la sede elegida.

**Investigado:** 2026-06-27 con lead real de Julian duque (26-jun 19:25) y prueba del formulario GHL paralelo.

---

## Flujo actual (confirmado)

```
Usuario llena Qikify form → Qikify → email a innovartmedicalips@gmail.com → N8N (IMAP) → GHL sub-cuenta
```

## Diagnóstico

| Item | Estado | Detalle |
|------|--------|---------|
| Email Qikify llega a Gmail | ✅ | Confirmado con Julian duque |
| Datos en email: Nombre, Tel, Email, Sede | ✅ | Campo "Sedes principales: Sede - Medellin" |
| fbclid en Submit URL | ✅ | Aparece si usuario viene directo del ad Meta |
| UTMs en Submit URL | ⚠️ | Solo si estaban en la URL al momento del submit |
| N8N procesa email → crea contacto en GHL | ❌ **ROTO** | Julian duque NO aparece en ninguna sub-cuenta |
| fbclid guardado en GHL | ❌ | N8N no parsea el Submit URL |
| Routing por sede | ❓ | No se puede verificar si N8N no corre |

## Problema crítico: N8N no está procesando

El lead de Julian duque (Sede: Medellin, 26-jun-2026 19:25) llegó al email pero NO fue creado en el GHL de Medellín (`h8DplQKVE6epDbbj5Kg8`) ni en ninguna sub-cuenta. N8N está caído o el flujo tiene un error.

**Acción inmediata:** Javier debe verificar con quien maneja N8N que el flujo IMAP esté activo.

---

## Plan de acción — 3 Fases

### FASE 1 — Reparar N8N (urgente, externa a Claude)
- Verificar que el nodo IMAP esté activo y apuntando a `innovartmedicalips@gmail.com`
- Confirmar que el flujo parsea el email de Qikify y crea contacto en la sub-cuenta correcta
- Mapeo de sede → sub-cuenta:
  - "Bogotá" → `DgjjDzD9nkCKv8AGF1Qb`
  - "Medellin" → `h8DplQKVE6epDbbj5Kg8`
  - "Barranquilla" → `cXH8KbMaAPGzkmf3Z2pP`
  - "Bucaramanga" → `s40Wa8mXYBxlFCieKohO`
  - "Panama" → `45SKYgIDgr4Eh6a6JcFz`

### FASE 2 — Enriquecer N8N con fbclid + UTMs
Una vez N8N funciona, agregar extracción de parámetros del campo "Submit URL" del email:
- Parsear `fbclid` → guardar en campo GHL `FYVJpTGSmAPhiqoRwm97` (fb_click_id)
- Parsear `utm_source` → campo `ffBWPx4Qlhxb6D6toNWO`
- Parsear `utm_medium` → campo `46qWfYJubx8IAOhyFlgT`
- Parsear `utm_campaign` → campo `lPfZB842vcw2a7iD3tOD`
- Agregar tag `fuente_web_qikify` al contacto

### FASE 3 — Campo oculto en Qikify (garantía)
Para que UTMs lleguen incluso si el usuario navega antes de llenar el form:
- Agregar Custom HTML oculto en Qikify que lea fbclid + UTMs del URL via JS
- Los incluye como campos en el email → N8N los lee directamente sin parsear URL
- Esto es opcional si la Fase 2 funciona bien, pero da más robustez

---

## Datos técnicos de referencia

**IDs de sub-cuentas GHL:**
- Principal: `NPhQTmLOHd6FbDtqLPnG`
- Bogotá: `DgjjDzD9nkCKv8AGF1Qb`
- Medellín: `h8DplQKVE6epDbbj5Kg8`
- Barranquilla: `cXH8KbMaAPGzkmf3Z2pP`
- Bucaramanga: `s40Wa8mXYBxlFCieKohO`
- Panamá: `45SKYgIDgr4Eh6a6JcFz`

**Custom fields UTM en GHL:**
- utm_source: `ffBWPx4Qlhxb6D6toNWO`
- utm_medium: `46qWfYJubx8IAOhyFlgT`
- utm_campaign: `lPfZB842vcw2a7iD3tOD`
- utm_content: `hFUkJs1bRuGskcA6X5TA`
- utm_term: `ni4PMQh6l93hmoiyfEEY`
- fbclid: `FYVJpTGSmAPhiqoRwm97`

**Email de prueba real (Qikify):**
- Asunto: "You received a message from Julian duque via Implante Capilar form"
- Sender: no-reply@qikify.com
- Campos: Form Name, Nombre Completo, Correo, Número de Celular, Sedes principales, Submit URL
- Submit URL incluye fbclid cuando el usuario viene de Meta

**How to apply:** Antes de trabajar en este tema, VER PRIMERO la sección "Arquitectura Alternativa" abajo. N8N está siendo REEMPLAZADO, no reparado.

---

## ⚠️ ACTUALIZACIÓN 2026-06-27 — Arquitectura Alternativa (N8N REEMPLAZADO)

Investigación adicional del mismo día confirmó que **N8N no es la ruta óptima** y que la solución más robusta es **JS Interceptor + Cloudflare Worker**, sin N8N ni dependencias externas.

### Por qué se descartó N8N

| Hallazgo | Detalle |
|---|---|
| Qikify webhook nativo | ❌ No existe |
| Shopify Flow "Send HTTP Request" | ❌ NO disponible en plan Basic (requiere Advanced/Plus) |
| N8N IMAP | ❌ Roto + crea dependencia externa frágil |

### Nueva arquitectura decidida

```
Usuario llena Qikify form
  → MutationObserver en theme.liquid detecta el submit
  → Lee: sede, nombre, email, teléfono + fbclid (localStorage) + UTMs (sessionStorage)
  → POST a Cloudflare Worker (ruta /qikify-lead — nueva en infraestructura existente)
  → Worker mapea sede → GHL location ID
  → Worker crea contacto en sub-cuenta correcta via GHL API
  → Worker guarda fbclid + UTMs en custom fields
  → Tag: fuente_web_qikify
```

**Ventajas vs N8N:**
- Sin round-trip email (real-time)
- Tokens GHL quedan en el Worker (servidor), NO expuestos en el browser JS
- Usa Cloudflare `innovart-capi-webhook-no-tocar` (infraestructura ya existente)
- Captura fbclid y UTMs del momento exacto del submit
- Plan Basic de Shopify es suficiente

**Estado:** ✅ IMPLEMENTADO, DESPLEGADO Y VERIFICADO E2E — 2026-06-28

**⚠️ REGLA DE SEGURIDAD:** Los GHL Private Integration Tokens (`pit-...`) NUNCA se guardan en memoria, chat ni documentación. Usar placeholder TOKEN_AQUI en scripts. Esta regla fue establecida explícitamente por Javier.

---

## ✅ IMPLEMENTACIÓN COMPLETADA — 2026-06-27

### Cloudflare Worker — ruta `/qikify-lead`
- Archivo: `innovart-capi-webhook-no-tocar/src/index.js`
- Worker URL: `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead`
- Versión desplegada: `831b9a61-1b97-45a5-9d04-1aeec154cb86`
- Mapeo sede → GHL sub-cuenta via `SEDE_MAP` (ver index.js líneas 29-35)
- 5 tokens GHL guardados como Wrangler secrets (`GHL_TOKEN_BOGOTA`, `GHL_TOKEN_MEDELLIN`, `GHL_TOKEN_BARRANQUILLA`, `GHL_TOKEN_BUCARAMANGA`, `GHL_TOKEN_PANAMA`)
- CORS configurado para `https://www.innovartmedical.com` únicamente
- Normalización de teléfono: +57 (Colombia 10 dígitos) o +507 (Panamá 8 dígitos)
- Tags aplicados: `fuente_web_qikify` + `landing_formulariov2`
- Custom fields UTM + fbclid guardados en cada sub-cuenta con IDs correctos por sede
- Manejo de duplicados: si GHL retorna 400 con `meta.contactId`, hace PUT para actualizar el contacto existente
- Versión Worker verificada: `bf5bb874-6f31-40af-adaf-b3e94e96efad`

### ⚠️ Pendiente — Bucaramanga UTM fields
Bucaramanga solo recibe `fbclid`. No tiene campos `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` creados en esa sub-cuenta. Para dejarla igual que las otras 4 sedes hay que crearlos manualmente en GHL Bucaramanga y agregar los IDs al `SEDE_MAP` del Worker.

---

## ✅ VERIFICACIÓN E2E COMPLETA — 2026-06-28

Prueba con 5 contactos simulando pauta real (`utm_source=facebook`, `utm_medium=paid_social`, `utm_campaign=implante_capilar_[ciudad]_jun2026`, `utm_content=video_resultados_hombres_v3`, `fbclid=IwAR3[ciudad]_test_0628_pauta`):

| Sede | Routing | Tags | fbclid | utm_source | utm_medium | utm_campaign | utm_content |
|---|---|---|---|---|---|---|---|
| Bogotá | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Medellín | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Barranquilla | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bucaramanga | ✅ | ✅ | ✅ | ⚠️ sin campos | ⚠️ | ⚠️ | ⚠️ |
| Panamá | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Panamá detecta país automáticamente como `PA` por número de 8 dígitos ✅

### Shopify theme.liquid (tema Dawn — GEO IA Innovart, ID 181331001645)
- **BLOQUE A** (head): Captura UTMs → `sessionStorage key: inno_utms`
- **BLOQUE B v3** (antes de `</body>`): Listener `bcontact:beforeFormSubmitted` → POST al Worker
- Cubre: páginas de ciudad Medellín, Barranquilla, Bucaramanga y páginas estándar

### Shopify theme.pagefly.liquid
- **BLOQUE C** (después de `<!-- End Innovart WA + Form UTM Enrichment -->`): Mismo listener que BLOQUE B v3
- Lee UTMs de AMBOS keys: `inno_utms` y `landing_utms`
- Cubre: Home, Bogotá, Valoración, Panamá, y otras páginas PageFly

### Evento disparador
- `bcontact:beforeFormSubmitted` (evento custom de Qikify, dispara ANTES del AJAX)
- Registrado a nivel `document` → captura el form desde CUALQUIER página del sitio
- Routing determinado por la sede seleccionada en el dropdown, NO por URL de la página
- Compatible con todas las landings de ciudad que se construyan en el futuro

### Campos leídos del formulario
- Nombre: `contact[Nombre Completo]` o label que contenga "nombre"
- Email: `contact[Correo]` o label con "correo/email"
- Teléfono: `contact[Numero de Celular]` o label con "celular/whatsapp/telefono"
- Sede: `contact[Sedes principales]` o label con "sede/ciudad"

---

## ✅ FIX LEADS HUÉRFANOS — Trigger `landing_formulariov2` en workflow `4.1` (2026-06-28)

**Problema:** Los leads de Qikify llegaban al CRM con tags `fuente_web_qikify` + `landing_formulariov2`, pero el workflow `4.1 Recibir lead de Landing_formulario` solo escuchaba `landing_form_home` y `landing_form_home4`. Los leads quedaban huérfanos: contacto creado pero sin oportunidad, sin asignación de asesor y sin notificación.

**Solución:** Se agregó `landing_formulariov2` como trigger adicional al `4.1` en cada sede, conservando todos los triggers y acciones existentes.

| Sede | Workflow `4.1` ID | Acción | Estado |
|------|-------------------|--------|--------|
| Bogotá | `d405fcaf-adc7-4281-b36c-f647f8707f17` | Trigger agregado | ✅ PUBLICADO |
| Medellín | `fbe353c5-7b84-45a4-8b09-0137235e72d0` | Trigger agregado | ✅ PUBLICADO |
| Barranquilla | `a15f77f1-8c1c-46cd-97e6-1d93517eb4c2` | Trigger agregado | ✅ PUBLICADO |
| Bucaramanga | `2efd5f03-79f8-45fe-bc82-a5bee8bdfddf` | Creado desde cero | ✅ PUBLICADO |
| Panamá | `93a0ecb1-c0ce-4159-b531-0f3f6ba9c059` | Trigger agregado | ✅ PUBLICADO |

**Flujo completo (5 sedes — COMPLETADO 2026-06-28):**
```
Lead llena Qikify → Worker → GHL (contacto + UTMs + tags)
  → tag landing_formulariov2 dispara 4.1
  → Crea oportunidad en pipeline Ventas/Frio
  → Asigna asesor (only_unassigned)
  → intentos_llamada = 1
  → SMS interno al asesor
```

**Bucaramanga — detalles de implementación:**
- Campo `intentos_llamada` creado: `mKJuNllkLyy54A3o1NL4`
- Pipeline Ventas: `r6twTNR4DbLvYrtXCIHR` | Stage Frio: `85ce8f62-302f-4c76-a256-bf93d87c7947`
- Asesor asignado: Aux Administrrativo (`Y1Lj2tAjeawnEoUwHy3B`) — admin local Bucaramanga
- Campos UTM ya existían (creados en sesión anterior): utm_source `nPJRTlPWxcVrKVKki0sF`, utm_medium `8vZkuEdu6n6yZYI7xn5V`, utm_campaign `YFaOUsGEEZVT5fFSTjJf`, utm_content `vPllZizKTgC0gCef9p6H`
- **Fix Worker (2026-06-28):** El `contact_tag` trigger de GHL no dispara para workflows recién creados vía API. Solución: el Worker enrolla el contacto directamente al workflow `2efd5f03` via `POST /contacts/{id}/workflow/{workflowId}` después de añadir el tag. El `allowMultiple: false` del workflow previene enrollamientos dobles.
- **Bonus:** Se agregaron campos UTM a SEDE_MAP de Bucaramanga (antes solo tenía fbclid). Ahora utm_source/medium/campaign/content se guardan igual que las otras 4 sedes.
- ⚠️ Nota: sin wait de horario laboral (formato incompatible con MCP); se puede agregar manualmente en GHL si se desea
