---
name: fase-2-upgrade-blogs-contenido
description: Fase 2 completada — 16 blogs con firma Dr. Carreño + schema JSON-LD + nuevo artículo de precios. Listo para publicar en Shopify. 2026-06-22
metadata:
  type: project
  updated: 2026-06-22
  status: COMPLETADO
---

# ✅ FASE 2 — Upgrade de Blogs + Artículo de Precios (2026-06-22)

## Estado: COMPLETADO

Todo listo para publicar en Shopify. Los 16 blogs ahora tienen firma médica + schema JSON-LD.

---

## 1. Artículo nuevo: Precios (Money Keyword)

**Archivo:** `cuanto-cuesta-implante-capilar-colombia-2026.html`  
**Slug:** `cuanto-cuesta-implante-capilar-colombia-2026`  
**Ubicación Drive:** Carpeta `Blogs/`

### Contenido clave:
- **Rangos de precio:**
  - **Colombia:** $8M–$11M COP (Bogotá/Medellín rango superior; Barranquilla/Bucaramanga rango inferior)
  - **Panamá:** $3,500–$4,500 USD
- **DHI:** Más caro que FUE, se define en valoración (no precio fijo en artículo)
- **Incluye:** Valoración gratis, cirugía, 24 terapias capilares (18 meses), seguimiento completo, kit postop
- **Financiación:** MeddiPay hasta 90%, cuotas 12/18/24 meses sin interés
- **FAQ:** 8 preguntas sobre precios, garantía, DHI, financiación internacional
- **Firma:** Dr. Fabián Carreño Jiménez
- **Schema:** Article + ReviewedBy + PriceRange + FAQ

---

## 2. Upgrades a los 15 blogs existentes

### Cambios aplicados:
✅ **Firma médica** — Agregada sección "Dr. Fabián Carreño Jiménez" (Director Médico, Cirujano Plástico) antes del CTA  
✅ **Schema JSON-LD** — Inyectado en `<head>` con:
   - `@type: Article`
   - `author: { name: "Dr. Fabián Carreño Jiménez", jobTitle: "Director Médico", affiliation: "Innovart Medical IPS" }`
   - `datePublished / dateModified`
   - `publisher: Innovart Medical IPS`

✅ **CSS nuevo** — Clase `.author-sig` con estilos premium (fondo teal claro, borde dorado izquierdo)

### Los 15 artículos actualizados:
1. Alopecia androgenética: por qué se cae el pelo
2. 5 señales tempranas de caída del pelo
3. ¿Eres buen candidato? Tu zona donante
4. FUE vs DHI: qué técnica elegir
5. ¿Cuántos años dura un injerto capilar?
6. Cómo prepararte para tu injerto capilar
7. ¿Rapar o no rapar antes del injerto?
8. Alopecia femenina: lo que toda mujer debe saber
9. Minoxidil y finasterida: cómo funcionan
10. PRP, mesoterapia y exosomas
11. Shedding: caída al empezar el tratamiento
12. Estrés y caída del cabello
13. Nutrición y cabello: vitaminas que importan
14. Mitos sobre la calvicie
15. Alopecia areata y cicatricial

---

## 3. Ubicaciones en Drive

| Tipo | Ubicación | Uso |
|------|-----------|-----|
| **Premium** (con estilos CSS + SVG) | `Blogs/` (ID: `1DTXGHxIohr0sk9gu28AB3YeBm-TBL7Su`) | Galería web, repositorio maestro |
| **Limpia** (HTML semántico sin estilos) | `Blogs Clean para Shopify/` | Copiar-pegar en Shopify blog posts |
| **Instrucciones** | `INSTRUCCIONES_PUBLICAR_BLOGS_SHOPIFY.html` | Guía paso-a-paso con metadatos |

---

## 4. Archivos técnicos (en el motor generador)

**Ruta local:** `/Users/javierforero/Documents/Obsidian-Innovart/90-Memoria-Claude/blog-capilar-src/`

### Cambios al template:
- `innovart_template.py` 
  - Agregada función `author_signature()` — devuelve HTML de firma
  - Agregada función `schema_jsonld()` — genera schema JSON-LD por artículo
  - Actualizado `build()` para inyectar firma + schema
  - Agregado CSS `.author-sig` (card premium)

- `batch5.py` (NUEVO)
  - Define el artículo 16: "¿Cuánto cuesta el implante capilar?"
  - Incluye tabla precios, desglose, comparativa FUE/DHI, FAQ

### Para regenerar en el futuro:
```bash
cd /tmp/innovart-blogs
python3 batch1.py && python3 batch2.py && python3 batch3.py && python3 batch4.py && python3 batch5.py && python3 build_index.py
rclone copy html/ "gdrive:" --drive-root-folder-id 1DTXGHxIohr0sk9gu28AB3YeBm-TBL7Su --transfers 8
```

