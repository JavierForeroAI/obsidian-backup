---
name: innovart-code-standards
description: Estándares de código consolidados para Innovart Medical IPS — versiones, stack técnico, integraciones y checklist de cumplimiento
metadata:
  type: reference
  fecha: 2026-06-30
  status: ACTIVO
  version: 1.0
  aplica_a: Shopify, PageFly, GemPages, Cloudflare Workers, GHL, Meta tracking
---

# Estándares de Código — Innovart Medical IPS

## I. Versionado Obligatorio

### Protocolo de Cambios Críticos

**REGLA ABSOLUTA:** Cada cambio en código crítico → versión en Obsidian + changelog + rollback.

**Aplica a:**
- `theme.liquid` (Shopify main theme)
- `theme.pagefly.liquid` (PageFly layouts)
- `theme.gempages.blank.liquid` (GemPages Panama)
- Cloudflare Workers (`innovart-capi-webhook-no-tocar`, `innovart-wa-redirect-320`)
- Scripts de tracking (fbclid, UTMs, CAPI events)
- GHL workflows críticos (4.1, lead routing)
- Qikify form configuration

**Estructura de archivo:**
```
[archivo]-v[numero]-[fecha-YYYY-MM-DD].md
Ejemplo: versionado-theme-pagefly-liquid-v4-2026-06-30.md
```

**Contenido obligatorio (cada versión):**
- **Cambio:** Qué exactamente se modificó
- **Por qué:** Razón del cambio (síntomas, datos que prueban la necesidad)
- **Código:** Versión completa del bloque afectado
- **Ubicación:** Línea aproximada en el archivo
- **Verificación:** Pasos para probar en DevTools/producción
- **Impacto esperado:** Qué debe funcionar después
- **Rollback:** Cómo volver a versión anterior si falla

**Referencia directa:** [[protocolo-versionado-codigo-critico]]

---

## II. Stack Técnico Actual (2026-06-30)

### Shopify (innovartmedical.com)
- **Tema:** `Dawn — GEO IA Innovart` (ID `181331001645`)
- **Editores de Landing:** 
  - PageFly (ciudades: Bogotá, Medellín, Barranquilla, Bucaramanga)
  - GemPages (Panamá: /panama, /barberia, /financiacion)
- **Theme archivos críticos:**
  - `theme.liquid` — Main theme (v2)
  - `theme.pagefly.liquid` — PageFly layouts (v4)
  - `theme.gempages.blank.liquid` — GemPages Panamá
- **Plan:** Basic / Moneda: COP
- **Pixel Shopify:** `[XXXXX]62` (Meta App oficial)

### GHL (6 sub-cuentas)
- Bogotá, Medellín, Barranquilla, Bucaramanga, Panamá
- Cuenta principal (auditoría multi-sede)
- **Línea principal SMS:** 573171224974 (Medellín hasta 312)
- **Línea WhatsApp API:** +57 310/317/313, 507 650 (Meta CTWA)

### Cloudflare Workers (Innovart)
1. **`innovart-capi-webhook-no-tocar`** (v4)
   - Recibe webhooks GHL
   - Filtra eventos fraudulentos (`SubmitApplication` sin PII/fbclid)
   - Envía a Meta CAPI + GHL CTWA tracker
   - Endpoint: `/qikify-lead`, `/wa-ctwa`, etc.

2. **`innovart-wa-redirect-320`**
   - Captura WhatsApp desde línea vieja 320 (bloqueada bajo LeadConnector)
   - Upsert contacto GHL + tarea para comercial

### Meta (Publicidad)
- **6 cuentas:** BGTA (USD), QUILLA, PANAMA, MEDELLIN (COP), LANDING DIEGO, INTERACCION REDES DIEGO
- **Pixels activos:** 1625645205284016 (GHL), 62 (Shopify)
- **App de tracking:** "CLAUDE CODE DA-JF" (1698932398019234) — API development, NO SDK
- **CAPI Token:** Almacenado en Cloudflare secrets
- **Webhook Meta para CTWA:** `innovart-wa-redirect-320` + `innovart-capi-webhook-no-tocar/wa-ctwa`

