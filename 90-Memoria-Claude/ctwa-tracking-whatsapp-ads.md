---
name: ctwa-tracking-whatsapp-ads
description: Sistema de tracking ctwa_clid para anuncios Meta → WhatsApp. Estado, phone_number_ids, secrets configurados y pasos pendientes.
metadata:
  type: project
---

# CTWA Tracking — Meta Ads → WhatsApp → GHL

**Fecha inicio:** 2026-06-29  
**Estado:** 🟡 En progreso — falta URL webhook de WhatsApp Plugins

**Why:** 386 conversaciones de WhatsApp por semana desde anuncios Meta = 0% atribución. No se sabe qué anuncio generó cada lead. El ctwa_clid es la huella digital del clic en el anuncio — Meta la envía al servidor de WhatsApp pero WhatsApp Plugins la borra antes de pasarla a GHL.

**How to apply:** El Worker intercepta el webhook de Meta ANTES de WhatsApp Plugins, guarda el ctwa_clid en el contacto de GHL, y luego reenvía el mensaje a WhatsApp Plugins para que todo funcione normal.

---

## Arquitectura de la solución

```
Meta (anuncio clickeado)
  ↓ webhook con ctwa_clid
Worker /wa-ctwa  ← NUEVO PUNTO DE INTERCEPCIÓN
  ↓ guarda ctwa_clid en GHL
  ↓ relay →  WhatsApp Plugins
                ↓
              GHL (conversación normal)
```

---

## Phone Number IDs de Meta (WABA) — CONFIRMADOS

| Ciudad | Número WA | phone_number_id Meta |
|---|---|---|
| Bogotá | +57 310 2031796 | `1156200067575713` |
| Medellín | +57 317 1224977 | `611850088685930` |
| Barranquilla | +57 313 2754191 | `625405087319822` |
| Panamá | +507 650 76869 | `662014553651143` |
| Bucaramanga | — | Sin WhatsApp aún |

**Nota:** Bogotá migró de número. El número antiguo era +57 320 8653730 (phone_number_id: `609046938958518`) — ya inactivo.

---

## Secrets en Cloudflare Worker (`innovart-capi-webhook-no-tocar`)

| Secret | Estado | Valor |
|---|---|---|
| `WA_VERIFY_TOKEN` | ✅ Configurado | `innovart-ctwa-verify-2026` |
| `WA_PHONE_NUMBER_MAP` | ✅ Configurado | `{"1156200067575713":"bogota","611850088685930":"medellin","625405087319822":"barranquilla","662014553651143":"panama"}` |
| `WA_PLUGINS_RELAY_URL` | ⏳ PENDIENTE | URL webhook de WhatsApp Plugins en Meta |

---

## Worker endpoint

- **URL:** `https://innovart-capi-webhook-no-tocar.workers.dev/wa-ctwa`
- **GET:** responde al challenge de verificación de Meta
- **POST:** procesa webhook, extrae ctwa_clid, upserta contacto en GHL, relay a WA Plugins

---

## Custom field ctwa_clid en GHL

- **ID del campo:** `UHB4VHlBQ2XnnZODeGRK`
- **fieldKey:** `contact.ctwa_clid`
- **Mismo ID en las 5 sub-cuentas** (verificado 2026-06-29)

---

## Pasos pendientes para activar

### Paso 1 — Obtener URL del webhook de WhatsApp Plugins (Javier)
1. Entrar a business.facebook.com
2. Configuración del negocio → Cuentas de WhatsApp
3. Clic en cualquier número (ej: Bogotá 310 2031796)
4. Buscar "URL de devolución de llamada" o "Configuración de webhook"
5. Copiar esa URL (empieza con https://app.whatsappplugins.com/... o similar)
6. Pasarla a Claude

### Paso 2 — Configurar último secret (Claude)
```
echo "URL_AQUÍ" | npx wrangler secret put WA_PLUGINS_RELAY_URL
```

### Paso 3 — Cambiar webhook en Meta para las 4 WABAs (Javier)
Para cada uno de los 4 números (Bogotá, Medellín, Barranquilla, Panamá):
1. business.facebook.com → Configuración → Cuentas de WhatsApp → seleccionar número
2. Configuración del webhook → Editar URL
3. Nueva URL: `https://innovart-capi-webhook-no-tocar.workers.dev/wa-ctwa`
4. Token de verificación: `innovart-ctwa-verify-2026`
5. Guardar

### Paso 4 — Verificar (Claude + Javier)
1. Javier envía un mensaje de prueba desde un anuncio activo
2. Claude verifica en GHL que el contacto tiene el campo ctwa_clid lleno

---

## GHL Workflow relacionado

- **Nombre:** `UTM-WA-Directo-Tracker`
- **ID:** `cf7e99e5-3efb-43ab-8775-c8b340428adc`
- **Rama A:** verifica si ctwa_clid existe → asigna tags UTM
- **Estado Rama A:** ⏳ NUNCA se activa hasta que el Worker esté configurado

---

## Contexto técnico

### Por qué el interceptor es necesario
WhatsApp Plugins recibe el webhook de Meta con el ctwa_clid incluido. Pero al reenviar el mensaje a GHL, WhatsApp Plugins NO incluye el ctwa_clid — solo manda el texto del mensaje. GHL nunca ve ese dato.

### Por qué el Worker puede interceptar
Meta permite que la URL del webhook WABA apunte a cualquier servidor. Si cambiamos esa URL al Worker, el Worker recibe PRIMERO el webhook (con ctwa_clid), lo guarda en GHL, y luego lo reenvía a WhatsApp Plugins. Todo funciona igual para el asesor, pero ahora el ctwa_clid queda en GHL.

### Tipo de integración por ciudad
- Medellín: GHL Cloud API nativa (type 19) — CTWA messages show *Headline:* in body
- Bogotá, Barranquilla, Panamá: WhatsApp Plugins (type 20 / TYPE_CUSTOM_SMS)
- Bucaramanga: Sin WhatsApp

### Todos tienen WABA propia en Meta
Confirmado por Javier: las 4 ciudades tienen línea directa con Meta (WABA propia). Bucaramanga no tiene ninguna línea abierta.
