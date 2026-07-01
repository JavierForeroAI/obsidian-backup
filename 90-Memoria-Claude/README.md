# README Maestro — Skill Distribución Multiplataforma Innovart

**Versión:** 1.0  
**Última actualización:** 30 de junio de 2026  
**Estado:** En desarrollo (roadmap 2-3 semanas part-time)  
**Mantenedor:** Javier Forero (@innovartmedicalips)

---

## Bienvenida Profesional

Bienvenido a la **Skill de Distribución Multiplataforma de Innovart**, la máquina automatizada que transforma un único contenido en campañas coordinadas en 7+ canales simultáneamente.

Esta skill está diseñada para **eliminar trabajo manual redundante** en la distribución de contenido, mientras mantiene la consistencia de marca y optimiza para cada plataforma específica. Es especialmente crítica para equipos pequeños (como Innovart) que necesitan máxima cobertura con mínimo esfuerzo operacional.

**Objetivo principal:** Blogs → Videos → Testimonios → Creativos → 7 Plataformas (YouTube, LinkedIn, Reddit, Wikipedia, Blog Shopify, GHL, + canales propios) con una sola interfaz.

---

## ¿Qué es esta Skill?

### En 30 segundos

Una máquina de contenido **pull-based** que:
1. **Monitorea carpetas** donde tu equipo sube contenido base (blogs, videos, PDFs)
2. **Analiza automáticamente** el contenido (extrae temas, audiencias, intent)
3. **Genera variaciones** optimizadas para cada plataforma (YouTube description ≠ LinkedIn post)
4. **Publica en paralelo** a 7+ canales con un clic
5. **Captura leads** a través de GHL integration
6. **Reporta ROI** por plataforma (views, clicks, conversiones)

### Arquitectura de 6 Fases

```
┌─────────────────────────────────────────────────────────────────┐
│ Fase 1: INGESTA                                                 │
│ • Equipo sube contenido a /Distribución/Input/[tipo]           │
│ • Script monitorea cambios (polling o webhook)                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Fase 2: ANÁLISIS                                                │
│ • Claude analiza: tema, audiencia objetivo, intent              │
│ • Extrae metadatos: keywords, CTAs, formatos                  │
│ • Evalúa viabilidad por plataforma                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Fase 3: GENERACIÓN VARIABLE                                     │
│ • YouTube: descripción 1,000 chars + tags + thumbnail brief   │
│ • LinkedIn: hilo 5 posts + imágenes + hashtags                │
│ • Reddit: post + contexto comunidad + rules compliance        │
│ • Wikipedia: sección neutral + referencias                    │
│ • Shopify Blog: artículo full HTML + SEO meta                 │
│ • GHL: lead magnet + copy conversión                          │
│ • Email/SMS: secuencia nurture                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Fase 4: PREAPROBACIÓN                                           │
│ • Checklist automático (marca, compliance, ortografía)         │
│ • Genera preview HTML por plataforma                           │
│ • Requiere aprobación Javier si hay cambios mayores            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Fase 5: PUBLICACIÓN                                             │
│ • APIs nativas: YouTube, LinkedIn, Reddit, Wikipedia           │
│ • Métodos fallback: Shopify MCP, GHL MCP, email directo       │
│ • Retry lógico + logging de cada publicación                  │
│ • Tags UTM injected automáticamente                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Fase 6: MONITOREO & REPORTING                                   │
│ • Recolecta métricas: views, clicks, comentarios, conversiones │
│ • Genera reporte diario por plataforma + total                │
│ • Identifica qué tipo de contenido funciona mejor             │
│ • Retroalimenta cambios automáticos (o sugiere manuales)      │
└─────────────────────────────────────────────────────────────────┘
```

### Casos de Uso Oficiales

| Caso | Trigger | Entrada | Salida | ROI Esperado |
|------|---------|---------|--------|--------------|
| **Blog nuevo** | Se sube a `/Input/Blogs/` | `.md` 2,000+ palabras | 7 posts (YT desc, LI hilo, Reddit, Wiki, Blog, GHL, Email) | 50-100 leads/mes |
| **Vídeo nuevo** | Se sube a `/Input/Videos/` | `.mp4` o enlace YouTube | YT optimizado + thumbnails + IG Reels + TikTok draft | 5,000-10,000 views/mes |
| **Testimonios** | Se suben transcripciones | `.docx` o `.pdf` | Blog post + LinkedIn case study + GHL social proof | 20-30 conversiones adicionales |
| **Creativos (imágenes)** | Se suben JPG/PNG | Imágenes base | Pinterest pins + Instagram posts + Facebook ads copy | 15-25 clicks adicionales por creativo |
| **Webinar/Live** | Se sube grabación + slides | `.mp4` + `.pptx` | YT, blog recap, LI article, lead magnet GHL, email secuencia | 100-200 leads calificados |
| **Informe/Whitepaper** | Se sube PDF | `.pdf` marketing | Blog summary + LI thought leadership + GHL gated + Email | 50-100 leads premium |

