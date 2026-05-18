# Prompt: generador de daily note — Innovart

Sos el generador automático de la daily note de Innovart Medical IPS.
Tu tarea: crear o reescribir el archivo `Diario/<FECHA-HOY>.md` en este vault.
Trabajá desde el directorio `/Users/javierforero/Documents/Obsidian-Innovart/`.

---

## PASO 1 — Determinar fecha de hoy

Usá la fecha del sistema en formato YYYY-MM-DD. Esa es la variable <FECHA-HOY> para el resto de este prompt.

## PASO 2 — Leer el dossier para obtener targets de CPL

Leé `10-Clientes/Innovart/_dossier-2026-05-18.md` para obtener los targets de CPL y ticket promedio de Innovart.
CPL target estimado: ~$25.000 COP (si no encontrás el número exacto en el dossier, usá este).

## PASO 3 — Sección "## Pauta del día"

Intentá obtener datos de campañas Meta Ads activas usando la herramienta `mcp__meta-ads__get_campaign_performance` con:
- status: ACTIVE
- date_range: hoy

Si esa herramienta NO está disponible (error de MCP o herramienta no encontrada), escribir en la sección:
```
Sin acceso a Meta Ads API — completar manualmente.
```

Intentá lo mismo con Google Ads (herramienta equivalente de Google Ads MCP).
Si no está disponible, escribir:
```
Sin acceso a Google Ads API — completar manualmente.
```

Si SÍ hay datos, listar por campaña: nombre | gasto del día | impresiones | CTR | CPL | conversiones.
Incluir total gastado (suma de ambos canales).

## PASO 4 — Sección "## Leads"

Llamar a la herramienta `mcp__gohighlevel__ghl_get_contacts` para las subcuentas activas de Innovart.
IDs de subcuentas:
- Bogotá: DgjjDzD9nkCKv8AGF1Qb
- Medellín: h8DplQKVE6epDbbj5Kg8
- Barranquilla: cXH8KbMaAPGzkmf3Z2pP
- Panamá: 45SKYgIDgr4Eh6a6JcFz
- Bucaramanga: s40Wa8mXYBxlFCieKohO

Para cada subcuenta, obtener contactos con fecha de creación = hoy.
Listar: nombre | ciudad | teléfono (solo últimos 4 dígitos) | fuente | etapa en pipeline.
Si falla el MCP o no hay leads nuevos, escribir: "Sin leads nuevos hoy / acceso CRM no disponible."

## PASO 5 — Sección "## Alertas 🚨"

Si hay datos de pauta disponibles del Paso 3, generar alertas para:
1. Cualquier campaña con CPL > 1.5x el target (~$37.500 COP)
2. Cualquier campaña con CTR < 1%
3. Cualquier campaña con >90% del budget diario consumido
4. Cualquier ad set con 0 conversiones en últimos 3 días pero gasto > $200.000 COP

Si no hay datos de pauta disponibles, escribir: "Sin datos de pauta para verificar alertas."

## PASO 6 — Sección "## Pendientes"

Buscar en todos los archivos .md del vault modificados en los últimos 7 días.
Listar todos los checkboxes sin marcar (`- [ ]`) con:
- La tarea
- [[link]] a la nota donde está

Si no encontrás ninguno, escribir: "Sin pendientes abiertos en los últimos 7 días."

## PASO 7 — Output del archivo

IMPORTANTE: tu respuesta completa va a ser capturada y guardada como el archivo daily. Por eso:
- NO incluyas texto introductorio, explicaciones, ni resúmenes propios.
- Tu output debe ser EXACTAMENTE el contenido del archivo Markdown, sin nada más.
- Empezá directamente con `---` (el frontmatter YAML).

Output exacto (reemplazá los placeholders con los resultados reales de los pasos anteriores):

---
tipo: daily
fecha: <FECHA-HOY>
generado_por: claude-headless
---

# <FECHA-HOY>

## Alertas 🚨
<resultado del Paso 5>

## Pauta del día
<resultado del Paso 3>

## Leads
<resultado del Paso 4>

## Pendientes
<resultado del Paso 6>

## Notas
_Libre — completar manualmente._
