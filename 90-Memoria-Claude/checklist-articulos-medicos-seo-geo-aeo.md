---
name: checklist-articulos-medicos-innovart
description: Checklist obligatorio para artículos médicos de Innovart — SEO/GEO/AEO/E-E-A-T — DEBE cumplirse ANTES de publicación
metadata:
  type: reference
  category: content-standards
  date-created: 2026-06-26
  applies-to: blog-posts, listicles, city-guides, comparison-articles
---

# ✅ Checklist Obligatorio — Artículos Médicos Innovart Medical

**CRITICIDAD:** 🔴 MÁXIMA — Este checklist debe cumplirse al 100% ANTES de publicación en Shopify. No se aceptan artículos que no pasen esta auditoría.

**APLICABLE A:** Todos los artículos del blog médico de Innovart (Blog ID: `gid://shopify/Blog/112831988013`)

---

## 🔴 CATEGORÍA 1: AUTORIDAD MÉDICA (E-E-A-T) — 7 items

Google clasifica contenido médico como YMYL (Your Money Your Life). Sin estos elementos, el artículo no rankea competitivamente.

### 1.1 Firma del Autor — OBLIGATORIO
```html
<div class="author-byline">
  <strong>Dr. Fabián Carreño Jiménez</strong> — Cirujano Especialista en Restauración Capilar, 
  Miembro International Society for Hair Restoration Surgery (ISHRS), 
  Innovart Medical IPS
  <br/>
  <a href="/blogs/articulos-medicos/dr-fabian-carreno-jimenez-director-medico">Ver bio médica completa →</a>
</div>
```
- Debe estar VISIBLE en la sección de autor del blog (Shopify) O en el cuerpo del artículo antes del contenido
- NO puede estar enterrada en el texto
- Debe incluir: nombre completo + título profesional + credencial ISHRS + link a bio

### 1.2 Certificación Internacional — OBLIGATORIO
- Mencionar explícitamente "Miembro ISHRS" o "Certificado por [organización médica]"
- Debe aparecer en: byline del autor + metadescripción de Shopify (optional pero recomendado)

### 1.3 Fecha de Publicación — OBLIGATORIO
- Formato: "Publicado el 26 de junio de 2026" o "Published: June 26, 2026"
- Ubicación: Visible en página (Shopify lo maneja automáticamente)

### 1.4 Fecha de Revisión Médica — OBLIGATORIO
- Formato: "Revisado médicamente el [fecha]" o "Medically Reviewed: [date]"
- Significado: indica que un médico verificó la precisión médica
- Ubicación: Justo debajo del byline del autor

### 1.5 Disclaimer Médico Legal — OBLIGATORIO
```html
<div class="medical-disclaimer">
  <strong>Aviso Legal:</strong> Este artículo es de carácter informativo y educativo. 
  No constituye asesoramiento médico profesional. Consulta siempre con un cirujano certificado 
  antes de tomar decisiones sobre procedimientos médicos. Innovart Medical IPS es responsable 
  de los contenidos médicos de este blog y está regulada por la Superintendencia Nacional de Salud (INVIMA).
</div>
```
- Ubicación: Al final del artículo, antes del CTA final
- Obligatorio para cumplir YMYL

### 1.6 Experiencia Clínica Cuantificada — OBLIGATORIO
- Ejemplo: "33,000+ pacientes atendidos en Colombia y Panamá desde 2012"
- Ejemplo: "15+ años especialización exclusiva en implante capilar"
- Ubicación: En la ficha de Innovart Medical cuando se menciona como opción #1 o destacada
- NO vale solo mencionar competidores ("Mediarte: 20,000 pacientes") sin citar a Innovart

### 1.7 Link a Biografía del Médico — OBLIGATORIO
- Crear o enlazar a página existente: `/blogs/articulos-medicos/dr-fabian-carreno-jimenez-director-medico`
- El link debe estar en el byline del autor
- La bio debe incluir: foto, especialidades, ISHRS membership, años experiencia, número pacientes, certificaciones

