---
tipo: prompt-template
tema: pauta
trigger: auditar landing, revisar landing, landing page, CRO landing
---

# Auditoría de Landing Page

## Cuándo usar
Antes de lanzar una campaña o cuando el CPL sube sin causa clara en Meta/Google.

## Variables que tenés que reemplazar
- `<URL_LANDING>`: URL completa de la landing a auditar
- `<OBJETIVO>`: ej. "agendar valoración", "enviar WhatsApp", "llamar"
- `<AUDIENCIA>`: ej. "hombres 35-50, alopecia grado III, interés en estética"

## Prompt
Auditá la landing page de Innovart Medical en <URL_LANDING> para el objetivo de conversión: <OBJETIVO>.

Audiencia objetivo: <AUDIENCIA>

Evaluá los siguientes puntos con nota 1-5 y recomendación específica:

**Above the fold**
- Claridad del headline principal (¿se entiende qué es y para quién en 3 segundos?)
- Presencia y fuerza del CTA principal
- Carga de prueba social (testimonios, números, certificaciones)

**Propuesta de valor**
- ¿El diferenciador de precio ($6M-$8M vs $14M competencia) está comunicado?
- ¿Se mencionan los beneficios FUE/DHI vs alternativas?
- ¿La garantía vitalicia está visible?

**Confianza médica**
- ¿Aparece el Dr. Fabián Carreño con credenciales?
- ¿Hay registro sanitario / habilitación IPS visible?
- ¿Los antes/después tienen disclaimer de resultados individuales?

**Formulario / CTA**
- ¿Cuántos campos tiene el formulario? (ideal: máximo 3)
- ¿El CTA dice exactamente qué pasa después?
- ¿Hay opción de WhatsApp directo como alternativa?

**Compliance**
- ¿Hay algún claim prohibido? (garantizado, sin riesgos, 100% efectivo)
- ¿Los precios tienen aclaración de "desde" o "referencial"?

Generá un resumen ejecutivo con top 3 problemas críticos y top 3 quick wins.

## Output esperado
Tabla de auditoría con notas por categoría + lista de problemas críticos + quick wins priorizados.

## Ejemplo de uso real
"Auditá la landing de Bogotá para el objetivo de agendar valoración, audiencia hombres 35-50"
