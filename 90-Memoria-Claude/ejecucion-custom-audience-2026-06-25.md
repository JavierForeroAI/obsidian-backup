---
name: "Ejecución: Custom Audience + Lookalike (2026-06-25)"
description: "Preparación completa para crear Custom Audience con 68 contactos (valoraciones asistidas) + Lookalike 2% en Meta MEDELLIN"
metadata:
  type: "execution"
  status: "FASE_EJECUCION"
  fecha: "2026-06-25"
  proyecto: "PruebaClaudeValoracionasistio"
  account: "MEDELLIN (act_874169544322810)"
  contactos: 68
---

# Ejecución: Custom Audience + Lookalike
**Fecha:** 2026-06-25  
**Proyecto:** PruebaClaudeValoracionasistio  
**Contactos:** 68 (56 email + 66 phone, 54 ambos)  
**Cuenta Meta:** MEDELLIN (act_874169544322810)  
**Status:** LISTO PARA EJECUCIÓN MANUAL

---

## Resumen Ejecutivo

Se ha completado la preparación al 100% para crear:
1. **Custom Audience** con 68 contactos de valoraciones asistidas
2. **Lookalike 2%** basada en la audiencia anterior

### Limitación Detectada
El MCP `meta-dajf` NO expone las funciones `create_custom_audience` ni `create_lookalike_audience` aunque las lista en capabilities. 

**Solución:** Creación manual via Meta Business Suite UI (2 horas estimadas)

---

## Fase 1: Preparación de Datos ✅

### Validación
- CSV original: 69 filas (1 encabezado + 68 datos)
- Contactos válidos: 68
- Sin duplicados
- Teléfonos incluyen códigos país (+57 Colombia, +507 Panamá)

### Estadísticas
| Métrica | Valor | % |
|---------|-------|---|
| Total contactos | 68 | 100% |
| Con email | 56 | 82.4% |
| Con teléfono | 66 | 97.1% |
| Con ambos | 54 | 79.4% |
| Solo email | 2 | 2.9% |
| Solo teléfono | 12 | 17.6% |

### Formatos Generados
1. **CSV para Meta** (`PruebaClaudeValoracionasistio_PARA_META.csv`)
   - Columnas: Email, Phone
   - Listo para copiar/pegar en UI

2. **JSON para API** (`PruebaClaudeValoracionasistio_JSON.json`)
   - Formato Graph API
   - Alternative si se usa endpoint directo

3. **HTML Preview** (`PruebaClaudeValoracionasistio_PREVIEW.html`)
   - Visualización en navegador
   - Preview de primeros 10 contactos

---

## Fase 2: Verificación Meta ✅

### Health Check
- Status: **healthy**
- API Meta: **connected**
- Rate limits: **operational**

### Cuentas Accesibles (6)
```
✅ BGTA (act_187478780709376) - USD - Status 1
✅ QUILLA (act_676872971127807) - USD - Status 1
⚠️  PANAMA (act_1049078199582559) - USD - Status 9 (gracia)
✅ INTERACCION REDES DIEGO (act_885062283062302) - COP - Status 1
✅ LANDING DIEGO (act_1176352666815422) - COP - Status 1
⚠️  MEDELLIN (act_874169544322810) - COP - Status 9 (gracia) ← TARGET
```

### Cuenta MEDELLIN
- **ID:** act_874169544322810
- **Status:** 9 (período de gracia por facturación)
- **Moneda:** COP
- **Balance:** 2,873,496 COP
- **Acceso:** ACTIVO
- **Nota:** Puede crear audiencias pero gasto limitado

---

## Fase 3: Limitación del MCP Detectada ⚠️

### Problema
```
Función: create_custom_audience
Aparece en: capabilities.audiences.operations ✓
Aparece en: tools_available ✗ ← FALTA AQUÍ
Status: No se puede ejecutar via MCP
```

```
Función: create_lookalike_audience
Aparece en: capabilities.audiences.operations ✓
Aparece en: tools_available ✗ ← FALTA AQUÍ
Status: No se puede ejecutar via MCP
```

