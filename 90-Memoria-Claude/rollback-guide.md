---
name: Rollback Guide — Revertir cambios en 30 min
description: Protocolo de rollback para theme.liquid, theme.pagefly.liquid, Workers y landings. Ejecución segura en producción sin pérdida de datos.
metadata:
  type: operational
  criticality: P0
  updated: 2026-06-30
---

# Rollback Guide — Revertir cambios en 30 min

**TIEMPO MÁXIMO DE EJECUCIÓN:** 30 minutos
**RIESGO:** Bajo (sin eliminación de datos, solo código)
**QUIÉN PUEDE EJECUTAR:** Javier + Claude Code

---

## CUÁNDO EJECUTAR ROLLBACK

Ejecutar **INMEDIATAMENTE** si:

- ❌ Leads no llegan a GHL (> 10 min)
- ❌ Formularios desaparecen de landing (> 5 min)
- ❌ fbclid NO se captura (verificado en GHL)
- ❌ Meta Pixel NO dispara (DevTools vacío)
- ❌ Errores JavaScript en consola post-deploy
- ❌ Workflow 4.1 NO se dispara automáticamente

**NO ESPERAR:** Ejecutar dentro de 60 minutos de detectado el problema.

---

## PASO 1: IDENTIFICAR QUÉ FALLÓ (5 min)

### 1a. Revisar console del navegador

Abrir landing en Chrome → F12 → Pestana "Console"

```javascript
// Ejecutar manualmente:
typeof window.BContact
// Si es "undefined" → Qikify NO cargó. Rollback theme.pagefly.liquid V3 → V2

// Revisar red:
console.log(new URLSearchParams(window.location.search).get('fbclid'))
// Si es null → fbclid NO se está capturando. Check headTrackingCode.
```

### 1b. Revisar GHL en últimas 30 min

1. Ir a GHL → Contactos
2. Filtrar por fecha creación = hoy
3. ¿Últimos 10 contactos tienen `fb_click_id` poblado?
   - **SÍ:** fbclid OK. Problema es otro.
   - **NO:** fbclid NO se captura. Rollback headTrackingCode.

### 1c. Revisar Cloudflare Worker logs

1. Ir a `https://dash.cloudflare.com/` → Workers
2. Seleccionar `innovart-capi-webhook-no-tocar`
3. Pestaña "Real-time logs"
4. ¿Hay errores 4XX o 5XX?
   - **SÍ:** Rollback Worker a versión anterior.
   - **NO:** Worker OK, problema en landing.

### 1d. Revisar Meta Ads Manager

1. Events Manager → Pixel Shopify (termina en **62**)
2. ¿Últimas 24h muestran eventos Lead/Purchase?
   - **NO:** Pixel NO dispara. Rollback theme.liquid.

**Resultado:** Ya sabes QUÉ componente falló. Ve al Paso 2.

---

## PASO 2: LOCATE VERSIÓN ANTERIOR (5 min)

### Para theme.pagefly.liquid

Ubicación de versionado:
```
/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/
  → versionado-theme-pagefly-liquid.md
```

Leer archivo y encontrar sección **"V2"** (versión anterior a V3).
- Copiar código completo V2
- Guardar en `/tmp/theme.pagefly.liquid.v2.backup` (local)

### Para theme.liquid

Ubicación:
```
/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/
  → versionado-theme-liquid.md (si existe)
  O → protocolo-versionado-codigo-critico.md (changelog anotado)
```

Si no existe documento de versionado:
1. Ir a Shopify Admin → Theme → "Dawn — GEO IA Innovart"
2. Editar → theme.liquid
3. **Ver historial:** Button "Previous versions" (derecha)
4. Seleccionar última versión estable (antes de hoy)
5. Copiar código completo

### Para Workers

