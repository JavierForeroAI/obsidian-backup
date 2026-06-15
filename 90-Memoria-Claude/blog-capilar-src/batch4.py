# -*- coding: utf-8 -*-
from innovart_template import *

# =====================================================================
# 13) NUTRICIÓN Y CABELLO
# =====================================================================
article(
 meta=dict(
   title="Nutrición y cabello: qué vitaminas importan de verdad (y cuáles no)",
   slug="nutricion-y-cabello-vitaminas-que-importan",
   category="Salud capilar",
   read_min=9,
   deck="El marketing te quiere vender un frasco. La ciencia dice que solo unos pocos nutrientes mueven la aguja, y casi siempre cuando ya hay un déficit. Te lo aclaramos.",
   meta_desc="Nutrición y caída del cabello: el papel real del hierro/ferritina, zinc, vitamina D, biotina y proteína, y qué analítica pedir. Por qué la biotina suele ser un mito. Por Innovart Medical.",
   keywords="nutrición cabello, ferritina caída pelo, biotina mito, zinc pelo, vitamina D cabello, analítica caída del pelo",
 ),
 lead="Pocos sectores prometen tanto como el de los suplementos “para el pelo”. La verdad médica es más aburrida y más útil: la nutrición tiene un impacto sobrevalorado por el marketing, pero ciertos déficits sí hunden la calidad del cabello. La clave no es tomar de todo, sino medir y corregir lo que de verdad falta.",
 takeaway_items=[
   "El nutriente más relacionado con la caída es el <b>hierro</b>: se mide por <b>ferritina</b>, no por hierro sérico.",
   "Las <b>dietas muy restrictivas o bajas en proteína</b> provocan efluvio telógeno.",
   "El <b>zinc</b> casi nunca está deficitario en dieta occidental; suplementarlo sin déficit no aporta.",
   "La <b>biotina es, en la práctica, un mito</b>: su déficit es rarísimo y puede <b>alterar analíticas</b>.",
   "El paso inteligente es una <b>analítica</b>, no un suplemento al azar.",
 ],
 sections=[
  ("La base: proteína y dietas extremas",
   "<p>El pelo se renueva a gran velocidad y está hecho de proteína (queratina). Por eso las dietas <strong>muy hipocalóricas</strong> (por debajo de 1.000–1.500 kcal) o <strong>bajas en proteína</strong> son nefastas: desencadenan un efluvio telógeno severo a los pocos meses. Antes de buscar el suplemento perfecto, asegúrate de no estar saboteando tu cabello con una dieta extrema.</p>"
   +img("Bodegón editorial de alimentos ricos en hierro y proteína (carnes magras, legumbres, huevos, espinacas) sobre superficie clara; estilo gastronómico premium y saludable.",
        "Una base nutricional suficiente en proteína y hierro sostiene el cabello")),
  ("Hierro y ferritina: el déficit que más importa",
   "<p>Es la deficiencia nutricional más relacionada con la caída, sobre todo en mujeres. Un matiz decisivo: la falta de hierro <strong>no produce calvicie</strong> (no miniaturiza), sino un <strong>efluvio telógeno crónico</strong>. Y el valor que hay que mirar no es el hierro en sangre, sino la <strong>ferritina</strong> (las reservas). Ferritinas por debajo de 20–30 ng/mL suelen requerir suplementación médica para frenar la caída.</p>"
   +pull("Te miden el hierro y “sale normal”, pero la ferritina está por el suelo. Ahí está, muchas veces, la respuesta.")),
  ("Vitamina D y zinc: importantes, pero sin obsesión",
   "<p>Dos nutrientes con mala fama de “milagrosos”:</p>"
   +table(["Nutriente","Qué hace","Cuándo suplementar"],
     [["Vitamina D","Modula el ciclo del folículo","Solo si los niveles están muy bajos (déficits comunes, pero no siempre relevantes para el pelo)"],
      ["Zinc","Síntesis de ADN y proteínas","Su déficit real es <b>muy raro</b> en dieta occidental. Suplementar sin déficit no aporta y en exceso causa molestias"]])),
  ("Biotina: el gran mito del marketing",
   "<p>Si un producto presume de biotina “para el pelo”, levanta la ceja. La biotina es esencial para la vida, pero su <strong>déficit en el mundo desarrollado es anecdótico</strong> (ocurre por ciertos fármacos, alcoholismo severo o dietas muy raras). En personas sanas, suplementarla <strong>no hace que el pelo crezca más grueso ni más rápido</strong>. Y tiene un riesgo poco conocido: <strong>puede alterar analíticas de sangre</strong>, dando falsos diagnósticos de tiroides o falseando la troponina (la prueba que se usa ante un posible infarto).</p>"
   +note("Antes de cualquier analítica importante, avisa a tu médico si tomas biotina. Puede ser la diferencia entre un diagnóstico correcto y uno falso.")),
  ("Entonces, ¿qué analítica pedir?",
   "<p>En lugar de comprar suplementos a ciegas, lo sensato ante una caída activa es estudiar el terreno. Un perfil razonable suele incluir:</p>"
   "<ul><li><strong>Perfil básico:</strong> hemograma y bioquímica (función hepática y renal, claves si se va a usar medicación).</li>"
   "<li><strong>Metabolismo y nutrientes:</strong> ferritina (esencial), TSH (tiroides), vitamina D, zinc, ácido fólico y B12 (sobre todo en dietas vegetarianas o uso de omeprazol).</li>"
   "<li><strong>Hormonas (en mujeres jóvenes):</strong> andrógenos como testosterona libre/total, DHEA-S y LH/FSH, para descartar hiperandrogenismos como el ovario poliquístico.</li></ul>"
   +note("En hombres, medir testosterona para estudiar la calvicie común suele ser inútil: la alopecia depende de la sensibilidad local del folículo, no del nivel de testosterona en sangre.")),
 ],
 faq_pairs=[
  ("¿Los suplementos “para el pelo” funcionan?","Solo cuando corrigen un déficit real (sobre todo hierro). En personas sin déficit, su efecto es mínimo o nulo. Por eso conviene medir antes de gastar."),
  ("¿El colágeno ayuda al cabello?","Para la alopecia androgenética, su eficacia es prácticamente nula. La proteína se descompone en aminoácidos que el cuerpo reparte donde necesita, no directamente al folículo."),
  ("Como sano y aun así se me cae el pelo, ¿por qué?","Porque la causa más frecuente (alopecia androgenética) es genética y hormonal, no nutricional. La dieta ayuda a no empeorar, pero no frena por sí sola una alopecia de base."),
  ("¿La caspa o el azúcar influyen en el pelo?","El exceso de azúcares rápidos eleva la insulina y aumenta la grasa y la inflamación del cuero cabelludo, lo que puede agravar dermatitis seborreica y acelerar la caída."),
 ],
)

