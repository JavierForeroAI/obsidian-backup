---
name: ghl-whatsapp-tipos-lineas
description: Dos tipos de WhatsApp en GHL — API (Meta Business) y Applevel (Business) — se comportan distinto como triggers. CRÍTICO para configurar filtros correctamente.
metadata:
  type: project
  date: 2026-06-28
---

# Dos Tipos de WhatsApp en GHL — Innovart

## Las dos líneas

| Nombre interno | Tipo de conexión | message.type en GHL | Reply channel en GHL |
|---|---|---|---|
| **WhatsApp de API** | Conectado con Meta Business (API oficial) | **19** (en trigger `type:"select"`) | WhatsApp |
| **WhatsApp Business de Applevel** | Conectado vía Applevel (LC Phone/Twilio) | **2** (en trigger `type:"select"`) | SMS |

⚠️ El valor `3` aparece en la API de mensajes/conversaciones de GHL (cuando lees un mensaje), pero en el sistema de TRIGGERS el campo `message.type` usa valores distintos: **19 = WhatsApp API, 2 = Applevel SMS**. No confundirlos.

**Ambas líneas reciben tráfico de pauta** — se les hace publicidad a las dos.

## Regla crítica para triggers GHL

> WhatsApp conectado vía **Applevel aparece como SMS** en GHL (message.type = 2), NO como WhatsApp (message.type = 3).

Si un workflow tiene trigger `Customer replied` con filtro `Reply channel = WhatsApp`, **NO capturará mensajes del número Applevel** — esos llegan como SMS.

## Implicación para UTM - WA Directo Tracker

Para capturar mensajes de AMBAS líneas, el trigger debe:
- **Opción A**: Sin filtro de canal (captura todo: WA, SMS, IG, FB, Email) + depender de `allowMultiple: false`
- **Opción B**: Dos triggers separados — uno `Reply channel = WhatsApp` + uno `Reply channel = SMS`
- **Opción C**: Filtrar solo por la línea que sea relevante para esa sub-cuenta

**Pendiente confirmar**: qué sub-cuentas usan WhatsApp de API vs Applevel.

## Por qué importa

Si el tracker solo filtra `WhatsApp`, perderá todos los leads que entren por el número Applevel (aparecen como SMS). El resultado: leads sin UTMs, EMQ bajo, show rate sin mejorar.

## Relacionado
- [[BRIEF-whatsapp-directo-tracking]]
- [[utm-tracking-avance-general]]
- [[stack-pauta]]