1. Ir a `https://dash.cloudflare.com/` → Workers
2. Seleccionar worker (ej. `innovart-capi-webhook-no-tocar`)
3. Pestaña "Deployments"
4. Buscar deploy anterior (generalmente 1h antes del actual)
5. Click "Rollback to this version"
   - ✅ Automático, sin confirmación requerida

**Resultado:** Tienes el código V2 en `/tmp/`. Ve al Paso 3.

---

## PASO 3: APLICAR ROLLBACK (15 min)

### Opción A: theme.pagefly.liquid (PageFly UI)

1. Ir a Shopify Admin → Pages
2. Editar página de landing (ej. "/implante-capilar-bogota")
3. Click Edit con PageFly
4. Pestaña "Code" (derecha abajo)
5. Seleccionar TODO el código actual
6. Reemplazar con V2 desde `/tmp/theme.pagefly.liquid.v2.backup`
7. Click "Save & Publish"
8. Esperar 15-30s

### Opción B: theme.liquid (Shopify Theme Editor)

1. Ir a Shopify Admin → Configuración → Temas
2. Hacer clic en "..." → "Editar código"
3. Abrir archivo `theme.liquid`
4. Seleccionar TODO
5. Pegar código V2 desde `/tmp/theme.liquid.v2.backup`
6. Click "Save"
7. Shopify compila en 5s

### Opción C: Workers (Cloudflare UI)

1. Ir a `https://dash.cloudflare.com/` → Workers
2. Seleccionar `innovart-capi-webhook-no-tocar` (o la que falló)
3. Pestaña "Deployments"
4. Buscar versión anterior
5. Click el botón "Rollback"
   - ✅ Automático, desplegado en < 30s

**Resultado:** Código reverted. Ve al Paso 4 para validar.

---

## PASO 4: VALIDACIÓN POST-ROLLBACK (5 min)

### 4a. Test en navegador

1. Abrir landing en navegador NUEVO (Ctrl+Shift+N para incognito)
2. Copiar URL completa de un anuncio Meta activo (con fbclid)
3. Pegar en barra de dirección
4. Esperar carga completa (20s)

```javascript
// En Console ejecutar:
typeof window.BContact
// Debe ser "object" (NO "undefined")

console.log(new URLSearchParams(window.location.search).get('fbclid'))
// Debe mostrar valor, NO null
```

### 4b. Llenar form + enviar

1. Completar fields: Nombre, Teléfono, Correo (test@innovart.com)
2. Click "Enviar" o "Agendar Cita"
3. Esperar 5-10s

```javascript
// Revisar Network tab en DevTools:
// - ¿POST a Worker/GHL? ✅ OK
// - ¿Respuesta 200? ✅ OK
// - ¿Respuesta 4XX/5XX? ❌ Rollback falló
```

### 4c. Verificar en GHL

1. Ir a GHL → Contactos → Búsqueda rápida: "test@innovart.com"
2. ¿Contacto aparece en < 30s?
   - **SÍ:** ✅ Rollback exitoso
   - **NO:** ❌ Hay otro problema. Ir a Paso 5.

### 4d. Revisar Meta Events Manager

1. Ir a Meta Ads Manager → Events Manager
2. Pixel Shopify (termina en **62**)
3. ¿Últimas 1h muestran evento "Lead"?
   - **SÍ:** ✅ Pixel OK, rollback trabajó
   - **NO:** ❌ Pixel aún muerto. Revisar Worker.

**Resultado:** Si TODO está ✅, rollback completado. Ve a Paso 5 para documentar.

---

## PASO 5: DOCUMENTAR + NOTIFICAR (2 min)

### Crear nota de rollback en Obsidian

Archivo: `/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/rollback-log.md`

