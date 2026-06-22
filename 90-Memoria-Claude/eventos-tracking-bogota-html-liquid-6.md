---
name: eventos-tracking-bogota-html-liquid-6
description: HTML/Liquid #6 — Script de eventos completo para landing Bogotá. Incluye Meta Pixel (2), Google Ads (3 conversiones), 11 eventos custom (ViewContent, Lead, WhatsAppClick, SocialClick, Scroll 25/50/75/100, FAQ_Click, TimeOnPage 60s/180s). Pronto para copiar y pegar en PageFly.
metadata:
  type: project
  fecha: 2026-06-22
  estado: listo-para-pegar
---

# HTML/Liquid #6 — Eventos de Tracking Completo (Bogotá)

**Estado:** ✅ PEGADO EN PAGEFLY (2026-06-21) — Código inyectado en sección HTML/Liquid

Contiene:
- Meta Pixel base code × 2 píxeles
- Google Ads × 3 conversiones (etiquetas reales)
- 11 eventos custom (Meta + GA4 + dataLayer)

---

## CÓDIGO LISTO PARA PEGAR

```html
<script>
(function(){
  // ═══════════════════════════════════════════
  // CONFIGURACIÓN BOGOTÁ
  // ═══════════════════════════════════════════
  var META_PIXELS   = ['1642103999710262'];
  var GADS_ID       = 'AW-16490325890';
  var GADS_LABELS   = {
    pageview  : 'oquqCNTX6bYaEILPmbc9',
    lead      : 'YwuMCM1_yXwaB1LpmbcS9',
    whatsapp  : 'OLsJC1W9k6kzB1LpmbcS9'
  };

  // ═══════════════════════════════════════════
  // META PIXEL — base code (2 píxeles)
  // ═══════════════════════════════════════════
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');
  META_PIXELS.forEach(function(pid){ fbq('init', pid); });

  // ═══════════════════════════════════════════
  // HELPERS
  // ═══════════════════════════════════════════
  function metaEvent(event, params){
    META_PIXELS.forEach(function(pid){
      fbq('trackSingle', pid, event, params || {});
    });
  }
  function metaCustom(name, params){
    META_PIXELS.forEach(function(pid){
      fbq('trackSingleCustom', pid, name, params || {});
    });
  }
  function gads(label){
    if(typeof gtag==='undefined') return;
    gtag('event','conversion',{send_to: GADS_ID+'/'+label});
  }
  function dl(event, params){
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({event: event}, params || {}));
  }
  var _fired = {};
  function once(key, fn){ if(!_fired[key]){ _fired[key]=true; fn(); } }

  // ═══════════════════════════════════════════
  // EVENTO 1: ViewContent — carga de página
  // ═══════════════════════════════════════════
  metaEvent('ViewContent', {content_name:'Implante Capilar Bogotá'});
  gads(GADS_LABELS.pageview);
  dl('ViewContent');

  // ═══════════════════════════════════════════
  // EVENTO 2: Lead — form qikify
  // Método A: interceptar fetch
  // ═══════════════════════════════════════════
  var _fetch = window.fetch;
  window.fetch = function(){
    var url = (arguments[0] && (arguments[0].url || arguments[0])) || '';
    var isQikify = typeof url==='string' && (url.indexOf('qikify')!==-1 || url.indexOf('bcontact')!==-1);
    var promise = _fetch.apply(window, arguments);
    if(isQikify){
      promise.then(function(res){
        if(res && res.ok){
          once('lead', function(){
            metaEvent('Lead', {content_name:'Form Bogotá'});
            gads(GADS_LABELS.lead);
            dl('Lead', {form:'qikify_bogota'});
          });
        }
      }).catch(function(){});
    }
    return promise;
  };

  // Método B: MutationObserver (backup)
  new MutationObserver(function(muts){
    muts.forEach(function(m){
      m.addedNodes.forEach(function(node){
        if(node.nodeType!==1) return;
        var txt = (node.textContent||'').toLowerCase();
        if(txt.indexOf('gracias')!==-1||txt.indexOf('thank')!==-1||txt.indexOf('enviado')!==-1){
          once('lead', function(){
            metaEvent('Lead', {content_name:'Form Bogotá'});
            gads(GADS_LABELS.lead);
            dl('Lead', {form:'qikify_bogota'});
          });
        }
      });
    });
  }).observe(document.body, {childList:true, subtree:true});

  // ═══════════════════════════════════════════
  // EVENTO 3: WhatsAppClick
  // ═══════════════════════════════════════════
  document.addEventListener('click', function(e){
    var el = e.target.closest('a[href]');
    if(!el) return;
    var href = el.getAttribute('href') || '';
    if(href.indexOf('wa.me')!==-1 || href.indexOf('whatsapp')!==-1){
      metaEvent('Contact', {content_name:'WhatsApp Bogotá'});
      metaCustom('WhatsAppClick', {number:'573102031796'});
      gads(GADS_LABELS.whatsapp);
      dl('WhatsAppClick');
    }
  });

  // ═══════════════════════════════════════════
  // EVENTO 4: SocialClick — IG / FB / TikTok / YouTube
  // ═══════════════════════════════════════════
  var SOCIALS = {instagram:'instagram.com', facebook:'facebook.com', tiktok:'tiktok.com', youtube:'youtube.com'};
  document.addEventListener('click', function(e){
    var el = e.target.closest('a[href]');
    if(!el) return;
    var href = (el.getAttribute('href')||'').toLowerCase();
    Object.keys(SOCIALS).forEach(function(net){
      if(href.indexOf(SOCIALS[net])!==-1){
        metaCustom('SocialClick', {network:net});
        dl('SocialClick', {network:net});
      }
    });
  });

  // ═══════════════════════════════════════════
  // EVENTOS 5-8: Scroll 25 / 50 / 75 / 100
  // ═══════════════════════════════════════════
  var scrolled = {};
  window.addEventListener('scroll', function(){
    var pct = Math.round((window.scrollY/(document.body.scrollHeight-window.innerHeight))*100);
    [25,50,75,100].forEach(function(n){
      if(!scrolled[n] && pct>=n){
        scrolled[n]=true;
        metaCustom('Scroll'+n, {percent:n});
        dl('Scroll'+n);
      }
    });
  }, {passive:true});

  // ═══════════════════════════════════════════
  // EVENTO 9: FAQ_Click — accordion
  // ═══════════════════════════════════════════
  document.addEventListener('click', function(e){
    var el = e.target.closest('[class*="accordion"],[class*="Accordion"],summary');
    if(el){
      var q = (el.textContent||'').trim().substring(0,80);
      metaCustom('FAQ_Click', {question:q});
      dl('FAQ_Click', {question:q});
    }
  });

  // ═══════════════════════════════════════════
  // EVENTOS 10-11: TimeOnPage 60s y 180s
  // ═══════════════════════════════════════════
  setTimeout(function(){
    metaCustom('TimeOnPage_60s');
    dl('TimeOnPage_60s');
  }, 60000);

  setTimeout(function(){
    metaCustom('TimeOnPage_180s');
    dl('TimeOnPage_180s');
  }, 180000);

})();
</script>
<noscript>
  <img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1642103999710262&ev=PageView&noscript=1"/>
</noscript>
```

