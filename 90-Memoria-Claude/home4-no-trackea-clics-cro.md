---
name: home4-no-trackea-clics-cro
description: Por qué Clarity no registró NINGÚN clic en la landing /home4 (form en iframe GHL = ciego, CTAs enterrados, sticky-bar vacío, color CTA = marca) y los cambios estructurales P0 para arreglarlo
metadata:
  type: project
---

# /home4: por qué Clarity no trackeó clics + fixes P0

**Fecha:** 2026-06-19. Landing `https://implantecapilarencolombia.com/home4` (218 KB HTML).
Complementa el diagnóstico de calor/scroll [[Informe-Clarity-home4-2026-06-18.html]] (que ya
explica el "no convierte"). Esta nota responde la pregunta puntual de Javier: **"¿por qué no
trackeó NADA de clics?"** — y NO es que la gente no haga clic, son causas técnicas + de
estructura.

## Por qué Clarity mostró 0 clics
1. **El formulario vive en un iframe cross-origin de GoHighLevel**
   (`api.leadconnectorhq.com/widget/form/6aGxlY1gdbBx3vQA7XR9`). **Clarity es CIEGO dentro de
   un iframe de otro dominio** → no ve campos, ni el botón Enviar, ni los clics. La acción más
   importante de la página es 100% invisible en los heatmaps. (Por eso la analítica del form
   se mide con la **nativa de GHL**, no con Clarity.)
2. **El form está al 100% de profundidad** (última sección) y solo lo alcanza el **3.6%**
   (24 de 673). Los **9 botones CTA** hacen *scroll suave hasta ese form del fondo*: hay tan
   pocos clics repartidos entre 9 botones enterrados que Clarity no dibuja punto caliente.
3. **El `<div class="sticky-bar">` está VACÍO:** reserva 88px abajo en móvil pero **no tiene
   botón** (no se llena por JS). No hay CTA persistente que capturar.

## Datos de scroll (Clarity, 12-18 jun, móvil)
| Profundidad | % tráfico |
|---|---|
| 5% (inicio) | 80.8% |
| 10% | 35% ← se cae el 56% aquí |
| 50% | 12.9% |
| **100% (el form)** | **3.6%** |

El video 9:16 del hero **empuja el H1 y el CTA por debajo del fold** (orden DOM móvil:
info-card → video → recién H1+sub+CTA). El usuario ve un video mudo antes que la promesa y el
botón → de ahí el desplome al 10%.

## Cambios P0 (lo que está sangrando conversión)
1. **Subir el formulario/captura corta al hero** (nombre + WhatsApp + "¿zona a tratar?"). No
   puede empezar al final.
2. **Llenar la barra fija inferior** (hoy vacía) con un botón persistente dividido:
   "📲 WhatsApp" + "Ver si califico". Rescata al 56% que se va antes del 10%.
3. **Bajar el video del hero**: headline + sub + botón visibles sin scrollear; video más
   pequeño o secundario.
4. **Color de acción único para el CTA.** Hoy el botón usa el mismo teal/azul de marca que
   está en TODO (badges, checks, precio, dots, los 9 CTAs) → **banner blindness cromática**.
   `.cta-btn{background:var(--gradient);color:#000;…}`. Reservar un color exclusivo de "aquí
   se hace clic", más grande y con halo/sombra.

**P1:** subir contraste de textos secundarios (`#6a6a6a`/`#9a9a9a` sobre negro fallan AA → mín
`#b0b0b0`); reducir fricción del form (medirlo con analítica GHL, no Clarity, por el iframe).

## Cómo se hizo
Inspección del HTML real + cruce con los 2 exports de Clarity (Attention/Scroll móvil) +
auditoría multi-agente de 6 lentes (dirección de arte/UX, comunicación, carga, compliance
médico, estrategia CRO, medición). El hallazgo de marca: assets fotográficos usan navy+azul
cielo+blanco mientras el sitio usa teal+azure sobre negro (inconsistencia).

> ⚠️ Distinto al Home de Shopify (innovartmedical.com). Esta `/home4` es una landing aparte en
> `implantecapilarencolombia.com`; su ruteo de leads en GHL está en [[landing-home4-routing]].

## Actualización 2026-06-20 — auditoría multi-agente (home4 + home5)
Una auditoría multi-agente que leyó el **código real** de la página destapó dos cosas que
NO se veían solo con Clarity y que cambian el diagnóstico:

1. **El video del hero pesa ~217 MB y arranca solo** (confirmado: 227.640.696 bytes + un
   `v.play()` automático a los ~2 s; la página entera tiene ~605 MB de video). El "1:50 min
   pegados arriba" NO es interés: es la gente **esperando que cargue el video** en datos
   móviles → esa es la causa real del desplome 5%→10% (se va el 56%). Comprimir a 1.5–3 MB y
   que **no** autoarranque es el fix #1.
2. **El evento `Lead` de Meta está inflado y no es confiable.** No se dispara con el envío del
   formulario: se dispara con un mensaje interno de LeadConnector (`set-sticky-contacts`,
   persistencia de cookie) **y además en cada clic de WhatsApp**. O sea: las campañas se vienen
   optimizando hacia un número que NO significa "lead real". Hasta moverlo al envío real del
   form (vía GHL + CAPI) **ningún reporte ni test de Meta es de fiar** en esta landing.

**Páginas / IDs (subcuenta GHL Bogotá `DgjjDzD9nkCKv8AGF1Qb`, funnel "Landing 1 Home"
`6gDZimr1JRoW9iQZZnRH`):**
- `home4` = **LIVE, no tocar** → page `PaBAMA8f6ISzy4H3HHty`.
- `home5` = **página de prueba** donde se trabajan las mejoras → page `F6xTmSqYRLizoZ1SJmDg`.
- Clarity ID del funnel: `x62cig8qug`. Este funnel tiene la versión **básica** del script de
  Meta; el funnel `DC-BOGOTA` ya tiene la **avanzada** (`lead_event_id` + dedup de `fbq Lead`)
  → replicarla aquí entra al plan de tracking.

> Método de edición seguro de home5: inyectar una capa de optimización compacta vía
> `update_funnel` (`bodyTrackingCode`, que mergea y preserva el `headTrackingCode`), scopeada
> con guard de `/home5`, **sin reescribir** los ~78 KB de custom-code. El MCP de GHL **no** tiene
> herramienta para subir media (la compresión del video se hace fuera). ⚠️ Persistencia de
> `update_page_content` aún no resuelta del todo — ver [[feedback-mcp-ghl-update-page]].

Relacionado: [[landing-home4-routing]] · [[clarity-mcp-microsoft]] · [[feedback_fbclid_landing_pages]] · [[estrategia-meta-showrate-valoraciones]]
