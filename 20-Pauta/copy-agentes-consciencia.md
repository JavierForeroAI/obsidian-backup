---
title: Copy Completo — Sistema de 7 Agentes por Nivel de Consciencia
categoria: pauta
tipo: copy-bots
fecha: 2026-06-12
tags: [whatsapp, ghl, bots, copy, consciencia, implante-capilar]
---

# Copy Completo — Sistema de Agentes por Nivel de Consciencia
## Clínica de Restauración Capilar | GHL-Ready

> Documento listo para implementar en GoHighLevel. Cada mensaje incluye timing, rama A (responde), rama B (no responde) y copy de reactivación.

---

## AGENTE 0 — CUALIFICADOR INICIAL

### Función
Recibe a todos los leads entrantes, los clasifica por nivel de consciencia y perfil de avatar, y los enruta al agente correcto.

---

### HOOKS DE BIENVENIDA POR CANAL

#### WhatsApp — Lead de Meta Ads Click-to-Chat
```
Hola 👋 Gracias por escribirnos.

Vi que llegaste desde uno de nuestros anuncios — así que imagino que algo te llamó la atención 😊

¿Me cuentas brevemente qué está pasando con tu cabello y qué te gustaría lograr?
```

#### Instagram DM — Lead Orgánico
```
Hola, qué bueno que escribiste 🙌

Veo que llegaste por Instagram — cuéntame, ¿qué te llevó a buscar información sobre restauración capilar?

(Sin compromiso, solo quiero entender bien tu situación para orientarte bien)
```

#### Facebook DM — Lead de Anuncio
```
Hola 👋 Recibí tu mensaje.

Vi que te interesó lo que compartimos sobre restauración capilar en Facebook.

Cuéntame: ¿llevas mucho tiempo con este tema o apenas estás empezando a buscar opciones?
```

#### Lead de Formulario — Sin contacto previo
```
Hola, acabo de ver que dejaste tus datos en nuestro formulario 🙌

Antes de enviarte información general, prefiero entender bien tu caso para darte lo que realmente te sirve.

¿Tienes 2 minutos para contarme cómo está tu cabello hoy y qué te gustaría mejorar?
```

---

### PREGUNTAS DE CUALIFICACIÓN (3 preguntas naturales)

**Pregunta 1 — Tiempo con el problema:**
```
Cuéntame... ¿cuánto tiempo llevas notando la caída o pérdida de cabello? ¿Es algo reciente o ya lleva años?
```
*(Clasifica: urgencia, nivel de dolor, proximidad a la decisión)*

**Pregunta 2 — Impacto emocional:**
```
Y eso que estás viviendo... ¿cómo te ha afectado en el día a día? ¿Lo piensas mucho, te afecta la confianza, tu imagen en el trabajo...?
```
*(Clasifica: avatar A/B/C, profundidad del dolor, motivación real)*

**Pregunta 3 — Grado de investigación:**
```
¿Ya has buscado opciones antes, viste algo sobre implantes o tratamientos, o apenas estás empezando a explorar el tema?
```
*(Clasifica: nivel de consciencia 0–4)*

---

### ÁRBOL DE ENRUTAMIENTO

| Respuesta | Nivel asignado | Agente |
|---|---|---|
| "Apenas me di cuenta" / "no sé mucho" | Nivel 0–1 | Agente 1 |
| "He buscado opciones" / "vi tratamientos" | Nivel 2 | Agente 2 |
| "Los conozco a ustedes" / "comparando clínicas" | Nivel 3 | Agente 3 |
| "Casi listo" / "quiero agendar" | Nivel 4 | Agente 4 |
| "Ya agendé" / confirmación | Nivel 5 | Agente 5 |
| No-show post-cita | Nivel 6 | Agente 6 |
| Fue a consulta, no cerró | Nivel 7 | Agente 7 |

---

---

## AGENTE 1 — NIVEL 0–1: INCONSCIENTE / PROBLEMA CONSCIENTE

### Perfil del lead
Llegó por un anuncio o interés vago. Sabe que pierde cabello pero no lo ha convertido en una búsqueda activa de solución. Necesita que alguien nombre su dolor antes de hablarle de soluciones.

### Tono
Empatía absoluta. Cero venta. Solo conexión con el dolor real.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — INMEDIATO (0–5 min después de clasificación)**
```
Entiendo 🙏

Hay algo que muy pocos dicen en voz alta sobre la pérdida de cabello:

No es solo cabello. Es la imagen que ves en el espejo. Es cómo te sientes cuando entras a una reunión, a una cita, a una foto.

¿Eso resuena contigo?
```
- **Respuesta esperada:** Confirmación emocional ("sí", "exacto", "eso me pasa")
- **Rama A (responde):** Profundizar en el impacto personal → Mensaje 2
- **Rama B (no responde):** Esperar 2 horas → Follow-up 1B

---

**MENSAJE 1B — FOLLOW-UP SI NO RESPONDE (+2h)**
```
Oye, no quiero ser pesado 😊

Solo quería preguntarte algo sencillo:

¿Hay algún momento del día en que la pérdida de cabello te molesta más? (Una reunión, una foto, un espejo...)
```
- **Respuesta esperada:** Apertura a conversar sobre el dolor
- **Rama A:** Continuar con Mensaje 2
- **Rama B:** Esperar 24h → Follow-up 2B

---

**MENSAJE 2 — CUANDO RESPONDE O +24h SI NO RESPONDIÓ**
```
Hay algo que me comentan muchos hombres cuando llegan aquí:

"Me acostumbré a no mirarme mucho en el espejo."
"Dejé de salir en fotos."
"Cambié cómo me pongo el cabello para disimular."

¿Alguno de esos te suena familiar? 🤔
```
- **Respuesta esperada:** Identificación con alguna de las situaciones
- **Rama A:** Ir a Mensaje 3 — validar y profundizar
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B — FOLLOW-UP (+24h sin respuesta)**
```
Solo una pregunta rápida y ya te dejo tranquilo:

Si pudieras recuperar tu cabello como lo tenías hace 5 o 10 años... ¿qué cambiaría en tu vida?

(No me refiero al cabello. Me refiero a lo que viene después de tenerlo.)
```
- **Rama A:** Continuar secuencia
- **Rama B:** +3 días → Mensaje de Reactivación

---

