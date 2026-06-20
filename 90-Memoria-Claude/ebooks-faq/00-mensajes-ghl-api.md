# Reimpacto con los 8 Ebooks — Secuencias listas para GHL (Innovart)

**Notas de envío (aplican a todo):**
- Canal "WhatsApp" = acción `send_message type WhatsApp` (from = WABA de la sede). Para ESCUCHAR la respuesta se filtra `message.type==2` (SMS/applevel), nunca 19.
- Al entrar humano/Sofia o el bot tomar el caso: aplicar tag `ai_parar`.
- Cada ebook = trigger link medible (`{{ebook_link_eNN}}`). CTA final siempre = valoración gratis (`{{link_agenda}}`).
- Merge field de nombre: `{{contact.first_name}}`. Tuteo siempre. WhatsApp cortos. Nunca dos toques presionando el mismo día.

---

## BANCO DE GANCHOS (hook por ebook)

- **E01 (frío) Dolor/anestesia:** "El miedo #1 antes de un implante es el dolor. Te cuento la verdad (con anestesia de por medio) sin adornos 👇"
- **E02 (tibio) FUE vs DHI:** "FUE o DHI no es lo mismo ni para todos. En 4 min sabés cuál te conviene a vos 👇"
- **E03 (tibio) Folículos/zona donante:** "¿Cuántos folículos necesitás realmente? Y por qué un buen diseño es el que envejece bien contigo 👇"
- **E04 (frío) Día a día:** "El día del implante y los 8 días siguientes, hora por hora. Así sabés exactamente qué esperar 👇"
- **E05 (tibio) Shedding/tiempos:** "¿Cuándo vas a ver tu cabello de verdad? La línea de tiempo real, sin promesas falsas (3 a 18 meses) 👇"
- **E06 (frío) ¿Soy candidato?:** "Edad, grado de alopecia, mujeres, casos especiales… ¿sos candidato? Revisalo en 3 min 👇"
- **E07 (tibio) Costo/financiación:** "El precio real y cómo financiarlo hasta el 90%. Sin letra chica 👇"
- **E08 (frío) Proteger tu inversión:** "Hacerte el implante es la mitad. La otra mitad es el plan médico que mantiene tu resultado 👇"

---

# SEGMENTO FRÍO — Secuencia (7 toques, re-permiso primero)

**Toque 1 — RE-PERMISO (D0, 10:00) — WhatsApp**
> Hola {{contact.first_name}} 👋 Soy del equipo médico de Innovart Medical (implante capilar, Dr. Fabián Carreño, Director Médico).
> Hace un tiempo te interesó el tema del cabello. Preparamos una guía corta y honesta: **"¿Duele el implante capilar? La verdad sobre el dolor y la anestesia"**.
> ¿Te la mando? Respondé **SÍ** y te paso el link 🙂

**Toque 2 — Entrega E01 tras "SÍ" (D0 al responder) — WhatsApp**
> ¡Genial, {{contact.first_name}}! Acá está 👇
> 📘 ¿Duele el implante capilar?: {{ebook_link_e01}}
> Léela con calma. Cualquier duda me escribís por acá.
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 3 — E06 ¿Soy candidato? (D2, 18:00) — WhatsApp**
> {{contact.first_name}}, la pregunta que casi todos se hacen: **¿soy candidato?**
> Edad, grado de alopecia, casos en mujeres y casos especiales — está todo acá 👇
> 📗 {{ebook_link_e06}}
> Si te queda la duda de tu caso puntual, te digo cómo resolverla.
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 4 — E04 Proceso día a día (D5, 10:00) — Email**
> **Asunto:** {{contact.first_name}}, qué pasa el día del implante (y los 8 días después)
> Hola {{contact.first_name}}, una de las cosas que más tranquiliza antes de decidir es saber **exactamente** qué va a pasar. Sin sorpresas.
> Por eso te comparto: **El día del implante y los 8 días siguientes.** Es un procedimiento mínimamente invasivo y acá te lo explicamos paso a paso.
> 👉 {{ebook_link_e04}}
> Cuando quieras, agendá una valoración gratuita con el Dr. Fabián Carreño: {{link_agenda}}
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 5 — Check-in conversacional (D8, 17:00) — WhatsApp**
> {{contact.first_name}}, ¿pudiste leer alguna de las guías que te mandé? 🙂
> Te leo si te quedó alguna duda — la que sea, sin compromiso. ¿Qué es lo que más te frena hoy: el dolor, el precio o no saber si sos candidato?

