# -*- coding: utf-8 -*-
"""
Sistema de plantillas para el blog de Innovart Medical.
Genera artículos HTML autocontenidos (CSS + SVG inline), listos para la web.
Voz: clínica Innovart Medical (NUNCA en nombre de terceros).
Cumplimiento: prohibido el término "Garantía Vitalicia".
"""
import os, re, html

OUT_DIR = "/tmp/innovart-blogs/html"
os.makedirs(OUT_DIR, exist_ok=True)

# ---- Contacto (línea principal Innovart) ----
PHONE_DISPLAY = "+57 312 456 5014"
PHONE_WA = "573124565014"
PHONE_TEL = "+573124565014"

# ---------------------------------------------------------------------------
# CSS / DESIGN SYSTEM
# ---------------------------------------------------------------------------
CSS = """
:root{
  --ink:#0E2733; --ink-soft:#3A4D55; --muted:#6B7B82;
  --teal:#0F766E; --teal-deep:#0B5A54; --teal-tint:#E9F3F1;
  --gold:#C0A24E; --gold-soft:#EFE7CF;
  --bg:#FBFAF7; --surface:#FFFFFF; --line:#E8E3D8;
  --shadow:0 18px 48px -24px rgba(14,39,51,.45);
  --radius:18px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  font-size:18px; line-height:1.75; -webkit-font-smoothing:antialiased;
}
h1,h2,h3,h4,.brandmark{font-family:'Fraunces','Georgia',serif; font-weight:600; letter-spacing:-.01em}
img{max-width:100%}
a{color:var(--teal-deep)}

/* ---- Top bar ---- */
.topbar{background:var(--ink); color:#fff}
.topbar .wrap{max-width:1080px;margin:0 auto;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.brandmark{font-size:22px;color:#fff;display:flex;align-items:center;gap:11px}
.brandmark .dot{width:11px;height:11px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 4px rgba(192,162,78,.22)}
.brandmark small{display:block;font-family:'Inter',sans-serif;font-weight:500;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#9FB4B9;margin-top:-2px}
.topnav{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#9FB4B9}
.topnav b{color:var(--gold);font-weight:600}
.topphone{display:inline-flex;align-items:center;gap:7px;background:var(--gold);color:#23210F;font-family:'Inter',sans-serif;font-weight:700;font-size:14px;text-decoration:none;padding:9px 16px;border-radius:999px;white-space:nowrap}

/* ---- Hero ---- */
.hero{position:relative;overflow:hidden;background:linear-gradient(135deg,#0B232E 0%,#0E3A39 55%,#0F766E 130%);color:#fff}
.hero .hsvg{position:absolute;inset:0;width:100%;height:100%;opacity:.16}
.hero .hwrap{position:relative;max-width:880px;margin:0 auto;padding:70px 24px 64px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:'Inter',sans-serif;font-size:12px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);margin-bottom:22px}
.eyebrow::before{content:"";width:30px;height:1px;background:var(--gold)}
.hero h1{font-size:clamp(33px,5.2vw,54px);line-height:1.18;margin:0 0 28px;max-width:18ch}
.hero .deck{font-size:clamp(18px,2.4vw,21px);line-height:1.7;color:#D6E5E3;max-width:62ch;margin:0;letter-spacing:.3px}
.meta{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:34px;font-family:'Inter',sans-serif;font-size:13.5px;color:#BFD3D1}
.meta span{display:inline-flex;align-items:center;gap:8px}
.meta b{color:#fff;font-weight:600}
.meta .pip{width:6px;height:6px;border-radius:50%;background:var(--gold)}

/* ---- Layout ---- */
.container{max-width:760px;margin:0 auto;padding:0 24px}
.article{padding:56px 0 30px}
.lead{font-size:21px;line-height:1.7;color:var(--ink-soft)}
.lead::first-letter{float:left;font-family:'Fraunces',serif;font-size:74px;line-height:.78;font-weight:600;color:var(--teal);padding:8px 14px 0 0}
.article p{margin:0 0 22px}
.article h2{font-size:29px;margin:52px 0 8px;padding-top:14px;position:relative}
.article h2::after{content:"";display:block;width:54px;height:3px;background:var(--gold);border-radius:3px;margin-top:14px}
.article h3{font-size:21px;margin:34px 0 6px;color:var(--teal-deep)}
.article ul,.article ol{margin:0 0 24px;padding-left:1.25em}
.article li{margin:0 0 10px}
.article strong{color:var(--ink)}
hr.sep{border:0;height:1px;background:var(--line);margin:46px 0}

/* ---- TOC ---- */
.toc{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px 28px;margin:8px 0 40px}
.toc h4{margin:0 0 12px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-family:'Inter',sans-serif;font-weight:700}
.toc ol{margin:0;padding-left:1.1em;columns:2;column-gap:30px;font-size:15.5px}
.toc a{color:var(--ink-soft);text-decoration:none}
.toc a:hover{color:var(--teal)}
@media(max-width:620px){.toc ol{columns:1}}

/* ---- Key takeaways ---- */
.takeaways{background:var(--teal-tint);border-radius:var(--radius);padding:28px 30px;margin:36px 0;border:1px solid #D5E8E4}
.takeaways h4{margin:0 0 14px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--teal-deep);font-family:'Inter',sans-serif;font-weight:700;display:flex;align-items:center;gap:9px}
.takeaways ul{list-style:none;margin:0;padding:0}
.takeaways li{position:relative;padding-left:30px;margin:0 0 12px;font-size:16.5px;line-height:1.6}
.takeaways li::before{content:"";position:absolute;left:0;top:9px;width:14px;height:14px;border-radius:50%;background:var(--teal);box-shadow:0 0 0 4px rgba(15,118,110,.16)}
.takeaways li:last-child{margin-bottom:0}

/* ---- Pull quote ---- */
.pquote{margin:42px 0;padding:6px 0 6px 30px;border-left:4px solid var(--gold);font-family:'Fraunces',serif;font-size:25px;line-height:1.4;color:var(--ink);font-style:italic}
.pquote cite{display:block;margin-top:12px;font-family:'Inter',sans-serif;font-style:normal;font-size:14px;letter-spacing:.04em;color:var(--muted)}

/* ---- Image suggestion ---- */
.imgsugg{margin:34px 0;border:1.5px dashed #C9C0AB;border-radius:14px;background:#FCFBF6;padding:22px 24px;display:flex;gap:18px;align-items:flex-start}
.imgsugg .ic{flex:0 0 44px;width:44px;height:44px;border-radius:11px;background:var(--gold-soft);display:flex;align-items:center;justify-content:center}
.imgsugg .ic svg{width:24px;height:24px}
.imgsugg .body{font-family:'Inter',sans-serif;font-size:14.5px;line-height:1.6;color:var(--ink-soft)}
.imgsugg .tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:6px}
.imgsugg b{color:var(--ink)}
.imgsugg .alt{margin-top:8px;font-size:13px;color:var(--muted)}

/* ---- Stat band ---- */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:38px 0}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:22px 20px;text-align:center}
.stat .n{font-family:'Fraunces',serif;font-size:36px;font-weight:600;color:var(--teal);line-height:1}
.stat .l{font-family:'Inter',sans-serif;font-size:13px;color:var(--muted);margin-top:8px;line-height:1.4}
@media(max-width:620px){.stats{grid-template-columns:1fr}}

/* ---- Timeline ---- */
.timeline{margin:36px 0;border-left:2px solid var(--gold-soft);padding-left:26px}
.tl{position:relative;margin:0 0 24px}
.tl::before{content:"";position:absolute;left:-33px;top:3px;width:13px;height:13px;border-radius:50%;background:var(--surface);border:3px solid var(--teal)}
.tl .when{font-family:'Inter',sans-serif;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.tl .what{font-family:'Fraunces',serif;font-size:18px;color:var(--ink);margin:2px 0 4px}
.tl p{margin:0;font-size:15.5px;color:var(--ink-soft)}

/* ---- Compare cards ---- */
.compare{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:34px 0}
.ccard{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:24px;border-top:4px solid var(--teal)}
.ccard:nth-child(2){border-top-color:var(--gold)}
.ccard h4{margin:0 0 12px;font-size:19px}
.ccard ul{margin:0;padding-left:1.1em;font-size:15px}
.ccard li{margin:0 0 8px}
@media(max-width:620px){.compare{grid-template-columns:1fr}}

/* ---- Data table ---- */
.tbl{width:100%;border-collapse:collapse;margin:30px 0;font-size:15.5px;font-family:'Inter',sans-serif}
.tbl th,.tbl td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);vertical-align:top}
.tbl th{background:var(--ink);color:#fff;font-weight:600;font-size:13px;letter-spacing:.04em}
.tbl tr:nth-child(even) td{background:#F6F4EE}

/* ---- Note / disclaimer ---- */
.note{background:#FBF7EC;border:1px solid var(--gold-soft);border-radius:14px;padding:20px 24px;margin:34px 0;font-family:'Inter',sans-serif;font-size:14.5px;line-height:1.65;color:var(--ink-soft)}
.note b{color:var(--ink)}

/* ---- CTA ---- */
.cta{margin:54px 0 10px;border-radius:22px;overflow:hidden;background:linear-gradient(135deg,#0B232E,#0F766E);color:#fff;box-shadow:var(--shadow)}
.cta .inner{padding:48px 44px;display:flex;flex-direction:column}
.cta h3{color:#fff;font-size:27px;margin:0 0 14px;max-width:22ch}
.cta p{color:#CFE2E0;font-size:16px;margin:0 0 28px;max-width:54ch}
.cta a.btn{display:inline-flex;align-items:center;gap:10px;background:var(--gold);color:#23210F;font-family:'Inter',sans-serif;font-weight:700;font-size:15.5px;letter-spacing:.01em;text-decoration:none;padding:15px 28px;border-radius:999px;width:fit-content;margin-bottom:12px}
.cta a.btn.ghost{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.45);margin-bottom:16px}
.cta .sedes{margin-top:28px;font-size:13px;color:#9FB9B6;letter-spacing:.02em}
@media(max-width:620px){.cta .inner{padding:40px 30px}.cta a.btn.ghost{margin-bottom:16px}}

/* ---- Sedes Grid (GEO) ---- */
.sedes-section{background:var(--bg);padding:56px 24px;margin:0}
.sedes-section h3{text-align:center;font-family:'Fraunces',serif;font-size:28px;color:var(--ink);margin:0 0 40px;max-width:60ch;margin-left:auto;margin-right:auto}
.sedes-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;max-width:1000px;margin:0 auto;padding:0 24px}
.sede-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:28px 24px;text-align:center;transition:all .3s ease;box-shadow:0 2px 8px rgba(14,39,51,.08)}
.sede-card:hover{border-color:var(--teal);box-shadow:0 8px 24px rgba(15,118,110,.12);transform:translateY(-2px)}
.sede-card h4{font-family:'Fraunces',serif;font-size:22px;color:var(--teal-deep);margin:0 0 12px;font-weight:600}
.sede-card .addr{font-size:14px;color:var(--ink-soft);margin:0 0 16px;line-height:1.5;font-weight:500}
.sede-card .sede-link{display:inline-block;color:var(--teal-deep);text-decoration:none;font-size:13px;font-weight:600;padding:8px 12px;border:1px solid var(--gold-soft);border-radius:8px;margin:0 6px 8px 0;transition:all .2s}
.sede-card .sede-link:hover{background:var(--gold-soft);color:#23210F}
@media(max-width:620px){.sedes-grid{grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px}.sede-card{padding:20px 16px}}

/* ---- Related articles ---- */
.related-articles{background:var(--teal-tint);border:1px solid #D5E8E4;border-radius:var(--radius);padding:32px 28px;margin:54px 0 40px;border-left:4px solid var(--gold)}
.related-articles h4{margin:0 0 20px;font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:var(--teal-deep);font-family:'Inter',sans-serif;font-weight:700;display:flex;align-items:center;gap:8px}
.related-articles .rel-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.related-articles li{margin:0;padding:0}
.related-articles a{display:flex;align-items:flex-start;gap:10px;padding:12px;background:var(--surface);border-radius:10px;border:1px solid #D5E8E4;text-decoration:none;color:var(--ink);font-size:14px;font-weight:500;line-height:1.4;transition:all .2s}
.related-articles a:hover{background:#fff;border-color:var(--teal);color:var(--teal-deep)}
.related-articles a::before{content:"→";flex:0 0 auto;color:var(--gold);font-weight:700}

/* ---- Author signature ---- */
.author-sig{background:var(--teal-tint);border:1px solid #D5E8E4;border-radius:var(--radius);padding:24px 28px;margin:46px 0 0;border-left:4px solid var(--gold)}
.author-sig .sig-title{font-family:'Fraunces',serif;font-size:18px;font-weight:600;color:var(--ink);margin:0 0 6px}
.author-sig .sig-role{font-family:'Inter',sans-serif;font-size:14px;color:var(--muted);margin:0}

/* ---- Footer ---- */
.foot{background:var(--ink);color:#9FB4B9;margin-top:60px;font-family:'Inter',sans-serif;font-size:13.5px}
.foot .wrap{max-width:880px;margin:0 auto;padding:46px 24px}
.foot .brandmark{color:#fff;font-size:20px;margin-bottom:14px}
.foot .grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:30px;margin:24px 0}
.foot h5{color:#fff;font-family:'Inter',sans-serif;font-size:12px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 10px}
.foot a{color:#9FB4B9;text-decoration:none}
.foot .legal{border-top:1px solid rgba(255,255,255,.1);margin-top:28px;padding-top:22px;font-size:12px;line-height:1.7;color:#7E9499}
@media(max-width:620px){.foot .grid{grid-template-columns:1fr}}
"""