**MENSAJE 3 — VALIDACIÓN DEL DOLOR**
```
Lo que describes es más común de lo que crees.

Y lo que más me llama la atención cuando alguien llega aquí no es el cabello en sí...

Es cuánto espacio ocupa eso en la cabeza todos los días. ¿Tú cuánto tiempo llevas con esto?
```
- **Respuesta esperada:** Revelar la duración del problema (crea urgencia implícita)
- **Rama A:** Ir a Mensaje 4
- **Rama B:** +24h → Follow-up 3B

---

**MENSAJE 3B — FOLLOW-UP (+24h)**
```
Sabes qué es lo curioso...

La mayoría de hombres que hablan conmigo esperaron años antes de buscar algo. Años cargando con eso.

Y cuando finalmente lo resuelven, lo primero que dicen es: "¿Por qué esperé tanto?"

Solo curiosidad — ¿cuánto tiempo llevas tú con este tema?
```

---

**MENSAJE 4 — TRANSICIÓN SUAVE A LA POSIBILIDAD**
```
Mira, no te voy a hablar de procedimientos ni de precios todavía.

Pero sí quiero que sepas algo: lo que describes tiene solución. Real, permanente, natural.

¿Te interesaría que te cuente cómo funciona, sin compromiso?
```
- **Respuesta esperada:** "Sí" o curiosidad
- **Rama A:** Transición al Agente 2
- **Rama B:** +48h → Follow-up 4B

---

**MENSAJE 4B — FOLLOW-UP (+48h)**
```
Ey, solo para que quede claro:

Aquí no hay presión ni apuro 🙌

Pero si en algún momento quieres entender bien qué opciones existen hoy para la pérdida de cabello... estoy aquí.

¿Hay algo puntual que te esté frenando para explorar esto?
```

---

**MENSAJE 5 — CIERRE DE NIVEL / ÚLTIMO INTENTO ANTES DE REACTIVACIÓN**
```
Última pregunta, te lo prometo 😊

Si supieras que hay una forma de recuperar tu imagen sin que se note que "hiciste algo"...

¿Lo considerarías?
```
- **Rama A:** Activar Mensaje de Transición
- **Rama B:** Archivar → Reactivación en 7 días

---

### B. RESPUESTAS A OBJECIONES — NIVEL 0–1

**Objeción 1: "¿Cuánto cuesta?"**
```
Eso depende mucho de cada caso — no es una cifra fija.

Lo que sí te puedo decir es que hay opciones que se adaptan a distintas situaciones.

Pero antes de hablar de números, ¿me dejas entender bien qué está pasando con tu cabello? Así te doy información que realmente te sirve 🙏
```

**Objeción 2: "Tengo miedo de que se vea falso"**
```
Ese miedo es el más común. Y es el más válido.

Te entiendo — nadie quiere verse con cabello de muñeco.

Por eso lo primero que te mostraría son resultados reales de personas normales, no fotos de catálogo. ¿Quieres ver algunos casos?
```

**Objeción 3: "No tengo tiempo ahorita"**
```
Sin problema, no hay apuro aquí 🙌

Solo una cosa: cuando tengas un momento, me avisas.

Y si quieres, te mando algo corto que puedas leer cuando tengas 3 minutos. ¿Te parece?
```

**Objeción 4: "Lo voy a pensar"**
```
Claro, es una decisión importante y tiene todo el sentido pensarla.

¿Hay algo específico sobre lo que tengas dudas? A veces ayuda tener la información correcta antes de pensar.

(Así el "pensar" parte de datos reales, no de suposiciones 😊)
```

**Objeción 5: "Vi otros lugares más baratos"**
```
Normal que estés explorando opciones — es lo que haría cualquier persona inteligente.

Lo que te puedo decir es que en algo que va en tu cara y tu imagen... el precio más bajo rara vez es la mejor decisión.

¿Quieres que te explique por qué hay tanta diferencia entre una clínica y otra? No para convencerte, sino para que compares bien.
```

---

### C. MENSAJE DE TRANSICIÓN AL NIVEL 2
```
Mira, creo que vale la pena que te cuente un poco más sobre qué existe hoy en día.

No para que decidas nada ahorita — sino para que tengas la información completa.

Te mando algo breve. ¿Te parece? 📲
```

---

### D. MENSAJE DE REACTIVACIÓN (lead frío en este nivel)
**Timing: 7 días sin respuesta**
```
Hola de nuevo 👋

Solo pasaba a saludar — no te escribo para venderte nada.

¿Sabes qué es lo que más me acuerdo de nuestra conversación? Que dijiste [insertar algo que mencionó].

¿Cómo estás con ese tema hoy?
```

**Timing: 15 días sin respuesta**
```
[Nombre], el mes pasado hablamos brevemente.

Hoy tuve una consulta con alguien que tenía exactamente lo que tú describías — y salió muy contento.

No para presionarte. Solo pensé en ti. ¿Sigues pensándolo?
```

---

---

## AGENTE 2 — NIVEL 2: SOLUCIÓN CONSCIENTE

### Perfil del lead
Ya sabe que pierde cabello y está buscando activamente qué opciones existen. Ha googeleado, vio videos, tal vez probó minoxidil. Necesita educación de calidad, no un vendedor. Quiere entender sus opciones sin sentirse presionado.

### Tono
Educativo. Autoridad sin arrogancia. Comparación honesta.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — INMEDIATO**
```
Perfecto, ya tienes algo de contexto sobre el tema 👌

Entonces te puedo hablar directo: hoy existen básicamente 3 caminos para la pérdida de cabello.

Uno es temporal (productos). Otro es parcial (medicamentos). Y el tercero es permanente.

¿Quieres que te explique brevemente cómo funciona cada uno?
```
- **Respuesta esperada:** "Sí" / curiosidad sobre el tercero
- **Rama A:** Ir a Mensaje 2
- **Rama B:** +2h → Follow-up 1B

---

**MENSAJE 1B — FOLLOW-UP (+2h)**
```
Oye, te preguntaba porque la mayoría de personas que investigan este tema terminan confundidas con tanta información.

¿Qué has encontrado hasta ahora en tu búsqueda? ¿Algo que te haya convencido o algo que te haya dado desconfianza?
```

---

**MENSAJE 2 — EDUCACIÓN DE LA SOLUCIÓN PERMANENTE**
```
El implante capilar (o trasplante) es la única solución permanente que existe hoy.

No es un injerto de catálogo — se usan tus propios folículos, de zonas donde no caen.

El resultado: cabello real, tuyo, que crece de forma natural para siempre. ¿Eso era lo que imaginabas o tenías otra idea?
```
- **Rama A:** Continuar educando o resolver duda específica
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B — FOLLOW-UP (+24h)**
```
Antes de seguir, una cosa importante:

Hay una diferencia enorme entre una clínica y otra en este procedimiento. No todas usan la misma tecnología ni tienen los mismos resultados.

¿Sabes qué preguntas hacerle a una clínica antes de confiar en ella?
```

