---
nombre: Prueba 10 Pacientes Mañana
descripcion: Plan para enriquecer 10 pacientes manualmente mañana (2026-06-27) sin automatización
fecha: 2026-06-26
estado: Listo para ejecutar mañana 09:00 AM
---

# 🚀 PRUEBA 10 PACIENTES — MAÑANA 09:00 AM

**Objetivo:** Ver cómo se vería Obsidian enriquecido con Drive + evolución  
**Tiempo:** 30 minutos  
**Método:** 100% manual, 0 automatización  
**Resultado:** 10 archivos enriquecidos, 1 ejemplo visual completo

---

## 📋 LOS 10 PACIENTES (MUESTRA)

| # | Cedula | Nombre | Ciudad | Tipo | Email |
|---|--------|--------|--------|------|-------|
| 1 | 1015439817 | FABIAN BOHORQUEZ | BOGOTA | CIRUGIA | fabian@email.com |
| 2 | 1000286412 | JOHAN SEBASTIÁN ACOSTA | BOGOTA | CIRUGIA | johan@email.com |
| 3 | 1035853755 | DIEGO ALEJANDRO MISAS | MEDELLIN | CIRUGIA | diemisas2@gmail.com |
| 4 | 1017258002 | DAVID LEGARDA OVALLE | MEDELLIN | CIRUGIA | david@email.com |
| 5 | 71782475 | JUAN PABLO ARANGO | MEDELLIN | MEDICAMENTOS | arango@email.com |
| 6 | 1012408987 | CARLOS DAVID VEGA | BOGOTA | CIRUGIA | cvega@email.com |
| 7 | 1072700338 | HECTOR FAVIO LEON GIL | BOGOTA | CIRUGIA | hector@email.com |
| 8 | 1020772001 | JUAN SEBASTIÁN CARDENAS | BOGOTA | CIRUGIA | cardenas@email.com |
| 9 | 80767053 | LUIS EMILIO BARRIOS | BOGOTA | CIRUGIA | barrios@email.com |
| 10 | 1049029100 | EDERSON ESTIVEN RUBIANO | BOGOTA | CIRUGIA | ederson@email.com |

---

## 🔍 INFORMACIÓN POR PACIENTE

### **#1 — FABIAN BOHORQUEZ (1015439817) — BOGOTA**

**De las carpetas Drive que revisamos, este está en Carpeta 1 (reciente):**

```
Folder ID: 1WXK16ouPZa5s1fnF52E7EssHChGtbw3k
URL: https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k

Controles en carpeta:
  - POSCIRUGIA (18/06/2026)
  - RETIRO DE COSTRAS (26/06/2026)

Datos:
  - Fecha cirugía: 18/06/2026
  - Meses post-op: 0 (hoy es 26/06/2026)
  - Fotos: SÍ (hay carpetas con fotos)
  - Autoriza imágenes: NO (especifica "No autoriza")
```

---

### **#2 — JOHAN SEBASTIÁN ACOSTA (1000286412) — BOGOTA**

**De Carpeta 2 (histórica):**

```
Folder ID: 1XgKe7mmjYEESJfx8aTvl5u_kIxJvG9_X
URL: https://drive.google.com/drive/folders/1XgKe7mmjYEESJfx8aTvl5u_kIxJvG9_X

Controles en carpeta:
  - POSCIRUGIA (aprox 2024-12)
  - 2MES CONTROL (aprox 2025-02)
  - 3MES CONTROL (aprox 2025-03)
  - 6MES CONTROL (aprox 2025-06)

Datos:
  - Fecha cirugía: Approx 2024-12-01
  - Meses post-op: 6+ (listo para testimonios)
  - Fotos: SÍ (múltiples controles)
  - Autoriza imágenes: PROBABLEMENTE SÍ (no dice "no autoriza")
```

---

### **#3 a #10 — RESTO (SIN CARPETA DRIVE AÚN)**

Para estos 8 pacientes:
- **Carpeta Drive:** VACÍO (no están en las 2 carpetas encontradas)
- **Meses post-op:** Los calculamos de la fecha_transaccion en Obsidian
- **Fotos/Autoriza:** DESCONOCIDO (no podemos saber sin revisar Drive)

