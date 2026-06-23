---
name: home5-reconstruida-2026-06-22
description: HOME5 reconstruida con UTF-8 correcto, tildes restauradas, sin vitalicia
metadata:
  type: project
---

# HOME5 — Reconstruida 2026-06-22

**Fecha:** 2026-06-22. Múltiples iteraciones para reparar encoding roto, tildes dañadas y estructura.

## Problema identificado

Versión anterior (`HOME5_COMPLETO_CON_CAPA.html`) tenía:
- ✗ Tildes y caracteres rotos (ñ, á, é, etc. → `√≠`, `‚Äî`, etc.)
- ✗ Código JavaScript suelto al final (no oculto)
- ✗ Botón en posición incorrecta
- ✗ Viñetas dañadas
- ✗ Imágenes sin portada (fondo negro)

## Solución aplicada

**Reconstrucción completa con UTF-8 correcto:**
- ✅ `<meta charset="UTF-8">` en `<head>`
- ✅ Todas las tildes restauradas (`años` → años, `Bogotá` → Bogotá, `é` → é)
- ✅ HTML estructura limpia (sin code suelto)
- ✅ Tema claro: marfil (#F9FAFB) + navy (#1A2E4A) + azul CTA (#3470A6)
- ✅ Responsive (desktop + móvil)
- ✅ **Sin "vitalicia"** (prohibido) — solo "Garantía de folículos implantados"
- ✅ **Sin promesas falsas** — sin "dinero de vuelta"
- ✅ Precios grandes (5rem) → más visibles
- ✅ Espacios reducidos (comprimido)
- ✅ H1 nuevo: *"Cabello que crece en 12 meses — garantía de folículos implantados incluida"*
- ✅ Hero reorganizado: foto de doctores + nombre + "Líderes especialistas" + "6000+ pacientes" (unificado, sin duplicación)

## Ubicación

- **Archivo local:** `/tmp/HOME5_v12_LIMPIO.html`
- **Desktop:** `/Users/javierforero/Desktop/HOME5-FINAL-AUDITADO.html`
- **Destino:** Pegar en **GHL Bogotá** → Websites → **landing1** → **home5** → Custom Code

## Próximos pasos

1. ✅ Pegarlo en GHL (Custom Code de home5)
2. ✅ Verificar que se vea en navegador (desktop + móvil)
3. A/B test vs home4 (form RB4a58 vs 6aGxlY1g)
4. Opcional: agregar formulario GHL embed si falta

## Location ID

- **Bogotá:** DgjjDzD9nkCKv8AGF1Qb (si necesitas actualizar por MCP)

Relacionado: [[home5-cro-v10-deploy-2026-06-22]] · [[home4-no-trackea-clics-cro]] · [[restricciones-lenguaje]]