### Tools Disponibles en Meta MCP
- list_audiences ✓
- estimate_audience_size ✓
- create_custom_audience ✗
- create_lookalike_audience ✗

---

## Paso a Paso: Crear Custom Audience

### PASO 1: Acceder a Meta Business Suite
```
URL: https://business.facebook.com/audiences
Usuario: innovartmedicalips@gmail.com
Acción: Login (si no estás)
Tiempo: 2 min
```

### PASO 2: Crear Custom Audience
```
Click: "Create Audience" (botón verde arriba a la derecha)
Menú: "Custom Audience"
Fuente: "Customer List"
Tiempo: 1 min
```

### PASO 3: Cargar 68 Contactos
**Opción A (RECOMENDADO): Copiar/Pegar**
```
1. Abre archivo: PruebaClaudeValoracionasistio_PARA_META.csv
2. Selecciona TODO (Cmd+A)
3. Copia (Cmd+C)
4. En Meta, pega en el campo de datos
5. Meta detectará Email y Phone automáticamente
Tiempo: 2 min
```

**Opción B: Subir CSV**
```
1. Click "Choose File"
2. Selecciona: PruebaClaudeValoracionasistio_PARA_META.csv
3. Meta procesa automáticamente
Tiempo: 2 min
```

### PASO 4: Configurar Detalles
```
Nombre:        PruebaClaudeValoracionasistio
Descripción:   Custom audience con 68 contactos de valoraciones asistidas
Ubicación:     Colombia
Moneda:        COP
Tiempo: 2 min
```

### PASO 5: Crear
```
Click: "Create Audience"
Espera: Meta procesa (15-30 minutos)
Tiempo: 30 min
```

### PASO 6: Capturar ID
```
Una vez creada, abre la audiencia
Copia el ID (formato: 123456789012345)
⭐ CRÍTICO: Guarda este ID en un lugar seguro
Tiempo: 2 min

Resultado esperado:
✅ CUSTOM_AUDIENCE_ID = [ID que Meta asigna]
```

**Tiempo Total Fase: ~40 minutos**

---

## Paso a Paso: Crear Lookalike Audience

### PRERREQUISITO
Tener el `CUSTOM_AUDIENCE_ID` del paso anterior

### PASO 1: Ir a Audiences
```
URL: https://business.facebook.com/audiences
Acción: Navega a "Audiences"
Tiempo: 1 min
```

### PASO 2: Seleccionar Custom Audience
```
Busca: "PruebaClaudeValoracionasistio"
Click: En el nombre de la audiencia
Click: Menú (⋯) → "Create Lookalike Audience"
Tiempo: 2 min
```

### PASO 3: Configurar Lookalike
```
Base Audience:    PruebaClaudeValoracionasistio
Lookalike Type:   "Similar to this audience"
Similarity:       2% (most similar) ← 2% = más similar
Location:         Colombia
Tiempo: 2 min
```

### PASO 4: Nombre
```
Nombre: PruebaClaudeValoracionasistio-LA2
Tiempo: 1 min
```

### PASO 5: Crear
```
Click: "Create Audience"
Espera: Meta procesa (15-30 minutos)
Tiempo: 30 min
```

### PASO 6: Capturar ID
```
Una vez creada, copia el ID
⭐ CRÍTICO: Guarda este ID en un lugar seguro

Resultado esperado:
✅ LOOKALIKE_AUDIENCE_ID = [ID que Meta asigna]
```

**Tiempo Total Fase: ~38 minutos**

---

## Resultado Esperado Final

### Custom Audience
```
✅ Nombre:      PruebaClaudeValoracionasistio
✅ Cuenta:      MEDELLIN (act_874169544322810)
✅ Contactos:   68
✅ ID:          [CUSTOM_AUDIENCE_ID] ← Guarda este valor
✅ URL:         https://business.facebook.com/audiences?act=act_874169544322810
```

