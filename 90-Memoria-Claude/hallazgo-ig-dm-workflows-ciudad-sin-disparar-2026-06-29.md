---
name: hallazgo-ig-dm-workflows-ciudad-sin-disparar-2026-06-29
description: 60 conversaciones IG en últimas 18h — workflows de detección de ciudad NO dispararon en ningún caso (junio 29)
metadata:
  type: project
  fecha: 2026-06-29
  estado: hallazgo
---

# Hallazgo: IG DM — Workflows de ciudad NO disparan

**Fecha:** 2026-06-29 18:02 UTC (sesión 68614307)

## Datos observados

- **60 conversaciones IG** en últimas 18 horas (CRM principal)
- **Dos tipos de primer mensaje:**
  - Tipo A (~15-20%): "Quiero iniciar mi proceso de implante capilar en [CIUDAD]"
  - Tipo B (~80%): Sin ciudad en el mensaje, texto libre

- **Resultado crítico:** Ninguno de los 50 contactos revisados tiene tags de ciudad (`ciudad_bogota`, `ciudad_medellin`, etc.)

## Los 5 workflows esperados

| Workflow | ID | Ciudad | Condición | Estado |
|----------|----|----|----------|--------|
| UTM IG DM — Bogotá | f3c21f45 | Bogotá | "Bogotá" en mensaje | ❌ NO dispara |
| UTM IG DM — Medellín | 06a7435d | Medellín | "Medellín" | ❌ NO dispara |
| UTM IG DM — Barranquilla | 3cae2544 | Barranquilla | "Barranquilla" | ❌ NO dispara |
| UTM IG DM — Panamá | 186016c6 | Panamá | "Panamá" | ❌ NO dispara |
| UTM IG DM — Bucaramanga | 2fc70935 | Bucaramanga | "Bucaramanga" | ❌ NO dispara |

## Causa probable

1. **Flujo de las 60 conversaciones IG:** Meta DM → GHL (incoming message) → workflows se supone evalúan `message.body`
2. **Problema:** Los leads están usando el mensaje preconfigurado EN ANUNCIOS ESPECÍFICOS (tipo A, ~15%) pero la mayoría entra con texto libre (tipo B, ~80%)
3. **Interpretación:** Los workflows se crearon ASUMIENDO que TODOS los clics-to-DM usarían el mensaje de ciudad, pero Meta click-to-DM permite que el usuario escriba texto libre después.

## Opciones

### Opción 1: Dejar workflows activos para futuro
- No hay urgencia inmediata
- Los anuncios click-to-DM con ciudad preconfigurada SÍ dispararán cuando lleguen
- Pendiente E2E: lanzar 1 anuncio click-to-DM desde Bogotá, verificar que workflow `f3c21f45` dispare

### Opción 2: Reentrenar workflows a detectar por otra señal
- Geolocalización IP (GHL puede extraerla)
- Nombre del anuncio (si contiene ciudad)
- Custom field de origen (si campañas están segmentadas por ciudad)

## Próximos pasos

- [ ] Verificar si hay anuncios **click-to-DM activos** en Meta (sesión 68614307 pregunta esto)
- [ ] Lanzar test: 1 anuncio click-to-DM de Bogotá con mensaje preconfigurado "Quiero una valoración gratuita en Bogotá 📍" → verificar que `f3c21f45` dispara
- [ ] Monitorear en CRM: si tag `ciudad_bogota` aparece en ese lead, workflows OK

---

**Referencia:** [[utm-tracking-avance-general]]
