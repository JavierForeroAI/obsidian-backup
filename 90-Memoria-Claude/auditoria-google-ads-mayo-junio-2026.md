---
name: auditoria-google-ads-mayo-junio-2026
description: Google Ads Health Score 26/100 (Grado F). Mayo-Junio 2026 — 11 hechos bloqueantes + 10 quick wins.
metadata:
  type: project
  date: 2026-06-26
  status: auditoria-completa-roadmap-listo
---

# GOOGLE ADS — AUDITORÍA MAYO-JUNIO 2026

**Health Score: 26/100 (Grado F)**

## Resumen Ejecutivo

| Métrica | Mayo | Junio | Tendencia |
|---------|------|-------|-----------|
| Gasto | $932 USD | $1,321 USD (proyectado) | ↑ +75.9% |
| CTR | 7.24% | 6.22% | ↓ -14% |
| CPC | $88 COP | $116 COP | ↑ +31.8% |
| Conversiones reportadas | 11,430 | 11,107 | -1.4% (sin valor real) |
| **Revenue atribuido** | **$0** | **$0** | **Sin cambio** |
| Impression Share | 24.6% | 37.1% | Mejor pero =60% perdida |

**Tendencia:** Gastando MÁS dinero en un sistema ROTO. Junio está peor que mayo.

---

## 🔴 TOP 5 BLOQUEANTES P0

### P0-1: CONVERSION TRACKING = $0
Google reporta 11,403 "conversiones" a COP $299 (~$0.07 USD) cada una. **Imposible para cirugía $8-11M COP.**

**Causa:** Sin definición de conversión primaria = lead real en GHL.

**Fix (1 hora):** 
- Definir 1 conversión = Lead real en GHL
- Asignar valor COP 200,000
- Actualizar todas las campañas

---

### P0-2: CERO LISTAS NEGATIVAS
11.3% del gasto Search junio (~COP 135K) se quema en:
- Shampoo, medicamentos, B2B
- "Medical care", "hair growth"
- Competencia (sin negativo)

**Fix (15 min):** Crear lista compartida (25 términos), aplicar a todas campañas.

---

### P0-3: PIERDES 60-75% DE SUBASTAS POR AD RANK
- **PMax:** Ganas 37% de subastas, pierdes 60% por bajo calidad
- **MED Search:** Pierdes 51% por presupuesto + 43% por rank

**Fix:** Mejorar Quality Score ANTES de escalar presupuesto.

---

### P0-4: TARGET CPA FICTICIO
**MED Search:** Target $0.97 USD para cirugía $8M COP. Imposible.

**Fix:** Cambiar a COP 150,000 cuando resuelvas P0-1 (conversión real).

---

### P0-5: 4 DE 6 CIUDADES SIN COBERTURA
Solo activas: Bogotá (PMax), Medellín Search (new), Panamá.
Sin activas: Barranquilla, Cali, Pereira.

**Fix:** Activar Barranquilla + Cali en mes 2.

---

## ⚡ TOP 10 QUICK WINS (1–4 semanas)

| # | Acción | Tiempo | Semana | Impacto |
|---|--------|--------|--------|---------|
| 1 | Crear lista negativa compartida | 15 min | 1 | CTR +0.5pp, CPC -5% |
| 2 | Definir conversión primaria (lead GHL) | 30 min | 1 | ROAS +35%, CPA visible |
| 3 | Audit Quality Score + mejorar ads | 2 hrs | 1 | Impression Share +15% |
| 4 | Agregar 3 headlines por ad + pruebas | 1 hr | 1–2 | CTR +1.2pp |
| 5 | Recalibrar Target CPA (COP 150K) | 15 min | 2 | Conversiones +30% |
| 6 | Activar Search Barranquilla | 45 min | 2 | Leads +40 |
| 7 | Audit keywords + remover low QS | 2 hrs | 2–3 | CPC -8%, ROI +20% |
| 8 | Smart Bidding: Maximize Conv. Value | 30 min | 3 | CPL +5%, volumen +15% |
| 9 | A/B test landing page por geo | 3 hrs | 3–4 | Conversion rate +8% |
| 10 | Reporte semanal automatizado | 2 hrs | 4 | Visibilidad KPIs |