# ---------------------------------------------------------------------------
# SVG ASSETS
# ---------------------------------------------------------------------------
HERO_SVG = """<svg class="hsvg" viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".9"/><stop offset="1" stop-color="#C0A24E" stop-opacity=".7"/></linearGradient></defs>
<g stroke="url(#g)" stroke-width="2" fill="none" stroke-linecap="round">
__FOLLICLES__
</g>
<g fill="#C0A24E" opacity=".5">__DOTS__</g>
</svg>"""

def _hero_pattern():
    import math, random
    random.seed(7)
    foll=[]; dots=[]
    for i in range(46):
        x=20+i*26%1180; base=120+ (i*53)%360
        amp=10+(i*7)%18; h=70+(i*13)%120
        d=f"M{x},{base} C{x-amp},{base-h*0.4} {x+amp},{base-h*0.7} {x},{base-h}"
        foll.append(f'<path d="{d}"/>')
        dots.append(f'<circle cx="{x}" cy="{base+4}" r="2.4"/>')
    return HERO_SVG.replace("__FOLLICLES__","".join(foll)).replace("__DOTS__","".join(dots))

HERO_SVG_FILLED=_hero_pattern()

CAM_ICON = """<svg viewBox="0 0 24 24" fill="none" stroke="#C0A24E" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h1.2l1-1.6A1 1 0 0 1 8.5 4h7a1 1 0 0 1 .8.4L17.3 6h1.2A2.5 2.5 0 0 1 21 8.5v8A2.5 2.5 0 0 1 18.5 19h-13A2.5 2.5 0 0 1 3 16.5z"/><circle cx="12" cy="12.5" r="3.6"/></svg>"""

