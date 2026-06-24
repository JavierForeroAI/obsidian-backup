# -*- coding: utf-8 -*-
from innovart_template import *

# =====================================================================
# 9) MINOXIDIL Y FINASTERIDA
# =====================================================================
article(
 meta=dict(
   title="Minoxidil y finasterida: cómo funcionan de verdad (y sus mitos)",
   slug="minoxidil-finasterida-como-funcionan-mitos",
   related=[('Alopecia androgénetica', 'alopecia-androgenetica-por-que-se-cae-el-pelo'), ('Shedding: caída al empezar', 'shedding-caida-al-empezar-tratamiento'), ('Estrés y caída del cabello', 'estres-y-caida-del-cabello')],
   category="Tratamientos",
   read_min=10,
   deck="Son los dos fármacos más usados contra la calvicie y los dos más malentendidos. Te explicamos su mecanismo real y separamos la evidencia del miedo de los foros.",
   meta_desc="Cómo funcionan el minoxidil y la finasterida/dutasterida contra la alopecia: mecanismo real, tópico vs oral, efectos secundarios reales vs mitos y síndrome post-finasterida. Contenido educativo de Innovart Medical.",
   keywords="minoxidil, finasterida, dutasterida, 5-alfa-reductasa, efectos secundarios finasterida, síndrome post-finasterida, sulfotransferasa",
 ),
 lead="Casi todo el mundo ha oído hablar del minoxidil y la finasterida, y casi nadie sabe cómo funcionan realmente. Esa mezcla de fama y desconocimiento alimenta dos extremos igual de dañinos: quien los usa mal y no ve resultados, y quien renuncia a tratarse por miedo a mitos sin base. Aquí va la explicación médica, sin alarmismo y sin marketing. Importante: ningún fármaco debe iniciarse sin valoración y prescripción de tu médico.",
 takeaway_items=[
   "El minoxidil <b>no funciona por “más riego sanguíneo”</b>: activa la vía Wnt que prolonga el crecimiento.",
   "Es un profármaco: necesita la enzima <b>sulfotransferasa</b> para activarse, y por eso a algunos el tópico no les hace nada.",
   "La finasterida y la dutasterida <b>no bajan la testosterona</b>: inhiben la 5-alfa-reductasa y reducen la DHT.",
   "Los efectos sexuales son <b>poco frecuentes (2–5%), dosis-dependientes y reversibles</b>.",
   "Todo esto es información educativa: la indicación y el seguimiento son <b>siempre médicos</b>.",
 ],
 sections=[
  ("Minoxidil: por qué NO es cuestión de “riego”",
   "<p>El mito más extendido dice que el minoxidil hace crecer el pelo porque “lleva más sangre”. Es falso. Si bastara con vasodilatar, cualquier antihipertensivo o incluso el sildenafilo harían crecer cabello, y no ocurre. Lo que realmente sucede es que el minoxidil modula unos canales de potasio en la papila dérmica y con ello <strong>activa la vía molecular Wnt/beta-catenina</strong>: esa señal le dice al folículo que <strong>deje de “suicidarse” (apoptosis), prolifere y alargue su fase de crecimiento</strong>.</p>"
   +img("Infografía del ciclo del pelo (anágena, catágena, telógena) destacando la prolongación de la fase de crecimiento; estilo editorial médico, paleta teal/dorado.",
        "El minoxidil prolonga la fase anágena (de crecimiento) del folículo")),
  ("El detalle que explica por qué a algunos no les funciona",
   "<p>El minoxidil es un <strong>profármaco</strong>: por sí mismo no hace nada. Para activarse debe convertirse en <strong>sulfato de minoxidil</strong> gracias a la enzima <strong>sulfotransferasa</strong> presente en el folículo. El problema: la cantidad de esta enzima en el cuero cabelludo <strong>depende de la genética</strong>. Quien tiene poca actividad enzimática folicular <strong>no verá resultados con la loción</strong>, por mucho que la aplique.</p>"
   +note("Esto explica la frustración de muchos pacientes con el minoxidil tópico. No es que “no les sirva el minoxidil”: es que su folículo no lo activa bien por vía local. El formato y la estrategia los define el médico."),
  ),
  ("Finasterida y dutasterida: qué hacen exactamente",
   "<p>Primer mito a romper: <strong>no son antiandrógenos</strong>. No bloquean el receptor de hormonas masculinas ni bajan la testosterona (que se mantiene o sube ligeramente). Lo que hacen es <strong>inhibir la enzima 5-alfa-reductasa</strong>, la que convierte la testosterona en DHT, la hormona que miniaturiza el folículo. Menos DHT, menos orden de miniaturización.</p>"
   +compare("Finasterida",
     ["Inhibe sobre todo la 5-alfa-reductasa <b>tipo 2</b>.",
      "Vida media corta (4–8 horas).",
      "Amplia experiencia de uso."],
     "Dutasterida",
     ["Inhibidor <b>dual</b> (tipo 1 y 2).",
      "Más potente y de vida media larga (semanas).",
      "Suele ser superior en zonas difíciles (frontal/entradas)."])
   +"<p>La elección entre una u otra, su dosis y su formato (oral o infiltrado) son decisiones estrictamente médicas, ajustadas a cada paciente.</p>"),
  ("Efectos secundarios: evidencia vs miedo de foro",
   "<p>Aquí es donde más daño hace la desinformación. La evidencia muestra que los efectos en la esfera sexual (bajada de libido, menor volumen seminal) son <strong>poco frecuentes: afectan a entre el 2% y el 5%</strong> de los pacientes, son <strong>dosis-dependientes</strong> y, cuando aparecen, son <strong>reversibles</strong> al ajustar la dosis o suspender. Las disfunciones severas son anecdóticas (en torno al 1% o menos).</p>"
   +stats([("2–5%","incidencia de efectos sexuales"),("~1%","disfunciones severas (anecdótico)"),("100%","reversibilidad al ajustar/suspender")])
   +"<p>Sobre el llamado <strong>síndrome post-finasterida</strong> (síntomas persistentes tras suspender): es un cuadro muy cuestionado a nivel farmacológico, porque la finasterida se elimina del cuerpo en horas, lo que hace difícil sostener un daño permanente meses después. La interpretación mayoritaria de la comunidad médica apunta a un fuerte componente del <strong>efecto nocebo</strong> (la sugestión tras leer foros) en perfiles vulnerables. Mencionarlo no es minimizar a quien sufre, sino situar el riesgo real en su contexto.</p>"
   +note("Conclusión sensata: ni automedicarse por moda, ni renunciar al tratamiento por pánico. La decisión correcta se toma con tu médico, valorando tu caso y haciendo seguimiento.")),
 ],
 faq_pairs=[
  ("¿El minoxidil oral es mejor que el tópico?","En muchos pacientes el oral resuelve el problema de la activación local (se activa en el hígado y endotelio), por lo que suele ser más eficaz. Pero el oral requiere indicación y control médico por sus efectos sistémicos."),
  ("Si dejo el tratamiento, ¿pierdo lo ganado?","Sí. Estos fármacos controlan un proceso crónico; al suspenderlos, la alopecia retoma su curso y se pierde lo recuperado en los meses siguientes. Por eso la decisión de iniciar se toma con criterio."),
  ("¿La finasterida afecta la fertilidad?","Puede reducir el volumen seminal en una minoría de casos, de forma reversible. Si hay búsqueda de embarazo, es un punto que se conversa y maneja con el médico."),
  ("¿Puedo combinar minoxidil y finasterida?","Es una combinación habitual porque actúan por vías distintas y complementarias, pero debe indicarla y supervisarla tu médico según tu caso."),
 ],
)

