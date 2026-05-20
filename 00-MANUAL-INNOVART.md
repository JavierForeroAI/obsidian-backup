---
tipo: manual
tema: sistema-completo
fecha: 2026-05-19
version: 1.0
---

# Manual del Sistema Innovart — Claude Code + Vault

**Cliente:** Innovart Medical IPS — clínica de implante capilar, 5 sedes (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá)
**Responsable técnico:** Javier Forero
**Repositorio vault:** `github.com/JavierForeroAI/innovart-vault` (privado)

---

## 1. Cómo abrir el sistema

```bash
# Opción A — alias rápido (desde cualquier lugar)
innovart

# Opción B — manual
cd ~/Documents/Obsidian-Innovart && claude
```

Al abrir, Claude carga automáticamente:
- Contexto del cliente Innovart (dossier, memoria, stack)
- Herramientas MCP conectadas (GHL, Playwright, Google Drive…)
- Prompts y skills especializados

---

## 2. Estructura del vault

```
Obsidian-Innovart/
├── 00-Inbox/           ← capturas rápidas, borradores
├── 10-Clientes/        ← dossiers, briefs, gaps por cliente
├── 20-Pauta/           ← estrategia Meta/Google, competidores
├── 30-CRM-Leads/       ← análisis de funnel y pipeline GHL
├── 40-Contenido/       ← calendarios, guiones, copy
├── 50-Reportes/        ← reportes semanales automáticos
├── 90-Memoria-Claude/  ← memoria persistente de Claude ⚠️ no editar
├── Diario/             ← notas diarias automáticas (8pm)
├── _prompts/           ← biblioteca de 16 prompts listos
├── _templates/         ← plantillas Obsidian
└── _setup/             ← snippets Raycast y configs
```

---

## 3. Automatizaciones activas

| Job | Horario | Qué hace | Dónde guarda |
|-----|---------|----------|--------------|
| **Daily report** | 20:00 diario | Consulta GHL → genera nota con leads, alertas, pendientes | `Diario/YYYY-MM-DD.md` |
| **Weekly report** | Lunes 8:00 | Consulta GHL 5 subcuentas → reporte semanal de leads y pipeline | `50-Reportes/YYYY/semana-NN.md` |
| **Competitor monitor** | Miércoles 9:00 | Navega sitios + Meta Ads Library de Mediarte, HERO, DHI | `20-Pauta/Competidores/YYYY/semana-NN.md` |
| **Vault backup** | 22:00 diario | `git commit + push` al repo privado de GitHub | GitHub |

Verificar que todos están corriendo:
```bash
launchctl list | grep innovart
```
Todos deben mostrar exit code `0`.

### Si un job falla

```bash
# Ver log del job específico
cat ~/Documents/Obsidian-Innovart/Diario/.logs/daily-report.log | tail -10
cat ~/Documents/Obsidian-Innovart/Diario/.logs/weekly-report.log | tail -10
cat ~/Documents/Obsidian-Innovart/Diario/.logs/competitor-monitor.log | tail -10

# Correr manualmente
bash ~/.claude/hooks/innovart-daily-report.sh
bash ~/.claude/hooks/innovart-weekly-report.sh
bash ~/.claude/hooks/innovart-competitor-monitor.sh
bash ~/.claude/hooks/innovart-vault-backup.sh
```

---

## 4. MCPs conectados

```bash
claude mcp list   # verificar status de todos
```

| MCP | Para qué sirve |
|-----|----------------|
| **GoHighLevel** | Consultar leads, oportunidades, pipelines, conversaciones de las 5 subcuentas |
| **Playwright** | Navegar sitios web, scraping de competidores, Meta Ads Library |
| **Chrome DevTools** | Debugging de páginas web, análisis de performance |
| **Google Drive** | Acceder a documentos del cliente en Drive |
| **Shopify** | Gestión del ecommerce / tienda Innovart |
| **Supabase** | Base de datos si se necesita |

### Subcuentas GHL disponibles

- Bogotá · Medellín · Barranquilla · Bucaramanga · Panamá

---

## 5. Biblioteca de prompts (`_prompts/`)

16 prompts listos para usar. Ver índice completo: [[_prompts/00-INDEX]]

| Categoría | Prompts |
|-----------|---------|
| **Pauta** | Reporte semanal, auditar landing, hooks para reel, benchmark campaña, brief creativo, ROAS proyectado |
| **CRM/Leads** | Analizar cohorte, script nurture WhatsApp, priorizar aging |
| **Contenido** | Calendario mensual, guión reel 30s, blog post SEO |
| **Reputación** | Responder reseña negativa, pedir reseña a paciente |
| **Operación** | Onboarding paciente nuevo, checklist post-cirugía |

**Cómo usar:** Abrí el prompt en Obsidian → copiá el texto → reemplazá las variables `<EN_MAYÚSCULA>` → pegalo en Claude.

