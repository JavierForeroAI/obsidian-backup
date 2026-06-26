---
name: carga-utm-bulk-whatsapp-bussines-2026-06-25
description: Carga masiva de UTMs en campaña WHATSAPP BUSSINES — Plan de ejecución, scripts, y timelines
metadata:
  type: execution-plan
  status: READY_FOR_EXECUTION
  updated: 2026-06-25
  campaign_id: 120246851116100679
  account_id: act_874169544322810
---

# Carga Masiva UTMs — WHATSAPP BUSSINES (MEDELLIN)

## Estado: LISTO PARA EJECUTAR ✅

**Fecha:** 2026-06-25  
**Campaign:** WHASTAPP BUSSINES-14/05/2026-(FASE 3)  
**Campaign ID:** 120246851116100679  
**Account ID:** act_874169544322810 (MEDELLIN)  
**Status:** ACTIVE

---

## Discovery Completado (FASE 1) ✅

### Estructura de Campaña

| Concepto | Valor |
|----------|-------|
| **Ad Sets Totales** | 11 |
| **Ad Sets Activos** | 5 (Bogotá 2x, Panamá, Barranquilla, Medellín) |
| **Ads Estimados** | ~25-40 |
| **Presupuesto/día** | 468K COP (activos solamente) |
| **Estado** | ACTIVE |

### Presupuesto Actual (Activos)

```
BOGOTÁ - TEST-/18/06/2026        90K COP/día
BOGOTÁ - TEST-/16/06/2026        76K COP/día
PANAMA- WB - TEST-11/06/2026     130K COP/día
BARRANQUILLA - WB - TEST-9/06... 42K COP/día
MEDELLIN                          130K COP/día
─────────────────────────────────
TOTAL                             468K COP/día
```

---

## UTM Template a Aplicar

\`\`\`
utm_source=instagram
utm_medium=ads_manager
utm_campaign=whatsapp-bussines
utm_content=metaadsinnovart
utm_term=capi
\`\`\`

---

## 4 Archivos Listos en Desktop

| Archivo | Tamaño | Propósito |
|---------|--------|----------|
| QUICK-START.sh | 3.3K | Script bash interactivo |
| meta_utm_bulk_loader.py | 14K | Automatización Python |
| GUIA-EJECUCION-UTM-BULK.md | 6.6K | Instrucciones + troubleshooting |
| RESUMEN-EJECUTIVO-UTM-BULK.txt | 8.7K | Datos técnicos, FAQ, impacto |

**Ubicación:** ~/Desktop/

---

## CÓMO EJECUTAR

### PASO 1: Obtener Access Token (5 min)
1. Ads Manager → Herramientas → Acceso API
2. Seleccionar App: "CLAUDE CODE DA-JF"
3. Copiar Token de Usuario

### PASO 2: Ejecutar Script (5 min)
\`\`\`bash
bash ~/Desktop/QUICK-START.sh
\`\`\`

### PASO 3: Monitorear (24-48h)
- Ads Manager: cambios a APPROVED
- UTMs se registran automáticamente

---

## Impacto Esperado

### 48 Horas
- ~25-40 ads en PENDING_REVIEW → APPROVED
- UTMs en URL destino
- Targeting y presupuestos preservados

### 7 Días
- EMQ: 4.9 → 5.5-6.0 (+0.6 a +1.1)
- GHL captura utm_campaign/utm_content
- GA4 breakdown por whatsapp-bussines

### 30 Días
- Revenue Tracking: 0% → 85%+
- Show Rate: 43% → 55-60% esperado
- Attribution Accuracy: +85%

---

## Validación Post-Ejecución

### ✅ Google Analytics (72h)
Adquisición > Todas las conversiones > utm_campaign=whatsapp-bussines

### ✅ GHL (inmediato)
Contactos → utm_campaign custom field capturando valores

### ✅ Meta Ads Manager (24-48h)
Campaña WHATSAPP BUSSINES → Ads en estado APPROVED

### ✅ Meta Insights (7 días)
Cuenta → EMQ debe haber subido +0.5 a +1.5 puntos

---

## FAQ

**¿Necesito apagar los ads?**  
No. Script preserva estado, presupuesto y targeting.

**¿Se reinicia el learning de Meta?**  
Sí, es esperado. EMQ mejorará en 7 días.

**¿Es reversible?**  
Sí. Script guarda rollback.json con creative_ids originales.

---

## Coordinar con Equipo

- **Esneider (Trafficker):** Notificar del progreso, monitorear aprobación
- **Diego (DM):** Verificar UTMs en conversaciones GHL
- **Dr. Carreño:** Expectativa EMQ 4.9 → 5.5-6.0 en 7 días

---

**Status:** READY_FOR_EXECUTION | Revisor: Claude Code 2026-06-25

