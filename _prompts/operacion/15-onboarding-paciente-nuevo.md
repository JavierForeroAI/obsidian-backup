---
tipo: prompt-template
tema: operacion
trigger: onboarding paciente, bienvenida paciente, post-venta, confirmación cirugía
---

# Onboarding de Paciente Nuevo

## Cuándo usar
Cuando un paciente confirma y paga la cirugía. Secuencia de comunicación pre-operatoria.

## Variables que tenés que reemplazar
- `<NOMBRE>`: nombre del paciente
- `<FECHA_CIRUGIA>`: ej. "viernes 23 de mayo"
- `<HORA_CIRUGIA>`: ej. "8:00 AM"
- `<SEDE>`: ej. "Bogotá, Cl. 116 No. 9-72, Consultorio 405"
- `<TECNICA>`: ej. "FUE", "DHI"
- `<INJERTOS>`: ej. "2.500 injertos"
- `<MEDICO>`: ej. "Dr. Fabián Carreño"
- `<ASESOR>`: nombre del asesor

## Prompt
Generá la secuencia completa de onboarding para <NOMBRE>, paciente de Innovart Medical que tiene su cirugía el <FECHA_CIRUGIA>.

Datos del procedimiento:
- Fecha: <FECHA_CIRUGIA> a las <HORA_CIRUGIA>
- Sede: <SEDE>
- Técnica: <TECNICA>, <INJERTOS> injertos
- Médico: <MEDICO>
- Asesor de seguimiento: <ASESOR>

Generá estos mensajes/documentos:

**Mensaje 1 — Confirmación inmediata (mismo día del pago)**
WhatsApp celebrando la decisión + confirmando detalles + próximos pasos.

**Mensaje 2 — 7 días antes de la cirugía**
Recordatorio + instrucciones pre-op (ayuno, medicamentos a evitar, qué traer).

**Mensaje 3 — Día anterior a la cirugía**
Recordatorio final + logística (estacionamiento, tiempo estimado del procedimiento).

**Mensaje 4 — Día de la cirugía (antes de entrar)**
Ánimo + qué esperar durante el procedimiento.

**Documento: instrucciones pre-operatorias** (para enviar como PDF o en WhatsApp):
- Qué hacer 7 días antes
- Qué hacer 24 horas antes
- Qué llevar al procedimiento
- Qué evitar

Todos los mensajes: tuteo, cálido pero profesional.

## Output esperado
4 mensajes de WhatsApp + documento de instrucciones pre-op estructurado.

## Ejemplo de uso real
"Generá el onboarding para Carlos, cirugía FUE de 2500 injertos el viernes 23 de mayo a las 8am en Bogotá con el Dr. Carreño, lo atiende Karla"