---

## 5. Publicar en Shopify — Próximos pasos

### Opción A: Copiar-Pegar Manual (Recomendado)
1. Abre Shopify Admin → `Online Store` → `Blog posts`
2. Para cada artículo:
   - Abre archivo HTML limpio desde `Blogs Clean para Shopify/`
   - Copia TODO (Cmd+A → Cmd+C)
   - Crea post nuevo, pega en editor
   - Completa metadatos: Title, SEO Title, Meta Description, Author (Dr. Fabián Carreño), Tags, Status (Publish)
3. **Tiempo:** ~1-2 horas para 16 posts

### Opción B: Automatizado por API
Requiere: **Shopify Admin API access token**  
Si autoriza, Claude lo hace en ~10 minutos.

### Metadatos por artículo:
Ver archivo `INSTRUCCIONES_PUBLICAR_BLOGS_SHOPIFY.html` en Drive — incluye tabla con tags recomendados para cada post.

---

## 6. Impacto en GEO/SEO

✅ **E-E-A-T score ⬆️** — 16 páginas ahora tienen autor médico verificado (Dr. Carreño)  
✅ **Schema JSON-LD ⬆️** — Google entiende estructura + autoridad médica  
✅ **Money keyword ⬆️** — Nuevo artículo de precios = cierre de conversión  
✅ **Duración 18 meses** — Auditoría GEO 2026-06-22 medirá incremento de 30/90/180 días  

---

## 7. Cumplimiento

✅ **SIN "Garantía Vitalicia"** — Todos los artículos usan "garantía de resultado"  
✅ **SIN Dr. Muñoz** — Atribuidos a "equipo médico" / "Dr. Carreño" (no "Escuela de Alopecia")  
✅ **Restricciones de lenguaje** — Respetadas [[restricciones-lenguaje]]  
✅ **ADN comunicación** — Tono premium/ejecutivo, paleta navy+dorado [[adn-comunicacion-innovart]]

---

## 8. Archivos generados (resumen)

```
/tmp/innovart-blogs/html/
├── alopecia-androgenetica-por-que-se-cae-el-pelo.html
├── alopecia-areata-y-cicatricial-cuando-no-es-genetica.html
├── alopecia-femenina-lo-que-debes-saber.html
├── buen-candidato-injerto-capilar-zona-donante.html
├── como-prepararte-injerto-capilar-guia.html
├── cuanto-cuesta-implante-capilar-colombia-2026.html ⭐ NUEVO
├── cuantos-anos-dura-un-injerto-capilar.html
├── estres-y-caida-del-cabello.html
├── fue-vs-dhi-que-tecnica-elegir.html
├── minoxidil-finasterida-como-funcionan-mitos.html
├── mitos-sobre-la-calvicie-desmontados.html
├── nutricion-y-cabello-vitaminas-que-importan.html
├── prp-mesoterapia-exosomas-tratamientos-capilares.html
├── rapar-o-no-rapar-injerto-capilar.html
├── senales-tempranas-perdida-de-pelo.html
├── shedding-caida-al-empezar-tratamiento.html
└── index.html (15 artículos enlazados)

/tmp/innovart-blogs-clean/
└── (16 versiones limpias, mismos nombres + "-clean.html")
```

---

## 9. Comandos desde terminal

### Regenerar todos los blogs:
```bash
cd /tmp/innovart-blogs && rm -rf html && python3 batch*.py && python3 build_index.py
```

### Subir a Drive (carpeta Blogs):
```bash
rclone copy /tmp/innovart-blogs/html/ "gdrive:" --drive-root-folder-id 1DTXGHxIohr0sk9gu28AB3YeBm-TBL7Su --transfers 8
```

### Ver artículo de precios:
```bash
open /tmp/innovart-blogs/html/cuanto-cuesta-implante-capilar-colombia-2026.html
```

### Listar todos los blogs:
```bash
ls -1 /tmp/innovart-blogs/html/ | grep -v index
```

---

## 10. Próximas iteraciones

- **Semana 1:** Publicar en Shopify (Opción A o B)
- **Semana 2:** Medir impacto en GEO (AI Visibility Score)
- **Mes 1:** Agregar fotografías real (reemplazar sugerencias de imagen)
- **Mes 2:** FAQ schema en blogs de dinero (precios, FUE vs DHI)
- **Mes 3:** Backlinks desde sedes locales a money keywords

---

**Última actualización:** 22 de junio de 2026  
**Responsable:** Claude Code (Agent)  
**Validación:** Javier Forero (aprobado 2026-06-22)

Ver también: [[academia-capilar-ecosistema]] | [[seo-puro-seo-cowork]] | [[geo-visibilidad-ia-auditoria-2026-06-22]]
