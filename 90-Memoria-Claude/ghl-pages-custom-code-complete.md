---
name: GHL Pages Custom Code — Guía Completa
description: HTML blocks, JavaScript, CSS, form handling, ejemplos para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# GHL Pages Custom Code — Guía Completa

## 1. Introducción a GHL Pages

GHL (GoHighLevel) es CRM + landing page builder. En Innovart se usa para:
- Landing `/home` (Bogotá)
- Funnel pages (home5, home4, etc.)
- Captura de leads vía formularios

**En Innovart:** GHL pages aceptan código custom en bloques específicos.

---

## 2. Acceso a GHL Pages

Desde GHL Dashboard:
```
Websites & Funnels → Pages → [Nombre Página] → Edit
```

O URL directa (reemplazar con tu account):
```
https://app.gohighlevel.com/account-settings/pages
```

---

## 3. Body Tracking Code — JavaScript Personalizado

En GHL, cada página tiene un campo "Body Tracking Code" donde inyectar JavaScript:

```javascript
<!-- Código de tracking e inicialización en GHL -->
<script>
  // ============================================
  // PHASE 1: Capturar UTMs y fbclid
  // ============================================
  
  function captureUTMs() {
    const params = new URLSearchParams(window.location.search);
    
    const utm_source = params.get('utm_source') || '';
    const utm_medium = params.get('utm_medium') || '';
    const utm_campaign = params.get('utm_campaign') || '';
    const utm_content = params.get('utm_content') || '';
    const utm_term = params.get('utm_term') || '';
    const fbclid = params.get('fbclid') || '';
    
    // Guardar en sessionStorage
    if (utm_source) sessionStorage.setItem('utm_source', utm_source);
    if (utm_medium) sessionStorage.setItem('utm_medium', utm_medium);
    if (utm_campaign) sessionStorage.setItem('utm_campaign', utm_campaign);
    if (utm_content) sessionStorage.setItem('utm_content', utm_content);
    if (utm_term) sessionStorage.setItem('utm_term', utm_term);
    if (fbclid) sessionStorage.setItem('fbclid', fbclid);
    
    console.log('UTMs captured:', { utm_source, utm_medium, utm_campaign, fbclid });
  }
  
  // ============================================
  // PHASE 2: Enriquecer formulario GHL
  // ============================================
  
  function enrichFormWithUTMs() {
    const formInputs = document.querySelectorAll('input, textarea');
    
    formInputs.forEach(input => {
      if (input.name === 'utm_source') {
        input.value = sessionStorage.getItem('utm_source') || '';
      }
      if (input.name === 'utm_medium') {
        input.value = sessionStorage.getItem('utm_medium') || '';
      }
      if (input.name === 'utm_campaign') {
        input.value = sessionStorage.getItem('utm_campaign') || '';
      }
      if (input.name === 'fbclid') {
        input.value = sessionStorage.getItem('fbclid') || '';
      }
    });
  }
  
  // ============================================
  // PHASE 3: Meta Pixel Tracking
  // ============================================
  
  function setupMetaPixelTracking() {
    if (typeof fbq !== 'undefined') {
      fbq('track', 'PageView');
      console.log('Meta Pixel PageView tracked');
      
      // Track cuando usuario hace submit
      const forms = document.querySelectorAll('form');
      forms.forEach(form => {
        form.addEventListener('submit', function() {
          fbq('track', 'Lead');
        });
      });
    }
  }
  
  // ============================================
  // PHASE 4: CAPI Event Tracking
  // ============================================
  
  function setupCAPITracking() {
    // Si la página envía eventos a CAPI, asegurarse que fbclid se incluya
    const originalSend = window.fetch;
    
    window.fetch = function(url, config) {
      if (url.includes('capi') || url.includes('webhook')) {
        const fbclid = sessionStorage.getItem('fbclid');
        
        if (config && config.body) {
          try {
            const body = JSON.parse(config.body);
            if (fbclid && !body.fbclid) {
              body.fbclid = fbclid;
              config.body = JSON.stringify(body);
            }
          } catch (e) {
            console.log('Could not enrich CAPI event');
          }
        }
      }
      
      return originalSend.apply(this, arguments);
    };
  }
  
  // ============================================
  // INITIALIZE
  // ============================================
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      captureUTMs();
      enrichFormWithUTMs();
      setupMetaPixelTracking();
      setupCAPITracking();
    });
  } else {
    captureUTMs();
    enrichFormWithUTMs();
    setupMetaPixelTracking();
    setupCAPITracking();
  }
</script>
```