---

**MENSAJE 3 — DIFERENCIACIÓN + AUTORIDAD**
```
Lo que diferencia un resultado natural de uno que "se nota" son tres cosas:

1️⃣ El diseño del nacimiento del cabello
2️⃣ La dirección y el ángulo de cada folículo
3️⃣ La experiencia del médico que lo hace

¿Quieres ver cómo se ven resultados bien hechos vs. mal hechos? (La diferencia es brutal.)
```
- **Rama A:** Enviar casos antes/después → Ir a Mensaje 4
- **Rama B:** +24h → Follow-up 3B

---

**MENSAJE 3B — FOLLOW-UP (+24h)**
```
Solo quería saber: ¿qué dudas tienes sobre el procedimiento en sí?

Muchas personas tienen preguntas sobre el dolor, el tiempo de recuperación, o si se nota que "hicieron algo".

¿Cuál es la tuya?
```

---

**MENSAJE 4 — CASOS DE RESULTADO + PRUEBA SOCIAL**
```
Mira este caso [link o imagen]:

Hombre de [edad similar al lead], zona de entradas y coronilla. Resultado a los 12 meses.

Lo que más valora: nadie le preguntó si se hizo algo. Solo noto que se "veía mejor".

¿Quieres que te cuente cómo fue el proceso de ese caso?
```
- **Rama A:** Continuar → Mensaje 5
- **Rama B:** +48h → Follow-up 4B

---

**MENSAJE 4B — FOLLOW-UP (+48h)**
```
Oye, una pregunta directa:

¿Hay algo que te esté frenando para explorar esto más a fondo? ¿Precio, tiempo, miedo, algo más?

Dímelo sin pena — lo que sea, lo resolvemos o lo aclaramos 🙏
```

---

**MENSAJE 5 — INVITACIÓN A LA VALORACIÓN**
```
Mira, con todo lo que has investigado ya tienes más contexto que el 90% de personas que nos escriben.

El siguiente paso natural sería una valoración gratuita con nuestro especialista.

En 30 minutos, él te dice exactamente: qué nivel de pérdida tienes, si eres candidato, y cómo quedarías. Sin compromiso. ¿Te interesa?
```
- **Rama A:** Transición al Agente 3/4
- **Rama B:** Reactivación en 3 días

---

### B. RESPUESTAS A OBJECIONES — NIVEL 2

**Objeción 1: "¿Cuánto cuesta?"**
```
Buena pregunta — y tiene mucho sentido hacerla en este punto.

El costo varía según el número de folículos que necesites, que se define en la valoración.

Lo que sí te puedo decir es que el rango general está entre [X] y [Y] USD. ¿Eso está dentro de lo que imaginabas?
```

**Objeción 2: "Tengo miedo de que se vea falso"**
```
Eso era real hace 15 años con las técnicas antiguas.

Hoy, con la técnica que usamos (FUE sin cicatriz), el resultado es indistinguible del cabello natural.

¿Quieres que te muestre fotos de resultados nuestros para que lo veas tú mismo?
```

**Objeción 3: "No tengo tiempo ahorita"**
```
Sin problema 🙌

La valoración dura 30 minutos y la hacemos en el horario que mejor te quede — incluyendo fines de semana.

¿Cuándo sería el momento menos complicado para ti?
```

**Objeción 4: "Lo voy a pensar"**
```
Claro, es una decisión que merece pensarse bien.

¿Hay algo específico que necesitas claridad antes de decidir? A veces la duda es sobre el resultado, otras veces sobre el costo, otras sobre el tiempo.

¿Cuál es la tuya?
```

**Objeción 5: "Vi otros lugares más baratos"**
```
Te entiendo y es importante comparar.

Lo que me gustaría que consideraras: en un procedimiento que va en tu imagen para siempre, ¿qué pesa más, el precio inicial o el resultado a largo plazo?

¿Quieres que te explique qué diferencia una clínica de precio bajo de una de resultado garantizado?
```

---

### C. MENSAJE DE TRANSICIÓN AL NIVEL 3
```
Creo que ya tienes suficiente información para dar el siguiente paso.

Lo que haría en tu lugar es una valoración gratuita — no te compromete a nada, y sales con claridad total sobre tu caso.

¿Quieres que te cuente cómo funciona?
```

---

### D. MENSAJE DE REACTIVACIÓN
**Timing: 5 días**
```
Hola [nombre] 👋

La semana pasada hablamos sobre opciones para tu cabello.

Encontré algo que creo que te puede interesar: [dato nuevo / caso similar / artículo breve].

¿Sigues investigando el tema?
```

**Timing: 12 días**
```
Solo paso a saludarte.

¿Algo cambió con el tema del cabello o sigues en el mismo punto?

(Sin presión — solo quiero saber si puedo ayudarte en algo)
```

---

---

## AGENTE 3 — NIVEL 3: PRODUCTO CONSCIENTE

### Perfil del lead
Conoce la clínica. Está comparando activamente. Ha visto otras opciones, quizás tiene cotizaciones. Necesita diferenciación clara, prueba social sólida y razones para elegir esta clínica sobre las demás.

### Tono
Serio. Datos. Diferenciación honesta. Confianza, no presión.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — INMEDIATO**
```
Me alegra que nos hayas encontrado 🙌

Ya que estás comparando opciones, quiero ser directo contigo:

Hay preguntas clave que deberías hacerle a cualquier clínica antes de decidir. ¿Quieres que te las comparta?
```
- **Respuesta esperada:** "Sí" — posicionamiento como asesor, no como vendedor
- **Rama A:** Ir a Mensaje 2
- **Rama B:** +2h → Follow-up 1B

---

**MENSAJE 1B (+2h)**
```
Oye, ya que estás en el proceso de comparar:

¿Qué es lo más importante para ti al elegir una clínica? ¿El precio, la naturalidad del resultado, la experiencia del médico, algo más?

Eso me ayuda a darte información que realmente te sirva 🙏
```

---

