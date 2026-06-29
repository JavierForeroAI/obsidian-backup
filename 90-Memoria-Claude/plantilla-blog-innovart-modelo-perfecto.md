---
name: plantilla-blog-innovart-modelo-perfecto
description: Plantilla HTML completa y definitiva para artículos del blog de Innovart Medical — diseño, autoridad, enlaces internos, firma Dr., SEO/GEO/AEO. Usar SIEMPRE como base antes de publicar cualquier artículo nuevo.
metadata:
  type: reference
  category: content-templates
  date-created: 2026-06-26
  status: DEFINITIVO — no modificar sin aprobación de Javier
---

# Plantilla Perfecta — Blog Innovart Medical IPS

> **REGLA ABSOLUTA:** Todo artículo publicado en `innovartmedical.com/blogs/articulos-medicos/` DEBE seguir esta plantilla al 100% antes de publicarse. Sin excepciones.

---

## Por qué existe esta plantilla

Después de auditar 10+ artículos publicados se encontró que TODOS fallaban en:
- ❌ Sin byline visible del Dr. Fabián Carreño Jiménez
- ❌ Sin firma del Dr. al final
- ❌ Sin enlaces internos entre artículos (interlinking)
- ❌ Sin WhatsApp CTA clickable
- ❌ Sin caja "At a Glance" / "En resumen"
- ❌ Precios incorrectos o inconsistentes
- ❌ Diseño plano sin color ni estructura visual
- ❌ Datos de contacto de competidores incluidos (NO se debe hacer)
- ❌ Sin sedes al final

Resultado: horas de trabajo retroactivo. Esta plantilla evita repetirlo.

---

## Precios Oficiales 2026 (NO cambiar sin autorización)

| Sede | COP | USD |
|------|-----|-----|
| Colombia (Bogotá, Medellín, Barranquilla, Bucaramanga) | $8M–$11M COP | $1,900–$2,600 USD |
| Panamá | — | $3,500–$4,500 USD |

---

## Regla de Competidores

- ✅ Mencionar SOLO el nombre de la clínica competidora
- ❌ NUNCA incluir: dirección, teléfono, sitio web, coordenadas de competidores
- ✅ De Innovart Medical: incluir TODO (dirección, WhatsApp, Maps, teléfono)

---

## Estructura Obligatoria del Artículo

```
1. [BYLINE]           ← inmediatamente después del H1
2. [AT A GLANCE]      ← después del primer párrafo intro
3. [WHATSAPP CTA #1]  ← cerca del inicio (después del At a Glance)
4. [CONTENIDO]        ← H2/H3, tablas, FAQ — contenido técnico sin tocar
5. [WHATSAPP CTA #2]  ← cerca del final (antes de sedes)
6. [ARTÍCULOS RELACIONADOS] ← enlaces internos al blog
7. [SEDES]            ← con links Google Maps
8. [FIRMA DR.]        ← siempre al final
9. [DISCLAIMER]       ← después de la firma
```

---

## HTML Completo — Español (ES)

### 1. BYLINE (inmediatamente después del H1)
```html
<p style="font-size:14px;color:#6b7280;margin:0 0 24px 0;padding:12px;background:#f0fdf4;border-left:4px solid #10B981;">Por <strong style="color:#059669;">Dr. Fabián Carreño Jiménez</strong> — Especialista en Restauración Capilar | Miembro ISHRS | Actualizado: 26 de junio de 2026</p>
```

### 2. AT A GLANCE (después del primer párrafo)
```html
<div style="background:#f0fdf4;border-left:4px solid #10B981;padding:20px;margin:24px 0;border-radius:4px;">
<h3 style="color:#059669;margin-top:0;font-size:16px;">Implante Capilar en [CIUDAD] — Datos Clave</h3>
<ul style="margin:0;padding-left:20px;font-size:14px;line-height:1.8;">
<li><strong>Rango de precios:</strong> $8M–$11M COP / $1,900–$2,600 USD</li>
<li><strong>Duración del procedimiento:</strong> 6–8 horas</li>
<li><strong>Recuperación:</strong> 7–10 días para actividades normales</li>
<li><strong>Resultados visibles:</strong> 3–6 meses · Resultado final: 12 meses</li>
<li><strong>Satisfacción de pacientes:</strong> 95%+ en clínicas certificadas</li>
<li><strong>Innovart Medical:</strong> 33,000+ pacientes atendidos · 15+ años de especialización</li>
</ul>
</div>
```
> Para Panamá: cambiar precio a `$3,500–$4,500 USD` y omitir COP.