# =====================================================================
# 10) PRP, MESOTERAPIA, EXOSOMAS
# =====================================================================
article(
 meta=dict(
   title="PRP, mesoterapia y exosomas: qué funciona de verdad (y qué es placebo)",
   slug="prp-mesoterapia-exosomas-tratamientos-capilares",
   related=[('Minoxidil y finasterida', 'minoxidil-finasterida-como-funcionan-mitos'), ('Nutrición y cabello', 'nutricion-y-cabello-vitaminas-que-importan')],
   category="Tratamientos",
   read_min=9,
   deck="Las terapias inyectables están de moda. Algunas tienen evidencia sólida como complemento; otras son, a efectos prácticos, agua cara. Te ayudamos a distinguirlas.",
   meta_desc="PRP, mesoterapia capilar, exosomas y polinucleótidos: qué son, cómo actúan, qué dice la evidencia y cuáles son placebo. Contenido educativo de Innovart Medical.",
   keywords="PRP capilar, mesoterapia capilar, exosomas pelo, polinucleótidos, dutasterida infiltrada, tratamientos capilares inyectables",
 ),
 lead="Hay un universo de tratamientos inyectables para el cabello, y el marketing los presenta a todos como milagrosos. La realidad médica es más matizada: la mayoría son complementos útiles —no sustitutos— del tratamiento de base, y dentro de ese grupo hay diferencias enormes de evidencia. Esto es lo que conviene saber antes de pagar por una sesión.",
 takeaway_items=[
   "Las terapias inyectables son <b>complemento</b>, no reemplazo del tratamiento oral o la cirugía.",
   "El <b>PRP</b> tiene eficacia baja-moderada y variable; su mejor nicho es frenar el efluvio activo.",
   "La <b>dutasterida infiltrada</b> es la mesoterapia con <b>más evidencia</b> en alopecia androgenética.",
   "Las “vitaminas” inyectadas son, a efectos prácticos, <b>placebo</b> (el beneficio viene del pinchazo).",
   "<b>Exosomas</b>: prometedores en laboratorio, pero aún sin ensayos robustos ni estandarización.",
 ],
 sections=[
  ("Antes de nada: complemento, no milagro",
   "<p>Conviene encuadrarlo bien: las terapias inyectables <strong>potencian</strong> un tratamiento de base, pero su potencia aislada es modesta. Esperar que un PRP por sí solo “cure” una alopecia androgenética activa es poner las expectativas en el lugar equivocado. Usadas con criterio, sin embargo, pueden aportar.</p>"
   +img("Detalle de procedimiento de mesoterapia capilar en cuero cabelludo con técnica estéril; entorno clínico premium, manos con guantes, enfoque profesional y respetuoso.",
        "Terapias inyectables capilares: un complemento del tratamiento de base")),
  ("PRP: plasma rico en plaquetas",
   "<p>Se obtiene de tu propia sangre, centrifugada para concentrar las plaquetas. Al activarse, estas liberan <strong>factores de crecimiento</strong> que, en teoría, estimulan las células madre foliculares, favorecen la formación de vasos y prolongan la fase de crecimiento. ¿La evidencia? En alopecia androgenética es <strong>baja a moderada y muy variable</strong>, lo que lo deja como opción para quienes no pueden o no quieren tomar medicación. Curiosamente, su nicho más útil parece ser <strong>frenar el efluvio telógeno crónico</strong> (la caída activa).</p>"),
  ("Mesoterapia: depende de qué se inyecte",
   "<p>Mesoterapia es simplemente inyectar sustancias en la dermis del cuero cabelludo. Y aquí el “qué” lo cambia todo:</p>"
   +table(["Qué se infiltra","Evidencia real"],
     [["Dutasterida","La de <b>mayor evidencia</b> en alopecia androgenética: añade un 10–15% extra de grosor cuando se suma al tratamiento oral."],
      ["“Vitaminas” / cócteles","A efectos prácticos, <b>placebo</b>. El leve beneficio viene del trauma de la aguja, no del cóctel."]])
   +pull("No preguntes solo “¿me hago mesoterapia?”. Pregunta “¿qué me van a infiltrar y qué evidencia tiene?”.")),
  ("Exosomas y polinucleótidos: la frontera",
   "<p>Son la punta de lanza de la medicina regenerativa, con perfiles muy distintos:</p>"
   +compare("Exosomas",
     ["Vesículas que transportan proteínas y ARN entre células.",
      "Resultados llamativos <b>en laboratorio</b>.",
      "En humanos: <b>sin ensayos robustos</b>, no estandarizados.",
      "Plantean dudas de seguridad según su origen."],
     "Polinucleótidos",
     ["Extractos purificados de ADN (a menudo de salmón).",
      "Muy seguros (no provocan rechazo).",
      "Acción antiinflamatoria y angiogénica.",
      "Eficacia <b>modesta</b> (similar al PRP); requieren mantenimiento."])
   +note("Que algo sea “lo último” no significa que sea lo más eficaz para ti. En medicina capilar, lo nuevo convive con lo prometedor-pero-no-probado. Conviene elegir con datos.")),
  ("Cómo lo usamos con criterio",
   "<p>En Innovart Medical integramos las terapias inyectables dentro de un plan, no como producto suelto. De hecho, nuestro acompañamiento postoperatorio incluye controles y mesoterapia durante el primer año para cuidar el resultado. La regla es simple: <strong>cada terapia, en el paciente correcto, por la razón correcta</strong> —y siempre como complemento de un tratamiento de base bien indicado.</p>"),
 ],
 faq_pairs=[
  ("¿El PRP sirve para la calvicie?","Como complemento puede ayudar, sobre todo para frenar caída activa, pero su efecto sobre la alopecia androgenética es limitado y variable. No sustituye al tratamiento médico de base."),
  ("¿Cada cuánto hay que repetir estas terapias?","Casi todas requieren mantenimiento (por ejemplo, polinucleótidos cada 6–12 meses), porque su efecto se desvanece con el tiempo. Eso forma parte del cálculo de coste-beneficio."),
  ("¿Los exosomas son seguros?","Los de origen humano plantean dudas de seguridad y aún faltan ensayos sólidos. Hoy se consideran experimentales. Pregunta siempre por el origen y la evidencia."),
 ],
)

