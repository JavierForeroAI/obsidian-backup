---
name: PageFly JavaScript Customization — Guía Completa
description: API, custom code blocks, embedding, tracking, ejemplos para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# PageFly JavaScript Customization — Guía Completa

## 1. Introducción a PageFly

PageFly es un constructor visual de landing pages para Shopify. Permite:
- Editar páginas sin código
- Inyectar HTML/CSS/JS personalizado
- Integración directa con Shopify

**En Innovart:** PageFly se usa para landings de ciudad (Bogotá, Medellín, Barranquilla, Bucaramanga).

---

## 2. Acceso a PageFly

Desde Shopify Admin:
```
Apps → PageFly → Dashboard → Edit Page
```

O URL directa (reemplazar con tu tienda):
```
https://innovartmedical.myshopify.com/admin/apps/pagefly/pages
```

---

## 3. Custom Code Block — HTML/CSS/JS

En PageFly, agregar un bloque "Custom Code":

```html
<div id="my-custom-block">
  <h2>Custom Heading</h2>
  <p>Custom paragraph</p>
  <button id="my-button">Click me</button>
</div>

<style>
  #my-custom-block {
    padding: 20px;
    background: #f5f5f5;
    border-radius: 8px;
  }
  
  #my-custom-block h2 {
    color: #333;
    margin-bottom: 10px;
  }
  
  #my-button {
    background: #0066cc;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  #my-button:hover {
    background: #0052a3;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('my-button');
    button.addEventListener('click', function() {
      alert('Button clicked!');
    });
  });
</script>
```

---

## 4. PageFly API — Acceso a Variables

PageFly expone variables globales accesibles:

```javascript
// Producto actual (si está en producto template)
if (typeof PageFly !== 'undefined' && PageFly.product) {
  console.log(PageFly.product.title);
  console.log(PageFly.product.price);
  console.log(PageFly.product.variants);
}

// Tienda
if (typeof PageFly !== 'undefined' && PageFly.shop) {
  console.log(PageFly.shop.name);
  console.log(PageFly.shop.currency);
}

// Customer (si está logueado)
if (typeof PageFly !== 'undefined' && PageFly.customer) {
  console.log(PageFly.customer.email);
  console.log(PageFly.customer.firstName);
}
```

---

## 5. Inyectar Qikify en PageFly

**Caso: Formulario de Qikify en landing de ciudad**

En Custom Code block:

```html
<!-- Qikify Contact Form Embed -->
<div id="qikify-form-container">
  <div contactform-embed="483316"></div>
</div>

<script>
  // Inyectar script de Qikify si no existe
  if (typeof window.Qikify === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://www.qikify.com/app/qikify.min.js';
    script.async = true;
    script.onload = function() {
      console.log('Qikify loaded');
      if (typeof window.BContact !== 'undefined') {
        console.log('BContact available');
      }
    };
    document.body.appendChild(script);
  }
</script>

<style>
  #qikify-form-container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
  }
</style>
```

---

## 6. Tracking — Meta Pixel en PageFly

Agregar Meta Pixel track en Custom Code:

```html
<script>
  // Meta Pixel - PageView
  if (typeof fbq !== 'undefined') {
    fbq('track', 'PageView');
    console.log('Meta Pixel PageView tracked');
  }
  
  // Track cuando usuario hace clic en botón
  document.addEventListener('DOMContentLoaded', function() {
    const ctaButton = document.querySelector('.cta-button');
    if (ctaButton) {
      ctaButton.addEventListener('click', function() {
        if (typeof fbq !== 'undefined') {
          fbq('track', 'Lead');
        }
      });
    }
  });
</script>
```

---

## 7. fbclid Capture en PageFly

Capturar y guardar `fbclid` para CAPI:

```html
<script>
  // Capturar fbclid y guardar en sessionStorage
  function captureFbclid() {
    const params = new URLSearchParams(window.location.search);
    const fbclid = params.get('fbclid');
    
    if (fbclid) {
      sessionStorage.setItem('fbclid', fbclid);
      console.log('fbclid captured:', fbclid);
    } else {
      const stored = sessionStorage.getItem('fbclid');
      if (stored) {
        console.log('fbclid from session:', stored);
      }
    }
  }
  
  // Ejecutar al cargar página
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', captureFbclid);
  } else {
    captureFbclid();
  }
</script>
```