### 3. WHATSAPP CTA (usar 2 veces: inicio y final)
```html
<div style="text-align:center;margin:24px 0;">
<a href="https://wa.me/573124565014?text=Hola%20Innovart%2C%20quiero%20información%20sobre%20implante%20capilar%20en%20[CIUDAD]" style="display:inline-block;background:#25D366;color:white;padding:14px 28px;border-radius:4px;text-decoration:none;font-weight:700;font-size:15px;">Consulta Gratis por WhatsApp</a>
<p style="font-size:12px;color:#6b7280;margin:8px 0 0 0;">Financiación MeddiPay disponible — hasta el 90%</p>
</div>
```

### 4. LINK A PRECIOS (después de cualquier tabla de precios)
```html
<p style="font-size:14px;margin:12px 0;"><a href="/pages/precios" style="color:#10B981;font-weight:600;">Ver Guía Completa de Precios →</a></p>
```

### 5. ARTÍCULOS RELACIONADOS (antes de sedes — OBLIGATORIO para interlinking SEO)
```html
<div style="background:#f3f4f6;border-left:4px solid #10B981;padding:20px;margin:30px 0;border-radius:4px;">
<h3 style="color:#1f2937;margin-top:0;font-size:16px;">Artículos Relacionados</h3>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;">
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/fue-vs-dhi-comparativa-definitiva-colombia-2026" style="color:#10B981;">FUE vs DHI: Comparativa Definitiva para Colombia 2026</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/que-es-implante-capilar-fue" style="color:#10B981;">¿Qué es el Implante Capilar FUE? Guía Completa</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/top-5-clinicas-de-implante-capilar-en-medellin-2026-guia-comparativa-actualizada" style="color:#10B981;">Top 5 Clínicas de Implante Capilar en Medellín 2026</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/top-5-clinicas-de-implante-capilar-en-barranquilla-2026-guia-del-caribe-colombiano" style="color:#10B981;">Top 5 Clínicas de Implante Capilar en Barranquilla 2026</a></li>
<li style="padding:6px 0;">→ <a href="/pages/precios" style="color:#10B981;">Guía de Precios — Implante Capilar Colombia y Panamá 2026</a></li>
</ul>
</div>
```
> ⚠️ Omite el link al artículo actual (no se enlaza a sí mismo).

### 6. SEDES (antes de la firma)
```html
<div style="background:#f3f4f6;border-left:4px solid #10B981;padding:20px;margin:30px 0;border-radius:4px;">
<h3 style="color:#1f2937;margin-top:0;font-size:16px;">Sedes Innovart Medical IPS</h3>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;">
<li style="padding:6px 0;"><strong>Bogotá:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar/@4.6959114,-74.0353125,19z" style="color:#10B981;">Ver en Maps</a></li>
<li style="padding:6px 0;"><strong>Medellín:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar+Medell%C3%ADn/@6.222832,-75.5715959,17z" style="color:#10B981;">Ver en Maps</a></li>
<li style="padding:6px 0;"><strong>Barranquilla:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+_+Implante+capilar+Barranquilla/@11.006033,-74.805632,17z" style="color:#10B981;">Ver en Maps</a></li>
<li style="padding:6px 0;"><strong>Panamá:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Implante+capilar+Panam%C3%A1/@9.0155565,-79.4672434,17z" style="color:#10B981;">Ver en Maps</a></li>
<li style="padding:6px 0;"><strong>Bucaramanga:</strong> Próximamente</li>
</ul>
</div>
```

### 7. FIRMA DR. (SIEMPRE AL FINAL — no negociable)
```html
<hr style="margin:40px 0 20px 0;border:none;border-top:2px solid #e5e7eb;">
<div style="background:#f0fdf4;border-left:4px solid #10B981;padding:20px;border-radius:4px;">
<p style="font-size:18px;font-weight:700;margin:0 0 4px 0;color:#1f2937;">Dr. Fabián Carreño Jiménez</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">Cirujano Especialista en Restauración Capilar</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">Miembro ISHRS (International Society of Hair Restoration Surgery)</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">Director Médico — Innovart Medical IPS</p>
<p style="font-size:12px;color:#6b7280;margin:8px 0 0 0;">Bogotá · Medellín · Barranquilla · Panamá</p>
</div>
```

### 8. DISCLAIMER (después de la firma — obligatorio YMYL)
```html
<p style="font-size:11px;color:#9ca3af;text-align:center;margin:16px 0;">Aviso Legal: Este artículo es de carácter informativo y educativo. No constituye asesoramiento médico profesional. Consulta siempre con un cirujano certificado antes de tomar decisiones sobre procedimientos médicos. Innovart Medical IPS está regulada por la Superintendencia Nacional de Salud (INVIMA).</p>
```

