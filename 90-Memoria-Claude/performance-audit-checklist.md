---
name: Performance Audit Checklist
description: Auditoría de rendimiento — velocidad de carga, render time, optimización de assets, CWV
metadata:
  type: checklist
  category: performance
  last_updated: 2026-06-30
  applies_to: landings, forms, tracking, CRM integrations
---

# Performance Audit Checklist — Speed, Render Time, Memory

**Cuándo usar:** Antes de publicar landing, después de agregar scripts, post-deploy en Shopify.
**Duración:** 20–40 min según scope.
**Owner:** Javier / Tech Lead / QA

---

## 1. CORE WEB VITALS (CWV) — Google PageSpeed Insights

### LCP (Largest Contentful Paint) — Target: <2.5s (Good)
- [ ] **Medir LCP**
  - [ ] Abrir landing en Chrome (Desktop mode)
  - [ ] DevTools → Lighthouse → Run audit (Mobile selected)
  - [ ] Ver LCP score en "Metrics" sección
  - [ ] Alternativa: PageSpeed Insights (`https://pagespeed.web.dev`)
  - [ ] Report: guardar HTML de Lighthouse (o screenshot)

- [ ] **LCP < 2.5s (Good)**
  - [ ] Si LCP > 2.5s: investigar causa (ver sección "LCP Optimization" abajo)
  - [ ] Si 2.5s–4.0s: Needs Improvement
  - [ ] Si > 4.0s: Poor

- [ ] **LCP Element Identification**
  - [ ] DevTools → Performance tab → Record page load → buscar "LCP" en timeline
  - [ ] LCP es típicamente: hero image, h1, video poster
  - [ ] Verificar: elemento se carga pronto en HTML (no al final)

### FID (First Input Delay) — Target: <100ms (Good)
- [ ] **Medir FID**
  - [ ] Lighthouse: no puede medir (requiere interacción real)
  - [ ] Chrome UX Report: si landing tiene traffic, usar PageSpeed Insights "Real user experience" sección
  - [ ] Test manual: Click button → note delay antes de respuesta visual
  - [ ] Target: <100ms (Good), 100–300ms (Needs Improvement), >300ms (Poor)

- [ ] **FID < 100ms (Good)**
  - [ ] Si FID >300ms: probablemente JavaScript bloqueante en main thread
  - [ ] Ver sección "Main Thread Blocking" abajo

### CLS (Cumulative Layout Shift) — Target: <0.1 (Good)
- [ ] **Medir CLS**
  - [ ] Lighthouse: muestra score directamente
  - [ ] DevTools → Performance → Record page load → buscar "CLS"
  - [ ] Visually: scroll landing → notar si elementos se mueven inesperadamente
  - [ ] Target: <0.1 (Good), 0.1–0.25 (Needs Improvement), >0.25 (Poor)

- [ ] **CLS < 0.1 (Good)**
  - [ ] Culprits típicos:
    - [ ] Images sin `width`/`height` (usar aspect-ratio en CSS)
    - [ ] Sticky bar que aparece sin reservar espacio
    - [ ] Ads/third-party scripts que inyectan contenido
  - [ ] Fixes: ver sección "CLS Optimization" abajo

### INP (Interaction to Next Paint) — Target: <200ms (Good, replacing FID)
- [ ] **Medir INP**
  - [ ] Lighthouse (v11+): incluye INP
  - [ ] Chrome DevTools → Lighthouse
  - [ ] Target: <200ms (Good), 200–500ms (Needs Improvement), >500ms (Poor)
  - [ ] Más sensible que FID (mide delay + processing + paint)

---

## 2. PAGE LOAD SPEED — Asset Optimization

### Image Optimization
- [ ] **Hero Image**
  - [ ] Formato: WebP (preferred) o JPEG (fallback)
  - [ ] Tamaño: <250KB (mobile <150KB)
  - [ ] Dimensiones: 1920×1080 (desktop), 750×1000 (mobile)
  - [ ] Lazy-load: No (hero debe eagerly load)
  - [ ] `srcset` responsive: sí (múltiples densidades/breakpoints)
  - [ ] Test: DevTools → Network → hero image request → check size + timing
