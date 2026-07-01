---
name: Gotchas, Security & Performance — Guía Completa
description: XSS prevention, form injection, performance bottlenecks, debugging tips
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# Gotchas, Security & Performance — Guía Completa

## 1. XSS Prevention (Cross-Site Scripting)

### Problema: XSS via innerHTML

```javascript
// ❌ INSEGURO
const userInput = '<img src=x onerror="alert(\'XSS\')">';
document.getElementById('output').innerHTML = userInput;
// El JS en onerror se ejecuta!

// ✅ SEGURO
document.getElementById('output').textContent = userInput;
// Solo renderiza texto, no HTML
```

### Usar textContent para texto, innerHTML para HTML limpio

```javascript
// ✅ Texto puro
element.textContent = user_input;

// ✅ HTML seguro (solo HTML, no scripts)
element.innerHTML = sanitize(user_input);

// ✅ Crear elementos DOM en lugar de innerHTML
const div = document.createElement('div');
div.textContent = user_input;
element.appendChild(div);
```

### Función sanitize para HTML

```javascript
function sanitize(html) {
  const temp = document.createElement('div');
  temp.textContent = html;
  return temp.innerHTML;
  
  // O usar librería: DOMPurify
  // return DOMPurify.sanitize(html);
}
```

---

## 2. Form Injection Prevention

### Problema: CSRF (Cross-Site Request Forgery)

```javascript
// ❌ INSEGURO
form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  fetch('/api/create-contact', {
    method: 'POST',
    body: JSON.stringify(formData)
  });
  // Cualquier sitio puede hacer esta petición!
});

// ✅ SEGURO - Con nonce
form.addEventListener('submit', function(e) {
  e.preventDefault();
  
  const nonce = form.querySelector('input[name="_nonce"]').value;
  
  fetch('/api/create-contact', {
    method: 'POST',
    headers: { 'X-Nonce': nonce },
    body: JSON.stringify(formData)
  });
});

// Servidor verifica nonce
app.post('/api/create-contact', (req, res) => {
  const nonce = req.headers['x-nonce'];
  if (!verifyNonce(nonce)) {
    return res.status(403).json({ error: 'CSRF token invalid' });
  }
  // Procesar...
});
```

### Problema: SQL Injection

```javascript
// ❌ INSEGURO
const email = form.email.value;
const query = `SELECT * FROM contacts WHERE email = '${email}'`;
// User puede poner: ' OR 1=1 --

// ✅ SEGURO - Usar prepared statements
const email = form.email.value;
const query = 'SELECT * FROM contacts WHERE email = ?';
db.query(query, [email]); // Email se trata como dato, no código
```

---

## 3. Form Validation & Sanitization

### Client-Side Validation (UX, NO seguridad)

```javascript
function validateForm(form) {
  let valid = true;
  
  // Email
  const email = form.email.value;
  if (!email.includes('@')) {
    form.email.classList.add('error');
    valid = false;
  }
  
  // Phone (10+ dígitos)
  const phone = form.phone.value;
  const phoneDigits = phone.replace(/\D/g, '');
  if (phoneDigits.length < 10) {
    form.phone.classList.add('error');
    valid = false;
  }
  
  // Name (no números)
  const name = form.name.value;
  if (/\d/.test(name)) {
    form.name.classList.add('error');
    valid = false;
  }
  
  return valid;
}

form.addEventListener('submit', function(e) {
  if (!validateForm(this)) {
    e.preventDefault();
  }
});
```

### Server-Side Validation (seguridad)

```python
# Python/Flask

@app.route('/api/create-contact', methods=['POST'])
def create_contact():
    data = request.json
    
    # Validar email
    email = data.get('email', '').strip().lower()
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email'}), 400
    
    # Validar phone
    phone = data.get('phone', '').strip()
    phone_digits = ''.join(c for c in phone if c.isdigit())
    if len(phone_digits) < 10:
        return jsonify({'error': 'Invalid phone'}), 400
    
    # Sanitizar nombre
    name = data.get('name', '').strip()
    name = re.sub(r'[^a-zA-Z\s\-]', '', name)
    if not name:
        return jsonify({'error': 'Invalid name'}), 400
    
    # Procesar de forma segura
    contact = Contact(email=email, phone=phone, name=name)
    db.session.add(contact)
    db.session.commit()
    
    return jsonify({'id': contact.id}), 201
```

---

## 4. Sensitive Data Exposure

### Problema: Tokens en el código

