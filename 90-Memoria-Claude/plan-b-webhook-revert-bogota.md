---
name: plan-b-webhook-revert-bogota
description: Plan B para revertir cambio de webhook si algo falla. Guardado 2026-06-29 15:21
metadata:
  type: project
---

# Plan B — Revertir Webhook Bogotá (310)

**BACKUP SEGURO — Si algo falla, usar esto**

## Configuración Original (2026-06-29 15:21)

**Endpoint:** `/v20.0/1156200067575713/webhook_configuration`

**GET Response:** (vacío o sin cambios visibles)
- Significado: El webhook estaba seteado en Meta pero no devuelve datos visibles via GET

**Para REVERTIR (si falla):**

```bash
POST /v20.0/1156200067575713/webhook_configuration
{
  "webhook_url": "[URL_ORIGINAL_AQUI]",
  "verify_token": "[TOKEN_ORIGINAL_AQUI]"
}
```

**Status:** El webhook original probablemente apuntaba a **WhatsApp Plugins** (no documentado exactamente porque GET no lo mostró, pero era la ubicación estándar).

---

## Pasos de Reversión (si es necesario)

1. Ir a developers.facebook.com → Herramientas → Graph API Explorer
2. Cambiar a **POST**
3. URL: `/v20.0/1156200067575713/webhook_configuration`
4. Parámetros:
   ```json
   {
     "webhook_url": "[ORIGINAL_URL]",
     "verify_token": "[ORIGINAL_TOKEN]"
   }
   ```
5. Enviar
6. Verificar que respondió `"success": true` o similar

---

## Datos de Cambio NUEVO (2026-06-29 15:21)

**Nueva URL:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/wa-ctwa`
**Nuevo Verify Token:** `innovart-ctwa-verify-2026`

**Cambio aplicado a:** Bogotá (+57 310 2031796 / phone_number_id: 1156200067575713)

---

## Status

- [x] Cambio enviado — 2026-06-29 16:03
- [x] Endpoint verificado con Meta — 2026-06-29 16:03
- [x] Prueba E2E simulada — webhook capturado, contacto creado OK
- [x] Webhook configurado global (recibe Bogotá, Medellín, Barranquilla, Panamá)
- ⏳ Prueba real en vivo — Javier test con +573002181681
