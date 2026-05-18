---
tipo: prompt-template
tema: reputacion
trigger: pedir reseña, solicitar review, google review, reseña positiva
---

# Pedir Reseña a Paciente

## Cuándo usar
A los 30-60 días post-cirugía cuando el paciente ya tiene resultados visibles y ha mostrado satisfacción.

## Variables que tenés que reemplazar
- `<NOMBRE>`: nombre del paciente
- `<ASESOR>`: nombre del asesor que lo atendió
- `<CIUDAD>`: ciudad de la sede
- `<DIAS_POST_OP>`: ej. "30 días", "45 días"
- `<PLATAFORMA>`: ej. "Google Maps", "Facebook" (donde más necesite reseñas)

## Prompt
Generá un mensaje de WhatsApp para pedirle a <NOMBRE> una reseña en <PLATAFORMA>, <DIAS_POST_OP> después de su cirugía en Innovart Medical <CIUDAD>.

Lo atiende <ASESOR>.

El mensaje debe:
- Arrancar preguntando por su evolución (no ir directo al pedido)
- Celebrar genuinamente el progreso
- Pedir la reseña de forma natural, sin presión
- Dar el link directo a la plataforma de reseña
- Dar instrucciones simples (2-3 pasos) de cómo dejar la reseña en <PLATAFORMA>
- Agradecer de antemano
- Máx 5 oraciones (puede ser en 2 mensajes separados)

Reglas:
- Nunca insinuar qué calificación poner (eso viola las políticas de Google/Meta)
- No ofrecer descuento o regalo a cambio de la reseña (práctica prohibida)
- Si el paciente no quiere dejar reseña: respuesta de seguimiento empática y sin presión

También generá un mensaje de seguimiento para 7 días después si no respondió.

## Output esperado
Mensaje 1 (día 0), Mensaje 2 (día 7 si no respondió), instrucciones del link.

## Ejemplo de uso real
"Pedile reseña a Carlos en Google Maps, 45 días post-op, sede Bogotá, lo atiende Ingrid"
