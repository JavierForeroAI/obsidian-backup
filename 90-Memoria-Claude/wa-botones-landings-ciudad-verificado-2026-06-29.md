---
name: wa-botones-landings-ciudad-verificado-2026-06-29
description: Verificación completa E2E — botones WA y formularios Qikify en página principal + 4 landings de ciudad. Todo funcionando con sufijo UTM.
metadata:
  type: project
  fecha: 2026-06-29
  status: COMPLETADO
---

# WA Buttons + Formularios — Verificación E2E (29 jun 2026)

## Resultado

| Página | Botones WA | Sufijo UTM | Formulario |
|---|---|---|---|
| `innovartmedical.com/` | 9 | `[fb/rtg]` ✅ | Qikify popup ✅ |
| `/pages/implante-capilar-bogota` | 9 | `[fb/rtg]` ✅ | Qikify popup ✅ |
| `/pages/implante-capilar-medellin` | 9 | `[fb/rtg]` ✅ | Qikify popup ✅ |
| `/pages/implante-capilar-barranquilla` | 9 | `[fb/rtg]` ✅ | Qikify popup ✅ |
| `/pages/implante-capilar-bucaramanga` | 9 | `[fb/rtg]` ✅ | Qikify popup ✅ |

## Qué se cambió para lograrlo

**Archivo:** `layout/theme.pagefly.liquid` (tema Dawn — GEO IA Innovart, ID 181331001645)

**Cambio:** Se reemplazó el mecanismo de enriquecimiento WA de `function enrich()` + MutationObserver (se apagaba a los 8s, frágil con React/PageFly) por un **click interceptor** en capture phase:

```javascript
document.addEventListener('click', function(e) {
  var el = e.target.closest('a[href*="wa.me"]');
  if (!el || !sfx) return;
  try {
    var url = new URL(el.href);
    var txt = decodeURIComponent(url.searchParams.get('text') || '');
    if (txt.indexOf('[') === -1) {
      url.searchParams.set('text', txt + sfx);
      e.preventDefault();
      e.stopImmediatePropagation();
      window.open(url.toString(), '_blank');
    }
  } catch(ee) {}
}, true); // capture:true = corre antes que cualquier handler de PageFly
```

**Por qué es mejor:** El sufijo se calcula en el momento del clic desde `window.location.search` — no depende del timing de React ni de observers. Funciona siempre sin importar cuántas veces PageFly re-renderice.

## Lo que NO se tocó
- Qikify → GHL v3 script (ruteado por sede vía Cloudflare Worker) — intacto
- UTM Capture script en `<head>` — intacto
- `theme.liquid` (páginas no-PageFly) — no se tocó
- Contenido de PageFly en cada ciudad — no se tocó

## Número WA en todas las páginas
Todas usan `573124565014` (CRM principal AppLevel).
Si se quiere número específico por sede, es un cambio manual en PageFly por página.

## Formato del sufijo
- `utm_source=facebook` + `utm_medium=retargeting` → `[fb/rtg]`
- `utm_source=instagram` + `utm_medium=paid_social` → `[ig/paid]`
- Sin UTMs → sin sufijo (tráfico directo no se marca)
