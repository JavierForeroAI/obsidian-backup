# 🗺️ MAPEO: Obsidian ↔ GHL (Solo Referencia)

**Estado:** Documentación de posibilidades  
**Objetivo:** Entender cómo se conectaría cada segmento a GHL sin ejecutar

---

## 📊 TABLA DE MAPEO

| Carpeta Obsidian | Clientes | GHL TAG (futuro) | Potencial GHL | Notas |
|---|---|---|---|---|
| **01a-Excelente-Evolucion-6m+** | ~50 | `testimonial-eligible` | 5-7 testimonios/mes | Alto valor social proof |
| **01b-Buena-Evolucion-3-6m** | ~50 | `medicinas-potencial` | $500K venta kit/cliente | Momento crítico mantenimiento |
| **02a-Con-Productos-Post-Op** | ~80 | `vip-repeat-buyer` | Upsell premium | Clientes leales, máx. ROAS |
| **02b-Sin-Productos-Post-Op** | ~70 | `sin-mantenimiento` | $500K venta kit/cliente | Recuperar venta perdida |
| **03a-Activos-Ultimos-3m** | ~300 | `active-cross-sell` | 2-3 productos/cliente | Mensualmente |
| **03b-Inactivos-6m** | ~400 | `dormant-reactivate` | 20-30% reconversión | Descuento + nueva oferta |
| **03c-Antiguos-2024** | ~194 | `old-winback` | 10-15% reconversión | Caso éxito + agresivo |

---

## 🔗 CÓMO SE CONECTARÍA (Cuando decidas)

```
Obsidian Folder          →  GHL Custom Field          →  GHL Tag
─────────────────────────────────────────────────────────────────
01a/                     →  segmento: testimonial    →  testimonial-eligible
   [[cliente-1234]]      →  potencial: alto          →  + vip
   [[cliente-5678]]      →  action_date: [fecha]     →  + Bogota

02b/                     →  segmento: sin-producto   →  sin-mantenimiento
   [[cliente-9999]]      →  medicinas_requeridas: sí →  + medicinas-potencial
                         →  kit_target: $500K        →  + target-15days
```

---

## 📊 SEGMENTO POR SEGMENTO

### 01a — Excelente Evolución 6m+

**Obsidian:** `/01-CIRUGIA-ALTO-VALOR/01a-Excelente-Evolucion-6m+/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~50 | Top testimonialistas |
| **Valor promedio** | $70M COP | Alto ticket pagado |
| **Criterio** | 6-12 meses post-op + evolución visible | Fotos antes-después excelentes |
| **GHL Tag** | `testimonial-eligible` | Identifica para contactar |
| **GHL Custom Field** | `potencial_testimonial: alto` | Score para prioridad |
| **Posible Acción** | Email: "Tu evolución es impactante" | Pedir video/foto |

**Preguntas para explorar:**
- ¿Cuántos tienen fotos antes-después?
- ¿Cuántos estarían dispuestos a video?
- ¿Qué incentivo funcionaría? (descuento/honorario/ambos)

---

### 01b — Buena Evolución 3-6m

**Obsidian:** `/01-CIRUGIA-ALTO-VALOR/01b-Buena-Evolucion-3-6m/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~50 | Target medicinas mantenimiento |
| **Valor promedio** | $30-50M COP | Punto de venta |
| **Criterio** | 3-6 meses post-op + evolución normal | Momento crítico mantenimiento |
| **GHL Tag** | `medicinas-potencial` | Identificar para vender |
| **GHL Custom Field** | `kit_target: $500K` | Precio sugerido |
| **Posible Acción** | SMS/Email: "Ahora entra la fase de mantenimiento" | Vender kit |

**Preguntas para explorar:**
- ¿Cuántos compraron medicinas ya?
- ¿Cuál es el % de conversión si se contacta ahora?
- ¿Mejor SMS o email?

---

### 02a — Con Productos Post-Op

