---
name: resumen-sesion-2026-06-22
description: Resumen de sesión 2026-06-22 — landing Bogotá completada al 95%. Qué hacer mañana.
metadata:
  type: project
  fecha: 2026-06-22
  estado: final-del-dia
---

# Resumen Sesión 2026-06-22 — Landing Bogotá

## ✅ LO QUE SE HIZO HOY

### Landing Bogotá — 6 elementos HTML/Liquid completos

| # | Elemento | Estado |
|---|---|---|
| 1 | gtag Google Ads `AW-16490325890` | ✅ |
| 2 | Schema GEO (MedicalClinic + MedicalProcedure + Breadcrumb) | ✅ |
| 3 | Bloque oculto `-9999px` | 🔴 PENDIENTE BORRAR |
| 4 | Script fbclid | ✅ |
| 5 | JSON-LD FAQPage | ✅ |
| 6 | **Eventos completo** (Meta Pixel + Google Ads + 11 eventos) | ✅ |

### Contenido de la página

| Elemento | Estado |
|---|---|
| H1 + párrafo intro | ✅ |
| NAP (dirección, horarios, teléfono) en texto | ✅ |
| Accordion FAQ (5 preguntas) en móvil | ✅ |
| Meta title + description (MCP) | ✅ |

### Archivos guardados en Obsidian

- **[[eventos-tracking-bogota-html-liquid-6]]** — Script listo para copiar/pegar
- **[[google-ads-meta-capi-mapeo-etiquetas]]** — Referencia de etiquetas (ViewContent, WhatsAppClick, Lead)
- **[[guia-replicacion-landings-ciudades]]** — Plantilla maestra para Medellín/Barranquilla/Bucaramanga
- **[[landing-ciudades-plantilla-checklist-2026-06-20]]** — Estado actualizado

---

## 🔴 PARA MAÑANA (3 TAREAS)

### 1. **Borrar bloque oculto `-9999px`** (con persona de Google)
   - Ubicación: HTML/Liquid #3 en PageFly (Bogotá)
   - Tiene: "garantía vitalicia" ×2 + H1 oculto duplicado
   - Acción: eliminar completamente el bloque
   - **Responsable:** Persona de Google (según lo agendado)

### 2. **Reemplazar imagen de horarios**
   - Problema: teléfono incorrecto `+57 318 8528481`
   - Solución: cambiar a `+57 312 456 5014`
   - Ubicación: imagen en móvil (en PageFly)
   - **Responsable:** Tú (o equipo de diseño)

### 3. **Pegar HTML/Liquid #6 en PageFly**
   - Ir a: [[eventos-tracking-bogota-html-liquid-6]]
   - Copiar todo el código
   - En PageFly → Panel izquierdo → + Add section → HTML/Liquid
   - Pegar y guardar
   - **Responsable:** Tú

### 4. **Publicar**
   - En PageFly: clic en **Publish** (arriba derecha)
   - En Shopify Admin: cambiar visibilidad de "Oculta" a "Visible"
   - Verificar URL en vivo: `https://www.innovartmedical.com/pages/implante-capilar-bogota`
   - **Responsable:** Tú

---

## 📋 CHECKLIST PARA MAÑANA

```
[ ] 1. Persona de Google borra bloque `-9999px`
[ ] 2. Reemplazar imagen horarios (teléfono 312)
[ ] 3. Pegar HTML/Liquid #6 en PageFly (eventos)
[ ] 4. Guardar en PageFly
[ ] 5. Publicar en Shopify
[ ] 6. Verificar URL en vivo
[ ] 7. Esperar 24-48h para que Google Ads valide
[ ] 8. En 15min: verificar Meta Ads Manager que reciba eventos
```

---

## 📊 DESPUÉS DE PUBLICAR BOGOTÁ

**Próximo paso:** Duplicar a **Medellín → Barranquilla → Bucaramanga**

Usar: [[guia-replicacion-landings-ciudades]]

Solo cambiar por ciudad:
- Dirección (MCP + texto PageFly)
- Barrio/zona
- URL handle
- Schema GEO (coordenadas)
- Google Ads etiquetas (si son diferentes)

El resto es idéntico.

---

## 🔗 Links rápidos

- Estado actual de Bogotá: [[landing-ciudades-plantilla-checklist-2026-06-20]]
- Script eventos listos: [[eventos-tracking-bogota-html-liquid-6]]
- Guía replicación: [[guia-replicacion-landings-ciudades]]
- Etiquetas Google Ads: [[google-ads-meta-capi-mapeo-etiquetas]]

---

**Pendiente post-publicación:** Auditoría de eventos en DevTools (console + network) para confirmar que Meta Pixel y Google Ads reciben datos correctamente.

*Sesión finalizada 2026-06-22*
