---
name: GemPages HTML/CSS Blocks — Guía Completa
description: Code blocks, HTML custom, CSS styling, ejemplos para Innovart
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# GemPages HTML/CSS Blocks — Guía Completa

## 1. Introducción a GemPages

GemPages es un editor visual de páginas para Shopify similar a PageFly. En Innovart se usa para:
- Home5 (Panamá, A/B testing)
- Algunas landings alternativas

**En Innovart:** GemPages es SECUNDARIO. PageFly es el editor principal para landings de ciudad.

---

## 2. Acceso a GemPages

Desde Shopify Admin:
```
Apps → GemPages → Editor
```

O URL directa:
```
https://innovartmedical.myshopify.com/admin/apps/gempages/pages
```

---

## 3. Custom HTML Block — Agregar Código

En GemPages, agregar bloque "Custom HTML":

```html
<div class="my-custom-section">
  <h2>Custom Heading</h2>
  <p>Custom paragraph content</p>
  <button class="my-button">Click Me</button>
</div>

<style>
  .my-custom-section {
    padding: 40px 20px;
    background: #f5f5f5;
    border-radius: 8px;
    max-width: 800px;
    margin: 40px auto;
  }
  
  .my-custom-section h2 {
    color: #333;
    font-size: 28px;
    margin-bottom: 15px;
    text-align: center;
  }
  
  .my-custom-section p {
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
  }
  
  .my-button {
    display: block;
    margin: 20px auto;
    padding: 12px 30px;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .my-button:hover {
    background: #0052a3;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.my-button');
    if (button) {
      button.addEventListener('click', function() {
        alert('Button clicked in GemPages!');
      });
    }
  });
</script>
```

---

## 4. Inyectar Qikify en GemPages

Agregar Qikify contact form:

```html
<!-- Qikify Form Embed para GemPages -->
<div id="qikify-container-gempages">
  <h2>Get Your Free Consultation</h2>
  <div contactform-embed="483316"></div>
</div>

<style>
  #qikify-container-gempages {
    max-width: 600px;
    margin: 40px auto;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  #qikify-container-gempages h2 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
  }
</style>

<script>
  // Inyectar script de Qikify si no está cargado
  if (typeof window.Qikify === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://www.qikify.com/app/qikify.min.js';
    script.async = true;
    
    script.onload = function() {
      console.log('Qikify loaded in GemPages');
      if (typeof window.BContact !== 'undefined') {
        console.log('window.BContact is available');
      }
    };
    
    script.onerror = function() {
      console.error('Failed to load Qikify');
    };
    
    document.body.appendChild(script);
  }
</script>
```

---

## 5. GemPages CSS Isolation (Important)

GemPages inyecta CSS con scope aislado. Para evitar conflictos:

```html
<div class="gem-custom-section" data-section-id="unique-section">
  <h2>Section Title</h2>
  <p>Content here</p>
</div>

<style>
  /* Usar data-attributes para mayor especificidad */
  [data-section-id="unique-section"] {
    padding: 20px;
    background: #f0f0f0;
  }
  
  [data-section-id="unique-section"] h2 {
    color: #333;
    font-size: 24px;
  }
  
  /* O usar clases con prefijo */
  .gem-custom-section {
    border: 1px solid #ddd;
    border-radius: 8px;
  }
  
  .gem-custom-section h2 {
    margin: 0 0 10px 0;
  }
</style>
```

---

## 6. Responsive Design en GemPages

```html
<div class="responsive-grid">
  <div class="grid-item">
    <h3>Item 1</h3>
    <p>Description</p>
  </div>
  <div class="grid-item">
    <h3>Item 2</h3>
    <p>Description</p>
  </div>
  <div class="grid-item">
    <h3>Item 3</h3>
    <p>Description</p>
  </div>
</div>

<style>
  .responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .grid-item {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
  }
  
  .grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  
  .grid-item h3 {
    margin: 0 0 10px 0;
    color: #333;
  }
  
  .grid-item p {
    margin: 0;
    color: #666;
    font-size: 14px;
  }
  
  /* Mobile */
  @media (max-width: 768px) {
    .responsive-grid {
      grid-template-columns: 1fr;
      padding: 15px;
    }
    
    .grid-item {
      padding: 15px;
    }
  }
</style>
```

---

## 7. Image Gallery en GemPages

