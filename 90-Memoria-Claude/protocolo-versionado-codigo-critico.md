---
name: protocolo-versionado-codigo-critico
description: 🔒 PROTOCOLO — Cada cambio en código crítico → versión con changelog en Obsidian. Regla de valor permanente.
metadata:
  type: feedback
  establecido: 2026-06-29
  aplica_a: theme.liquid, theme.pagefly.liquid, Cloudflare Workers, GHL workflows, scripts tracking
---

# 🔒 PROTOCOLO: Versionado de Código Crítico en Obsidian

## Regla Absoluta

**Cada vez que muevas/cambies código crítico (Shopify, Cloudflare, tracking, workflows):**

1. ✅ **Guarda la versión en Obsidian ANTES de tocar producción**
2. ✅ **Documenta el cambio:** qué cambió, por qué, cómo verificar
3. ✅ **Numeración:** v1 → v2 → v3 (cada sesión suma versión)
4. ✅ **Referencia directa:** en el archivo, enlaza a la sesión anterior (`[[v1-nombre-cambio]]`)
5. ✅ **Actualiza MEMORY.md** con la nueva versión

## Ejemplo: Lo que acabamos de hacer (2026-06-29)

### Archivo original:
```markdown
qikify-formulario-estructura-html-2026-06-29.md
```

### Si mañana hay que tocar esto de nuevo:
```markdown
qikify-formulario-estructura-html-v2-2026-06-30.md
- Versión anterior: [[qikify-formulario-estructura-html-2026-06-29]]
- Cambios: [lista de qué se modificó]
- Verificación: [cómo probar]
```

## Estructura de Nombre

```
[archivo]-v[numero]-[fecha-YYYY-MM-DD].md
```

**Ejemplos:**
- `theme-pagefly-liquid-v1-2026-06-29.md`
- `theme-pagefly-liquid-v2-2026-07-15.md`
- `cloudflare-worker-qikify-v1-2026-06-29.md`
- `cloudflare-worker-qikify-v2-2026-06-30.md`

## Contenido Obligatorio (cada versión)

```markdown
---
name: [nombre-archivo]-v[N]
description: [resumen 1 línea del cambio]
metadata:
  type: reference
  version: [N]
  fecha: [YYYY-MM-DD]
  status: [ACTIVO|DEPRECATED|ROLLBACK]
---

## Resumen
[Qué cambió]

## Cambios desde v[N-1]
- [Punto 1]
- [Punto 2]
- [Referencias: [[v1-nombre]], [[v2-nombre]]]

## Código Completo
[HTML/JS/Liquid completo, verificado]

## Verificación
[Pasos para probar en producción]

## Si falla (rollback)
[Instrucciones para volver a v[N-1]]
```

## Cuándo Aplicar esta Regla

✅ **SIEMPRE:**
- theme.liquid y theme.pagefly.liquid
- Cloudflare Workers (innovart-capi-webhook-no-tocar, innovart-wa-redirect-320)
- Scripts de tracking (fbclid, UTMs, CAPI)
- GHL workflows críticos (4.1, lead routing)
- Qikify form config

❌ **NO es necesario:**
- Cambios de contenido (blogs, páginas de texto)
- Configuración que NO es código (como cambiar un tag en GHL)
- Cambios visuales en PageFly (si el código HTML no cambia)

## En la Próxima Sesión

Cuando entres a trabajar en código crítico:
1. **Busca el archivo en Obsidian** (ej: "theme-pagefly-liquid")
2. **Lee la última versión** (v1, v2, vN)
3. **Si vas a cambiar:** crea v[N+1] ANTES de tocar producción
4. **Si algo se rompe:** tienes el rollback documentation listico

## Por Qué Esto Importa

| Problema | Solución | Beneficio |
|---|---|---|
| "¿Qué cambió hace 3 meses?" | Versión documentada + changelog | No pierdes contexto |
| "¿Cómo vuelvo atrás?" | Rollback steps en la versión anterior | Recuperación en minutos |
| "¿Dónde está el código correcto?" | v[N] en Obsidian | No buscar en chat/Drive/screenshots |
| "¿Otro cambio rompió esto?" | Comparar v[N-1] vs v[N] | Root cause analysis rápido |

---

## Links Relacionados

- [[qikify-formulario-estructura-html-2026-06-29]] — Primera versión (Qikify Form)
- [[plan-formulario-qikify-innovartmedical]] — Flujo Qikify → GHL completo
- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]] — Guía técnica PageFly

---

## Nota Final

**Esta regla NO es burocracia** — es un escudo. Cada versión documentada es:
- 15 min ahora → 0 min indagación después
- Contexto completo para que otro dev entienda en 2 min
- Seguro de rollback si algo falla

**Javier:** Pedirme "documenta como v2" cuando toques código. Yo me encargo de la estructura.
