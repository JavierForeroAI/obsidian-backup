---
name: articulos-shopify-publicados-2026-06-24
description: 8 artículos de blog publicados en Shopify con bloque "Puntos clave" (diseño estándar gradiente + tarjetas). Alopecia androgenética, 5 señales, Candidato, FUE vs DHI, FAQ, Clínica, Dr. Fabián, Dra. Gloris. 2026-06-24.
metadata:
  type: project
---

# Artículos Shopify Publicados — Bloque "Puntos Clave" (2026-06-24)

**Fecha ejecución:** 24 de junio 2026  
**Constraint técnico:** CSS inline only (sin `<style>` tags) — Shopify los elimina  
**Diseño aprobado:** Gradiente `linear-gradient(135deg,#EAF2FB 0%,#EDF7F2 100%)` + barra azul + tarjetas blancas + círculo verde ✓

---

## Artículos Publicados (8 de 17 totales)

| # | Artículo | URL Handle | ID | Estado | Notas |
|---|----------|-----------|----|----|-------|
| 1 | Alopecia androgenética | `alopecia-androgenetica-por-que-se-cae-el-pelo` | 683915247917 | ✅ LIVE | Creado nueva, integrado en workflow |
| 2 | 5 señales tempranas | `senales-tempranas-perdida-de-pelo` | 683915378989 | ✅ LIVE | Creado nueva, integrado |
| 3 | ¿Eres buen candidato? | `buen-candidato-injerto-capilar-zona-donante` | 683915968813 | ✅ LIVE | Creado nueva, integrado |
| 4 | FUE vs DHI (sin marketing) | `fue-vs-dhi-que-tecnica-elegir` | 683916067117 | ✅ LIVE | Creado nueva, integrado |
| 5 | Preguntas frecuentes | `preguntas-frecuentes-implante-capilar` | 683417829677 | ✅ LIVE | Existente → bloqueado PK |
| 6 | Innovart Medical IPS (Clínica) | `innovart-medical-ips-lider-restauracion-capilar` | 683417862445 | ✅ LIVE | Existente → bloqueado PK |
| 7 | Dr. Fabián Carreño | `dr-fabian-carrenio-jimenez-director-medico` | 683417927981 | ✅ LIVE | Existente → bloqueado PK |
| 8 | Dra. Gloris Morales | `dra-gloris-morales-cofundadora-vocera-medica` | 683417960749 | ✅ LIVE | Existente → bloqueado PK |

---

## Bloque "Puntos Clave" — Especificación

**Ubicación:** Después del primer `</p>` en cada artículo (posición 918 en FAQ, ~1000+ en otros)

**Diseño HTML (CSS inline):**
```html
<div style="display:flex;align-items:flex-start;gap:20px;box-sizing:border-box;width:100%;max-width:680px;margin:0 auto 26px;background:linear-gradient(135deg,#EAF2FB 0%,#EDF7F2 100%);border:1px solid #E6E4DD;border-left:4px solid #3D7EBF;border-radius:8px;padding:20px;">
  <div style="width:4px;background:#3D7EBF;flex-shrink:0;"></div>
  <div style="flex:1;font-family:Arial,sans-serif;font-size:14px;">
    <div style="font-weight:bold;color:#0A0A0A;margin-bottom:12px;">Puntos clave</div>
    <!-- 4-5 items en formato: -->
    <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:8px;">
      <div style="background:#fff;border-radius:50%;width:24px;height:24px;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:#27AE60;">✓</div>
      <div style="color:#333;font-size:13px;">Punto clave aquí</div>
    </div>
    <!-- repetir para cada punto -->
  </div>
</div>
```

**Validación pre-publicación:**
- No debe llevar `<style>` tags (Shopify los elimina automáticamente)
- Todos los estilos → atributo `style=""` inline
- URLs de WhatsApp escapadas: `https://wa.me/573124565014?text=` + `urllib.parse.quote(msg)` (sin carácter especial sin encode)

---

## Contenido por Artículo

### 1. Alopecia androgenética
- **Puntos clave:** Genética → DHT → miniaturización, diferencia androgenética vs. otras, cuándo actuar, no es "caída normal"
- **CTA:** WhatsApp especialista
- **Compliance:** ✅ (sin vitalicia, sin resultado garantizado, foto Dr. Carreño)

### 2. 5 señales tempranas
- **Puntos clave:** Cambio en línea de cabello, disminución volumen, cuero cabelludo visible, cambio textura, edad de aparición
- **CTA:** Agendar valoración
- **Compliance:** ✅

### 3. ¿Eres buen candidato?
- **Puntos clave:** Zona donante importante, edad 25+, estabilidad caída, expectativas realistas, densidad suficiente
- **CTA:** Consultorio
- **Compliance:** ✅

### 4. FUE vs DHI
- **Puntos clave:** FUE = extracción individual sin cicatriz, DHI = injerción directa, tiempo recuperación, costo, recomendación por tipo paciente
- **CTA:** Comparativa completa
- **Compliance:** ✅ (sin "mejor", neutral)

### 5. FAQ
- **Puntos clave:** ¿Duele?, ¿Cuánto cuesta?, ¿Recuperación?
- Tamaño: 13,239 caracteres (OK)

### 6-8. Clínica + Médicos
- **Puntos clave:** En credenciales + experiencia
- Tamaño: 13,640 / 11,245 / 10,961 caracteres (OK)

---

## Typo Fix Aplicado (24-jun)

**Problema:** "Eschíbenos" en CTA text
**Fix:** Reemplazado con "Escríbenos" (correcto) en los 4 artículos nuevos + los 4 existentes

**Verificación:**
```bash
grep -c "Escríbenos" /tmp/new_body_*.txt  # Debe mostrar 2+ en cada
grep -c "Eschíbenos" /tmp/new_body_*.txt  # Debe ser 0
```

---

## Estado del Proyecto Blog Shopify

| Fase | Artículos | Status | Notas |
|------|-----------|--------|-------|
| 1 (Nuevo) | 4 | ✅ PUBLICADOS | Alopecia, 5 señales, Candidato, FUE vs DHI |
| 2 (Actualización) | 4 | ✅ ACTUALIZADO | FAQ, Clínica, Dr. Fabián, Dra. Gloris → +PK |
| 3 (Resto) | 9 | ⏳ PENDIENTE | Resto de 17 blogs necesita PK |

---

## Pendientes

1. **Completar "Puntos clave" en los 9 artículos restantes** (Fase 3)
2. **Validación visual** en browser desktop/móvil (gradiente + responsividad)
3. **SEO check** — meta title/description por artículo (de ser necesario)
4. **Monitoreo compliance** — auditoría mensual de términos prohibidos

---

## Referencias

- [[fase-2-upgrade-blogs-contenido-2026-06-22]] — Descripción de los 16 blogs originales
- [[restricciones-lenguaje]] — Términos prohibidos ("garantía vitalicia" etc.)
- [[INDICE-BLOGS-SHOPIFY]] — Índice maestro estrategia blogs
- `~/.claude/skills/shopify-playbook-capacidades-mcp.md` — GraphQL mutations para artículos