### Google Ads
- **MCP:** Conectado (solo lectura), Project `innovart-google-ads-mcp`
- **MCC:** 2084232674
- **Creds:** `~/google-ads.yaml`

---

## III. Tracking — Capas Integradas

### Capa 1: Meta Pixel + fbclid
- **Pixel ID:** `1625645205284016` (GHL landings) + `62` (Shopify)
- **fbclid capture:** localStorage + custom field `fb_click_id` (Bucaramanga: FYVJpTGSmAPhiqoRwm97, Medellín: SFpTjWRflMI3AURvNBqF)
- **Ubicación:** Custom Code Head (GHL landings) + theme.liquid (Shopify)
- **Validación:** URLSearchParams + localStorage test

### Capa 2: CAPI Server-Side
- **Worker:** `innovart-capi-webhook-no-tocar`
- **Eventos:** Lead, Schedule, Purchase, SubmitApplication
- **PII requerido:** Email (hash SHA256) + Phone (hash) + City
- **Filtro:** Bloquea eventos sin fbclid/fbp O sin PII
- **Redundancia:** Meta Pixel + CAPI (2 vías)

### Capa 3: UTMs Persistentes
- **Fuentes activas:** Landing (✅), DM IG (✅), DM FB (✅), WA Directo (⏳), Typeform (⏳), Lead Forms (⏳)
- **Parámetros:** `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`
- **Captura:** sessionStorage → localStorage → GHL form
- **Permanencia:** Acción Router + etiquetado workflow

### Capa 4: ctwa_clid (WhatsApp Ads)
- **Custom field GHL:** `ctwa_clid` (por sede)
- **Webhook Meta:** Dispara en `innovart-wa-redirect-320`
- **Worker endpoint:** `/wa-ctwa`
- **Validación:** Field ID by location (Bogotá, Medellín, etc.)

### Capa 5: Clarity (Microsoft)
- **MCP:** microsoft/clarity-mcp-server (first-party)
- **Token:** Data Export guardado (⚠️ REGENERAR — expuesto en chat)
- **Limit:** 10 llamadas/día → pull 1 vez y cachear
- **Métricas:** Heatmap, scroll, navegabilidad, errores JS

**Referencia completa:** [[tracking-setup-completa-2026-06-23]]

---

## IV. Formularios Qikify → GHL → Worker

### Flujo Qikify (V4 — 2026-06-30)

1. **Carga:** `<script src="https://app.qikify.com/embed.js" async></script>` (NO www.qikify.com)
2. **Embed:** `<div contactform-embed="483316"></div>` + `</body>` ANTES de `</html>`
3. **Listener:** `bcontact:beforeFormSubmitted` → intercept datos
4. **Post:** `https://innovart-capi-webhook-no-tocar.innovartmedicalips.workers.dev/qikify-lead`
5. **GHL:** Worker enruta a sub-cuenta por sede + tags + crea oportunidad

**Verificación DevTools:**
```javascript
typeof window.BContact
// Debe retornar: "object" (NO "undefined")
```

**Crítico:** Sin `</body>` en theme.pagefly.liquid, el formulario desaparece.

**Referencia:** [[versionado-theme-pagefly-liquid]], [[paso-a-paso-arreglo-formularios-2026-06-30]]

---

## V. Ciudades Soportadas (NO CALI)