---

## HTML Completo — Inglés (EN)

### 1. BYLINE
```html
<p style="font-size:14px;color:#6b7280;margin:0 0 24px 0;padding:12px;background:#f0fdf4;border-left:4px solid #10B981;">By <strong style="color:#059669;">Dr. Fabián Carreño Jiménez</strong> — Hair Restoration Specialist | ISHRS Member | Updated: June 26, 2026</p>
```

### 2. AT A GLANCE
```html
<div style="background:#f0fdf4;border-left:4px solid #10B981;padding:20px;margin:24px 0;border-radius:4px;">
<h3 style="color:#059669;margin-top:0;font-size:16px;">Key Facts — [CITY] Hair Transplant</h3>
<ul style="margin:0;padding-left:20px;font-size:14px;line-height:1.8;">
<li><strong>Price range:</strong> COP $8M–$11M / USD $1,900–$2,600</li>
<li><strong>Procedure duration:</strong> 6–8 hours</li>
<li><strong>Recovery:</strong> 7–10 days to normal activities</li>
<li><strong>Visible results:</strong> 3–6 months · Final result: 12 months</li>
<li><strong>Patient satisfaction:</strong> 95%+ at certified clinics</li>
<li><strong>Innovart Medical:</strong> 33,000+ patients · 15+ years specialization</li>
</ul>
</div>
```

### 3. WHATSAPP CTA
```html
<div style="text-align:center;margin:24px 0;">
<a href="https://wa.me/573124565014?text=Hello%20Innovart%2C%20I%20want%20information%20about%20hair%20transplant%20in%20[CITY]" style="display:inline-block;background:#25D366;color:white;padding:14px 28px;border-radius:4px;text-decoration:none;font-weight:700;font-size:15px;">Free Consultation on WhatsApp</a>
<p style="font-size:12px;color:#6b7280;margin:8px 0 0 0;">MeddiPay financing available — up to 90%</p>
</div>
```

### 4. ARTÍCULOS RELACIONADOS (EN)
```html
<div style="background:#f3f4f6;border-left:4px solid #10B981;padding:20px;margin:30px 0;border-radius:4px;">
<h3 style="color:#1f2937;margin-top:0;font-size:16px;">Related Articles</h3>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;">
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/fue-vs-dhi-the-definitive-comparison-for-hair-transplants" style="color:#10B981;">FUE vs DHI: The Definitive Comparison for Hair Transplants</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/colombia-hair-transplant-city-guide-2026-bogota-vs-medellin-vs-barranquilla-vs-bucaramanga-vs-panama-innovart-medical" style="color:#10B981;">Colombia Hair Transplant City Guide 2026</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/hair-transplant-bogota-2026" style="color:#10B981;">Top 5 Hair Transplant Clinics in Bogotá 2026</a></li>
<li style="padding:6px 0;">→ <a href="/blogs/articulos-medicos/top-5-hair-transplant-clinics-in-barranquilla-2026-caribbean-medical-tourism-guide" style="color:#10B981;">Top 5 Hair Transplant Clinics in Barranquilla 2026</a></li>
<li style="padding:6px 0;">→ <a href="/pages/precios" style="color:#10B981;">Pricing Guide — Hair Transplant Colombia &amp; Panama 2026</a></li>
</ul>
</div>
```

### 5. SEDES (EN)
```html
<div style="background:#f3f4f6;border-left:4px solid #10B981;padding:20px;margin:30px 0;border-radius:4px;">
<h3 style="color:#1f2937;margin-top:0;font-size:16px;">Innovart Medical IPS — Our Locations</h3>
<ul style="list-style:none;padding:0;margin:0;font-size:14px;">
<li style="padding:6px 0;"><strong>Bogotá:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar/@4.6959114,-74.0353125,19z" style="color:#10B981;">View on Maps</a></li>
<li style="padding:6px 0;"><strong>Medellín:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar+Medell%C3%ADn/@6.222832,-75.5715959,17z" style="color:#10B981;">View on Maps</a></li>
<li style="padding:6px 0;"><strong>Barranquilla:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Ips+_+Implante+capilar+Barranquilla/@11.006033,-74.805632,17z" style="color:#10B981;">View on Maps</a></li>
<li style="padding:6px 0;"><strong>Panamá:</strong> <a href="https://www.google.com/maps/place/Innovart+Medical+Implante+capilar+Panam%C3%A1/@9.0155565,-79.4672434,17z" style="color:#10B981;">View on Maps</a></li>
</ul>
</div>
```