- [ ] **Form/CTA Images**
  - [ ] Iconos: SVG (< 10KB) o PNG/WebP (<50KB)
  - [ ] Lazy-load: Sí (fuera viewport)
  - [ ] Test: scroll → imágenes cargan on-demand
- [ ] **Background Images**
  - [ ] CSS: `background-image` → usar WebP + fallback
  - [ ] Tamaño: <150KB cada una
  - [ ] Alternativa: solid color + pattern (más rápido)
- [ ] **Thumbnail/Video Poster**
  - [ ] Size: <80KB
  - [ ] Format: JPEG or WebP
  - [ ] Lazy-load: Sí

### CSS & JavaScript Bundling
- [ ] **CSS Size**
  - [ ] Total: <100KB (gzip) para theme + custom
  - [ ] Measure: DevTools → Network → filter `.css` → sum sizes
  - [ ] Unused CSS: Lighthouse reporta (eliminar si >10% waste)
  - [ ] Critical CSS: inline en `<head>` (first paint)
- [ ] **JavaScript Size**
  - [ ] Total: <300KB (gzip) para tracking + third-party + custom
  - [ ] Breakdown:
    - [ ] Meta Pixel: ~40KB gzip
    - [ ] GA4: ~20KB gzip
    - [ ] Qikify: ~60KB gzip
    - [ ] Clarity: ~30KB gzip
    - [ ] Custom scripts: <50KB gzip
  - [ ] Measure: DevTools → Network → filter `.js` → sum
  - [ ] Unused JS: DevTools → Coverage tab → check %unused
- [ ] **Minification**
  - [ ] CSS minified: `.css` (no `.css.raw`)
  - [ ] JS minified: `.js` (no source maps in production)
  - [ ] HTML minified: opcional (Shopify auto-minifies)
- [ ] **Tree Shaking**
  - [ ] Bundler (if using): webpack/vite with tree-shake enabled
  - [ ] Unused imports: auditar código importado no usado
  - [ ] Example: si importas `lodash`, usar `lodash-es` + tree-shake

### Network Requests Waterfall
- [ ] **Request Count**
  - [ ] Desktop: <50 requests (ideally <40)
  - [ ] Mobile: <40 requests (ideally <30)
  - [ ] Measure: DevTools → Network → Ctrl+Shift+J → copy as cURL → count
  - [ ] Culprits: multiple tracking pixels, fonts, third-party
- [ ] **Request Waterfall Order**
  - [ ] Priority: HTML → Critical CSS → Above-fold images → JS async
  - [ ] Verify: DevTools → Network → Priority column
  - [ ] Expected order:
    1. HTML document
    2. CSS (critical, inline o separate)
    3. Hero image(s)
    4. Third-party scripts (Meta Pixel, GA4) → async
    5. Form script (Qikify) → async
    6. Tracking/CAPI → async
- [ ] **DNS Lookup Time**
  - [ ] Measure: DevTools → Network → buscar "DNS Lookup" en timing breakdown
  - [ ] Target: <50ms per domain
  - [ ] Domains: innovartmedical.com, shopify.com, facebook.net, googletagmanager.com, qikify.com, clarity.ms, gohighlevel.com
  - [ ] If slow: puede ser DNS resolver (configurar 1.1.1.1 o 8.8.8.8)

### Caching Strategy
- [ ] **Browser Cache (static assets)**
  - [ ] Cacheable: images, CSS, JS bundles, fonts
  - [ ] TTL: 30 days (images/CSS/JS)
  - [ ] Verify: DevTools → Network → Response Headers → `Cache-Control: public, max-age=2592000`
  - [ ] Test: reload page twice → 2nd time faster (304 Not Modified)
- [ ] **CDN Cache (Shopify/Cloudflare)**
  - [ ] Images: cached at edge (Shopify CDN automatic)
  - [ ] Workers: cached at Cloudflare edge
  - [ ] TTL: 24 hours (config depends on change frequency)
  - [ ] Purge: manual purge after major changes
