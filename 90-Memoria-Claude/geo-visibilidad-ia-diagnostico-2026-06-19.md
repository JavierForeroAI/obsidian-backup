---
name: geo-visibilidad-ia-diagnostico-2026-06-19
description: Diagnóstico GEO/visibilidad en IA de Innovart (19-jun-2026). AI Visibility Score 37/100. Invisible en respuestas generativas comerciales; home sin schema; competidores ganan por listicles+precio, no estructura. Roadmap 30/90/180. HTML en Drive + correo enviado.
metadata:
  type: project
---

# Diagnóstico GEO — Visibilidad en IA de Innovart (2026-06-19)

Primera auditoría de **Generative Engine Optimization (GEO)** de Innovart, hecha con la
skill [[skill-geo-salud-ia-autoaprendizaje]]. Basada en inspección real de huella digital
(no opinión): schema/robots/llms/sitemap/meta + comparativa de schema vs competidores +
pruebas de citabilidad con búsqueda en vivo.

## Resultado
- **AI Visibility Score: 37/100** (banda "Emergente"). Subscores: Citability 20 · GEO
  Readiness 30 · Knowledge Graph 35 · Brand Consistency 38 · Semantic 40 · Entity 45 ·
  Trust 50 · Medical Authority 58.
- **AI Citation Probability:** branded 62/100, **no-branded comercial 18/100** (lo que mueve negocio).

## Hallazgos clave (con evidencia)
- 🔴 **Home (PageFly) con 0 schema JSON-LD.** La página más enlazada es ilegible como entidad para LLM.
- 🔴 **Invisible en respuestas generativas comerciales:** "mejor clínica implante capilar Bogotá"
  → IA cita DHI, Capilix, Rogans, Mediarte, Sin Calvicie. Consultas de precio → Rogans, Sin Calvicie,
  Capilclinic. Innovart no aparece.
- 🟢 **Oportunidad grande:** competidores que la IA recomienda (DHI, Mediarte) tienen schema POBRE
  (solo Organization/Article). El **blog de Innovart ya tiene schema médico más rico** (MedicalOrganization,
  MedicalProcedure, Person, PostalAddress) que sus homes → propagarlo a money pages para superarlos.
- 🟡 Colisión de entidad ("Clinica Innovart" / "Innovación capilar" España).
- 🟡 NAP inconsistente (la home omite Panamá). `<title>` duplicados filtrados (widget Bcontact).
- 🔴 **"Garantía vitalicia"** (PROHIBIDA, ver [[restricciones-lenguaje]]) aún en Top Doctors y la IA la repite.
- Anclas de entidad existentes: Top Doctors (centro + Dr. Fabián Carreño), YouTube, TikTok. 2º médico: Dra. Gloris Morales [VERIFICAR].

## Quick wins (30 días)
1. Schema `MedicalClinic`/`MedicalOrganization` en home+sedes (JSON-LD listo en el informe).
2. Página de **precio/transparencia** + `FAQPage` (donde hoy gana Rogans).
3. Unificar NAP/sedes + eliminar "garantía vitalicia" en todas las superficies.
4. Publicar `llms.txt` médico.

## Entregable
- HTML 12 entregables en Drive: carpeta **GEO - Visibilidad IA** (`1TeMVcOu4cdSsrt6BzjzAfo0iNiCYqTIA`,
  bajo 3.MERCADEO/CLAUDE). Archivo `1V9gkkWpq081sibod6wIuOj0T94kBNWag`. Copia local en `~/Downloads/GEO-Innovart/`.
- Correo resumen email-safe enviado a innovartmedicalips@gmail.com (vía SMTP).

## Pendiente (implementación)
Aún no ejecutado en la web: inyectar schema (ojo Shopify/PageFly sobrescribe `<head>` —
ver [[shopify-ecosistema-mcp]]), crear página de precio, perfiles `Physician`, comparativas
FUE vs DHI, `AggregateRating`. Verificar datos `[VERIFICAR]`: nº pacientes (¿33.000?), sedes
activas, reseñas, registros médicos. Conecta con el plan [[seo-puro-seo-cowork]].
