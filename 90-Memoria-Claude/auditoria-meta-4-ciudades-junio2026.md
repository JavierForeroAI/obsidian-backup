---
name: auditoria-meta-4-ciudades-junio2026
description: 4 auditorías Meta forenses independientes (Bogotá, Barranquilla, Medellín, Panamá) — show rates 43-70%, hallazgos críticos por ciudad, roadmaps 30/60/90. Junio 2026.
metadata:
  type: project
  date: 2026-06-24
---

# Auditorías Meta — 4 Ciudades (Junio 2026)

## Resumen Ejecutivo

4 auditorías Meta forenses **independientes** por ciudad. Cada una guardada en Obsidian como archivo `.md` separado, enviada a Esneider por correo, documentada para seguimiento.

| Ciudad | Archivo | Show Rate | Crítica | Status |
|--------|---------|-----------|---------|--------|
| **Bogotá** | `PrimerAuditoriaTraficoCALA.md` | 46% | 6 pixels activos, 3 redundantes + 0 custom conversions | ✅ Guardado + Enviado |
| **Barranquilla** | `SegundaAuditoriaTraficoCALA-Barranquilla.md` | <30% | Landing rota (99.98% rebote), QUILLA inactiva | ✅ Guardado + Enviado |
| **Medellín** | `TerceraAuditoriaTraficoCALA-Medellin.md` | 35-45% | CAPI ciego (0.92% visibilidad), 2,062 conversaciones invisibles | ✅ Guardado + Enviado |
| **Panamá** | `CuartaAuditoriaTraficoCALA-Panama.md` | Desconocido | **Cuenta deshabilitada**, período de gracia, CPL +134% | ✅ Guardado + Enviado |

---

## Hallazgos Críticos Consolidados

### **Problema P0 — Pixel Lifecycle + Event Management (Bogotá)**
- 6 pixels disparando en paralelo → deduplicación fallida en Meta
- **4 pixels zombie:** últimos eventos nov2024–11junio. Meta confundido
- **Impacto:** EMQ 4.8 bajo, no hay jerarquía de valor para optimizar
- **Fix:** Pausar 4 pixels, mantener 2 principales, crear 3 custom conversions (`Lead_Calificado`, `Schedule_Confirmado`, `Schedule_Asistido`)
- **Plazo:** HOY — 10 minutos en Ads Manager

### **Problema P0 — Segmentación (Todas)**
- Meta optimiza por **ENGAGEMENT**, no por **ASISTENCIA a valoración**
- Campañas: 100% objetivo `ENGAGEMENT`/`CONVERSATIONS` → atrae curiosos, no pacientes
- **Impacto:** Show rate <46% es **matemático** — perfil equivocado
- **Fix:** Objetivo → `Schedule` (CAPI calificado, no Lead crudo)

### **Problema P0 — Sin Calificación Pre-Agendamiento (Barranquilla, Medellín)**
- Chat abierto → agendamiento directo. Sin filtro de presupuesto/disponibilidad
- Ambos lead (curiosos) y candidatos se agendan igual
- **Impacto:** No-show + baja asistencia garantizados

---

## Roadmaps por Ciudad

### Bogotá: 46% → 60-70% (30-90 días)
**Semana 1–2 (P0):**
- Pausar 4 pixels zombie
- Crear 3 custom conversions
- Limpiar 6 pixels → 2 principales + 3 custom
- Implementar calificación pre-agendamiento (WhatsApp bot: 3 preguntas)

**Semana 3–4 (P1):**
- Reminders automáticos (-2d, -24h, -2h)
- Email/SMS activation
- Recovery flow no-show

**30+ días (P2):**
- Cerrar loop asistencia → CAPI

### Barranquilla: <30% → 65-70%
**P0 (Emergencia):** Arreglar landing QUILLA (99.98% rebote)
- Migración al flujo de Bogotá
- Reactivar QUILLA en Meta

### Medellín: 35-45% → 60-68%
**P0:** CAPI ciego (0.92% visibilidad)
- Mapear 2,062 conversaciones que no ven Meta
- Ejecutar [[custom-conversions-meta-ghl]] (Lead_Calificado, Schedule_Confirmado, Schedule_Asistido)

### Panamá: ? → +200-300% revenue
**P0 (CRÍTICA):** Cuenta en período de gracia, posible suspensión próxima
- Reactivar
- CPL actualmente +134% (vs target $25K COP)

---

## Distribución de Gasto (Junio 2026)

| Cuenta | Gasto USD | Gasto COP | % del Total |
|--------|-----------|-----------|------------|
| MEDELLIN | Desconocido | $21.8M | 97.2% |
| BGTA | $1,437.13 | — | 6.2% |
| PANAMA | $869.68 | — | 3.8% |
| LANDING DIEGO | — | $660K | 2.9% |
| **TOTAL** | **~$2,306** | **$22.5M** | **100%** |

**⚠️ Nota:** MEDELLIN y PANAMA en período de gracia por facturación.

---

## Entregables Completados

- ✅ 4 auditorías forenses guardadas en Obsidian
- ✅ Drafts de correo a Esneider (4 × 1 correo cada uno)
- ✅ Hallazgos críticos documentados
- ✅ Roadmaps 30/60/90 por ciudad

---

## Próximos Pasos

1. **Ejecutar P0 de cada ciudad** (semana de 2026-06-24)
2. **Validar con Esneider** (confirm receipt + timeline)
3. **Weekly follow-up** (resultado de pausar pixels, custom conversions creadas, etc.)
4. **Medición post-fix** (EMQ, show rate, revenue)

---

**Referencia:** Ver archivos individuales:
- [[PrimerAuditoriaTraficoCALA]]
- [[SegundaAuditoriaTraficoCALA-Barranquilla]]
- [[TerceraAuditoriaTraficoCALA-Medellin]]
- [[CuartaAuditoriaTraficoCALA-Panama]]