```html
<div class="gallery-container">
  <div class="gallery-main">
    <img id="main-image" src="https://via.placeholder.com/600x400" alt="Main image">
  </div>
  <div class="gallery-thumbs">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 1" onclick="updateMainImage(this)">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 2" onclick="updateMainImage(this)">
    <img src="https://via.placeholder.com/80x80" alt="Thumb 3" onclick="updateMainImage(this)">
  </div>
</div>

<style>
  .gallery-container {
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
  
  .gallery-thumbs {
    display: flex;
    gap: 10px;
    justify-content: center;
  }
  
  .gallery-thumbs img {
    width: 80px;
    height: 80px;
    cursor: pointer;
    border: 2px solid transparent;
    border-radius: 4px;
    transition: border-color 0.3s;
  }
  
  .gallery-thumbs img:hover,
  .gallery-thumbs img.active {
    border-color: #0066cc;
  }
</style>

<script>
  function updateMainImage(thumb) {
    const mainImage = document.getElementById('main-image');
    mainImage.src = thumb.src.replace('80x80', '600x400');
    
    // Marcar como activo
    document.querySelectorAll('.gallery-thumbs img').forEach(img => {
      img.classList.remove('active');
    });
    thumb.classList.add('active');
  }
  
  // Marcar primera imagen como activa al cargar
  document.addEventListener('DOMContentLoaded', function() {
    const firstThumb = document.querySelector('.gallery-thumbs img');
    if (firstThumb) {
      firstThumb.classList.add('active');
    }
  });
</script>
```

---

## 8. Accordion/Collapse Section

```html
<div class="accordion">
  <div class="accordion-item">
    <button class="accordion-header">
      <span>What is included?</span>
      <span class="icon">+</span>
    </button>
    <div class="accordion-content">
      <p>Our service includes consultation, treatment plan, and follow-up care.</p>
    </div>
  </div>
  
  <div class="accordion-item">
    <button class="accordion-header">
      <span>How long does it take?</span>
      <span class="icon">+</span>
    </button>
    <div class="accordion-content">
      <p>Typical procedure takes 2-4 hours depending on extent of work.</p>
    </div>
  </div>
  
  <div class="accordion-item">
    <button class="accordion-header">
      <span>Is it painful?</span>
      <span class="icon">+</span>
    </button>
    <div class="accordion-content">
      <p>We use anesthesia to ensure comfort. Most patients experience minimal discomfort.</p>
    </div>
  </div>
</div>

<style>
  .accordion {
    max-width: 600px;
    margin: 40px auto;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .accordion-item {
    border-bottom: 1px solid #ddd;
  }
  
  .accordion-item:last-child {
    border-bottom: none;
  }
  
  .accordion-header {
    width: 100%;
    padding: 16px;
    background: #f5f5f5;
    border: none;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 16px;
    font-weight: bold;
    color: #333;
    transition: background 0.3s;
  }
  
  .accordion-header:hover {
    background: #e8e8e8;
  }
  
  .accordion-header.active {
    background: #0066cc;
    color: white;
  }
  
  .icon {
    transition: transform 0.3s;
  }
  
  .accordion-header.active .icon {
    transform: rotate(45deg);
  }
  
  .accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    background: white;
  }
  
  .accordion-content.active {
    max-height: 300px;
  }
  
  .accordion-content p {
    padding: 16px;
    margin: 0;
    color: #666;
    line-height: 1.6;
  }
</style>

<script>
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', function() {
      const content = this.nextElementSibling;
      const isActive = content.classList.contains('active');
      
      // Cerrar todos
      document.querySelectorAll('.accordion-content').forEach(c => {
        c.classList.remove('active');
      });
      document.querySelectorAll('.accordion-header').forEach(h => {
        h.classList.remove('active');
      });
      
      // Abrir clickeado (si no estaba activo)
      if (!isActive) {
        content.classList.add('active');
        this.classList.add('active');
      }
    });
  });
</script>
```

---

## 9. Video Hero Section

```html
<div class="video-hero">
  <video autoplay muted loop playsinline>
    <source src="https://example.com/video.mp4" type="video/mp4">
  </video>
  
  <div class="hero-overlay">
    <h1>Your Heading</h1>
    <p>Subheading goes here</p>
    <button class="cta-button">Learn More</button>
  </div>
</div>

<style>
  .video-hero {
    position: relative;
    height: 500px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .video-hero video {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
  }
  
  .hero-overlay {
    position: relative;
    z-index: 2;
    text-align: center;
    color: white;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  }
  
  .hero-overlay h1 {
    font-size: 48px;
    margin: 0 0 20px 0;
    font-weight: bold;
  }
  
  .hero-overlay p {
    font-size: 20px;
    margin: 0 0 30px 0;
  }
  
  .cta-button {
    padding: 12px 30px;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s;
  }
  
  .cta-button:hover {
    background: #0052a3;
  }
  
  @media (max-width: 768px) {
    .video-hero {
      height: 350px;
    }
    
    .hero-overlay h1 {
      font-size: 32px;
    }
    
    .hero-overlay p {
      font-size: 16px;
    }
  }
</style>
```

---

## 10. Testimonials Slider