**EJEMPLO #3 — DIEGO ALEJANDRO MISAS (1035853755):**
```
Archivo Obsidian actual:
  fecha_transaccion: 2025-07-17

Cálculo:
  Hoy: 2026-06-26
  Diferencia: ~11 meses
  → meses_post_op: 11

drive_folder_id: ??? (no sabemos si tiene en Drive)
fotos_antes_despues: ???
autoriza_imagenes: ???
```

---

## ✏️ PLANTILLA: ANTES vs DESPUÉS

### **ANTES (Actual)**

```yaml
---
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
email: fabian@email.com
telefono: 3001234567
ciudad: BOGOTA
tipo_cliente: CIRUGIA
procedimiento: IMPLANTE CAPILAR
valor: 3200000.0
fecha_transaccion: 2026-06-18 00:00:00
metadata:
  ghl_city_tag: bogota
  ghl_type_tag: cirugia
  ghl_sync_date: null
  ghl_contact_id: null
---
```

### **DESPUÉS (Enriquecido)**

```yaml
---
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
email: fabian@email.com
telefono: 3001234567
ciudad: BOGOTA
tipo_cliente: CIRUGIA
procedimiento: IMPLANTE CAPILAR
valor: 3200000.0
fecha_transaccion: 2026-06-18 00:00:00

# ← NUEVOS CAMPOS AGREGADOS
drive_folder_id: "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
drive_url: "https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
fecha_cirugia: "2026-06-18"
meses_post_op: 0
controles_realizados:
  - "POSCIRUGIA (18/06/2026)"
  - "RETIRO DE COSTRAS (26/06/2026)"
fotos_antes_despues: "sí"
autoriza_imagenes: "no"
ghl_tags:
  - "0-3m-post-op"
  - "sin-medicinas-target"
  - "fotos-no-autoriza"

metadata:
  ghl_city_tag: bogota
  ghl_type_tag: cirugia
  ghl_sync_date: null
  ghl_contact_id: null
---
```

---

## 📝 PASO A PASO — LO QUE HARÁS MAÑANA

### **PARA CADA UNO DE LOS 10 PACIENTES:**

**Paso 1: Abrir archivo en Obsidian**
```
/Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/clientes/
  BOGOTA/CIRUGIA/1015439817-fabian-bohorquez.md
```

**Paso 2: Agregar estos 8 campos después de `fecha_transaccion`:**

```
drive_folder_id: "[REVISAR CARPETA DRIVE]"
drive_url: "https://drive.google.com/drive/folders/[ID]"
fecha_cirugia: "[Extraer de fecha_transaccion]"
meses_post_op: [Calcular: hoy - fecha]
controles_realizados: ["CONTROL 1", "CONTROL 2"]
fotos_antes_despues: "sí" | "no"
autoriza_imagenes: "sí" | "no"
ghl_tags: ["tag1", "tag2"]
```

**Paso 3: Guardar en Obsidian**

---

## 🎯 DATOS ESPECÍFICOS PARA CADA UNO

### **#1-2 (FABIAN + JOHAN): COPIAR EXACTO**

Estos están en las carpetas que revisamos. Copiar datos tal cual:

```
#1 — FABIAN BOHORQUEZ
drive_folder_id: "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
drive_url: "https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
fecha_cirugia: "2026-06-18"
meses_post_op: 0
controles_realizados:
  - "POSCIRUGIA (18/06/2026)"
  - "RETIRO DE COSTRAS (26/06/2026)"
fotos_antes_despues: "sí"
autoriza_imagenes: "no"
ghl_tags:
  - "0-3m-post-op"
  - "sin-medicinas-target"
  - "fotos-no-autoriza"

#2 — JOHAN SEBASTIÁN ACOSTA
drive_folder_id: "1XgKe7mmjYEESJfx8aTvl5u_kIxJvG9_X"
drive_url: "https://drive.google.com/drive/folders/1XgKe7mmjYEESJfx8aTvl5u_kIxJvG9_X"
fecha_cirugia: "2024-12-01"
meses_post_op: 6
controles_realizados:
  - "POSCIRUGIA (12/2024)"
  - "2MES CONTROL (02/2025)"
  - "3MES CONTROL (03/2025)"
  - "6MES CONTROL (06/2025)"
fotos_antes_despues: "sí"
autoriza_imagenes: "sí"
ghl_tags:
  - "6m-post-op"
  - "testimonial-eligible"
  - "evolución-visible"
```