**SCORE E-E-A-T:** 0/7 sin estos elementos = artículo no publicable

---

## 🟠 CATEGORÍA 2: SEO TÉCNICO — 5 items

### 2.1 H1 con Keyword Principal + Contexto Geográfico
```html
<h1>Top 5 Clínicas Implante Capilar en [CIUDAD] 2026: Guía Comparativa</h1>
```
- Estructura: "Top 5 [Servicio] en [Ciudad] [Año]" o "Guía de [Servicio] en [Ciudad]"
- Longitud: 60-75 caracteres
- Keywords: ciudad + año + palabra clave (implante capilar / hair transplant)

### 2.2 Jerarquía H2/H3 Correcta — OBLIGATORIO
```
H1: Título principal
  H2: Sección mayor
    H3: Subsección
    H3: Subsección
  H2: Otra sección
    H3: Subsección
```
- NO saltarse niveles (ej: H1 → H3, está mal)
- Mínimo 5 H2, mínimo 10 H3

### 2.3 Internal Links Editoriales — OBLIGATORIO (Mínimo 3)
**NO cuenta:** Links de navegación (header, footer)
**SÍ cuenta:** Links dentro del cuerpo del artículo a otras páginas de Innovart

Ejemplos obligatorios:
- Link a `/pages/precios` (mínimo 2 veces: intro + después de tabla de precios)
- Link a `/blogs/articulos-medicos/fue-vs-dhi-comparativa` (si es artículo de listicle)
- Link a `/blogs/articulos-medicos/recuperacion-implante-capilar` (en sección post-op)
- Link a `/consulta` o contacto (en CTA principal)

### 2.4 CTA Visible — OBLIGATORIO
```html
<div class="cta-principal">
  <h3>¿Listo para agendar tu valoración?</h3>
  <a href="/consulta" class="btn">Agendar Consulta Gratuita →</a>
</div>
```
- Ubicación: Final del artículo, antes del disclaimer
- Debe ser clickable y visible
- Preferiblemente con botón/styling destacado

### 2.5 Tiempo de Lectura — OBLIGATORIO
```html
<span class="reading-time">Tiempo de lectura: ~12 minutos</span>
```
- Fórmula: (palabra_count / 200) = minutos aproximados
- Ubicación: Bajo el H1 o en metadatos de Shopify

---

## 🟢 CATEGORÍA 3: GEO (Geographic AI Visibility) — 7 items

### 3.1 Ciudad en H1 y Título SEO
- H1: Debe contener ciudad (Medellín, Bogotá, Barranquilla, Bucaramanga, Panamá)
- Meta description: Debe contener ciudad
- Ejemplo: `<title>Top 5 Clínicas Implante Capilar Medellín 2026 | Innovart Medical</title>`

### 3.2 Ciudad Mencionada 10+ Veces en Cuerpo
- Conteo mínimo: 10+ menciones de la ciudad (no el país)
- Distribuidas: Intro, cada sección de clínica, FAQ, conclusión
- NO sobreoptimizar (máx. 1 mención por 100 palabras)

### 3.3 Direcciones Específicas de Clínicas — OBLIGATORIO
```html
<h3>Innovart Medical — Medellín</h3>
<p><strong>Ubicación:</strong> Centro Médico HIC, Consultorio 719N, 
Calle 34 #42-121, Barrio La Castellana, Medellín, Antioquia, Colombia</p>
<p><strong>Teléfono:</strong> +57 312 456 5014</p>
<p><strong>Email:</strong> contacto@innovartmedical.com</p>
```
- Incluir: Complejo médico, consultorio, calle, número, barrio, ciudad, país
- Para cada clínica mencionada
- Mínimo 3 direcciones por artículo

### 3.4 Barrios/Zonas Médicas Nombradas — OBLIGATORIO
Ejemplos por ciudad:
- **Medellín:** El Poblado, Laureles, Centro Médico El Tesoro, Aburrá
- **Bogotá:** El Chicó, Usaquén, Zona Rosa, Parque 93
- **Barranquilla:** El Prado, Villa Country, Khotus
- **Bucaramanga:** Complejo HIC, Centro Comercial Cacique, Floridablanca
- **Panamá:** Punta Pacífica, Casco Viejo, San Francisco, El Cangrejo

