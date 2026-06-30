---
name: webhook-config-location-meta
description: Ubicación exacta de configuración de webhooks en Meta + datos Bogotá + plantilla para otros números
metadata:
  type: reference
---

# Webhook Configuration — Ubicación Exacta en Meta

**Hallazgo final:** 2026-06-29 15:58

---

## **RUTA EXACTA EN META (developers.facebook.com)**

```
My Apps 
  → [Selecciona tu app: CLAUDE CODE DA-JF]
  → Use case: "Conectar en WhatsApp"
  → Menú izquierdo: "Configuración de la API"
  → Paso 3: "Configurar webhooks para recibir mensajes"
  → Botón azul: "Configurar webhooks"
```

---

## **INTERFAZ DE CONFIGURACIÓN**

La pantalla tiene 3 campos editables:

1. **URL de devolución de llamada** — campo de texto (HTTPS requerido)
2. **Token de verificación** — campo de texto (Meta envía este token en GET challenge)
3. **Campos del webhook** — tabla subscriptible (account_alerts, account_review_update, etc.)

Botones de acción:
- **"Verificar y guardar"** (azul) — aplica los cambios
- **"Eliminar suscripción"** (gris) — borra la configuración

---

## **DATOS ACTUAL — BOGOTÁ (310)**

**Estado:** ACTIVO (apunta a innovart-wa-redirect-320)

| Campo | Valor Actual |
|---|---|
| URL de devolución de llamada | `https://innovart-wa-redirect-320.innovartmedicalips.workers.dev/` |
| Token de verificación | `••••••••••••••` (oculto, guardado en Meta) |
| Campos suscritos | account_alerts, account_review_update, account_settings_update, account_update, automatic_events, business_capability_update, business_status_update, + más |

---

## **DATOS NUEVO — BOGOTÁ (310) — CTWA TRACKING**

**Estado:** PENDIENTE DE APLICAR

| Campo | Valor Nuevo |
|---|---|
| URL de devolución de llamada | `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/wa-ctwa` |
| Token de verificación | `innovart-ctwa-verify-2026` |
| Campos suscritos | (no cambiar — mantener igual) |

**Pasos:**
1. Editar URL — reemplazar completamente
2. Editar Token — reemplazar completamente
3. Haz clic en **"Verificar y guardar"**
4. Meta enviará GET challenge a la URL nueva
5. Nuestro Worker responde con el verify_token
6. Si OK → confirmación en verde

---

## **PLANTILLA PARA OTROS 3 NÚMEROS**

Cuando configuremos Medellín (317), Barranquilla (313), Panamá (650):

**Misma URL para TODOS:**
```
https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/wa-ctwa
```

**Mismo Token para TODOS:**
```
innovart-ctwa-verify-2026
```

**Nota:** Un ÚNICO webhook en el Worker CAPI recibe TODOS los números.
El routing interno (by phone_number_id) detecta la ciudad.

---

## **VERIFICACIÓN POST-CAMBIO**

Después de guardar cada número:

1. ✅ Meta debe mostrar "Verificado" en verde
2. ✅ Nuestro Worker debe recibir 1x GET challenge
3. ✅ Worker responde con el challenge token
4. ✅ Meta confirma la configuración

**Cómo verificar:**
- Log en nuestro Worker (tail Cloudflare): buscar GET request desde Meta
- Comando: `npx wrangler tail` en `/innovart-capi-webhook-no-tocar`

---

## **ESTADO POR CIUDAD**

| Ciudad | Número | phone_number_id | Estado | Acción |
|---|---|---|---|---|
| Bogotá | +57 310 2031796 | 1156200067575713 | ⏳ Listo para cambiar | Cambiar URL + Token |
| Medellín | +57 317 1224977 | 611850088685930 | ⏳ Pendiente | Aplicar misma URL + Token |
| Barranquilla | +57 313 2754191 | 625405087319822 | ⏳ Pendiente | Aplicar misma URL + Token |
| Panamá | +507 650 76869 | 662014553651143 | ⏳ Pendiente | Aplicar misma URL + Token |

---

## **REFERENCIAS RELACIONADAS**

- [[whatsapp-phone-numbers-meta-api]] — Números y phone_number_ids
- [[ctwa-tracking-whatsapp-ads]] — Sistema completo CTWA
- [[plan-b-webhook-revert-bogota]] — Plan B si falla Bogotá
