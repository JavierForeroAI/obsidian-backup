---
name: gemas-notebooklm-innovart
description: "Gemas (notebooks) de NotebookLM de Innovart y el flujo para alimentarlas — los links de Instagram/redes NO los ingiere NotebookLM, hay que destilarlos y subirlos citando la fuente."
metadata: 
  node_type: memory
  type: project
  originSessionId: dcf43f2b-5ed7-405c-a335-765965e06ead
---

# Gemas de NotebookLM — Innovart

Cerebros (notebooks) creados vía CLI `notebooklm` (skill local, cuenta Google de Javier, ya autenticada). CLI v0.4.1 en `/opt/homebrew/bin/notebooklm`. Se manejan 100% desde Claude Code (crear, cargar fuentes, chatear, generar podcast/video/reporte/quiz, descargar).

## Gemas activas
- **GEMSEOINNOVART** — ID `0d02f9de-fde1-4934-a809-3102734f485b`. Cerebro **SEO de Innovart**: trucos, tácticas, referencias y material SEO/GEO. Creada 2026-06-20. Fuentes (todas `ready`):
  1. Reel suelto de GoBig Systems (quick-win keywords pág. 2 con GSC + Claude) — `2026-06-20_reel-gobig-truco-seo-pagina2-gsc-claude.md`
  2. **Biblioteca 98 captions @gobigsystems** (mayo–jun 2026) raspadas con Apify (`apify/instagram-scraper`) → `gobigsystems-instagram-seo-2026-06-20.md`: SEO local/GBP/Maps, GSC, GEO/IA, on-page.
  3. ⭐ **30 reels TRANSCRITOS @gobigsystems** — descargados y transcripción de audio con `apify/instagram-reel-scraper` → `gobigsystems-30reels-transcritos-trucos-2026-06-20.md`. Contiene los **trucos reales con nombres de herramientas y rutas exactas**: GMB Spy (robar categorías GBP), alsoask.com / AnswerThePublic / Answer Socrates (contenido), Ubersuggest (backlinks), GSC página 2 + Claude (mejorar rankings), indexación (GSC → Sitemaps → `site:domain`), GEO/AI Mode (15 señales + posts con outcome para Google AI Mode), mapa embebido en Contacto, canibalización.
  Método reusable: raspar perfil IG con Apify → destilar a .md con fuentes citadas → `source add`.
- **GEMALANDINGPAGES** — ID `9eb11d98-0196-43ee-8216-a4b882a219d2`. Cerebro de **landing pages de referencia** que le gustan a Javier y quiere tener a mano. Creada 2026-06-20.

## Flujo permanente: "mete este link en la gema X"
Cuando Javier envíe un **video de Instagram, una página, un reel, una URL, etc.** para guardarlo en una gema:

1. **Identificar la gema destino** (GEMSEOINNOVART para SEO; GEMALANDINGPAGES para landings de referencia; o la que indique).
2. **NotebookLM NO traga URLs de Instagram/redes** (muro de login → error "behind a paywall / requires authentication"). Tampoco contenido que requiera sesión.
3. Por eso: **destilar primero el contenido yo mismo**:
   - Video/reel → skill [[skill-ver-videos]] (fotogramas + transcripción).
   - Página web pública → leer/extraer su contenido.
4. **Crear un .md destilado** con: resumen, método/puntos clave, transcripción si aplica, y **la cita de la fuente** (URL original) bien visible. Guardar copia local en `~/.claude/notebooklm-sources/<NOMBRE_GEMA>/`.
5. **Subirlo a la gema**: `notebooklm source add "<ruta.md>" -n <ID_gema> --json`.
6. Verificar `notebooklm source list -n <ID_gema>` (status `ready`) y **borrar cualquier stub roto** del intento de URL directa.

**Por qué:** así el contenido queda buscable dentro de la gema y siempre con su fuente citada, sorteando el bloqueo de NotebookLM a redes sociales.

**Cómo aplicar:** si Javier solo manda un link y dice "a la gema", asumir este flujo sin preguntar; solo confirmar a qué gema si es ambiguo. Las URLs públicas (no-login) se pueden intentar directo con `source add <url>`, pero ante error, destilar y subir .md.

## Notas
- Las gemas de NotebookLM viven en **Google**, NO en el cerebro Obsidian. Son para procesar/conversar fuentes. Si algo merece quedar en memoria persistente, destilarlo aparte al cerebro Obsidian.
- Historial previo de extracción de notebooks: ver [[notebooklm/INDEX.md]].
