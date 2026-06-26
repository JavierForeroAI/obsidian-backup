---
name: clientes-innovart-base-centralizada
description: Base de datos centralizada de 1,194 clientes únicos. Estructura Obsidian + sincronización automática GHL → Obsidian en cada compra.
metadata:
  type: project
  date: 2026-06-26
  status: fase-1-2-completa
---

# CLIENTES INNOVART — Base Centralizada + Sincronización Automática

## Qué es

Sistema de inteligencia sobre clientes: 1,194 pacientes únicos deduplicados de Excel histórico (Bogotá, Barranquilla, Medellín 2024-2026). Centralizado en Obsidian con sincronización automática **GHL → Obsidian** en tiempo real cada vez que hay una compra/evento.

**Objetivo:** Identificar pacientes en estado de evolución post-op, candidatos a testimonios, recompra de medicinas, upsell.

## Ubicación

```
/Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/
├── MEMORY.md (índice central)
├── SETUP.md (instrucciones de configuración)
├── _data/
│   ├── clientes_consolidado.csv (raw, 1,194 registros)
│   └── clientes_consolidado.json (para scripts)
├── clientes/ (1,194 archivos [[cliente-cedula-nombre]])
├── scoring/
│   ├── 01-rfm-scoring.md (Alto/Medio/Bajo por valor)
│   └── 02-post-cirugia-evolucion.md (6-12m: testimonios, 3-6m: medicinas)
└── workflows-ghl/
    ├── webhook_handler.py (escucha GHL, actualiza Obsidian)
    ├── SETUP_WEBHOOK.md (cómo registrar webhook)
    └── plantillas-workflows.md (templates GHL)
```

## Segmentación Automática

| Segmento | Cantidad | Acción Recomendada |
|----------|----------|-------------------|
| Alto Valor (RFM 75+) | 64 | Reactivación VIP + medicinas premium |
| Post-Op 6-12m | 202 | 🔥 **TOP:** Pedir testimonios + reviews |
| Post-Op 3-6m | 14 | Medicinas mantenimiento |

## Flujo de Sincronización

```
1. Javier vende en GHL (crear orden/oportunidad/compra)
   ↓
2. GHL Workflow dispara webhook
   ↓
3. Script webhook_handler.py recibe evento
   ↓
4. Busca cliente en Obsidian por cédula/email/teléfono
   ↓
5. Actualiza archivo [[cliente-cedula-nombre]] con:
   - Monto nuevo
   - Productos comprados
   - Fecha transacción
   - ID orden GHL
   ↓
6. Cliente tiene historial completo (todas sus compras acumuladas)
```

## Cómo Usar

### Consulta rápida

Busca en Obsidian por cédula o apellido dentro de carpeta `clientes/`.

### Identificar candidatos

Lee `01-rfm-scoring.md` para clientes Alto Valor.
Lee `02-post-cirugia-evolucion.md` para pacientes en 6-12 meses (mejor momento para testimonios).

### Reimpacto

En GHL, créa un workflow con trigger "tag = alto_valor" → envía medicinas/oferta upsell.

## Configuración del Webhook (PENDIENTE)

Ver `SETUP_WEBHOOK.md` en la carpeta.

**Resumen:**
1. Obtener URL endpoint del servidor donde corre `webhook_handler.py`
2. Registrar en GHL → Webhooks → URL + evento `purchase`
3. Testear con una compra de prueba
4. Monitorear logs

## Campos Capturados por Cliente

- Cédula (dedup key)
- Email + Teléfono
- Dirección
- Ciudad
- Procedimientos (FUE, DHI, medicinas)
- Precios (COP + USD)
- Fechas (primera compra, última compra, tiempo post-op)
- ID GHL
- Scoring RFM + evolución temporal

## Límites (Hasta hoy)

- ✅ 1,194 clientes importados de Excel (historico 2024-2026)
- ⏳ Webhook NO ACTIVO TODAVIA (necesita config en GHL)
- ⏳ Sincronización en tiempo real pendiente

**Next:** Configurar webhook en GHL cuando Javier esté disponible (15 min).

---

**Why:** Javier tiene ~3.2B COP en transacciones de 1,194 pacientes únicos. Sin un cerebro sobre quiénes son, cuándo operaron, qué compraron, es imposible **venderles medicinas, pedirles reviews, reimpactarlos en el momento correcto**. Este sistema lo hace automático.