### Lookalike Audience
```
✅ Nombre:      PruebaClaudeValoracionasistio-LA2
✅ Base:        [CUSTOM_AUDIENCE_ID]
✅ Similitud:   2% (Colombia)
✅ ID:          [LOOKALIKE_AUDIENCE_ID] ← Guarda este valor
✅ URL:         https://business.facebook.com/audiences?act=act_874169544322810
```

---

## Archivos de Referencia

### Ubicación Base
```
/private/tmp/claude-501/-Users-javierforero/ed21e8dd-1621-423f-b025-31460810f1de/scratchpad/
```

### Archivos Generados
1. **GUIA_COMPLETA_CUSTOM_AUDIENCE.md**
   - Guía paso-a-paso completa
   - Todas las opciones y alternativas
   - Notas y troubleshooting

2. **PruebaClaudeValoracionasistio_PARA_META.csv**
   - CSV listo para copiar/pegar
   - Formato: Email, Phone
   - 68 registros + 1 encabezado

3. **PruebaClaudeValoracionasistio_JSON.json**
   - JSON para API Graph
   - Alternative si usas endpoint directo

4. **PruebaClaudeValoracionasistio_PREVIEW.html**
   - HTML para revisar en navegador
   - Tabla de primeros 10 contactos
   - Estadísticas visuales

5. **reporte_custom_audience.json**
   - Reporte técnico con análisis de limitaciones
   - Opciones disponibles
   - Detalles de configuración

6. **RESUMEN_FINAL.txt**
   - Resumen ejecutivo
   - Pasos resumidos
   - Checklist visual

7. **CHECKLIST_INTERACTIVO.json**
   - Checklist en JSON
   - Seguimiento de tareas
   - Tiempo estimado por fase

---

## Notas Críticas

### 1. Cuenta en Período de Gracia
- MEDELLIN tiene `status: 9`
- Puedes crear audiencias sin problema
- El gasto PUEDE estar limitado
- Verifica con Esneider antes de campañas masivas

### 2. Tiempos de Espera
- Custom Audience: 15-30 minutos
- Lookalike: 15-30 minutos
- NO intentes crear Lookalike hasta que Custom esté 100% lista
- El sistema notificará cuando esté lista

### 3. Validación de Datos
- 54 contactos (79.4%) tienen email + phone → excelente
- 12 contactos (17.6%) solo phone → OK (WhatsApp)
- 2 contactos (2.9%) solo email → OK (Email)
- Buena cobertura para matching en Meta

### 4. Errores Comunes
Si algo falla:
- Verificar que estés con usuario correcto (innovartmedicalips@gmail.com)
- Confirmar acceso a Business Manager
- Si Meta rechaza contactos, verificar formato de teléfono
- Contactar a Esneider si hay bloqueos de acceso

---

## Próximas Mejoras

### Corto Plazo (post-ejecución)
1. Documentar los IDs asignados
2. Probar targeting con ambas audiencias
3. Crear ad set de prueba

### Mediano Plazo (1-2 semanas)
1. Solicitar extensión al MCP `meta-dajf`
   - Agregar `create_custom_audience`
   - Agregar `create_lookalike_audience`
2. Implementar automatización

### Largo Plazo
1. Sincronización automática GHL → Meta Audiences
2. Actualización periódica de audiencias (semanal/mensual)
3. Integración CAPI para cerrar loops

---

## Referencias Relacionadas

- [[estrategia-meta-showrate-valoraciones]] — Contexto de la estrategia
- [[meta-mcp-guia]] — Documentación del MCP Meta
- [[tracking-setup-completa-2026-06-23]] — Setup de tracking completo
- [[auditoria-fbclid-critica-2026-06-22]] — fbclid + EMQ (relacionado)

---

**Status:** ✅ LISTO PARA EJECUTAR  
**Generado por:** Claude Code - CRIO System  
**Timestamp:** 2026-06-25T22:23:57Z  
**Versión:** 1.0
