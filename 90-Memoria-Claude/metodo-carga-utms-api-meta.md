---
name: metodo-carga-utms-api-meta
description: Cómo cargar UTMs (url_tags) en ads de Meta por API + app meta-dajf ahora en modo Live
metadata:
  type: project
---

# Carga de UTMs en ads de Meta por API (método verificado)

**2026-06-18.** Primera carga real de UTMs por API en Innovart. Campaña **"Trafico a web RM (Fase 2)"** (cuenta **LANDING DIEGO** `act_1176352666815422`, COP) — campaña ACTIVE/gastando (~600K COP/30d), no apagada como se creía. Se cargaron UTMs en los **5 ads web**; el 6º ("v2-Landing - ABRIL 1") es **DM/click-to-message** (`INSTAGRAM_MESSAGE`, sin URL) y NO lleva UTM de URL → se trackea por `ctwa_clid`. Ver protocolo en `~/skills/user/protocolo-utm-innovart.md`.

## App meta-dajf AHORA en modo Live
- La app detrás del MCP `meta-dajf` es **"CLAUDE CODE DA-JF"**, App ID **`1698932398019234`**, Business `940287337027000`. Javier es admin.
- **Se pasó de Desarrollo → Live el 2026-06-18** (developers.facebook.com → app → "Publicar" → botón azul Publicar). Permisos completos (`ads_management`, etc.).
- **Por qué importa:** en modo Desarrollo Meta bloquea crear publicaciones publicitarias nuevas (error subcode `1885183`). En Live ya se pueden **crear/recrear creativos por API**. Esto habilita futuras ediciones de creativos, no solo lectura.

## Método para añadir url_tags sin perder el creativo
Meta NO deja editar `url_tags` in-place (creativos inmutables). Hay que **recrear el creativo + reasignarlo al mismo ad_id**:
1. GET creativo completo: `object_story_spec, asset_feed_spec, degrees_of_freedom_spec, contextual_multi_ads, effective_object_story_id`.
2. POST `/{act}/adcreatives` reusando esos specs + `url_tags`. **Limpiezas obligatorias:**
   - Quitar `standard_enhancements` de `degrees_of_freedom_spec.creative_features_spec` (deprecado → error subcode `3858504`).
   - Quitar `thumbnail_url` de cada video en `asset_feed_spec.videos` y `image_url` de `object_story_spec.video_data/link_data` (URLs firmadas, usar `image_hash`).
3. POST `/{ad_id}` con `creative={"creative_id": nuevo}`.
4. Verificar `creative{url_tags, asset_feed_spec}`.
- **Consecuencia inevitable (cualquier método):** cambiar el creativo deja el ad en PENDING_REVIEW/IN_PROCESS y **reinicia aprendizaje**; vuelve a ACTIVE al aprobar. NO cambia el on/off del ad.
- **Alternativa en modo Desarrollo** (si la app no estuviera Live): crear creativo con `object_story_id`=post existente + `url_tags` — funciona pero **aplana** el dinámico (pierde `asset_feed_spec`). Evitar si se puede usar Live.
- Script reutilizable: `/tmp/apply_utms.py` (+ `find_rm_campaign.py`, `dump_creatives.py`). Rollback con creative_id originales en `/tmp/rm_rollback.json`.

## UTM aplicado (formato del protocolo oficial)
`utm_source=facebook&utm_medium=remarketing&utm_campaign=nacional-retargeting-feb2026&utm_term=remarketing-web&utm_content=video-landing-feb-vN`
(uno por pieza: v2..v6). `utm_campaign` = ciudad-objetivo-mesaño; aquí nacional + retargeting + feb2026 (mes de lanzamiento de la campaña).

Relacionado: [[reporte-utm-junio-2026]] · [[meta-mcp-guia]] · [[feedback-cuentas-meta-no-son-sedes]]