### **#3-10 (RESTO): DÉJALO VACÍO POR AHORA**

Para estos, como NO están en las carpetas Drive que revisamos:

```
drive_folder_id: "BUSCAR EN DRIVE" (o dejar vacío)
drive_url: ""
fecha_cirugia: "2025-07-17"  (copiar de fecha_transaccion)
meses_post_op: 11  (calcular)
controles_realizados: "???  (no sabemos)"
fotos_antes_despues: "???"
autoriza_imagenes: "???"
ghl_tags: []
```

---

## ⏰ TIMELINE MAÑANA (2026-06-27)

```
09:00 AM  → Abrir Obsidian
09:05 AM  → Paciente #1 FABIAN (copiar datos)
09:08 AM  → Paciente #2 JOHAN (copiar datos)
09:15 AM  → Pacientes #3-10 (dejar Drive vacío, solo meses_post_op)
09:30 AM  → TERMINADO ✅
```

---

## 🎬 DESPUÉS: VER EL RESULTADO

Una vez enriquecidos los 10:

**En Obsidian:**
```
Abres archivo de FABIAN
  ↓
Ves en el frontmatter:
  - drive_folder_id: "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
  - meses_post_op: 0
  - fotos_antes_despues: "sí"
  - ghl_tags: ["0-3m-post-op", ...]
  ↓
Haces click en drive_url
  ↓
🎯 BOOM → Ves su carpeta Drive con fotos directamente desde Obsidian
```

**En GHL (manual):**
```
Quiero contactar a JOHAN (6 meses post-op con fotos)
  ↓
Abro Obsidian
  ↓
Busco en BOGOTA/CIRUGIA/
  ↓
Veo: "meses_post_op: 6, fotos_antes_despues: sí, autoriza: sí"
  ↓
Copio su email y teléfono
  ↓
Voy a GHL
  ↓
Busco contacto por email
  ↓
Envío email personal: "Tu caso es inspirador, ¿video testimonial?"
  ↓
Espero respuesta
```

---

## 📊 QUÉ VEREMOS DESPUÉS DE LOS 10

Una vez completados:

✅ **FABIAN:**
- Vemos su carpeta Drive completa
- Sabemos que está en mes 0 post-op
- Sabemos que NO autoriza (no podemos usar fotos)
- **Acción:** Contactarlo para medicinas mes 0-3

✅ **JOHAN:**
- Vemos su evolución 6-8 meses
- Sabemos que autoriza imágenes
- **Acción:** Contactarlo para testimonial VIDEO

✅ **DIEGO + 7 OTROS:**
- Sabemos cuántos meses post-op
- No sabemos si tienen Drive (aún)
- **Acción:** Después buscar en Drive si existen

---

## ✅ CHECKLIST MAÑANA

- [ ] Abrir Obsidian
- [ ] Localizar los 10 archivos
- [ ] Copiar datos de FABIAN (5 min)
- [ ] Copiar datos de JOHAN (5 min)
- [ ] Llenar resto con datos básicos (20 min)
- [ ] Guardar todo
- [ ] Revisar 1 archivo completo
- [ ] Tomar screenshot de FABIAN con drive_url
- [ ] Mandarme el screenshot
- [ ] ✅ PRUEBA 1 COMPLETADA

---

## 🎯 QUÉ APRENDEREMOS

Después de esto:
1. **¿Se ve bien en Obsidian?** ¿El formato es claro?
2. **¿El link a Drive funciona?** ¿Fácil acceso?
3. **¿Es útil tener meses_post_op calculado?**
4. **¿Quieres agregar más campos?**
5. **¿Ya ves cómo harías campañas?**

Luego decidimos:
- ¿Hacemos los 1,194 así?
- ¿Automatizamos con script?
- ¿Agregamos más campos?

---

**¿LISTO PARA MAÑANA A LAS 9AM?** 🚀

O si quieres, hacemos una prueba HOY con 1 solo paciente para asegurar que el formato está bien.
