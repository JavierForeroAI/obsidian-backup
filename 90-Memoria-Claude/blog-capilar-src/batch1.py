# -*- coding: utf-8 -*-
from innovart_template import *

# =====================================================================
# 1) ALOPECIA ANDROGENÉTICA
# =====================================================================
article(
 meta=dict(
   title="Alopecia androgenética: por qué se cae el pelo (y qué la acelera)",
   slug="alopecia-androgenetica-por-que-se-cae-el-pelo",
   category="Ciencia capilar",
   read_min=9,
   deck="No es un exceso de hormonas: es la sensibilidad genética de tu folículo a la DHT. Te explicamos, con criterio médico, el mecanismo real de la calvicie común y por qué actuar a tiempo lo cambia todo.",
   meta_desc="Qué es la alopecia androgenética, el papel de la DHT y la 5-alfa-reductasa, cómo se hereda la calvicie y a qué velocidad avanza. Explicado por el equipo médico de Innovart Medical.",
   keywords="alopecia androgenética, DHT, 5-alfa-reductasa, miniaturización, herencia calvicie, caída del cabello",
 ),
 lead="La alopecia androgenética es la causa de más del 90% de la pérdida de cabello en hombres y de buena parte de la caída en mujeres. Y, sin embargo, casi todo lo que se cuenta sobre ella es impreciso. No se cae el pelo por usar gorra, por estrés aislado ni por tener “demasiada testosterona”. Se cae porque algunos folículos heredaron una hipersensibilidad a una hormona concreta. Entender ese mecanismo es el primer paso para frenarlo.",
 takeaway_items=[
   "La calvicie común no es exceso de hormonas, sino <b>exceso de sensibilidad</b> del folículo a niveles hormonales normales.",
   "La enzima <b>5-alfa-reductasa</b> convierte la testosterona en <b>DHT</b>, la hormona que ordena al folículo miniaturizarse.",
   "Sin tratamiento, la alopecia avanza <b>un grado en la escala de Norwood cada 4,5–5 años</b>.",
   "Si no se frena a tiempo, la miniaturización termina en <b>fibrosis: cicatrización irreversible</b>.",
   "Paradoja clave: los más jóvenes pierden pelo más rápido, pero también son <b>quienes mejor responden al tratamiento</b>.",
 ],
 sections=[
  ("El mecanismo real: DHT, 5-alfa-reductasa y receptor androgénico",
   "<p>El motor de la alopecia androgenética no es la cantidad de hormona en sangre, sino <strong>qué hace tu folículo con ella</strong>. Dentro del folículo, la enzima <strong>5-alfa-reductasa</strong> (sobre todo el tipo 2) transforma la testosterona en <strong>dihidrotestosterona (DHT)</strong>, un andrógeno mucho más potente y con una afinidad extrema por el receptor de hormonas masculinas.</p>"
   "<p>La DHT se une a ese receptor en el núcleo de las células foliculares. Y aquí entra la genética: la fuerza de esa unión depende del número de <strong>repeticiones “CAG”</strong> en el gen del receptor androgénico. A menos repeticiones, <strong>más hipersensible es el receptor</strong> y más temprana y agresiva tiende a ser la calvicie. Por eso dos personas con la misma testosterona pueden tener destinos capilares opuestos.</p>"
   +img("Ilustración 3D limpia de un folículo piloso en corte transversal, mostrando la conversión de testosterona a DHT y la unión al receptor. Estilo editorial médico, paleta teal y dorado sobre fondo claro.",
        "Esquema del folículo piloso: testosterona convertida en DHT por la 5-alfa-reductasa")),
  ("Miniaturización: cómo el pelo se vuelve invisible",
   "<p>Cuando la DHT activa un receptor hipersensible, envía a la célula una orden de <strong>apoptosis</strong> (muerte celular programada). La fase de crecimiento (anágena) se acorta ciclo tras ciclo, y el cabello que asoma es cada vez <strong>más fino, más corto y más claro</strong>, hasta parecer un simple vello. A esto lo llamamos miniaturización, y es el verdadero corazón de la alopecia: el folículo no “muere” de golpe, se encoge.</p>"
   +pull("La calvicie no empieza con un pelo que se cae. Empieza con un pelo que se vuelve más fino y deja de notarse.")
   +"<p>Hay un matiz que muchos desconocen: la miniaturización no es solo hormonal. Los andrógenos y el estrés oxidativo generan una <strong>microinflamación silenciosa y crónica</strong> alrededor del folículo. Si no se detiene, las células foliculares sufren una transición hacia tejido cicatricial (fibrosis). En ese punto, <strong>el pelo ya no puede volver a crecer</strong>. Por eso la ventana de oportunidad importa tanto.</p>"),
  ("¿De quién se hereda la calvicie? El mito materno, revisado",
   "<p>“Mira a tu abuelo materno” tiene una base real, pero es una verdad a medias. El gen del receptor de andrógenos (gen AR) está en el <strong>cromosoma X</strong>, que los hombres heredan obligatoriamente de su madre. Si el abuelo materno es calvo, hay una probabilidad relevante de haber heredado esa sensibilidad.</p>"
   "<p>Pero la calvicie es <strong>poligénica</strong>: intervienen más de 300 genes, con cerca de un 80% de heredabilidad, y muchos de ellos se heredan <strong>tanto del padre como de la madre</strong>. Los datos son claros sobre el riesgo acumulado:</p>"
   +table(["Antecedente familiar","Efecto sobre tu riesgo"],
     [["Padre con calvicie","Riesgo multiplicado ~2,5 veces"],
      ["Abuelo materno calvo","Mayor probabilidad de heredar el receptor hipersensible (vía cromosoma X)"],
      ["Padre + abuelo materno calvos","Riesgo extremo: alopecia importante y muy precoz"]])
   +note("Tener antecedentes no es una sentencia. Es justo la información que permite <b>actuar antes</b> de que la miniaturización avance hacia la fibrosis.")),
  ("¿A qué velocidad avanza? El reloj de la alopecia",
   "<p>La alopecia androgenética es progresiva, pero no lineal. En cohortes amplias se observa que, <strong>sin ningún tratamiento, empeora un grado entero en la escala Hamilton-Norwood cada 4,5 a 5 años</strong>. Es decir, un joven con grado 1 a los 20 puede estar en grado 3 a los 30.</p>"
   +stats([("4,5–5","años por cada grado de Norwood sin tratar"),("18–25","la franja de pérdida más agresiva"),("80%","heredabilidad estimada de la calvicie")])
   +"<p>La presión genética y hormonal es máxima entre los 18 y los 25 años; ahí la caída puede ser galopante. Con la edad, esa “fuerza” destructiva decrece: un hombre de 78 seguirá perdiendo pelo, pero mucho más despacio que uno de 22. La contracara es importante: pasados los 50–60 años el folículo entra en <strong>senescencia</strong> y responde peor a la medicación, mientras que entre los 20 y los 40 la respuesta puede ser casi espectacular.</p>"
   "<p>Además existen <strong>brotes de aceleración</strong>: el estrés sostenido, el tabaquismo o una mala higiene capilar (dermatitis seborreica) actúan como gasolina y empujan al folículo a miniaturizarse mucho antes de esos “5 años por grado”.</p>"
   +img("Comparativa visual elegante de la escala Hamilton-Norwood (grados I a VII) en silueta masculina, minimalista, línea fina dorada sobre fondo crema.",
        "Escala Hamilton-Norwood de progresión de la alopecia androgenética")),
  ("Qué puedes hacer hoy",
   "<p>La buena noticia es que la alopecia androgenética es de las condiciones que <strong>mejor responden cuando se diagnostica a tiempo</strong>. El abordaje médico (que tu médico definirá tras valorarte) busca tres cosas: frenar la conversión a DHT, prolongar la fase de crecimiento y apagar esa microinflamación. Y cuando ya hay zonas sin folículos viables, la microcirugía capilar permite redistribuir tu propio cabello resistente.</p>"
   "<p>En Innovart Medical no empezamos por la solución, empezamos por el <strong>diagnóstico</strong>: medimos el calibre real de tu pelo con dermatoscopia y diseñamos un plan a tu medida. Lo que no se mide, no se puede frenar.</p>"),
 ],
 faq_pairs=[
  ("¿La testosterona alta causa calvicie?","No directamente. La calvicie depende de la <strong>sensibilidad genética</strong> del folículo a la DHT, no de cuánta testosterona tengas en sangre. Por eso pedir niveles de testosterona para estudiar la calvicie común en hombres suele ser poco útil."),
  ("¿La alopecia androgenética tiene cura?","Hoy no hablamos de “cura”, sino de <strong>control</strong>. Con tratamiento médico se puede frenar y revertir parcialmente la miniaturización, y con microcirugía capilar se restaura la cobertura. La clave es no dejar que avance hasta la fibrosis."),
  ("Tengo 22 años y ya tengo entradas, ¿es grave?","Es la edad de mayor velocidad de pérdida, pero también la de mejor respuesta al tratamiento. Lo importante es valorarte cuanto antes para no perder folículos recuperables."),
  ("¿Es verdad que se hereda solo de la madre?","No. La vía materna (cromosoma X) pesa, pero la calvicie es poligénica y también se hereda del padre. El mayor riesgo aparece cuando hay antecedentes en ambas ramas."),
 ],
)

