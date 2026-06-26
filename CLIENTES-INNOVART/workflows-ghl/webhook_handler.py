#!/usr/bin/env python3
"""
WEBHOOK HANDLER — GHL → Obsidian Sync
Escucha eventos de compra en GHL y actualiza archivos de clientes en Obsidian

Eventos soportados:
  - order.completed
  - order.created
  - contact.updated
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import hashlib
import hmac
from datetime import datetime
from pathlib import Path
import re

# Configuración
OBSIDIAN_DIR = Path('/Users/javierforero/Documents/Obsidian-Innovart/CLIENTES-INNOVART/clientes')
GHL_WEBHOOK_SECRET = "tu-webhook-secret"  # ← REEMPLAZAR CON EL REAL DE GHL
PORT = 8888

class GHLWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Maneja POST de webhooks de GHL"""
        # Validar firma
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        # Verificar HMAC
        signature = self.headers.get('X-GHL-Signature', '')
        expected_sig = hmac.new(
            GHL_WEBHOOK_SECRET.encode(),
            body,
            hashlib.sha256
        ).hexdigest()

        if signature != expected_sig:
            print(f"❌ Firma inválida: {signature}")
            self.send_response(401)
            self.end_headers()
            return

        try:
            data = json.loads(body)
            evento = data.get('type')
            payload = data.get('data', {})

            print(f"\n🔔 Webhook recibido: {evento}")
            print(f"   Payload: {json.dumps(payload, indent=2)}")

            # Procesar por tipo de evento
            if evento == 'order.completed':
                self._procesar_orden_completada(payload)
            elif evento == 'contact.updated':
                self._procesar_contacto_actualizado(payload)
            else:
                print(f"   ⚠️  Evento no manejado: {evento}")

            # Responder OK
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok'}).encode())

        except Exception as e:
            print(f"❌ Error procesando webhook: {e}")
            self.send_response(500)
            self.end_headers()

    def _procesar_orden_completada(self, payload):
        """Procesa compra completada"""
        # Extraer info de la orden
        orden_id = payload.get('id')
        cliente_id = payload.get('contactId')
        cliente_email = payload.get('email')
        cliente_nombre = payload.get('contactName')
        monto = payload.get('total', 0)
        productos = payload.get('products', [])
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M')

        print(f"   📦 Orden: {orden_id}")
        print(f"   💰 Monto: ${monto}")
        print(f"   👤 Cliente: {cliente_nombre} ({cliente_email})")

        # Buscar cliente en Obsidian
        archivo = self._buscar_cliente(cliente_email, cliente_nombre)

        if archivo:
            self._actualizar_cliente(archivo, {
                'tipo': 'COMPRA',
                'monto': monto,
                'productos': productos,
                'fecha': fecha,
                'orden_id': orden_id,
                'fuente': 'GHL Webhook'
            })
            print(f"   ✅ Actualizado: {archivo.name}")
        else:
            print(f"   ⚠️  Cliente no encontrado: {cliente_email}")

    def _procesar_contacto_actualizado(self, payload):
        """Procesa actualización de contacto"""
        cliente_email = payload.get('email')
        cliente_nombre = payload.get('firstName') + ' ' + payload.get('lastName', '')

        archivo = self._buscar_cliente(cliente_email, cliente_nombre)

        if archivo:
            print(f"   ✅ Contacto actualizado: {archivo.name}")

    def _buscar_cliente(self, email, nombre):
        """Busca archivo de cliente por email o nombre"""
        email_clean = email.lower().strip() if email else ''

        # Buscar por email en fronmatter
        for archivo in OBSIDIAN_DIR.glob('*.md'):
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    # Extraer email del frontmatter
                    match = re.search(r'email:\s*([^\n]+)', contenido)
                    if match:
                        archivo_email = match.group(1).strip()
                        if archivo_email.lower() == email_clean:
                            return archivo
            except:
                pass

        return None

    def _actualizar_cliente(self, archivo, compra_info):
        """Actualiza archivo de cliente con nueva compra"""
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Separar frontmatter del contenido
        partes = contenido.split('---')
        if len(partes) >= 3:
            frontmatter = partes[1]
            body = '---'.join(partes[2:])
        else:
            frontmatter = ''
            body = contenido

        # Actualizar metadata en frontmatter
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        frontmatter = re.sub(
            r'fecha_ultima:\s*[^\n]+',
            f'fecha_ultima: {fecha_actual}',
            frontmatter
        )

        # Agregar nueva transacción en el cuerpo
        nueva_transaccion = f"""

### Transacción {datetime.now().strftime('%Y-%m-%d %H:%M')}
- **Tipo:** {compra_info['tipo']}
- **Monto:** ${compra_info['monto']:,.0f}
- **Productos:** {', '.join(compra_info['productos'])}
- **Orden:** {compra_info['orden_id']}
- **Fuente:** {compra_info['fuente']}
"""

        # Reconstruir archivo
        contenido_actualizado = f"---{frontmatter}---{body}{nueva_transaccion}"

        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_actualizado)

        print(f"      ✍️  Actualizado: {compra_info['tipo']} - ${compra_info['monto']:,.0f}")

    def log_message(self, format, *args):
        """Suprimir logs de acceso HTTP estándar"""
        pass


def main():
    server = HTTPServer(('0.0.0.0', PORT), GHLWebhookHandler)
    print(f"""
    ╔═════════════════════════════════════════════════════════╗
    ║         WEBHOOK HANDLER — GHL → Obsidian              ║
    ║                                                         ║
    ║  Escuchando en: http://localhost:{PORT}               ║
    ║  Obsidian Dir: {OBSIDIAN_DIR}         ║
    ║                                                         ║
    ║  Para registrar en GHL:                               ║
    ║  1. Ve a GHL → Webhooks                               ║
    ║  2. URL: http://tu-ip:8888                            ║
    ║  3. Events: order.completed, contact.updated          ║
    ║  4. Secret: (igual a GHL_WEBHOOK_SECRET)              ║
    ║                                                         ║
    ║  NOTA: Si estás en local, usa ngrok para exponer      ║
    ║  ngrok http 8888                                       ║
    ╚═════════════════════════════════════════════════════════╝
    """)
    print(f"⏳ Escuchando webhooks...")
    server.serve_forever()


if __name__ == '__main__':
    main()