**MENSAJE 2 — LAS PREGUNTAS CLAVE**
```
Estas son las 4 preguntas que deberías hacerle a cualquier clínica:

1️⃣ ¿El médico que opera tiene certificación específica en restauración capilar?
2️⃣ ¿Muestran fotos de SUS pacientes reales, no de catálogos?
3️⃣ ¿Qué pasa si el resultado no es el esperado?
4️⃣ ¿El diseño del nacimiento lo hace el médico o un técnico?

¿Quieres saber cómo respondemos nosotros a cada una? 😊
```
- **Rama A:** Continuar con diferenciación
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B (+24h)**
```
Una cosa que me gustaría mostrarte:

Tenemos una galería de casos reales — antes y después de pacientes nuestros, con sus nombres y su historia.

¿Te la comparto? Es la mejor forma de evaluar el nivel de nuestro trabajo.
```

---

**MENSAJE 3 — DIFERENCIACIÓN CLÍNICA**
```
Lo que nos diferencia no es solo el procedimiento. Es esto:

✔ Médico especialista, no técnico
✔ Diseño del nacimiento personalizado por tu estructura facial
✔ Respaldamos tu resultado — si algo no está bien, lo corregimos
✔ Tecnología FUE sin cicatriz visible

¿Alguna de esas cosas ya la habías comparado con otras clínicas?
```
- **Rama A:** Responder a comparación específica
- **Rama B:** +24h → Follow-up 3B

---

**MENSAJE 3B (+24h)**
```
Mira, sé que estás comparando y eso es lo correcto.

Solo quiero que lo hagas con información real.

¿Me dices qué otras opciones estás evaluando? No para hablar mal de nadie — sino para ayudarte a comparar con criterios que importan.
```

---

**MENSAJE 4 — PRUEBA SOCIAL FUERTE**
```
Déjame contarte algo que pasó hace 3 semanas:

Un ejecutivo de [ciudad] llegó a nosotros después de cotizar en 4 clínicas.

La nuestra no era la más barata. La eligió porque fue el único médico que le explicó el diseño antes de hablar de precio.

Hoy tiene 8 meses de resultado y dice que fue la mejor inversión de su carrera. ¿Quieres ver su caso?
```
- **Rama A:** Ir a Mensaje 5
- **Rama B:** +48h → Follow-up 4B

---

**MENSAJE 4B (+48h)**
```
Entiendo que la decisión no es sencilla.

¿Qué es lo que más te genera duda en este momento — el resultado, el proceso, el costo, o algo sobre la clínica en sí?

Dímelo y lo atacamos directo 🎯
```

---

**MENSAJE 5 — CIERRE HACIA VALORACIÓN**
```
Mira, la forma más honesta de compararnos con cualquier otra clínica es esta:

Ven a una valoración gratuita. Nuestro especialista te hace la evaluación, diseña tu caso en pantalla, y te explica todo.

Si después decides ir a otra clínica — sin problema. Pero al menos decides con toda la información sobre la mesa.

¿Cuándo tienes 30 minutos disponibles esta semana?
```
- **Rama A:** Agendar → Agente 5
- **Rama B:** Reactivación

---

### B. RESPUESTAS A OBJECIONES — NIVEL 3

**Objeción 1: "¿Cuánto cuesta?"**
```
El precio exacto lo definimos en la valoración, porque depende del número de folículos de tu caso específico.

Lo que sí te puedo decir es nuestro rango: entre [X] y [Y] USD.

Y una cosa importante: tenemos opciones de financiamiento disponibles. ¿Eso cambia algo en tu evaluación?
```

**Objeción 2: "Miedo a que se vea falso"**
```
Ese miedo es exactamente por lo que existe nuestra garantía de resultado.

El médico te muestra el diseño antes de operar. Ves cómo va a quedar antes de que empiece.

Y si a los 12 meses algo no está bien — se corrige. ¿Eso te da más tranquilidad?
```

**Objeción 3: "No tengo tiempo"**
```
La valoración la hacemos en 30 minutos y en el horario que tú elijas.

¿Un sábado por la mañana te funciona, o prefieres entre semana?
```

**Objeción 4: "Lo voy a pensar"**
```
Tiene todo el sentido.

Una sugerencia: haz la valoración gratuita antes de decidir. Así piensas con datos reales en la mano, no con suposiciones.

¿Qué te parece eso? 🙏
```

**Objeción 5: "Hay lugares más baratos"**
```
Sí, los hay — y es válido considerarlos.

Solo te pido que hagas una cosa: pregúntales esas 4 preguntas que te compartí antes.

Si las responden bien, adelante. Si no... ya sabrás por qué nosotros costamos lo que costamos.
```

---

### C. MENSAJE DE TRANSICIÓN AL NIVEL 4
```
Perfecto. Creo que lo mejor que podemos hacer ahora es ponernos cara a cara.

Te propongo una valoración gratuita esta semana — sin compromiso, solo para que tengas toda la información.

¿El miércoles o el jueves te funcionan?
```

---

### D. MENSAJE DE REACTIVACIÓN
**5 días:**
```
Hola [nombre], la semana pasada hablamos mientras comparabas opciones.

¿Tomaste ya alguna decisión o sigues evaluando?

Sin presión — si quieres más información o tienes preguntas, aquí estoy 🙏
```

**10 días:**
```
[Nombre], solo quería compartirte esto:

Acaba de terminar el tratamiento de un paciente con un perfil muy similar al tuyo — y el resultado fue increíble.

¿Te lo muestro?
```

---

---

## AGENTE 4 — NIVEL 4: MÁS CONSCIENTE / LISTO PARA DECIDIR

### Perfil del lead
Ya tomó la decisión internamente. Solo necesita el último empujón: certeza, urgencia real, y que el proceso sea fácil. No necesita más educación — necesita que se lo pongan fácil.

### Tono
Directo. Facilitador. Urgencia suave y real. Cero presión artificial.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — INMEDIATO**
```
Oye, por lo que me comentas ya tienes bastante claro que quieres hacer algo con esto.

El siguiente paso es simple: una valoración gratuita donde el médico te evalúa y te dice exactamente qué, cuánto y cómo.

¿Qué días tienes disponibles esta semana?
```
- **Respuesta esperada:** Dar disponibilidad
- **Rama A:** Confirmar fecha → Mensaje 2
- **Rama B:** +2h → Follow-up 1B

---

**MENSAJE 1B (+2h)**
```
Entiendo que hay que cuadrar horarios 😊

¿Prefieres que te diga los horarios disponibles esta semana para que elijas el que más te convenga?

(También tenemos fines de semana si eso ayuda)
```

---

