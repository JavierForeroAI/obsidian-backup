---
name: skill-geo-salud-ia-autoaprendizaje
description: Skill geo-salud-ia (Estratega de Visibilidad en IA para salud / GEO) instalada en Claude Code, con autoaprendizaje semanal vía launchd (lunes 9:15) que busca novedades GEO y mejora su propio conocimiento.
metadata:
  type: reference
---

# Skill `geo-salud-ia` + autoaprendizaje semanal (2026-06-19)

Skill propia construida en Claude Code para auditar **visibilidad en IA (GEO/LLM SEO/
Entity SEO)** de clínicas/médicos. Produce AI Visibility Score (0-100) + 8 subscores,
hallazgos con evidencia, roadmap 30/90/180 y activos GEO (schema JSON-LD, FAQ GEO, etc.).
Primer uso real: [[geo-visibilidad-ia-diagnostico-2026-06-19]].

## Dónde vive
`~/.claude/skills/geo-salud-ia/`
- `SKILL.md` — persona + flujo (lee learnings → recoge evidencia → 6 ejes → score → 12 entregables).
- `references/` — `framework-geo.md`, `scoring-rubric.md` (pesos), `schema-templates.md`
  (JSON-LD listo: MedicalClinic/Physician/MedicalProcedure/FAQPage/MedicalWebPage),
  `geo-query-bank.md` (consultas para medir citabilidad), `compliance-co.md` (términos prohibidos).
- `knowledge/` — `learnings.md` (base viva, se auto-actualiza), `sources.md` (qué vigilar).
- `scripts/` — `geo-inspect.sh` (inspector de huella: schema/robots/llms/sitemap/meta + comparativa
  vs competidores, solo curl) · `weekly-learn.sh` + `weekly-learn-prompt.md` (motor de autoaprendizaje).

## Cómo invocarla
`/geo-salud-ia` o "auditoría GEO de [marca]" / "por qué no me recomienda la IA".

## Autoaprendizaje semanal (se mejora sola)
- **launchd** (NO cron: macOS bloquea crontab por TCC). Agente
  `com.innovart.geo-weekly-learn` → `~/Library/LaunchAgents/com.innovart.geo-weekly-learn.plist`.
- Corre **lunes 9:15** (y al despertar el equipo si estaba dormido). Log: `~/.claude/logs/geo-weekly-learn.log`.
- `weekly-learn.sh` lanza `claude -p` headless (modelo sonnet, `--dangerously-skip-permissions`,
  `--add-dir` acotado a la skill) que hace WebSearch sobre cambios GEO/IA + competidores y
  **agrega entradas con fecha a `knowledge/learnings.md`** (lo más nuevo arriba). Cada auditoría
  lee ese archivo antes de calificar → la skill no se queda congelada.
- Forzar ciclo ahora: `bash ~/.claude/skills/geo-salud-ia/scripts/weekly-learn.sh`.
- Gestionar: `launchctl list | grep geo-weekly` · `launchctl bootout gui/$(id -u) <plist>` para quitar.