- [ ] **Server-Side Cache (GHL/Meta API)**
  - [ ] GHL contacts: cached in app (real-time writes OK)
  - [ ] Meta API: rate-limit aware (batch calls)
  - [ ] Don't over-cache: fresh data matters

---

## 3. RENDERING PERFORMANCE — Main Thread, JavaScript

### JavaScript Execution Time
- [ ] **Measure Script Execution**
  - [ ] DevTools → Performance tab → Record page load (3 sec)
  - [ ] Export → analyze "Self Time" per script
  - [ ] Yellow bars: JavaScript execution (should be <3.5s total for homepage)
- [ ] **Long Tasks (>50ms)**
  - [ ] DevTools → Performance → search "Long Task" warnings
  - [ ] Target: 0 long tasks on page load
  - [ ] If present: offload to Web Worker or split execution
  - [ ] Example bad: Qikify init taking 200ms → lazy-load form

### Third-Party Script Impact
- [ ] **Meta Pixel**
  - [ ] Load: async + defer (non-blocking)
  - [ ] Exec time: ~30–50ms
  - [ ] Impact: Low (well-optimized by Meta)
- [ ] **GA4**
  - [ ] Load: async
  - [ ] Exec time: ~20–40ms
  - [ ] Impact: Low
- [ ] **Qikify**
  - [ ] Load: async (after DOM ready preferred)
  - [ ] Exec time: ~60–100ms (form rendering)
  - [ ] Impact: Medium (form below fold OK to lazy-load)
  - [ ] Tip: delay Qikify init until form in viewport
- [ ] **Clarity**
  - [ ] Load: async
  - [ ] Exec time: ~10–20ms
  - [ ] Impact: Low
- [ ] **Custom Tracking Scripts**
  - [ ] fbclid capture: <5ms
  - [ ] UTM capture: <5ms
  - [ ] CAPI dispatch: <50ms (async)

### Memory Usage
- [ ] **Heap Size at Load**
  - [ ] DevTools → Memory → Take snapshot → check "Total" size
  - [ ] Target: <50MB heap (mobile friendly)
  - [ ] If >100MB: likely memory leak or oversized bundle
  - [ ] Baseline: empty page ~30MB, with scripts + data ~45MB
- [ ] **Memory Leak Detection**
  - [ ] Open landing
  - [ ] Snapshot 1 (at load)
  - [ ] Interact (click buttons, submit form)
  - [ ] Snapshot 2 (after 1min idle)
  - [ ] Compare: if heap grew 10%+ → possible leak
  - [ ] Fix: detach event listeners, clear timeouts/intervals
- [ ] **Garbage Collection Pauses**
  - [ ] DevTools → Performance → look for "GC" events
  - [ ] GC duration: <100ms acceptable (ideally <50ms)
  - [ ] Frequency: every 5–10 seconds OK
  - [ ] If: every 1 sec → memory pressure, reduce allocations

---

## 4. MOBILE PERFORMANCE — Mobile-Specific Optimizations

### Mobile Load Time
- [ ] **Simulate 4G (Lighthouse)**
  - [ ] DevTools → Lighthouse → Throttling = "Slow 4G"
  - [ ] Run audit → record metrics
  - [ ] Target:
    - [ ] FCP (First Contentful Paint): <3.0s
    - [ ] LCP: <4.0s (mobile is slower than desktop)
    - [ ] TTI (Time to Interactive): <5.5s
- [ ] **Real Device Testing**
  - [ ] Use iPhone or Android device
  - [ ] Test on actual 4G/LTE (not WiFi)
  - [ ] Measure: open landing, note time to interactive
  - [ ] Compare: desktop vs. mobile (mobile should not be >50% slower)

### Mobile Layout & Viewport
- [ ] **Viewport Meta Tag**
  - [ ] Verify: `<meta name="viewport" content="width=device-width, initial-scale=1">`
  - [ ] Check: page is responsive (no horizontal scroll at 320px width)
- [ ] **Touch Targets**
  - [ ] Buttons: minimum 44×44px (iOS) or 48×48px (Android)
  - [ ] Measure: DevTools → Device Mode → identify small buttons
  - [ ] Impact on performance: larger targets = fewer re-taps = faster
