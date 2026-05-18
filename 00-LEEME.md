---
tipo: referencia
tema: onboarding
fecha: 2026-05-18
---

# Bienvenido al Vault Innovart

Este vault es el segundo cerebro del proyecto **Innovart Medical IPS** — clínica de implante capilar con 5 sedes (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá).

Acá vive todo: investigación del cliente, estrategia de pauta, análisis de CRM, contenido, reportes y la memoria persistente de Claude.

---

## Mapa de carpetas

| Carpeta | Propósito |
|---|---|
| `00-Inbox/` | Notas sin clasificar, borradores rápidos, capturas del hook auto-memory |
| `10-Clientes/` | Dossiers, gaps, briefs y documentos por cliente |
| `20-Pauta/` | Estrategia y ejecución de ads — Meta, Google, TikTok |
| `30-CRM-Leads/` | Análisis de funnel, pipeline GHL, comportamiento de leads |
| `40-Contenido/` | Calendarios editoriales, guiones, copys, captions |
| `50-Reportes/` | KPIs semanales, análisis de rendimiento, exportaciones |
| `90-Memoria-Claude/` | **Memoria persistente de Claude** — NO editar manualmente (ver regla abajo) |
| `Diario/` | Notas diarias del plugin Daily Notes |
| `_templates/` | Plantillas Obsidian para notas recurrentes |

---

## Regla importante: 90-Memoria-Claude/ es territorio de Claude

**No edites manualmente nada dentro de `90-Memoria-Claude/`.**

Esa carpeta la gestiona Claude Code automáticamente entre sesiones. Si editás a mano, la memoria puede quedar inconsistente. Si necesitás corregir algo, pedíselo a Claude directamente.

---

## Cómo abrir Claude conectado al vault

En Terminal:
```bash
cd ~/Documents/Obsidian-Innovart
claude
```

Claude carga automáticamente el contexto de Innovart al iniciar la sesión gracias al hook `innovart-session-context.sh`.

---

## Auto-memory activado — Frases que Claude detecta

Si escribís cualquiera de estas frases en un prompt dentro del vault, Claude guarda automáticamente la información como nota en Obsidian:

| Frase trigger | Ejemplo |
|---|---|
| `acordate que` / `acuérdate que` / `recordá` | "recordá que el ticket real es $7M COP" |
| `guardá esto` / `guarda esto` / `anotá` | "anotá: el Dr. Carreño prefiere reuniones los martes" |
| `para la próxima` / `para futuro` | "para la próxima, siempre separar frio de caliente" |
| `regla:` / `preferencia:` / `convención:` / `estilo:` | "regla: los copies de Meta siempre en tuteo" |
| `importante:` / `no olvides` / `memo:` | "importante: Mediarte cobra el doble que Innovart" |
| `aprendí que` / `aprendi que` / `learning:` / `insight:` | "insight: el show rate real es ~11% en sábados" |
| `decisión:` / `decidimos` / `quedamos en` | "decidimos usar FUE como técnica principal en los ads" |

Claude clasifica la nota según el tema (pauta, CRM, contenido, reportes, etc.) y confirma dónde la guardó.

---

## Convenciones del vault

1. **Frontmatter YAML obligatorio** en notas nuevas. Mínimo:
   ```yaml
   ---
   tipo: [nota|lead|creativo|reporte|referencia|gap]
   tema: descripción breve
   fecha: YYYY-MM-DD
   ---
   ```

2. **Wikilinks** en vez de rutas relativas: `[[nombre-de-nota]]` no `../ruta/archivo.md`.

3. **Tags** con `#` para clasificación transversal: `#meta-ads`, `#bogota`, `#funnel`, `#cierre`.

4. **Nombres de archivo** en kebab-case, sin tildes ni espacios.

---

## Documentos clave

- Dossier del cliente (investigación completa): [[10-Clientes/Innovart/_dossier-2026-05-18]]
- Preguntas pendientes para el cliente: [[10-Clientes/Innovart/_gaps-para-cliente]]
- Memoria de pauta y CRM: [[90-Memoria-Claude/stack-pauta]]
- Memoria del funnel: [[90-Memoria-Claude/crm-funnel]]