---

## 4. Head Tracking Code — Meta Pixel + Clarity

En GHL, hay un campo "Head Tracking Code" para inyectar en `<head>`:

```html
<!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1642103999710262'); // ID del pixel
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=1642103999710262&ev=PageView&noscript=1"
/></noscript>

<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "x62cig8qug");
</script>

<!-- fbclid Capture -->
<script>
  function captureFbclid() {
    const params = new URLSearchParams(window.location.search);
    const fbclid = params.get('fbclid');
    if (fbclid) {
      sessionStorage.setItem('fbclid', fbclid);
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', captureFbclid);
  } else {
    captureFbclid();
  }
</script>
```

---

## 5. Custom HTML Block en GHL

Agregar bloque custom (no formulario, no imagen, sino HTML libre):

```html
<div class="ghl-custom-section">
  <h2>Custom Section Title</h2>
  <p>Custom content here</p>
  <ul>
    <li>Benefit 1</li>
    <li>Benefit 2</li>
    <li>Benefit 3</li>
  </ul>
</div>

<style>
  .ghl-custom-section {
    padding: 40px 20px;
    background: #f0f0f0;
    border-radius: 8px;
    margin: 20px 0;
  }
  
  .ghl-custom-section h2 {
    color: #333;
    margin-bottom: 15px;
  }
  
  .ghl-custom-section ul {
    list-style: none;
    padding: 0;
  }
  
  .ghl-custom-section li {
    padding: 8px 0;
    color: #666;
  }
  
  .ghl-custom-section li:before {
    content: "✓ ";
    color: #0066cc;
    font-weight: bold;
    margin-right: 8px;
  }
</style>
```

---

## 6. Form Handling Personalizado

En GHL, interceptar submit de formulario:

```javascript
<script>
  // Esperar a que GHL cargue sus scripts
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupFormHandler);
  } else {
    setupFormHandler();
  }
  
  function setupFormHandler() {
    const form = document.querySelector('form');
    
    if (!form) {
      console.log('No form found');
      return;
    }
    
    // Interceptar submit
    form.addEventListener('submit', function(e) {
      const formData = new FormData(form);
      
      // Agregar datos adicionales
      formData.append('utm_source', sessionStorage.getItem('utm_source') || '');
      formData.append('utm_medium', sessionStorage.getItem('utm_medium') || '');
      formData.append('fbclid', sessionStorage.getItem('fbclid') || '');
      formData.append('page_url', window.location.href);
      formData.append('timestamp', new Date().toISOString());
      
      console.log('Form submitted with enriched data');
      
      // Log antes de enviar
      for (let [key, value] of formData.entries()) {
        console.log(`${key}: ${value}`);
      }
    });
  }
</script>
```

---

## 7. Sticky Header con CTA

```html
<style>
  .ghl-sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: #0066cc;
    color: white;
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .ghl-sticky-header h3 {
    margin: 0;
    font-size: 18px;
  }
  
  .ghl-sticky-header button {
    background: white;
    color: #0066cc;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
    font-size: 14px;
  }
  
  .ghl-sticky-header button:hover {
    background: #f0f0f0;
  }
  
  body {
    padding-top: 60px; /* Make room for sticky header */
  }
</style>

<div class="ghl-sticky-header">
  <h3>Free Consultation</h3>
  <button onclick="scrollToForm()">Book Now</button>
</div>

<script>
  function scrollToForm() {
    const form = document.querySelector('form');
    if (form) {
      form.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>
```

---

## 8. Validación de Formulario GHL

