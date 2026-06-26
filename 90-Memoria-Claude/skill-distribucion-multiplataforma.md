---
name: skill-distribucion-multiplataforma
description: Skill IA para content distribution multiplataforma — blogs, videos, testimonios, creativos → YouTube, LinkedIn, Reddit, Wikipedia, Blog + GHL integration
metadata:
  type: project
  status: PENDIENTE-DESARROLLO
  prioridad: ALTA
  estimacion: 2-3 semanas
  fecha_creacion: 2026-06-25
---

# 🚀 SKILL: Distribución Multiplataforma (PENDIENTE DESARROLLO)

**Estado:** 🔴 DISEÑO COMPLETADO — LISTO PARA DESARROLLAR  
**Responsable:** Javier Forero  
**Fecha creación:** 2026-06-25  
**Última actualización:** 2026-06-25  

---

## 🎯 Misión

Crear una **máquina de contenido permanente** que:
- Tome contenido del equipo (blogs, videos, testimonios, creativos)
- Lo adapte automáticamente por plataforma (YouTube, LinkedIn, Reddit, Wikipedia, Blog)
- Lo publique en calendario quincenal/mensual
- Capture engagement → integre con GHL
- Genere rankings SEO + autoridad de marca

**Objetivo final:** Presencia activa 24/7 sin intervención diaria.

---

## 📊 Análisis de Viabilidad (COMPLETADO — 2026-06-25)

### APIs + MCPs Disponibles ✅

| Plataforma | API/MCP | Scheduling | Status |
|---|---|---|---|
| **YouTube** | Data API v3 | Nativo (100 vids/día) | ✅ READY |
| **LinkedIn** | Share API | Cron job interno | ✅ READY |
| **Reddit** | PRAW + API | Scheduling built-in | ✅ READY |
| **Wikipedia** | MediaWiki API | Edits/propuestas | ✅ READY |
| **GHL** | MCP oficial + V2 API | Webhooks + lead capture | ✅ READY |
| **Google Drive** | MCP Claude | Read+write | ✅ READY |
| **Shopify** | MCP Claude | Blog API | ✅ READY |
| **Supabase** | MCP Claude | Métricas + calendarios | ✅ READY |

**Conclusión:** 100% viable. Todas las integraciones existen.

---

## 🏗️ ARQUITECTURA TÉCNICA

### Stack
```
LENGUAJE:      Claude Prompt + Python (crons opcionales)
MCPs USADOS:   Google Drive, Shopify, GHL (webhooks), Supabase
APIs USADAS:   YouTube Data v3, LinkedIn Share, Reddit PRAW, Wikipedia MediaWiki, GHL V2
ALMACENAJE:    Supabase (métricas, calendarios, versiones)
SCHEDULING:    n8n / Make (cron jobs) o Cloudflare Workers
MONITORING:    Clarity MCP (bounce, clicks landings)
```

### Flujo General
```
┌─────────────────────────┐
│ RECOLECCIÓN (Pull)      │
│ Google Drive/Notion/RSS │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ ANÁLISIS + PLAN         │
│ Keywords, audiencia,    │
│ formato, timing         │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ GENERACIÓN              │
│ 5 variantes por plat    │
│ Validación SEO/marca    │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ PUBLICACIÓN (Cron)      │
│ YouTube, LinkedIn,      │
│ Reddit, Wiki, Blog      │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ CAPTURA + GHL           │
│ Engagement → webhooks   │
│ → Pipeline              │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│ REPORTES                │
│ Semanal + Mensual       │
│ ROI por canal           │
└─────────────────────────┘
```

---

## 📋 FASES DE DESARROLLO

### FASE 1: Recolección (Semana 1)
- [ ] Conectar Google Drive MCP
- [ ] Detectar automáticamente nuevos blogs/videos/testimonios
- [ ] Parsear metadatos (título, autor, fecha, categoría)
- [ ] Almacenar en tabla Supabase `contenido_fuente`

**Deliverable:** Sistema que lee carpeta compartida automáticamente

---

### FASE 2: Análisis + Planificación (Semana 1-2)
- [ ] Extraer keywords + SEO metadata
- [ ] Detectar tema + audiencia objetivo
- [ ] Generar 5 variantes de ángulos creativos
- [ ] Crear calendario editorial (quincenal/mensual)
- [ ] Validar compliance médico vs. políticas Innovart
- [ ] Asignar horarios óptimos por plataforma

**Deliverable:** Calendar JSON + metadata enriquecido

---

### FASE 3: Generación de Contenido (Semana 2-3)