**MENSAJE 2 — REDUCIR FRICCIÓN / FACILITAR**
```
Perfecto — te tengo [día] a las [hora].

Para la valoración solo necesitas:
✅ Venir tú (sin nada que preparar)
✅ 30 minutos de tu tiempo

El médico hace la evaluación, el diseño, y te explica todo. Sin presión de cierre ese día.

¿Confirmas? 🙌
```
- **Rama A:** Confirmar → Agente 5
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B (+24h)**
```
¿Pudiste revisar los horarios?

Quiero asegurarte el espacio porque esta semana tenemos pocos turnos disponibles.

¿Cuál te queda mejor?
```

---

**MENSAJE 3 — URGENCIA REAL (si hay disponibilidad limitada)**
```
Aviso rápido:

Esta semana solo tenemos [X] espacios de valoración disponibles con el Dr. [nombre].

No quiero que te quedes sin lugar. ¿Confirmamos hoy?
```
- **Rama A:** Confirmar
- **Rama B:** +24h → Follow-up 3B

---

**MENSAJE 3B (+24h)**
```
[Nombre], ¿todo bien?

Solo quería saber si hubo algo que te frenó — a veces es el horario, a veces una duda de último momento.

¿Qué está pasando?
```

---

**MENSAJE 4 — MANEJO DE ÚLTIMA DUDA**
```
Mira, cuando alguien está listo para dar el paso y de repente se frena...

Casi siempre es por una de estas cosas:
1. Una duda sobre el resultado
2. Una duda sobre el costo
3. Un miedo que no ha dicho en voz alta

¿Cuál de esas es la tuya? Sin pena 🙏
```
- **Rama A:** Resolver objeción específica → Cerrar valoración
- **Rama B:** +48h → Mensaje 5

---

**MENSAJE 5 — CIERRE DEFINITIVO DE NIVEL**
```
[Nombre], última vez que te pregunto esta semana 😊

¿Agendamos la valoración o prefieres esperar a la próxima semana?

Cualquiera de las dos está bien — solo quiero saber para cuadrar el espacio.
```
- **Rama A:** Confirmar → Agente 5
- **Rama B:** Reactivación en 5 días

---

### B. RESPUESTAS A OBJECIONES — NIVEL 4

**Objeción 1: "¿Cuánto cuesta?" (en este punto, pregunta legítima)**
```
En la valoración te damos el precio exacto para tu caso.

Lo que te puedo adelantar: el rango general es [X]–[Y] USD, y tenemos opciones de financiamiento desde [monto] al mes.

¿Eso está dentro de lo que pensabas manejar?
```

**Objeción 2: "Miedo a que se vea falso"**
```
En la valoración, el médico te muestra el diseño antes de cualquier decisión.

Ves en pantalla cómo quedaría tu nacimiento de cabello, la densidad, la dirección.

Literalmente ves el resultado antes de que pase. ¿Eso te da más paz?
```

**Objeción 3: "No tengo tiempo"**
```
30 minutos. Eso es todo.

¿Hay algún momento esta semana, así sea a las 7am o un sábado, que puedas sacar eso?
```

**Objeción 4: "Lo voy a pensar"**
```
Claro — la valoración es justo para terminar de pensar con datos reales.

No te pido que decidas en la valoración. Te pido que vayas con las preguntas que tienes y salgas con respuestas.

¿Eso sí lo puedes hacer?
```

**Objeción 5: "Vi otros lugares más baratos"**
```
Si te dan resultados iguales al mismo nivel de calidad — hazlo.

Pero antes de decidir por precio, ¿ya visitaste esa clínica y viste casos reales de sus pacientes?

Si no lo has hecho, hazlo. Y luego compara. Con eso en mente, la decisión se vuelve obvia.
```

---

### C. MENSAJE DE TRANSICIÓN AL NIVEL 5
```
Excelente — quedamos para [día] a las [hora] en nuestra clínica.

Te voy a confirmar la dirección y lo que necesitas saber para la visita.

¿Tienes el número guardado por si necesitas escribirme antes? 😊
```

---

### D. MENSAJE DE REACTIVACIÓN
**5 días:**
```
Hola [nombre] 👋

Hace unos días ibas a agendar la valoración.

¿Qué pasó? ¿Pudiste resolverlo o hay algo que no cuadró?
```

**10 días:**
```
[Nombre], solo paso a decirte que el espacio que teníamos para ti sigue disponible.

Si quieres retomarlo, dímelo y lo cuadramos en 2 minutos.
```

---

---

## AGENTE 5 — NIVEL 5: COMPROMETIDO / PRE-CITA

### Perfil del lead
Agendó su cita. El mayor riesgo ahora es el no-show. Necesita confirmación, anticipación positiva, reducción de ansiedad y recordatorios sin ser invasivo.

### Tono
Cálido. Confianza. Anticipación. Logístico sin ser frío.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — CONFIRMACIÓN INMEDIATA (minutos después de agendar)**
```
¡Listo! 🎉 Tu valoración está confirmada.

📅 [Día], [fecha] a las [hora]
📍 [Dirección]

Guarda este mensaje — te voy a escribir el día anterior para recordarte.

¿Tienes alguna duda antes de la visita?
```

---

**MENSAJE 2 — 48h ANTES DE LA CITA**
```
Hola [nombre] 👋

Tu valoración es pasado mañana — solo quería recordártelo.

Una cosa: ven tranquilo. No hay nada que preparar, no hay nada que decidir ese día. Es solo para que el médico te evalúe y te cuente qué es posible en tu caso 🙌
```

---

**MENSAJE 3 — 24h ANTES**
```
Mañana es tu valoración 🙌

📅 [Día] a las [hora]
📍 [Dirección / link Google Maps]

Si necesitas cambiar el horario por cualquier cosa, escríbeme hoy y lo resolvemos sin problema.

¿Todo sigue en pie?
```
- **Rama A (confirma):** Mensaje 4
- **Rama B (pide cambio):** Reagendar → volver a Mensaje 2 con nueva fecha
- **Rama C (no responde):** +12h → Follow-up 3C

---

**MENSAJE 3C — FOLLOW-UP (+12h sin respuesta)**
```
Solo para confirmar que sigues en pie para mañana 😊

Si algo cambió en tu agenda, me avisas y lo movemos sin problema.
```

---

**MENSAJE 4 — DÍA DE LA CITA (mañana, 2h antes)**
```
Buenos días [nombre] ☀️

Hoy es tu valoración. En [X] horas te esperamos.

Cualquier duda de último momento — escríbeme aquí mismo. Que tengas un excelente día 💪
```

---

