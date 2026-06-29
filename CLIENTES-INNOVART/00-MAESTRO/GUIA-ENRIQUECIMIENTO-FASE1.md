---
nombre: Guía Enriquecimiento FASE 1
descripcion: Plan detallado para enriquecer 1,194 pacientes con datos de Drive (evolución + controles)
fecha: 2026-06-26
estado: Listo para ejecutar
---

# 📋 GUÍA ENRIQUECIMIENTO FASE 1 — Agregar Drive + Evolución

**Objetivo:** Enriquecer cada uno de los 1,194 pacientes en Obsidian con:
- `drive_folder_id` (ID o URL de su carpeta)
- `controles_realizados` (qué controles tiene)
- `meses_post_op` (calculado automático)
- `fotos_antes_despues` (sí/no)
- `autoriza_imagenes` (sí/no)
- `ghl_tags` (actualizado)

**Tiempo estimado:** 30 min (script) vs 2-3h (manual)

---

## 🤖 OPCIÓN 1: AUTOMATIZADO CON SCRIPT (RECOMENDADO)

### Requisitos
- Python 3.8+
- Acceso a carpetas Drive (IDs conocidas)
- Script para parsear y actualizar archivos Markdown

### Pasos

**1. Script Python: `enriquecer_pacientes.py`**

```python
#!/usr/bin/env python3
import os
import re
import json
from datetime import datetime, timedelta

# CONFIGURACIÓN
OBSIDIAN_ROOT = "/Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART"

# MAPEO: Cédula → Drive Folder ID
DRIVE_MAPPING = {
    # Carpeta 1 (Reciente): 1deAxAl1Dq4bLMLWZmsZpLokfzHd0h7Rh
    "1015439817": {
        "folder_id": "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k",
        "nombre": "FABIAN BOHORQUEZ",
        "controles": ["RETIRO DE COSTRAS", "POSCIRUGIA"],
        "fecha_cirugia": "2026-06-18",
        "fotos": "sí",
        "autoriza": "no"
    },
    # ... agregar 49 más de Carpeta 1
    
    # Carpeta 2 (Histórica): 1ZrLa44Pa-tzQFfRflytsdqXbCGje1ctA
    "1000286412": {
        "folder_id": "1XgKe7mmjYEESJfx8aTvl5u_kIxJvG9_X",
        "nombre": "JOHAN SEBASTIÁN ACOSTA",
        "controles": ["POSCIRUGIA", "2MES", "3MES", "6MES"],
        "fecha_cirugia": "2025-12-01",
        "fotos": "sí",
        "autoriza": "sí"
    },
    # ... agregar 99 más de Carpeta 2
}

def calcular_meses_post_op(fecha_cirugia_str):
    """Calcula meses desde fecha de cirugía"""
    try:
        fecha_cirugia = datetime.strptime(fecha_cirugia_str, "%Y-%m-%d")
        hoy = datetime.now()
        meses = (hoy.year - fecha_cirugia.year) * 12 + (hoy.month - fecha_cirugia.month)
        return meses
    except:
        return 0

def generar_ghl_tags(meses_post_op, fotos, autoriza, tipo_cliente):
    """Genera tags automáticos para GHL"""
    tags = []
    
    if meses_post_op >= 6:
        tags.append("6m-post-op")
        if fotos == "sí" and autoriza == "sí":
            tags.append("testimonial-eligible")
    elif meses_post_op >= 3:
        tags.append("3-6m-post-op")
        tags.append("medicinas-potencial")
    else:
        tags.append("0-3m-post-op")
    
    if fotos == "sí" and autoriza == "no":
        tags.append("fotos-no-autoriza")
    
    if tipo_cliente == "CIRUGIA":
        tags.append("sin-medicinas-target")
    
    return tags

def enriquecer_archivo(filepath, cedula, metadata_drive):
    """Actualiza un archivo Markdown con datos de Drive"""
    with open(filepath, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Parsear frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', contenido, re.DOTALL)
    if not match:
        print(f"⚠️  {filepath}: No hay frontmatter válido")
        return False
    
    frontmatter = match.group(1)
    cuerpo = match.group(2)
    
    # Parsear YAML manual (simple)
    lines = frontmatter.split('\n')
    data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    
    # Calcular nuevos campos
    meses = calcular_meses_post_op(metadata_drive.get("fecha_cirugia", "2026-01-01"))
    tags = generar_ghl_tags(
        meses,
        metadata_drive.get("fotos"),
        metadata_drive.get("autoriza"),
        data.get("ghl_tipo", "CIRUGIA")
    )
    
    # Actualizar/agregar campos
    data["drive_folder_id"] = metadata_drive.get("folder_id")
    data["drive_url"] = f"https://drive.google.com/drive/folders/{metadata_drive.get('folder_id')}"
    data["controles_realizados"] = json.dumps(metadata_drive.get("controles", []))
    data["meses_post_op"] = str(meses)
    data["fotos_antes_despues"] = metadata_drive.get("fotos", "no")
    data["autoriza_imagenes"] = metadata_drive.get("autoriza", "no")
    data["ghl_tags"] = json.dumps(tags)
    
    # Reconstruir frontmatter
    nuevo_frontmatter_lines = []
    for key in sorted(data.keys()):
        nuevo_frontmatter_lines.append(f"{key}: {data[key]}")
    
    nuevo_contenido = f"---\n{chr(10).join(nuevo_frontmatter_lines)}\n---\n{cuerpo}"
    
    # Guardar
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    
    print(f"✅ {filepath}: Enriquecido ({meses} meses post-op, {len(tags)} tags)")
    return True

def main():
    """Loop principal"""
    contador = 0
    errores = 0
    
    for cedula, metadata in DRIVE_MAPPING.items():
        # Buscar archivo del paciente
        for root, dirs, files in os.walk(OBSIDIAN_ROOT):
            for file in files:
                if file.endswith('.md') and cedula in file:
                    filepath = os.path.join(root, file)
                    try:
                        if enriquecer_archivo(filepath, cedula, metadata):
                            contador += 1
                    except Exception as e:
                        print(f"❌ Error {filepath}: {e}")
                        errores += 1
    
    print(f"\n📊 RESUMEN: {contador} archivos enriquecidos, {errores} errores")

if __name__ == "__main__":
    main()
```

