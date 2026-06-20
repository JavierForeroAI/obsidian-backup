---
name: proyecto-reimpacto-ebooks-faq
description: Proyecto ejecutado (2026-06-19) — 8 ebooks técnicos FAQ de implante capilar + estrategia de reimpacto leads fríos/tibios + mensajes listos para GHL API. Construido con equipo multiagente.
metadata:
  type: project
  updated: 2026-06-19
  carpeta: /Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/ebooks-faq/
  copia_downloads: /Users/javierforero/Downloads/Ebooks-FAQ-Innovart/
  indice_html: /Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/ebooks-faq/index.html
---

# Proyecto Reimpacto — 8 Ebooks Técnicos + Estrategia GHL

> Ejecutado (no es plan) el 2026-06-19 con equipo multiagente (workflow `innovart-ebooks-faq-reimpacto`, 11 agentes). Reactiva leads fríos/tibios de las ~160K+ opps dormidas ([[crm-funnel]]) usando ebooks técnicos como **excusa de valor**, no oferta de venta. Companion de [[plan-ebooks-metaads]] y [[academia-capilar-ecosistema]].

## Entregables (todos en la carpeta `ebooks-faq/` + copia en Downloads)
**8 ebooks HTML** (1.879–2.820 palabras c/u, diseño Innovart, FAQ reales, cumplimiento verificado: 0 términos prohibidos, los 8 con disclaimer):
- E01 frío — ¿Duele el implante? (dolor/anestesia) · E02 tibio — FUE vs DHI · E03 tibio — ¿Cuántos folículos? (zona donante, "fórmula del pelazo" / Valor de Cobertura) · E04 frío — El día del implante y los 8 días siguientes · E05 tibio — ¿Cuándo veré mi cabello? (shedding 3-18 meses) · E06 frío — ¿Soy candidato? · E07 tibio — ¿Cuánto cuesta y cómo pagarlo? (financiación 90%) · E08 frío — Proteger tu inversión (plan médico)
- Archivos: `ebook-faq-0X-slug.html` · índice navegable: `index.html`
- **CTAs comerciales (2026-06-19):** cada ebook tiene botón flotante WhatsApp, barra de conversión bajo la portada, 3 CTAs contextuales, CTA final doble (WhatsApp + web) y footer con link a la web. Navegación a `https://www.innovartmedical.com` con UTMs (`utm_source=ebook&utm_medium=guia&utm_campaign=reimpacto&utm_content=eNN`); conversión por WhatsApp `wa.me/573124565014`.
- `00-estrategia-reimpacto.md` y `00-mensajes-ghl-api.md`

## Estrategia de reimpacto
- **Segmentación:** FRÍO (3 sub: F1 curioso TOFU, F2 dormido +60-90d, F3 dudas candidatura) vs TIBIO (5 sub: T1 no-show, T2 pareja/casi-cliente, T3 precio/MeddiPay, T4 cancelado, T5 vacaciones). Reglas de smart list + tags `reimp_*` por sede. **Excluir operados** (cruce pipeline Operaciones, won roto).
- **Mapa ebook→segmento:** fríos = E01/E04/E06/E08 (educación); tibios = E02/E03/E05/E07 (decisión). 1 ebook por toque.
- **Cadencia:** fríos con re-permiso ("responde SÍ"), máx 3 ebooks (D0/D2/D5/D9/D14); tibios directos y ágiles (D0/D3/D7/D12). Horario mar-sáb 10-12 y 15-18. Olas 500-1000/día/sede (salud WABA, alerta optout >2-3%).

## Mensajes GHL API (listos para pegar)
- Secuencia FRÍA (7 toques) + TIBIA (7 toques), mezcla WhatsApp/Email. Banco de 8 ganchos (1 por ebook), 5 respuestas a objeciones (dolor/precio/lo-pensaré/lejanía/naturalidad), mensajes de conversión a valoración, recordatorio 24h/3h y no-show. Tuteo colombiano, disclaimer en cada mensaje con resultados.
- Placeholders: `{{contact.first_name}}`, `{{ebook_link_e01..e08}}` (trigger links), `{{link_agenda}}`, `{{appointment.start_time}}`.

## Mecánica GHL (cómo se envía por API)
- 1 workflow por segmento por sede (`WF-REIMP-FRIO/TIBIO-[sede]`). Enrolar por smart list + tag (`bulk_add_to_workflow`).
- Enviar = acción WhatsApp (WABA sede); escuchar = `message.type==2` (SMS applevel, NUNCA 19) — ver [[feedback-whatsapp-applevel-sms]].
- Ebooks como **trigger links** medibles (`create_trigger_link`) → clic = +score + avanza secuencia. Scoring: respuesta +15, clic ebook +10, clic agenda +25. Umbral `score>=70` o intención → handoff a Sofia (`ai_parar`).
- Agenda → Schedule CAPI; cirugía → Purchase CAPI ([[integracion-ghl-meta-capi]] · [[capi-webhook-worker]]).
- `conversationProviderId` = `628f88b07cf43a7641c58089`.

## Pendiente para activar (3 pasos)
1. Hospedar los 8 ebooks (Shopify/host) + crear trigger links por sede.
2. Montar en GHL: tags + smart lists + workflows WF-REIMP con los mensajes + aprobar templates WhatsApp ([[whatsapp-templates-ghl]]).
3. **Quick win:** primera ola a T1 no-show + T2 casi-cliente con E05/E07.
- Pre-requisito transversal: medición de clic (hoy 0% UTMs en 176 ads, [[reporte-utm-junio-2026]]).

## Fuentes técnicas usadas
NotebookLM: [[100-preguntas]] · [[libro-alopecia]] · [[escuela-alopecia]] (Dr. Muñoz/Carlos) · [[geminnovart]] (la Gema) + investigación web de FAQ.

Ver también: [[plan-ebooks-metaads]] · [[avatares-clientes]] · [[restricciones-lenguaje]] · [[crm-funnel]] · [[stack-pauta]]