---

## 📊 Estado por Campaña (Junio)

### PMax Bogotá
- Gasto: COP $2.2M (~$539 USD)
- Leads: 4,200 (micro-eventos, no leads reales)
- CPA: $0.12 (ficticio)
- Status: **Optimizando por ruido, no valor**

### Search Medellín (nuevo)
- Activo desde ~Jun 15
- Gasto: COP $1.8M (~$443 USD)
- CPA Target: COP $3,998 ($0.97) ← **INVIABLE**
- Status: **Arranque incorrecto, necesita recalibración**

### Panamá (bloqueada)
- Sin datos recientes
- Status: Probablemente pausada

---

## 🎯 Plan de Acción — Semana 1 (1.5 horas)

1. **Abrir Google Ads Manager** → Campaña MED Search
2. **Crear lista negativa:**
   - Copiar 25 términos negativos
   - Crear lista compartida "Innovart Negatives"
   - Aplicar a PMax + Search
3. **Actualizar Conversion Tracking:**
   - Goal: Lead real en GHL (teléfono + formulario)
   - Conversión primaria = Lead
   - Valor: COP 200,000
4. **Mejorar Ad Copy:**
   - Agregar 3 headlines por ad
   - Incluir CTA claro (Agendar, Consultar, Cotizar)
5. **Recalibrar Target CPA:**
   - Cambiar MED Search a COP 150,000
   - Mantener pero observar

---

## Comparativa Meta vs Google Ads

| Aspecto | Meta | Google |
|---------|------|--------|
| Gasto acumulado | $26.8M COP/mes | $1.3M COP/mes (2.1% |
| Formato principal | Video + carrusel | Search keywords |
| ROI aparente | ROAS 0x (sin revenue real) | ROAS 0x (idem) |
| Bloqueo principal | EMQ 4.9 + fbclid | Conversion tracking $0 |
| Quick win | Resetear EMQ + UTMs | Definir conversión real |

**Conclusión:** Ambos canales están ciegos. Meta es 20x mayor pero identicamente roto.

---

## 📋 Roadmap 30/60/90

### 30 días (Quick Wins 1–5)
- Listas negativas viva
- Conversión real definida
- Quality Score mejorado
- Barranquilla activada

**Expected:** Health 26→45 (Grado C), CPL -15%, leads +40%.

### 60 días (Consolidación)
- A/B testing por geo
- Automation Smart Bidding
- Keyword cleanup
- Landing page optimization

**Expected:** Health 45→62 (Grado B), ROI visible, CPL estable.

### 90 días (Escala)
- Expandir a Cali, Pereira
- Budgets aumentados (condicionado a ROI)
- Feed dinámico (si viable)
- Reporting automático

**Expected:** Health 62→75 (Grado B+), leads +200%, ROI 3-5x.

---

## 📌 Notas Finales

1. **Sin definición de lead real**, Google Ads no puede optimizar → sigue ciega
2. **Listas negativas son low-hanging fruit** — 15 min por 5% CTR
3. **Conversion value es MÁS importante que volume** — quality over quantity
4. **Plan viable: Semana 1 fixes P0 + Quick Wins 1–5** — 8 horas trabajo
5. **Relacionado:** Conectar con [[diagnostico-dm-fbclid-2026-06-26]] — fbclid perdido en DM también afecta Google Ads attribution

---

**Status:** Auditoría completa. Roadmap listo. Bloqueante: Javier necesita autorizar fixes P0-1 (conversión tracking) e iniciar Semana 1.

**Owner:** Esperando instrucción. Script `innovart-google-ads-audit-diario.py` puede automatizar reporte semanal si lo autorizas.