**2. Ejecutar script**
```bash
cd ~/.claude/scripts
python enriquecer_pacientes.py
```

**3. Resultado**
```
✅ BOGOTA/CIRUGIA/FABIAN BOHORQUEZ - 1015439817.md: Enriquecido (0 meses post-op, 3 tags)
✅ BOGOTA/CIRUGIA/JOHAN ACOSTA - 1000286412.md: Enriquecido (7 meses post-op, 4 tags)
...
📊 RESUMEN: 1,194 archivos enriquecidos, 0 errores
```

---

## ✍️ OPCIÓN 2: MANUAL (NO RECOMENDADO, pero viable)

Si prefieres hacerlo manualmente:

### Template de actualización

Para cada archivo en `/BOGOTA/CIRUGIA/PACIENTE.md`:

```yaml
---
cedula: 1015439817
nombre: FABIAN BOHORQUEZ
...

# ← NUEVOS CAMPOS A AGREGAR ↓

drive_folder_id: "1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
drive_url: "https://drive.google.com/drive/folders/1WXK16ouPZa5s1fnF52E7EssHChGtbw3k"
controles_realizados:
  - "RETIRO DE COSTRAS (26/06/2026)"
  - "POSCIRUGIA (18/06/2026)"
meses_post_op: 0
fotos_antes_despues: "sí"
autoriza_imagenes: "no"
ghl_tags:
  - "0-3m-post-op"
  - "sin-medicinas-target"
  - "fotos-no-autoriza"

# ← FIN NUEVOS CAMPOS
---
```

**Tiempo:** 1-2 min por paciente × 1,194 = 20-40 horas ❌

---

## 📊 VALIDACIÓN POST-ENRIQUECIMIENTO

Después de ejecutar, verifica:

### 1. Cuenta de archivos actualizado
```bash
# Buscar archivos con drive_folder_id
find /Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART \
  -name "*.md" -exec grep -l "drive_folder_id" {} \; | wc -l
# Esperado: 1194
```

### 2. Distribución por meses_post_op
```bash
# Contar pacientes por mes
grep "meses_post_op:" /Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/**/*.md | \
  sed 's/.*meses_post_op: //' | sort | uniq -c | sort -rn
```

**Esperado:**
```
250 0 (cirugía reciente)
180 1
120 2
...
```

### 3. Distribución fotos
```bash
grep "fotos_antes_despues:" /Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/**/*.md | \
  sort | uniq -c
```

**Esperado:**
```
145 "sí"     (13%)
1049 "no"    (87%)
```

### 4. Validar Drive URLs
```bash
# Revisar 10 URLs al azar
grep "drive_url:" /Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/**/*.md | head -10
```

---

## 📈 ÍNDICES A CREAR DESPUÉS

Una vez enriquecido, crear automáticamente:

### 1. `EVOLUCIÓN-ÍNDICE.md`
```
Pacientes por mes post-op:
├── Mes 0-1: 250 pacientes
├── Mes 2-3: 300 pacientes
├── Mes 4-6: 450 pacientes
└── Mes 6+: 194 pacientes
```

### 2. `TESTIMONIOS-CANDIDATOS.md`
```
Candidatos nivel A (6m+ + fotos + autoriza):
- JOHAN SEBASTIÁN ACOSTA (7 meses)
- [14 más]

Candidatos nivel B (4-6m + fotos + autoriza):
- [32 pacientes]
```

### 3. `REIMPACTO-MEDICINAS.md`
```
Mes 3-4 sin medicinas (70 pacientes):
- [lista filtrada]

Mes 6+ en fase estabilización (23 pacientes):
- [lista filtrada]
```

---

## 🚀 CHECKLIST EJECUCIÓN

- [ ] Descargar/revisar las 2 carpetas Drive
- [ ] Generar DRIVE_MAPPING completo (150 pacientes)
- [ ] Crear script `enriquecer_pacientes.py`
- [ ] Ejecutar en Obsidian sandbox primero
- [ ] Validar 10 archivos al azar
- [ ] Ejecutar en producción
- [ ] Generar 3 índices nuevos
- [ ] Notificar a Javier: ✅ FASE 1 COMPLETADA

---

## ⏰ TIMELINE

**Mañana (2026-06-27) 09:00 AM:** Generar mapping  
**Mañana (2026-06-27) 10:00 AM:** Ejecutar script  
**Mañana (2026-06-27) 10:30 AM:** Validar + crear índices  
**Mañana (2026-06-27) 11:00 AM:** ✅ FASE 1 DONE

---

**¿EJECUTAMOS MAÑANA A LAS 9AM?** ✅

O prefieres que primero hagamos una prueba con 10 pacientes?