---

## 8. Enriquecer Formulario Qikify con UTMs

Cuando usuario envía formulario de Qikify, agregar UTMs/fbclid:

```javascript
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Esperar a que Qikify esté listo
    if (typeof window.BContact !== 'undefined') {
      const originalSubmit = window.BContact.send;
      
      window.BContact.send = function(data) {
        // Capturar UTMs
        const params = new URLSearchParams(window.location.search);
        const utm_source = params.get('utm_source') || '';
        const utm_medium = params.get('utm_medium') || '';
        const utm_campaign = params.get('utm_campaign') || '';
        const fbclid = sessionStorage.getItem('fbclid') || '';
        
        // Agregar a payload
        data.utm_source = utm_source;
        data.utm_medium = utm_medium;
        data.utm_campaign = utm_campaign;
        data.fbclid = fbclid;
        
        // Enviar
        return originalSubmit(data);
      };
    }
  });
</script>
```

---

## 9. Validación de Formulario Personalizado

```html
<form id="custom-form">
  <input type="email" id="email" name="email" required placeholder="Email">
  <input type="tel" id="phone" name="phone" required placeholder="Phone">
  <input type="text" id="name" name="name" required placeholder="Name">
  <button type="submit">Submit</button>
  <div id="form-error" style="color: red; display: none;"></div>
</form>

<script>
  document.getElementById('custom-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const name = document.getElementById('name').value;
    const errorDiv = document.getElementById('form-error');
    
    // Validar email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      errorDiv.textContent = 'Invalid email';
      errorDiv.style.display = 'block';
      return;
    }
    
    // Validar teléfono (10+ dígitos)
    const phoneRegex = /\d{10,}/;
    if (!phoneRegex.test(phone.replace(/\D/g, ''))) {
      errorDiv.textContent = 'Invalid phone';
      errorDiv.style.display = 'block';
      return;
    }
    
    // Si es válido, enviar
    errorDiv.style.display = 'none';
    console.log('Form valid, submitting...', { email, phone, name });
    
    // Aquí enviar a servidor
  });
</script>

<style>
  #custom-form {
    max-width: 400px;
    margin: 20px auto;
  }
  
  #custom-form input {
    display: block;
    width: 100%;
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  #custom-form button {
    width: 100%;
    padding: 10px;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
</style>
```

---

## 10. Conditional Content (Mostrar/Ocultar)

```html
<div id="logged-in-content" style="display: none;">
  <p>Welcome back!</p>
</div>

<div id="guest-content">
  <p>Sign up for exclusive offers</p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Chequear si customer está logueado
    // En Shopify, esto está disponible en Liquid como {{ customer.id }}
    
    // Alternativa: verificar cookie
    const cookies = document.cookie;
    if (cookies.includes('customer_id')) {
      document.getElementById('guest-content').style.display = 'none';
      document.getElementById('logged-in-content').style.display = 'block';
    }
  });
</script>
```

---

## 11. Product Carousel en PageFly

```html
<div id="product-carousel">
  <div class="carousel-container">
    <div class="carousel-slide">
      <img src="https://example.com/product1.jpg" alt="Product 1">
      <h3>Product 1</h3>
      <p>$99.99</p>
    </div>
    <div class="carousel-slide">
      <img src="https://example.com/product2.jpg" alt="Product 2">
      <h3>Product 2</h3>
      <p>$149.99</p>
    </div>
  </div>
  <button class="carousel-prev">← Prev</button>
  <button class="carousel-next">Next →</button>
</div>

<style>
  #product-carousel {
    position: relative;
    max-width: 800px;
    margin: 40px auto;
  }
  
  .carousel-container {
    display: flex;
    gap: 20px;
    overflow: hidden;
    border-radius: 8px;
  }
  
  .carousel-slide {
    flex: 0 0 100%;
    text-align: center;
    padding: 20px;
    background: #f9f9f9;
    transition: opacity 0.3s;
  }
  
  .carousel-slide img {
    max-width: 100%;
    height: auto;
    margin-bottom: 15px;
  }
  
  .carousel-prev, .carousel-next {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0,0,0,0.5);
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 4px;
    z-index: 10;
  }
  
  .carousel-prev { left: 10px; }
  .carousel-next { right: 10px; }
</style>

<script>
  const carousel = document.querySelector('.carousel-container');
  const slides = document.querySelectorAll('.carousel-slide');
  let currentSlide = 0;
  
  function showSlide(n) {
    carousel.style.transform = `translateX(-${n * 100}%)`;
  }
  
  document.querySelector('.carousel-next').addEventListener('click', () => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  });
  
  document.querySelector('.carousel-prev').addEventListener('click', () => {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  });
</script>
```