### 6. FIRMA DR. (EN)
```html
<hr style="margin:40px 0 20px 0;border:none;border-top:2px solid #e5e7eb;">
<div style="background:#f0fdf4;border-left:4px solid #10B981;padding:20px;border-radius:4px;">
<p style="font-size:18px;font-weight:700;margin:0 0 4px 0;color:#1f2937;">Dr. Fabián Carreño Jiménez</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">Hair Restoration Surgery Specialist</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">ISHRS Member (International Society of Hair Restoration Surgery)</p>
<p style="font-size:14px;color:#374151;margin:4px 0;">Medical Director — Innovart Medical IPS</p>
<p style="font-size:12px;color:#6b7280;margin:8px 0 0 0;">Bogotá · Medellín · Barranquilla · Panamá</p>
</div>
<p style="font-size:11px;color:#9ca3af;text-align:center;margin:16px 0;">This content is informational and does not constitute medical diagnosis. Consult a certified specialist before making decisions about hair transplant procedures. Innovart Medical IPS is regulated by INVIMA (Colombia) and health authorities in Panama.</p>
```

---

## Colores del sistema de diseño

| Elemento | Color | Uso |
|----------|-------|-----|
| Acento principal | `#10B981` | Bordes izquierdos, links, iconos |
| Verde texto | `#059669` | Nombre Dr., títulos de cajas |
| Fondo verde claro | `#f0fdf4` | Byline, At a Glance, firma Dr. |
| Fondo gris | `#f3f4f6` | Sedes, artículos relacionados |
| WhatsApp | `#25D366` | Solo botones WhatsApp |
| Texto principal | `#1f2937` | H1, H2, nombres |
| Texto secundario | `#374151` | Párrafos, specs del Dr. |
| Texto muted | `#6b7280` | Byline, metadatos, notas |
| Disclaimer | `#9ca3af` | Solo disclaimer legal |

---

## Checklist antes de publicar

```
□ Byline Dr. Carreño + ISHRS visible (inicio)
□ At a Glance / Datos Clave box presente
□ WhatsApp CTA x2 (inicio Y final) — número: +57 312 456 5014
□ Link a /pages/precios (mínimo 2 veces)
□ Precios correctos: Colombia $8M–$11M COP / $1,900–$2,600 USD
□ Precios Panamá: $3,500–$4,500 USD (solo USD)
□ Artículos Relacionados (mínimo 4 links a otros blogs)
□ NO hay dirección/teléfono/web de competidores
□ Sedes con links Google Maps al final
□ Firma Dr. Fabián Carreño Jiménez al final
□ Disclaimer INVIMA al final
□ Sedes en orden: Bogotá, Medellín, Barranquilla, Panamá, Bucaramanga (próximamente)
```

---

## Handles actuales del blog (para interlinking)

| Artículo | Handle |
|----------|--------|
| FUE vs DHI ES | `fue-vs-dhi-comparativa-definitiva-colombia-2026` |
| FUE vs DHI EN | `fue-vs-dhi-the-definitive-comparison-for-hair-transplants` |
| Qué es FUE ES | `que-es-implante-capilar-fue` |
| Medellín ES | `top-5-clinicas-de-implante-capilar-en-medellin-2026-guia-comparativa-actualizada` |
| Barranquilla ES | `top-5-clinicas-de-implante-capilar-en-barranquilla-2026-guia-del-caribe-colombiano` |
| Bucaramanga ES | `implante-capilar-bucaramanga` |
| Panamá ES | `clinica-implante-capilar-panama-2026` |
| Bogotá EN | `hair-transplant-bogota-2026` |
| Barranquilla EN | `top-5-hair-transplant-clinics-barranquilla-colombia-2026` |
| Bucaramanga EN | `bucaramanga-hair-transplant-2026` |
| Medellín EN | `top-5-clinicas-implante-capilar-medellin-2026-en` |
| Colombia City Guide EN | `colombia-hair-transplant-city-guide-2026-bogota-vs-medellin-vs-barranquilla-vs-bucaramanga-vs-panama-innovart-medical` |

---

## Relacionado

- [[articulos-medicos-checklist-seo-geo-aeo]] — 24 items de calidad obligatorios
- [[gbp-sedes-innovart]] — Links Google Maps por sede
- [[PLAN-MAESTRO-SEO-GEO-AEO-2026-06-25]] — Estrategia general
