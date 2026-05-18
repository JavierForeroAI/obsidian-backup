---
tipo: prompt-template
tema: operacion
trigger: post cirugía, post-op, cuidados post, seguimiento post operatorio
---

# Checklist y Seguimiento Post-Cirugía

## Cuándo usar
Inmediatamente después de la cirugía y en los 30 días siguientes para asegurar resultados y satisfacción.

## Variables que tenés que reemplazar
- `<NOMBRE>`: nombre del paciente
- `<FECHA_CIRUGIA>`: fecha en que se realizó
- `<TECNICA>`: FUE o DHI
- `<INJERTOS>`: cantidad de injertos realizados
- `<ASESOR>`: asesor de seguimiento
- `<MEDICO>`: médico que realizó el procedimiento

## Prompt
Generá el plan completo de seguimiento post-operatorio para <NOMBRE>, paciente de Innovart Medical.

Procedimiento: <TECNICA>, <INJERTOS> injertos, realizado el <FECHA_CIRUGIA> por <MEDICO>.
Asesor de seguimiento: <ASESOR>.

Generá:

**Secuencia de mensajes de seguimiento**

- Día 0 (post-cirugía, antes de salir): resumen del procedimiento + cuidados primeras 24h
- Día 1: chequeo de cómo pasó la primera noche
- Día 3: recordatorio de primer lavado
- Día 7: ¿cómo va la zona donante?
- Día 14: recordatorio de que el shock loss es NORMAL (caída de cabellos trasplantados)
- Día 30: primera foto de seguimiento + compartir en grupo si autorizó
- Día 90: foto de seguimiento + motivación (todavía en crecimiento)
- Día 180: foto de seguimiento + invitar a compartir testimonio
- Día 365: resultado final + pedido de reseña

**Checklist de cuidados para el paciente** (para enviar como PDF):
- Primeras 24 horas
- Días 1-7 (fase aguda)
- Días 7-30 (fase de reposo)
- Mes 2-6 (fase de crecimiento)
- Señales de alarma que requieren contactar al médico 🚨

**Criterios de alerta para el asesor**:
¿Cuándo escalar a médico? Lista de síntomas/situaciones que no son normales.

## Output esperado
Secuencia de 9 mensajes + checklist de cuidados + criterios de alerta para el equipo.

## Ejemplo de uso real
"Generá el seguimiento post-op para Carlos, FUE 2500 injertos el 23 de mayo, lo sigue Karla"
