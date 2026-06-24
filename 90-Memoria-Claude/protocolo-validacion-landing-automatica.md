---
name: protocolo-validacion-landing-automatica
description: Protocolo automático post-deploy landing. Ejecutar siempre después de implementar landing de prueba en GHL.
metadata:
  type: feedback
---

# Protocolo de Validación Landing (POST-DEPLOY AUTOMÁTICO)

**Cuándo activar:** Después de publicar CUALQUIER landing nueva o modificada en GHL
**Responsable:** Claude Code (automático)
**Tiempo estimado:** 10-15 minutos
**Confirmación:** Reporte final + memoria actualizada

---

## FASE 1: CONEXIÓN Y SETUP (2 min)

### 1.1 Conectar MCPs
```bash
/mcp
# Output esperado: "Reconnected to gohighlevel."
```

✅ Verificar: GHL + Meta conectados

### 1.2 Recopilar datos de la landing
- **URL:** implantecapilarencolombia.com/home (o la nueva)
- **Formulario ID:** (ej: `6aGxlY1gdbBx3vQA7XR9`)
- **Router ID:** (ej: `fbd5387a`)
- **Flujo asociado:** (ej: `d405fcaf` = Flujo 4.1)
- **Tags esperados:** landing_form_home

---

## FASE 2: VERIFICACIÓN TÉCNICA (5 min)

### 2.1 Meta Pixel Helper
```
Elemento: Meta Pixel Helper extension en Chrome
Esperado: "Pixel encontrado • N eventos"
Acción: Screenshot console si hay errores
```

### 2.2 fbclid Capture (Console)
```javascript
// En DevTools → Console
// Esperado: [FbclidCapture] Captured: <valor>
// Si no aparece → ERROR: fbclid no se captura
```

### 2.3 Router en GHL
```
Via GHL MCP:
- get_workflow_full(workflowId='<router_id>')
- Verificar: triggers, actions, tags
- Esperado: publicado (status = 'published')
```

### 2.4 Flujo asociado en GHL
```
Via GHL MCP:
- get_workflow_full(workflowId='<flujo_id>')
- Verificar: triggers include el tag esperado
- Verificar: Create Or Update Opportunity está en actions
```

---

## FASE 3: TEST END-TO-END (5 min)

### 3.1 Llenar formulario en vivo
```
URL: https://implantecapilarencolombia.com/<landing>?fbclid=IwAR_TEST_<timestamp>
Campos requeridos:
  - Email: test@innovart.com
  - Teléfono: +573001234567
  - Checkbox: ✅
Action: SUBMIT
```

### 3.2 Verificar contacto en GHL
```
Via GHL MCP:
- search_contacts(query='test@innovart.com')
- get_contact(contactId='<id>')
- Verificar:
  ✅ Email capturado
  ✅ fbclid capturado (campo: click_id o fbclid)
  ✅ fbp capturado (Facebook Browser Pixel Cookie)
  ✅ Tag landing_form_home aplicado
  ✅ Oportunidad creada en pipeline Ventas/Frio
```

### 3.3 Verificar Flujo ejecutado
```
Via GHL MCP:
- get_workflow_full(workflowId='<flujo_id>', includeLogs=true)
- Buscar: contact = test@innovart.com
- Verificar execution log:
  ✅ Assign to user: Executed
  ✅ Create Or Update Opportunity: Executed
  ✅ Workflow completado sin errores
```

---

## FASE 4: LIMPIEZA Y REPORTE (2 min)

### 4.1 Limpiar contacto de prueba
```
Via GHL MCP:
- delete_contact(contactId='<test_contact_id>')
# O marcar como "Test/Prueba" con tag
```

### 4.2 Generar reporte final
```
✅ fbclid capture: [FUNCIONA / ERROR]
✅ Meta Pixel: [FUNCIONA / ERROR]
✅ Router: [PUBLICADO / DRAFT]
✅ Flujo: [EJECUTADO / NO EJECUTADO]
✅ Oportunidad: [CREADA / NO CREADA]
✅ Test E2E: [EXITOSO / FALLIDO]

Métricas esperadas (48h después):
- EMQ score: target 5.5+
- Leads en GHL: +5 mín en 24h
- UTM coverage: <completar si aplica>
```

### 4.3 Actualizar memoria
```markdown
- Crear archivo: <landing>-validacion-exitosa-<fecha>.md
- Actualizar: MEMORY.md con nuevo enlace
- Guardar: Observaciones, issues encontrados, recomendaciones
```

---

## CHECKLIST RÁPIDO

| Paso | Status | Acción si falla |
|---|---|---|
| 1. `/mcp` conecta | ✅ / ❌ | Reintentar |
| 2. Pixel Helper ve eventos | ✅ / ❌ | Revisar console errors |
| 3. fbclid en console | ✅ / ❌ | Verificar custom code |
| 4. Router publicado | ✅ / ❌ | Publicar desde GHL |
| 5. Flujo con trigger correcto | ✅ / ❌ | Agregar trigger si falta |
| 6. Test E2E: contacto creado | ✅ / ❌ | Revisar formulario |
| 7. Test E2E: fbclid capturado | ✅ / ❌ | Revisar fieldmap GHL |
| 8. Test E2E: oportunidad creada | ✅ / ❌ | Verificar Flujo 4.1 |
| 9. Reporte guardado | ✅ / ❌ | Crear archivo en memoria |

---

## ERRORES COMUNES Y FIXES

### Error: "fbclid no se captura en console"
**Causa probable:** Custom Code no está inyectado o mal formado
**Fix:** 
1. Verificar que Custom Code existe en página
2. Revisar que fbq esté inicializado ANTES que fbclid capture
3. Inyectar código manualmente si no está

### Error: "Router no ejecuta flujo"
**Causa probable:** Tag no coincide o router no está publicado
**Fix:**
1. Verificar nombre exacto del tag (case-sensitive)
2. Confirmar router está en status "published"
3. Revisar triggers en router contienen el form_id correcto

### Error: "Oportunidad no se crea"
**Causa probable:** Flujo 4.1 no tiene trigger para el tag, o flujo no está publicado
**Fix:**
1. Agregar trigger al flujo con tag landing_form_home
2. Publicar flujo desde GHL
3. Esperar ~30s y reintentar test

---

## AUTOMATIZACIÓN FUTURA

**Próxima fase:** Script `validate-landing.ts` en Claude Code que:
1. Ejecute todo esto en paralelo
2. Genere reporte HTML automático
3. Envíe Slack a Javier si algo falla
4. Actualice memoria automáticamente

---

## REFERENCIAS

- [[fbclid-home-implementacion-exitosa-2026-06-22]] — Ejemplo exitoso (home)
- [[tracking-pixels-config]] — IDs de pixels
- [[feedback-cuentas-meta-no-son-sedes]] — Reglas GHL