---

## Cuándo Usarla: 15+ Ejemplos Concretos

### Ejemplos por Plataforma

#### 1. **YouTube**
- Tengo un video de "Implante capilar FUE vs FUT" (15 min)
- **Dispatch:** `/distribucion upload-video implante-fue-vs-fut.mp4`
- **Resultado:** Descripción 1,200 chars, 25 tags, thumbnail brief, subtítulos automáticos, playlist asignada
- **Lead capture:** CTA a landing Bogotá en descripción con UTM

#### 2. **LinkedIn**
- Blog nuevo: "Signos de caída de cabello a los 30 años"
- **Dispatch:** `/distribucion upload-blog signos-caida-30.md`
- **Resultado:** Hilo de 5 posts (1 hook + 3 insights + 1 CTA), imágenes entrelazadas, hashtags (#AlopeciaJoven #Capilar)
- **Lead capture:** QR en imagen final → landing Medellín

#### 3. **Reddit**
- Artículo: "Mitos comunes sobre trasplantes capilares"
- **Dispatch:** `/distribucion upload-blog mitos-trasplantes.md`
- **Resultado:** Posts en r/AskMen, r/Hairloss, r/AskWomen con reglas compliance
- **Lead capture:** Comentario pinned con "Si tienes dudas, DM" + link WhatsApp

#### 4. **Wikipedia**
- Explicación científica de alopecia androgenética
- **Dispatch:** `/distribucion upload-wiki alopecia-androgenética.md`
- **Resultado:** Sección Wikipedia con referencias académicas + backlink a blog Innovart
- **Lead capture:** NO (Wikipedia es neutral), pero SEO + autoridad mejora

#### 5. **Blog Shopify**
- Caso de éxito: "De perder 200 cabellos/día a recuperar densidad"
- **Dispatch:** `/distribucion upload-blog caso-exito-densidad.md`
- **Resultado:** Artículo publicado en blog.innovartmedical.com con SEO meta, imágenes, HTML limpio
- **Lead capture:** CTA en hero + form al pie + popup para email

#### 6. **GHL (Lead Magnet)**
- Guía descargable: "Checklist pre-trasplante capilar"
- **Dispatch:** `/distribucion upload-ghl-lead-magnet checklist-pre-trasplante.pdf`
- **Resultado:** Landing GHL autogenerada + formulario + flujo nurture automático
- **Lead capture:** Email + teléfono + ciudad + intent nivel

#### 7. **Email Sequence**
- Blog sobre "Recuperación post-trasplante" (primeras 2 semanas)
- **Dispatch:** `/distribucion upload-email-sequence recuperacion-post-trasplante.md`
- **Resultado:** Secuencia de 5 emails (Day 1: expectativa, Day 3: tips, Day 7: riesgos, Day 14: seguimiento, Day 21: testimonios)
- **Lead capture:** Abiertos + clicks → retargeting + lead scoring automático

---

### Ejemplos Avanzados: Batches Multi-contenido

#### 8. **Campaña Completa: "Cabello Saludable a los 40"**
```
├─ Blog (2,500 palabras)
├─ Video (12 minutos)
├─ Infografía (3 formatos: Pinterest, Instagram, LinkedIn)
├─ Testimonios (3 videos, 30 segundos cada)
└─ Email secuencia (7 emails)

Dispatch: /distribucion batch campana-cabello-40.yaml

Resultado:
├─ YouTube: 1 video + playlist + comunidad post
├─ LinkedIn: 7 posts + 3 articles
├─ Pinterest: 3 pins (vertical formatos)
├─ Instagram: 7 posts + 3 Reels
├─ TikTok: 3 verticales (15 segundos)
├─ Blog Shopify: Artículo principal + 2 guest posts relacionados
├─ GHL: Landing lead magnet + 3 workflows activos
└─ Email: Secuencia 7 emails + SMS complementario

Lead capture: 200-400 leads estimados en 30 días
ROI: $50,000 - $100,000 COP en nuevas consultas (estimado)
```

#### 9. **Reposicionamiento Seasonal: "Otoño = Reinicio Capilar"**
- 1 artículo maestro
- Dispatch: `/distribucion seasonal-batch otono-reinicio-2026.md`
- Resultado: 12 variaciones (por ciudad, por plataforma, por audiencia)
- Reutilizable cada 6 meses

#### 10. **Crisis Management: "Alopecia por estrés"**
- Contenido sensible (trending topic)
- Dispatch: `/distribucion urgent alopecia-por-estres.md`
- Resultado: Publicación en paralelo en TODAS las plataformas en <2 horas
- Lead capture: +50% intent en 24h respecto a contenido normal

---

### Ejemplos Específicos por Audiencia

#### 11. **Para Hombresy Mujeres Jóvenes (18-35)**
- Content: Short-form videos + memes + relatability
- Dispatch: `/distribucion target-demographic young-adults video-alopecia.mp4`
- Plataformas primarias: TikTok, Instagram Reels, YouTube Shorts
- Tono: Conversacional, sin tecnicismos

#### 12. **Para Profesionales (35-55)**
- Content: Thought leadership + artículos en profundidad
- Dispatch: `/distribucion target-demographic professionals linkedin-article.md`
- Plataformas primarias: LinkedIn, Medium, blog corporativo
- Tono: Formal, basado en evidencia, números

#### 13. **Para Médicos/Salud (todosedades)**
- Content: Research, casos clínicos, protocolos
- Dispatch: `/distribucion target-demographic healthcare caso-clinico.pdf`
- Plataformas primarias: LinkedIn, ResearchGate, Wikipedia, Pubmed (si aplica)
- Tono: Académico, citable, peer-review ready

#### 14. **Para Tomadores de Decisión (decisores de compra)**
- Content: ROI, casos de éxito, comparativas
- Dispatch: `/distribucion target-demographic decision-makers caso-exito.md`
- Plataformas: LinkedIn, blog, email premium
- Tono: Números, garantías, social proof

#### 15. **Para Retargeting (ya visitó web)**
- Content: Urgencia, scarcity, testimonios
- Dispatch: `/distribucion retargeting-batch recuperar-carrito.md`
- Plataformas: Facebook Ads, Instagram, Email, SMS
- Tono: Conversión, oferta limitada

---

## Cómo Navegar esta Knowledge Base

### Estructura de Directorios

```
/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/
├── MEMORY.md (índice maestro — LEER PRIMERO)
├── README.md (este archivo)
│
├── 📁 distribucion-multiplataforma/ (nueva carpeta)
│   ├── GUIA-COMPLETA.md (manual técnico completo)
│   ├── ARQUITECTURA.md (diagramas + flujos)
│   ├── APIs-Y-INTEGRACIONES.md (YouTube, LinkedIn, Reddit, etc.)
│   ├── GHL-INTEGRATION.md (lead capture + workflows)
│   ├── TROUBLESHOOTING.md (problemas + soluciones)
│   ├── EJEMPLOS-YAML.md (templates batch)
│   └── ROADMAP-DESARROLLO.md (qué falta, qué viene)
│
├── 📁 tracking/ (tracking integrado)
│   ├── utm-tracking-avance-general.md
│   └── ctwa-sistema-100-operacional.md
│
├── 📁 crm/ (leads y workflows)
│   └── (archivos relacionados)
│
└── 📁 pauta/ (contexto de campañas)
    └── (archivos relacionados)
```

### Puntos de Entrada por Rol

| Rol | Lee Primero | Luego Lee | Skill |
|-----|------------|-----------|-------|
| **Javier (Dueño)** | Este README + [[skill-distribucion-multiplataforma-guia-completa]] | [[ROADMAP-DESARROLLO]] | `/distribucion batch campana-xxx.yaml` |
| **Community Manager** | [[GUIA-COMPLETA]] + [[EJEMPLOS-YAML]] | [[APIs-Y-INTEGRACIONES]] | `/distribucion upload-blog xxx.md` |
| **Trafficker/Digital** | [[GHL-INTEGRATION]] + [[TRACKING-SETUP]] | [[APIS-Y-INTEGRACIONES]] | `/distribucion batch-utm-tags campana.yaml` |
| **Desarrollador** | [[ARQUITECTURA]] + [[APIs-Y-INTEGRACIONES]] | [[TROUBLESHOOTING]] | Scripts /home/claude/scripts/ |
| **QA/Testing** | [[TROUBLESHOOTING]] | [[ARQUITECTURA]] | Checklist pre-publicación |

### Búsqueda Rápida: Preguntas Frecuentes

- **¿Cómo publico un blog en 7 plataformas a la vez?**  
  → [[GUIA-COMPLETA#Paso-a-paso-4-minutos | Paso a paso en GUIA-COMPLETA]]

- **¿Qué plataformas capturan leads automáticamente?**  
  → [[GHL-INTEGRATION#Lead-capture-por-plataforma | Tabla en GHL-INTEGRATION]]

- **¿Cómo configuro UTMs automáticos?**  
  → [[APIs-Y-INTEGRACIONES#UTM-Tagging | UTM-Tagging en APIS]]

- **¿Qué pasa si falla una plataforma en publicación?**  
  → [[TROUBLESHOOTING#Publicacion-falló-en-1-de-7-plataformas | Troubleshooting]]

- **¿Cuál es el costo estimado para implementar esto?**  
  → [[ROADMAP-DESARROLLO#Estimacion-esfuerzo | Estimación en ROADMAP]]

---

## Reglas Críticas de Innovart (⚠️ LEER ANTES DE USAR)

### 1. **NO Mezclar Sedes con Cuentas Meta**
- Las cuentas Meta NO son geográficas
- BGTA puede tener campañas de Medellín, Barranquilla, Panamá
- **REGLA:** Extraer ciudad del nombre de campaña, description, o destino, NO del nombre de cuenta
- **Impacto:** UTM `utm_campaign` DEBE incluir ciudad explícitamente
- **Referencia:** [[feedback-cuentas-meta-no-son-sedes|feedback-cuentas-meta-no-son-sedes.md]]

### 2. **Las Sedes Reales son 5 (Cali ❌ NO existe)**
- ✅ Bogotá
- ✅ Medellín
- ✅ Barranquilla
- ✅ Bucaramanga
- ✅ Panamá
- ❌ Cali (NUNCA usar)

**Impacto:** Copias, CTAs, números WhatsApp y configuración de GHL por ciudad
**Referencia:** [[regla-sedes-definitivas|regla-sedes-definitivas.md]]

### 3. **Shopify está en ESPAÑOL, instrucciones SIEMPRE en español**
- Editor de landings = **PageFly** (NO GemPages)
- Todos los nombres de menú en español exacto
- No ofrecer cambios vía MCP en código live (solo pasos manuales)

**Referencia:** 
- [[feedback-shopify-instrucciones-en-espanol|feedback-shopify-instrucciones-en-espanol.md]]
- [[feedback-editor-landings-es-pagefly|feedback-editor-landings-es-pagefly.md]]
- [[feedback-shopify-paginas-en-vivo|feedback-shopify-paginas-en-vivo.md]]

### 4. **Tracking: fbclid + UTMs + CAPI son NO NEGOCIABLES**
- Todo contenido publicado debe incluir `fbclid` capture en landing
- UTMs: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` + `utm_city`
- CAPI sin fbclid/email/teléfono = bloqueado (filtro automático)

**Estado actual:**
- fbclid ✅ en `/home`
- UTMs ✅ en landings, pendiente en 166 ads Meta
- CAPI ✅ con filtro SubmitApplication fantasma activo

**Referencia:** [[tracking-setup-completa-2026-06-23|tracking-setup-completa-2026-06-23.md]]

### 5. **No equivocarse con Números WhatsApp por Sede**
| Sede | Línea SMS (LeadConnector) | WhatsApp API (Meta CTWA) | Teléfono GHL |
|------|---------------------------|--------------------------|--------------|
| Bogotá | 573171224974 (Medellín, fallback) | +57 310/317/313 | +57 1 (código Bogotá) |
| Medellín | 573171224974 | +57 310/317/313 | +57 4 (código Med) |
| Barranquilla | 573171224974 | +57 300/301 | +57 5 (código Barq) |
| Bucaramanga | 573171224974 | +57 300/301 | +57 7 (código Bucaram) |
| Panamá | N/A | +507 650/6500 | +507 (código Panamá) |

**REGLA:** No asumir número por nombre de cuenta. Confirmar siempre por ciudad real de destino.
**Referencia:** [[lineas-innovart-sms-whatsapp-api-estructura|lineas-innovart-sms-whatsapp-api-estructura.md]]

### 6. **Compliance: Términos y Condiciones No Negociables**
- NUNCA prometer "garantía vitalicia" (no es legal)
- NUNCA garantizar "100% de resultados" (no científico)
- Siempre incluir disclaimer: "Resultados varían según caso individual"
- Siempre citar "Dr. Fabián Carreño Jiménez" como Director Médico

**Referencia:** [[home5-reconstruida-2026-06-22|home5-reconstruida-2026-06-22.md]]

### 7. **Blog: Estándar Maestro de 10 Criterios**
Antes de publicar cualquier blog (propio o distribuido):
- ✅ H1 único y relevante
- ✅ 2,000+ palabras
- ✅ SEO meta (título <60 chars, descripción <160 chars)
- ✅ Byline con foto + biografía Dr.
- ✅ "At a Glance" box (puntos clave)
- ✅ 2 botones WhatsApp (móvil e inline)
- ✅ Referencias a 3-5 artículos relacionados
- ✅ Bloque de sedes con números
- ✅ Firma con redes sociales
- ✅ Disclaimer médico

**Referencia:** [[estandar-maestro-blogs-innovart|estandar-maestro-blogs-innovart.md]]

---

## Quick Links — Toda la Documentación

### Pilares Técnicos
| Área | Archivo | Estado |
|------|---------|--------|
| **Tracking** | [[tracking-setup-completa-2026-06-23]] | ✅ 100% live |
| **WhatsApp CTWA** | [[ctwa-sistema-100-operacional-2026-06-29]] | ✅ Operacional |
| **UTM Tracking** | [[utm-tracking-avance-general]] | ✅ Landing OK, ads pendiente |
| **fbclid Capture** | [[fbclid-home-implementacion-exitosa-2026-06-22]] | ✅ /home live |
| **CAPI Filtering** | [[filtro-capi-submitapplication-2026-06-22]] | ✅ Bloqueando fantasmas |
| **Schema.org** | [[schema-arquitectura-logica-no-tocar]] | ✅ 4 sedes, 0 errores |
| **Landings CRO** | [[actualizacion-home-cro-2026-06-23]] | ✅ Ready |
| **GHL Integration** | [[flujo-crm-qikify-verificado-2026-06-29]] | ✅ E2E OK |

### Plataformas & Canales
| Plataforma | Guía | Estado |
|-----------|------|--------|
| **Meta Ads** | [[meta-mcp-guia]] | ✅ 6 cuentas live |
| **Google Ads** | [[google-ads-guia]] | 🔴 Score 26/100, auditoría lista |
| **Blog Shopify** | [[estandar-maestro-blogs-innovart]] | ✅ Template perfecta |
| **GHL (CRM)** | [[MEMORY#CRM-y-leads]] | ✅ Workflows activos |
| **WhatsApp API** | [[lineas-innovart-sms-whatsapp-api-estructura]] | ✅ 5 líneas por sede |
| **Telegram Bot** | [[bot-telegram-meta-ads]] | ✅ Working |

### Auditorías Recientes
| Auditoría | Fecha | Hallazgos | Impacto |
|-----------|-------|-----------|---------|
| **Meta 4 Ciudades** | 2026-06-24 | Bogotá -6 pixels fantasma, Barranquilla landing rota, Medellín CAPI ciego | $7-12K/mes si fijo |
| **Google Ads** | 2026-06-26 | Score 26/100, conversion tracking $0, cero negativos, Target CPA ficticio | Top priority |
| **fbclid Critical** | 2026-06-22 | 0 contactos con fbclid (600+ eventos/mes perdidos) | FIXED ✅ |
| **Show Rate 43%** | 2026-06-24 | EMQ 4.9 (falta email), reminders en draft, bot desacoplado | Roadmap 4 semanas |
| **Landing Clarity** | 2026-06-18 | Bounce 98%, scroll 14%, video 605 MB autoarranca | HOME5 v12 fixing |

---

## Troubleshooting Guide

### Problema: "Publiqué en 7 plataformas pero LinkedIn no sale"

**Diagnóstico:**
1. ¿LinkedIn fue marcado como "skip" en YAML? → Check `platforms.linkedin.enabled: true`
2. ¿Token de LinkedIn expiró? → OAuth reauth requerido
3. ¿Es un hilo o un articulo? → Verifica `type: article` vs `type: post`
4. ¿El post está en pending? → LinkedIn drafts requieren aprobación manual

**Solución:**
```bash
/distribucion debug linkedin-failed-2026-06-30.yaml
# Genera reporte detallado de por qué falló
# Si es token: /distribucion auth linkedin-refresh
# Si es pendiente: ve a LinkedIn Creator Studio y publica manual
```

---

### Problema: "El formulario GHL no captura leads"

**Diagnóstico:**
1. ¿Script Qikify está inyectado? → Busca `<div contactform-embed>` en tema
2. ¿El formulario tiene campo de email? → Sin email, EMQ baja
3. ¿El webhook GHL está activo? → Verifica en Settings → Webhooks
4. ¿Hay un router asignado? → Sin router, leads se pierden

**Solución:**
```
Referencia: [[paso-a-paso-arreglo-formularios-2026-06-30]]
Checklist de 4 pasos (10 minutos)
```

---

### Problema: "UTMs no se aplican automáticamente a los 166 ads"

**Diagnóstico:**
- UTM batch está en `pending_import`
- Meta API requiere recrear creativos (borra `standard_enhancements`)
- Método: API `url_tags` en ad_id

**Solución:**
```
Referencia: [[metodo-carga-utms-api-meta]]
Script Python: /tmp/apply_utms.py
1ª carga: 5 ads web completada 2026-06-18
Pendiente: 161 ads en 3 campañas
```

---

### Problema: "Show rate sigue en 43%, no sube a 55%"

**Diagnóstico:**
- EMQ 4.9 (debería ser 6+) → falta email en leads
- Reminders workflow están en DRAFT (no disparan)
- Avatar-bot desacoplado de GHL

**Solución:**
```
Roadmap 4 semanas: https://obsidian-path/bloqueantes-show-rate-43percent-junio2026
Fase 1 (semana 1): Activar reminders + captura email WhatsApp
Fase 2-4: Avatar bot, optimización Schedule
```

---

### Problema: "¿Por qué mi creativo da 8 CPC pero el de otra ciudad 3 CPC?"

**Diagnóstico:**
- Audiencias NO están separadas por ciudad (targeting global)
- Ofertas compiten entre ciudades (CBO imposible con monedas mixtas)
- Creativo puede ser irrelevante para algún mercado

**Solución:**
```
REGLA: Crear ad sets separados por ciudad (mesmo creativo, diferente targeting)
No hacer CBO entre cuentas diferentes (BGTA, MEDELLIN, etc.)
Si comparten presupuesto, hacerlo SÍ dentro de la misma cuenta
Referencia: [[auditoria-meta-4-ciudades-junio2026]]
```

---

### Problema: "Wikipedia rechazó mi envío de sección"

**Diagnóstico:**
- Tono no es neutral (demasiado comercial)
- Referencias no son académicas (blogs ≠ ciencia)
- Ya existe sección sobre el tema

**Solución:**
```
1. Reescribir en voz pasiva, sin "nuestra clínica"
2. Reemplazar referencias blog con PubMed/NIH
3. Buscar si sección existe; si sí, proponer en Discussion tab
4. Wikipedia moderadores responden en 48-72 horas
```

---

### Problema: "El batch publicó pero no tengo reporte de ROI"

**Diagnóstico:**
- Reporte automático está en delay (max 24 horas)
- Algunas plataformas no tienen API de analytics
- UTMs no fueron inyectados → tracking desacoplado

**Solución:**
```bash
/distribucion batch-report campana-xxx.yaml --force

# Si sigue sin datos:
/distribucion analytics-manual youtube linkedin shopify
# Genera tabla manual en 5 minutos
```

---

## Links a Documentación Oficial

### Claude Code & MCP
- **Claude API Docs:** https://docs.anthropic.com/
- **MCP Specification:** https://spec.modelcontextprotocol.io/
- **Claude Code Skills:** https://github.com/anthropics/claudecode-skills

### Integraciones de Plataformas
| Plataforma | API Docs | Status | Notes |
|------------|----------|--------|-------|
| **YouTube Data API v3** | https://developers.google.com/youtube/v3 | ✅ Ready | OAuth setup required |
| **LinkedIn API** | https://docs.microsoft.com/linkedin/shared/api-reference/api-reference | ✅ Ready | Enterprise scopes needed |
| **Reddit API** | https://www.reddit.com/dev/api/ | ✅ Ready | PRAW library installed |
| **Wikipedia API** | https://www.mediawiki.org/wiki/API/en | ✅ Ready | Edit token required |
| **Meta Graph API** | https://developers.facebook.com/docs/graph-api | ✅ Ready | 6 cuentas connected |
| **Shopify REST API** | https://shopify.dev/api/admin-rest | ✅ Ready | Custom app created |
| **GHL API** | https://developer.gohighlevel.com/ | ✅ Ready | MCP client active |

### Librerías Python Usadas
```python
# Core
anthropic==0.45.0  # Claude API
google-auth==2.35.0  # Google OAuth
google-auth-oauthlib==1.2.0  # YouTube
python-linkedin==0.2.0  # LinkedIn (fallback)
praw==7.7.1  # Reddit
mwclient==0.11.0  # Wikipedia
shopify==14.0.0  # Shopify
requests==2.32.0  # HTTP requests

# Media
ffmpeg-python==0.2.1  # Video processing
pillow==11.0.0  # Image manipulation
pydub==0.25.1  # Audio processing

# Data & Analytics
pandas==2.2.0  # Data frames
sqlalchemy==2.0.23  # Database ORM
```

---

## Roadmap de Desarrollo (En Progreso)

### Fase Actual: **Análisis de Viabilidad** ✅ COMPLETADO
- ✅ APIs disponibles para todas las plataformas
- ✅ Arquitectura 6 fases diseñada
- ✅ Estimación: 2-3 semanas part-time

### Próxima Fase: **Desarrollo MVP** (Roadmap 2-3 semanas)

**Semana 1:** Scaffolding + ingesta
- Skill structure (`~/.claude/skills/distribucion-multiplataforma/`)
- Monitoring de carpetas `/Distribución/Input/`
- Parsing de `.md`, `.mp4`, `.pdf`

**Semana 2:** Análisis + generación
- Claude análisis automático (tema, audiencia, keywords)
- Templates Jinja2 por plataforma
- Generación paralela (7 variaciones)

**Semana 3:** Publicación + reporting
- APIs integradas (YouTube, LinkedIn, Reddit, Wikipedia, Shopify, GHL)
- Preaprobación checklist
- Logging automático + alertas

**Semana 4+:** Optimización iterativa
- Analytics agregado (views, clicks, leads por plataforma)
- Feedback loop (qué contenido funciona mejor)
- Auto-optimizaciones (ajustes mínimos sin Javier)

---

## Iniciar Ahora

### Para Javier (Go/No-Go Decision)

```bash
# 1. Revisar arquitectura
cat /Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/distribucion-multiplataforma/ARQUITECTURA.md

# 2. Estimar esfuerzo real (15 minutos)
/distribucion estimate-effort

# 3. Si es OK, iniciar desarrollo
/distribucion init --project innovart-distribucion --timeline 2-3w part-time
```

### Para Community Manager (Usar Ahora — Beta)

```bash
# 1. Crear primer blog
/distribucion upload-blog mi-primer-articulo.md

# 2. Ver preview antes de publicar
/distribucion preview mi-primer-articulo.yaml

# 3. Publicar cuando esté listo
/distribucion publish campana-1.yaml
```

### Para Desarrollador (Contribuir al Código)

Referencia: [[ARQUITECTURA|distribucion-multiplataforma/ARQUITECTURA.md]]

---

## Contacto & Soporte

| Pregunta | Canal | Response SLA |
|----------|-------|--------------|
| Bloqueos técnicos | Obsidian + Javier directo | <2 horas |
| Preguntas de uso | [[TROUBLESHOOTING]] (primero) | -  |
| Bugs API | GitHub issues (privado) | <24 horas |
| Roadmap/feature request | Javier + roadmap board | Semanal review |

---

## Licencia & Confidencialidad

- **Propiedad intelectual:** Innovart Medical IPS
- **Período de desarrollo:** 2026 (confidencial)
- **Acceso:** Solo Javier, Community Manager, desarrolladores autorizados
- **Retención:** Indefinida (parte del stack estratégico)

---

**Última actualización:** 30 de junio de 2026 — Javier Forero  
**Siguiente revisión:** 31 de julio de 2026 (post-MVP)