```javascript
// ❌ NUNCA
const API_KEY = 'sk_test_51234567890';
const SECRET = 'secret_key_exposed';

// El cliente puede ver esto en:
// - DevTools Network tab
// - Page source
// - Browser cache

// ✅ SIEMPRE
// Guardar secrets en servidor/Cloudflare Worker
// Cliente obtiene token de corta duración

fetch('/api/get-token', {
  method: 'POST',
  body: JSON.stringify({ action: 'get_ghl_token' })
}).then(res => res.json()).then(data => {
  const token = data.token; // Token de 1 hora
  // Usar token para llamadas a GHL
});
```

### Problema: PII en logs

```javascript
// ❌ INSEGURO
console.log('User data:', { email, phone, ssn });
// Cualquiera abriendo DevTools ve datos personales

// ✅ SEGURO
if (window.debug === true) { // Solo en desarrollo
  console.log('Email:', email.substring(0, 3) + '***');
}

// En servidor, usar logger con redacción
logger.info('Contact created', {
  email: 'j***@example.com', // Redactado
  source: 'web_form'
});
```

---

## 5. Performance Bottlenecks

### Problema: Script Síncrono Bloqueante

```html
<!-- ❌ BLOQUEA carga de página -->
<head>
  <script src="analytics.js"></script>
  <script src="forms.js"></script>
  <script src="tracking.js"></script>
</head>

<!-- ✅ CORRECTO -->
<head>
  <!-- Crítico para el sitio -->
  <script src="critical.js"></script>
</head>

<body>
  <!-- Contenido -->
  
  <!-- No-crítico, cargar al final o async -->
  <script src="analytics.js" async></script>
  <script src="tracking.js" async></script>
</body>
```

### Problema: Large Images

```html
<!-- ❌ Cargar una imagen 5MB -->
<img src="hero.jpg" alt="Hero">

<!-- ✅ Optimizar -->
<picture>
  <source srcset="hero-320w.webp 320w, hero-640w.webp 640w" type="image/webp">
  <img src="hero-640w.jpg" alt="Hero" loading="lazy">
</picture>

<!-- Comprimir imágenes -->
<!-- https://tinypng.com/ -->
```

### Problema: Múltiples fetch requests

```javascript
// ❌ Lento (3 requests secuenciales)
async function fetchData() {
  const users = await fetch('/api/users').then(r => r.json());
  const posts = await fetch('/api/posts').then(r => r.json());
  const comments = await fetch('/api/comments').then(r => r.json());
}

// ✅ Rápido (3 requests paralelos)
async function fetchData() {
  const [users, posts, comments] = await Promise.all([
    fetch('/api/users').then(r => r.json()),
    fetch('/api/posts').then(r => r.json()),
    fetch('/api/comments').then(r => r.json())
  ]);
}
```

### Problema: DOM Thrashing

```javascript
// ❌ Leer/escribir alternado (lento)
for (let i = 0; i < 100; i++) {
  element.style.left = element.offsetLeft + 10 + 'px';
  // Cada acceso a offsetLeft causa reflow!
}

// ✅ Batch reads y writes
let left = element.offsetLeft; // Leer una vez
for (let i = 0; i < 100; i++) {
  left += 10;
}
element.style.left = left + 'px'; // Escribir una vez
```

---

## 6. Memory Leaks

### Problema: Event Listeners no removidos

```javascript
// ❌ Event listener permanece en memoria
const button = document.querySelector('button');
button.addEventListener('click', expensiveFunction);

// Si removemos el button del DOM, el listener sigue en memoria

// ✅ Remover listener
button.removeEventListener('click', expensiveFunction);

// O mejor aún, usar {once: true}
button.addEventListener('click', expensiveFunction, { once: true });
// Se ejecuta una sola vez y se remueve automáticamente
```

### Problema: Circular References

```javascript
// ❌ Referencia circular
const obj = {};
obj.self = obj;
// Garbage collector no puede limpiar

// ✅ Limpiar referencias
obj.self = null;
obj = null;
```

---

## 7. Debugging Tips

### Usar Chrome DevTools

```javascript
// Breakpoints
debugger; // Pausa ejecución aquí

// Console logging
console.log('text');
console.error('error');
console.warn('warning');
console.table(arrayOfObjects); // Tabla

// Conditional logging
console.assert(value > 0, 'Value should be > 0');

// Timing
console.time('label');
// ... código ...
console.timeEnd('label'); // Imprime tiempo

// Grupos
console.group('Grouped');
console.log('Item 1');
console.log('Item 2');
console.groupEnd();
```

### Inspeccionar red

```javascript
// DevTools → Network tab

// Monitorear fetch en tiempo real
const originalFetch = window.fetch;
window.fetch = function(...args) {
  console.log('FETCH:', args[0]);
  return originalFetch.apply(this, args);
};

// Ver payloads
fetch('/api/create-contact', {
  method: 'POST',
  body: JSON.stringify(data)
}).then(res => {
  console.log('Response:', res.status, res.statusText);
  return res.json();
}).then(data => {
  console.log('Data:', data);
});
```

