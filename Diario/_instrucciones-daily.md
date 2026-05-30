# Prompt: generador de daily note — Innovart

⚠️ INSTRUCCIÓN CRÍTICA DE OUTPUT: Tu output debe ser EXACTAMENTE el contenido del archivo Markdown, sin nada más. **NO uses la herramienta Write ni ninguna otra herramienta de escritura de archivos.** No pidas permisos. No expliques lo que estás haciendo. No agregues frases introductorias. El script que te invocó captura tu stdout directamente con `--print` y lo guarda como archivo. Empezá DIRECTAMENTE con `---` (el frontmatter YAML). Cualquier texto fuera del Markdown corrompe el archivo.

Sos el generador automático de la daily note de Innovart Medical IPS.
Tu tarea: generar el contenido del archivo `Diario/<FECHA-HOY>.md` (el script lo guarda, no vos).
Trabajá desde el directorio `/Users/javierforero/Documents/Obsidian-Innovart/`.

---

## PASO 1 — Determinar fecha de hoy

Usá la fecha del sistema en formato YYYY-MM-DD. Esa es la variable <FECHA-HOY> para el resto de este prompt.

## PASO 2 — Leer el dossier para obtener targets de CPL

Leé `10-Clientes/Innovart/_dossier-2026-05-18.md` para obtener los targets de CPL y ticket promedio de Innovart.
CPL target estimado: ~$25.000 COP (si no encontrás el número exacto en el dossier, usá este).

## PASO 3 — Sección "## Pauta del día"

Obtené datos de Meta Ads usando la herramienta `mcp__meta-dajf__get_insights` con `date_preset: "yesterday"` y `level: "account"` para CADA una de estas 4 cuentas en paralelo:

- BGTA: `act_187478780709376` (USD)
- PANAMÁ: `act_1049078199582559` (USD)
- LANDING DIEGO: `act_1176352666815422` (COP)
- MEDELLÍN: `act_874169544322810` (COP)

Fields a solicitar: `["spend","impressions","clicks","ctr","cpc","reach","actions","cost_per_action_type"]`

De `actions`, extraé:
- `lead` → leads del día
- `onsite_conversion.total_messaging_connection` → conexiones WhatsApp
- `onsite_conversion.messaging_conversation_started_7d` → conversaciones iniciadas

De `cost_per_action_type`, extraé:
- `lead` → CPL del día

Si una cuenta no devuelve datos (sin actividad ese día), escribir "Sin gasto ayer".
Si el MCP no responde con error, escribir "Sin acceso a Meta Ads API — completar manualmente."

Formatear como tabla por cuenta: Cuenta | Gasto | Leads | CPL | CTR | Conversaciones DM

Intentá también Google Ads (herramienta equivalente de Google Ads MCP).
Si no está disponible, escribir "Sin acceso a Google Ads API — completar manualmente."

Incluir total gastado USD + COP (separados por moneda).

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