```javascript
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    if (!form) return;
    
    // Validación personalizada antes de submit
    form.addEventListener('submit', function(e) {
      const email = form.querySelector('input[type="email"]');
      const phone = form.querySelector('input[type="tel"]');
      
      // Validar email
      if (email && !isValidEmail(email.value)) {
        e.preventDefault();
        showError('Please enter a valid email');
        return false;
      }
      
      // Validar teléfono (al menos 10 dígitos)
      if (phone) {
        const phoneDigits = phone.value.replace(/\D/g, '');
        if (phoneDigits.length < 10) {
          e.preventDefault();
          showError('Please enter a valid phone number');
          return false;
        }
      }
      
      // Si todo es válido, permitir submit
      return true;
    });
    
    function isValidEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
    
    function showError(message) {
      const errorDiv = document.createElement('div');
      errorDiv.textContent = message;
      errorDiv.style.cssText = 'color: red; padding: 10px; background: #ffe0e0; border-radius: 4px; margin: 10px 0;';
      form.insertBefore(errorDiv, form.firstChild);
      
      setTimeout(() => errorDiv.remove(), 5000);
    }
  });
</script>
```

---

## 9. WhatsApp CTA in GHL

```html
<div class="ghl-whatsapp-cta">
  <a href="https://wa.me/573101234567?text=Hola,%20me%20interesa%20saber%20más%20sobre%20los%20servicios" 
     target="_blank"
     class="whatsapp-button">
    <span>💬 Chat on WhatsApp</span>
  </a>
</div>

<style>
  .ghl-whatsapp-cta {
    text-align: center;
    padding: 20px 0;
  }
  
  .whatsapp-button {
    display: inline-block;
    background: #25d366;
    color: white;
    padding: 14px 28px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }
  
  .whatsapp-button:hover {
    background: #1faa52;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }
</style>

<script>
  document.querySelector('.whatsapp-button').addEventListener('click', function() {
    // Track click en Meta Pixel
    if (typeof fbq !== 'undefined') {
      fbq('track', 'Contact');
    }
  });
</script>
```

---

## 10. Countdown Timer GHL

```html
<div class="ghl-countdown">
  <h3>Limited Time Offer</h3>
  <div class="timer">
    <div class="time-unit">
      <span id="days">0</span>
      <p>Days</p>
    </div>
    <div class="time-unit">
      <span id="hours">0</span>
      <p>Hours</p>
    </div>
    <div class="time-unit">
      <span id="minutes">0</span>
      <p>Minutes</p>
    </div>
    <div class="time-unit">
      <span id="seconds">0</span>
      <p>Seconds</p>
    </div>
  </div>
</div>

<style>
  .ghl-countdown {
    background: #fff3cd;
    padding: 30px;
    border-radius: 8px;
    text-align: center;
    margin: 20px 0;
  }
  
  .timer {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .time-unit {
    background: white;
    padding: 15px 20px;
    border-radius: 8px;
    min-width: 80px;
  }
  
  .time-unit span {
    display: block;
    font-size: 32px;
    font-weight: bold;
    color: #d63031;
  }
  
  .time-unit p {
    margin: 5px 0 0 0;
    font-size: 12px;
    color: #666;
  }
</style>

<script>
  function updateCountdown() {
    // Reemplazar con fecha real
    const endDate = new Date('2026-12-31').getTime();
    const now = new Date().getTime();
    const distance = endDate - now;
    
    if (distance < 0) {
      document.querySelector('.ghl-countdown').innerHTML = '<p>Offer ended</p>';
      return;
    }
    
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    document.getElementById('days').textContent = days;
    document.getElementById('hours').textContent = hours;
    document.getElementById('minutes').textContent = minutes;
    document.getElementById('seconds').textContent = seconds;
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      updateCountdown();
      setInterval(updateCountdown, 1000);
    });
  } else {
    updateCountdown();
    setInterval(updateCountdown, 1000);
  }
</script>
```

---

## 11. Image Gallery GHL

