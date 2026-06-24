"""
Plantilla estándar Innovart Medical — Blogs
Versión aprobada: 23 junio 2026
"""
import re

def build_puntos_clave(items: list[str]) -> str:
    """Genera bloque 'Puntos clave' con diseño aprobado."""
    rows = ""
    for item in items:
        rows += f'<div style="display:flex;align-items:flex-start;gap:12px;background:#ffffff;border-radius:10px;padding:13px 16px;border:1px solid #D6E6F7;margin-bottom:8px;"><span style="flex-shrink:0;display:inline-block;width:24px;height:24px;background:#1D9E75;border-radius:50%;text-align:center;line-height:24px;color:#fff;font-size:13px;font-weight:800;">✓</span><span style="font-size:15px;line-height:1.6;color:#2B2F36;padding-top:2px;">{item}</span></div>'
    return f'<div style="box-sizing:border-box;width:100%;max-width:680px;margin:0 auto 28px;background:linear-gradient(135deg,#EAF2FB 0%,#EDF7F2 100%);border:1px solid #C8DCF0;border-radius:16px;padding:26px 28px;"><div style="display:flex;align-items:center;gap:10px;margin:0 0 18px;"><span style="display:inline-block;width:5px;height:28px;background:linear-gradient(180deg,#185FA5,#1D9E75);border-radius:3px;flex-shrink:0;"></span><span style="font-size:20px;font-weight:800;color:#0C447C;letter-spacing:-.01em;">Puntos clave</span></div>{rows}</div>'

def extract_puntos_items(body: str) -> list[str]:
    """Extrae los items del bloque Puntos clave actual."""
    # Match the old table format
    pattern = r'<td style="vertical-align:top;padding:7px 0;color:#2B2F36;font-size:16px;line-height:1\.55;">(.*?)</td>'
    items = re.findall(pattern, body, re.DOTALL)
    return [item.strip() for item in items]

def fix_whatsapp_url(body: str, handle: str, topic: str) -> str:
    """Actualiza la URL de WhatsApp con mensaje claro y bien codificado."""
    import urllib.parse
    msg = f"Hola, vi el blog de Innovart sobre {topic} y quiero una valoración gratuita."
    encoded = urllib.parse.quote(msg)
    new_url = f"https://wa.me/573124565014?text={encoded}"
    return re.sub(r'https://wa\.me/573124565014\?text=[^"]+', new_url, body)

def upgrade_body(body: str, handle: str, topic: str) -> str:
    """Aplica todas las mejoras de diseño al body de un artículo."""
    # 1. Extraer items actuales
    items = extract_puntos_items(body)
    
    if items:
        # 2. Construir nuevo bloque
        new_block = build_puntos_clave(items)
        # 3. Reemplazar el bloque viejo
        old_pattern = r'<div style="box-sizing:border-box;width:100%;max-width:680px;margin:0 auto 28px;background:#EAF2FB;border:1px solid #D6E6F7;border-radius:14px;padding:24px 26px;">.*?</table>\n</div>'
        body = re.sub(old_pattern, new_block, body, flags=re.DOTALL)
    
    # 4. Fijar URL de WhatsApp
    body = fix_whatsapp_url(body, handle, topic)
    
    return body

