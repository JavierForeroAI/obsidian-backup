---
name: google-ads-mcp-conexion
description: Conexión del MCP oficial de Google Ads a Claude Code (solo lectura) — credenciales, scripts, cómo reconectar y regenerar el refresh token
metadata:
  type: integration
  updated: 2026-06-19
---

# Google Ads MCP — Conexión a Claude Code (solo lectura)

> 2026-06-19. Se conectó el **MCP oficial de Google** (`google-marketing-solutions/google_ads_mcp`)
> a Claude Code en el Mac de Javier, en modo **SOLO LECTURA** (sin `ADS_MCP_ENABLE_MUTATIONS`).
> Sirve para ver campañas/métricas en vivo y pasarle mejoras al trafficker; NO modifica la cuenta.
> Complementa (no reemplaza) los agentes/skills de [[google-ads-guia]].

## Por qué SOLO LECTURA
El MCP oficial de Google en su versión actual **solo lee** (diagnóstico/analítica). No pausa
campañas, no cambia presupuestos ni crea anuncios. Para escritura habría que usar un MCP de
terceros (más riesgo) o `ADS_MCP_ENABLE_MUTATIONS=true` cuando el oficial lo soporte. Decisión de
Javier: quedarse en lectura, los cambios los ejecuta el trafficker.

## Nivel de acceso de la API
- Developer token en **Basic Access** (15.000 operaciones/día) → suficiente, accede a cuentas reales.
- **Standard Access fue NEGADO** por Google (correo del equipo de Compliance) — es normal: solo lo dan
  cuando topas el límite con errores `RESOURCE_EXHAUSTED`. No se necesita para Innovart. No reaplicar
  hasta que el volumen lo exija.

## Datos de la conexión (identificadores, NO secretos)
- **Proyecto Google Cloud:** `innovart-google-ads-mcp` (project id `silent-blade-497118-t4`).
- **OAuth Client:** tipo **App de escritorio (Desktop)** llamado "Claude MCP Innovart Desktop".
  (Había un cliente previo tipo "Aplicación web" `Innovart Mcp web client` — NO se usa, da problemas
  con el flujo loopback local.)
- **login_customer_id (MCC):** `2084232674`.
- **Pantalla de consentimiento:** modo *Testing*, con `innovartmedicalips@gmail.com` como usuario de prueba
  (Google Auth Platform → pestaña "Público" → Usuarios de prueba). Sin esto, OAuth bloquea con
  "Acceso no autorizado".
- **Scope:** `https://www.googleapis.com/auth/adwords`.

## Archivos en el Mac (`/Users/javierforero/`)
- **`google-ads.yaml`** ← credenciales (developer_token, client_id, client_secret, refresh_token,
  login_customer_id, use_proto_plus). ⚠️ Contiene secretos, no commitear ni exponer.
- **`get_refresh_token.py`** ← genera/renueva el refresh_token. Lee client_id/secret del yaml, abre el
  navegador (InstalledAppFlow loopback), y reescribe `refresh_token` en el yaml. Correr con:
  `uv run /Users/javierforero/get_refresh_token.py`
- **`Downloads/conectar-google-ads-claude.html`** ← guía interactiva (8 pasos, casillas, botón que arma
  el `google-ads.yaml` y el comando todo-en-uno). Para futuras reconexiones o enseñar el proceso.

## Comando de conexión del MCP (registrado en `~/.claude.json`, scope local)
⚠️ **NO usar `uvx --from git+...` directo** como comando del MCP: revisa GitHub en cada arranque y se
pasa del timeout del health check → "✘ Failed to connect" (aunque el server sí funcione). 

**Método correcto (binario fijo, arranque instantáneo):**
```
# 1) instalar el server como herramienta persistente (compila 1 vez)
uv tool install --force "git+https://github.com/google-marketing-solutions/google_ads_mcp.git"
#    → instala 2 binarios en ~/.local/bin/: run-mcp-server y run-mcp-server-stdio
# 2) registrar el MCP apuntando al binario STDIO directo
claude mcp add google-ads -e GOOGLE_ADS_CREDENTIALS=/Users/javierforero/google-ads.yaml -- \
  /Users/javierforero/.local/bin/run-mcp-server-stdio
```
- Para Claude (cliente stdio) usar **`run-mcp-server-stdio`**, no `run-mcp-server`.
- Verificado: `claude mcp get google-ads` → **✔ Connected**. Server = "Google Ads API" v3.4.2.
- El MCP **solo se carga al reiniciar** la sesión. Javier usa Claude en **terminal** → salir y reabrir `claude`.
- Actualizar el server en el futuro: `uv tool upgrade google-ads-mcp`.

## Cómo regenerar el refresh_token (si caduca o se revoca)
Caduca si: no se usa 6 meses, cambio de password, o cambio de scope.
```
uv run /Users/javierforero/get_refresh_token.py
```
Autorizar en el navegador (en "Google no ha verificado esta app" → Continuar) → se reescribe solo en el yaml.

## ⚠️ Seguridad pendiente
Las credenciales (developer_token, client_secret, refresh_token) pasaron por el chat al configurarlas
→ considerar **rotar el client_secret** en Google Cloud (Credenciales → editar cliente Desktop) por higiene.
Mismo patrón que el token de Clarity [[clarity-mcp-microsoft]].

**Ver también:**
- [[google-ads-guia]] — agentes, skills, flujo de trabajo, cuentas y métricas
- [[google-politicas-publicitarias]] — cumplimiento salud/estética
- [[meta-mcp-guia]] — equivalente para Meta (meta-dajf)
