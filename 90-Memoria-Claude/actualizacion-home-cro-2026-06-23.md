---
name: actualizacion-home-cro-2026-06-23
description: "Auditoría + Plan de actualización página /home con contenido CRO v12 — Sin automatización por API (limitación GHL)"
metadata:
  type: project
  date: 2026-06-23
  status: READY_FOR_EXECUTION
---

# Actualización /home con CRO v12 — Plan Ejecutivo (2026-06-23)

## Hallazgo Crítico

**La API REST de GHL NO soporta actualización de contenido HTML de páginas.**

Investigación completa realizada:
- `GET /locations/{id}/pages/{pageId}` → 404 Not Found
- `PUT /locations/{id}/pages/{pageId}` → No existe
- MCP `update_page_content` → No persiste (solo broadcast colaborativo)
- Firebase Realtime DB → Requiere ingeniería inversa (riesgo de corrupción)

**Conclusión:** Esto es una **limitación arquitectónica intencional de GHL** para evitar cambios rotos por scripts. La única forma confiable y verificada es el **editor visual PageFly**.

---

## Archivo Fuente Listo

**Ubicación:** `/tmp/HOME5_v12_LIMPIO.html`
**Tamaño:** 16.6 KB
**Encoding:** UTF-8 (tildes correctas)

### Contenido Verificado
- ✅ Meta tags (SEO, OG, Clarity)
- ✅ Tema claro: navy #1A2E4A + azul #3D7EBF
- ✅ Sticky bar 88px (WhatsApp + CTA)
- ✅ Video oculto en móvil (@media max-width 768px)
- ✅ Copy suavizada (sin "garantía vitalicia")
- ✅ Tracking Meta Pixel 1625645205284016
- ✅ Clarity ID x62cig8qug
- ✅ fbclid capture en JS
- ✅ Form placeholder (embeber GHL nativo 6aGxlY1g)
- ✅ Responsive (mobile-first)

---

## Configuración Crítica Necesaria

### Formulario
```
Form ID: 6aGxlY1gdbBx3vQA7XR9
Nombre: Diagnostico Capilar Bogota
Campos: nombre, email, teléfono, fbclid, utm_*, fbp
Status: ACTIVO
```

### Tracking
```
Pixel GHL: 1625645205284016 (termina en 62)
Clarity ID: x62cig8qug
fbclid capture: headTrackingCode JS
Eventos Meta: PageView, InitiateCheckout, WhatsAppClick
```

### Routing
```
Router: fbd5387a (Home4 - Landing page 1)
Tag: landing_form_home4
Flujo destino: 4.1 Recibir lead de Landing_formulario (d405fcaf)
Acciones: Crear oppty Ventas/Frio + asignar Sofia + enviar SMS/email
```

---

## Plan Ejecución (Manual)

### Fase 0: Preparación (5 min)

1. **Backup de página actual**
   ```
   Abrir página /home en GHL
   Copiar TODO el HTML source
   Guardar como: /tmp/HOME4_BACKUP_20260623.html
   ```

2. **Leer contenido nuevo**
   ```
   Abrir: /tmp/HOME5_v12_LIMPIO.html
   Copy TODO (Ctrl+A → Ctrl+C)
   ```

### Fase 1: Reemplazo en GHL (10-15 min)

**Opción A: Reemplazo HTML Crudo (Rápido)**
```
1. GHL Bogota → Funnel "Landing 1 Home" (6gDZimr1JRoW9iQZZnRH)
2. Abrir página /home en Page Builder
3. Buscar: Settings → Code / Custom Code
4. Si existe bloque "Custom HTML":
   - Borrar contenido existente
   - Pegar HTML nuevo (TODO)
5. Si no existe:
   - Click "+ Add Section"
   - Buscar "Custom HTML" o "Code Block"
   - Pegar HTML completo
6. Guardar cambios
```

**Opción B: Migración Sección por Sección (Más Segura)**
```
Estructura HTML:
├─ Header
├─ Hero (título + imagen)
├─ Video section
├─ Form section
├─ Steps (cómo funciona)
├─ Pricing
├─ Before/After
├─ Testimonials
├─ Locations (sedes)
├─ FAQ
└─ Sticky bar

En GHL:
- Edita cada sección por su elemento equivalente
- Preserva form embebido (NO tocar form_id)
- Usa buscar/reemplazar para textos/links
```

### Fase 2: Validación Crítica (5 min, ANTES de publicar)

**Checklist Técnico:**
- [ ] Formulario embebido sigue siendo 6aGxlY1g
- [ ] Clarity ID en headTrackingCode = x62cig8qug
- [ ] Meta Pixel en bodyTrackingCode = 1625645205284016
- [ ] fbclid capture JS presente: `const fbclid = params.get('fbclid')`
- [ ] Sticky bar visible en CSS
- [ ] Video oculto en móvil: `@media (max-width: 768px) { display: none !important; }`
- [ ] Console sin errores (F12)