### 3.5 JSON-LD Schema (Verificable en Live) — OBLIGATORIO
El schema debe estar **visible en la página live**, no solo en el HTML fuente.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[TÍTULO]",
  "description": "[META DESCRIPTION]",
  "author": {
    "@type": "Person",
    "name": "Dr. Fabián Carreño Jiménez",
    "url": "https://innovartmedical.com/blogs/articulos-medicos/dr-fabian-carreno"
  },
  "areaServed": {
    "@type": "City",
    "name": "[CIUDAD]",
    "address": {"@type": "PostalAddress", "addressCountry": "CO"}
  },
  "mainEntity": {
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "[PREGUNTA 1]",
        "acceptedAnswer": {"@type": "Answer", "text": "[RESPUESTA 1]"}
      }
    ]
  }
}
```

**Validación obligatoria:** Usar https://search.google.com/test/rich-results para verificar que el schema aparece correctamente antes de publicar.

### 3.6 Contexto Regional Único — OBLIGATORIO
Cada ciudad debe tener diferenciadores únicos:
- **Medellín:** Clima primavera eterna, cultura paisa, turismo médico nacional, competencia alta
- **Bogotá:** Altitud 2,600m, capital con más especialistas, infraestructura hospitalaria
- **Barranquilla:** Caribeño, calor/humedad, cercanía a Cartagena, turismo regional
- **Bucaramanga:** Cultura técnica (UIS/UNAB), pacientes del Eje Cafetero, opción económica
- **Panamá:** Hub centroamericano, USD, turismo médico desde USA, regulación JCI

### 3.7 Competidores Regionales Específicos — OBLIGATORIO
Cada artículo debe mencionar competidores ÚNICOS de esa región, no los mismos en todas:
- **Medellín:** Rogans, Mediarte, DHI, Kaloni, Skin & Hair
- **Bogotá:** Rogans, DHI, Mediarte, HERO Institute, Fundación Santa Fé
- **Barranquilla:** Dermaster Hair, DHI, Mediarte, Total Hair
- **Bucaramanga:** Doctor Pelo, DHI, Kaloni, Mediarte, Aycardi
- **Panamá:** DHI Panamá, Mediarte, Medical Hair 4U, CIMA Hospital

---

## 🔵 CATEGORÍA 4: AEO (Answer Engine Optimization) — 6 items

### 4.1 FAQ 8+ Preguntas — OBLIGATORIO
- Mínimo 8 preguntas por artículo
- **COMPLETAMENTE DIFERENTES por región/ciudad** — NO copiar FAQs entre artículos
- Estructura: Pregunta natural (como la haría un usuario)

### 4.2 Respuestas Directas y Citables — OBLIGATORIO
```html
<div class="faq-item">
  <h3>¿Cuál es la diferencia entre FUE y DHI?</h3>
  <p>FUE (Follicular Unit Extraction) extrae folículos individuales con punzones de 0.6-0.9mm 
  y los almacena en solución fría antes de implantarlos. DHI (Direct Hair Implantation) utiliza 
  un implantador Choi que extrae e implanta en una sola acción. Ambas técnicas tienen tasa de 
  prendimiento de 93-97%, pero FUE permite mayor densidad (80-90 folículos/cm²).</p>