- [ ] **Scroll Performance (60 FPS)**
  - [ ] Scroll landing smoothly → should see 60 FPS (no jank)
  - [ ] DevTools → Performance → record scroll → check FPS
  - [ ] Target: 60 FPS sustained (avoid frame drops)
  - [ ] If jank: likely CSS animation or scroll listener (fix with `will-change` or passive listeners)

### Mobile-Specific Assets
- [ ] **Hero Image**
  - [ ] Mobile version: portrait (750×1000) vs. desktop landscape (1920×1080)
  - [ ] Use: `<picture>` element + `srcset` per breakpoint
  - [ ] Size: mobile <150KB, desktop <250KB
- [ ] **Video (if used)**
  - [ ] Autoplay: NO on mobile (respects mute constraint)
  - [ ] Poster: required (shows before play)
  - [ ] Format: mp4 (H.264) for compat
  - [ ] Bitrate: mobile <2Mbps (for 4G), desktop <5Mbps
  - [ ] Duration: <10 sec (convert to GIF if longer, test UX)
- [ ] **Sticky Bar**
  - [ ] Height: 88px (reserve space, no layout shift)
  - [ ] Interaction: CTA tappable (target 48×48px minimum)
  - [ ] Performance: position fixed (should be 60 FPS, not laggy)

---

## 5. FORM PERFORMANCE — Qikify, Submission

### Form Rendering
- [ ] **Form Load Time**
  - [ ] Qikify embed: <500ms after script init
  - [ ] Measure: DevTools → Network → Qikify requests → sum
  - [ ] If >1s: lazy-load form (init when scrolled into view)
- [ ] **Form Fields Rendering**
  - [ ] Fields appear in correct order (name, phone, email)
  - [ ] Inputs are interactive (not disabled)
  - [ ] Buttons respond to click immediately (<100ms)
  - [ ] Measure: click button → check in Performance tab