```html
<div class="testimonials-section">
  <h2>What Our Clients Say</h2>
  
  <div class="testimonials-slider">
    <div class="testimonial-slide active">
      <div class="testimonial-content">
        <p>"Excellent service and results. Highly recommended!"</p>
        <p class="author">— John Doe</p>
      </div>
    </div>
    
    <div class="testimonial-slide">
      <div class="testimonial-content">
        <p>"Professional team, great care, fantastic outcome."</p>
        <p class="author">— Jane Smith</p>
      </div>
    </div>
    
    <div class="testimonial-slide">
      <div class="testimonial-content">
        <p>"Changed my life. Cannot thank them enough!"</p>
        <p class="author">— Mike Johnson</p>
      </div>
    </div>
  </div>
  
  <div class="slider-controls">
    <button class="slider-prev">← Prev</button>
    <button class="slider-next">Next →</button>
  </div>
</div>

<style>
  .testimonials-section {
    padding: 60px 20px;
    background: #f5f5f5;
    text-align: center;
  }
  
  .testimonials-section h2 {
    font-size: 32px;
    margin-bottom: 40px;
    color: #333;
  }
  
  .testimonials-slider {
    max-width: 600px;
    margin: 0 auto 30px;
    position: relative;
  }
  
  .testimonial-slide {
    display: none;
    padding: 40px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .testimonial-slide.active {
    display: block;
    animation: fadeIn 0.3s;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  .testimonial-content p {
    font-size: 16px;
    line-height: 1.6;
    color: #666;
    margin: 0 0 15px 0;
  }
  
  .author {
    font-weight: bold;
    color: #333 !important;
  }
  
  .slider-controls {
    display: flex;
    gap: 10px;
    justify-content: center;
  }
  
  .slider-prev, .slider-next {
    padding: 10px 20px;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
  }
</style>

<script>
  let currentTestimonial = 0;
  const testimonials = document.querySelectorAll('.testimonial-slide');
  
  function showTestimonial(n) {
    testimonials.forEach(t => t.classList.remove('active'));
    testimonials[n].classList.add('active');
  }
  
  document.querySelector('.slider-next').addEventListener('click', () => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
  
  document.querySelector('.slider-prev').addEventListener('click', () => {
    currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
</script>
```

---

## 11. Contact Form

```html
<form class="gem-contact-form" id="contact-form">
  <h2>Contact Us</h2>
  
  <div class="form-group">
    <input type="text" placeholder="Your Name" name="name" required>
  </div>
  
  <div class="form-group">
    <input type="email" placeholder="Your Email" name="email" required>
  </div>
  
  <div class="form-group">
    <input type="tel" placeholder="Your Phone" name="phone" required>
  </div>
  
  <div class="form-group">
    <textarea placeholder="Your Message" name="message" rows="5" required></textarea>
  </div>
  
  <button type="submit" class="submit-button">Send Message</button>
  <div class="form-message" id="form-message"></div>
</form>

<style>
  .gem-contact-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .gem-contact-form h2 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    font-family: inherit;
  }
  
  .form-group input:focus,
  .form-group textarea:focus {
    outline: none;
    border-color: #0066cc;
    box-shadow: 0 0 0 3px rgba(0,102,204,0.1);
  }
  
  .submit-button {
    width: 100%;
    padding: 12px;
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s;
  }
  
  .submit-button:hover {
    background: #0052a3;
  }
  
  .form-message {
    margin-top: 15px;
    padding: 12px;
    border-radius: 4px;
    display: none;
    text-align: center;
  }
  
  .form-message.error {
    background: #ffe0e0;
    color: #c00;
    display: block;
  }
  
  .form-message.success {
    background: #e0ffe0;
    color: #0a0;
    display: block;
  }
</style>

<script>
  document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formMessage = document.getElementById('form-message');
    const form = this;
    
    const data = {
      name: form.name.value,
      email: form.email.value,
      phone: form.phone.value,
      message: form.message.value
    };
    
    // Aquí enviar a servidor
    console.log('Form data:', data);
    
    formMessage.textContent = 'Message sent successfully!';
    formMessage.className = 'form-message success';
    
    form.reset();
  });
</script>
```

---

## 12. Gotchas en GemPages

### Problema: CSS conflictúa con otros bloques

**Solución:** Usar selectores específicos y clases únicas:

```css
.gem-custom-my-section {
  /* Específico a esta sección */
}
```

### Problema: JavaScript no se ejecuta

**Solución:** Usar `DOMContentLoaded`:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  // Código aquí
});
```

### Problema: Qikify no carga

**Causa:** Script no se inyectó correctamente.

**Solución:** Ver sección 4, asegurarse de inyectar script completo.

---

## 13. GemPages vs PageFly en Innovart

| Aspecto | GemPages | PageFly |
|---------|----------|---------|
| Home5 (Panamá) | ✅ Usar | ❌ No |
| Landings de ciudad | ❌ No | ✅ Usar |
| Facilidad | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| CSS Isolation | ⚠️ Cuidado | ✅ Bueno |

---

## 14. Recursos Oficiales

- [GemPages Documentation](https://help.gempages.io/)
- [GemPages Custom Code](https://help.gempages.io/article/113-custom-code-block)
- [Shopify Liquid Reference](https://shopify.dev/api/liquid)

