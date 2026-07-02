---
name: mcp-n8n-reconfiguracion-2026-07-01
description: MCP de n8n renombrado a mcpN8N con token nuevo, scope user (todas las terminales) — el anterior "n8n" quedó con token revocado (401)
metadata:
  type: reference
---

# MCP de N8N — reconfiguración 2026-07-01

**Contexto:** El MCP `n8n` (proceso `node /Users/javierforero/n8n-mcp/index.js`, apunta a `https://herramientas-n8n.xtcjgv.easypanel.host/api/v1`) tenía el token revocado — Javier lo había borrado desde n8n porque otra terminal reportó que "no teníamos nada" configurado. Daba 401 unauthorized.

## Qué se hizo
1. Javier generó un token nuevo desde n8n (Settings → n8n API → Create an API key).
2. Se removió el servidor `n8n` y se creó de nuevo con el token nuevo, en **scope `user`** (disponible automáticamente en todas las terminales/proyectos, sin config adicional).
3. A pedido de Javier, se **renombró de `n8n` a `mcpN8N`**.

## Estado actual
- **Nombre del servidor MCP:** `mcpN8N` (las herramientas aparecen como `mcp__mcpN8N__*`, ej. `mcp__mcpN8N__n8n_list_workflows`).
- **Scope:** user — todas las terminales lo heredan sin configurar nada.
- **Requiere reiniciar sesión de Claude Code** para que cada terminal tome el nombre/token nuevos (el proceso ya abierto se queda con la config vieja en memoria hasta reiniciar).
- **Uso:** no hace falta invocar el nombre del MCP — basta pedir en lenguaje natural ("lista los workflows de n8n", "activa el workflow X", "revisa las credenciales") y Claude usa la herramienta correspondiente de `mcpN8N`.

## Nota de seguridad
El token (`N8N_API_KEY`, JWT) pasó por el chat en texto plano una vez. Si se necesita rotar de nuevo, repetir: generar token nuevo en n8n → `claude mcp remove mcpN8N -s user && claude mcp add mcpN8N -s user -e N8N_API_KEY=<TOKEN> -- node /Users/javierforero/n8n-mcp/index.js`.