| Ciudad | Sede | GHL Location | SMS | WhatsApp API | Pixel | Página Landing |
|---|---|---|---|---|---|---|
| Bogotá | BTA | BGTA-USD | 312/Principal | +57 310 | 62 + GHL | /implante-capilar-bogota |
| Medellín | MDE | MDE-COP | 312 | +57 317 | 62 + GHL | /implante-capilar-medellin |
| Barranquilla | BAQ | BAQ-COP | 312 | +57 313 | 62 + GHL | /implante-capilar-barranquilla |
| Bucaramanga | BUC | BUC-COP | 312 | +57 310 | 62 + GHL | /implante-capilar-bucaramanga (EN PROGRESO) |
| Panamá | PAN | PANAMA-USD | N/A | +507 650 | 62 + GHL | /pages/panama + GemPages |

**❌ NUNCA Cali** — Referencia: [[regla-sedes-definitivas]]

---

## VI. Workflows Críticos (GHL)

### Workflow 4.1 "Recibir lead de Landing_formulario"
- **Trigger:** Form submission (varias formas: Qikify, nativa GHL, etc.)
- **Entrada:** Contacto con tags `fuente_web_qikify` + `landing_formulariov2` + `oportunidad ventas frio`
- **Acciones:**
  - Activar SMS/WhatsApp al lead (habilitado en 4 sedes)
  - ⚠️ Bucaramanga: Paso NO existe aún — pendiente agregar
- **Tags:** landing_form_home, landing_form_home5, landing_formulariov2
- **Status:** ✅ Activo (excepto Bucaramanga step faltante)

### Workflow 21 "Agentes de IA" (Multi-agente)
- **Propósito:** IA conversacional en multi-canal (WA, IG, FB, form)
- **Entrada:** Lead con ciertos tags
- **Salida:** Mensajes contextuales + reactivación + social proof

### Validación Landing POST-DEPLOY
- **Protocolo:** 4 fases (MCP check → validación técnica → E2E test → limpieza)
- **Duración:** ~10 min
- **Referencia:** [[protocolo-validacion-landing-automatica]]

---

## VII. Schema.org + SEO

### MedicalClinic (Home + 5 ciudades)
- **Ubicación:** theme.liquid (home) + theme.pagefly.liquid (ciudades)
- **Propiedades:** 65+ (aumento de 12)
- **Validez:** 0 errores, 0 advertencias (Rich Results Test)
- **Agregado Rating:** `4.3/103` (Bogotá), `5.0/25` (Medellín), `4.8/37` (Barranquilla)
- **PriceRange:** COP 8M–11M (Colombia), USD 3,500–4,500 (Panamá)
- **Sedes:** 5 direcciones + coordenadas GPS + GBP links

### FAQPage
- **Ubicación:** Separada por ciudad (Bogotá, Medellín, Barranquilla, Bucaramanga)
- **8 preguntas base** + respuestas con procedimiento específico
- **NO en MedicalProcedure** — va en tema aparte
- **Validación:** Rich Results Test ✅

### JSON-LD Inyección
- **Método:** Shopify GraphQL metafieldsSet (theme.liquid)
- **Alternativa:** Liquid snippet (theme.pagefly.liquid para ciudades)
- **Nunca:** Hardcoded en HTML (se pierde en actualizaciones)

**Referencia:** [[schema-arquitectura-logica-no-tocar]]

---

## VIII. Seguridad + Compliance

### Datos Sensibles (NUNCA en client-side)
- ❌ GHL API tokens
- ❌ Passwords Meta
- ❌ Private keys Cloudflare
- ✅ Usar environment variables + Cloudflare secrets

### GDPR / LSPDP Panamá
- Consentimiento en landing pages (checkbox)
- Política de privacidad enlazada
- Datos con PII → hash SHA256 antes de CAPI
- Retención: 90 días (GHL default)

### Idioma
- **Shopify Admin:** Español (instrucciones)
- **Código:** Comentarios en inglés/español (consistencia)
- **GHL:** Siempre español (tags, workflows, planes)

---

## IX. Restricciones de Lenguaje

**PROHIBIDO en cualquier comunicación Innovart:**
- "Garantía vitalicia" → "Garantía de folículos implantados"
- "Cure la alopecia" (claim falso)
- Promesas de "cabello de verdad = cabello de antes"
- Términos médicos sin disclaimer