# =====================================================================
# 2) SEÑALES TEMPRANAS
# =====================================================================
article(
 meta=dict(
   title="5 señales tempranas de que estás perdiendo el pelo (y cuándo actuar)",
   slug="senales-tempranas-perdida-de-pelo",
   category="Diagnóstico",
   read_min=8,
   deck="Cuando el espejo te avisa, la miniaturización ya lleva tiempo trabajando. Aprende a leer las señales que aparecen antes de que el cuero cabelludo se note.",
   meta_desc="Cómo detectar la caída del cabello a tiempo: afinamiento, ensanchamiento de la raya, entradas, exceso de grasa y picor. El valor de la dermatoscopia. Por Innovart Medical.",
   keywords="señales caída del pelo, miniaturización, ensanchamiento de raya, entradas, tricoscopia, dermatoscopia capilar",
 ),
 lead="La alopecia androgenética no empieza con mechones en la almohada. Empieza mucho antes, de forma silenciosa, con folículos que se afinan sin que tú lo percibas. Para cuando “se ve” el cuero cabelludo, una parte del trabajo ya está hecha. Estas son las señales que un ojo entrenado detecta primero.",
 takeaway_items=[
   "La señal inicial no es la caída, es la <b>miniaturización</b>: el pelo se vuelve más fino, no necesariamente más escaso.",
   "El <b>ensanchamiento de la raya</b> es la primera pista en mujeres y en patrón femenino.",
   "Que una entrada esté peor que la otra <b>es normal</b> (la derecha suele ser ~23% más acusada).",
   "El <b>exceso de grasa y el picor</b> no causan calvicie, pero la aceleran.",
   "Solo la <b>dermatoscopia</b> mide el daño real: a simple vista llegas tarde.",
 ],
 sections=[
  ("1. Tu pelo se vuelve más fino (aunque no se caiga más)",
   "<p>La clave de la alopecia androgenética no es perder pelos, sino que los pelos <strong>se encogen</strong>. Un cabello sano mide más de 70–80 micras de grosor; uno miniaturizado baja de 50–60. Ese afinamiento progresivo hace que la melena pierda cuerpo y densidad óptica mucho antes de que aparezcan zonas despobladas. Si notas que tu pelo “ya no es el de antes” aunque la cantidad parezca similar, presta atención.</p>"),
  ("2. La raya del peinado se ensancha",
   "<p>En mujeres —y en hombres con patrón femenino— la primera línea frontal suele conservarse, pero el pelo se afina de forma difusa en la zona central. El resultado visible es un <strong>ensanchamiento progresivo de la raya</strong>: cada vez se ve un poco más de cuero cabelludo al peinarte. Es una de las señales más fiables y más fáciles de ignorar.</p>"
   +img("Foto cenital de una raya del cabello con apertura sutil, iluminación suave de estudio, tono editorial y respetuoso (sin dramatizar). Persona real, primer plano del cuero cabelludo.",
        "Ensanchamiento progresivo de la raya del peinado como señal temprana de alopecia")),
  ("3. Las entradas retroceden… y de forma asimétrica",
   "<p>El retroceso de la línea frontal y las entradas es el patrón clásico masculino. Muchos pacientes se alarman al ver que <strong>una entrada está peor que la otra</strong>. Tranquilidad: es completamente normal. La recesión de la entrada derecha suele ser cerca de un 23% más marcada que la izquierda, posiblemente por la arquitectura individual del folículo o por factores mecánicos como dormir apoyado sobre ese lado.</p>"
   +note("Una asimetría leve no indica una enfermedad rara. Pero un cambio brusco o muy desigual sí merece valoración para descartar otras causas.")),
  ("4. Exceso de grasa, caspa y picor",
   "<p>La misma sensibilidad hormonal que miniaturiza el pelo <strong>hiperactiva las glándulas sebáceas</strong>. Ese exceso de sebo alimenta al hongo <em>Malassezia</em>, que dispara microinflamación, descamación y picor. Por sí solos, la grasa y el picor no producen calvicie, pero funcionan como un <strong>acelerador inflamatorio</strong> que adelanta la miniaturización. Si conviven caída + grasa + picor, el reloj corre más rápido.</p>"),
  ("5. La prueba que de verdad importa: la dermatoscopia",
   "<p>Contar pelos en la almohada es engañoso: el pelo largo abulta más y simula caídas masivas falsas. La herramienta que cambia el juego es la <strong>tricoscopía o dermatoscopia</strong>, que permite:</p>"
   "<ul><li>Medir matemáticamente el <strong>calibre</strong> de cada cabello.</li>"
   "<li>Calcular el porcentaje de pelos miniaturizados y el ratio folicular.</li>"
   "<li>Detectar inflamación perifolicular, fibrosis o vasos anómalos que obligarían a cambiar de estrategia.</li></ul>"
   "<p>A simple vista es imposible cuantificar el daño. Por eso, cuando la pérdida “se nota” en el espejo, la miniaturización ya avanzó. La dermatoscopia te permite intervenir <strong>en la fase reversible</strong>.</p>"
   +img("Dermatoscopio digital apoyado sobre cuero cabelludo con pantalla mostrando folículos ampliados; entorno clínico limpio, profesional con guantes, paleta médica premium.",
        "Tricoscopía: dermatoscopia digital para medir el calibre del cabello")),
 ],
 faq_pairs=[
  ("¿Cuántos pelos al día es normal perder?","Perder entre 50 y 100 pelos al día está dentro de lo esperable. Lo relevante no es el número, sino si los pelos nuevos salen más finos (miniaturización) o si la caída se mantiene en el tiempo."),
  ("¿Puedo saber en casa si tengo alopecia?","Puedes sospecharla por estas señales, pero confirmarla y medir su gravedad requiere dermatoscopia. Una valoración profesional evita tanto la falsa alarma como la falsa tranquilidad."),
  ("Si actúo ahora, ¿puedo recuperar el pelo afinado?","Mientras el folículo siga vivo (miniaturizado pero no fibrosado), hay margen de recuperación con tratamiento médico. Esa es exactamente la razón para no esperar."),
 ],
)

