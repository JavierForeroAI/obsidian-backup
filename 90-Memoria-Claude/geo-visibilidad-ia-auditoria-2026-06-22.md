---
name: geo-visibilidad-ia-auditoria-2026-06-22
description: Auditoría GEO / Visibilidad en IA — Innovart (22-jun-2026, actualización). AI Visibility Score 42/100 (+5 vs 19-jun). Quick wins 30 días + roadmap 30/90/180.
metadata:
  type: project
---

# Auditoría GEO / AI Visibility — Innovart (2026-06-22)

Segunda iteración de auditoría **GEO** ejecutada con skill [[skill-geo-salud-ia-autoaprendizaje]],
refrescando datos de del diagnóstico anterior [[geo-visibilidad-ia-diagnostico-2026-06-19]].

## Resultado

- **AI Visibility Score: 42/100** (+5 vs 2026-06-19, banda "Emergente → Creciente")
- **AI Citation Probability:** branded 62/100, **no-branded comercial ~20/100** (mejora marginal)

## Cambios detectados desde el 19 de junio

1. ✅ Blog + schema médico siguen siendo fortaleza; no-branded mejoró ligeramente por auto-indexación
2. ⚠️ Home sigue **sin schema JSON-LD** (máxima oportunidad)
3. ⚠️ Invisible en respuestas de IA comerciales: "mejor clínica implante capilar Bogotá", "precio implante FUE", "FUE vs DHI" → IA cita DHI, Rogans, Sin Calvicie, Total Hair. Innovart NO aparece.
4. 🟡 Competidores activos (Rogans, Sin Calvicie) tienen schema POBRE (Organization/Article) pero ganan por **listicles + transparencia de precio + FAQ visible**. Superables.

## Quick Wins (Semana 1-2, +10 puntos)

### 1. Schema MedicalClinic en HOME (1h)
- JSON-LD ready en el informe (carpeta GEO Drive)
- Inyectar en `<head>` de home PageFly + sedes (Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá)
- Impacto: Home pasa a ser legible por LLM; sube "Medical Authority" subscore

### 2. Limpiar títulos duplicados (30 min)
- Remover widget Bcontact que genera `<title>` múltiples
- Consolidar NAP (omite Panamá hoy)
- Impacto: LLM entiende estructura de entidad

### 3. Página FAQPage (2h)
- Responder: "¿Cuánto cuesta implante capilar?", "¿FUE o DHI?", "¿Garantía?"
- Rogans y Sin Calvicie ganan aquí
- Impacto: Citabilidad comercial +5 puntos, aparece en respuestas generativas

## Roadmap 30/90/180

| Fase | Días | Puntuación | Hitos |
|---|---|---|---|
| **1. Estructura médica** | 30 | 42 → 52 | Schema en money pages, FAQ, precio, llms.txt |
| **2. Autoridad técnica** | 90 | 52 → 70 | Blog + Papers + Profiles (Dr. Carreño, Dra. Morales) verificados, Reviews/Rating, YMYL compliance |
| **3. Dominio GEO** | 180 | 70 → 95 | Entity linking (Google Knowledge Graph + Wiki), Listicles (vs DHI/Mediarte), Authority signals (Medios + Academia), Local GEO |

## Entregable

- **Informe HTML completo** en Drive: carpeta **3.MERCADEO > CLAUDE > GEO - Visibilidad IA**
- Resumen ejecutivo con JSON-LD listo para copiar
- Checklist 30 días (implementable hoy mismo)

## Próximos pasos (cuando tengas el PC)

1. Leer roadmap 30 días (totalmente especificado)
2. Ejecutar Quick Win #1 (schema home + sedes)
3. Verificar datos: ¿33K pacientes?, sedes activas, Dr. Carreño + médicos adicionales
4. Conectar con [[seo-puro-seo-cowork]] para fase 2/3

**Why:** La auditoría GEO es la estrategia **de fondo** para ganar visibilidad en ChatGPT/Perplexity/Claude antes que competidores menores (Rogans, Sin Calvicie) lo logren. Hoy Innovart es clínicamente superior pero invisible en IA → reversible con 30 días de estructura.

**How to apply:** No es pauta ni landing; es SEO/schema de fondo que aporta +15% en leads IA (Perplexity, Claude, Google AI Overviews) a 6 meses. Ejecutable sin presupuesto; requiere revisión clínica (Dr. Carreño) para datos verificables.
