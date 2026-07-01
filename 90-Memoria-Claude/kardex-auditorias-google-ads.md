---
name: kardex-auditorias-google-ads
description: Kardex histórico de auditorías de Google Ads — qué se encontró, qué se aplicó, qué funcionó y qué no. Ejercicio de evolución cuenta a cuenta.
metadata:
  type: project
  cuenta: "9275722919 (Innovart medical IPS, MCC 2084232674)"
  estado: ACTIVO
  fecha_inicio_kardex: 2026-06-30
---

# KARDEX — Auditorías Google Ads Innovart

**Documento central de evolución.** Cada auditoría registrada con: QUÉ se encontró + QUÉ se recomendó + QUÉ se aplicó + RESULTADO en la siguiente auditoría. El objetivo es poder comparar auditoría vs auditoría y ver objetivamente qué funcionó y qué no.

**Ver también:** [[auditoria-google-ads-mayo-junio-2026]] (auditoría previa basada en CSV, Health Score 26/100), [[google-ads-mcp-conexion]], [[google-ads-guia]], [[criterio-google-ads-innovart-global-local]].

---

## AUDITORÍA #1 — 2026-06-30 (primera auditoría vía MCP en vivo)

| Campo | Valor |
|-------|-------|
| **Fecha** | 2026-06-30 |
| **Fuente de datos** | Google Ads MCP oficial (solo lectura), en vivo — no CSV exportado |
| **Período analizado** | Últimos 30 días |
| **Documento** | `~/Desktop/primerauditoriagoogle.html` |
| **Estructura de cuenta al momento** | Bogotá = único PMax + conversión ($130.000/día). Medellín = Search puro ($61.426/día). Panamá = Search puro ($105.600/día). Barranquilla = Search pausada. 10 campañas legacy pausadas. |

### Hallazgos clave

| # | Hallazgo | Severidad | Evidencia |
|---|---|---|---|
| 1 | **Conversiones fantasma en PMax Bogotá** — 11.790 conversiones/30d sobre 50.435 clics (~23%), tasa fisiológicamente imposible para cirugía capilar | 🔴 P0 | CPC promedio $74 COP (absurdamente bajo) → sugiere Display/Discover de baja calidad + mismo patrón que `SubmitApplication Fantasma` ya confirmado en Meta |
| 2 | **Keywords activas apuntando a "Cali"** en campaña de Medellín | 🔴 P0 | Cali NO es sede real (ver [[regla-sedes-definitivas]]) — gasto desperdiciado + riesgo de promesa falsa |
| 3 | **Cero palabras clave negativas** en toda la cuenta (ni por campaña ni lista compartida) | 🔴 P0 | Mismo hallazgo que auditoría mayo-junio — sigue sin resolver |
| 4 | Gasto en términos irrelevantes: cosméticos (l'oréal, spectral men, tónico rapunzel), B2B ("empresas de dispositivos médicos"), genéricos ("medical care", "hair growth") | 🟠 P1 | ~$49.000 COP identificados en una sola pasada de 30 días |
| 5 | Impression Share bajo — MED 9,99% (pierde 47% por presupuesto + 47% por ranking), PAN 25,7% (pierde 74% por ranking, 0% por presupuesto), Bogotá PMax 36% (pierde 61,7% por ranking) | 🟠 P1 | Confirma que no es solo problema de presupuesto |
| 6 | Barranquilla sigue sin fusionarse a las ubicaciones del asset group de Bogotá (PMax Bogotá solo targetea "Bogotá, ciudad") | 🟠 P1 | Decisión pendiente de ejecutar, ya acordada por Javier |
| 7 | Google recomienda subir presupuesto PMax Bogotá $130k→$150k/día | 🟡 Info | **NO aplicar** hasta resolver hallazgo #1 (evitaría financiar más el problema) |
| 8 | 10 campañas legacy pausadas sin actividad ensuciando la cuenta | 🟢 P2 | Cosmético, no afecta gasto |

### Roadmap propuesto (aún no ejecutado a la fecha de esta entrada)

- **P0:** auditar evento `Form_success` (¿dispara con acción real o con carga de página en GHL?), no subir presupuesto de PMax Bogotá todavía, quitar keywords "Cali", crear lista de negativas compartida.
- **P1:** fusionar Barranquilla como ubicación del asset group de Bogotá, evaluar subir presupuesto de Medellín (solo después de limpiar negativas).
- **P2:** aplicar recomendaciones de Ad Strength (PMax Bogotá + RSA Panamá) y las 4 keywords sugeridas por Google para Medellín, archivar campañas pausadas.

### Estado de aplicación
⏳ **Pendiente** — ninguna acción del roadmap ejecutada aún al cierre de esta entrada. Próxima auditoría debe revisar punto por punto qué se aplicó y comparar métricas.

### Estrategia derivada — Julio 2026
A partir de esta auditoría se generó `~/Desktop/estrategia-google-julio-2026.html` (workflow multiagente: presupuesto/puja, estructura/keywords, tracking, creativos + síntesis), corregida con el criterio local de Diego (ver [[criterio-google-ads-innovart-global-local]] — targeting específico 80% / negativas defensivas selectivas 20%, no listas genéricas). Plan semana a semana: $332.000/día (sem.1) → $450-470.000/día (sem.4). La próxima auditoría de este Kardex debe comparar resultados reales contra las métricas de éxito definidas en esa estrategia (sección 7 del HTML).

---

## Plantilla para la próxima auditoría

Copiar este bloque y llenar en la siguiente pasada:

```
## AUDITORÍA #N — [fecha]

| Campo | Valor |
|---|---|
| Fecha | |
| Período analizado | |
| Documento | |

### Qué cambió desde la auditoría anterior
- [ ] Punto P0-1 (Form_success fantasma): ¿se investigó? ¿resultado?
- [ ] Punto P0-2 (Cali): ¿se quitaron las keywords?
- [ ] Punto P0-3 (negativas): ¿se creó la lista? ¿cuántos términos?
- [ ] Punto P1 (Barranquilla): ¿se fusionó la ubicación?

### Métricas comparadas vs auditoría anterior
| Métrica | Auditoría anterior | Esta auditoría | Cambio |
|---|---|---|---|
| Conversiones PMax Bogotá / clics | 23% | | |
| CPC promedio PMax Bogotá | $74 | | |
| IS Search Medellín | 9,99% | | |
| IS Search Panamá | 25,7% | | |
| Gasto en términos irrelevantes detectados | ~$49.000 | | |

### Qué funcionó / qué no
(honestidad objetiva — si algo no se aplicó o no sirvió, decirlo aquí)

### Nuevos hallazgos
```

---

**Regla de uso:** cada vez que se pida una auditoría de Google Ads nueva, LEER este Kardex primero (para no repetir trabajo y para poder comparar), y AGREGAR una entrada nueva al final siguiendo la plantilla — nunca sobreescribir entradas anteriores.