# =====================================================================
# 3) BUEN CANDIDATO A INJERTO
# =====================================================================
article(
 meta=dict(
   title="¿Eres buen candidato para un injerto capilar? Tu zona donante decide",
   slug="buen-candidato-injerto-capilar-zona-donante",
   category="Cirugía capilar",
   read_min=9,
   deck="El éxito de un trasplante no se ve en la zona calva, se calcula en la zona donante. Te explicamos qué evalúa de verdad un cirujano antes de operar.",
   meta_desc="Qué define a un buen candidato para injerto capilar: densidad de la zona donante, calibre del pelo, ratio folicular, color y estabilidad médica. Explicado por Innovart Medical.",
   keywords="candidato injerto capilar, zona donante, valor de cobertura, ratio folicular, calibre del pelo, trasplante capilar",
 ),
 lead="Hay una idea equivocada muy extendida: que cualquiera con calvicie puede operarse y “rellenarse” la cabeza. La realidad es más exigente y más honesta. El trasplante capilar redistribuye un recurso limitado —tu propio pelo resistente— y no todos los pacientes parten de las mismas condiciones. Esto es lo que un cirujano serio mide antes de prometerte nada.",
 takeaway_items=[
   "Un buen candidato se define por la <b>zona donante</b>, no por la zona calva.",
   "El factor más determinante es el <b>calibre (grosor) del pelo</b>: el cabello grueso cubre mucho más.",
   "El <b>ratio folicular</b> (pelos por unidad) y el <b>contraste pelo/piel</b> cambian el resultado óptico.",
   "El mejor candidato tiene su alopecia <b>estabilizada con tratamiento médico previo</b>.",
   "Un menor de 25 años con pérdida agresiva y sin tratamiento es, casi siempre, un <b>mal candidato</b> todavía.",
 ],
 sections=[
  ("El concepto clave: “valor de cobertura”",
   "<p>El cirujano no cuenta solo cuántos folículos puede extraer; calcula el <strong>valor de cobertura</strong>, una relación que combina el calibre del pelo con el ratio folicular. Dicho simple: <strong>no es lo mismo tener muchos folículos finos que tener folículos gruesos y multifibrosos</strong>. Dos pacientes con el mismo número de injertos disponibles pueden lograr coberturas radicalmente distintas.</p>"
   +img("Infografía editorial mostrando una unidad folicular con 1, 2, 3 y 4 pelos saliendo del mismo punto; etiquetas limpias, paleta teal/dorado, estilo médico premium.",
        "Unidades foliculares de 1 a 4 pelos: el ratio folicular determina la cobertura")),
  ("El factor decisivo: el grosor de tu pelo",
   "<p>Es, de lejos, el dato más importante. Un cabello grueso (más de 70–80 micras) cubre mucha más superficie y necesita menos densidad de injertos para tapar el cuero cabelludo. Un cabello fino (menos de 50 micras) exige muchísimos más folículos para el mismo efecto visual. Por eso un paciente de pelo grueso puede tener un resultado espectacular con relativamente pocos injertos.</p>"),
  ("Ratio folicular, color y tipo de pelo",
   "<p>Tres factores ópticos terminan de definir el resultado:</p>"
   +table(["Factor","Favorece la cobertura cuando…"],
     [["Ratio folicular","Las unidades tienen 2,5–3 pelos de media (mejor que 1,8)"],
      ["Contraste pelo/piel","El contraste es <b>bajo</b> (pelo oscuro sobre piel morena; o pelo claro sobre piel clara)"],
      ["Forma del pelo","Es ondulado o rizado: aporta más volumen y disimula los espacios"]])
   +"<p>El contraste alto —pelo muy oscuro sobre piel muy blanca— hace más visibles los huecos entre cabellos, así que exige diseños y densidades más cuidadosos.</p>"),
  ("La zona donante: un recurso que no se regenera",
   "<p>Los folículos se extraen de la <strong>zona donante segura</strong> (occipital y parieto-temporal), genéticamente programada para resistir la DHT. Pero es un banco finito. El cirujano evalúa que tenga <strong>alta densidad y sin signos de miniaturización</strong> para poder extraer sin dejar clareos visibles. Vaciar de más esa zona —el temido <em>overharvesting</em>— arruina el aspecto del paciente de por vida.</p>"
   +pull("El trasplante no crea pelo nuevo: redistribuye el que ya tienes. Cuidar la zona donante es cuidar tu futuro.")),
  ("Estabilidad médica: el requisito que muchas clínicas saltan",
   "<p>El candidato ideal tiene su alopecia <strong>frenada con tratamiento médico</strong> antes de operarse. ¿Por qué? Porque si operamos un pelo que sigue cayendo, en pocos años quedará un mechón injertado rodeado de zonas que el paciente sigue perdiendo. Un menor de 25 años con caída agresiva y sin tratamiento previo <strong>no es un buen candidato aún</strong>: primero hay que estabilizar y conocer su patrón real de pérdida.</p>"
   +note("En Innovart Medical, una clínica ética te dirá si <b>todavía no</b> es tu momento de operarte. Eso también es cuidar tu resultado.")),
 ],
 faq_pairs=[
  ("¿Hay una edad mínima para el injerto?","No es cuestión de edad exacta, sino de estabilidad. Operar muy joven sin tratamiento previo suele dar malos resultados a medio plazo. Lo habitual es estabilizar primero la caída."),
  ("¿Y si mi zona donante es débil?","Existen protocolos de fortalecimiento previo de la zona donante. En algunos casos se puede mejorar su densidad antes de planificar la cirugía; en otros, el trasplante no está indicado y conviene saberlo a tiempo."),
  ("¿Las mujeres pueden ser candidatas?","Sí, pero el estudio es distinto: hay que descartar causas hormonales y nutricionales, y valorar el patrón de caída. Muchas mujeres se benefician más del tratamiento médico que de la cirugía."),
  ("¿Cuántos folículos voy a necesitar?","Depende de tu calibre, ratio y superficie a cubrir. Por eso no damos cifras por foto ni por WhatsApp: se calcula en valoración con dermatoscopia."),
 ],
)

