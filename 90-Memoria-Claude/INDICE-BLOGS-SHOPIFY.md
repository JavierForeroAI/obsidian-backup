---
name: INDICE-BLOGS-SHOPIFY
description: "Índice maestro: todos los documentos sobre estrategia de publicar 16 blogs médicos en Shopify"
metadata:
  type: index
  fecha: 2026-06-23
---

# Índice Maestro: 16 Blogs Médicos → Shopify

**Fecha:** 23 de junio de 2026  
**Proyecto:** Publicar 16 blogs médicos de Innovart en Shopify sin romper tema ni sanitizar contenido  
**Estado:** Análisis completado — 4 opciones evaluadas, 1 recomendada  

---

## 📑 Documentos

### 1. PARA LEER PRIMERO (Si tienes 15 min)
**[[guia-practica-blogs-shopify-javier]]**
- Lenguaje simple, sin jargón técnico
- Explica qué va dónde y cómo funciona
- Responde todas las dudas comunes
- Checklist: "¿estamos listos?"
- **Ideal para:** Javier, decisión rápida

### 2. PARA DECIDIR (Si tienes 5 min)
**[[resumen-ejecutivo-blogs-shopify]]**
- 1 página, tabla comparativa de 3 opciones descartadas vs. 1 ganadora
- Por qué Opción 4 (Hybrid Approach)
- Matriz de riesgos mitigados
- Siguientes pasos directos
- **Ideal para:** ejecutivos, personas ocupadas

### 3. PARA ENTENDER (Si tienes 30 min)
**[[estrategia-publicar-blogs-shopify-2026-06-23]]**
- Análisis profundo de 4 opciones arquitectónicas
- Pros/contras de cada una
- Evaluación de riesgos
- Plan de ejecución (3 fases)
- Schema JSON-LD: cómo se preserva
- WhatsApp tracking: cómo funciona
- GEO/SEO impacto
- Documentación futura
- **Ideal para:** arquitectos de soluciones, técnicos que quieren el "por qué"

### 4. PARA IMPLEMENTAR (Si tienes que hacer el trabajo)
**[[shopify-blog-post-template-tecnico]]**
- Especificación técnica COMPLETA
- JSON schema de metafields
- Template Liquid de 7 secciones
- CSS centralizado (listo para pegar)
- GraphQL mutations (crear blog posts)
- Python script automático (crear 16 blogs)
- Checklist de validación
- **Ideal para:** desarrolladores, ops que ejecutan

---

## 🎯 Recorrido recomendado por perfil

### Si eres Javier (propietario):
1. Leer: [[guia-practica-blogs-shopify-javier]] (15 min)
2. Decidir: "Vamos con Opción 4"
3. Autorizar: "Claude, configura FASE 1"
4. Validar: "Revisamos el blog de prueba en preview"
5. Publicar: "Claude, publica los 16 blogs"

### Si eres Dev/Ops (implementador):
1. Leer: [[estrategia-publicar-blogs-shopify-2026-06-23]] (entender el contexto)
2. Técnico: [[shopify-blog-post-template-tecnico]] (guía paso-a-paso)
3. Ejecutar: metafield definitions → template → secciones → CSS → validar
4. Automatizar: generar datos + script Shopify
5. Publicar: ejecutar script, validar, celebrar

### Si eres gestor de proyecto:
1. Leer: [[resumen-ejecutivo-blogs-shopify]] (5 min, decisión rápida)
2. Presentar a Javier: [[guia-practica-blogs-shopify-javier]]
3. Timeline: Fase 1 (4h) → Fase 2–3 (20 min) → Fase 4 (30 min) = Total 5h
4. Riesgo: MUY BAJO (metafields son datos, tema toca UNA sola vez)
5. ROI: 30–50% de leads nuevos en 90 días (estima baja)

---

## 📊 Matriz de decisión

| Opción | Fidelidad | Seguridad | Escalabilidad | Mantenibilidad | Veredicto |
|--------|-----------|-----------|---------------|----------------|----------|
| 1: Solo metafields | 60% | ✅ Muy alto | ✅ Alta | ✅ Alta | ❌ Básica |
| 2: CSS en metafield | 95% | ⚠️ Medio | ⚠️ Media | ❌ Baja | ❌ Pesada |
| 3: GemPages | 85% | ✅ Muy alto | ⚠️ Media | ⚠️ Media | ❌ Confusa |
| **4: Hybrid** ⭐ | **95%** | **✅ Máximo** | **✅ Perfecta** | **✅ Excelente** | **✅ GANADORA** |

---

## 🔄 Fases de ejecución

```
FASE 0: Decisión (15 min)
  └─ Lees guía, dices "sí"

FASE 1: Setup tema (4–5 h)
  ├─ Metafield definitions
  ├─ Template blog-post.json
  ├─ Secciones Liquid (7 archivos)
  ├─ CSS centralizado
  └─ Validar en preview

FASE 2: Preparar datos (1 h, automático)
  └─ Python script: HTML locales → JSON

FASE 3: Publicar (20 min, automático)
  └─ Python script: JSON → 16 blogs en Shopify

FASE 4: Validar (30 min, manual)
  ├─ ¿Se ve bien?
  ├─ ¿Schema JSON en <head>?
  ├─ ¿Tracking WhatsApp funciona?
  ├─ ¿Related articles redirigen?
  └─ ✅ Google Rich Results Test

FASE 5: Medir (30 días, observar)
  ├─ Google Search Console: indexación
  ├─ AI Visibility Score: visibilidad SEO
  ├─ GHL analytics: leads por blog
  └─ ROI: conversión vs. expectativa
```