### Form Submission Performance
- [ ] **POST Request Time**
  - [ ] Worker endpoint: <500ms response (target <300ms)
  - [ ] Measure: DevTools → Network → POST to innovart-capi-webhook → Timing tab
  - [ ] Breakdown: Waiting (server) + Receiving (response body)
  - [ ] If Waiting >500ms: server bottleneck (check Worker code)
  - [ ] If Receiving >500ms: response too large (shouldn't be, check payload)
- [ ] **GHL Create Contact**
  - [ ] Behind the POST: API call to GHL
  - [ ] Latency: ~200–500ms typical
  - [ ] Test: POST → measure time in Worker logs (if timestamps available)
- [ ] **Success Feedback**
  - [ ] Message appears: <100ms after server response (JS DOM update)
  - [ ] Form clears: <200ms after success
  - [ ] Measure: DevTools → Performance → record submit → paint timing

### Form Validation Performance
- [ ] **Client-Side Validation**
  - [ ] Instant feedback: <50ms (no debounce needed for form fields)
  - [ ] Example: typing email → "Invalid email" appears <50ms
  - [ ] Test: DevTools console → measure validation function
- [ ] **Server-Side Validation**
  - [ ] Error response: <300ms from POST
  - [ ] Clear error message displayed
  - [ ] Test: intentionally submit bad data → measure response time

---

## 6. TRACKING & ANALYTICS PERFORMANCE — Pixel, CAPI, GA4

### Meta Pixel Performance
- [ ] **Script Load**
  - [ ] fbevents.js: async, <100ms execution
  - [ ] Measure: DevTools → Network → facebook.net requests
  - [ ] No blocking: pixel loads in background
- [ ] **Pixel Event Fire**
  - [ ] PageView event: <500ms after page load
  - [ ] Custom events (ViewContent, Contact, Schedule): <200ms after trigger
  - [ ] Measure: DevTools → Network → filter `facebook` → see pixel requests
- [ ] **CAPI Request**
  - [ ] Worker batches events: <1s latency after POST form
  - [ ] Network: POST to `innovart-capi-webhook...` → status 200
  - [ ] Impact on user: none (async, doesn't block form submit success)

### GA4 Performance
- [ ] **gtag.js Load**
  - [ ] Script: <100ms, async
  - [ ] Measure: DevTools → Network → googletagmanager.com
- [ ] **GA4 Event Fire**
  - [ ] PageView: <500ms after page load
  - [ ] Custom events: <200ms after trigger
  - [ ] No blocking: events sent async

### Clarity Performance
- [ ] **Clarity Load**
  - [ ] Script: <100ms, async
  - [ ] Measure: DevTools → Network → clarity.ms
- [ ] **Session Recording**
  - [ ] Overhead: <1–2% CPU (negligible on desktop, slight on mobile)
  - [ ] Memory: +5–10MB per session
  - [ ] No impact on user interactions (runs in background)

### Combined Tracking Load (All 4 Systems)
- [ ] **Total Impact**
  - [ ] Combined script size: ~150KB gzip
  - [ ] Combined exec time: ~200–300ms
  - [ ] Memory overhead: ~30–40MB heap
  - [ ] Network requests: ~8–12 (Meta pixel, GA4, Clarity, custom)
  - [ ] Target: all async, page interactive by 2–3s (with LCP)

---

## 7. CRM & API PERFORMANCE — GHL Integration, Worker

### GHL API Performance
- [ ] **Create Contact Latency**
  - [ ] Expected: 200–500ms per request
  - [ ] Measure: add custom logging in Worker (timestamp before/after API call)
  - [ ] Target: <500ms (user tolerance)
  - [ ] If >1s: check GHL status page or rate limiting
- [ ] **Rate Limiting**
  - [ ] GHL limits: ~60 requests/min per API key (roughly 1/sec)
  - [ ] Innovart scale: ~50–100 forms/day = OK within limit
  - [ ] Verify: GHL Activity log → no "Rate Limit Exceeded" errors
- [ ] **Concurrent Requests**
  - [ ] If 10+ forms submit simultaneously: queue in Cloudflare (max workers concurrency)
  - [ ] Test: simulate 10 concurrent POSTs → should handle gracefully
  - [ ] Expected: requests queued, none lost, all succeed within 5 sec

### Cloudflare Worker Performance
- [ ] **Worker Execution Time**
  - [ ] Limit: 30 seconds (standard plan)
  - [ ] Target: <1 second per request
  - [ ] Measure: Cloudflare dashboard → Analytics → Workers → Requests CPU time
  - [ ] Breakdown: parse input + validate + GHL API call + respond
- [ ] **Worker Memory Usage**
  - [ ] Limit: 128MB (standard plan)
  - [ ] Target: <50MB per request (temporary)
  - [ ] If exceeded: will error (rare, only if bulky payloads)
- [ ] **Worker Cold Start**
  - [ ] First request after deploy: ~100–300ms (one-time)
  - [ ] Subsequent requests: <100ms (cached)
  - [ ] Verify: check logs for cold start indicator

### Database Query Performance (GHL backend)
- [ ] **Contact Search by Email**
  - [ ] Expected: <200ms (GHL's DB is optimized)
  - [ ] Measure: within GHL API response time (included in 200–500ms total)
- [ ] **Custom Field Update**
  - [ ] Expected: <100ms per field
  - [ ] Measure: within GHL API response time
  - [ ] Multiple fields (fbclid, utm_source, utm_medium, utm_campaign) in one API call

---

## 8. COMPARATIVE BENCHMARKS — Desktop vs. Mobile

| Metric | Desktop Target | Mobile Target | Current Status |
|---|---|---|---|
| **LCP** | <2.5s | <4.0s | TBD |
| **FID** | <100ms | <100ms | TBD |
| **CLS** | <0.1 | <0.1 | TBD |
| **TTI** | <3.5s | <5.5s | TBD |
| **Total JS** | <300KB | <250KB | TBD |
| **Total CSS** | <100KB | <80KB | TBD |
| **Requests** | <50 | <40 | TBD |
| **Requests size** | <3MB | <2MB | TBD |
| **Form load** | <500ms | <800ms | TBD |
| **Form submit** | <300ms | <500ms | TBD |

---

## 9. OPTIMIZATION TACTICS — Common Fixes

### LCP Optimization (if > 2.5s)
- [ ] **Identify LCP Element**
  - [ ] DevTools → Lighthouse → Diagnostics → "Largest Contentful Paint element"
  - [ ] Usually: hero image, h1, or video
- [ ] **If Hero Image:**
  - [ ] 1. Reduce image size (compress, resize, convert to WebP)
  - [ ] 2. Move image earlier in HTML (above fold)
  - [ ] 3. Preload: add `<link rel="preload" as="image" href="..." >`
  - [ ] 4. Lazy-load non-critical images (not hero)
  - [ ] 5. Use CDN with edge caching (Shopify CDN automatic)
- [ ] **If Text (h1):**
  - [ ] 1. Inline critical CSS (heading styles in `<head>`)
  - [ ] 2. Preload font (if custom): `<link rel="preload" as="font" href="..." >`
  - [ ] 3. Reduce blocking JavaScript (move `<script>` to end or async)
  - [ ] 4. Use `font-display: swap` (show fallback immediately)
- [ ] **If Video Poster:**
  - [ ] 1. Compress poster image (<80KB)
  - [ ] 2. Preload poster
  - [ ] 3. Don't autoplay (especially mobile)

### CLS Optimization (if > 0.1)
- [ ] **Identify Shifting Elements**
  - [ ] DevTools → Lighthouse → Diagnostics → "Cumulative Layout Shift"
  - [ ] Or: visually watch page load, note movement
- [ ] **Common Culprits & Fixes:**
  - [ ] **Images without width/height:**
    ```html
    <!-- Bad -->
    <img src="hero.jpg">
    <!-- Good -->
    <img src="hero.jpg" width="1920" height="1080" style="aspect-ratio: 16/9;">
    ```
  - [ ] **Sticky bar without space:**
    ```css
    /* Bad: sticky bar appears without push */
    .sticky-bar { position: fixed; top: 0; height: 88px; }
    body { margin-top: 0; }
    
    /* Good: reserve space */
    body { margin-top: 88px; }
    .sticky-bar { position: fixed; top: 0; height: 88px; }
    ```
  - [ ] **Dynamic content (ads, notifications):**
    - [ ] Reserve space in HTML (invisible box, then populate)
    - [ ] Don't inject without layout
  - [ ] **Font loading:**
    ```css
    font-display: swap; /* show fallback, swap when ready */
    ```

### FID/INP Optimization (if > 100ms)
- [ ] **Identify Long Tasks**
  - [ ] DevTools → Performance → search "Long Task"
- [ ] **Fixes:**
  - [ ] 1. **Split JavaScript:** if script is 200ms, split into chunks + debounce
  - [ ] 2. **Defer non-critical:** move `<script>` to before `</body>` (after page content)
  - [ ] 3. **Use Web Workers:** offload heavy computation (rare for forms)
  - [ ] 4. **Optimize dependencies:** remove unused libraries
  - [ ] 5. **Profiling:** DevTools → Performance → Profile individual functions

### Request Count / Bundle Size Optimization
- [ ] **Reduce Request Count:**
  - [ ] Combine multiple small CSS files (minify + bundle)
  - [ ] Combine multiple small JS files
  - [ ] Use CSS sprites for icons (or SVG)
  - [ ] Remove duplicate third-party scripts
  - [ ] Example: if loading jQuery + Bootstrap, check if really needed (Qikify may include)
- [ ] **Reduce Bundle Size:**
  - [ ] 1. Remove unused dependencies (DevTools → Coverage)
  - [ ] 2. Use minified versions (not source)
  - [ ] 3. Compress images (WebP + optimized JPEG)
  - [ ] 4. Lazy-load non-critical JS (form below fold? defer Qikify)
  - [ ] 5. Code split: separate critical path from analytics

---

## 10. MONITORING & CONTINUOUS PERFORMANCE

### Automated Monitoring
- [ ] **Google PageSpeed Insights**
  - [ ] Check weekly (manual or automated): https://pagespeed.web.dev
  - [ ] Set alert: if score drops >5 points
  - [ ] Track: desktop + mobile separately
- [ ] **Shopify Page Speed Insights**
  - [ ] Admin → Online Store → Monitor or Themes → Analytics
  - [ ] Built-in speed report (if enabled)
- [ ] **Lighthouse CI (optional)**
  - [ ] Set up in GitHub Actions: run Lighthouse on each deploy
  - [ ] Fail build if metrics regress
  - [ ] Track: historical trends (Google Sheets, Grafana, etc.)
- [ ] **Real User Monitoring (RUM)**
  - [ ] GA4 → Web Vitals (if enabled)
  - [ ] Clarity → Session recordings (qualitative, see slowdowns)
  - [ ] Compare: field data (real users) vs. lab data (Lighthouse)

### Performance Regressions
- [ ] **Detect Regression**
  - [ ] LCP changed from 2.0s → 3.5s? Investigate cause
  - [ ] Possible causes: new image added, new script loaded, CSS change
  - [ ] Check: recent Shopify theme edits (Activity Log)
- [ ] **Root Cause Analysis**
  - [ ] Compare: before/after Lighthouse report
  - [ ] Network tab: look for new slow requests
  - [ ] Performance tab: look for new long tasks
  - [ ] Memory: take snapshots, check for leak
- [ ] **Fix & Verify**
  - [ ] Apply fix (optimize image, defer script, etc.)
  - [ ] Re-run Lighthouse: verify metrics improved
  - [ ] Monitor for 24h: ensure fix stable

---

## Quick Checklist (10 min)

Use para cambios menores o CI/CD gates:

- [ ] **Lighthouse score >90** (Desktop: Perf, Accessibility, Best Practices, SEO)
- [ ] **LCP <2.5s** (desktop) or <4.0s (mobile)
- [ ] **CLS <0.1**
- [ ] **Form submit <300ms** (desktop) or <500ms (mobile)
- [ ] **No long tasks (>50ms)**
- [ ] **Hero image <250KB**
- [ ] **Total JS <300KB gzip**
- [ ] **Request count <50** (desktop) or <40 (mobile)
- [ ] **No layout shift** when scrolling

---

## Testing Setup

### Local Testing (Chrome DevTools)
```javascript
// In console, measure performance:

// 1. Get LCP (Largest Contentful Paint)
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  console.log('LCP:', entries[entries.length - 1].renderTime || entries[entries.length - 1].loadTime);
});
observer.observe({entryTypes: ['largest-contentful-paint']});

// 2. Measure script execution time
console.time('myScript');
// ... do work ...
console.timeEnd('myScript');

// 3. Get memory usage
console.log(performance.memory); // {usedJSHeapSize, totalJSHeapSize, ...}

// 4. Measure Form Submit
const start = performance.now();
document.querySelector('button[type="submit"]').click();
setTimeout(() => {
  console.log('Form submit time:', performance.now() - start);
}, 100);
```

### Lighthouse Batch Testing
```bash
# Install Lighthouse CLI
npm install -g @lhci/cli@^0.9

# Create lighthouserc.json
# {
#   "ci": {
#     "collect": {
#       "numberOfRuns": 3,
#       "url": ["https://innovartmedical.com", "https://innovartmedical.com/bogota"]
#     },
#     "upload": { "target": "temporary-public-storage" }
#   }
# }

# Run
lhci autorun

# Output: results + links to view reports
```

### WebPageTest
- [ ] Go to https://www.webpagetest.org
- [ ] Enter landing URL
- [ ] Select location (US East for US perf, or Colombia for local)
- [ ] Run test → detailed waterfall + metrics

---

## References

- [[home5-cro-v10-deploy-2026-06-22]] — Performance baseline for /home
- [[informe-clarity-home4-2026-06-18]] — Clarity data on mobile scroll/performance
- [[paso-a-paso-arreglo-formularios-2026-06-30]] — Form POST latency considerations
- [[referencia-tecnica-shopify-pagefly-whatsapp-tracking]] — Tracking script impact
- Google PageSpeed Insights: https://pagespeed.web.dev
- Web Vitals Guide: https://web.dev/vitals
