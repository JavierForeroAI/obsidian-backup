---
name: captura-linea-vieja-320-ghl
description: Worker que captura los entrantes de la línea WhatsApp VIEJA de Bogotá (320) y avisa al comercial en GHL, porque la línea está bloqueada bajo LeadConnector y no puede responder.
metadata:
  type: project
---

# Captura de leads — Línea WhatsApp VIEJA de Bogotá (+57 320 8653730)

**Fecha:** 2026-06-19. Contexto: la pauta ya migró a la línea **310** (+57 310 2031796). La **320** (`phone_id 609046938958518`, WABA `1306754600435441`) quedó como línea vieja y NO se atiende.

## El candado (por qué no se pudo "responder solo" desde la 320)
- La 320 es **Cloud API** pero su ENVÍO está registrado a la app de **LeadConnector** (BSP). En Cloud API, varias apps pueden RECIBIR el webhook, pero solo la app dueña puede ENVIAR.
- Nuestra app (`CLAUDE CODE DA-JF`, `1698932398019234`) se suscribió al webhook de la WABA y **recibe** los mensajes, pero al intentar responder da `(#200) You do not have the necessary permissions to send messages` — aunque se le asignó MANAGE sobre la WABA.
- Para tomar el envío habría que **re-registrar** el número bajo nuestra app con el PIN de 2 pasos, pero: no hay PIN guardado, no hay SIM/teléfono físico, y **resetear el PIN en WhatsApp Manager falla** ("The PIN could not be changed") porque LeadConnector controla la verificación. → Bloqueado sin acceso físico.
- La 320 tampoco está enrutada a ninguna sede de GHL (huérfana): los entrantes le llegan a LeadConnector pero no caen en bandeja. Por eso quien escribe **no recibe respuesta**.

## La solución desplegada (captura, no respuesta)
Como la 320 no puede contestar, **capturamos** a quien escriba y avisamos a su comercial para que lo contacte desde la 310 — así no se pierde el lead.

- **Worker Cloudflare:** `innovart-wa-redirect-320` → `https://innovart-wa-redirect-320.innovartmedicalips.workers.dev`. Proyecto en `/Users/javierforero/innovart-wa-redirect-320/`.
- **Webhook:** app `CLAUDE CODE DA-JF` configurada (`object=whatsapp_business_account, fields=messages`) apuntando al worker; WABA `1306754600435441` suscrita a nuestra app (LeadConnector sigue suscrita pero inerte).
- **Flujo por cada entrante a la 320** (filtra SOLO `phone_number_id=609046938958518`):
  1. `upsert` del contacto en GHL **Bogotá** (`DgjjDzD9nkCKv8AGF1Qb`) + tag `lead_linea_vieja_320` (no toca el nombre existente).
  2. **Nota** con el texto del mensaje.
  3. **Tarea** asignada al **comercial que ya tiene el contacto** (lo notifica GHL): "te escribió por la 320 vieja, contáctalo para no perder la info" + nombre + teléfono.
  4. Si el contacto **no tiene dueño** → se asigna a **Sofia Forero** (`ajPncm2f7Yvjgle1kZwy`) + tag `lead_320_sin_dueno`.
- Verificado end-to-end 2026-06-19 (crea nota+tarea, asigna al dueño real; prueba limpiada).

## Detalles técnicos clave
- **GHL está detrás de Cloudflare → exige User-Agent de navegador** o devuelve **error 1010** (browser_signature_banned). El worker y cualquier script Python deben mandar UA tipo `Mozilla/5.0 ... Chrome`.
- Secrets del worker: `GHL_TOKEN` (PIT de Bogotá, del registro `~/Library/Application Support/elitedcs-ghl-mcp/.ghl-tokens.json`), `VERIFY_TOKEN` (handshake). `WA_TOKEN` quedó inerte (ya no se envía).
- Para listar los leads capturados: contactos con tag `lead_linea_vieja_320` en la sede Bogotá.

## Pendiente
- **Baja suave del perfil de la 320** en WhatsApp Manager → pestaña "Perfil": quitar la foto de la clínica + descripción "Número fuera de servicio, escríbenos al +57 310 203 1796". Así la línea deja de verse activa. (El nombre verificado no se puede cambiar fácil; está EXPIRED.)
- Si algún día se consigue el PIN o acceso físico al 320 → se puede migrar a nuestra app y entonces sí auto-responder (el worker quedaría listo).

Relacionado: [[flujo-financiacion-bta-capi]] (esa WABA también figura ahí), [[feedback-whatsapp-applevel-sms]], [[referencia-ghl-cuentas-innovart]].
