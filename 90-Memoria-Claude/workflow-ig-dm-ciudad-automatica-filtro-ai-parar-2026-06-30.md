---
name: workflow-ig-dm-ciudad-automatica-filtro-ai-parar-2026-06-30
description: Workflow GHL "IG DM - Ciudad Automatica" (ID b7be059f) — se agregó filtro para no reactivar spam marcado ai_parar. Reglas de negocio acordadas con Javier sobre retargeting, tags y respeto al comercial asignado
metadata:
  type: project
  fecha: 2026-06-30
  estado: parcialmente-implementado
---

# Workflow "IG DM - Ciudad Automatica" — filtro ai_parar + reglas de retargeting

**Workflow ID:** `b7be059f-d972-4065-8af4-3ce43d70d770` (cuenta principal GHL). No confundir con los 5 workflows separados "UTM IG DM — [Ciudad]" documentados en [[hallazgo-ig-dm-workflows-ciudad-sin-disparar-2026-06-29]] (esos evalúan `message.body` por ciudad; este workflow detecta/etiqueta ciudad de forma distinta y corre en el Worker de Cloudflare).

## Problema detectado

El workflow disparaba para **todos** los leads que responden por Instagram DM, incluyendo los que el comercial ya había marcado con el tag `ai_parar` (que se usa para decir "este lead es mío, manéjalo manualmente, no automatizar"). Resultado: leads marcados como spam/manuales estaban siendo reactivados por la IA sin que el comercial lo pidiera.

## Cambio aplicado — 2026-06-30 12:26 (versión 7, publicado y LIVE)

Se agregó al trigger (`Customer Replied` + Instagram DM, `message.type == 18`) la condición:

```
✅ SI: message.type == 18
✅ SI: Contact does NOT have tag "ai_parar"
```

Publicado vía `mcp__ghl__update_workflow_actions` + `mcp__ghl__publish_workflow`. Confirmado en el extracto de sesión: versión pasó de 5 → 6 (edición) → 7 (publicado).

## Reglas de negocio acordadas con Javier (para el PRÓXIMO ajuste, aún no implementado)

Contexto de negocio explicado por Javier: un lead de Instagram llega primero al bot **Sofia** (centro de operaciones comercial). El director/coordinador comercial luego reasigna el lead a un comercial disponible según su gestión. El comercial marca `ai_parar` para manejarlo manualmente.

Reglas que el sistema debe respetar (pendiente de implementar en el Worker, sesión quedó interrumpida antes de ejecutar):

1. **Nunca reasignar** el lead a otro comercial si ya tiene uno asignado — si un lead que ya fue atendido vuelve a escribir, debe **mantenerse con el mismo comercial**, no reasignarse a Sofia/bot ni a otro.
2. **Nunca quitar el tag `ai_parar`** al lead — incluso si vuelve a escribir y se le corre el proceso de detección de ciudad de nuevo.
3. **Sí se puede seguir corriendo el proceso de tags/ciudad** en retargeting (es decir, si el lead vuelve a escribir por una nueva pauta, se le puede volver a poner tags de ciudad — "de eso se trata el retargeting") — lo que no se puede es tocar `ai_parar` ni la asignación de comercial, ni reactivar la IA de conversación.
4. **Regla específica para "ciudad sin detectar":**
   - Si es un lead **nuevo** que llega desde publicidad sin mencionar ciudad → SÍ colocar el tag `ciudad_sin_detectar`.
   - Si es un lead **viejo** (ej. entró hace 4 meses, no tiene ciudad, no siguió conversación) → también colocar `ciudad_sin_detectar` (no dejarlo sin tag), pero sin que esto dispare ninguna reactivación de IA ni reasignación.
5. El único requisito no negociable: que el workflow siga clasificando/etiquetando ciudad, pero **jamás** le quite `ai_parar` al comercial ni reasigne el lead a otra persona/bot.

## Estado

- ✅ Filtro `ai_parar` en el trigger: implementado y publicado (v7).
- ⏳ Filtro "no reasignar si ya está asignado a un comercial" + ajuste del Worker de Cloudflare (reglas 1-4 arriba): **discutido y acordado pero NO implementado aún**. Javier dijo explícitamente "no cambies nada aún" al final de la sesión — quedó pausado a propósito.

## Próxima sesión — qué hacer

1. Ajustar el Worker/CAPI (`innovart-capi-webhook-no-tocar`) para que en el flujo de detección de ciudad de leads de Instagram:
   - Nunca haga `DELETE` sobre el tag `ai_parar`.
   - No reasigne `assignedTo` si el contacto ya tiene un comercial asignado (asignación ≠ Sofia/bot default).
   - Siga aplicando `ciudad_sin_detectar` a leads nuevos y viejos sin ciudad, sin que eso dispare reactivación de IA.
2. Publicar como versión 8 del workflow (o cambio en el Worker, según dónde viva la lógica) y validar E2E con un lead de prueba.

---
Referencias: [[hallazgo-ig-dm-workflows-ciudad-sin-disparar-2026-06-29]], [[referencia-ghl-workflows-mcp]]