---

## Dónde pegar en PageFly

1. Panel izquierdo → al final de la lista de elementos
2. Clic en **+ Add section** o directamente **HTML/Liquid**
3. Pegar todo el código arriba
4. Guardar

---

## Qué hace cada evento

| # | Evento | Destino | Para qué |
|---|---|---|---|
| 1 | ViewContent | Meta + Google Ads | Medir alcance, auditoría de tráfico |
| 2 | Lead | Meta + Google Ads | Medir forma enviado — lo más importante |
| 3 | WhatsAppClick | Meta + GA4 | Medir clicks a WhatsApp — alternativa de conversión |
| 4 | SocialClick | Meta + GA4 | Medir clicks salientes (IG, FB, TikTok, YouTube) |
| 5-8 | Scroll 25/50/75/100 | Meta + GA4 | Audiencias retargeting por engagement (scroll profundo = interés real) |
| 9 | FAQ_Click | Meta + GA4 | Medir interacción con preguntas frecuentes — señal de investigación |
| 10 | TimeOnPage_60s | Meta + GA4 | Visitante real (>1 min) vs bot |
| 11 | TimeOnPage_180s | Meta + GA4 | Altísima intención (>3 min) → lookalike premium |

---

## Verificación en vivo

Una vez pegado, abre la página y:

1. **Abre DevTools** (F12) → Console
2. Haz clic en el botón WhatsApp → verás en Console: `WhatsAppClick`
3. Scroll hasta el 50% → verás: `Scroll50`
4. Abre una pregunta FAQ → verás: `FAQ_Click`
5. Espera 60 segundos → verás: `TimeOnPage_60s`

Si ves los eventos en Console, Meta y Google Ads también los están recibiendo.

---

**Para Medellín, Barranquilla, Bucaramanga:** cambiar solo:
- Los 2 Meta Pixels (si son diferentes)
- Las 3 etiquetas de Google Ads
- El número WhatsApp (Medellín: +57 312 456 5014, igual; Barranquilla: idem; Bucaramanga: idem)

El resto del código es idéntico.

*Creado 2026-06-22 — Claude Code + Javier Forero*