# =====================================================================
# 14) MITOS
# =====================================================================
article(
 meta=dict(
   title="Mitos sobre la calvicie: gorras, lavado, sol y más, desmontados con ciencia",
   slug="mitos-sobre-la-calvicie-desmontados",
   category="Mitos y verdades",
   read_min=8,
   deck="¿La gorra te deja calvo? ¿Lavarte a diario es malo? ¿Cortarte el pelo lo fortalece? Repasamos los mitos más repetidos y separamos lo falso de lo que sí tiene base.",
   meta_desc="Mitos de la calvicie desmentidos: gorras, lavar el pelo a diario, sol, agua dura, cortarse el pelo y colágeno. Qué es falso y qué tiene parte de verdad. Por Innovart Medical.",
   keywords="mitos calvicie, gorra calvicie, lavar el pelo a diario, sol y pelo, agua dura cabello, cortar el pelo fortalece, colágeno alopecia",
 ),
 lead="Pocas áreas de la salud acumulan tantos mitos como la caída del cabello. Algunos son inofensivos; otros llevan a la gente a tomar decisiones que empeoran su pelo o a ignorar lo que de verdad ayuda. Vamos a pasar los más famosos por el filtro de la evidencia: unos son rotundamente falsos, otros esconden una parte de verdad.",
 takeaway_items=[
   "<b>Gorras:</b> no causan calvicie. Solo importan si la humedad favorece dermatitis por mala higiene.",
   "<b>Lavarse a diario:</b> mito que sea malo. En pelo graso es recomendable e incluso necesario.",
   "<b>Sol:</b> verdadero, daña el pelo y el folículo por estrés oxidativo (y arruina injertos).",
   "<b>Cortarse el pelo:</b> no lo fortalece; el tallo es tejido inerte.",
   "<b>Colágeno oral:</b> eficacia nula para revertir la alopecia androgenética.",
 ],
 sections=[
  ("“La gorra deja calvo” — FALSO (con matiz)",
   "<p>El pelo se nutre de los vasos sanguíneos de la piel, no del aire exterior, así que una gorra <strong>no asfixia el folículo</strong> ni causa calvicie. El único matiz real: usarla muchas horas aumenta calor y humedad, lo que favorece al hongo <em>Malassezia</em> y puede empeorar una dermatitis seborreica <strong>si no hay buena higiene</strong>. La solución no es dejar la gorra, es lavarte bien.</p>"
   +img("Composición editorial de una gorra y un peine sobre fondo neutro con un sello tipo “mito / verdad”; estética limpia, divulgativa, paleta de marca.",
        "Mitos capilares: separar lo falso de lo que tiene base científica")),
  ("“Lavarse a diario es malo y da más grasa” — FALSO",
   "<p>Es uno de los errores más extendidos. Lavarse <strong>no genera un efecto rebote</strong> de grasa: la glándula sebácea está dentro de la piel y sigue su propio ciclo hormonal, ajeno a lo que hagas por fuera. En hombres y personas de pelo graso, lavarse a diario es <strong>recomendable</strong> para retirar el sebo, eliminar descamación y frenar la microinflamación que acelera la caída.</p>"
   +pull("No te ensucia el pelo lavarlo. Te lo cuida.")),
  ("“El sol daña el pelo” — VERDADERO (con matiz)",
   "<p>Este sí. La radiación UV degrada la cutícula, la queratina y la melanina (lo que se conoce como <em>weathering</em>), dejando el pelo quebradizo y apagado. Pero hay un matiz más serio: la radiación crónica genera un fuerte <strong>estrés oxidativo en el cuero cabelludo</strong> que precede e induce la muerte celular del folículo, acelerando alopecias y <strong>arruinando la supervivencia de futuros injertos</strong>. Proteger el cuero cabelludo del sol no es estética, es salud capilar.</p>"),
  ("“El agua dura estropea el pelo” — VERDADERO (con matiz)",
   "<p>El agua rica en calcio y magnesio se deposita en la cutícula y roba humedad, dejando el pelo áspero, opaco y más propenso a romperse. Es un daño <strong>estético y mecánico</strong> real. Lo que <strong>no</strong> hace es producir alopecia desde la raíz, salvo que provoque una irritación extrema que derive en dermatitis.</p>"),
  ("Dos clásicos: cortarse el pelo y el colágeno",
   "<p>Cerramos con dos mitos muy queridos:</p>"
   +compare("“Cortarse/raparse fortalece el pelo” — FALSO",
     ["El tallo piloso es <b>tejido inerte</b>.",
      "Cortarlo no envía señal alguna a la raíz.",
      "Solo da una <b>ilusión óptica</b> de densidad al cortar la punta afinada."],
     "“El colágeno revierte la calvicie” — FALSO",
     ["Eficacia clínica <b>nula</b> en alopecia androgenética.",
      "Se digiere en aminoácidos que el cuerpo reparte a su criterio.",
      "No “va” directamente a construir pelo."])
   +note("Regla práctica frente a cualquier mito capilar: si suena fácil, barato y milagroso, casi siempre es falso. Lo que funciona requiere diagnóstico y constancia.")),
 ],
 faq_pairs=[
  ("Entonces, ¿cada cuánto debo lavarme el pelo?","Depende de tu tipo de cuero cabelludo. En pelo graso, a diario suele ser lo ideal. Lo importante es retirar el exceso de sebo y la descamación, no “dejar descansar” el pelo."),
  ("¿Debo dejar de usar gorra?","No es necesario. Solo cuida la higiene si la usas muchas horas, para evitar que la humedad favorezca dermatitis. La gorra no te dejará calvo."),
  ("¿Sirve de algo algún champú para la caída?","Los champús con activos como ketoconazol ayudan a controlar la dermatitis seborreica que acelera la caída, pero no “curan” la alopecia androgenética. Son un apoyo, no el tratamiento de base."),
 ],
)