# =====================================================================
# 11) SHEDDING
# =====================================================================
article(
 meta=dict(
   title="Shedding: por qué se te cae MÁS pelo al empezar el tratamiento",
   slug="shedding-caida-al-empezar-tratamiento",
   related=[('¿Cuántos años dura un injerto capilar?', 'cuantos-anos-dura-un-injerto-capilar'), ('Minoxidil y finasterida', 'minoxidil-finasterida-como-funcionan-mitos'), ('PRP y tratamientos capilares', 'prp-mesoterapia-exosomas-tratamientos-capilares')],
   category="Tratamientos",
   read_min=6,
   deck="Empiezas a tratarte… y se te cae más pelo. Antes de entrar en pánico y abandonar, entiende por qué eso suele ser una excelente señal.",
   meta_desc="Qué es el shedding capilar, por qué el minoxidil provoca más caída al inicio, cuánto dura y por qué es un signo de buen pronóstico. Explicado por Innovart Medical.",
   keywords="shedding capilar, caída inicial minoxidil, efluvio telógeno agudo, fase anágena, tratamiento alopecia",
 ),
 lead="Es uno de los momentos que más pacientes hace abandonar el tratamiento, justo cuando está empezando a funcionar. Comienzas con minoxidil, pasan un par de semanas y, en lugar de mejorar, se te cae más pelo. La reacción instintiva —dejarlo— es exactamente la peor decisión. Te explicamos qué está pasando.",
 takeaway_items=[
   "El shedding es un <b>efluvio telógeno agudo</b>: una caída temporal al iniciar tratamientos estimuladores.",
   "Ocurre porque el fármaco <b>acelera la salida</b> de los pelos viejos para dar paso a pelos nuevos.",
   "Suele empezar <b>a las 2 semanas</b>, llega a su pico hacia la 4ª y baja sobre la 6ª.",
   "Es un <b>marcador de buen pronóstico</b>: tus folículos están respondiendo, no muriendo.",
   "La peor decisión es <b>asustarse y suspender</b>: la caída se autolimita sola.",
 ],
 sections=[
  ("Qué es exactamente el shedding",
   "<p>El <em>shedding</em> es un <strong>efluvio telógeno agudo</strong>: un aumento paradójico de la caída al iniciar tratamientos que estimulan el folículo, sobre todo el minoxidil (especialmente el tópico). Dicho de otro modo: el pelo se cae <strong>porque el tratamiento empezó a trabajar</strong>, no porque esté fallando.</p>"),
  ("Por qué ocurre: una cuestión de sincronización",
   "<p>En tu cuero cabelludo, los pelos están en fases distintas y desincronizadas. Cuando un pelo entra en fase de caída (telógena), no se desprende al instante: tarda entre 2 y 4 meses. El minoxidil envía una <strong>orden de aceleración metabólica</strong> al folículo y obliga a esos pelos que ya estaban “de salida” a <strong>acortar su fase telógena y caer rápido</strong>, para dejar sitio a un pelo nuevo en fase de crecimiento. Lo que ves caer es, en realidad, el relevo.</p>"
   +img("Infografía del relevo folicular: un pelo viejo y fino cayendo mientras emerge uno nuevo y grueso desde el mismo folículo; estilo editorial limpio, teal/dorado.",
        "El shedding es el relevo: cae el pelo viejo para dar paso al nuevo")),
  ("El cronograma: cuánto dura",
   "<p>Saber los plazos evita el pánico:</p>"
   +timeline([
     ("Semana ~2","Empieza","La caída suele iniciarse a partir de los 14 días; puedes perder 20–30 pelos extra al día."),
     ("Semana ~4","Pico","Alcanza su punto máximo. Es la fase más angustiante… y la más temporal."),
     ("Semana ~6","Disminuye","Empieza a remitir. A partir de aquí la caída se vuelve incluso menor que antes de empezar."),
   ])),
  ("Por qué es una buena noticia",
   "<p>Aunque parezca contradictorio, el shedding es un <strong>signo de muy buen pronóstico</strong>. Significa que tus folículos <strong>no están muertos ni senescentes</strong>: están respondiendo con fuerza y “despertando”. Los pelos que caen son reemplazados en los meses siguientes por cabellos más gruesos y sanos.</p>"
   +pull("El shedding no es el tratamiento fallando. Es el tratamiento empezando a funcionar.")
   +note("Si suspendes por miedo justo en esta fase, interrumpes el relevo y pierdes el beneficio. Ante la duda, consulta con tu médico antes de abandonar: casi siempre la indicación es continuar.")),
 ],
 faq_pairs=[
  ("¿Todo el mundo tiene shedding?","No todos lo notan, y es más frecuente y visible con minoxidil tópico. Su ausencia tampoco significa que el tratamiento no funcione."),
  ("¿Y si la caída no para después de 2 meses?","Si la caída se prolonga mucho más allá de lo esperado, conviene revisarlo con tu médico para descartar otras causas (ferritina, tiroides, dosis o formato inadecuados)."),
  ("¿El shedding también pasa con la finasterida?","Puede haber una caída inicial leve, pero el fenómeno clásico e intenso se asocia sobre todo al minoxidil. En ambos casos, la recomendación general es no suspender por la caída inicial."),
 ],
)