---

## 6. Skills especializados

Los skills se activan automáticamente cuando Claude detecta el contexto correcto, o los podés invocar con `/nombre-del-skill`:

| Skill | Cuándo úsarlo |
|-------|---------------|
| `/medical-compliance-copy` | Antes de publicar cualquier copy médico — verifica que no viole regulaciones de salud |
| `/whatsapp-nurture-clinica` | Para generar secuencias de mensajes de seguimiento a leads de clínica |
| `/before-after-strategy` | Para planificar creativos de antes/después con cumplimiento de consentimiento |

---

## 7. Statusline de Claude Code

La barra de estado muestra en tiempo real:

```
✨ Innovart 📁 ~/Documents/Obsidian-Innovart | 🌿 main● | 🤖 sonnet-4-6 | ⏳ 3h 45m left | 🕐 09:15
```

| Segmento | Significa |
|----------|-----------|
| `✨ Innovart` | Estás en el proyecto Innovart |
| `📁 ruta` | Directorio actual |
| `🌿 main●` | Branch git + `●` si hay cambios sin commitear |
| `🤖 modelo` | Modelo Claude activo |
| `⏳ tiempo` | Tiempo restante del bloque de 5h de tokens |
| `🕐 hora` | Hora local |

---

## 8. Snippets de WhatsApp (Raycast)

12 mensajes comerciales pre-cargados. Archivo: `_setup/raycast-snippets.json`

Para importar: Raycast → buscar "Import Snippets" → seleccionar el archivo.

| Keyword | Mensaje |
|---------|---------|
| `!inv-hola` | Saludo inicial |
| `!inv-precio` | Precio FUE con garantía |
| `!inv-garantia` | Explicación garantía vitalicia |
| `!inv-precio-obj` | Respuesta a objeción de precio |
| `!inv-agendar` | Invitación a valoración |
| `!inv-sede-bog` | Dirección Bogotá |
| `!inv-fue-dhi` | Explicación FUE vs DHI |
| `!inv-recuperacion` | Timeline de recuperación |
| `!inv-follow24` | Seguimiento 24h |
| `!inv-recordatorio` | Recordatorio de cita |
| `!inv-resultados` | Mensaje resultados 6 meses |
| `!inv-brief` | Encabezado brief creativo |

---

## 9. Backup y restauración

**Backup automático:** Git + GitHub privado todos los días a las 22:00.

```bash
# Verificar último backup
cat ~/Documents/Obsidian-Innovart/Diario/.logs/backup.log | tail -3

# Backup manual
bash ~/.claude/hooks/innovart-vault-backup.sh
```

**Restaurar en Mac nuevo:**
```bash
brew install gh && gh auth login
gh repo clone JavierForeroAI/innovart-vault ~/Documents/Obsidian-Innovart
brew install node && npm install -g ccusage
brew install bash
```
Luego reinstalar Claude Code desde claude.ai/code y reconfigurar los hooks.

---

## 10. Competidores monitoreados

| Competidor | Precio | Diferenciador |
|------------|--------|---------------|
| **Mediarte** | $14M–$17.5M COP | 22+ sedes, Long FUE sin rasurar |
| **HERO Institute** | No publicado | Robótica ARTAS, 70% pacientes internacionales |
| **DHI Colombia** | No publicado | Especialización exclusiva en DHI |

**Ventaja de Innovart:** 2x más barato que Mediarte para el mismo procedimiento. No está siendo comunicado en pauta actualmente.

Perfiles completos: [[20-Pauta/Competidores/_perfiles]]
Monitor automático: [[20-Pauta/Competidores/_instrucciones-monitor]]

---

## 11. Contactos y accesos

| Sistema | Acceso |
|---------|--------|
| GHL (CRM) | 6 subcuentas — ver MCP gohighlevel |
| GitHub vault | `github.com/JavierForeroAI/innovart-vault` |
| Obsidian | `~/Documents/Obsidian-Innovart` |
| Claude Code | `innovart` (alias) o `cd ~/Documents/Obsidian-Innovart && claude` |

---

## 12. Checklist de verificación rápida (pre-reunión)

```bash
# 1. Todo funciona
launchctl list | grep innovart          # todos exit 0
claude mcp list                         # todos ✓ Connected

# 2. Último backup
cat ~/Documents/Obsidian-Innovart/Diario/.logs/backup.log | tail -2

# 3. Último reporte semanal
ls ~/Documents/Obsidian-Innovart/50-Reportes/2026/

# 4. Claude conectado al vault
innovart
```

---

*Manual generado: 2026-05-19 · Sistema instalado: 2026-05-18*
*Ver también: [[00-LEEME]] (guía del vault) · [[_prompts/00-INDEX]] (biblioteca de prompts)*
