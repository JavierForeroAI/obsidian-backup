---
name: INDEX-CODE-STANDARDS
description: Punto de entrada integrado — Estándares de código + Checklist de validación + Referencias del sistema
metadata:
  type: index
  fecha: 2026-06-30
  status: ACTIVO
  version: 1.0
---

# Estándares de Código Innovart — Punto de Entrada Integrado

**LEER ESTO PRIMERO cuando hagas cualquier cambio de código o deploy en Innovart.**

---

## 🎯 Los 3 Documentos Maestros

### 1. [[innovart-code-standards]] (REFERENCIA TÉCNICA)
**Cuándo leer:** Antes de escribir código | Después de cambios | Para verificar stack actual

**Secciones clave:**
- **Sección I:** Protocolo versionado (OBLIGATORIO)
- **Sección II:** Stack técnico actual (Shopify, GHL, Cloudflare)
- **Sección III:** Capas de tracking (fbclid, CAPI, UTMs, CTWA)
- **Sección IV:** Formularios Qikify → GHL
- **Sección V:** Ciudades soportadas (NO Cali)
- **Sección VI:** Workflows críticos
- **Sección VII:** Schema.org + SEO
- **Sección VIII:** Seguridad + Compliance
- **Sección IX-XIII:** Integraciones, rollback, hitos

**Usa como:** Referencia mientras codeas | Validación pre-deploy | Guía de rollback

---

### 2. [[checklist-e2e-validation]] (PASO-A-PASO POST-DEPLOY)
**Cuándo leer:** Después de CADA deploy | Antes de comunicar "listo"

**Secciones clave:**
- **Sección 1:** Meta Pixel + fbclid en URL
- **Sección 2:** fbclid captura → localStorage → GHL field
- **Sección 3:** Qikify formulario → Worker → GHL creación
- **Sección 4:** Landing técnico (schema, alt text, performance)
- **Sección 5:** WhatsApp + CTWA tracking
- **Sección 6:** UTM tracking persistencia
- **Sección 7:** GHL workflow integración
- **Sección 8:** Cross-platform (Shopify ↔ GHL, Google Ads)
- **Sección 9:** Cleanup + confirmación

**Usa como:** Checklist ejecutable | DevTools step-by-step | Troubleshooting table

**Duración:** 10–15 min por landing/feature

---

### 3. [[MEMORY]] (ÍNDICE DEL RESTO)
**Cuándo leer:** Primera vez | Para contexto histórico | Links a auditorías pasadas

**Apunta a:**
- Versionado actual (theme.pagefly.liquid V4, etc.)
- Protocolos (validación landing, versionado código)
- Tracking detallado (fbclid auditoría crítica, CAPI filtro)
- Landings por ciudad (Bogotá, Medellín, etc.)
- GHL workflows + integraciones
- WhatsApp + CTWA sistema

---

## 🚀 Flujo Tipo: Deploy de Landing Nueva

### Paso 1: Plan + Versionado (Antes de tocar código)
- [ ] Leer [[innovart-code-standards]] Sección I (protocolo)
- [ ] Crear archivo Obsidian: `landing-[ciudad]-v1-[fecha].md`
- [ ] Documentar: qué cambios, por qué, dónde vivirá código

### Paso 2: Desarrollo (Seguir estándares)
- [ ] Consultar [[innovart-code-standards]] Sección II–VII (stack + tracking)
- [ ] Codigo crítico: Shopify/PageFly/GHL → versionado en Obsidian AHORA (no después)
- [ ] Schema.org: validar contra Sección VII
- [ ] Compliance: revisar Sección VIII

### Paso 3: Testing Local
- [ ] DevTools: fbclid, Qikify, UTMs (ver [[checklist-e2e-validation]] Sección 2–6)
- [ ] Formulario → GHL (ver Sección 3)

### Paso 4: Deploy a Producción
- [ ] Hard-refresh en navegador test
- [ ] Verificar una vez más: pixel, fbclid, Qikify

### Paso 5: E2E Validation (CRITICO)
- [ ] **Ejecutar [[checklist-e2e-validation]] COMPLETO (Secciones 1–9)**
- [ ] Marcar cada ✅ a medida que completas
- [ ] Si algo falla → troubleshooting table en Sección 9
- [ ] Duración: ~15 min

### Paso 6: Cleanup + Confirmación
- [ ] Eliminar test data (Sección 9.1)
- [ ] Hard-refresh browser (Sección 9.2)
- [ ] Email a Javier + Esneider (Sección 9.3)

---

## 🔧 Escenarios Rápidos

### Si Cambias theme.pagefly.liquid
1. Leer [[innovart-code-standards]] Sección IV (Qikify)
2. Revisar [[versionado-theme-pagefly-liquid]] (versión actual)
3. Crear v[N+1] en Obsidian con tu cambio
4. Deploy
5. Ejecutar [[checklist-e2e-validation]] Sección 3 (Qikify formulario)

### Si Cambias Meta Pixel / Tracking
1. Leer [[innovart-code-standards]] Sección III (tracking)
2. Revisar [[tracking-setup-completa-2026-06-23]] (fases)
3. Deploy cambio
4. Ejecutar [[checklist-e2e-validation]] Secciones 1–2, 5–6