# =====================================================================
# 12) ESTRÉS Y CAÍDA
# =====================================================================
article(
 meta=dict(
   title="Estrés y caída del cabello: la conexión que no deberías ignorar",
   slug="estres-y-caida-del-cabello",
   related=[('Alopecia androgénetica', 'alopecia-androgenetica-por-que-se-cae-el-pelo'), ('Nutrición y cabello', 'nutricion-y-cabello-vitaminas-que-importan')],
   category="Salud capilar",
   read_min=8,
   deck="El estrés no “inventa” una calvicie que no tenías, pero sí puede ser la gasolina que la acelera. Te explicamos el mecanismo real, sin dramatismos.",
   meta_desc="Cómo el estrés afecta al cabello: efluvio telógeno, cortisol, inflamación neurógena y por qué la caída aparece 2-4 meses después. Explicado por Innovart Medical.",
   keywords="estrés caída del cabello, efluvio telógeno, cortisol pelo, inflamación neurógena, estrés y alopecia",
 ),
 lead="“Se me cae el pelo del estrés” es una frase que escuchamos a diario. A veces es una excusa fácil; a veces es literalmente cierto. La biología detrás es más fina de lo que parece: el estrés agudo y el crónico afectan al pelo por vías distintas, y entender cuál es la tuya cambia el abordaje.",
 takeaway_items=[
   "El estrés <b>agudo</b> dispara un efluvio telógeno: caída difusa <b>2–4 meses después</b> del evento.",
   "El estrés <b>crónico</b> eleva el cortisol y mantiene una <b>inflamación de bajo grado</b>.",
   "La <b>inflamación neurógena</b> (sustancia P, mastocitos) ataca el folículo y cronifica la caída.",
   "El estrés <b>no causa</b> la calvicie genética, pero la <b>acelera</b>.",
   "También empeora la areata, la dermatitis seborreica y favorece las canas.",
 ],
 sections=[
  ("Estrés agudo: el efluvio que llega tarde",
   "<p>Un evento traumático (una cirugía, una pérdida, una enfermedad, un parto) libera de golpe hormonas del estrés que impactan el ciclo del pelo. Empuja a un porcentaje alto de folículos a entrar prematuramente en fase de reposo y caída. Pero —y esto desconcierta a casi todos— <strong>la caída masiva no es inmediata: aparece entre 2 y 4 meses después</strong> del evento. Por eso muchas personas no relacionan la caída con lo que vivieron un trimestre atrás.</p>"
   +note("Si tu pelo se cae “sin razón”, repasa qué pasó hace 2–4 meses. El desencadenante casi siempre está ahí.")),
  ("Estrés crónico: el cortisol que no baja",
   "<p>El estrés sostenido mantiene activado el eje del cortisol. Ese exceso crónico favorece un estado de <strong>oxidación e inflamación de bajo grado</strong> en todo el cuerpo. Esa inflamación actúa como un <strong>acelerador del envejecimiento celular</strong>: propicia canas (por daño a los melanocitos) y empeora el pronóstico de enfermedades como la alopecia areata o la dermatitis seborreica.</p>"
   +img("Imagen conceptual y serena de una persona con expresión de tensión sostenida, iluminación editorial; evoca estrés crónico sin caer en el cliché, paleta sobria.",
        "El estrés crónico mantiene una inflamación de bajo grado que afecta al folículo")),
  ("Inflamación neurógena: cuando los nervios atacan al folículo",
   "<p>Hay un mecanismo más fino y fascinante. El estrés crónico altera las terminaciones nerviosas que llegan al folículo, que empiezan a liberar neuropéptidos proinflamatorios como la <strong>sustancia P</strong>. Estas moléculas activan los mastocitos, liberan histamina y reclutan glóbulos blancos que <strong>atacan el pelo y cronifican la caída</strong>. No es “estar nervioso”: es una cascada inflamatoria real alrededor de la raíz.</p>"
   +pull("El estrés no se imagina la caída del pelo. La fabrica, a través de una cascada inflamatoria muy concreta.")),
  ("El matiz clave para la calvicie común",
   "<p>Importante no exagerar: el estrés <strong>por sí solo no causa la alopecia androgenética</strong>. Pero esa microinflamación neurógena y oxidativa actúa como <strong>gasolina sobre la base genética</strong>, haciendo que la calvicie común coja más velocidad y empeore más rápido de lo que “tocaría”. Es decir: el estrés no enciende el fuego genético, pero lo aviva.</p>"),
  ("Qué puedes hacer",
   "<p>El abordaje es doble. Por un lado, <strong>gestionar la causa</strong> (sueño, ejercicio, manejo del estrés) reduce el combustible inflamatorio. Por otro, si hay una alopecia de base, el estrés es una razón más para <strong>diagnosticar y tratar a tiempo</strong>, porque sobre un terreno genético la caída acelerada hace más daño. Si la caída es brusca y difusa, conviene valorar también ferritina y tiroides, que suelen acompañar a estos cuadros.</p>"),
 ],
 faq_pairs=[
  ("¿El pelo que pierdo por estrés vuelve a salir?","En el efluvio telógeno por estrés agudo, sí: suele ser transitorio y el pelo se recupera al cesar el desencadenante. El problema es cuando el estrés crónico se suma a una alopecia genética de base."),
  ("¿Cuánto tarda en recuperarse?","Tras controlar el factor estresante, la recuperación suele tomar varios meses, en línea con el propio ciclo del pelo. La paciencia y descartar otras causas son clave."),
  ("¿Los suplementos anti-estrés ayudan al pelo?","Lo que ayuda es reducir el estrés real y corregir déficits si los hay (hierro, vitamina D). Suplementar sin medir rara vez aporta y puede despistar el diagnóstico."),
 ],
)

print("Batch 3 listo.")
