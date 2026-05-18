---
tipo: prompt-template
tema: reputacion
trigger: reseña negativa, responder reseña, review negativo, google reviews
---

# Responder Reseña Negativa

## Cuándo usar
Cuando hay una reseña negativa en Google Maps, Facebook o cualquier plataforma de reputación.

## Variables que tenés que reemplazar
- `<RESENA>`: el texto completo de la reseña negativa
- `<PLATAFORMA>`: ej. "Google Maps", "Facebook", "Doctoralia"
- `<CIUDAD>`: ej. "Bogotá"
- `<NOMBRE_PACIENTE>`: si aparece en la reseña (o "el paciente" si es anónimo)

## Prompt
Redactá una respuesta profesional a esta reseña negativa en <PLATAFORMA> para Innovart Medical IPS, sede <CIUDAD>.

Reseña:
"""
<RESENA>
"""

Pautas para la respuesta:
- Tono: empático, profesional, nunca defensivo ni agresivo
- Extensión: máx 5 oraciones
- Estructura: 1) agradecer y reconocer, 2) expresar preocupación genuina, 3) invitar al canal privado, 4) reafirmar compromiso
- NO revelar información médica del paciente (aunque el paciente la mencione)
- NO prometer descuentos ni compensaciones en la respuesta pública
- Siempre cerrar con una invitación a contacto directo: WhatsApp o email

Si la reseña contiene información médica sensible o claims potencialmente difamatorios, indicame primero y recomendá si se debe reportar a la plataforma antes de responder.

Después de la respuesta pública, generá también un mensaje privado corto (WhatsApp) para enviarle al paciente si es identificable.

## Output esperado
Dos textos: (1) respuesta pública para copiar y pegar en la plataforma, (2) mensaje privado de WhatsApp opcional.

## Ejemplo de uso real
"Respondé esta reseña de Google Maps de un paciente en Medellín que dice que tardaron 2 horas más de lo prometido"