```markdown
## Rollback 2026-06-30 · 14:32 UTC

**Componente:** theme.pagefly.liquid
**De versión:** V3 → V2
**Razón:** fbclid NO se capturaba en landing Bogotá
**Tiempo ejecución:** 8 min
**Status:** ✅ Completado — Leads fluyendo normalmente

**Cambios detectados en V3:**
- Script Qikify faltaba en línea XXX
- window.BContact = undefined

**Validación post-rollback:**
- ✅ typeof window.BContact = "object"
- ✅ fbclid capturado en test
- ✅ Contacto test@innovart.com creado en GHL
- ✅ Pixel eventos 5 registrados en últimas 1h

**Próximos pasos:**
1. Revisar commit/cambio que introdujo el bug
2. Volver a aplicar V3 CON la línea de Qikify correcta
3. Test E2E en dev antes de live
```

### Notificar a equipo

```
Asunto: ⚠️ ROLLBACK completado — Landing Bogotá

Hola Esneider,

Se completó rollback exitoso en tema.pagefly.liquid (V3 → V2).
Razón: fbclid no se capturaba.

Status actual: ✅ Leads fluyendo normalmente (test verificado).

El cambio que causó el bug fue...
[explicación breve]

Próximo intento: [fecha/hora].
```

---

## REFERENCIA RÁPIDA: QUÉ REVERTIR

### Si fbclid NO se captura

**Revertir:**
- `headTrackingCode` en GHL funnel /home
- **O** Script en theme.pagefly.liquid (V3 → V2)

**Validación:** `console.log(new URLSearchParams(window.location.search).get('fbclid'))`

**Tiempo:** 5 min

---

### Si form desaparece

**Revertir:**
- theme.pagefly.liquid (V3 → V2)
- Causa probable: `</body>` faltante

**Validación:** form visible en landing desktop + móvil

**Tiempo:** 5 min

---

### Si Worker da errores 500

**Revertir:**
- Worker Cloudflare → última versión estable (Deployments → Rollback)
- Causa probable: cambio en schema CAPI o validación

**Validación:** `curl https://innovart-capi-webhook-no-tocar/health` → 200 OK

**Tiempo:** 2 min

---

### Si Pixel NO dispara

**Revertir:**
- theme.liquid (V2 → V1)
- Causa probable: script de Pixel removido o malformado

**Validación:** DevTools Network → `t.facebook.com/tr` presente

**Tiempo:** 5 min

---

### Si GHL workflows NO se disparan

**ESTE NO ES ROLLBACK DE CÓDIGO**, ver [[flujo-4-1-sms-lead-habilitado-2026-06-29.md]]:

1. Verificar workflow 4.1 está "Published" (NO Draft)
2. Verificar trigger: "Customer reply" → Canal "SMS" type 2
3. Verificar paso 1: Tag assignment activo

**Tiempo:** 5 min (sin rollback)

---

## MATRIZ DE DECISIÓN: QUÉ REVERTIR

| Síntoma | Causa probable | Componente | Versión anterior |
|---|---|---|---|
| fbclid null en consola | headTrackingCode muerto | theme.pagefly.liquid | V2 |
| Form desaparece | `</body>` falta | theme.pagefly.liquid | V2 |
| window.BContact undefined | Script Qikify falta | theme.pagefly.liquid | V2 |
| Pixel eventos = 0 | Script Meta removido | theme.liquid | V1 |
| Worker 500 error | Cambio en validación | Worker CAPI | Deployment anterior |
| Contacto NO llega a GHL | POST no dispara | theme.pagefly.liquid + Worker | V2 + Deployment anterior |
| Workflow 4.1 no dispara | Trigger deshabilitado | GHL (NO rollback) | Ver protocolo GHL |

---

## RECUPERACIÓN DE CÓDIGO HISTÓRICO

### Si no existe documento versionado en Obsidian

**Opción 1: Shopify Theme History**
1. Admin → Temas
2. Clic en "..." → "Editar código"
3. Arriba: "Previous versions" (dropdown)
4. Seleccionar date anterior al cambio problemático
5. Copiar código completo