# ---------------------------------------------------------------------------
# COMPONENT HELPERS
# ---------------------------------------------------------------------------
def slugify(t):
    t=t.lower()
    for a,b in [("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"),("ñ","n"),("ü","u")]:
        t=t.replace(a,b)
    t=re.sub(r"[^a-z0-9]+","-",t).strip("-")
    return t

def takeaways(items, title="Lo esencial en 30 segundos"):
    lis="".join(f"<li>{i}</li>" for i in items)
    return f'<div class="takeaways"><h4>★ {title}</h4><ul>{lis}</ul></div>'

def pull(text, cite="Equipo médico · Innovart Medical"):
    c=f'<cite>{cite}</cite>' if cite else ""
    return f'<blockquote class="pquote">{text}{c}</blockquote>'

def img(prompt, alt, tag="Sugerencia de imagen"):
    return (f'<figure class="imgsugg"><div class="ic">{CAM_ICON}</div>'
            f'<div class="body"><span class="tag">{tag}</span><div><b>{prompt}</b></div>'
            f'<div class="alt">Texto alternativo (alt) sugerido: «{alt}»</div></div></figure>')

def stats(triples):
    cells="".join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in triples)
    return f'<div class="stats">{cells}</div>'

def timeline(items):
    rows="".join(f'<div class="tl"><div class="when">{w}</div><div class="what">{t}</div><p>{p}</p></div>' for w,t,p in items)
    return f'<div class="timeline">{rows}</div>'

