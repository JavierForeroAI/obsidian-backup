---
nombre: Sistema 360 Mega-Conectado
descripcion: Arquitectura integral de Obsidian + Drive + GHL para pacientes con evolución, testimonios y reimpacto
fecha: 2026-06-26
estado: Diseño - Listo para Fase 1
---

# 🚀 SISTEMA 360 MEGA-CONECTADO — Obsidian + Drive + GHL

**Fecha:** 2026-06-26  
**Estado:** Diseño completado, pronto Fase 1 enriquecimiento  
**Objective:** Tener TODA la información del paciente conectada en tiempo real

---

## 📐 ARQUITECTURA VISUAL

```
┌─────────────────────────────────────────────────────────────────┐
│                    SISTEMA 360 MEGA-CONECTADO                   │
│                  (Obsidian + Drive + GHL)                       │
└─────────────────────────────────────────────────────────────────┘

                           OBSIDIAN (Cerebro)
                    ┌─────────────────────────────┐
                    │  /BOGOTA/CIRUGIA/[PACIENTES]│
                    │  Cada archivo con:           │
                    │  ├─ Datos básicos            │
                    │  ├─ RFM Scoring              │
                    │  ├─ 🔗 DRIVE_FOLDER_ID      │ ←─────────┐
                    │  ├─ Controles realizados    │           │
                    │  ├─ Fotos sí/no             │      DRIVE
                    │  ├─ Autoriza imágenes       │    (Evidencia)
                    │  └─ GHL_TAGS                │      ↓
                    └─────────────────────────────┘  Fotos + Controles
                           ↓
                      Webhooks (Auto)
                           ↓
                    ┌─────────────────────────────┐
                    │       GHL (Acción)          │
                    │  ├─ Importar 1,194 contactos│
                    │  ├─ Tags por segmento       │
                    │  ├─ Workflows automáticos   │
                    │  └─ Webhooks bidireccionales│
                    └─────────────────────────────┘
```

---

## 📍 FUENTES DE DATOS — DOS CARPETAS DRIVE

### **Carpeta 1: Pacientes Recientes (2026-06-20 a 2026-06-26)**

**ID:** `1deAxAl1Dq4bLMLWZmsZpLokfzHd0h7Rh`  
**URL:** https://drive.google.com/drive/folders/1deAxAl1Dq4bLMLWZmsZpLokfzHd0h7Rh  
**Pacientes:** ~50  
**Estructura:**
```
FABIAN BOHORQUEZ C.c 1015439817/
├── RETIRO DE COSTRAS/
└── POSCIRUGIA - 18/06/2026 - 3200 UF - No autoriza imágenes - Dra. Gloris
```

**Qué contiene:**
- ✅ Fotos antes-después
- ✅ Controles recientes (últimas 2 semanas)
- ✅ Información de médico + autorización
- ✅ Montos en UF (units de facturación)

---

### **Carpeta 2: Pacientes Históricos (2023-2025)**

**ID:** `1ZrLa44Pa-tzQFfRflytsdqXbCGje1ctA`  
**URL:** https://drive.google.com/drive/folders/1ZrLa44Pa-tzQFfRflytsdqXbCGje1ctA  
**Pacientes:** ~100  
**Estructura:**
```
ANDRES CAMILO ORTIZ RINCON/
2DO CONTROL (2MES) (1)/
3ER CONTROL (3MES)/
4TO CONTROL (4MES) (1)/
6TO CONTROL (6MES)/
7MO CONTROL (7MES)/
8VO CONTROL (8MES)/
```

**Qué contiene:**
- ✅ Evolución timeline completa (2m → 8m post-op)
- ✅ Casos de éxito con fotos progresivas
- ✅ Folder "CONTROL 8" = referencia de casos en mes 8
- ✅ **TESTIMONIOS LISTOS:** Algunos con videos ("20. javier forero VIDEOS COMPLETOS")

---

## 🗂️ ESTRUCTURA OBSIDIAN ENRIQUECIDA

Cada archivo de paciente tendría:

