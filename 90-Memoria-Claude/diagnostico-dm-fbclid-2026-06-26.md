---
name: diagnostico-dm-fbclid-critico-2026-06-26
description: ✅ COMPLETADO 2026-06-29 — fbclid en DM/IG directo resuelto por Javier.
metadata:
  type: project
  status: COMPLETADO
  fecha_completado: 2026-06-29
  date: 2026-06-26
  status: solucion-lista-pero-bloqueada
---

# DIAGNÓSTICO CRÍTICO — fbclid Perdido en DM/IG (No es /home)

## El Problema Real (Diferente a lo que se pensaba)

**Situación RESUELTA:** fbclid SÍ se captura en `/home` via headTrackingCode. ✅

**Situación BLOQUEANTE (Nueva):** Cuando un lead **ingresa directamente por DM/IG** sin pasar por `/home`, Meta **NO pasa fbclid en el webhook** que recibe GHL.

### Flujo que falla:
```
User ve Ad en IG/FB (fbclid=abc123 en Meta internamente)
       ↓
Clickea → Va a tu perfil @innovartmedical
       ↓
Lee contenido + Envía DM ORGÁNICO
       ↓
DM llega a GHL webhook
       ↓
❌ GHL recibe: {phone, message, timestamp}
❌ FALTA: fbclid (Meta no lo pasa)
```

**Por qué no funciona:**
- Meta crea `fbclid` al hacer clic en el ad
- Instagram **no preserva parámetros URL en el perfil visible** (`instagram.com/@innovartmedical` — sin fbclid en URL)
- Cuando el user envía DM, Meta **no incluye fbclid en el webhook de GHL**
- GHL webhook recibe solo: phone, message, channel, timestamp (NO click_id, NO fbclid)

## Impacto en Revenue

- **EMQ 4.9** (no mejora) porque Meta no recibe fbclid → **no matchea eventos con el click original**
- **Show rate 43%** no mejora porque Meta optimiza por "generic event" no por "valued lead"
- **Pérdida ~600 leads/mes** sin atribución a la ad que los trajo

## Las 3 Soluciones Candidatas

| Opción | Dificultad | Validez | Impacto |
|--------|-----------|---------|---------|
| **A: Meta Graph API** | Difícil | ⭐⭐⭐ ÓPTIMA | GHL busca fbclid por teléfono en Meta, lo guarda |
| **B: Redirect Shortlink** | Media | ⭐⭐ OK | Bio IG → link con tracking + sesión preservada |
| **C: Filtro por canal** | Fácil | ⭐ Workaround | Reconocer DM/IG vs landing, procesar diferente |

**Recomendación:** Opción A si tienes acceso a Meta Graph API (admin token). Si no, Opción B (menos efectivo, pero viable).

---

**Why:** fbclid es **la única conexión entre el click de Meta y el evento en Meta** que permite que Meta aprenda qué tipo de lead convierte. Sin él, Meta sigue ciega.

**Status:** Solución teórica lista. Bloqueante: Javier necesita decidir opción + proveer tokens/acceso.