def compare(a_title,a_items,b_title,b_items):
    al="".join(f"<li>{i}</li>" for i in a_items)
    bl="".join(f"<li>{i}</li>" for i in b_items)
    return (f'<div class="compare"><div class="ccard"><h4>{a_title}</h4><ul>{al}</ul></div>'
            f'<div class="ccard"><h4>{b_title}</h4><ul>{bl}</ul></div></div>')

def table(headers, rows):
    th="".join(f"<th>{h}</th>" for h in headers)
    trs=""
    for r in rows:
        trs+="<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>"
    return f'<table class="tbl"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'

def note(text, label="Importante"):
    return f'<div class="note"><b>{label}:</b> {text}</div>'

def author_signature():
    return '''<div class="author-sig">
<div class="sig-title">Dr. Fabián Carreño Jiménez</div>
<div class="sig-role">Director Médico · Cirujano Plástico y Reconstructivo especializado en Restauración Capilar · Innovart Medical IPS</div>
</div>'''

def schema_jsonld(*, title, deck, slug, date="2026-06-13"):
    import json
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": deck,
        "image": "https://innovartmedical.com/logo.png",
        "datePublished": date,
        "dateModified": date,
        "author": {
            "@type": "Person",
            "name": "Dr. Fabián Carreño Jiménez",
            "jobTitle": "Director Médico, Cirujano Plástico y Reconstructivo",
            "affiliation": {
                "@type": "Organization",
                "name": "Innovart Medical IPS"
            }
        },
        "publisher": {
            "@type": "Organization",
            "name": "Innovart Medical IPS",
            "url": "https://innovartmedical.com"
        },
        "articleBody": title
    }
    return f"<script type=\"application/ld+json\">{json.dumps(schema, ensure_ascii=False)}</script>"