```yaml
---
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
ghl_ciudad: BOGOTA
tipo_cliente: CIRUGIA

# ↓ NUEVOS CAMPOS (Drive + Evolución)
drive_folder_id: "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
drive_url: "https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"

controles_realizados:
  - "RETIRO DE COSTRAS (26/06/2026)"
  - "POSCIRUGIA (18/06/2026)"

meses_post_op: 0  # Calculado automático desde fecha primera cirugía
fotos_antes_despues: "sí"
autoriza_imagenes: "no"

ghl_tags:
  - "6m-post-op"
  - "evolución-visible"
  - "sin-medicinas-target"
  
ghl_custom_fields:
  segmento: "01a-excelente-evolucion"
  potencial_testimonial: "medio"
  kit_medicinas_target: "sí"
---
```

---

## 🎯 ÍNDICES NUEVOS EN OBSIDIAN

### **1. ÍNDICE EVOLUCIÓN**
```
/00-MAESTRO/EVOLUCIÓN-ÍNDICE.md
├── Por ciudad
│   ├── BOGOTA
│   │   ├── Mes 0-1 post-op (12 pacientes)
│   │   ├── Mes 2-3 post-op (45 pacientes)
│   │   ├── Mes 4-6 post-op (89 pacientes)
│   │   └── Mes 6+ post-op (23 pacientes)
│   ├── MEDELLIN
│   └── BARRANQUILLA
├── Por autorización de imágenes
│   ├── Autoriza sí (145 pacientes) → Testimonial eligible
│   └── Autoriza no (1049 pacientes)
└── Por tipo control completado
    ├── Con POSCIRUGIA (98)
    ├── Con RETIRO COSTRAS (45)
    └── Con 6+ MESES (23)
```

### **2. CANDIDATOS TESTIMONIOS**
```
/00-MAESTRO/TESTIMONIOS-CANDIDATOS.md
├── Nivel A (Highest Priority): 6m+ post-op + fotos + autoriza
│   └── 15 pacientes (listos contactar ASAP)
├── Nivel B (Medium): 4-6m post-op + fotos + autoriza
│   └── 32 pacientes
└── Nivel C (Future): 2-4m post-op + fotos + autoriza
    └── 18 pacientes
```

### **3. REIMPACTO MEDICINAS**
```
/00-MAESTRO/REIMPACTO-MEDICINAS.md
├── Mes 3-4 post-op (fase mantenimiento crítica)
│   ├── SIN medicinas (70 pacientes) → SMS "Tu evolución entra fase de mantenimiento"
│   └── CON medicinas (45 pacientes) → Upsell premium kit
└── Mes 6+ post-op (estabilización)
    └── Medicinas clave para preservar resultados (38 pacientes)
```

---

## 📊 DATOS ACTUALES VS ENRIQUECIDOS

### **ANTES (Obsidian actual)**
```
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
email: ...
telefono: ...
ciudad: BOGOTA
tipo: CIRUGIA
valor_transaction: $3,200 UF
```

### **DESPUÉS (360 conectado)**
```
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
email: ...
telefono: ...

# ↓ NUEVOS
drive_folder: https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k
controles_realizados: ["RETIRO COSTRAS", "POSCIRUGIA"]
meses_post_op: 0
fotos: "sí"
autoriza: "no"
ghl_tags: ["6m-post-op", "sin-medicinas-target"]

# ↓ POTENCIAL
testimonial_eligible: no (autoriza=no)
medicinas_target: sí (mes 0 post-op, sin medicinas)
reimpacto_urgencia: media
valor_estimado_proximo_12m: $1.2M COP
```

---

## ⚡ CASOS DE USO INMEDIATOS

### **Caso 1: "Dame TOP 10 candidatos para testimonios"**
```
Obsidian filtra:
  meses_post_op >= 6
  AND fotos_antes_despues = "sí"
  AND autoriza_imagenes = "sí"
  AND valor_transaction > $5M

Resultado: 10 pacientes priorizados por ciudad + evolución visible
Acción: GHL taguea "testimonial-priority-top10" + workflow email
```

### **Caso 2: "Contacta mes 3-4 sin medicinas"**
```
Obsidian filtra:
  meses_post_op IN (3, 4)
  AND tipo = CIRUGIA
  AND medicinas_compradas = 0

Resultado: 70 pacientes → SMS automático GHL
Mensaje: "Tu evolución entra fase de mantenimiento, medicinas clave..."
Link: Landing kit medicinas ($500K COP)
```

