---
name: feedback-informes-drive
description: Instrucción permanente — todos los informes generados deben guardarse en Google Drive. Archivos pesados (PDF/binarios) usar rclone, nunca el MCP de Drive.
metadata:
  type: feedback
  updated: 2026-06-12
---

Cuando se solicite generar un informe, reporte, auditoría o documento, guardarlo SIEMPRE en Google Drive en la carpeta CLAUDE dentro de 3. MERCADEO.

**Carpeta destino:** `3. MERCADEO / CLAUDE`
**ID carpeta CLAUDE en Drive:** `1rGB1E0XR4lcUwOes2Q9yACe4NphL8Tv5`
**ID carpeta 3. MERCADEO padre:** `1IhZv0uHtvx6aSXheRSgBFoVLYzHR12BT`
**Cuenta Google Drive:** innovartmedicalips@gmail.com

**Why:** El usuario quiere centralizar todos los documentos generados por Claude en esta carpeta de Drive. El MCP de Drive falla con archivos >100KB en base64 (el parámetro tiene límite de tamaño). Esto causó 6+ horas perdidas intentando subir un PDF de 591KB.

**How to apply:**

### Archivos ligeros (HTML, texto, JSON — menos de ~80KB)
Usar el MCP de Drive directamente:
```
mcp__681e05ae__create_file con parentId apropiado
```

### Archivos pesados (PDF, imágenes, binarios — más de ~80KB)
**SIEMPRE usar rclone** — está instalado y autenticado en la máquina del usuario:
```bash
rclone copy "/ruta/local/archivo.pdf" "gdrive:" --drive-root-folder-id FOLDER_ID
```

**rclone ya está configurado** como remote `gdrive` con cuenta innovartmedicalips@gmail.com.
No necesita autenticación adicional. Sube cualquier tamaño en segundos.

### IDs de carpetas frecuentes
- Informes diarios Meta: `1XFEluaAao-mpp8rnDMKL2JirHp2WlWNl`
- Carpeta CLAUDE general: `1rGB1E0XR4lcUwOes2Q9yACe4NphL8Tv5`

### Regla de decisión rápida
| Tipo de archivo | Herramienta |
|---|---|
| HTML / texto / JSON | MCP Drive `create_file` |
| PDF / imagen / binario | `rclone copy` vía Bash |
