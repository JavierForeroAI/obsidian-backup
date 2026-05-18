---
tipo: prompt-template
tema: pauta
trigger: ROAS, proyección, calcular retorno, ROI pauta, proyectar ingresos
---

# Calcular ROAS Proyectado

## Cuándo usar
Al planificar presupuesto de pauta o al justificar inversión ante el cliente.

## Variables que tenés que reemplazar
- `<PRESUPUESTO_MES>`: ej. "$5.000.000 COP"
- `<CPL_ESPERADO>`: ej. "$25.000 COP"
- `<TASA_CIERRE>`: ej. "8%" (leads → cirugías)
- `<TICKET_PROMEDIO>`: ej. "$7.000.000 COP" (usar este si no tenés otro)

## Prompt
Calculá el ROAS proyectado para la pauta de Innovart Medical con estos parámetros:

- Presupuesto mensual: <PRESUPUESTO_MES>
- CPL esperado: <CPL_ESPERADO>
- Tasa de cierre lead → cirugía: <TASA_CIERRE>
- Ticket promedio cirugía: <TICKET_PROMEDIO>

Calculá:
1. Leads proyectados = presupuesto / CPL
2. Cirugías proyectadas = leads × tasa de cierre
3. Ingresos proyectados = cirugías × ticket promedio
4. ROAS = ingresos / presupuesto pauta
5. Punto de equilibrio: ¿a qué tasa de cierre el ROAS = 1?
6. Escenarios: pesimista (CPL +30%, cierre -30%), base, optimista (CPL -20%, cierre +20%)

Presentá en tabla clara con los 3 escenarios y la conclusión en 2 líneas: ¿conviene invertir a este CPL?

Nota: si el ROAS < 3, marcarlo como 🚨 y recomendar qué variable ajustar primero.

## Output esperado
Tabla de escenarios con ROAS, ingresos proyectados, y recomendación de go/no-go.

## Ejemplo de uso real
"Con $5M de presupuesto, CPL $25.000, cierre del 8% y ticket $7M, ¿cuánto retorno espero?"