def faq(pairs):
    items=""
    for q,a in pairs:
        items+=f'<details style="border:1px solid var(--line);border-radius:12px;padding:6px 20px;margin:0 0 12px;background:var(--surface)"><summary style="cursor:pointer;font-family:\'Fraunces\',serif;font-size:18px;padding:12px 0;color:var(--ink)">{q}</summary><div style="padding:0 0 16px;color:var(--ink-soft);font-size:16px;line-height:1.65">{a}</div></details>'
    return f'<h2 id="preguntas-frecuentes">Preguntas frecuentes</h2>{items}'

def cta(h="Da el primer paso: agenda tu valoración capilar",
        p="En Innovart Medical estudiamos tu caso con dermatoscopia y un plan personalizado. La primera valoración es sin costo y sin compromiso, presencial en nuestras sedes o por videollamada.",
        slug=""):
    wa_link = f"https://wa.me/{PHONE_WA}?text=Hola,%20vengo%20del%20blog%20'{slug}'%20y%20me%20interesa%20saber%20m%C3%A1s"
    cal_link = f"https://innovartmedical.com?utm_source=blog&utm_content={slug}"
    return f"""<div class="cta"><div class="inner">
<h3>{h}</h3><p>{p}</p>
<a class="btn" href="{wa_link}">📲 Escríbenos al {PHONE_DISPLAY}</a><a class="btn ghost" href="{cal_link}">Agenda tu valoración gratuita →</a>
</div></div>"""