**MENSAJE 5 — POST-CITA (1–2h después de la hora de cita, si no hay feedback)**
```
Hola [nombre], ¿cómo te fue en la valoración?

¿El médico pudo responderte todo lo que necesitabas?
```
- **Rama A (fue):** Transición a Agente 7 o cierre
- **Rama B (no fue):** Transición a Agente 6

---

### B. RESPUESTAS A OBJECIONES — NIVEL 5

**Objeción 1: "¿Puedo saber el precio antes de ir?"**
```
El precio exacto se define en la valoración porque depende del número de folículos de tu caso.

Lo que sí te digo: el rango está entre [X] y [Y] USD, y hay financiamiento disponible.

Pero lo más importante: la valoración es gratis y sin compromiso. Solo ves, preguntas, y decides después.
```

**Objeción 2: "¿Y si voy y luego no me convence?"**
```
Perfectamente válido.

La valoración no te compromete a nada. Puedes ir, escuchar, ver el diseño... y tomarte todo el tiempo que necesites.

Nadie te va a presionar. Te lo prometo 🙏
```

**Objeción 3: "Tengo poco tiempo ese día"**
```
Sin problema — la valoración dura 30 minutos.

Si tienes algún apuro, dime a qué hora necesitas salir y lo organizamos para que llegues a tiempo a lo siguiente.
```

**Objeción 4: "Lo estoy pensando de nuevo"**
```
Normal — es una decisión importante y es bueno pensarla bien.

¿Qué es lo que está rondando tu cabeza? Dímelo y lo conversamos antes de la cita, para que llegues con las ideas más claras.
```

**Objeción 5: "Vi algo más barato y me generó duda"**
```
Eso pasa mucho — y tiene sentido.

Mi sugerencia: ven a la valoración igual. Escucha al médico, ve el diseño de tu caso, y con esa información en la mano compara lo que quieras.

Así la comparación es justa y tú decides con todo en la mesa 🙏
```

---

### C. MENSAJE DE TRANSICIÓN (post-cita)
```
Me alegra que hayas podido ir 🙌

¿El médico te explicó bien todo? ¿Quedaste con alguna pregunta pendiente?

(Esto es importante — quiero que tengas todo claro antes de cualquier decisión)
```

---

### D. MENSAJE DE REACTIVACIÓN (si había cita pero dejó de responder antes)
```
Hola [nombre] 👋

Tu cita es [fecha]. ¿Sigues en pie o necesitas cambiar algo?

Dímelo con tiempo y lo resolvemos 🙏
```

---

---

## AGENTE 6 — NIVEL 6: NO-SHOW

### Perfil del lead
No fue a la cita. Puede ser por miedo, por imprevistos reales, o por enfriamiento. NO se le juzga. Se le da una puerta fácil de volver a entrar sin vergüenza.

### Tono
Empatía total. Sin juicio. Facilidad absoluta para reagendar. Normalizar la situación.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — 30–60 MIN DESPUÉS DE LA HORA DE CITA**
```
Hola [nombre] 👋

Veo que no pudiste llegar hoy — completamente entendible, pasan cosas.

¿Estás bien? ¿Hubo algo que te surgió?
```
- **Respuesta esperada:** Explicación o disculpa
- **Rama A (explica):** Empatizar → Reagendar → Mensaje 2
- **Rama B (no responde):** +3h → Follow-up 1B

---

**MENSAJE 1B (+3h)**
```
Oye, no te preocupes por no haber podido ir hoy.

Si quieres retomar, basta con decirme y cuadramos un nuevo espacio. Sin formularios, sin explicaciones.

¿Te parece?
```

---

**MENSAJE 2 — REAGENDAMIENTO FÁCIL**
```
Para reagendar es muy sencillo:

Dime cuál es el mejor día y hora para ti esta semana o la siguiente, y yo te lo organizo.

No hay que volver a empezar desde cero — ya tienes tu caso registrado 🙌
```
- **Rama A:** Confirma nuevo horario → Vuelve al flujo del Agente 5
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B (+24h)**
```
[Nombre], ¿tienes un momento para decirme cuándo podrías venir?

No me toma más de 2 minutos cuadrarte el nuevo espacio.

¿Esta semana o la próxima?
```

---

**MENSAJE 3 — SI HAY SILENCIO (+48h)**
```
Entiendo que a veces estas cosas se postergan.

Solo quiero que sepas que el espacio sigue disponible para cuando estés listo.

¿Hay algo que te generó duda o te cambió el ánimo sobre el tema?
```
- **Rama A:** Resolver la duda → Reagendar
- **Rama B:** +72h → Mensaje 4

---

**MENSAJE 4 — REACTIVACIÓN EMOCIONAL (+72h)**
```
[Nombre], a veces cuando uno no va a la cita es porque algo por dentro dice "no sé si quiero".

Y eso es completamente válido.

¿Es eso lo que está pasando, o fue solo un imprevisto? (Te lo pregunto de verdad, no para venderte nada)
```
- **Rama A:** Honestidad → manejo humano
- **Rama B:** +5 días → Mensaje 5

---

**MENSAJE 5 — ÚLTIMO INTENTO NIVEL 6**
```
Oye, solo quiero decirte algo antes de dejar de escribirte por un tiempo:

Lo que sentías sobre tu imagen cuando hablamos — eso no desaparece solo.

Cuando sientas que es el momento, aquí voy a estar. Sin juicio, sin apuro. 🙏

¿Hay algo en lo que pueda ayudarte hoy?
```
- **Rama A:** Reagendar
- **Rama B:** Archivar → Reactivación en 21 días

---

### B. RESPUESTAS A OBJECIONES — NIVEL 6

**Objeción 1: "Me da pena no haber ido"**
```
No hay absolutamente nada de qué avergonzarse — te lo digo en serio.

Pasa constantemente. Lo que importa es que cuando quieras retomarlo, el espacio sigue aquí.

¿Cuándo te queda mejor esta semana?
```

**Objeción 2: "Creo que no es el momento"**
```
Entiendo y respeto eso.

¿Me puedes decir qué cambió? ¿Fue algo externo (tiempo, dinero) o algo interno (dudas sobre el procedimiento)?

Pregunto porque a veces hay algo que sí podemos resolver 🙏
```

**Objeción 3: "Tuve un imprevisto de verdad"**
```
Sin problema, eso le pasa a cualquiera 🙌

Cuéntame cuándo tienes disponibilidad y lo cuadramos en 2 minutos.

¿Esta semana o la siguiente?
```

**Objeción 4: "Estoy muy ocupado"**
```
Completamente entendido.

¿Y si lo agendamos para dentro de 2–3 semanas? Así lo tienes en el radar pero sin presión inmediata.

¿Te parece?
```