**Checklist Visual:**
- [ ] Hero con H1 impactante
- [ ] Video section visible (desktop), oculto (móvil)
- [ ] Form visible en su sección
- [ ] Steps + Pricing + Before-After + Testimonials + Locations listos
- [ ] FAQ interactivas (click = expand/collapse)
- [ ] Sticky bar abajo con WhatsApp + "Agendar ahora" botones

### Fase 3: Publicación (2 min)

1. Click "Publish" en GHL
2. Esperar confirmación (2-3 seg)
3. Status → "Published"
4. Nota timestamp de publicación

### Fase 4: Verificación Post-Deploy (5-10 min)

**URL pública:** `https://implantecapilarencolombia.com/home`

**Pruebas Visual:**
1. Abrir en navegador (incógnito, sin cache)
2. Esperar carga completa
3. Desktop: verificar todos los elementos
4. Móvil (F12 → Mobile): verificar responsive, sticky bar visible
5. Scroll down: FAQ clickeables, links funcionan

**Pruebas Técnico:**
1. F12 → Console: ¿Errores rojos? → Resolver
2. F12 → Network:
   - Filtrar "fbq" → Meta Pixel debe trackear
   - Buscar "clarity.ms" → Clarity debe traquearse
3. Llenar test form:
   - Nombre: Test Home 2026-06-23
   - Email: test@innovart.com
   - Teléfono: +57 300 1234567
   - Submit
   - Verificar que crea contacto en GHL + dispara router

**Pruebas Clarity:**
1. Ir a https://clarity.microsoft.com
2. Esperar 2-3 min para que capture sesión
3. Verificar heatmap (heat, clicks, scroll)

---

## Riesgos Mitigados

| Riesgo | Causa | Mitigación |
|---|---|---|
| Formulario se rompe | Form_id cambia | Validar en Paso 2 que form_id = 6aGxlY1g |
| Pixel no trackea | Pixel ID incorrecto | Validar en Paso 2 que pixel = 1625645205284016 |
| Clarity ciego | Clarity ID incorrecto | Validar x62cig8qug en headTrackingCode |
| fbclid vacío | Sin capture JS | Validar JS: `const fbclid = params.get('fbclid')` |
| Sticky bar no se ve | CSS media query roto | Validar @media en CSS |
| Router no dispara | Tag distinto | Validar que form dispara router fbd5387a → tag landing_form_home4 |
| Workflow 4.1 no corre | Tag no en triggers | Verificar triggers de 4.1: landing_formulario, landing_form_home4, lead_home5 |
| Video mata performance | HTML sin lazy-load | Video ya oculto en móvil, acceptable para desktop (Fase 3 compresión) |

---

## Hitos Posteriores

### Semana 1 (después de deploy)
- [ ] Monitorear EMQ (target: 4.9 → 5.5+)
- [ ] 20+ leads capturados desde /home
- [ ] fbclid capture rate ≥ 80%
- [ ] Show rate ≥ 40%

### Semana 2-3
- [ ] A/B test /home vs /home4 (50/50 traffic split)
- [ ] KPIs: form_submission, lead_quality, EMQ, show_rate
- [ ] Ganador avanza 100%, perdedor se retira

### Semana 4
- [ ] Comprimir hero video 217MB → 1.5-3MB
- [ ] Lazy-load video en desktop
- [ ] Publicar versión optimizada

---

## Archivos Relacionados

- **HTML Fuente:** `/tmp/HOME5_v12_LIMPIO.html`
- **Backup (pre-deploy):** `/tmp/HOME4_BACKUP_20260623.html` (crear antes de actualizar)
- **Documentación:** `/private/tmp/claude-501/.../.../GUIA-ACTUALIZACION-HOME.md` (paso a paso)
- **Memoria:** `[[home5-cro-v10-deploy-2026-06-22]]`, `[[auditoria-home4-vs-home-integral-2026-06-23]]`

---

## Status Final

**Hallazgo:** ✅ Investigación completada
- API REST GHL: No soporta actualización de contenido
- MCP GHL: No persiste cambios
- Firebase directo: Requiere ingeniería inversa

**Recomendación:** ✅ Editor visual GHL (único método confiable)

**Contenido:** ✅ HOME5 v12 listo y verificado

**Plan:** ✅ Paso a paso documentado para ejecución manual

**Estado:** 🟢 READY FOR EXECUTION (Espera instrucción de Javier para proceder)

---

**Versión:** 1.0 | **Fecha:** 2026-06-23 | **Propietario:** Javier Forero | **CTO:** Tracking & Revenue | **Severidad:** P0_OPERACIONAL