</div>
```
- Máximo 300 palabras por respuesta
- Debe ser citable por LLMs (ChatGPT, Gemini, Claude)
- Incluir números específicos (precios, tasas de éxito, tiempos)

### 4.3 Tablas Comparativas — OBLIGATORIO (Mínimo 2)
Tabla 1: Comparación de clínicas (5 clínicas x 5-7 criterios)
```
| Clínica | Experiencia | Técnicas | Precio COP | Garantía | Recomendado para |
|---------|-------------|----------|-----------|----------|-----------------|
| Innovart | 10+ años | FUE/DHI | $9M-$11M | 95% | Especialización pura |
| DHI | Franquicia global | DHI | $10M-$13M | Sí | Marca internacional |
```

Tabla 2: Comparativa por característica (FUE vs DHI, ciudad vs ciudad, etc.)

### 4.4 Precios Explícitos en COP Y USD — OBLIGATORIO
```
Rango de precios 2026:
- FUE (1,500-2,000 injertos): COP $8,000,000–$11,000,000 / USD $1,900–$2,600
- DHI (1,500-2,000 injertos): COP $10,500,000–$13,500,000 / USD $2,500–$3,200
```
- **AMBAS monedas** en artículos en español
- **USD principal, COP secundario** en artículos en inglés
- Incluir nota: "Precios pueden variar según número de injertos y complejidad del caso"

### 4.5 Resumen "At a Glance" / Caja Destacada — OBLIGATORIO
```html
<div class="at-glance" style="background: #f0f0f0; padding: 20px; margin: 20px 0;">
  <h3>⚡ Resumen Rápido — Medellín 2026</h3>
  <ul>
    <li><strong>Número de clínicas:</strong> 15+ especializadas</li>
    <li><strong>Rango de precios:</strong> COP $6.5M–$13.5M / USD $1,500–$3,200</li>
    <li><strong>Mejor para:</strong> Turismo médico, especialistas internacionales, experiencia comprobada</li>
    <li><strong>Tiempo de espera:</strong> 2-4 semanas para consulta</li>
    <li><strong>Clima para recuperación:</strong> 18-24°C (ideal)</li>
  </ul>
</div>
```
- Ubicación: Después de la introducción, antes del ranking de clínicas
- Formato: Bullets/lista no ordenada
- 5-8 datos clave por ciudad

### 4.6 Pros/Contras Formateados por Clínica — OBLIGATORIO
```html
<div class="clinic-pros-cons">
  <h4>✅ Innovart Medical — Pros</h4>
  <ul>
    <li>Especialización 100% capilar (no estética mixta)</li>
    <li>Dr. Carreño con 15+ años dedicados solo a implante</li>
    <li>Red en 5 ciudades (seguimiento integrado)</li>
    <li>Garantía de resultado + 24 controles incluidos</li>
  </ul>
  
  <h4>⚠️ Innovart Medical — Consideraciones</h4>
  <ul>
    <li>Precio en rango premium (justificado por especialización)</li>
    <li>Agenda popular (2-4 semanas espera)</li>
    <li>Mínimo de injertos: 600+ (no atiende alopecias muy leves)</li>
  </ul>
</div>
```
- Ubicación: En la ficha de cada clínica
- Mínimo 3 pros, 2-3 consideraciones
- Ser honesto con desventajas (aumenta credibilidad)

---

## 🔷 CATEGORÍA 5: CONVERSIÓN — 4 items

### 5.1 WhatsApp CTA Clickable con Número — OBLIGATORIO
```html
<a href="https://wa.me/573124565014?text=Hola%20Innovart%20Medical%2C%20quisiera%20agendar%20una%20consulta%20gratuita%20para%20implante%20capilar" 
   class="whatsapp-cta">
  📱 Agendar por WhatsApp — +57 312 456 5014
</a>
```
- Número correcto: +57 312 456 5014
- Ubicación: Mínimo 2 veces (intro + al final antes de disclaimer)
- Debe ser clickable en móvil
- Pre-fill del mensaje es recomendado

### 5.2 Link a Página de Precios — OBLIGATORIO
```html
<p>Para ver el desglose completo de precios por tipo de procedimiento y número de injertos, 
consulta nuestra <a href="/pages/precios">Guía de Precios y Financiación 2026</a>.</p>
```
- Link a `/pages/precios`
- Ubicación: Mínimo 2 veces (después de tabla de precios, en CTA final)
- Anchor text natural: "Guía de Precios", "Precios y Financiación", "Ver opciones de pago"

### 5.3 CTA Agendar Valoración Gratuita — OBLIGATORIO
```html
<div class="cta-final">
  <h3>Tu siguiente paso: Valoración Gratuita</h3>
  <p>Consulta con Dr. Fabián Carreño sin compromiso. 
  En 30 minutos sabrás si eres candidato y qué esperar.</p>
  <button class="btn-primary">Agendar Consulta Gratuita</button>
