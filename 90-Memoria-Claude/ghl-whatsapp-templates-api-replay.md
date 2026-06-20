---
name: ghl-whatsapp-templates-api-replay
description: Cómo crear/copiar plantillas WhatsApp en GHL por código (replay del backend LeadConnector) — endpoint, auth de agencia, formato de variables, y mapa WABA↔sede. Skill API_Whatsapp_Tem_GHL.
metadata:
  type: reference
---

# GHL WhatsApp Templates — automatización por API (replay backend)

2026-06-19. Skill **API_Whatsapp_Tem_GHL**. Cómo gestionar plantillas WhatsApp de Innovart
de forma automatizada, después de descubrir que ni el MCP de GHL ni la API de Meta sirven
para *crear en GHL*.

## Hechos clave (probados)
- **Meta API** (token con `whatsapp_business_management`): sirve para **leer/auditar/crear/borrar**
  plantillas en el WABA, pero **GHL NO importa** lo creado por Meta (su catálogo es propio) y el
  **envío** lo controla LeadConnector (Meta da `#200` si intentas enviar con token propio).
  Ver [[whatsapp-templates-lectura-creacion]].
- **La vía que SÍ funciona** para que GHL las muestre y las envíe: **replay del backend de GHL**
  (la misma petición del botón "+ Create template").

## Endpoint de creación (replay)
```
POST https://backend.leadconnectorhq.com/phone-system/whatsapp/location/{LOCATION_ID}/template
GET  (mismo path) → lista las plantillas de esa sede EN FORMATO GHL (con customVariables+example)
```
- **Cloudflare 1010**: obligatorio header `user-agent` de navegador (si no → 403 browser_signature_banned).
- **Auth** (headers): `authorization: Bearer <spm-ts JWT>` + `token-id: <firebase JWT>` +
  `channel: APP`, `source: WEB_USER`, `app-name: spm-ts`, `version: 2021-07-28`, `content-type: application/json`.
  - El token es **de AGENCIA** (`userType: agency`, role admin) → su `token-id` lista las **6 subcuentas**
    Innovart en `locations[]`, así que **una sola captura sirve para crear en cualquiera de las 6 sedes**.
  - ⚠️ **Caducan ~1h** (firebase `token-id` exp = iat+3600). Para automatización durable → MCP de navegador
    (Playwright, "Path B"). Mientras, hay que **recapturar** el token desde DevTools (Network → la POST
    `template` 201 → Copy as cURL / pestaña Payload).

## Body (payload) — formato GHL
```json
{
  "cta_url_link_tracking_opted_out": true,
  "name": "snake_case",
  "language": "es",
  "category": "UTILITY | MARKETING",
  "components": [
    {"type":"HEADER","format":"TEXT","text":"Hola {{1}}","example":{"header_text":["Mario"]},"customVariables":["{{contact.first_name}}"]},
    {"type":"BODY","text":"te habla {{1}} ...","example":{"body_text":[["Leidy"]]},"customVariables":["{{user.first_name}}"]}
  ]
}
```
- **Variables**: por cada `{{1}}`, `{{2}}`… un elemento en `customVariables` = **merge tag de GHL**
  (ej. `{{contact.first_name}}`, `{{user.first_name}}`) + el `example` con valores de muestra (lo usa Meta).
- Sin variables → `customVariables: []`.
- Respuesta: `201 {id, status:PENDING, category}`. Meta aprueba aparte (UTILITY en minutos).
  Si el formato de variable está mal → status **REJECTED**.

## Método de copia recomendado: GHL→GHL
1. `GET` plantillas de la sede origen (formato GHL nativo, con customVariables+example).
2. `POST` cada una a la sede destino (mismo formato). Dedupe por `name` (Meta rechaza nombres duplicados por WABA).
   - ⚠️ Si antes creaste el mismo nombre por **Meta API** (huérfanos), hay que **borrarlos del WABA** primero
     (Meta API DELETE por nombre) o chocan.
   - 🚫 **GOTCHA CRÍTICO (2026-06-19):** NUNCA crear+borrar un nombre por Meta API en un WABA de producción.
     Al borrar una plantilla aprobada, Meta **reserva/bloquea el nombre** mientras termina el borrado
     (error al recrear: *"New Spanish content can't be added while the existing Spanish content is being deleted"*),
     candado que dura de **minutos hasta ~4 semanas**. Pasó con 23 del núcleo (cirugía/valoración/opc/bienvenida)
     al limpiar huérfanos → quedaron bloqueadas para recrear en GHL. **Regla: crear SIEMPRE directo por GHL,
     jamás por Meta API si luego hay que borrar.**

## Mapa sede → location GHL → WABA (verificado 2026-06-19)
| Sede | GHL location | WABA | Línea | Templates |
|---|---|---|---|---|
| Bogotá ACTUAL | `DgjjDzD9nkCKv8AGF1Qb` | `1183841487216235` | +57 310 2031796 | ~13 (poca) |
| Bogotá anterior (retirada) | — | `1306754600435441` | +57 320 8653730 | 168 |
| Medellín | `h8DplQKVE6epDbbj5Kg8` | `1050305186428924` | +57 317 1224977 | 104 |
| Barranquilla | `cXH8KbMaAPGzkmf3Z2pP` | `966905258928980` | +57 313 2754191 | 144 |
| Panamá | `45SKYgIDgr4Eh6a6JcFz` | `9412257795531439` | +507 6507-6869 | 85 |
| Sede 322 (¿Bucaramanga?) | `s40Wa8mXYBxlFCieKohO`? | `547127801813891` | +57 322 8246704 | 91 |
| Principal | `NPhQTmLOHd6FbDtqLPnG` | — | — | — |

BM Meta: **Implante Innovart Medical** `940287337027000`. App con WhatsApp: "CLAUDE CODE DA-JF"
(`1698932398019234`, se le agregó el caso de uso WhatsApp). System user "CLAUDE CODE API DA-JF"
con las 20 cuentas WhatsApp asignadas. Token Meta en `~/.claude/scripts/.wa-templates.json`.

## Scripts
- Replay GHL: `/tmp/ghl_wa_replay.py` (tokens caducan; recapturar).
- Meta API (leer/crear/copiar/borrar): `~/.claude/skills/whatsapp-templates-ghl/assets/crear_whatsapp_templates_innovart.py`.

## Inventario base
HTML en Drive (carpeta auditoría GHL `1LCzzvFFQgz-SHm_5raj2DTBOoJYsli3A`):
`Inventario-Plantillas-WhatsApp-Innovart-2026-06-18.html`. 7 líneas activas, 614 templates.
Compliance: `video_garantia_vitalicia` (término prohibido [[restricciones-lenguaje]]) en 5 líneas.