#### YouTube
- [ ] Títulos SEO optimizados (60-70 chars)
- [ ] Descripciones (2000 chars con links internos)
- [ ] Timestamps + capítulos automáticos
- [ ] Miniatura sugerida (prompt para imagen)
- [ ] 3 Shorts de 15-60s (templates automáticos)
- [ ] 2-3 Community posts por video

#### LinkedIn
- [ ] Post corto (150-200 chars con emoji)
- [ ] Post largo (800-1000 chars narrativo)
- [ ] Carrusel (3 slides educativo)
- [ ] CTA estratégico (Lead, Sign Up, Comment)
- [ ] Hashtags relevantes (8-10)
- [ ] Mentions sugeridas (Innovart, doctores, partners)

#### Reddit
- [ ] Identificar 3-5 subreddits relevantes
- [ ] Analizar reglas (no-spam check)
- [ ] Títulos que responden preguntas
- [ ] Post que agrega valor (no promocional)
- [ ] Respuestas a comentarios pre-escritas

#### Wikipedia
- [ ] Propuestas de mejora (neutral, verificable)
- [ ] Referencias añadidas (con links a fuentes)
- [ ] Secciones expandidas (con data de Innovart si aplica)
- [ ] Borrador para revisión manual

#### Blog Shopify
- [ ] Versión larga (SEO optimized, 2000+ words)
- [ ] Meta description (155 chars)
- [ ] Internal links automáticos (a blogs relacionados)
- [ ] Schema JSON-LD (Article, MedicalClinic, FAQ)
- [ ] Imagen hero (prompt para generación)

**Deliverable:** Contenido generado por plataforma en tabla Supabase

---

### FASE 4: Publicación Automática (Semana 3)
- [ ] YouTube: Usar Data API v3 para scheduled upload
- [ ] LinkedIn: Cron job + Share API
- [ ] Reddit: Scheduler built-in (PRAW)
- [ ] Wikipedia: Propuestas (manual review → editores)
- [ ] Blog: Shopify API para crear/publicar posts
- [ ] Logging: Todos los posts en `publicaciones` table Supabase

**Deliverable:** Sistema de cron jobs que publica en calendario

---

### FASE 5: Captura de Engagement (Semana 4)
- [ ] Monitorear comentarios en YouTube (Data API)
- [ ] Monitorear mentions en Reddit (PRAW)
- [ ] Webhooks GHL: cada comment/engagement → contact create
- [ ] Sentiment analysis: positivo/pregunta/objeción
- [ ] Lead scoring automático
- [ ] Pipeline assignment (cold/warm/hot)

**Deliverable:** GHL workflows que capturan engagement automático

---

### FASE 6: Reportes + Optimización (Semana 4)
- [ ] Dashboard Supabase: impresiones, clicks, CTR por plataforma
- [ ] Reportes semanales (email automático)
- [ ] Análisis de qué funcionó (trending topics)
- [ ] Recomendaciones automáticas (ajustes para próximo mes)
- [ ] SEO tracking: rankings por keywords

**Deliverable:** Dashboard + reportes automáticos

---

## 📥 ENTRADAS (Contenido del Equipo)

El equipo sube a **Google Drive** (o donde prefieras):

```
/Innovart-Contenido/
├── 📝 Blogs/
│   ├── blog-1-implante-capilar.md
│   ├── blog-2-resultados-6meses.md
│   └── ...
├── 🎥 Videos/
│   ├── video-1-testimonio-bogota.md (con link YouTube)
│   ├── video-2-tecnica-fue.md
│   └── ...
├── 📱 Testimonios/
│   ├── testimonio-carlos-bogota.md (texto + foto)
│   ├── testimonio-maria-video.md
│   └── ...
└── 🎨 Creativos/
    ├── creativo-1-antes-despues.md (imagen descripción)
    ├── creativo-2-beneficios.md
    └── ...
```

**Formato:** Markdown simple con metadatos:
```markdown
---
titulo: "..."
autor: "Dr. Carreño"
tema: "implante capilar"
audiencia: "hombres 30-50"
palabras_clave: "implante, calvicie, FUE"
ciudad: "Bogotá, Medellín, Panamá"
fecha: "2026-06-25"
---

Contenido aquí...
```

---

## 📤 SALIDAS (Publicaciones)

### Por Plataforma

**YouTube:** [Título]
- Description + timestamps
- 3 Shorts generados
- 2 Community posts
- Scheduled para 2026-06-30 9:00 AM

