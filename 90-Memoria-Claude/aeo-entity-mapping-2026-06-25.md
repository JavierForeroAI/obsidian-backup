---
name: aeo-entity-mapping-2026-06-25
description: Mapa completo de entidades y relaciones AEO para Knowledge Graph de Innovart. 63 entidades, 101 triples. Documento en Drive.
metadata:
  type: project
  date: 2026-06-25
  status: COMPLETADO
  drive_id: 1MYXNjecYXmLir8XPrAmSE4iLfMiR1Do1Ahl5-miKu30
---

# AEO Entity Mapping — Innovart Medical IPS

**Documento Drive:** [AEO Entity Mapping — Innovart Medical IPS (2026-06-25)](https://docs.google.com/document/d/1MYXNjecYXmLir8XPrAmSE4iLfMiR1Do1Ahl5-miKu30/edit)

## Resumen

- **63 entidades mapeadas** (Organizaciones, Personas, Lugares, Procedimientos, Condiciones, Precios, Digitales)
- **101 triples de relación** (Knowledge Graph completo)
- **Baseline AEO:** 35/100 → Target post-P0: 50-58/100 → Target 90 días: 72-85/100

## Distribución por tipo

| Tipo | Cantidad | IDs |
|------|----------|-----|
| Organizaciones | 13 | E01-E13 |
| Personas | 6 | E14-E19 |
| Lugares / Sedes | 14 | E20-E33 |
| Procedimientos médicos | 10 | E34-E43 |
| Condiciones médicas | 8 | E44-E51 |
| Precios / Comercial | 6 | E52-E57 |
| Activos digitales | 8 | E58-E63 |

## GAPs P0 más críticos (requieren acción esta semana)

1. **GBP ausentes** (5 sedes) → Knowledge Graph 0% → +30 pts AEO si se crean
2. **NAP inconsistente** (5 variantes de nombre, 3 teléfonos) → +15 pts confianza
3. **Bio Dr. Carreño** (cero credenciales públicas) → +25 pts E-E-A-T
4. **RealSelf + WhatClinic** (ausentes) → +10 pts citación internacional
5. **Snippet precio por folículo** (Rogans lo tiene, Innovart no) → +15 pts Featured Snippets
6. **Wikidata** (sameAs vacío) → +8 pts Knowledge Graph

## Grupos de triples

- **Grupo A:** Identidad central (R01-R10)
- **Grupo B:** Sedes geográficas (R11-R20)
- **Grupo C:** Procedimientos técnicos (R21-R38)
- **Grupo D:** Precios comerciales (R39-R45)
- **Grupo E:** Dr. Carreño E-E-A-T (R46-R52)
- **Grupo F:** Benchmark competencia (R53-R58)
- **Grupo G:** Condiciones → Tratamientos (R59-R65)
- **Grupo H:** NAP + Digital (R66-R72)
- **Grupo I:** Contenido adicional (R73-R101)

## Siguiente paso

Ver [[PLAN-MAESTRO-SEO-GEO-AEO-2026-06-25]] Línea C, P0:
1. Crear 5 GBP (Javier ejecuta manualmente)
2. Consolidar NAP
3. Publicar bio Dr. Carreño (Claude implementa cuando Javier provea datos)