---

## 12. Countdown Timer

```html
<div id="countdown-timer">
  <h2>Offer Ends In:</h2>
  <div class="timer">
    <span id="days">0</span>d <span id="hours">0</span>h 
    <span id="minutes">0</span>m <span id="seconds">0</span>s
  </div>
</div>

<style>
  #countdown-timer {
    text-align: center;
    padding: 20px;
    background: #fff3cd;
    border-radius: 8px;
    margin: 20px 0;
  }
  
  .timer {
    font-size: 24px;
    font-weight: bold;
    color: #d63031;
    margin-top: 10px;
  }
</style>

<script>
  function updateCountdown() {
    // Fecha final (reemplazar con fecha real)
    const endDate = new Date('2026-12-31').getTime();
    const now = new Date().getTime();
    const distance = endDate - now;
    
    if (distance < 0) {
      document.getElementById('countdown-timer').innerHTML = '<p>Offer ended</p>';
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
  
  updateCountdown();
  setInterval(updateCountdown, 1000);
</script>
```

---

## 13. WhatsApp Integration en PageFly

```html
<div id="whatsapp-cta">
  <a href="https://wa.me/573101234567?text=Hola,%20me%20interesa%20saber%20m%C3%A1s" 
     target="_blank"
     class="whatsapp-button">
    💬 Chat on WhatsApp
  </a>
</div>

<style>
  .whatsapp-button {
    display: inline-block;
    background: #25d366;
    color: white;
    padding: 12px 24px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    transition: background 0.3s;
  }
  
  .whatsapp-button:hover {
    background: #1faa52;
  }
</style>

<script>
  document.querySelector('.whatsapp-button').addEventListener('click', function() {
    if (typeof fbq !== 'undefined') {
      fbq('track', 'Contact');
    }
  });
</script>
```

---

## 14. Gotchas en PageFly

### Problema: Scripts no se cargan

**Solución:** Usar `DOMContentLoaded` y verificar que elementos existan:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const element = document.getElementById('my-element');
  if (element) {
    // Código seguro
  }
});
```

### Problema: Estilos conflictúan

**Solución:** Usar IDs y clases únicas + `!important`:

```css
#my-custom-block .button {
  background: #0066cc !important;
}
```

### Problema: Qikify no aparece

**Causa:** Script Qikify no se inyectó, o falta `</body>` en theme.liquid.

**Solución:** 
1. Verificar que theme.liquid tenga `</body>`
2. Inyectar script en Custom Code de PageFly (ver sección 5)

---

## 15. PageFly vs GemPages en Innovart

| Aspecto | PageFly | GemPages |
|---------|---------|----------|
| Landings de ciudad | ✅ Usar | ❌ No |
| Home (Panamá) | ❌ No | ✅ Usar |
| Facilidad | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| API Robusta | ✅ | ⭐⭐ |
| Qikify Integration | ✅ Fácil | ⚠️ Complicado |

---

## 16. Recursos Oficiales

- [PageFly Documentation](https://docs.pagefly.io/)
- [PageFly API Reference](https://docs.pagefly.io/api)
- [Shopify Liquid Reference](https://shopify.dev/api/liquid)
- [Meta Pixel Events](https://developers.facebook.com/docs/facebook-pixel/events/)