**Objeción 5: "Lo estoy reconsiderando"**
```
Eso está bien — es una decisión importante y merece reconsiderarse.

¿Hubo algo en específico que cambió? A veces es útil hablarlo para tener claridad.

¿Qué fue lo que te generó duda?
```

---

### C. MENSAJE DE TRANSICIÓN AL NIVEL 5 (reagendamiento)
```
Perfecto, quedamos para [nueva fecha] a las [hora].

Esta vez te voy a confirmar el día anterior, igual que antes.

¿Todo bien desde tu lado? 🙏
```

---

### D. MENSAJE DE REACTIVACIÓN (después de 21 días de silencio)
```
Hola [nombre] 😊

Hace unas semanas intentaste venir a la valoración.

No sé si el momento llegó todavía, pero quería saludarte y preguntarte: ¿cómo estás con el tema del cabello hoy?
```

---

---

## AGENTE 7 — NIVEL 7: POST-CONSULTA SIN CIERRE

### Perfil del lead
Fue a la consulta. Escuchó al médico. Vio el diseño. Sabe el precio. Y no cerró. La razón casi siempre es financiera o de "tiempo para pensarlo". Este es el nivel más estratégico: el lead ya compró emocionalmente, solo falta remover la última barrera.

### Tono
Acompañamiento. Paciencia. Manejo de objeciones financieras. Cero presión directa.

---

### A. SECUENCIA DE MENSAJES

---

**MENSAJE 1 — 2–3h DESPUÉS DE LA CONSULTA**
```
Hola [nombre], ¿cómo te fue con la valoración?

¿El Dr. [nombre] te pudo explicar bien todo lo que necesitabas?
```
- **Respuesta esperada:** Feedback sobre la consulta
- **Rama A:** Continuar con Mensaje 2
- **Rama B:** +24h → Follow-up 1B

---

**MENSAJE 1B (+24h)**
```
[Nombre], ayer fue tu valoración.

Quería saber cómo te sentiste — ¿quedaste con preguntas pendientes o con alguna duda que no te animaste a hacer?
```

---

**MENSAJE 2 — VALIDAR LA EXPERIENCIA**
```
Me alegra que hayas podido ir 🙌

A veces después de la consulta quedan cosas que procesar. Es normal — es una decisión importante.

¿Qué es lo que más te quedó resonando de lo que te explicó el médico?
```
- **Rama A:** Identificar motivación real → reforzar
- **Rama B:** +24h → Follow-up 2B

---

**MENSAJE 2B (+24h)**
```
Una pregunta directa:

Después de la consulta, ¿hay algo que te frena para dar el paso, o solo estás tomando tu tiempo para pensarlo?

Sin presión — quiero entender dónde estás 🙏
```

---

**MENSAJE 3 — IDENTIFICAR LA BARRERA REAL**
```
Hay básicamente tres razones por las que alguien no decide después de una consulta:

1. Necesita más tiempo para pensar
2. Tiene una duda que no se resolvió del todo
3. El tema financiero no cuadra aún

¿Cuál de esas es la tuya? (O si es otra, también cuéntame)
```
- **Rama A — Tiempo:** Ir a Mensaje 4A
- **Rama B — Duda técnica:** Ir a Mensaje 4B
- **Rama C — Financiero:** Ir a Mensaje 4C

---

**MENSAJE 4A — MANEJO "NECESITO TIEMPO"**
```
Entiendo. Es una decisión importante y merece tiempo.

¿Cuánto tiempo crees que necesitas para tomar la decisión?

(Lo pregunto para no molestarte antes de que estés listo 😊)
```

---

**MENSAJE 4B — MANEJO DUDA TÉCNICA**
```
Dime cuál es la duda — sin pena.

A veces en la consulta no se pregunta todo porque el momento no lo da.

¿Qué es lo que no quedó 100% claro?
```
*(Resolver la duda → Ir a Mensaje 5)*

---

**MENSAJE 4C — MANEJO OBJECIÓN FINANCIERA**
```
El tema del costo es completamente válido — es una inversión importante.

¿Me dices cuál es la parte que no cuadra? ¿El total, el momento, o la forma de pagarlo?

Porque hay opciones que quizás no te mencionaron en la consulta 🙏
```

---

**MENSAJE 5 — PRESENTAR OPCIONES DE FINANCIAMIENTO**
```
Mira, para que no sea una barrera:

Tenemos financiamiento disponible desde [X] al mes, sin entrada.

Eso significa que puedes empezar tu proceso hoy y distribuir el costo cómodamente.

¿Quieres que te explique cómo funciona?
```
- **Rama A:** Detallar financiamiento → Cerrar
- **Rama B:** +48h → Follow-up 5B

---

**MENSAJE 5B (+48h)**
```
[Nombre], ¿pudiste pensar en el tema del financiamiento?

Si hay algo que no quedó claro o quieres que lo revisemos juntos, dime y lo vemos ahora.
```

---

**MENSAJE 6 — CIERRE SUAVE CON URGENCIA REAL**
```
[Nombre], quiero ser honesto contigo:

El diseño de tu caso ya está listo. El médico ya sabe qué hacer. Solo falta tu decisión.

¿Hay algo que yo pueda hacer para que ese paso sea más fácil para ti?
```
- **Rama A:** Responde → Resolver y cerrar
- **Rama B:** +5 días → Reactivación

---

### B. RESPUESTAS A OBJECIONES — NIVEL 7

**Objeción 1: Precio total**
```
Entiendo — es una inversión considerable.

Lo que te pido que consideres: ¿cuánto le estás "costando" a tu confianza cada año que pasa sin resolverlo?

No para presionarte — sino para que la comparación sea real.

¿Quieres explorar las opciones de pago disponibles?
```

**Objeción 2: "Se ve muy caro para el resultado"**
```
Eso me parece importante aclararlo.

¿Recuerdas los casos que te mostró el médico? Eso es lo que logra este equipo.

Un procedimiento más barato puede darte un resultado que tengas que corregir — y eso cuesta el doble.

¿Quieres ver más casos de resultados nuestros antes de decidir?
```

**Objeción 3: "Lo voy a hacer el año que viene"**
```
Eso suena razonable... pero ¿sabes qué pasa mientras tanto?

La pérdida de cabello avanza. Y cuanto más esperas, más folículos necesitas.

No es urgencia artificial — es biología. ¿Quieres que te explique por qué actuar antes da mejores resultados?
```