**LinkedIn:** [Post corto]
- Post largo
- Carrusel
- CTA
- Programado para 2026-07-01 9:00 AM

**Reddit:** [Título post]
- Análisis de subreddits
- Post por comunidad
- Respuestas pre-escritas

**Wikipedia:** [Propuesta mejora]
- Borrador neutral
- Referencias añadidas
- Pendiente manual review

**Blog Shopify:** [Post largo]
- SEO optimized
- Schema JSON-LD
- Internal links
- Publicado en shopify

---

## 🔗 Integración GHL

### Webhooks Automáticos
```json
{
  "event": "youtube_comment",
  "video_id": "...",
  "commenter": "...",
  "sentiment": "question|objection|praise",
  "text": "...",
  "action": "create_contact|score_lead|assign_workflow"
}
```

### Flujos
- YouTube comment → GHL contact (email si tiene, tag por tema)
- Reddit mention → GHL lead scoring
- LinkedIn engagement → warm lead
- All → CRM pipeline automático

---

## 🎯 Métricas (Dashboard Supabase)

### Semanal
- [ ] Impresiones por plataforma
- [ ] Clicks/CTR
- [ ] Engagement (likes, comments, shares)
- [ ] Leads capturados
- [ ] Valor de MQL (qualified)

### Mensual
- [ ] ROI por canal (leads × valor medio)
- [ ] SEO ranking movement (keywords target)
- [ ] Autoridad ganada (backlinks, mentions)
- [ ] Costo por lead por plataforma
- [ ] Recomendaciones (qué cambiar mes próximo)

---

## 🚨 Reglas + Compliance

### Para Todos
- ✅ Validar gramática + ortografía
- ✅ Verificar facts médicos (no inventar)
- ✅ Respetar manual de marca Innovart
- ✅ Sin promesas falsas (ej: "vitalicia" = PROHIBIDO)
- ✅ SEO primero, promoción después

### Por Plataforma
- **YouTube:** Thumbnails, descripciones SEO, community guidelines OK
- **LinkedIn:** Profesional, educativo, CTA suave
- **Reddit:** NUNCA spam, SIEMPRE valor, respetar reglas subreddit
- **Wikipedia:** Neutral, verificable, con referencias
- **Blog:** INVIMA compliant, schema correcto, links internos

---

## 🛠️ Skills + Recursos Existentes

Reutilizar:
- [[skill-ver-videos]] — procesar videos automáticamente
- [[skill-geo-salud-ia]] — GEO ranking + insights
- [[skill-aeo-maestro]] — Answer Engine Optimization (AEO)
- [[notebooklm]] — bases de conocimiento (GEMINNOVART, GEMSEOINNOVART)
- [[adn-comunicacion-innovart]] — tono, avatares, restricciones

---

## 📅 Timeline Estimado

| Fase | Semanas | Hitos |
|---|---|---|
| 1. Recolección | 1 | Drive sync + Supabase schema |
| 2. Análisis | 1-2 | Calendar generado |
| 3. Generación | 2-3 | Contenido por plataforma |
| 4. Publicación | 3 | Crons activos |
| 5. Captura | 4 | GHL webhooks OK |
| 6. Reportes | 4 | Dashboard vivo |
| **TOTAL** | **2-3 semanas** | **MVP listo** |

**Próximas plataformas:** Instagram, TikTok, X, Medium, Quora (después)

---

## 🚀 Siguiente Paso (Cuando Empieces)

1. **Copia este archivo** a tu workspace local
2. **Crea rama:** `feature/skill-distribucion-v1`
3. **Inicia con FASE 1:** Solo lectura de Google Drive
4. **Testea con 1 blog:** Que llegue a YouTube + LinkedIn
5. **Escala:** Agregar plataformas una por una

---

## 📌 Notas Javier

- Este es tu **proyecto de tiempos libres**
- Está 100% planeado, solo falta code
- Reutiliza skills + MCPs existentes
- Comienza pequeño (1 plataforma) → escala
- Cada fase toma ~1 semana de dev part-time
- Preguntas → revisa [[skill-distribucion-multiplataforma]] (este archivo)

**Este sistema te ahorrará ~5 horas/semana de content ops manual.**

---

## 📍 Archivos Relacionados

- [[adn-comunicacion-innovart]] — Tono + avatares
- [[skill-ver-videos]] — Procesar videos
- [[skill-geo-salud-ia]] — GEO ranking
- [[skill-aeo-maestro]] — SEO authority
- [[tracking-setup-completa-2026-06-23]] — Metrics
- [[gemas-notebooklm-innovart]] — Knowledge bases
