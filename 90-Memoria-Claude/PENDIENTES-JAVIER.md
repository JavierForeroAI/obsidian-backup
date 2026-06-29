---
name: pendientes-javier
description: Listado master de pendientes y tareas en progreso para Javier — prioridad, fechas, roadmaps
metadata:
  type: project
  última_actualización: 2026-06-26
---

# 📋 PENDIENTES JAVIER — Master List

**Última actualización:** 2026-06-26

---

## 🔴 PRIORIDAD BAJA (Tiempos libres)

### #1 — Skill Distribución Multiplataforma
**Estado:** Pendiente  
**Estimación:** 2-3 semanas part-time  
**Descripción:** Máquina de contenido automatizada (blogs, videos, testimonios, creativos) → YouTube, LinkedIn, Reddit, Wikipedia, Blog Shopify + GHL integration.

**📚 Referencia completa:**
- [[skill-distribucion-multiplataforma]] — Análisis, arquitectura, 6 fases, roadmap

**🚀 Para empezar:**
1. Lee el documento maestro (skill-distribucion-multiplataforma.md)
2. Crea rama: `feature/skill-distribucion-v1`
3. Fase 1: Google Drive sync + Supabase schema
4. Test rápido: 1 blog → YouTube + LinkedIn
5. Escala: plataformas una por una

**⏱️ Roadmap:**
- Semana 1: Fase 1-2 (Recolección + Análisis)
- Semana 2-3: Fase 3-4 (Generación + Publicación)
- Semana 4: Fase 5-6 (Captura + Reportes)

**💡 Beneficio:** Ahorra ~5 horas/semana de content ops manual

---

## 🟡 PRIORIDAD NORMAL (En curso / próxima semana)

### #2 — Reacciones a Stories de IG disparan el bot en vano
**Estado:** Pendiente  
**Fecha detectado:** 2026-06-27  
**Descripción:** Los mensajes vacíos (`body: ""`) de Instagram son reacciones/likes a stories de Innovart. GHL los registra como conversaciones TYPE_INSTAGRAM y activan el workflow "3. Recibir msj IG" completo — Sofia responde con el saludo aunque no hay lead real. Es ruido puro que consume mensajes del bot y crea contactos fantasma.

**Ejemplo real:** "el cuco humor" tiene 6 entradas distintas (May-Jun 2026), todas `body: ""`, todas respondidas por Sofia.

**Solución propuesta:**  
Agregar condición al inicio del workflow "3. Recibir msj IG":
- `IF message.body == "" → STOP (no procesar)`  
O crear una rama de salida temprana para `body` vacío antes del saludo.

**Impacto:** Reduce ruido en CRM, ahorra mensajes del bot, evita contactos irrelevantes.

---

## 🟢 PRIORIDAD ALTA (CRÍTICO / BLOQUEANTE)

*(Vacío — sin bloqueantes activos)*

---

## ✅ COMPLETADOS (Esta sesión)

- ✅ Análisis viabilidad skill distribución multiplataforma
- ✅ Búsqueda de APIs + MCPs disponibles
- ✅ Diseño de arquitectura 6 fases
- ✅ Creación de documento maestro
- ✅ Setup en MEMORY.md + Task List

---

## 📌 NOTAS RÁPIDAS

- **Skill final:** `/distribución-contenido` (recomendado) o `/content-distribution`
- **Pull-based:** El equipo sube a carpetas compartidas, sistema automatiza todo
- **Integración GHL:** Webhooks + lead capture automático
- **Compliance:** Validar claims médicos, respetar INVIMA

---

## 🔗 Links útiles

- **Documento maestro:** `/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/skill-distribucion-multiplataforma.md`
- **Task en Claude:** `claude task #1`
- **Ver tareas:** `claude tasks`
- **Cerebro Innovart:** `/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/`

---

## 💭 Próxima sesión

Cuando retomes: lee skill-distribucion-multiplataforma.md, abre branch feature/skill-distribucion-v1, y comienza Fase 1 (Google Drive sync).