# =====================================================================
# 15) ALOPECIA AREATA Y CICATRICIAL
# =====================================================================
article(
 meta=dict(
   title="Cuando NO es genética: alopecia areata y alopecias cicatriciales",
   slug="alopecia-areata-y-cicatricial-cuando-no-es-genetica",
   category="Diagnóstico",
   read_min=9,
   deck="No toda caída es calvicie común. Algunas alopecias son autoinmunes y otras destruyen el folículo para siempre. Reconocer las señales a tiempo puede salvar tu pelo.",
   meta_desc="Alopecia areata (autoinmune) y alopecias cicatriciales (liquen plano pilar, frontal fibrosante, foliculitis decalvante): causas, señales de alarma y por qué el diagnóstico temprano es vital. Por Innovart Medical.",
   keywords="alopecia areata, alopecia cicatricial, liquen plano pilar, alopecia frontal fibrosante, foliculitis decalvante, tricodinia",
 ),
 lead="La gran mayoría de las consultas por caída son alopecia androgenética, pero no todas. Hay dos grupos que conviene conocer porque cambian por completo el pronóstico y la urgencia: las alopecias autoinmunes (como la areata) y las cicatriciales, que destruyen el folículo de forma irreversible. En estas, el tiempo no es un detalle: es el factor decisivo.",
 takeaway_items=[
   "La <b>alopecia areata</b> es autoinmune: el cuerpo ataca el folículo y causa “moneditas” sin pelo.",
   "Las formas focales tienen <b>buen pronóstico</b> y a menudo se repueblan; las graves tienen tratamientos nuevos (anti-JAK).",
   "Las <b>alopecias cicatriciales</b> destruyen las células madre del folículo: son <b>irreversibles</b>.",
   "Señales de alarma: <b>picor, ardor, enrojecimiento, descamación y tricodinia</b> (dolor al mover el pelo).",
   "El objetivo es <b>apagar la inflamación a tiempo</b> para salvar los folículos que aún viven.",
 ],
 sections=[
  ("Alopecia areata: cuando el sistema inmune ataca al pelo",
   "<p>La alopecia areata es una <strong>enfermedad autoinmune</strong>: tus propios linfocitos pierden la tolerancia, atacan el bulbo del folículo y fuerzan la caída. Tiene base genética, y sobre ese terreno actúan detonantes como un <strong>shock emocional, estrés agudo o infecciones</strong>. Es habitual que se asocie a otras condiciones autoinmunes, como la tiroiditis de Hashimoto.</p>"
   "<p>Se manifiesta de forma muy reconocible: <strong>calvas redondeadas, como “moneditas”</strong>, que aparecen de forma repentina y sin cicatriz visible.</p>"
   +img("Ilustración médica clara de una placa redondeada de alopecia areata en cuero cabelludo, estilo divulgativo y respetuoso, sin dramatismo, paleta de marca.",
        "Alopecia areata: placas redondeadas de pérdida de pelo sin cicatriz")),
  ("Areata: qué hacer y qué tratamientos hay",
   "<p>Ante la aparición de pequeñas calvas, lo primero es <strong>no entrar en pánico</strong>: las formas focales tienen excelente pronóstico y muchas veces se repueblan solas o con unas infiltraciones locales. Cuando la enfermedad es grave (areata total o universal), se requiere tratamiento sistémico. La gran novedad son los <strong>fármacos anti-JAK</strong>, biológicos potentes que bloquean la vía inflamatoria y consiguen repoblar a pacientes que llevaban años sin respuesta.</p>"
   +note("La areata no es la calvicie común y no se trata igual. Por eso un diagnóstico correcto evita tratamientos inútiles y angustia innecesaria.")),
  ("Alopecias cicatriciales: el reloj corre en contra",
   "<p>Aquí cambia todo. En las alopecias cicatriciales primarias (liquen plano pilar, <strong>alopecia frontal fibrosante</strong>, foliculitis decalvante, lupus discoide), la inflamación se localiza justo donde residen las <strong>células madre del folículo</strong>. Cuando el sistema inmune las destruye, el folículo es reemplazado por tejido fibrótico: <strong>es como si el terreno fértil se convirtiera en desierto</strong>. Por eso son <strong>irreversibles</strong>: ningún fármaco devuelve la vida a un folículo cicatrizado.</p>"
   +pull("En las alopecias cicatriciales no luchamos por recuperar lo perdido, sino por salvar lo que aún sigue vivo. Por eso el tiempo lo es todo.")),
  ("Las señales de alarma que no debes ignorar",
   "<p>A diferencia de la calvicie común (silenciosa e indolora), las alopecias cicatriciales suelen <strong>dar síntomas</strong>. Consulta sin demora si notas:</p>"
   "<ul><li><strong>Picor mantenido</strong> y enrojecimiento alrededor del poro.</li>"
   "<li><strong>Descamación pegada al pelo.</strong></li>"
   "<li><strong>Tricodinia:</strong> dolor o ardor al mover o tocar el pelo (muy característico).</li>"
   "<li>En formas con pus: <strong>granos, costras amarillentas</strong> y pústulas.</li>"
   "<li>En la frontal fibrosante: <strong>retroceso de la línea como una diadema</strong>, con pérdida de cejas.</li></ul>"
   +note("Picor o dolor + caída no es normal. Es justo la combinación que obliga a una valoración rápida para frenar el daño.")),
  ("Por qué el diagnóstico temprano lo cambia todo",
   "<p>Como no se puede revertir un folículo destruido, el objetivo terapéutico es <strong>apagar la inflamación cuanto antes</strong> (con antiinflamatorios, antipalúdicos o anti-JAK según el caso) para salvar los folículos que aún sobreviven. Si la enfermedad se inactiva durante años, un trasplante muy meticuloso podría restaurar la zona, sabiendo que la supervivencia del injerto en tejido cicatricial es menor que en piel sana. Todo empieza por un diagnóstico preciso —y a tiempo—.</p>"
   "<p>En Innovart Medical, la valoración con dermatoscopia nos permite distinguir estos cuadros de la calvicie común y derivar el tratamiento adecuado. Confundirlos cuesta folículos que no vuelven.</p>"),
 ],
 faq_pairs=[
  ("¿La alopecia areata se cura?","Las formas leves suelen recuperarse, a veces solas. Las graves hoy cuentan con tratamientos eficaces (anti-JAK). No deja cicatriz, así que el folículo conserva el potencial de repoblar."),
  ("¿Puedo hacerme un injerto si tengo alopecia cicatricial?","Solo si la enfermedad lleva años inactiva, y con expectativas realistas: la supervivencia del injerto en tejido cicatricial es menor. Primero hay que apagar y estabilizar la inflamación."),
  ("¿Cómo sé si mi caída es genética o cicatricial?","La calvicie común es indolora y progresiva; las cicatriciales suelen dar picor, ardor o enrojecimiento. La dermatoscopia y, si hace falta, una biopsia lo confirman. Ante síntomas, consulta pronto."),
  ("La areata, ¿es por estrés?","El estrés puede ser un detonante en personas con predisposición genética, pero la enfermedad es autoinmune. Controlar el estrés ayuda, pero no sustituye el tratamiento médico."),
 ],
)

print("Batch 4 listo.")