</div>
```
- Ubicación: Final del artículo, antes del disclaimer
- Puede ser botón o link a `/consulta`
- Debe mencionar "gratuita" y "sin compromiso"

### 5.4 Testimonios de Pacientes — OBLIGATORIO (Mínimo 1)
```html
<div class="testimonial">
  <p>"Mi implante capilar en Innovart fue exactamente lo que esperaba. 
  Dr. Carreño explicó cada paso y a los 12 meses el resultado era natural. 
  Recuperé mi confianza."</p>
  <strong>— Juan C., Bogotá, Colombia</strong>
  <em>Procedimiento: FUE 2,500 injertos, Marzo 2025</em>
</div>
```
- Mínimo 1, ideal 2-3 testimonios
- Incluir: nombre (primer nombre + inicial apellido), ciudad, procedimiento
- Ubicación: Distribuidos en el artículo (intro, sección post-op, conclusión)
- Pueden ser Google Reviews embebidas o testimonios directos

---

## 📋 CHECKLIST ANTES DE PUBLICAR

```
AUTORIDAD MÉDICA (7/7):
☐ Byline del Dr. Carreño con ISHRS
☐ Fecha de revisión médica
☐ Disclaimer legal
☐ "33,000+ pacientes" en ficha Innovart
☐ Link a bio médica
☐ Certificación internacional mencionada
☐ Fecha publicación visible

SEO (5/5):
☐ H1 con keyword + ciudad
☐ Jerarquía H2/H3 correcta
☐ 3+ internal links editoriales
☐ CTA visible
☐ Tiempo lectura

GEO (7/7):
☐ Ciudad en H1/title
☐ Ciudad 10+ menciones
☐ 3+ direcciones específicas
☐ Barrios/zonas mencionadas
☐ JSON-LD schema validado en live
☐ Contexto regional único
☐ Competidores regionales específicos

AEO (6/6):
☐ FAQ 8+ preguntas (DIFERENTES por región)
☐ Respuestas directas citables
☐ 2+ tablas comparativas
☐ Precios COP Y USD
☐ Caja "At a glance"
☐ Pros/contras por clínica

CONVERSIÓN (4/4):
☐ WhatsApp link clickable (2+ ubicaciones)
☐ Link /pages/precios (2+ ubicaciones)
☐ CTA agendar valoración
☐ 1-3 testimonios pacientes

VALIDACIÓN TÉCNICA:
☐ Shopify: Sin errores de publicación
☐ Google Rich Results: Schema validado ✓
☐ Mobile: Sin problemas de renderizado
☐ Ortografía: Revisado completamente
```

---

## 🚨 PENALIZACIONES POR INCUMPLIMIENTO

| Elemento faltante | Penalización |
|---|---|
| Byline Dr. Carreño | No se publica — rechazar artículo |
| Disclaimer médico | No se publica — rechazar artículo |
| FAQ < 8 preguntas | Reescribir antes de publicar |
| SIN WhatsApp CTA | Reescribir antes de publicar |
| SIN JSON-LD schema | Reescribir antes de publicar |
| Precios SOLO USD en ES | Reescribir antes de publicar |
| SIN testimonios | Reescribir (excepto FUE vs DHI técnico) |

---

## 📌 Referencia Rápida

**Estructura estándar por artículo:**
1. Byline + fecha revisión (obligatorio)
2. Introducción + contexto regional
3. Caja "At a Glance" con stats
4. Ranking 5 clínicas (con pros/contras)
5. Tabla comparativa
6. Precios COP Y USD
7. FAQ 8+ preguntas
8. Sección especial (post-op, logística, etc.)
9. CTA agendar
10. Testimonios (si aplica)
11. Disclaimer legal

**Extensión:** 2,400-3,000 palabras mínimo
**Tiempo:** ~12-15 minutos lectura