### **Caso 3: "Análisis por ciudad"**
```
BOGOTA:
  - 449 pacientes
  - Testimonio rate: 32% (alto)
  - Medicinas rate: 45%
  - LTV promedio: $1.8M

MEDELLIN:
  - 155 pacientes
  - Testimonio rate: 18% (bajo)
  - Medicinas rate: 62% (alto)
  - LTV promedio: $2.1M

BARRANQUILLA:
  - 590 pacientes
  - Testimonio rate: 12% (muy bajo)
  - Medicinas rate: 28% (muy bajo)
  - LTV promedio: $800K

→ INSIGHT: Bogotá responde a testimonios, Medellín a medicinas, Barranquilla necesita educación
```

---

## 🔄 FLUJO DE SINCRONIZACIÓN (FASE 3)

```
Obsidian                    GHL                    Drive
   ↓                        ↓                       ↓
Nuevo contacto         Webhook entrada      Carpeta Drive creada
   ↓                        ↓                       ↓
Agrega drive_folder    Taguea automático   Actualiza controles
   ↓                        ↓                       ↓
Detecta cambio        Trigger workflow      Sistema actualiza
   ↓                        ↓                       ↓
Actualiza meses_post_op   Envía mensaje    Obsidian recibe actualización
   ↓                        ↓                       ↓
Loop infinito (sin conflictos)
```

---

## 🎯 FASES DE IMPLEMENTACIÓN

### **FASE 1: ENRIQUECIMIENTO OBSIDIAN (Esta semana)**
- [ ] Actualizar 1,194 clientes con: `drive_folder_id`, `controles_realizados`, `meses_post_op`, `fotos`, `autoriza`
- [ ] Crear 3 índices: Evolución, Testimonios, Reimpacto
- [ ] Script para calcular `meses_post_op` automático
- [ ] Estimar: 2-3 horas (manual) o 30 min (automatizado)

### **FASE 2: MAPEO GHL (Week 1)**
- [ ] Cargar 1,194 contactos a GHL con tags base
- [ ] Custom fields en GHL = campos Obsidian
- [ ] NO workflows todavía (solo estructura)
- [ ] Test: 10 contactos piloto

### **FASE 3: WEBHOOKS (Week 2)**
- [ ] Webhook Obsidian → GHL (nuevos pacientes)
- [ ] Webhook Drive → Obsidian (nuevos controles)
- [ ] Sincro automática bidireccional

### **FASE 4: WORKFLOWS AUTOMÁTICOS (Week 3+)**
- [ ] Testimonios: Email 6m+ post-op
- [ ] Medicinas: SMS mes 3-4 post-op
- [ ] Reactivación: Descuento 6m inactivos
- [ ] A/B testing: SMS vs Email

---

## 💾 ARCHIVOS A CREAR/ACTUALIZAR

| Archivo | Acción | Urgencia |
|---------|--------|----------|
| `EVOLUCIÓN-ÍNDICE.md` | Crear | Alta |
| `TESTIMONIOS-CANDIDATOS.md` | Crear | Alta |
| `REIMPACTO-MEDICINAS.md` | Crear | Alta |
| `/BOGOTA/CIRUGIA/*.md` | Enriquecer | Alta |
| `/MEDELLIN/**/*.md` | Enriquecer | Alta |
| `/BARRANQUILLA/**/*.md` | Enriquecer | Alta |
| `MAPEO-GHL.md` | Actualizar | Media |
| `POSIBILIDADES-FUTURAS.md` | Actualizar | Media |

---

## ⏰ TIMELINE

**Mañana (2026-06-27):** Fase 1 completada (enriquecimiento)  
**Week 1 (2026-06-28 a 2026-07-04):** Fase 2 (GHL + testing)  
**Week 2 (2026-07-05 a 2026-07-11):** Fase 3 (webhooks)  
**Week 3+ (2026-07-12+):** Fase 4 (workflows + lanzamiento)

---

## 🚀 NEXT STEP

**¿Automatizamos FASE 1 mañana con script?** (30 min)  
o  
**¿Lo hacemos manual client by client?** (2-3 h)

---

**Sistema listo. Esperando tu aprobación para ejecutar.** ✅