---

## 🚀 Quick Start (si tienes prisa)

1. **Leer:** [[resumen-ejecutivo-blogs-shopify]] (5 min)
2. **Decidir:** Opción 4 ✅
3. **Autorizar:** "Vamos"
4. **Mensaje a Claude:** 
   ```
   Vamos con la estrategia Opción 4 (Hybrid). 
   Por favor, configura FASE 1 (metafields + template + secciones + CSS).
   Tiempo estimado: 4–5 horas.
   ```
5. **Esperar:** Claude configura
6. **Validar:** "¿Cómo se ve el blog de prueba?"
7. **Publicar:** Claude publica 16 blogs (20 min automático)
8. **Celebrar:** 16 blogs LIVE, Google indexando, leads llegando

---

## 📋 Checklist de decisión

- [ ] Entiendo que los blogs se dividen en Shopify admin + metafields
- [ ] Entiendo que Shopify sanitiza HTML (es normal, schema está protegido)
- [ ] Entiendo que puedo cambiar estilos/contenido después fácilmente
- [ ] Entiendo que tracking WhatsApp se preserva
- [ ] Confío en que Opción 4 es la mejor arquitectura
- [ ] Estoy listo para que Claude configure el tema
- [ ] Estoy listo para publicar los 16 blogs
- [ ] Estoy listo para validar en frontend y medir impacto en 30 días

**Si marcaste todos:** ✅ Listo para comenzar

---

## 📞 Contacto y escaladas

| Pregunta | Responsable | Documento |
|----------|-------------|-----------|
| "¿De qué va?" | Javier | [[guia-practica-blogs-shopify-javier]] |
| "¿Cuál es la mejor opción?" | PM | [[resumen-ejecutivo-blogs-shopify]] |
| "¿Por qué esa opción?" | Arquitecto | [[estrategia-publicar-blogs-shopify-2026-06-23]] |
| "¿Cómo se implementa?" | Dev | [[shopify-blog-post-template-tecnico]] |
| "¿Se puede cambiar después?" | PM + Dev | [[estrategia-publicar-blogs-shopify-2026-06-23]] (Mantenimiento) |
| "¿Cuánto va a mejorar el SEO?" | SEO | [[estrategia-publicar-blogs-shopify-2026-06-23]] (Impacto GEO/SEO) |

---

## 🔗 Documentos relacionados

**Contexto historico:**
- [[fase-2-upgrade-blogs-contenido-2026-06-22]] (16 blogs generados con firma + schema)
- [[blog-salud-capilar-drive]] (blogs en Google Drive)

**Shopify ecosystem:**
- [[shopify-ecosistema-mcp]] (inventario tienda, limitaciones MCP)
- [[shopify-playbook-capacidades-mcp]] (qué se puede/no se puede hacer en Shopify)
- [[shopify-alt-text-home-panama]] (caso anterior: editar PageFly)

**SEO/GEO:**
- [[seo-plan-shopify-2026-05]] (plan SEO general, blogs es una parte)
- [[geo-visibilidad-ia-auditoria-2026-06-22]] (impacto GEO esperado)

---

## 📈 Timeline y responsabilidades

| Hito | Fecha est. | Responsable | Duración | Status |
|------|-----------|-------------|----------|--------|
| **Decisión** | Hoy | Javier | 15 min | ⏳ A DECIDIR |
| **FASE 1: Setup tema** | Semana 1 | Claude | 4–5 h | ⏳ A AUTORIZAR |
| **FASE 2: Datos** | Semana 1 | Claude | 1 h | ⏳ A EJECUTAR |
| **FASE 3: Publicar** | Semana 1–2 | Claude | 20 min | ⏳ A EJECUTAR |
| **FASE 4: Validar** | Semana 2 | Javier + Claude | 30 min | ⏳ A HACER |
| **FASE 5: Medir** | Semana 2–5 | Javier + Analytics | 30 días | ⏳ A OBSERVAR |
| **Bono: Backlinks** | Semana 3–4 | Marketing | TBD | ⏳ FUTURO |

---

## ❓ FAQ rápido

**P: ¿Se va a romper algo?**  
R: No. Tema se toca UNA sola vez. Metafields son datos puros. Cero riesgo de ruptura.

**P: ¿Shopify sanitiza el schema JSON-LD?**  
R: No. Schema está en metafield (JSON seguro). Liquid lo inyecta en `<head>`.

**P: ¿Puedo cambiar estilos después?**  
R: Sí. Editas 1 archivo CSS, todos los 16 blogs reflejan el cambio (DRY).

**P: ¿Puedo agregar blog 17 en el futuro?**  
R: Sí. Script automático en 5 min.

**P: ¿Cuánto tiempo toma el setup?**  
R: 4–5 horas (una sola vez). Después, publicar blogs = 5 min cada uno automático.

**P: ¿Cuándo vemos resultados SEO?**  
R: Google indexa en 1–2 semanas. Tráfico empieza en semana 3–4. Visibilidad máxima en mes 2–3.

**P: ¿Cuál es el ROI?**  
R: Estima baja: 30–50% de leads nuevos en 90 días. Blogs = tráfico "gratuito" que dura años.

---

**Última actualización:** 23 de junio de 2026  
**Próximo checkpoint:** Autorización de Javier para FASE 1  
**Responsable:** Claude Code  
**Validador:** Javier Forero

---

*Para comenzar: lee [[guia-practica-blogs-shopify-javier]] o [[resumen-ejecutivo-blogs-shopify]] según tengas prisa.*
