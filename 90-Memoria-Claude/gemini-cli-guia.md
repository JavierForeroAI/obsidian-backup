---
name: gemini-cli-guia
description: Guía de uso de Gemini CLI desde Claude Code — comandos, modelos disponibles y casos de uso para Innovart
metadata:
  type: reference
  updated: 2026-05-22
  version: 0.43.0
---

# Gemini CLI — Guía de Uso desde Claude Code

## Estado de la conexión

- **Versión instalada:** 0.43.0
- **Ruta:** `/opt/homebrew/bin/gemini`
- **Conexión verificada:** 2026-05-22 ✅

---

## Cómo llamar Gemini desde Claude Code

### Modo no-interactivo (headless) — el más útil aquí
```bash
! gemini -p "tu prompt aquí"
```

### Con modelo específico
```bash
! gemini -m gemini-2.5-pro -p "tu prompt aquí"
```

### Pasar contenido por stdin (analizar texto/archivos)
```bash
! cat archivo.txt | gemini -p "analiza este contenido"
```

### Modo interactivo (abre sesión completa)
```bash
! gemini
```

### Iniciar con prompt y continuar interactivo
```bash
! gemini -i "contexto inicial aquí"
```

### Retomar sesión previa
```bash
! gemini --resume latest          # sesión más reciente
! gemini --resume 5               # sesión por índice
! gemini --list-sessions          # ver sesiones disponibles
```

### Modo YOLO (acepta todo sin confirmación)
```bash
! gemini -y -p "tu prompt aquí"
```

### Salida en formato JSON
```bash
! gemini -p "tu prompt" -o json
```

---

## Modelos Disponibles

| Modelo | Familia | Velocidad | Mejor para |
|---|---|---|---|
| `gemini-3.1-pro-preview` | Gemini 3 | Lenta | Máximo razonamiento, thinking, multimodal |
| `gemini-3-pro-preview` | Gemini 3 | Lenta | Alto razonamiento, thinking, multimodal |
| `gemini-3-flash-preview` | Gemini 3 | Rápida | Alta velocidad, multimodal |
| `gemini-3.1-flash-lite-preview` | Gemini 3 | Muy rápida | Máxima velocidad, tareas simples |
| `gemini-2.5-pro` | Gemini 2.5 | Lenta | Tareas complejas, razonamiento confiable |
| `gemini-2.5-flash` | Gemini 2.5 | Media | Balance velocidad/rendimiento |
| `gemini-2.5-flash-lite` | Gemini 2.5 | Muy rápida | Tareas sencillas, el más estable |
| `gemma-4-31b-it` | Gemma 4 | Media | Thinking, arquitectura abierta local |

### Cambiar modelo
```bash
# Al inicio
! gemini -m gemini-2.5-pro -p "prompt"

# Variable de entorno (sesión actual)
export GEMINI_MODEL="gemini-2.5-pro"

# Permanente — editar ~/.gemini/settings.json
# propiedad: model.name
```

**Recomendación:** Usar `gemini-2.5-flash` para la mayoría de tareas (balance velocidad/calidad). Usar `gemini-2.5-pro` o `gemini-3-pro-preview` solo para análisis complejos.

---

## Subcomandos Disponibles

| Comando | Uso |
|---|---|
| `gemini mcp` | Gestionar servidores MCP conectados a Gemini |
| `gemini extensions` | Gestionar extensiones del CLI |
| `gemini skills` | Gestionar skills/agentes |
| `gemini hooks` | Gestionar hooks automáticos |
| `gemini gemma` | Gestionar modelo Gemma local |

---

## Modos de Aprobación

| Modo | Comportamiento |
|---|---|
| `default` | Pide confirmación para cada acción |
| `auto_edit` | Aprueba ediciones automáticamente |
| `yolo` | Aprueba todo sin confirmación (`-y`) |
| `plan` | Solo lectura, no ejecuta acciones |

```bash
! gemini --approval-mode auto_edit -p "prompt"
```

---

## Casos de Uso para Innovart Marketing

### Generar variaciones de copy para anuncios
```bash
! gemini -p "Genera 5 titulares para Google Ads de una clínica de implante capilar en Bogotá. Público: hombres 30-55 años con alopecia. Límite: 30 caracteres cada uno."
```

### Analizar métricas de campaña
```bash
! cat reporte-campana.csv | gemini -m gemini-2.5-pro -p "Analiza estas métricas de Google Ads e identifica los principales problemas y oportunidades de optimización"
```

### Generar ángulos creativos
```bash
! gemini -p "Genera 10 ángulos creativos para anuncios de Meta Ads de una clínica de implante capilar. Enfócate en testimoniales, transformación antes-después, y garantía vitalicia."
```

### Revisar copy vs. políticas
```bash
! gemini -p "¿Este copy cumple las políticas de Meta Ads para salud/estética? [pegar copy aquí]"
```

### Análisis de competencia
```bash
! gemini -m gemini-2.5-pro -p "Analiza las estrategias publicitarias típicas de clínicas de implante capilar en Latinoamérica y sugiere diferenciadores para Innovart Medical IPS"
```

### Generar ideas de segmentación
```bash
! gemini -p "Sugiere audiencias de segmentación detalladas en Meta Ads para una clínica de implante capilar en Colombia. Incluye intereses, comportamientos y datos demográficos."
```

---

## Usar Gemini + Claude en Paralelo

Una estrategia potente: usar ambos modelos para obtener perspectivas diferentes y validar.

```bash
# Gemini genera ideas
! gemini -p "Genera 10 ideas de campaña para Innovart"

# Claude evalúa y refina
# (en el mismo chat de Claude Code, pegar output de Gemini y pedir análisis)
```

---

## Configuración Permanente

Archivo de configuración: `~/.gemini/settings.json`

```json
{
  "model": {
    "name": "gemini-2.5-flash"
  }
}
```

---

## Notas Técnicas

- El CLI incluye herramientas integradas (GrepTool, filesystem) — similar a Claude Code
- Puede conectarse a servidores MCP igual que Claude Code (`gemini mcp`)
- Soporta worktrees de git (`-w`) para trabajo aislado
- Las sesiones se guardan y pueden retomarse con `--resume`
- Salida puede ser `text`, `json` o `stream-json`

**Ver también:**
- [[meta-mcp-guia]] — Herramientas MCP de Meta Ads
- [[google-ads-guia]] — Trabajo con Google Ads desde Claude
- [[google-politicas-publicitarias]] — Políticas Google Ads
- [[meta-politicas-publicitarias]] — Políticas Meta Ads
