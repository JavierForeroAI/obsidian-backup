---
name: meta-mcp-guia
description: Guía de uso del MCP meta-dajf para gestión de Meta Ads — cuentas disponibles, herramientas y flujo de trabajo
metadata:
  type: reference
  updated: 2026-05-29
---

# Guía MCP Meta Ads (meta-dajf)

## Conexión verificada

Conexión confirmada el 2026-05-29. Token válido con 18 scopes incluyendo `ads_management`, `ads_read`, `leads_retrieval`. Todas las cuentas activas bajo Business Manager **Implante Innovart Medical** (BM ID: `940287337027000`).

---

## Cuentas Publicitarias Disponibles

| Nombre | ID | Moneda | Balance |
|---|---|---|---|
| BGTA | `act_187478780709376` | USD | $5,603 |
| QUILLA | `act_676872971127807` | USD | $0 |
| PANAMA | `act_1049078199582559` | USD | $8,521 |
| INTERACCION REDES DIEGO | `act_885062283062302` | COP | $0 |
| LANDING DIEGO | `act_1176352666815422` | COP | $29,760 |
| MEDELLIN | `act_874169544322810` | COP | $894,858 |

Todas en zona horaria: `America/Bogota` | `account_status: 1` (activas)

---

## Herramientas Disponibles en meta-dajf

### Autenticación
| Tool | Uso |
|---|---|
| `health_check` | Verificar que la conexión MCP funciona |
| `validate_token` | Verificar validez del token de acceso |
| `get_token_info` | Ver permisos y scopes del token |
| `generate_auth_url` | Generar URL de autenticación OAuth |
| `exchange_code_for_token` | Intercambiar código por token |
| `refresh_to_long_lived_token` | Renovar token a larga duración |
| `generate_system_user_token` | Generar token de usuario de sistema |

### Cuentas y Configuración
| Tool | Uso |
|---|---|
| `get_ad_accounts` | Listar todas las cuentas publicitarias |
| `get_capabilities` | Ver capacidades disponibles en la cuenta |

### Campañas
| Tool | Uso |
|---|---|
| `list_campaigns` | Listar campañas de una cuenta |
| `get_campaign` | Detalle de una campaña específica |
| `create_campaign` | Crear nueva campaña |
| `update_campaign` | Actualizar campaña existente |
| `pause_campaign` | Pausar campaña |
| `resume_campaign` | Reanudar campaña pausada |
| `delete_campaign` | Eliminar campaña |

### Conjuntos de Anuncios (Ad Sets)
| Tool | Uso |
|---|---|
| `list_ad_sets` | Listar ad sets de una campaña |
| `create_ad_set` | Crear nuevo ad set con segmentación y presupuesto |

### Anuncios y Creativos
| Tool | Uso |
|---|---|
| `list_ads` | Listar anuncios de un ad set |
| `list_creatives` | Listar creativos disponibles |
| `create_ad_creative` | Crear nuevo creativo |
| `update_creative` | Actualizar creativo existente |
| `delete_creative` | Eliminar creativo |
| `preview_ad` | Vista previa de un anuncio |
| `upload_creative_asset` | Subir imagen o video |

### Audiencias
| Tool | Uso |
|---|---|
| `list_audiences` | Listar audiencias personalizadas |
| `create_custom_audience` | Crear audiencia personalizada |
| `create_lookalike_audience` | Crear audiencia lookalike |
| `update_custom_audience` | Actualizar audiencia |
| `delete_audience` | Eliminar audiencia |
| `estimate_audience_size` | Estimar tamaño de audiencia |
| `get_audience_insights` | Insights de audiencia |

### Métricas y Análisis
| Tool | Uso |
|---|---|
| `get_insights` | Métricas de rendimiento (impresiones, clics, conversiones, CPC, CTR, ROAS) |
| `get_campaign_performance` | Rendimiento específico de campaña |
| `get_creative_performance` | Rendimiento por creativo |
| `get_attribution_data` | Datos de atribución |
| `compare_performance` | Comparar rendimiento entre campañas/periodos |
| `export_insights` | Exportar datos de insights |

### Pruebas A/B
| Tool | Uso |
|---|---|
| `setup_ab_test` | Configurar prueba A/B |

---

## Flujo de Trabajo Recomendado

### Para Crear una Campaña Nueva
```
1. health_check → confirmar conexión
2. get_ad_accounts → seleccionar cuenta objetivo
3. [Verificar cumplimiento con [[meta-politicas-publicitarias]]]
4. create_campaign → definir objetivo, nombre, estado
5. create_ad_set → segmentación, presupuesto, placements
6. upload_creative_asset → subir imagen/video si necesario
7. create_ad_creative → construir el anuncio
8. preview_ad → revisar antes de activar
```

### Para Auditar Rendimiento
```
1. list_campaigns → obtener IDs activos
2. get_campaign_performance → métricas generales
3. get_creative_performance → identificar creativos ganadores/perdedores
4. compare_performance → comparar periodos o campañas
```

### Para Gestión de Audiencias
```
1. list_audiences → ver audiencias existentes
2. estimate_audience_size → validar tamaño antes de crear
3. create_custom_audience → subir lista de clientes/leads
4. create_lookalike_audience → expandir desde audiencia base
```

---

## Reglas de Cumplimiento — Siempre Aplicar

> Antes de crear cualquier campaña o creativo, verificar [[meta-politicas-publicitarias]].

Puntos críticos para Innovart Medical IPS:
- Segmentación de salud/estética: **solo +18**
- No implicar "cuerpo ideal" ni autopercepción negativa en creativos
- No solicitar datos de salud en leads sin permiso especial de Meta
- Landing page debe coincidir con el anuncio
- Usar cuentas separadas por ciudad/mercado (ya configurado correctamente)

---

## Notas Técnicas

- **Parámetro obligatorio en casi todas las tools:** `account_id` — usar los IDs de la tabla de arriba
- **Formato de ID:** siempre con prefijo `act_` (ej: `act_187478780709376`)
- **Zona horaria:** todas las cuentas en `America/Bogota`
- **Business Manager ID:** `940287337027000`
