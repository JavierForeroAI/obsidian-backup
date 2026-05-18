---
tipo: prompt-template
tema: crm
trigger: cohorte leads, análisis leads, calidad leads, pipeline análisis
---

# Analizar Cohorte de Leads

## Cuándo usar
Para entender dónde se están cayendo los leads en el pipeline y qué campaña trae mejor calidad.

## Variables que tenés que reemplazar
- `<CIUDAD>`: ej. "Bogotá", "Medellín", o "todas"
- `<PERIODO>`: ej. "mayo 2026", "últimas 4 semanas"
- `<FUENTE>`: ej. "Facebook Lead Forms", "todas las fuentes"

## Prompt
Analizá la cohorte de leads de Innovart Medical en <CIUDAD> durante <PERIODO>, provenientes de <FUENTE>.

Usando el CRM GHL disponible (mcp__gohighlevel), extraé y analizá:

**Volumen y velocidad**
- Leads totales del período
- Leads por día de la semana (¿cuándo llegan más?)
- Leads por hora del día (primeras 24h de cada lead)

**Etapas del pipeline**
- Distribución por etapa actual (Frío / Primer contacto / Tibio / Agenda / Asistió / No asistió / Ganado / Perdido)
- Tasa de avance entre etapas (ej. ¿qué % de "Primer contacto" llega a "Agenda"?)
- Tiempo promedio entre etapas

**Calidad**
- Leads con número de teléfono válido vs inválido
- Leads con conversación activa (respuesta en < 24h) vs sin respuesta
- Etiquetas más frecuentes (ej. "Consultar con esposa", "Precio alto", "MeddiPay")

**Señales de calidad**
- ¿Cuál es la etiqueta más asociada a leads que llegan a "Asistió"?
- ¿Qué ciudad tiene mayor tasa de valoraciones completadas?

Conclusión: top 3 cuellos de botella del funnel y recomendación de dónde actuar primero.

## Output esperado
Tabla de etapas con tasas de conversión + mapa de cuellos de botella + 3 recomendaciones.

## Ejemplo de uso real
"Analizá los leads de Bogotá en mayo de Facebook Lead Forms y decime dónde se cae el funnel"