**Referencia:** [[restricciones-lenguaje]]

---

## X. Integraciones Cross-Platform

| De | A | Método | Status | Referencia |
|---|---|---|---|---|
| Shopify | GHL | Webhook (form + purchase) | ✅ | [[integraciones-cross-platform-maestro]] |
| WordPress | GHL | Gravity Forms + custom hooks | ✅ (listo) | [[integraciones-cross-platform-maestro]] |
| Qikify | GHL | Worker (bcontact event) | ✅ | [[versionado-theme-pagefly-liquid]] |
| Qikify | CAPI | Worker (fb_pixel + events) | ✅ | [[versionado-theme-pagefly-liquid]] |
| Meta Ads | GHL | CTWA webhook → Worker | ✅ | [[ctwa-sistema-100-operacional-2026-06-29]] |
| GHL | Meta CAPI | Worker (eventos Lead/Purchase) | ✅ | [[capi-webhook-worker]] |
| GHL | Clarity | MCP (heatmaps + scroll) | ✅ | [[clarity-mcp-microsoft]] |

---

## XI. Checklist Pre-Publicación (Landing/Blog)

### Technical
- [ ] Pixel Meta dispara (Network tab)
- [ ] fbclid capturado en localStorage
- [ ] Qikify carga (typeof window.BContact === "object")
- [ ] Form POST llega a Worker (Console log + Network)
- [ ] Schema válido (Rich Results Test)
- [ ] Alt text en todas las imágenes
- [ ] Título + meta description únicos

### Compliance
- [ ] Byline Dr. Carreño presente (blogs)
- [ ] ISHRS + disclaimer visible
- [ ] Fecha de última revisión actual
- [ ] NO "garantía vitalicia" ni claims falsos
- [ ] Sedes correctas (Bogotá, Medellín, etc. — NO Cali)
- [ ] Teléfonos correctos por sede

### Tracking
- [ ] utm_source, utm_medium, utm_campaign completos (si aplica)
- [ ] ctwa_clid mapeado (WhatsApp ads)
- [ ] CAPI event mapping correcto
- [ ] Clarity tag presente (head)

---

## XII. Rollback + Emergency

### Si algo falla en Producción

1. **Identifica** archivo afectado (theme.liquid, Cloudflare, etc.)
2. **Busca en Obsidian** la versión actual (ej. versionado-theme-pagefly-liquid-v4)
3. **Lee rollback steps** en la versión anterior (v3)
4. **Contacta a Javier** con: versión actual, error observado, logs
5. **Ejecuta rollback** manualmente (pasar 15 min a evitar 2 horas de debugging)

### Canales de Emergencia
- **Javier:** innovartmedicalips@gmail.com
- **Esneider (Media):** esneidervc17@gmail.com
- **Dev emergencia:** Claude Code (chat directo)

---

## XIII. Próximos Hitos (2026-06-30+)

- ✅ Qikify V4 (2026-06-30)
- ⏳ Bucaramanga: SMS step en 4.1 + E2E test
- ⏳ Fase 3 GEO/IA: Video FAQ
- ⏳ Pixel 1 permisos CAPI verificación
- ⏳ IG DM: Workflows ciudad E2E test real

---

## Contactos Rápidos

| Rol | Contacto | Usar para |
|---|---|---|
| Director Médico | Dr. Fabián Carreño | Compliance médico, bylines |
| Media Buyer | Esneider (esneidervc17@gmail.com) | Campañas Meta, UTMs, CAPI |
| Trafficker Local | Diego | Criterios Google Ads local |
| Dev/Ops | Javier (innovartmedicalips@gmail.com) | Código crítico, rollback |

---

**Última actualización:** 2026-06-30
**Versión:** 1.0
**Próxima revisión:** 2026-07-15 (cambios mayores)
