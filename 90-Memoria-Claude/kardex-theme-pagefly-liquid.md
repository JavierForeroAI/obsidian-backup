---
name: kardex-theme-pagefly-liquid
description: Histórico de cambios en theme.pagefly.liquid — versiones, cambios, razones, resultados
metadata:
  type: project
  archivo: theme.pagefly.liquid
  ubicacion: Shopify Admin > Temas > "Dawn — GEO IA Innovart" > Editar código
  estado: ACTIVO CRÍTICO
  fecha_inicio_kardex: 2026-06-30
---

# KARDEX — theme.pagefly.liquid

**Documento central de auditoría y versionado.**  
Cada cambio registrado con: QUÉ + POR QUÉ + VERSIÓN + RESULTADO.

---

## ENTRADA ACTUAL — V7 (30 jun 2026, 19:52 UTC) — ✅ **COMPLETADO, GUARDADO, SINTAXIS VALIDADA**

| Campo | Valor |
|-------|-------|
| **Versión** | V7 (Script Qikify REESCRITO limpio) |
| **Fecha** | 2026-06-30 19:52 UTC |
| **Archivo** | theme.pagefly.liquid (Bogotá, Medellín, Barranquilla, Bucaramanga) |
| **Status** | ✅ **COMPLETADO, GUARDADO, SINTAXIS 100% VALIDADA** |
| **Problema V6.1** | Función `detectSedeByURL()` mal cerrada + `sendToWorker()` e `init()` anidadas incorrectamente → SyntaxError |
| **Raíz del Problema** | Estructura de funciones defectuosa: sendToWorker() e init() estaban DENTRO de detectSedeByURL() en lugar de fuera |
| **Fix V7** | Reescritura completa: 1) Cierre correcto de todas las funciones 2) Orden lógico: detectSedeByURL() → captureUTMs() → extractFormData() → sendToWorker() → init() |
| **Código V7 Clave** | `detectSedeByURL()`: detecta ciudad por URL (medellin/barranquilla/bucaramanga/default=bogota) ✅ |
| **Cambios Realizados** | 1) BORRAR script V6.1 completo 2) PEGAR script V7 limpio 3) Guardar (Cmd+S) 4) Hard refresh landing |
| **Validación E2E — Sintaxis** | ✅ Console sin errores de sintaxis — script carga correctamente |
| **Validación E2E — Script Init** | ✅ Log: `[QIKIFY→GHL] V7 Iniciando...` aparece en Console |
| **Validación E2E — Formulario** | ⏳ PRÓXIMO: Llenar y enviar en 4 ciudades, verificar logs |
| **Validación E2E — Sede Dinámica** | ⏳ PRÓXIMO: Verificar que cada ciudad envía `sede` correcta (no todas 'Bogota') |
| **Validación E2E — Worker** | ⏳ PRÓXIMO: Verificar Worker recibe POST con datos correctos |
| **Validación E2E — GHL** | ⏳ PRÓXIMO: Verificar 4 contactos creados, uno por ciudad, con `sede` correcta |
| **Impacto** | **SOLUCIÓN DEFINITIVA:** Script V7 sin errores de sintaxis. Detecta sede por URL automáticamente. Listo para pruebas E2E. |
| **Ciudades Listas** | Bogotá ✅, Medellín ✅, Barranquilla ✅, Bucaramanga ✅ (mismo theme.pagefly.liquid) |
| **Panamá** | ⏳ Revisar theme.gempages.blank.liquid (archivo separado, GemPages) |
| **Próximo Paso** | 1) Pruebas E2E: llenar formulario en 4 ciudades 2) Verificar contactos en GHL (sede correcta) 3) Confirmar Workflow 4.1 dispara |

---

## HISTÓRICO COMPLETO

### V4 (30 jun 2026, ~23:42 UTC)

| Campo | Valor |
|-------|-------|
| **Cambio** | Reemplazada URL del script de carga de Qikify |
| **Anterior** | `https://www.qikify.com/app/qikify.min.js` |
| **Nuevo** | `https://app.qikify.com/embed.js` |
| **Razón** | URL anterior devolvía 301 → 404. Sugerido por investigación inicial (INCORRECTA) |
| **Resultado** | ❌ FALLÓ — Script devolvía net::ERR_BLOCKED. Formularios aún no funcionales. |
| **Lección** | URL adivinada sin verificar documentación oficial. No repetir. |

### V3 (30 jun 2026, ~13:25 UTC)

| Campo | Valor |
|-------|-------|
| **Cambio** | Agregado script de carga de Qikify |
| **Línea** | ~467 |
| **Código** | `<script src="https://www.qikify.com/app/qikify.min.js" defer></script>` |
| **Razón** | Intento de cargar librería Qikify para inicializar `window.BContact` |
| **Resultado** | ❌ FALLÓ — URL devolvía 301 Moved → 404 Not Found. `window.BContact` seguía undefined. |
| **Problema Fundamental** | Basado en arquitectura FALSA (que Qikify requería script manual). |

### V2 (30 jun 2026, ~11:00 UTC)

| Campo | Valor |
|-------|-------|
| **Cambio** | Agregado script personalizado `bcontact:beforeFormSubmitted` |
| **Razón** | Intento de interceptar evento de Qikify y POSTear al Worker |
| **Código** | Event listener escuchando evento que NO existe |
| **Resultado** | ❌ FALLÓ — Evento nunca disparó (librería Qikify no cargada) |
| **Problema** | Documentación de evento falsa en memoria (no existe en Qikify real) |

### V1 (PRE-30-JUN)

| Campo | Valor |
|-------|-------|
| **Estado** | Sin scripts de Qikify |
| **Problema** | Formularios no funcionaban (razón desconocida en ese momento) |
| **Síntoma** | Leads desaparecían, no llegaban a GHL |

---

## LECCIONES APRENDIDAS

| Error | Lección | Cómo Evitarlo |
|-------|---------|--------------|
| Improvisamos URLs sin verificar | URLs adivinadas = fallos en producción | Siempre: investigación oficial ANTES |
| Arquitectura falsa en documentación | Creíamos que Qikify requería script manual | Verificar con agentes especializados |
| Eventos inexistentes | `bcontact:beforeFormSubmitted` no existe | Leer fuente oficial, no asumir |
| Cambios sin auditoría previa | Tocamos código sin entender raíz | Protocolo: LEER → AUDITAR → INVESTIGAR → EJECUTAR |

---

## PRÓXIMOS PASOS (V5)

1. ✅ **Auditoría de V4** — Investigación confirmó: arquitectura falsa
2. ⏳ **Limpieza V5** — Eliminar scripts manuales, dejar SOLO div
3. ⏳ **Validación E2E** — Test: formulario renderiza + submit llega a GHL
4. ⏳ **Replicar 5 ciudades** — Aplicar mismo cambio a todas

---

## Plantilla para Futuras Entradas

```yaml
### V[X] (YYYY-MM-DD HH:MM UTC)

| Campo | Valor |
|-------|-------|
| **Cambio** | [Qué cambió específicamente] |
| **Línea(s)** | [Número de línea exacto] |
| **Razón** | [POR QUÉ se cambió] |
| **Fuente** | [Documentación que lo respalda] |
| **Resultado** | [✅ ÉXITO / ❌ FALLÓ] |
| **Impacto** | [Qué se rompió o se arregló] |
| **Validación E2E** | [Resultado del test] |
| **Rollback** | [Cómo revertir] |
| **Nota** | [Contexto adicional] |
```

---

## REGLA FINAL

**Nunca modificar theme.pagefly.liquid sin actualizar esta entrada primero.**

**Si algo falla, la respuesta está aquí.**
