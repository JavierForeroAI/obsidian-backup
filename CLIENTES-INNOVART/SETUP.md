# 🚀 SETUP CLIENTES-INNOVART

**Estado:** ✅ Fase 1 + 2 Completadas  
**Generado:** 2026-06-25  
**Clientes:** 1,194 únicos

---

## ✅ COMPLETADO

### 1. Base de Datos Central
- ✅ 1,194 clientes consolidados y deduplicados
- ✅ CSV + JSON en `_data/`
- ✅ 100% con email + teléfono

### 2. Estructura Obsidian
- ✅ 1,194 archivos `[[cliente-cedula-nombre]]`
- ✅ MEMORY.md (índice central)
- ✅ Scoring automático (RFM, post-op)

### 3. Archivos de Scoring
- ✅ `01-rfm-scoring.md` — Alto/Medio/Bajo valor
- ✅ `02-post-cirugia-evolucion.md` — 3m/6m/12m+

---

## ⏳ PRÓXIMO: Configurar Sincronización GHL

**Objetivo:** Cuando hay compra en GHL → se actualiza automáticamente en Obsidian

### 2 Opciones:

#### 🏠 Opción A: Webhook Local (Tu PC)
- Simple
- Rápido de setup (10 min)
- Requiere que tu PC esté prendido

**Setup:**
```bash
# 1. Instala ngrok
brew install ngrok

# 2. Ejecuta handler
python3 workflows-ghl/webhook_handler.py

# 3. En otra terminal
ngrok http 8888

# 4. Copia URL ngrok → registra en GHL
```

#### ☁️ Opción B: Cloudflare Workers (Recomendado)
- Siempre activo
- Sin tu PC
- Setup 15 min

**Setup:**
```
1. Crea Worker en https://dash.cloudflare.com
2. Pega código de webhook_handler.py (versión Workers)
3. Registra URL en GHL
```

### Instrucciones detalladas:
👉 **Lee:** `workflows-ghl/SETUP_WEBHOOK.md`

---

## 📊 Insights Actuales

### Por Valor
| Segmento | Cantidad | Acción |
|----------|----------|--------|
| Alto (75+) | 64 | Reactivación VIP |
| Medio (50-75) | 120 | Nurture |
| Bajo (<50) | 1,010 | Base para upsell |

### Por Evolución Post-Op
| Estado | Cantidad | Acción |
|--------|----------|--------|
| 12+ meses | ??? | Reactivación histórica |
| 6-12 meses | 202 | 🔥 **Testimonios** |
| 3-6 meses | 14 | Medicinas mantenimiento |

---

## 🔄 Flujo de Trabajo Diario

1. **Un cliente compra en GHL**
   ↓
2. **Webhook dispara automáticamente**
   ↓
3. **Archivo en Obsidian se actualiza**
   ```markdown
   ### Transacción 2026-06-25 14:30
   - Tipo: COMPRA
   - Monto: $500000
   - Productos: KIT COMPLETO
   - Orden: ORD-abc123
   ```
   ↓
4. **Tú ves actualizaciones en tiempo real**
   ↓
5. **Datos acumulan historial completo**

---

## 📁 Estructura Final

```
CLIENTES-INNOVART/
├── SETUP.md (LÉEME PRIMERO)
├── MEMORY.md (índice central)
├── _data/
│   ├── clientes_consolidado.csv
│   └── clientes_consolidado.json
├── clientes/
│   ├── INDEX.md
│   ├── cliente-80863551-john-javier.md
│   ├── cliente-79758707-jaurer-humberto.md
│   └── ... (1,194 más)
├── scoring/
│   ├── 01-rfm-scoring.md
│   └── 02-post-cirugia-evolucion.md
└── workflows-ghl/
    ├── SETUP_WEBHOOK.md (instrucciones)
    ├── webhook_handler.py (escucha GHL)
    ├── 01_workflow_reimpacto.md
    └── 02_workflow_medicinas.md
```

---

## 🎯 Próximos Pasos

### Hoy
1. ✅ Abre Obsidian
2. ✅ Carga `CLIENTES-INNOVART/MEMORY.md`
3. ✅ Revisa algunos `[[cliente-*]]` para ver estructura
4. ✅ Lee `workflows-ghl/SETUP_WEBHOOK.md`

### Esta Semana
1. Elige Opción A (local) o B (Worker)
2. Configura webhook
3. Haz test con orden de prueba
4. Verifica que se actualice en Obsidian

### Próximas 2 Semanas
1. Activar workflows de reimpacto
2. Contactar top 202 (post-op 6-12m) para testimonios
3. Crear estrategia upsell medicinas

---

## 💬 Queries Útiles en Obsidian

Una vez sincronizado, puedes hacer:

```
Buscar: #bogota
↓ Todos los clientes de Bogotá

Buscar: #alto-valor
↓ Top 64 clientes por RFM

Buscar: post_cirugia_6m
↓ 202 candidatos para testimonios

Filtrar por "Últimas 7 días"
↓ Clientes con transacciones recientes
```

---

## ⚙️ Preguntas Frecuentes

**P: ¿Qué pasa si un cliente no existe en Obsidian?**  
R: El webhook lo busca por email. Si no coincide exactamente, lo ignora (safe mode).

**P: ¿Se actualiza en tiempo real?**  
R: Sí. Máximo 1-2 segundos entre orden en GHL y archivo en Obsidian.

**P: ¿Puedo editar el archivo manualmente?**  
R: Sí. El webhook solo AGREGA transacciones, no sobrescribe.

**P: ¿Si hay 2 clientes con mismo email?**  
R: El webhook toma el primero. Recomienda deduplicar manualmente o cambiar email en GHL.

---

## 🚨 Importante

- **NO BORRES los archivos de `_data/`** — son el respaldo
- **Revisa el webhook secret** — debe ser igual en GHL y en el script
- **Si cambias de IP (ngrok)** — actualiza la URL en GHL webhooks

---

**¿Listo?** Abre Obsidian y empieza. 🚀