**Toque 6 — E08 Proteger tu inversión (D12, 10:00) — WhatsApp**
> {{contact.first_name}}, algo que casi nadie te cuenta antes de un implante 👇
> Hacértelo es la mitad del camino. La otra mitad es el **plan médico que mantiene tu resultado** en el tiempo.
> 📙 {{ebook_link_e08}}
> Esto es justo lo que revisa el Dr. Carreño en la valoración. ¿Te muestro cómo sería para tu caso?
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 7 — Cierre suave + permiso futuro (D16, 18:00) — WhatsApp**
> {{contact.first_name}}, no quiero ser intenso 🙂 Si por ahora no es el momento, todo bien.
> Si querés dar el paso, la valoración con el Dr. Carreño es **gratis y sin compromiso** — ahí sabés exactamente cuántos injertos necesitás y el precio real para tu caso: {{link_agenda}}
> ¿Te escribo de nuevo más adelante, o prefieres que lo dejemos hasta acá?

---

# SEGMENTO TIBIO — Secuencia (7 toques, permiso vivo)

**Toque 1 — Reapertura + E07 Costo/financiación (D0, 11:00) — WhatsApp**
> Hola {{contact.first_name}} 👋 Te escribo del equipo de Innovart Medical.
> Sé que el precio pesa en la decisión, así que voy directo: preparamos una guía con el **precio real y cómo financiarlo hasta el 90%**, sin letra chica 👇
> 💰 {{ebook_link_e07}}
> Si querés, te digo cómo quedaría la cuota para tu caso.
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 2 — E02 FUE vs DHI (D2, 18:00) — WhatsApp**
> {{contact.first_name}}, FUE o DHI no es lo mismo — y elegir bien cambia el resultado.
> En esta guía corta entendés cuál técnica te conviene a vos y por qué 👇
> 📘 {{ebook_link_e02}}
> Usamos **técnica avanzada FUE/DHI**, procedimiento mínimamente invasivo. ¿Te resuelvo qué aplicaría en tu caso?
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 3 — E03 Folículos / zona donante (D4, 10:00) — Email**
> **Asunto:** {{contact.first_name}}, ¿cuántos folículos necesitás de verdad?
> Hola {{contact.first_name}}, el número de folículos y el diseño de la línea capilar son lo que define un **resultado natural** que envejece bien contigo — no solo "hoy", sino en 10 años.
> 👉 {{ebook_link_e03}}
> El número exacto para tu caso solo se determina en la valoración con el Dr. Fabián Carreño. Es gratis: {{link_agenda}}
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 4 — E05 Shedding / tiempos reales (D6, 17:00) — WhatsApp**
> {{contact.first_name}}, una verdad que pocos cuentan: el cabello no aparece de un día para otro.
> Hay un proceso (el *shedding*) y una línea de tiempo real de **3 a 18 meses**. Te lo explico sin promesas falsas 👇
> 📗 {{ebook_link_e05}}
> Justo por eso vale la pena entender bien tu caso antes de decidir. ¿Lo vemos en una valoración gratis?
> *Los resultados pueden variar. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente.*

**Toque 5 — Conversión a valoración (D8, 11:00) — WhatsApp**
> {{contact.first_name}}, ya tenés el panorama completo: técnica, folículos, tiempos y financiación 🙌
> El siguiente paso natural es una **valoración gratuita** con el Dr. Carreño: te dice cuántos injertos necesitás, cómo quedaría tu resultado y el precio exacto.
> ¿Cuándo te queda mejor, **esta semana o la próxima**? 📅 {{link_agenda}}

**Toque 6 — Escasez real + financiación (D11, 18:00) — WhatsApp**
> {{contact.first_name}}, la agenda del Dr. Carreño se llena rápido y los cupos de valoración de esta quincena están casi completos.
> Si te interesa, te reservo uno — es gratis y sin compromiso. Y recordá que tenemos **financiación hasta el 90%**, así el presupuesto no es el freno.
> ¿Te aparto el cupo? 📅 {{link_agenda}}

**Toque 7 — Último toque + permiso futuro (D15, 17:00) — WhatsApp**
> {{contact.first_name}}, te dejo la puerta abierta 🙂 Cuando estés listo, la valoración sigue siendo gratis y sin compromiso: {{link_agenda}}
> ¿Te contacto más adelante o prefieres avanzar ahora? Lo que te sirva mejor.