### Si Cambias Schema.org
1. Leer [[innovart-code-standards]] Sección VII
2. Revisar [[schema-arquitectura-logica-no-tocar]] (reglas)
3. Deploy cambio
4. Ejecutar [[checklist-e2e-validation]] Sección 4.1 (Rich Results Test)

### Si Algo Falla en Producción
1. Identifica archivo (theme.liquid, Worker, etc.)
2. Busca versión actual en Obsidian (ej. [[versionado-theme-pagefly-liquid]])
3. Lee sección **Rollback** de la versión anterior (v[N-1])
4. Ejecuta pasos de rollback
5. Contacta a Javier: "Version v[N] falló, revertí a v[N-1], causa: [error observado]"

---

## 📋 Tabla de Referencia Rápida

| Necesitas... | Ir a... | Sección |
|---|---|---|
| Entender cómo versionar código | [[innovart-code-standards]] | I |
| Verificar stack técnico actual | [[innovart-code-standards]] | II |
| Implementar fbclid tracking | [[tracking-setup-completa-2026-06-23]] | FASE 2 + [[innovart-code-standards]] III |
| Arreglar formulario Qikify | [[versionado-theme-pagefly-liquid]] + [[paso-a-paso-arreglo-formularios-2026-06-30]] | — |
| Validar E2E post-deploy | [[checklist-e2e-validation]] | TODOS |
| Entender schema.org | [[schema-arquitectura-logica-no-tocar]] + [[innovart-code-standards]] VII | — |
| Rollback emergencia | Versión anterior en Obsidian (v1, v2, etc.) | Rollback section |
| Configurar GHL workflow | [[referencia-ghl-workflows-mcp]] | — |
| Entender CTWA / WhatsApp Ads | [[ctwa-tracking-whatsapp-ads]] + [[innovart-code-standards]] III | — |

---

## 🎯 Checklist Mental Antes de Cualquier Deploy

```
¿Hice cambio de código crítico?
  └─→ SÍ: ¿Documenté en Obsidian como v[N]? 
         └─→ NO: HAZLO AHORA antes de deploy
         └─→ SÍ: ¿Incluí rollback steps? 
                └─→ CONTINÚA

¿Deploy de landing o feature nueva?
  └─→ SÍ: ¿Voy a ejecutar checklist-e2e-validation COMPLETO?
         └─→ NO: HAZLO DESPUÉS del deploy (no opción)
         └─→ SÍ: ¿Tengo 15 min? 
                └─→ CONTINÚA

¿Algo falla durante E2E?
  └─→ SÍ: ¿Hay troubleshooting table en el checklist?
         └─→ SÍ: SIGUE los pasos
         └─→ NO: Abre DevTools, busca error en Console, contacta Claude

¿Todo ✅?
  └─→ SÍ: Email a Javier + Esneider (Sección 9.3 checklist)
         DEPLOY COMPLETADO ✅
```

---

## 👥 Contactos de Emergencia

| Rol | Contacto | Para |
|---|---|---|
| Lead técnico | Javier (innovartmedicalips@gmail.com) | Código crítico, rollback, arquitectura |
| Media Buyer | Esneider (esneidervc17@gmail.com) | Campañas, UTMs, Meta tracking |
| Backup técnico | Claude Code (chat directo) | Troubleshooting, DevTools debugging |

---

## 📚 Referencias Externas (EN OBSIDIAN)

**Auditoría y diagnósticos pasados:**
- [[auditoria-capimetaghl-base]] — Estado Meta + GHL + CAPI (verificación diaria)
- [[auditoria-fbclid-critica-2026-06-22]] — Root cause show rate 40% + EMQ
- [[diagnostico-dm-fbclid-2026-06-26]] — IG DM tracking resuelto
- [[paso-a-paso-arreglo-formularios-2026-06-30]] — Guía actual Qikify + GemPages

**Esquemas y templates:**
- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]] — Cómo funciona el tracking
- [[integraciones-cross-platform-maestro]] — Todas las integraciones unificadas
- [[plantilla-blog-innovart-modelo-perfecto]] — Para blogs nuevos
- [[adn-comunicacion-innovart]] — Antes de escribir copy

**Workflows y GHL:**
- [[referencia-ghl-workflows-mcp]] — Cómo construir workflows por API
- [[ghl-carpetas-workflows]] — Organización de workflows

---

## 🔄 Ciclo de Actualización

**Este documento se actualiza:**
- Cada deploy crítico (tema, landing, tracking)
- Cada auditoría completada
- Cada cambio de versión major

**Última actualización:** 2026-06-30
**Próxima revisión:** 2026-07-15 (si cambios mayores) o a demanda

---

## ✨ TL;DR (Muy Rápido)

1. **Antes de codear:** Leer [[innovart-code-standards]]
2. **Durante código:** Documentar en Obsidian (versionado)
3. **Después de deploy:** Ejecutar [[checklist-e2e-validation]]
4. **Algo falla:** Buscar versión anterior en Obsidian → rollback
5. **¿Pregunta?** → Leer tabla de referencia arriba

---

**Hecho para Javier. Actualizado por Claude Code. Sincronizado con MEMORY.md.**
