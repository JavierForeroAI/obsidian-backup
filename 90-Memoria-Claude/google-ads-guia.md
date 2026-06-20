---
name: google-ads-guia
description: Guía de trabajo con Google Ads desde Claude — agentes disponibles, skills, flujo de trabajo y cuentas de Innovart
metadata:
  type: reference
  updated: 2026-06-19
---

# Guía de Google Ads desde Claude

> ✅ **ACTUALIZACIÓN 2026-06-19:** Google Ads YA tiene MCP conectado (oficial de Google, modo **solo lectura**).
> Ver detalles de la conexión en [[google-ads-mcp-conexion]].
> Además siguen disponibles los **agentes especializados** y **skills** para análisis profundo.

---

## Herramientas Disponibles

### 1. Agente Especializado — `audit-google`
**Qué hace:** Auditoría completa de cuentas Google Ads.

Analiza:
- Conversiones y tracking (píxel, etiquetas de conversión)
- Gasto desperdiciado (palabras clave negativas, términos irrelevantes)
- Estructura de cuenta (campañas, grupos de anuncios, keywords)
- Quality Score y extensiones de anuncio
- Campañas Performance Max (PMax)
- Estrategias de puja y configuración
- Activos de anuncio y variaciones

**Cómo invocar:**
```
Usa el agente audit-google para auditar la cuenta [ID]
```

### 2. Skill — `/ads-google`
**Qué hace:** Análisis profundo y optimización de campañas Google Ads. Incluye:
- Revisión de keywords, Quality Score y estructura
- Identificación de oportunidades de mejora
- Recomendaciones de puja y presupuesto

### 3. Skill — `/ads-audit`
**Qué hace:** Auditoría multi-plataforma que incluye Google Ads como parte de un análisis completo de paid media.

### 4. Skill — `/ads-budget`
**Qué hace:** Análisis y optimización de presupuesto y pujas en Google Ads.

### 5. Skill — `/ads`
**Qué hace:** Skill maestro de paid advertising — orquesta análisis en Google, Meta, YouTube, LinkedIn, TikTok, Microsoft y Apple Search Ads. Incluye 225+ verificaciones.

### 6. Skill — `/ads-create`
**Qué hace:** Creación de nuevas campañas y estructuras publicitarias.

### 7. Skill — `/ads-creative`
**Qué hace:** Generación y optimización de creativos y copy para anuncios.

### 8. Skill — `/ads-landing`
**Qué hace:** Análisis y optimización de landing pages para campañas de pago.

### 9. Skill — `/ads-math`
**Qué hace:** Cálculos de métricas: ROAS, CPA objetivo, presupuesto mínimo, proyecciones.

---

## Flujo de Trabajo Recomendado

### Para Auditar una Cuenta Existente
```
1. Exportar datos de Google Ads (keywords, campañas, métricas) como CSV
2. Compartir los archivos con Claude
3. Invocar: /ads-google o agente audit-google
4. Revisar recomendaciones priorizadas por impacto
```

### Para Crear una Campaña Nueva
```
1. [Verificar cumplimiento con [[google-politicas-publicitarias]]]
2. /ads-create → definir objetivo, tipo de campaña, estructura
3. /ads-creative → generar copies y variaciones de anuncio
4. /ads-landing → auditar landing page de destino
5. Implementar en Google Ads Manager
```

### Para Optimización de Presupuesto
```
1. Exportar datos de rendimiento (últimos 30-90 días)
2. /ads-math → calcular CPA objetivo, ROAS mínimo, distribución óptima
3. /ads-budget → recomendaciones de reasignación de presupuesto
```

### Para Análisis Competitivo
```
1. /ads-competitor → análisis de competidores en Google Search
2. Identificar gaps de keywords y oportunidades de copy
```

---

## Cuentas Google Ads de Innovart

> ⚠️ Confirmar IDs reales conectando directamente a Google Ads Manager.
> Las cuentas de Meta están separadas de Google — verificar MCC (My Client Center) de Innovart.

**Business Manager asociado:** Implante Innovart Medical
**Mercados activos:** Bogotá (BGTA), Barranquilla (QUILLA), Panamá, Medellín
**Monedas:** USD (BGTA, QUILLA, PANAMA) | COP (MEDELLIN, LANDING DIEGO)

---

## Métricas Clave a Monitorear

| Métrica | Benchmark Referencia | Alerta si... |
|---|---|---|
| CTR (Search) | 3-5% en salud/estética | < 2% |
| Quality Score | 7-10 ideal | < 5 en keywords principales |
| CPA | Según objetivo por ciudad | > 2x CPA objetivo |
| ROAS | > 3x mínimo | < 2x |
| Impression Share | > 60% en branded | < 40% |
| Conversion Rate | 2-5% en landing médica | < 1% |

---

## Tipos de Campaña Relevantes para Innovart

| Tipo | Uso Recomendado |
|---|---|
| **Search** | Captura demanda activa: "implante capilar Bogotá", "trasplante de cabello" |
| **Performance Max** | Ampliación de alcance con señales de audiencia de clientes actuales |
| **Display Remarketing** | Recuperar visitantes del sitio que no convirtieron |
| **YouTube** | Video testimoniales / antes-después (cumplir políticas de salud) |
| **Demand Gen** | Audiencias similares a pacientes actuales |

---

## Reglas de Cumplimiento — Siempre Aplicar

> Antes de crear cualquier campaña o anuncio, verificar [[google-politicas-publicitarias]].

**Puntos críticos para Innovart Medical IPS:**
- Categoría de salud → posible requisito de certificación según país
- No prometer resultados específicos ("recupera el 100%", "cura garantizada")
- Landing page debe coincidir exactamente con el anuncio
- No usar lenguaje terapéutico sin respaldo clínico
- Excluir categorías sensibles de salud en audiencias de remarketing
- Cumplir leyes locales de publicidad médica en Colombia y Panamá

---

## Integración con el Ecosistema Innovart

```
Google Ads (leads) → Landing Page → Formulario → GHL (CRM) → WhatsApp → Bot IA → Consulta
```

- **Conversiones a trackear:** Formulario enviado, Clic en WhatsApp, Llamada telefónica
- **Audiencias de remarketing:** Visitantes sin conversión, Pacientes actuales (CRM upload)
- **Lookalike:** Basado en lista de pacientes convertidos

**Ver también:**
- [[meta-politicas-publicitarias]] — Políticas de Meta para comparación
- [[meta-mcp-guia]] — Cuentas y herramientas de Meta Ads
- [[stack-pauta]] — Stack completo de pauta y CRM
- [[crm-funnel]] — Volumen de leads y funnel