# =====================================================================
# 4) FUE vs DHI
# =====================================================================
article(
 meta=dict(
   title="FUE vs DHI: qué técnica de injerto capilar elegir (sin marketing)",
   slug="fue-vs-dhi-que-tecnica-elegir",
   category="Cirugía capilar",
   read_min=8,
   deck="Te han vendido FUE y DHI como si fueran rivales. No lo son: una es cómo se extrae el pelo y la otra cómo se implanta. Te lo explicamos sin humo.",
   meta_desc="Diferencias reales entre FUE y DHI, qué es el zafiro y el Choi pen, ventajas de cada técnica y cómo elegir. Explicado con criterio médico por Innovart Medical.",
   keywords="FUE vs DHI, injerto capilar, zafiro, Choi pen, técnica trasplante capilar, implantes capilares",
 ),
 lead="Pocas decisiones generan tanta confusión —y tanto marketing— como elegir entre FUE y DHI. La verdad, dicha con honestidad médica, desinfla buena parte del debate: no compiten entre sí, porque describen pasos distintos del mismo procedimiento. Aclararlo te protege de clínicas que cobran de más por “tecnologías” que en realidad son nombres comerciales.",
 takeaway_items=[
   "<b>FUE</b> describe la <b>extracción</b> folicular (uno a uno con micropunch).",
   "<b>DHI</b> describe la <b>implantación</b> con un dispositivo tipo bolígrafo (Choi pen).",
   "<b>“Zafiro”</b> es el material de las cuchillas de incisión, no una técnica aparte.",
   "Ninguna técnica es mágicamente superior: importa la <b>pericia del cirujano</b>.",
   "Lo que define tu resultado es el <b>diseño, la densidad y la supervivencia del folículo</b>, no la sigla.",
 ],
 sections=[
  ("Primero, desmontemos la confusión",
   "<p>Vamos a lo importante: <strong>FUE (Follicular Unit Extraction)</strong> es únicamente la forma de <strong>extraer</strong> el pelo, sacando cada unidad folicular con un microbisturí cilíndrico (punch). Lo que el marketing llama <strong>DHI (Direct Hair Implantation)</strong> se refiere a la forma de <strong>implantar</strong>, usando un dispositivo tipo bolígrafo (el famoso Choi pen). Por eso comparar “FUE vs DHI” es como comparar “conducir vs aparcar”: son fases, no equipos rivales.</p>"
   +img("Diagrama editorial de dos pasos: a la izquierda extracción FUE con micropunch, a la derecha implantación con Choi pen. Líneas limpias, paleta teal/dorado, estilo infografía médica.",
        "FUE describe la extracción; DHI describe la implantación")),
  ("Cómo se implanta: incisión previa vs implanter",
   "<p>Hay dos grandes formas de colocar los folículos:</p>"
   +compare("Incisiones + colocación (estilo “FUE clásico”)",
     ["El cirujano hace primero todas las incisiones receptoras…",
      "…con cuchillas (de ahí el término “zafiro”) o agujas.",
      "Luego se insertan los folículos con pinzas.",
      "Permite juntar mucho las incisiones para <b>densidades muy altas</b> (&gt;50 unidades/cm²)."],
     "Implanter / Choi pen (estilo “DHI”)",
     ["El dispositivo hace la incisión y deposita el folículo <b>en un solo movimiento</b>.",
      "Más fácil de estandarizar para el equipo.",
      "Puede <b>reducir la manipulación</b> del folículo.",
      "A veces dificulta densidades extremas por el efecto <em>popping</em>."])
   +"<p>El “zafiro” solo describe el material de las cuchillas (cristal de zafiro), que permite incisiones más finas. No es una técnica distinta: es un detalle de instrumental.</p>"),
  ("¿Cuál es mejor para ti?",
   "<p>La respuesta honesta: <strong>la que el cirujano domine mejor</strong>. Manos expertas logran densidades excelentes con ambos métodos. La elección depende del caso —líneas frontales y zonas que conviene no rapar suelen beneficiarse del implanter; superficies amplias y densidades altas, de las incisiones previas— y, sobre todo, de la experiencia del equipo.</p>"
   +pull("La sigla de moda no operará tu cabeza. Lo hará un cirujano. Elige por el equipo, no por el acrónimo.")),
  ("Lo que de verdad decide tu resultado",
   "<p>Más allá de FUE o DHI, tu resultado depende de variables que casi nunca aparecen en los anuncios:</p>"
   "<ul><li><strong>Diseño de la línea frontal:</strong> natural, con irregularidades y densidad progresiva, acorde a tu edad.</li>"
   "<li><strong>Supervivencia del folículo:</strong> cuanto menos tiempo pasa fuera del cuerpo, mejor.</li>"
   "<li><strong>Manejo de la zona donante:</strong> extracción homogénea, sin clareos.</li>"
   "<li><strong>Sesiones responsables:</strong> sin megasesiones que asfixian los injertos.</li></ul>"
   "<p>En Innovart Medical elegimos la técnica <strong>en función de tu caso</strong>, no de una etiqueta de marketing, y lo definimos contigo en la valoración.</p>"),
 ],
 faq_pairs=[
  ("¿El DHI deja menos cicatriz que el FUE?","Ambos parten de extracción folicular (FUE), que deja puntos diminutos en lugar de una línea. La cicatriz depende del buen manejo de la zona donante, no de cómo se implante después."),
  ("¿El DHI permite no raparse?","El implanter facilita injertar entre pelo existente, útil en retoques o en mujeres. Pero en cirugías grandes, no rapar complica el procedimiento y puede afectar la supervivencia del folículo."),
  ("¿Por qué algunas clínicas cobran más por “zafiro” o “DHI”?","A veces es marketing. El zafiro y el Choi pen son instrumentos válidos, pero no justifican por sí solos un sobreprecio enorme. Pregunta siempre qué incluye realmente tu plan."),
 ],
)

print("Batch 1 listo.")