**Obsidian:** `/02-CIRUGIA-MEDIO-VALOR/02a-Con-Productos-Post-Op/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~80 | VIP clientes leales |
| **Comportamiento** | Cirugía + medicinas + repetición | Patrón demostrado |
| **GHL Tag** | `vip-repeat-buyer` | Top prioridad |
| **GHL Custom Field** | `lifetime_value: alto` | Score automático |
| **Posible Acción** | Membresía VIP / Ofertas exclusivas | Fidelización |

**Preguntas para explorar:**
- ¿Qué productos compran de repetición?
- ¿Cada cuánto meses compran?
- ¿Membresía es viable?

---

### 02b — Sin Productos Post-Op

**Obsidian:** `/02-CIRUGIA-MEDIO-VALOR/02b-Sin-Productos-Post-Op/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~70 | Recuperar venta faltante |
| **Gap** | Pagaron cirugía pero 0 medicinas | Oportunidad |
| **GHL Tag** | `sin-mantenimiento-target` | Focus |
| **GHL Custom Field** | `medicinas_requeridas: sí` | Trigger |
| **Posible Acción** | Reimpacto agresivo: "Tu evolución se estabiliza, estos productos..." | Vender kit |

**Preguntas para explorar:**
- ¿Por qué no compraron medicinas?
- ¿Tienen dinero disponible?
- ¿Descuento funciona o educación?

---

### 03a — Activos Últimos 3m

**Obsidian:** `/03-SOLO-PRODUCTOS/03a-Activos-Ultimos-3m/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~300 | Engranaje activo |
| **Frecuencia** | Compra cada 30-60 días | Recurrente |
| **GHL Tag** | `active-cross-sell` | Monthly touch |
| **GHL Custom Field** | `next_buy_date: predictive` | Anticipar |
| **Posible Acción** | Email mensual: "Nuevos productos" | Mantener activos |

**Preguntas para explorar:**
- ¿Cuál es el ticket promedio?
- ¿Qué productos compran juntos?
- ¿Son recomendadores?

---

### 03b — Inactivos 6m

**Obsidian:** `/03-SOLO-PRODUCTOS/03b-Inactivos-6m/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~400 | Reactivar con incentivo |
| **Gap** | Compraban pero hace 6+ meses nada | Dormant |
| **GHL Tag** | `dormant-reactivate` | Segmento recovery |
| **GHL Custom Field** | `reactivation_discount: 20%` | Incentivo |
| **Posible Acción** | Email: "Te echamos de menos, 20% desc" | Win-back |

**Preguntas para explorar:**
- ¿Por qué pararon?
- ¿20% es suficiente o menos?
- ¿En qué mes desactivan?

---

### 03c — Antiguos 2024

**Obsidian:** `/03-SOLO-PRODUCTOS/03c-Antiguos-2024/`

| Campo | Valor | Propósito |
|-------|-------|-----------|
| **Clientes** | ~194 | Última esperanza |
| **Gap** | Última compra hace 1+ año | Muy dormant |
| **GHL Tag** | `old-winback` | Última etapa |
| **GHL Custom Field** | `reactivation_discount: 30%` | Agresivo |
| **Posible Acción** | Email + SMS: Casos de éxito 2026 | Pull fuerte |

**Preguntas para explorar:**
- ¿Qué porcentaje vuelve con 30%?
- ¿Vale la pena contactar?
- ¿Mejor testimonio o precio?

---

## 📍 POR CIUDAD

Cada ciudad (BOGOTA, MEDELLIN, BARRANQUILLA) tendría los mismos 7 segmentos.

```
POR-CIUDAD/
├── BOGOTA/
│   ├── 01a-Excelente... (X clientes)
│   ├── 01b-Buena...
│   ├── 02a-Con-Productos...
│   ├── 02b-Sin-Productos...
│   ├── 03a-Activos...
│   ├── 03b-Inactivos...
│   └── 03c-Antiguos...
├── MEDELLIN/
│   ├── ...
└── BARRANQUILLA/
    └── ...
```

**Ventaja:** Dar carpetas a equipo regional con sus clientes.

---

## ⚠️ IMPORTANTE

**Esto NO está activo en GHL.** Solo documentado.

Cuando decidas activar:
1. Cargar contactos a GHL
2. Asignar tags según segmento
3. ENTONCES montar workflows

Por ahora: **Solo exploración.**

---

**¿Algún segmento que quieras entender mejor?**