### Monitorear performance

```javascript
// Medir tiempo de carga
window.addEventListener('load', function() {
  const perfData = performance.timing;
  const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
  console.log('Page load time:', pageLoadTime, 'ms');
});

// Medir tiempo de operación
const start = performance.now();
// ... código ...
const end = performance.now();
console.log('Operation took', end - start, 'ms');

// Ver métrica de Core Web Vitals
if ('PerformanceObserver' in window) {
  const observer = new PerformanceObserver(list => {
    for (const entry of list.getEntries()) {
      console.log(entry.name, entry.value);
    }
  });
  observer.observe({ entryTypes: ['largest-contentful-paint'] });
}
```

---

## 8. Gotchas Comunes en Innovart

### Gotcha 1: theme.liquid sin </body>

```liquid
<!-- ❌ Rompe Qikify -->
</html>
<!-- Falta </body> antes -->

<!-- ✅ Correcto -->
  </body>
</html>
```

### Gotcha 2: Multiple fbclid captures

```javascript
// ❌ Capturar múltiples veces es lento
for (let i = 0; i < 10; i++) {
  const fbclid = new URL(window.location).searchParams.get('fbclid');
}

// ✅ Capturar una vez
const fbclid = new URL(window.location).searchParams.get('fbclid');
sessionStorage.setItem('fbclid', fbclid);

// Luego usar sessionStorage
const cachedFbclid = sessionStorage.getItem('fbclid');
```

### Gotcha 3: Form re-submits

```javascript
// ❌ Puede enviar dos veces si user hace click rápido
form.addEventListener('submit', function(e) {
  e.preventDefault();
  fetch('/api/create');
});

// ✅ Bloquear tras primera submit
let submitted = false;
form.addEventListener('submit', function(e) {
  if (submitted) return;
  submitted = true;
  e.preventDefault();
  fetch('/api/create').finally(() => submitted = false);
});
```

### Gotcha 4: sessionStorage vs localStorage

```javascript
// sessionStorage: Se borra al cerrar pestaña
sessionStorage.setItem('fbclid', fbclid);
// Ideal para: fbclid, tokens de corta vida

// localStorage: Persiste
localStorage.setItem('user_preference', 'dark_mode');
// Ideal para: preferencias de usuario

// No guardar en ninguno: passwords, APIs keys
```

---

## 9. Common Errors & Solutions

### Error: "undefined is not a function"

```javascript
// ❌ window.BContact aún no está disponible
window.BContact.send(data); // Error!

// ✅ Esperar a que Qikify cargue
if (typeof window.BContact !== 'undefined') {
  window.BContact.send(data);
}
```

### Error: "Cannot read property X of undefined"

```javascript
// ❌ No verificar que objeto existe
const email = user.profile.email; // Error si user.profile = undefined

// ✅ Verificar cada paso
const email = user?.profile?.email; // Null coalescing
// O
const email = user && user.profile && user.profile.email;
```

### Error: "CORS error"

```javascript
// ❌ Request desde cliente a servidor diferente
fetch('https://other-domain.com/api/data'); // CORS error

// ✅ Proxy vía servidor propio
fetch('/api/proxy?url=https://other-domain.com/api/data');

// O configurar CORS en servidor
app.use(cors({
  origin: 'https://my-domain.com'
}));
```

---

## 10. Security Checklist

- [ ] No exponer API keys/secrets en cliente
- [ ] Validar datos en servidor, no solo cliente
- [ ] Usar HTTPS para todas las requests
- [ ] Nonce/CSRF tokens en forms
- [ ] Sanitizar HTML user-input
- [ ] Hash/encrypted passwords
- [ ] Rate limiting en endpoints
- [ ] Log de cambios críticos
- [ ] GDPR compliance (consent para tracking)
- [ ] Security headers (CSP, X-Frame-Options, etc.)

---

## 11. Performance Checklist

- [ ] Imágenes optimizadas (< 100KB hero)
- [ ] Scripts async/defer excepto críticos
- [ ] Minificar CSS/JS en producción
- [ ] Lazy load imágenes (loading="lazy")
- [ ] Cache headers configurados
- [ ] Gzip compression habilitado
- [ ] CDN para assets estáticos
- [ ] Bundle size < 200KB
- [ ] LCP < 2.5s, FID < 100ms, CLS < 0.1

---

## 12. Recursos Oficiales

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web.dev Performance](https://web.dev/performance/)
- [MDN Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

