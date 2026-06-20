---
name: bitacora-2026-06-19-geo-innovart-ai
description: Hilo maestro / handoff de la conversación "GEO innovart AI". Punto único para retomar el trabajo de visibilidad en IA (GEO) de Innovart desde cualquier sesión nueva de Claude Code.
metadata:
  type: project
---

# 📓 Hilo maestro — "GEO innovart AI" (handoff)

Este archivo es el **punto de retoma** del trabajo de GEO/Visibilidad en IA de Innovart.
Cualquier sesión nueva de Claude Code: lee esto + invoca `/geo-salud-ia` y tienes todo.
Origen: sesión del 2026-06-19.

## Qué se hizo (todo VERIFICADO y funcionando)
1. **Diagnóstico GEO de Innovart** → [[geo-visibilidad-ia-diagnostico-2026-06-19]].
   AI Visibility Score **37/100** (no-branded 18, branded 62). Innovart invisible en
   respuestas generativas comerciales; competidores ganan por listicles+precio, no estructura.
2. **Skill `geo-salud-ia`** construida y registrada → [[skill-geo-salud-ia-autoaprendizaje]].
   Invocar con `/geo-salud-ia`. Vive en `~/.claude/skills/geo-salud-ia/`.
3. **Autoaprendizaje semanal** activo vía launchd `com.innovart.geo-weekly-learn`
   (lunes 9:15). Cargado y probado (headless `claude` responde).

## Dónde vive todo (paths e IDs)
- Skill: `~/.claude/skills/geo-salud-ia/` (SKILL.md · references/ · knowledge/ · scripts/).
- Inspector de huella: `~/.claude/skills/geo-salud-ia/scripts/geo-inspect.sh <dominio> [comp1] [comp2]`.
- Base viva de aprendizaje: `~/.claude/skills/geo-salud-ia/knowledge/learnings.md`.
- LaunchAgent: `~/Library/LaunchAgents/com.innovart.geo-weekly-learn.plist` · log `~/.claude/logs/geo-weekly-learn.log`.
- Informe HTML (12 entregables): Drive carpeta **GEO - Visibilidad IA**
  `1TeMVcOu4cdSsrt6BzjzAfo0iNiCYqTIA` (bajo 3.MERCADEO/CLAUDE); archivo
  `1V9gkkWpq081sibod6wIuOj0T94kBNWag`. Copia local: `~/Downloads/GEO-Innovart/`.
- Correo resumen enviado a innovartmedicalips@gmail.com.

## Pendientes (próximas acciones, en orden)
1. **Verificar datos `[VERIFICAR]`** del informe: nº pacientes (¿33.000?), sedes activas,
   teléfono/dirección por sede, reseñas (para AggregateRating), registros médicos.
2. **Quick wins on-page** (ver roadmap del informe):
   - Inyectar schema `MedicalClinic`/`MedicalOrganization` en home+sedes. ⚠️ PageFly/GemPages
     sobrescriben el `<head>` de Shopify → usar snippet de theme o app de JSON-LD y validar con
     Rich Results Test. Ver [[shopify-ecosistema-mcp]].
   - Crear **página de precio/transparencia** + `FAQPage` (donde hoy gana Rogans).
   - Unificar NAP/sedes + **eliminar "garantía vitalicia"** de Top Doctors y toda superficie
     ([[restricciones-lenguaje]]). Corregir `<title>` duplicados del widget.
   - Publicar `llms.txt` médico.
3. **Medium/strategic:** perfiles `Physician`, páginas de tratamiento (`MedicalProcedure`),
   comparativas FUE vs DHI, outreach a listicles, hub de autoridad con la Academia Capilar
   ([[academia-capilar-ecosistema]]).

## Cómo retomar en una sesión nueva
- El cerebro Obsidian se auto-carga → ya tendrás el índice GEO.
- Di "continuemos el GEO de Innovart" o invoca `/geo-salud-ia`.
- Para re-auditar tras cambios: `/geo-salud-ia` (vuelve a correr inspector + score).
- Para forzar un ciclo de aprendizaje: `bash ~/.claude/skills/geo-salud-ia/scripts/weekly-learn.sh`.

Relacionado: [[seo-puro-seo-cowork]] · [[shopify-ecosistema-mcp]] · [[academia-capilar-ecosistema]] · [[restricciones-lenguaje]]