def sedes_grid():
    sedes = [
        ("Bogotá", "Calle 116 #9-72", "4.7110", "-74.0721", "https://share.google/unA0jM58IDgsldKhl"),
        ("Medellín", "CC Oviedo, Piso 16", "6.2186", "-75.5754", "https://share.google/rtE6wmM6zx18dG2JA"),
        ("Barranquilla", "Green Tower, Piso 14", "10.9639", "-74.7964", "https://share.google/NlrnR03cCYoShIKqz"),
        ("Bucaramanga", "HIC Business Center", "7.1190", "-73.1245", "https://goo.gl/maps/innovart-bucaramanga"),
        ("Ciudad de Panamá", "Costa del Este", "8.9824", "-79.5199", "https://share.google/GrA5R5tOD5HLKLSpM"),
    ]
    cards = ""
    for city, addr, lat, lon, gmb_link in sedes:
        cards += f'''<div class="sede-card">
<h4>{city}</h4>
<p class="addr">{addr}</p>
<a href="{gmb_link}" class="sede-link" target="_blank">📍 Ver en Maps</a>
</div>'''
    return f'''<section class="sedes-section">
<h3>Nuestras sedes en Colombia y Panamá</h3>
<div class="sedes-grid">{cards}</div>
</section>'''

def related_articles(blog_slug, related_list):
    """related_list = [("titulo blog", "slug-blog"), ...]"""
    if not related_list:
        return ""
    items = "".join(f'<li><a href="/{r[1]}.html">{r[0]}</a></li>' for r in related_list)
    return f'''<div class="related-articles">
<h4>📖 Lee también</h4>
<ul class="rel-list">{items}</ul>
</div>'''

def schema_localbusiness():
    """Genera Schema LocalBusiness para todas las sedes"""
    sedes = [
        ("Bogotá", "Calle 116 #9-72", "4.7110", "-74.0721"),
        ("Medellín", "CC Oviedo, Piso 16", "6.2186", "-75.5754"),
        ("Barranquilla", "Green Tower, Piso 14", "10.9639", "-74.7964"),
        ("Bucaramanga", "HIC Business Center", "7.1190", "-73.1245"),
        ("Ciudad de Panamá", "Costa del Este", "8.9824", "-79.5199"),
    ]
    import json
    schemas = []
    for city, addr, lat, lon in sedes:
        schemas.append({
            "@type": "LocalBusiness",
            "@context": "https://schema.org",
            "name": f"Innovart Medical - {city}",
            "image": "https://innovartmedical.com/logo.png",
            "description": "Clínica especializada en restauración capilar y tratamientos de alopecia",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": addr,
                "addressLocality": city,
                "addressCountry": "CO" if city != "Ciudad de Panamá" else "PA"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": float(lat),
                "longitude": float(lon)
            },
            "telephone": PHONE_TEL,
            "url": "https://innovartmedical.com",
            "priceRange": "$$$"
        })
    return f"<script type=\"application/ld+json\">{json.dumps(schemas, ensure_ascii=False)}</script>"

DISCLAIMER = ("Este contenido es informativo y educativo; no sustituye una consulta médica. "
    "El diagnóstico de la alopecia y la indicación de cualquier tratamiento o procedimiento "
    "deben ser realizados por un profesional de la salud tras una valoración individual. "
    "Innovart Medical IPS está habilitada bajo los estándares del Ministerio de Salud de Colombia. "
    "Los resultados de cualquier tratamiento varían según cada paciente.")

