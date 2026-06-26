# Setup: Sincronización GHL → Obsidian

**Objetivo:** Cada compra en GHL → actualiza automáticamente cliente en Obsidian

---

## ✅ Opción 1: Webhook Local (Simple)

### Paso 1: Instala ngrok (expone tu PC a internet)

```bash
# Descarga desde https://ngrok.com/download
# O con brew:
brew install ngrok
```

### Paso 2: Inicia el webhook handler

```bash
python3 /Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/workflows-ghl/webhook_handler.py
```

Output esperado:
```
╔═══════════════════════════════════════════════╗
║    WEBHOOK HANDLER — Escuchando en :8888     ║
╚═══════════════════════════════════════════════╝
⏳ Escuchando webhooks...
```

### Paso 3: Expone con ngrok

En otra terminal:
```bash
ngrok http 8888
```

Verás algo como:
```
Forwarding  https://abc123def456.ngrok.io -> http://localhost:8888
```

**Copia la URL:** `https://abc123def456.ngrok.io`

### Paso 4: Registra webhook en GHL

1. Ve a **GHL → Settings → Webhooks** (en CADA subcuenta de Innovart)
2. Click **+ Add Webhook**
3. **URL:** `https://abc123def456.ngrok.io` (tu URL ngrok)
4. **Events:** Marca:
   - ✅ `order.completed`
   - ✅ `contact.updated`
5. **Secret:** (lo generará GHL) → cópialo y pega en `webhook_handler.py` línea 11:
   ```python
   GHL_WEBHOOK_SECRET = "abc123...xyz"
   ```
6. Click **Save**

### Paso 5: Prueba

Crea una orden de prueba en GHL → deberías ver:
```
🔔 Webhook recibido: order.completed
   📦 Orden: ORD-12345
   💰 Monto: $50000
   ✅ Actualizado: cliente-cedula.md
```

---

## 🚀 Opción 2: Cloudflare Workers (Recomendado — Sin tu PC)

### Ventajas
- Cero mantenimiento
- Siempre activo (no necesita tu PC prendido)
- Escalable
- Gratis tier

### Paso 1: Crea un Cloudflare Worker

1. Ve a https://dash.cloudflare.com
2. **Workers** → **Create Service**
3. Nombre: `innovart-ghl-sync`
4. Edita el código:

```javascript
export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('Not Found', { status: 404 });
    }

    const body = await request.text();
    const signature = request.headers.get('X-GHL-Signature');
    
    // Validar firma
    const secret = env.GHL_SECRET;
    const hash = await crypto.subtle.sign(
      'HMAC',
      await crypto.subtle.importKey('raw', new TextEncoder().encode(secret), 
        { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']),
      new TextEncoder().encode(body)
    );
    
    const hex = Array.from(new Uint8Array(hash))
      .map(b => b.toString(16).padStart(2, '0'))
      .join('');
    
    if (signature !== hex) {
      return new Response('Invalid Signature', { status: 401 });
    }

    const data = JSON.parse(body);
    const evento = data.type;
    const payload = data.data;

    // Procesar compra
    if (evento === 'order.completed') {
      const email = payload.email;
      const monto = payload.total;
      
      // Aquí irá el código para actualizar Obsidian
      // Por ahora, solo log
      console.log(`✅ Orden completada: ${email} - $${monto}`);
    }

    return new Response(JSON.stringify({ status: 'ok' }), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
```

5. **Secrets:** Click **Settings** → **Add Secret**
   - Nombre: `GHL_SECRET`
   - Valor: (el secret que GHL te da)

6. **Deploy**

7. Tu URL será: `https://innovart-ghl-sync.tudominio.workers.dev`

### Paso 2: Registra en GHL

Igual que Opción 1, pero con la URL del Worker.

---

## ⚙️ Configuración Final

### Para todas las subcuentas de Innovart:
1. **BOGOTA-USD**
2. **MEDELLIN**
3. **BARRANQUILLA**
4. **QUILLA**
5. **LANDING DIEGO**
6. **INTERACCION REDES DIEGO**

Repite los pasos de webhook en CADA una.

---

## 🔍 Cómo Verificar

### Logs locales
```bash
tail -f /tmp/ghl_webhook.log
```

### En Obsidian
- Abre `clientes/` 
- Busca un cliente con compra reciente
- Deberías ver una sección "Transacción YYYY-MM-DD HH:MM"

### Ejemplo de actualización:

```markdown
### Transacción 2026-06-25 14:30
- **Tipo:** COMPRA
- **Monto:** $500000
- **Productos:** KIT COMPLETO, SHAMPOO
- **Orden:** ORD-abc123
- **Fuente:** GHL Webhook
```

---

## 🆘 Troubleshooting

| Problema | Solución |
|----------|----------|
| "Signature inválida" | Verifica que el secret en el script = secret en GHL |
| No llegan webhooks | Revisa que el evento esté activado en GHL settings |
| ngrok desconecta | ngrok desconecta cada 8h en tier gratis; usa Worker para 24/7 |
| Cliente no encontrado | Verifica que el email en GHL coincida exactamente con Obsidian |

---

## 📌 Próximos Pasos

1. **Elige opción** (Local o Worker)
2. **Setup del webhook**
3. **Test con orden de prueba**
4. **Verifica archivo en Obsidian**

¿Necesitas ayuda con alguno de estos pasos?