**Opción 2: Git (si tienes acceso)**
```bash
cd ~/innovart-shopify-theme
git log --oneline theme.liquid
# Encuentra commit anterior al problemático
git show <commit-hash>:theme.liquid > /tmp/theme.liquid.safe
```

**Opción 3: Cloudflare Deployments**
1. Workers → `innovart-capi-webhook-no-tocar`
2. Deployments → historial completo
3. Click versión anterior → "View"

---

## TROUBLESHOOTING: ROLLBACK NO FUNCIONA

### Síntoma: Rollback completado pero problema persiste

**Diagnosticar:**

1. Verificar rollback se guardó:
   ```bash
   # Theme
   curl -H "Authorization: Bearer $SHOPIFY_TOKEN" \
     https://shopify.com/admin/api/themes/XXX/assets.json | grep theme.liquid
   
   # Worker
   curl https://dash.cloudflare.com/api/account/workers/deployment-rollout
   ```

2. Limpiar cache navegador:
   - Ctrl+Shift+Del → "Vaciar todo"
   - O abrir en navegador incognito

3. Esperar 5 min (Cloudflare/Shopify caché global)

4. Verificar en otra sede:
   - Si landing Bogotá funciona pero Medellín no → problema en landing específica, NO theme global

### Síntoma: Rollback falló con error de permisos

**Diagnosticar:**

1. Shopify: ¿Token tiene scope `write_themes`?
   ```bash
   # Verificar
   curl -H "Authorization: Bearer $SHOPIFY_TOKEN" \
     https://shopify.com/admin/oauth/access_scopes.json
   ```

2. Cloudflare: ¿Cuenta tiene permiso de Workers?
   - Ir a `https://dash.cloudflare.com/profile/api-tokens`
   - Verificar token "Workers Scripts — Edit" está activo

3. GHL: ¿Token de agencia válido?
   - Ir a GHL → Settings → Integrations → API → copiar token nuevo
   - Guardar en `~/.ghl-token` y reintentar

### Síntoma: Código rollback aplicado pero landing sigue antigua

**Solución:**

1. Hard refresh navegador: **Ctrl+Shift+R** (no Ctrl+R)
2. Limpiar CDN de Shopify:
   ```bash
   # Purgar cache de assets
   curl -X POST https://cdn.shopify.com/... -H "Purge-All: true"
   # O: Admin → Theme → "Delete cache"
   ```
3. Esperar 10 min (propagación global)

---

## CONTACTOS DE EMERGENCIA

| Rol | Contacto | Teléfono |
|---|---|---|
| Media Buyer | Esneider | esneidervc17@gmail.com |
| CTO Innovart | (Javier) | — |
| Soporte Shopify | support@shopify.com | — |
| Soporte Cloudflare | @cloudflare/help | — |

**ESCALADA P0 (pérdida de leads > 30 min):**
1. Ejecutar rollback (20 min)
2. Contactar Esneider + Javier (5 min)
3. Esperar 5 min confirmación

---

## ANEXO: CHECKLIST ROLLBACK RÁPIDO

```
⏱️ TIEMPO MÁXIMO: 30 MIN

[ ] 5 min — Identificar componente que falló (console + GHL + CloudFlare)
[ ] 5 min — Locate versión anterior (Obsidian O Shopify History)
[ ] 10 min — Aplicar rollback (copiar-pegar + Save)
[ ] 5 min — Validar (form + GHL + Pixel)
[ ] 2 min — Documentar + notificar equipo

✅ DONE: Leads fluyendo, fbclid capturado, form visible
```

---

**ÚLTIMA ACTUALIZACIÓN:** 2026-06-30
**VALIDACIÓN:** Testeado E2E en 5 cambios
**REFERENCIAS:**
- [[innovart-integration-final.md]] — Integración maestra
- [[protocolo-versionado-codigo-critico.md]] — Cómo documentar cambios
- [[paso-a-paso-arreglo-formularios-2026-06-30.md]] — Último estado de formularios