# ---------------------------------------------------------------------------
# PAGE BUILDER
# ---------------------------------------------------------------------------
def build(*, title, deck, category, read_min, body, toc, slug=None,
          meta_desc="", keywords="", date="13 de junio de 2026", related=[]):
    slug = slug or slugify(title)
    toc_html = "".join(f'<li><a href="#{slugify(t)}">{t}</a></li>' for t in toc)
    schema_tag = schema_jsonld(title=title, deck=deck, slug=slug, date=date)
    schema_local = schema_localbusiness()
    author_sig = author_signature()
    sedes = sedes_grid()
    rel_articles = related_articles(slug, related) if related else ""
    cta_section = cta(slug=slug)

    page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Innovart Medical</title>
<meta name="description" content="{html.escape(meta_desc)}">
<meta name="keywords" content="{html.escape(keywords)}">
<meta name="author" content="Innovart Medical IPS">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(meta_desc)}">
<meta property="og:site_name" content="Innovart Medical">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{schema_tag}
{schema_local}
<style>{CSS}</style>
</head>
<body>
<header class="topbar"><div class="wrap">
  <div class="brandmark"><span class="dot"></span><span>Innovart Medical<small>Microcirugía capilar</small></span></div>
  <a class="topphone" href="https://wa.me/{PHONE_WA}?text=Hola,%20vengo%20del%20blog%20'{slug}'%20y%20me%20interesa%20saber%20m%C3%A1s">📲 {PHONE_DISPLAY}</a>
</div></header>

<section class="hero">{HERO_SVG_FILLED}<div class="hwrap">
  <div class="eyebrow">{category}</div>
  <h1>{title}</h1>
  <p class="deck">{deck}</p>
  <div class="meta">
    <span><span class="pip"></span>Por <b>el equipo médico de Innovart</b></span>
    <span><span class="pip"></span>{read_min} min de lectura</span>
    <span><span class="pip"></span>{date}</span>
  </div>
</div></section>

<main class="article"><div class="container">
<nav class="toc"><h4>En este artículo</h4><ol>{toc_html}</ol></nav>
{body}
{author_sig}
{rel_articles}
{cta_section}
</div></main>

{sedes}

<footer class="foot"><div class="wrap">
  <div class="brandmark"><span class="dot" style="display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--gold);margin-right:8px"></span>Innovart Medical IPS</div>
  <p style="max-width:60ch;margin:0">Restauración capilar con criterio médico. Tratamos la alopecia como una condición que afecta la salud emocional, no solo la estética.</p>
  <div class="grid">
    <div><h5>Sedes</h5>Bogotá · Calle 116 #9-72<br>Medellín · CC Oviedo<br>Barranquilla · Green Tower<br>Bucaramanga · HIC<br>Ciudad de Panamá · Costa del Este</div>
    <div><h5>Síguenos</h5><a href="https://instagram.com/innovartmedicalips">Instagram</a><br><a href="#">Facebook</a><br><a href="#">TikTok</a><br><a href="#">YouTube</a></div>
    <div><h5>Contacto</h5><a href="https://wa.me/{PHONE_WA}" style="color:#fff;font-weight:600">WhatsApp {PHONE_DISPLAY}</a><br><a href="tel:{PHONE_TEL}">Llamar {PHONE_DISPLAY}</a><br><a href="https://innovartmedical.com">innovartmedical.com</a></div>
  </div>
  <div class="legal"><b style="color:#fff">Aviso médico:</b> {DISCLAIMER}<br><br>© 2026 Innovart Medical IPS · NIT 901608860. Todos los derechos reservados.</div>
</div></footer>
</body>
</html>"""
    path=os.path.join(OUT_DIR, f"{slug}.html")
    with open(path,"w",encoding="utf-8") as f:
        f.write(page)
    print(f"  ✓ {slug}.html  ({len(page)//1024} KB)")
    return path

def article(meta, lead, takeaway_items, sections, faq_pairs):
    """sections: list of (title, html). Builds toc+body and writes the page."""
    toc=[t for t,_ in sections]+["Preguntas frecuentes"]
    body=f'<p class="lead">{lead}</p>'
    body+=takeaways(takeaway_items)
    for t,h in sections:
        body+=f'<h2 id="{slugify(t)}">{t}</h2>'+h
    body+=faq(faq_pairs)
    return build(body=body, toc=toc, **meta)