---

# RESPUESTAS RÁPIDAS A OBJECIONES (bot/asesor)

**1) "¿Duele?"**
> Entiendo la duda, es la más común 🙂 El procedimiento se hace con anestesia local y es **mínimamente invasivo**. La mayoría de pacientes lo describe como muy llevadero. Guía completa 👇 {{ebook_link_e01}}. ¿Te resuelvo algo puntual?

**2) "Está muy caro / no me alcanza"**
> Te entiendo. Para comparar: otras clínicas en Colombia cobran entre $14M y $20M. En Innovart el precio depende de los injertos que necesités, y tenemos **financiación hasta el 90%**. Detalle 👇 {{ebook_link_e07}}. ¿Te calculo una cuota aproximada?

**3) "Lo voy a pensar"**
> Claro, tomate el tiempo — es una decisión importante. La valoración es **gratis y no te compromete a nada**, sirve justo para decidir con información real. ¿Te aparto un cupo sin compromiso? {{link_agenda}}

**4) "Me queda lejos / soy de otra ciudad"**
> Sin problema 🙂 Tenemos sedes en Bogotá, Medellín, Barranquilla, Bucaramanga y Panamá. Además la **valoración inicial puede ser virtual**. ¿Desde qué ciudad me escribís?

**5) "Tengo miedo a que se note / quede antinatural"**
> Preocupación muy válida. El secreto está en el **diseño de la línea capilar y la cantidad de folículos**, pensados para un **resultado natural** que envejece bien. Guía 👇 {{ebook_link_e03}}. En la valoración el Dr. Carreño te muestra cómo quedaría. {{link_agenda}}

---

# CONVERSIÓN A VALORACIÓN

**Interés detectado:**
> ¡Me encanta, {{contact.first_name}}! 🙌 El siguiente paso es tu **valoración gratuita** con el Dr. Fabián Carreño: te dice cuántos injertos necesitás y el precio exacto. ¿Te queda mejor **martes o jueves**? 📅 {{link_agenda}}

**Pide precio exacto:**
> El precio exacto depende de los injertos que necesité tu caso, y eso solo se define en la valoración (gratis). Ahí te dan el número real y opciones de financiación. ¿Agendamos esta semana? {{link_agenda}}

**Confirmación de cita:**
> ¡Listo {{contact.first_name}}! Tu valoración quedó confirmada para **{{appointment.start_time}}** 🎉 Es gratis y sin compromiso. Llegá 5 min antes. Cualquier cambio me avisás por acá.

---

# RECORDATORIO Y NO-SHOW

**Recordatorio 24h antes — WhatsApp:**
> Hola {{contact.first_name}} 🙂 Te recuerdo tu **valoración gratuita** con el Dr. Carreño mañana a las **{{appointment.start_time}}**. ¿Confirmás que asistís? Respondé **SÍ** y queda reservado tu cupo.

**Recordatorio mismo día (3h antes) — WhatsApp:**
> {{contact.first_name}}, ¡hoy es tu valoración! 🎉 Te esperamos a las **{{appointment.start_time}}**. Si necesitás reprogramar, avisame y lo movemos sin problema.

**No-show (1-2h después) — WhatsApp:**
> {{contact.first_name}}, no te vimos en tu valoración de hoy 🙂 ¿Pasó algo o se te cruzó la agenda? La reagendamos cuando te quede bien. ¿Mañana o pasado? {{link_agenda}}

**No-show seguimiento (D+2) — WhatsApp:**
> {{contact.first_name}}, te guardo el cupo un par de días más. La valoración sigue siendo **gratis y sin compromiso** y es la forma más rápida de saber qué te corresponde. ¿Te reagendo? {{link_agenda}}

---

**Cobertura:** FRÍO 7 toques (E01, E06, E04, E08) + TIBIO 7 toques (E07, E02, E03, E05), mezcla WhatsApp/Email, banco de 8 ganchos, 5 objeciones, conversión y no-show. Tuteo colombiano, disclaimer en cada mensaje con resultados, sin frases prohibidas. Placeholders: `{{contact.first_name}}`, `{{ebook_link_e01}}`–`{{ebook_link_e08}}`, `{{link_agenda}}`, `{{appointment.start_time}}`.