```html
<div class="ghl-gallery">
  <div class="gallery-main">
    <img id="gallery-main-image" src="https://via.placeholder.com/600x400" alt="Main">
  </div>
  <div class="gallery-thumbnails">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 1" onclick="changeImage(this)">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 2" onclick="changeImage(this)">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 3" onclick="changeImage(this)">
  </div>
</div>

<style>
  .ghl-gallery {
    max-width: 600px;
    margin: 40px auto;
  }
  
  .gallery-main {
    margin-bottom: 20px;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .gallery-main img {
    width: 100%;
    height: auto;
    display: block;
  }
  
  .gallery-thumbnails {
    display: flex;
    gap: 10px;
    justify-content: center;
  }
  
  .gallery-thumbnails img {
    width: 80px;
    height: 80px;
    cursor: pointer;
    border: 2px solid transparent;
    border-radius: 4px;
    transition: border-color 0.3s;
  }
  
  .gallery-thumbnails img:hover,
  .gallery-thumbnails img.active {
    border-color: #0066cc;
  }
</style>

<script>
  function changeImage(thumb) {
    const mainImage = document.getElementById('gallery-main-image');
    mainImage.src = thumb.src.replace('80x80', '600x400');
    
    // Marcar como activo
    document.querySelectorAll('.gallery-thumbnails img').forEach(img => {
      img.classList.remove('active');
    });
    thumb.classList.add('active');
  }
  
  // Marcar primera como activa
  document.addEventListener('DOMContentLoaded', function() {
    const firstThumb = document.querySelector('.gallery-thumbnails img');
    if (firstThumb) firstThumb.classList.add('active');
  });
</script>
```

---

## 12. Modal Popup GHL

```html
<button class="ghl-modal-trigger">Open Modal</button>

<div id="ghl-modal" class="ghl-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <h2>Special Offer</h2>
    <p>Limited time offer. Get 20% off today!</p>
    <button class="modal-cta">Claim Offer</button>
  </div>
</div>

<style>
  .ghl-modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    align-items: center;
    justify-content: center;
  }
  
  .ghl-modal.active {
    display: flex;
  }
  
  .modal-content {
    background: white;
    padding: 40px;
    border-radius: 8px;
    max-width: 500px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    animation: slideIn 0.3s ease;
  }
  
  @keyframes slideIn {
    from { transform: translateY(-50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  
  .close {
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    color: #999;
  }
  
  .close:hover {
    color: #333;
  }
  
  .modal-cta {
    background: #0066cc;
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    margin-top: 20px;
  }
  
  .modal-cta:hover {
    background: #0052a3;
  }
</style>

<script>
  const modal = document.getElementById('ghl-modal');
  const trigger = document.querySelector('.ghl-modal-trigger');
  const closeBtn = document.querySelector('.close');
  
  trigger.addEventListener('click', () => modal.classList.add('active'));
  closeBtn.addEventListener('click', () => modal.classList.remove('active'));
  
  window.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
    }
  });
</script>
```

---

## 13. Gotchas en GHL

### Problema: Body Tracking Code se ejecuta múltiples veces

**Causa:** GHL puede reinicializar el DOM.

**Solución:**

```javascript
if (window.ghlInitialized) return;
window.ghlInitialized = true;

// Tu código aquí
```

### Problema: Formulario no envía

**Causa:** GHL requiere campos específicos.

**Solución:** Verificar que el formulario tenga los campos requeridos en GHL settings.

### Problema: fbclid no se captura

**Causa:** Script de captura no se ejecutó a tiempo.

**Solución:** Usar `DOMContentLoaded` y sessionStorage como backup.

---

## 14. GHL vs PageFly vs GemPages

| Aspecto | GHL | PageFly | GemPages |
|---------|-----|---------|----------|
| CRM Integración | ✅ Nativa | ❌ API | ❌ API |
| Landing /home | ✅ Usar | ⭐⭐⭐ | ⭐⭐ |
| Landings ciudad | ❌ No | ✅ Usar | ❌ No |
| Form Handling | ✅⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Custom Code | ✅ Fácil | ✅ Fácil | ✅ Fácil |

---

## 15. Recursos Oficiales

- [GHL Documentation](https://docs.gohighlevel.com/)
- [GHL Pages Guide](https://help.gohighlevel.com/article/36-pages)
- [GHL Tracking Code](https://help.gohighlevel.com/article/119-conversion-tracking)

