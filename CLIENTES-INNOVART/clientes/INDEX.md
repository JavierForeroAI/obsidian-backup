# 📁 CLIENTES — Estructura City/Type

**Generado:** 2026-06-26 11:30  
**Total:** 1,194 clientes

---

## 📊 RESUMEN POR CIUDAD Y TIPO

| Ciudad | CIRUGIA | MEDICAMENTOS | HIBRIDO | Total |
|--------|---------|--------------|---------|-------|
| **BOGOTA** | 427 | 0 | 612 | 1039 |
| **MEDELLIN** | 12 | 143 | 0 | 155 |
| **BARRANQUILLA** | 0 | 0 | 0 | 0 |
| **TOTAL** | 439 | 143 | 612 | **1,194** |

---

## 🏗️ ESTRUCTURA

```
clientes/
├── BOGOTA/
│   ├── CIRUGIA/ (427 clientes)
│   ├── MEDICAMENTOS/ (0 clientes)
│   └── HIBRIDO/ (612 clientes)
├── MEDELLIN/
│   ├── CIRUGIA/ (12 clientes)
│   ├── MEDICAMENTOS/ (143 clientes)
│   └── HIBRIDO/ (0 clientes)
└── BARRANQUILLA/
    ├── CIRUGIA/ (0 clientes)
    ├── MEDICAMENTOS/ (0 clientes)
    └── HIBRIDO/ (0 clientes)
```

---

## 🎯 CAMPOS GHL-READY EN CADA CLIENTE

Cada archivo tiene:
- `cedula` ✓
- `email` ✓
- `telefono` ✓
- `ciudad` ✓
- `tipo_cliente` (GHL tag) ✓
- `ghl_contact_id` (vacío, se llena al sincronizar) ✓
- `ghl_sync_date` (timestamp de sincronización) ✓

---

## 🔄 PARA SINCRONIZAR CON GHL MAÑANA

1. Leer carpeta BOGOTA/CIRUGIA/ → crear contactos en GHL con tag "bogota" + "cirugia"
2. Leer carpeta BOGOTA/MEDICAMENTOS/ → crear contactos en GHL con tag "bogota" + "medicamentos"
3. Leer carpeta BOGOTA/HIBRIDO/ → crear contactos en GHL con tag "bogota" + "hibrido"
4. Repetir por ciudad
5. Al sincronizar, actualizar `ghl_contact_id` en cada archivo

---

## 📌 TIPOS DE CLIENTE

- **CIRUGIA:** Solo procedimiento de implante
- **MEDICAMENTOS:** Solo compra de medicinas/productos
- **HIBRIDO:** Cirugía + medicinas post-op (clientes leales)

---

**Listo para sincronización GHL mañana.** 🚀
