---
name: blog-salud-capilar-drive
description: Blog SEO de salud capilar (15 artículos HTML + índice) generado para la web de Innovart, basado en el notebook de Carlos Muñoz. Ubicación en Drive.
metadata:
  type: project
  updated: 2026-06-13
---

# Blog de salud capilar — Innovart Medical

El 2026-06-13 se generaron **15 artículos tipo blog en HTML autocontenido** (CSS + SVG inline, voz de la clínica, NO en nombre de Carlos Muñoz) + una **página índice** (`index.html`), listos para la web (Shopify).

## Ubicación en Drive
- Carpeta: **3. MERCADEO / CLAUDE / Blogs**
- ID carpeta `Blogs`: `1DTXGHxIohr0sk9gu28AB3YeBm-TBL7Su`
- [Abrir carpeta](https://drive.google.com/drive/folders/1DTXGHxIohr0sk9gu28AB3YeBm-TBL7Su)
- Subidos con `rclone copy` (remote `gdrive`).

## Fuente del contenido
- Notebook NotebookLM **#7 "Escuela de alopecia Carlos Muñoz"** (300 fuentes YouTube). ID: `b06d14db-2080-459c-ae3f-deb528314256`.
- Contenido técnico extraído vía `notebooklm ask` (5 consultas clúster: fisiopatología, cirugía, no-androgenéticas, fármacos, estrés/nutrición/mitos/pre-postop).

## Los 15 temas (slug)
1. alopecia-androgenetica-por-que-se-cae-el-pelo
2. senales-tempranas-perdida-de-pelo
3. buen-candidato-injerto-capilar-zona-donante
4. fue-vs-dhi-que-tecnica-elegir
5. cuantos-anos-dura-un-injerto-capilar
6. como-prepararte-injerto-capilar-guia
7. rapar-o-no-rapar-injerto-capilar
8. alopecia-femenina-lo-que-debes-saber
9. minoxidil-finasterida-como-funcionan-mitos
10. prp-mesoterapia-exosomas-tratamientos-capilares
11. shedding-caida-al-empezar-tratamiento
12. estres-y-caida-del-cabello
13. nutricion-y-cabello-vitaminas-que-importan
14. mitos-sobre-la-calvicie-desmontados
15. alopecia-areata-y-cicatricial-cuando-no-es-genetica

## Detalles técnicos
- Cada artículo: hero con gradiente + SVG, TOC, "Lo esencial en 30 seg", H2/H3, tablas, timelines, comparativas, FAQ (`<details>`), CTA a valoración, aviso médico, footer con sedes.
- **Imágenes:** hero SVG renderizado + componentes visuales (stats/timeline/compare) + bloques de "sugerencia de imagen" con prompt y alt-text para que el equipo inserte fotografía real (no se generaron antes/después por cumplimiento — ver [[before-after-strategy]]).
- Plantilla generadora local: `/tmp/innovart-blogs/innovart_template.py` (efímero).
- Cumplimiento: NO se usó "Garantía Vitalicia" (ver [[restricciones-lenguaje]]); se usó "garantía de resultado / respaldamos tu procedimiento". Tono educativo sin promesas médicas absolutas.

## Pendiente sugerido
- Publicar en blog de Shopify (ver [[seo-plan-shopify-2026-05]]), insertar fotografía real en los bloques de sugerencia, añadir schema Article/FAQ.

Ver también: [[notebooklm-escuela-alopecia]] | [[geminnovart]] | [[feedback-informes-drive]]
