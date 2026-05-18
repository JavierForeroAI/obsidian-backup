---
tipo: prompt-template
tema: pauta
trigger: reporte semanal, pauta semanal, resumen semana
---

# Reporte Semanal de Pauta

## Cuándo usar
Al inicio de la semana para revisar el rendimiento de la semana anterior.

## Variables que tenés que reemplazar
- `<SEMANA>`: ej. "12-18 de mayo 2026"
- `<CPL_TARGET>`: ej. "$25.000 COP"
- `<PRESUPUESTO_SEMANAL>`: ej. "$1.500.000 COP"

## Prompt
Analizá el rendimiento de la pauta de Innovart Medical para la semana <SEMANA>.

Datos disponibles:
- Canal: Meta Ads (Facebook + Instagram), Facebook Lead Forms
- CRM: GoHighLevel (subcuentas por ciudad: Bogotá, Medellín, Barranquilla, Panamá, Bucaramanga)
- CPL target: <CPL_TARGET>
- Presupuesto semanal total: <PRESUPUESTO_SEMANAL>

Usando las herramientas disponibles (GHL MCP para leads, drive para reportes previos):
1. Contá los leads nuevos de la semana por ciudad
2. Calculá CPL real si tenés datos de gasto
3. Identificá la ciudad con mejor y peor rendimiento
4. Listá los 3 top leads por engagement (etapa más avanzada en pipeline)
5. Generá 3 recomendaciones de acción concretas para la semana siguiente
6. Alertas 🚨 si CPL > <CPL_TARGET> x 1.5 o si alguna ciudad tiene 0 leads

Guardá el reporte en 50-Reportes/reporte-<SEMANA>.md usando el template [[_templates/Reporte-semanal]].

## Output esperado
Archivo markdown con tabla de métricas por ciudad, top leads, recomendaciones priorizadas y alertas.

## Ejemplo de uso real
"Generá el reporte de la semana del 12-18 de mayo con CPL target $25.000"