**Objeción 4: "Mi pareja/familia no sabe / no apoya"**
```
Eso es más común de lo que crees.

¿Me dices cuál es la preocupación de ellos? Porque a veces es falta de información, no falta de apoyo.

¿Quieres que te pase algo que puedas mostrarles para que entiendan bien en qué consiste?
```

**Objeción 5: "Quiero comparar con otra clínica antes"**
```
Perfectamente válido — es lo que haría yo también.

Solo una cosa: cuando vayas, pide ver casos reales de sus pacientes y pregunta quién hace el diseño del nacimiento.

Con eso en mente, la comparación se vuelve muy fácil 🙏
```

---

### C. MENSAJE DE CIERRE / TRANSICIÓN A CLIENTE
```
[Nombre], creo que llegó el momento.

Tienes toda la información, viste el diseño de tu caso, conoces el equipo.

¿Damos el paso? Te confirmo la fecha de procedimiento y te mando los detalles de cómo prepararte.
```

---

### D. MENSAJE DE REACTIVACIÓN POST-CONSULTA
**7 días:**
```
Hola [nombre] 😊

Han pasado unos días desde tu valoración.

¿Tomaste alguna decisión o sigues en el proceso de pensar? Sin apuro — solo quiero saber cómo acompañarte.
```

**21 días:**
```
[Nombre], hace unas semanas tuviste la consulta con nosotros.

No quiero asumir nada — ¿sigue siendo algo que tienes en mente o lo dejaste para más adelante?

(Dímelo con confianza, ambas respuestas están bien 🙏)
```

---

---

## BIBLIOTECA DE MICRO-COPYS DE URGENCIA Y ESCASEZ

> Todos reales y creíbles. Para usar en cualquier nivel del funnel.

1. "Solo tenemos [X] espacios de valoración disponibles esta semana con el Dr. [nombre]."
2. "Los turnos de los viernes se llenan generalmente el martes. Si quieres ese día, hay que moverlo hoy."
3. "Este mes tenemos un solo espacio disponible para procedimientos — los demás están ocupados hasta [mes]."
4. "El precio actual es el que te cotizamos en la valoración. Si lo dejas para el próximo trimestre, puede cambiar."
5. "Estamos recibiendo muchas consultas esta semana — prefiero reservarte el espacio hoy para que no te quedes sin él."
6. "El Dr. [nombre] tiene agenda muy limitada. Esta semana tiene 2 espacios libres para valoración."
7. "Los resultados más naturales se logran cuando se opera antes de perder más densidad. Cada mes que pasa importa."
8. "Tu diseño ya está listo — solo falta tu decisión para bloquearte la fecha."
9. "Hay una lista de espera para cirugías de este mes. Si quieres entrar, hay que moverlo hoy."
10. "Normalmente los leads de este mes tienen respuesta en 48h — esta semana estamos procesando muchas consultas, así que te confirmo lo antes posible."

---

---

## BIBLIOTECA DE SOCIAL PROOF

> Mini-testimonios en formato WhatsApp. Sin nombres reales. Representativos de avatares A, B y C.

---

**Testimonio 1 — Avatar A (Ejecutivo / Profesional Premium)**
```
"Llevo 3 años trabajando en una empresa grande. Siempre pensé que era vanidad. Pero cuando estaba en una reunión con gente de mi edad que se veían 10 años menores, algo cambió. Hice la valoración sin decirle a nadie. Hoy, 9 meses después, nadie sabe que me hice algo. Solo notan que me veo bien."
```

---

**Testimonio 2 — Avatar B (Joven Emprendedor)**
```
"Tengo 31 años y mi marca personal lo es todo. Empecé a notar que en mis stories y videos lo primero que veía era la entradas. Lo hice y fue la mejor inversión de mi carrera. La gente en mis redes no sabe qué cambié — solo dicen que me veo diferente. Mejor."
```

---

**Testimonio 3 — Avatar C (Hombre Maduro)**
```
"Tenía 52 años y llevaba como 15 con esto. Mi esposa siempre me dijo que no importaba pero yo lo sentía. Lo hice más por mí que por cualquier otra persona. A los 8 meses me vi en una foto familiar y no me reconocí — pero en el buen sentido. Me sentí yo de nuevo."
```

---

**Testimonio 4 — Objeción resuelta (miedo a lo artificial)**
```
"Mi miedo más grande era parecer uno de esos tipos con cabello de muñeco. El médico me mostró el diseño antes de empezar. Cuando lo vi dije 'así quiero quedar' — y quedé igual. Nadie jamás me ha preguntado si me hice algo. Solo que si bajé de peso o si estoy haciendo ejercicio."
```

---

**Testimonio 5 — Objeción resuelta (precio)**
```
"Al principio me pareció caro. Luego pensé: llevo 8 años gastando en productos que no funcionan, usando gorras para disimular, evitando fotos. Sumas eso y el costo se ve diferente. Fue la decisión financieramente más inteligente que tomé en mucho tiempo."
```

---

---

## NOTAS DE IMPLEMENTACIÓN EN GHL

### Variables dinámicas a configurar
- `{{contact.first_name}}` → [nombre]
- `{{appointment.date}}` → [fecha]
- `{{appointment.time}}` → [hora]
- `{{doctor.name}}` → [nombre del médico]
- `{{clinic.address}}` → [dirección]
- `{{price.range.low}}` / `{{price.range.high}}` → rango de precio
- `{{financing.monthly}}` → cuota mensual de financiamiento

### Timings recomendados de automatización
| Trigger | Delay recomendado |
|---|---|
| Lead entra al nivel | Inmediato (0–5 min) |
| Sin respuesta mensaje 1 | +2 horas |
| Sin respuesta mensaje 2 | +24 horas |
| Sin respuesta mensaje 3 | +48 horas |
| Lead se enfría | +5 días |
| Reactivación profunda | +14–21 días |
| Día anterior a cita | -24 horas |
| Día de cita | -2 horas |
| Post-cita feedback | +2 horas |

### Etiquetas de nivel para enrutamiento
- `nivel-0` → sin clasificar
- `nivel-1` → problema consciente
- `nivel-2` → busca solución
- `nivel-3` → comparando clínicas
- `nivel-4` → listo para decidir
- `nivel-5` → cita agendada
- `nivel-6` → no-show
- `nivel-7` → post-consulta sin cierre
- `cliente` → cerrado

---

*Documento generado: 2026-06-12 | Innovart Medical | Uso interno*
*Revisar y actualizar precios, disponibilidad y nombre de médicos antes de activar en producción.*
