---
tipo: prompt-template
tema: pauta
trigger: benchmark, comparar campaña, rendimiento vs industria, CPL industria
---

# Comparar Campaña vs Benchmark de Industria

## Cuándo usar
Cuando el cliente pregunta si el rendimiento es bueno o malo en términos absolutos, o al presentar resultados.

## Variables que tenés que reemplazar
- `<CANAL>`: ej. "Meta Ads", "Google Ads"
- `<CPL_ACTUAL>`: ej. "$28.000 COP"
- `<CTR_ACTUAL>`: ej. "1.8%"
- `<GASTO_PERIODO>`: ej. "$3.500.000 COP en mayo"
- `<LEADS_PERIODO>`: ej. "125 leads en mayo"

## Prompt
Comparame el rendimiento de la campaña de Innovart Medical en <CANAL> contra benchmarks de la industria de salud estética / medicina estética en Colombia y Latinoamérica.

Datos actuales del período:
- CPL: <CPL_ACTUAL>
- CTR: <CTR_ACTUAL>
- Gasto total: <GASTO_PERIODO>
- Leads generados: <LEADS_PERIODO>

Contexto de la clínica:
- Ticket promedio: $7.000.000 COP
- Producto: implante capilar FUE/DHI (alta consideración, decisión 2-8 semanas)
- Canal: Facebook Lead Forms → WhatsApp

Analizá:
1. ¿El CPL de <CPL_ACTUAL> es alto/medio/bajo para este tipo de producto?
2. ¿El CTR de <CTR_ACTUAL> es competitivo para salud estética en Meta?
3. ¿Cuál sería el CAC real si la tasa de cierre es del 5-10%?
4. ¿El ROAS implícito justifica el gasto dado el ticket de $7M?
5. ¿Qué palancas mover primero para mejorar el CPL?

Incluí benchmarks con fuentes (aunque sean estimados de industria) y marcá claramente qué es dato real vs estimado.

## Output esperado
Tabla comparativa CPL/CTR actual vs benchmark + cálculo de CAC + ROAS + 3 recomendaciones priorizadas.

## Ejemplo de uso real
"Comparame el rendimiento de mayo en Meta con CPL $28.000, CTR 1.8%, 125 leads con $3.5M de gasto"
