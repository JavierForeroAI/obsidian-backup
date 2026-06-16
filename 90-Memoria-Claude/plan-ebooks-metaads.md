---
name: plan-ebooks-metaads
description: Plan de marketing validado para captar TOFU masivo con ebooks en Meta Ads (capa sobre la respuesta directa) — arquitectura de campañas, audiencias, creativos/copy, nurture+scoring, economía del funnel y secuencia de ejecución
metadata:
  type: project
  updated: 2026-06-15
  entregable_html: /Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/Plan-Marketing-Ebooks-MetaAds-Innovart.html
  copia_downloads: /Users/javierforero/Downloads/Plan-Marketing-Ebooks-MetaAds-Innovart.html
---

# Plan de Marketing — Ebooks como Motor TOFU en Meta Ads

> Companion de [[academia-capilar-ecosistema]]. Valida y operacionaliza la idea de Javier: captación masiva de usuarios vía **ebooks** para alimentar el TOFU y traer leads desde otra perspectiva. Construido 2026-06-15 con 4 piezas en paralelo (arquitectura Meta, creativos+copy, nurture+scoring, medición+economía) + filtro `medical-compliance-copy`. Calibrado al **gasto real Meta mayo 2026** (vía MCP meta-dajf).

## Veredicto: VÁLIDA con 4 condiciones no negociables
1. **Capa, no reemplazo.** El BOFU de respuesta directa actual (CTWA/Lead Forms → WhatsApp) es piso intocable; el ebook es capa TOFU incremental encima. El ebook = combustible del algoritmo (señal de primera parte), no "campaña de descargas".
2. **Nunca optimizar por la descarga.** Optimizar por `Schedule` donde haya volumen (BGTA, MEDELLIN), o por `Lead` cualificado **sembrado con lookalike de compradores** donde no (PANAMA, Barranquilla, Bucaramanga). Purchase nunca como evento de conjunto (no llega a 50/sem); solo valor CAPI + semilla lookalike.
3. **Nurture + lead scoring ANTES de escalar gasto.** Separar curioso de candidato real. El motor ataca además el show rate <40%.
4. **Arreglar tracking primero (bloqueante).** UTMs al 95%+ (hoy 0% en 176 ads, ver [[reporte-utm-junio-2026]]) + migrar funnel CAPI intermedio (Contact/Schedule/ViewContent/NoShow) a webhook ([[integracion-ghl-meta-capi]] · [[capi-webhook-worker]]). Purchase ya validado ✅ 2026-06-14 ([[auditoria-capimetaghl-base]]).

## Riesgo central
Era Andrómeda/Advantage+: si pides "descargas", Meta trae cazadores de PDFs, no compradores de COP 8M. Antídoto = evento de optimización profundo + lookalike de compradores como semilla, no la oferta del ebook.

## Arquitectura Meta (resumen)
- Estructura por cuenta-ciudad (6 cuentas, USD vs COP): 1 campaña TOFU-Ebook (CBO, Advantage+) + 1 MOFU (ABO) + las BOFU existentes intactas.
- TOFU broad consolidado + conjunto lookalike compradores 1-3%. MOFU = retargeting de quien descargó/leyó y no agendó.
- Custom Audiences a crear CA-1..CA-7 (compradores, agendadores, descargadores, lectores blog, abrió-no-agendó, engagers, **video viewers 960K+ desaprovechados**).
- Nomenclatura: `ebook-[temp]-[ciudad]-[pilar]-[tema]-[periodo]` con UTMs desde el día 1.

## Creativos (ver [[avatares-clientes]] · [[angulos-creativos]])
- Matriz ebook × avatar: E1 imán amplio (cold broad), E5 mayor intención (MOFU/decisor), E4 nicho (Gay Premium). Gubernamental solo primario en E5.
- Copy deck de 3 campañas (A=E1 cold, B=E5 decisor, C=E4 emocional) ya validado por compliance.

## Economía (1 USD = 4.000 COP; USD y COP separados)
- Caso BASE (USD 5.000/COP 20M, 1 sede): descarga→cirugía ~0,66% → ≈23 cirugías, CAC ≈ USD 217/COP 869K, **ROAS ≈9,2x**.
- 3 escenarios/mes: Conservador (USD 3K/COP 12M → ~4 cirugías, ROAS 2,7x) · Base (USD 8K/COP 32M → ~37, 9,3x) · Optimista (USD 15K/COP 60M → ~208, 27,7x; techo teórico).
- Nodos frágiles: **% lead cualificado** y **show rate**. Si cae a "descargadores puros" (LQ 6%, show 35%) → ROAS 1,3x = matar.
- Probar ciclo largo: cohortes por mes de descarga (juzgar a mes+3/+4), ventana negocio 90-120d en GHL, geo-holdout.

## Secuencia de ejecución (5 fases)
- **Fase 0 (sem 1-2, bloqueante):** arreglar tracking (UTMs + CAPI funnel) + crear CA-1..7 + lookalike compradores.
- **Fase 1 (sem 2-3):** nurture + lead scoring + WF-CITA/WF-NOSHOW (ataca show rate ya). Quick win: reactivar casi-clientes + no-shows con E5 sobre las 160K+ opps ([[crm-funnel]]).
- **Fase 2 (sem 3-5):** producir E2 + E5, lanzar TOFU Conservador 1-2 sedes (CTWA + Instant Form cualificado).
- **Fase 3 (sem 5-12):** validar por cohortes; escalar 20%/sem solo si CPLQ y ROAS aguantan.
- **Fase 4 (sem 12+):** replicar E1/E3/E4 + nurtures, más ciudades, migrar a optimización por evento profundo (≥50 Purchase/sem → Schedule/Purchase + VBB).

## Cumplimiento
Todo copy por [[restricciones-lenguaje]] + skill `medical-compliance-copy`. Prohibido "garantía vitalicia" (usar "garantía de resultado"), "garantizado/100%", "cura", "resultados inmediatos". Disclaimer obligatorio en anuncios con resultados: "Resultados individuales. Consulta médica requerida. Innovart Medical IPS — registro sanitario vigente." Before/after solo bajo [[before-after-strategy]].
- ⚠️ Deuda: `20-Pauta/avatares-m4-canvas.md` aún contiene "garantía vitalicia" (líneas 326, 328, 340, 352) → corregir.

Ver también: [[academia-capilar-ecosistema]] · [[avatares-clientes]] · [[stack-pauta]] · [[crm-funnel]] · [[reporte-utm-junio-2026]] · [[integracion-ghl-meta-capi]] · [[auditoria-capimetaghl-base]] · [[blog-salud-capilar-drive]]
