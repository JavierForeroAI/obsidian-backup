# -*- coding: utf-8 -*-
from innovart_template import CSS, HERO_SVG_FILLED, OUT_DIR, PHONE_DISPLAY, PHONE_WA, PHONE_TEL
import os

# (slug, categoria, titulo, deck, min)
ARTS = [
 ("alopecia-androgenetica-por-que-se-cae-el-pelo","Ciencia capilar","Alopecia androgenética: por qué se cae el pelo","El mecanismo real de la calvicie común: DHT, miniaturización, genética y velocidad de avance.",9),
 ("senales-tempranas-perdida-de-pelo","Diagnóstico","5 señales tempranas de que estás perdiendo el pelo","Las pistas que aparecen antes de que el espejo te avise, y cuándo actuar.",8),
 ("buen-candidato-injerto-capilar-zona-donante","Cirugía capilar","¿Eres buen candidato para un injerto capilar?","El éxito no se ve en la zona calva: se calcula en la zona donante.",9),
 ("fue-vs-dhi-que-tecnica-elegir","Cirugía capilar","FUE vs DHI: qué técnica elegir (sin marketing)","No son rivales: una es cómo se extrae y otra cómo se implanta.",8),
 ("cuantos-anos-dura-un-injerto-capilar","Cirugía capilar","¿Cuántos años dura un injerto capilar?","Sí, es permanente… con los matices que ninguna clínica seria debería ocultarte.",7),
 ("como-prepararte-injerto-capilar-guia","Cirugía capilar","Cómo prepararte para tu injerto capilar","Del tabaco al mes 12: qué hacer antes y qué esperar después, mes a mes.",10),
 ("rapar-o-no-rapar-injerto-capilar","Cirugía capilar","¿Rapar o no rapar antes del injerto?","La duda estética que más frena a los pacientes, explicada con medicina.",6),
 ("alopecia-femenina-lo-que-debes-saber","Salud capilar femenina","Alopecia femenina: lo que toda mujer debe saber","Hormonas, hierro, tiroides y estrés se entrelazan: por eso el diagnóstico lo es todo.",9),
 ("minoxidil-finasterida-como-funcionan-mitos","Tratamientos","Minoxidil y finasterida: cómo funcionan (y sus mitos)","Los dos fármacos más usados y más malentendidos contra la calvicie.",10),
 ("prp-mesoterapia-exosomas-tratamientos-capilares","Tratamientos","PRP, mesoterapia y exosomas: qué funciona","Algunas terapias tienen evidencia sólida; otras son agua cara. Te ayudamos a distinguirlas.",9),
 ("shedding-caida-al-empezar-tratamiento","Tratamientos","Shedding: por qué se cae MÁS pelo al empezar","Antes de entrar en pánico y abandonar, entiende por qué suele ser buena señal.",6),
 ("estres-y-caida-del-cabello","Salud capilar","Estrés y caída del cabello: la conexión real","El estrés no inventa una calvicie, pero puede ser la gasolina que la acelera.",8),
 ("nutricion-y-cabello-vitaminas-que-importan","Salud capilar","Nutrición y cabello: qué vitaminas importan","Solo unos pocos nutrientes mueven la aguja. Te decimos cuáles (y cuáles no).",9),
 ("mitos-sobre-la-calvicie-desmontados","Mitos y verdades","Mitos sobre la calvicie, desmontados con ciencia","Gorras, lavado, sol, agua dura: qué es falso y qué tiene base.",8),
 ("alopecia-areata-y-cicatricial-cuando-no-es-genetica","Diagnóstico","Cuando NO es genética: areata y cicatriciales","No toda caída es calvicie común. Reconocer las señales puede salvar tu pelo.",9),
]

cards=""
for slug,cat,title,deck,mn in ARTS:
    cards+=f"""<a class="card" href="{slug}.html">
      <span class="ccat">{cat}</span>
      <h3>{title}</h3>
      <p>{deck}</p>
      <span class="cmeta">{mn} min de lectura →</span>
    </a>"""

extra = """
.bloglist{max-width:1080px;margin:0 auto;padding:56px 24px 20px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{display:block;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:26px;text-decoration:none;color:var(--ink);transition:transform .15s ease,box-shadow .15s ease}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.ccat{font-family:'Inter',sans-serif;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--teal)}
.card h3{font-size:21px;margin:10px 0 10px;line-height:1.2}
.card p{font-family:'Inter',sans-serif;font-size:14.5px;color:var(--ink-soft);margin:0 0 18px;line-height:1.55}
.cmeta{font-family:'Inter',sans-serif;font-size:12.5px;font-weight:600;color:var(--gold)}
@media(max-width:900px){.grid3{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.grid3{grid-template-columns:1fr}}
"""

page=f"""<!doctype html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog de salud capilar | Innovart Medical</title>
<meta name="description" content="Artículos sobre alopecia, injerto capilar y salud del cabello, con criterio médico. Blog de Innovart Medical IPS.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}{extra}</style></head><body>
<header class="topbar"><div class="wrap">
  <div class="brandmark"><span class="dot"></span><span>Innovart Medical<small>Microcirugía capilar</small></span></div>
  <a class="topphone" href="https://wa.me/{PHONE_WA}">📲 {PHONE_DISPLAY}</a>
</div></header>
<section class="hero">{HERO_SVG_FILLED}<div class="hwrap">
  <div class="eyebrow">Blog de salud capilar</div>
  <h1>Entiende tu cabello. Decide con criterio médico.</h1>
  <p class="deck">Alopecia, injerto capilar y tratamientos, explicados sin marketing y sin mitos por el equipo médico de Innovart Medical. Porque la mejor decisión empieza por entender qué te pasa.</p>
</div></section>
<main class="bloglist"><div class="grid3">{cards}</div></main>
<footer class="foot"><div class="wrap">
  <div class="brandmark"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--gold);margin-right:8px"></span>Innovart Medical IPS</div>
  <p style="max-width:60ch;margin:8px 0 0">Restauración capilar con criterio médico en Bogotá, Medellín, Barranquilla, Bucaramanga y Ciudad de Panamá.</p>
  <p style="margin:14px 0 0;font-size:15px"><a href="https://wa.me/{PHONE_WA}" style="color:#fff;font-weight:700;text-decoration:none">📲 WhatsApp {PHONE_DISPLAY}</a> &nbsp;·&nbsp; <a href="tel:{PHONE_TEL}" style="color:#9FB4B9;text-decoration:none">Llamar {PHONE_DISPLAY}</a></p>
  <div class="legal" style="margin-top:24px">© 2026 Innovart Medical IPS · NIT 901608860. Contenido informativo; no sustituye una consulta médica.</div>
</div></footer></body></html>"""

with open(os.path.join(OUT_DIR,"index.html"),"w",encoding="utf-8") as f:
    f.write(page)
print(f"  ✓ index.html ({len(page)//1024} KB) — {len(ARTS)} artículos enlazados")
