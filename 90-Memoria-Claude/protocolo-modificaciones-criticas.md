---
name: protocolo-modificaciones-criticas
description: Protocolo ABSOLUTO para modificar código crítico — 7 pasos no negociables
metadata:
  type: feedback
  fecha: 2026-06-30
  estado: ACTIVO
---

# PROTOCOLO — Modificaciones de Código Crítico

**Reglas de Oro para cambios en archivos críticos.**  
Creado después de aprender lecciones en conversación 30 jun 2026.

---

## ARCHIVOS CRÍTICOS

```
Requieren protocolo COMPLETO:
- theme.liquid (base Shopify)
- theme.pagefly.liquid (landings PageFly)
- theme.gempages.blank.liquid (landings GemPages)
- Cloudflare Workers (CAPI, webhooks)
- Scripts tracking (fbclid, CAPI, pixels)
- Configuración GHL (workflows, fields)
```

---

## PROTOCOLO — 7 PASOS OBLIGATORIOS

### PASO 1: LEER
```
Antes de tocar NADA:
✅ Lee el código actual COMPLETO
✅ Entiende qué hace CADA línea
✅ Identifica dependencias (otros scripts, eventos, campos)
✅ Documenta estado ACTUAL en Kardex

No avances sin entender 100%.
```

### PASO 2: AUDITAR
```
Pregúntate:
✅ ¿POR QUÉ está así el código?
✅ ¿Cuándo se agregó? (revisar versionado)
✅ ¿Qué pasaría si lo elimino?
✅ ¿Hay dependencias que se romperían?
✅ ¿Fue probado? (E2E history)

Documentar hallazgos.
```

### PASO 3: INVESTIGAR
```
✅ Buscar documentación oficial (NO asumir)
✅ Consultar con agentes especializados
✅ Verificar si ya hay solución conocida
✅ Revisar gotchas/problemas previos

Fuente = documentación + precedentes.
Nunca = intuición o URLs adivinadas.
```

### PASO 4: REGISTRAR (Kardex ANTES)
```yaml
Versión: V[X]
Fecha: YYYY-MM-DD HH:MM UTC
Cambio Planeado: [QUÉ vas a cambiar]
Línea(s): [Exacto]
Razón: [POR QUÉ lo cambias]
Fuente: [Documentación que lo respalda]
Impacto Estimado: [Qué afecta]
Rollback Plan: [Cómo revertir]
Status: 🟡 PLANEADO
```

**REGLA:** No ejecutes sin haber registrado esto.
```

### PASO 5: EJECUTAR
```
✅ Cambio pequeño, específico, una cosa
✅ Línea exacta, no aproximado
✅ Guarda
✅ Hard refresh (Cmd+Shift+R)
✅ Toma screenshot

No toques 10 cosas a la vez.
```

### PASO 6: VALIDAR E2E
```
✅ ¿El cambio funcionó?
✅ ¿Se rompió algo más?
✅ ¿Formularios responden?
✅ ¿Leads llegan a GHL?
✅ ¿Tracking funciona?
✅ Console sin errores críticos?

Usar checklist de validación por tipo de cambio.
```

### PASO 7: ACTUALIZAR KARDEX
```yaml
Status: ✅ COMPLETADO / ❌ FALLÓ
Validación E2E: [Resultado]
Impacto Real: [Qué pasó vs estimado]
Lecciones: [Qué aprendimos]
Próximos Pasos: [Qué sigue]
```

---

## CHECKLIST DE VALIDACIÓN

### Para cambios en theme.pagefly.liquid
```markdown
[ ] Formulario Qikify renderiza visualmente
[ ] Click en "Agendar Cita" no produce error
[ ] Datos del formulario se envían al Worker
[ ] Worker recibe POST (ver Cloudflare logs)
[ ] Contacto aparece en GHL correcto
[ ] Tags aplicadas: fuente_web_qikify, landing_formulariov2
[ ] UTMs/fbclid capturados
[ ] SMS/WA workflow 4.1 dispara automático
[ ] Console sin errores (Preserve Log ON)
```

### Para cambios en theme.liquid
```markdown
[ ] Home page carga sin errores
[ ] Checkout funciona
[ ] Todas las landings cargando
[ ] Meta Pixel funciona (Network tab)
[ ] GA4 funciona
[ ] fbclid capturado en localStorage
[ ] Sin conflictos de scripts
```

### Para cambios en Cloudflare Workers
```markdown
[ ] Función despliega sin errores
[ ] Logs muestran requests correctas
[ ] POST desde landing llega al Worker
[ ] Worker valida datos
[ ] POST a GHL API exitoso (201/200)
[ ] GHL recibe contacto completo
[ ] Sin errores 422/403
```

---

## NUNCA HAGAS ESTO

```
❌ Improvisar URLs sin documentación oficial
❌ Cambiar 10 cosas a la vez
❌ Tocar código sin entender qué hace
❌ Ejecutar sin registrar en Kardex primero
❌ Validar solo tú, sin pedir segunda opinión
❌ Usar "debería funcionar" en lugar de probado
❌ Modificar sin rollback plan
❌ Ignorar advertencias del navegador/console
❌ Cambiar código crítico sin auditoría previa
```

---

## ROLLBACK RÁPIDO

Si algo falla:
```bash
1. NO toques más código
2. Lee Kardex para encontrar ÚLTIMA versión buena
3. Restaura esa versión
4. Documenta: "Revertido a VX porque [razón]"
5. Analiza: ¿Por qué falló?
6. Planifica fix alternativo
```

---

## LECCIONES DEL 30 JUN 2026

| Error | Lección | Regla |
|-------|---------|-------|
| Improvisamos URLs | URLs adivinadas = fallo garantizado | Paso 3: INVESTIGAR siempre |
| Sin Kardex | No sabíamos qué se cambió | Paso 4: Registrar ANTES |
| Múltiples cambios | Confundimos cuál rompió qué | Paso 5: Cambio singular |
| Sin auditoría | Arquitectura falsa en memoria | Paso 2: AUDITAR completo |
| No seguimos protocolo | Dimos vueltas 6 horas | Paso 1-7: Protocol SIEMPRE |

---

## RESPONSABILIDAD

**Si modificas código crítico SIN seguir este protocolo y falla:**
- Eres responsable de documentar el error
- Debes actualizar Kardex con lección aprendida
- Próxima vez: SIGUE EL PROTOCOLO

**Si lo sigues y aún falla:**
- Está documentado
- Sabemos dónde revisar
- Aprendemos juntos

---

## RESUMEN

```
LEER → AUDITAR → INVESTIGAR → REGISTRAR → EJECUTAR → VALIDAR → DOCUMENTAR

Sin atajos.
```

