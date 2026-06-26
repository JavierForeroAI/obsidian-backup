---
name: pendientes-backup-obsidian
description: Backup automático de Obsidian a GitHub - tareas pendientes
metadata:
  type: project
  priority: alta
  fecha: 2026-06-26
---

# PENDIENTES: Backup Obsidian → GitHub

## 📋 Tarea
Configurar backup automático de carpetas Obsidian (Innovart + Claude-Brains) a GitHub privado.

## 🎯 Pasos pendientes

### 1️⃣ Crear repo privado en GitHub
- [ ] Ir a github.com → New repository
- [ ] Nombre: `obsidian-backup` o `claude-brains-backup`
- [ ] Seleccionar **Private**
- [ ] Copiar URL del repo (ej: `https://github.com/tu-usuario/obsidian-backup.git`)

### 2️⃣ Configurar Git local
- [ ] Inicializar repo en `/Users/javierforero/Documents/Obsidian-Innovart/`
- [ ] Agregar remote a GitHub
- [ ] Primer commit y push

### 3️⃣ Automatizar backups diarios
- [ ] Crear script en `~/.claude/scripts/backup-obsidian.sh`
- [ ] Agregar a crontab para ejecutar cada noche a las 2 AM

## 📁 Carpetas a respaldar
- `~/Documents/Obsidian-Innovart/` (principal)
- `~/Documents/Claude-Brains/` (General, Innovart, Churra, Ritual)

## 🔧 Script básico a crear
```bash
#!/bin/bash
VAULT_PATH="$HOME/Documents/Obsidian-Innovart"
DATE=$(date +%Y-%m-%d_%H:%M:%S)

cd "$VAULT_PATH"
git add .
git commit -m "Backup: $DATE" || true
git push origin main

echo "✅ Backup guardado a GitHub"
```

## ⚙️ Configuración cron
```
0 2 * * * /Users/javierforero/.claude/scripts/backup-obsidian.sh
```

---

**Status**: ⏳ Pendiente configuración  
**Asignado a**: Javier  
**Next step**: Crear repo en GitHub
