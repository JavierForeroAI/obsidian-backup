---
tipo: prompt-template
tema: crm
trigger: script WhatsApp, nurture, seguimiento, secuencia mensajes, follow up
---

# Script de WhatsApp Nurture Personalizado

## Cuándo usar
Para generar una secuencia de mensajes personalizada para un lead específico o segmento.

## Variables que tenés que reemplazar
- `<NOMBRE>`: nombre del lead
- `<CIUDAD>`: ciudad del lead
- `<ETAPA>`: etapa actual en GHL (ej. "Tibio — no respondió en 3 días")
- `<OBJECION>`: objeción o señal detectada (ej. "mencionó que tiene que consultar con su esposa")
- `<DIAS_SIN_RESPUESTA>`: ej. "3 días", "1 semana"
- `<ASESOR>`: nombre del asesor que enviará los mensajes

## Prompt
Generá una secuencia de 3 mensajes de WhatsApp para re-enganchar a <NOMBRE>, lead de Innovart Medical en <CIUDAD>.

Contexto del lead:
- Etapa actual: <ETAPA>
- Objeción / señal: <OBJECION>
- Días sin respuesta: <DIAS_SIN_RESPUESTA>
- Asesor: <ASESOR>

Reglas:
- Tuteo siempre
- Mensajes cortos: máx 3 oraciones cada uno
- Espaciados: Mensaje 1 hoy, Mensaje 2 en 2 días, Mensaje 3 en 5 días
- Nunca dos mensajes el mismo día
- Progresión: informativo → emocional → urgencia real (no falsa)
- NO prometer descuento antes del mensaje 3
- Si hay objeción de precio → mencionar MeddiPay a partir del mensaje 2
- Incluir sugerencia de medio (solo texto, o texto + media)

Para cada mensaje:
- Texto exacto listo para copiar
- Día de envío recomendado
- Media sugerida (si aplica): foto, video, link

## Output esperado
3 mensajes listos para copiar en WhatsApp Business, con timing y media opcional.

## Ejemplo de uso real
"Generá secuencia para Juan de Medellín, está en etapa Tibio hace 4 días, dijo que tiene que consultarlo con su esposa, lo atiende Karla"
