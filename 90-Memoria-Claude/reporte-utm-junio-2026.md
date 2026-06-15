---
name: reporte-utm-junio-2026
description: Auditoría UTM junio 2026 — 176 anuncios activos, 0% cobertura, reporte enviado a Esneider
metadata:
  type: project
---

# Auditoría UTM — Junio 2026

## Hallazgo principal

**176 anuncios activos en 6 cuentas Meta Ads, 0 con UTMs configurados.** GHL Medellín tiene todos los campos listos pero vacíos.

**Why:** Se perdió la configuración de URL Parameters en Meta Ads Manager en algún momento posterior a enero 2026. El sistema sí funcionó antes (evidencia: contacto "esneider lopez" en GHL con UTMs completos de ene-2026).

**How to apply:** Cuando se hable de tracking, atribución de creativos o decisiones de pauta, recordar que actualmente NO hay datos de atribución llegando al CRM.

---

## Estado por cuenta (snapshot 12 junio 2026)

| Cuenta | Ads | Destino | Prioridad |
|--------|-----|---------|-----------|
| MEDELLIN | 105 | WhatsApp / DM IG | Alta |
| BGTA | 25 | WhatsApp 100% | Alta |
| PANAMA | 21 | DM IG / Web | Media |
| LANDING DIEGO | 19 | Web + WA + Perfil IG | Media-Alta |
| Artes y Bronces | 4 | E-commerce / Web | Media |
| QUILLA | 2 | Web / WhatsApp | Baja |

## Distribución de destinos

- 54 ads → Engagement (sin URL)
- 47 ads → WhatsApp Message
- 37 ads → DM Instagram
- 14 ads → Perfil IG
- 12 ads → URL / Web ← **prioridad #1, deben tener UTM en URL**
- 12 ads → Catálogo dinámico

## Infraestructura GHL Medellín — campos confirmados listos

| Campo | GHL ID | Estado |
|-------|--------|--------|
| utm_campaign | EYtlSV5Zo5bIFMWrt7zd | Vacío |
| utm_content | fkLu6dW4S2Qq61NlM20J | Vacío |
| utm_medium | LBRvQTYSAxKyWSATOvOG | Vacío |
| utm_source | kLMdTD6z21PLsxOVccGh | Vacío |
| campaign_id | Xf5lds4uZSdapqo2Xyag | Vacío |
| ad_id | p4HuAUmR8ctd2sD8Irc9 | Vacío |
| ad_set_id | yXQW8JklyYWcHxLEwWB9 | Vacío |
| ctwa_clid | 4V2IZiwCCkLdt0jTUI8K | **Activo ✓** |

## Plantilla estándar de URL Parameters (Meta Ads Manager)

```
utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&campaign_id={{campaign.id}}&ad_id={{ad.id}}&adset_id={{adset.id}}
```

## Plan de acción

1. Configurar URL Parameters en MEDELLIN y BGTA (130 ads) — ~2-3h con edición masiva
2. Agregar UTMs a URL destino de los 12 anuncios web (LANDING DIEGO, MEDELLIN, QUILLA, PANAMA)
3. Verificar en GHL 24h después que los campos se llenan

## Entregables generados

- Reporte HTML: `/tmp/reporte_utm_innovart.html` (diseño calm/tranquil, 8 secciones)
- Google Sheet: ID `16fWeDP64RLDshvoyKb9D24ir1f-R0yiKLMK4PJaXfmA` — "Meta Ads Activos - Estado UTM Real 2026-06-12"
- Carpeta Drive: `10B8IXyGK8m-3Fr01-keT9RpA8kF_TdmB` (3. MERCADEO / CLAUDE / utm)
- Email enviado a Esneider (`esneidervc17@gmail.com`) — borrador Gmail `19ebe87ff665fc74` desde `innovartmedicalips@gmail.com`
