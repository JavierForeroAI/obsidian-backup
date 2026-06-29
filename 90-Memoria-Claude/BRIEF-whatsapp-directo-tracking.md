---
name: BRIEF-whatsapp-directo-tracking
description: Documento maestro para implementar tracking de WhatsApp Directo en las 5 sub-cuentas GHL de Innovart
metadata:
  type: project
  date: 2026-06-28
  status: COMPLETADO
---

# BRIEF — Tracking WhatsApp Directo (5 Sedes)

## Estado: ✅ IMPLEMENTADO Y PUBLICADO (2026-06-28)

- ✅ Cuenta Principal — workflow publicado
- ✅ Bogotá — workflow publicado
- ✅ Medellín — workflow publicado
- ✅ Barranquilla — workflow publicado
- ✅ Bucaramanga — campos UTM creados + workflow publicado
- ✅ Panamá — workflow publicado

---

## Por qué existe este documento

El sistema Meta ↔ GHL estaba completamente desconectado. Se implementó tracking para:
- ✅ Landing forms (implantecapilarencolombia.com + Qikify innovartmedical.com)
- ✅ DM Instagram
- ✅ DM Facebook
- ✅ **WhatsApp Directo ← COMPLETADO 2026-06-28**

---

## Cómo llegan los leads de WA a GHL

Hay 3 tipos distintos — **no tratarlos igual**:

| Tipo | Origen | ctwa_clid | fbclid | Qué hace el workflow |
|---|---|---|---|---|
| **WA desde anuncio Click-to-WA** | Meta Ad con destino WA | ✅ presente | ❌ | utm_source=facebook, utm_medium=whatsapp_ads, tag fuente_whatsapp_ads |
| **WA desde botón en landing** | Botón WA en /home o Qikify (pauta → landing → WA) | ❌ | ✅ (capturado antes) | Solo tag fuente_whatsapp_landing |
| **WA directo orgánico** | Usuario escribe el número manualmente o de referido | ❌ | ❌ | utm_source=directo, utm_medium=whatsapp_organico, tag fuente_whatsapp_directo |

---

## Arquitectura de la solución

**Para CADA sub-cuenta GHL**, 1 workflow paralelo publicado:

```
Trigger: Customer Reply (primer mensaje entrante por WhatsApp, message.type == 3)
allowMultiple: false → solo una vez por contacto

Rama A: ctwa_clid tiene valor
   → utm_source = "facebook"
   → utm_medium = "whatsapp_ads"
   → Tag: "fuente_whatsapp_ads"
   
Rama B: ctwa_clid vacío + utm_source ya tiene valor
   → Tag: "fuente_whatsapp_landing"
   
Rama C: ctwa_clid vacío + utm_source vacío
   → utm_source = "directo"
   → utm_medium = "whatsapp_organico"
   → Tag: "fuente_whatsapp_directo"
```

---

## Sub-cuentas GHL — IDs, fields y workflow IDs

⚠️ Los tokens GHL (`pit-...`) NUNCA se guardan aquí. Se obtienen en runtime.

### Cuenta Principal (`NPhQTmLOHd6FbDtqLPnG`)
- utm_source: `ffBWPx4Qlhxb6D6toNWO`
- utm_medium: `46qWfYJubx8IAOhyFlgT`
- utm_campaign: `lPfZB842vcw2a7iD3tOD`
- utm_content: `hFUkJs1bRuGskcA6X5TA`
- ctwa_clid: `pmfzBxCFdjeojgCLmEWu` (ya existía)
- fbclid: `ROjbROGU9919xi7GR9rO`
- **Workflow ID:** `cf7e99e5-3efb-43ab-8775-c8b340428adc` — PUBLISHED v3

### Bogotá (`DgjjDzD9nkCKv8AGF1Qb`)
- utm_source: `bRG4YVkotWP9YjicYhnA`
- utm_medium: `GYiGihp4RIr2kVk34C2i`
- utm_campaign: `MBNCUu8uyZbQassuPs6r`
- utm_content: `ZZOmsPTSRhnKhUvSGgVu`
- ctwa_clid: `ebBHQovnCw3AgAij7BAA` (creado 2026-06-27)
- fbclid: `DnKbVMv2xH3kNEksDV5h`
- **Workflow ID:** `ec3d0cbb-f68b-4806-b3de-2a913cbcbafe` — PUBLISHED v3

### Medellín (`h8DplQKVE6epDbbj5Kg8`)
- utm_source: `kLMdTD6z21PLsxOVccGh`
- utm_medium: `LBRvQTYSAxKyWSATOvOG`
- utm_campaign: `EYtlSV5Zo5bIFMWrt7zd`
- utm_content: `fkLu6dW4S2Qq61NlM20J`
- ctwa_clid: `4V2IZiwCCkLdt0jTUI8K` (ya existía)
- fbclid: `BS2KOGaMzTsjCzTx1D3R`
- **Workflow ID:** `2fe984c3-6ac1-454c-8e6c-8debd3326969` — PUBLISHED v3

### Barranquilla (`cXH8KbMaAPGzkmf3Z2pP`)
- utm_source: `syjwhDFSmmEm0An4mzIS`
- utm_medium: `gVOYkuBVKWNa2kHH8z86`
- utm_campaign: `d5m9y1LDbWO6nApy0GbK`
- utm_content: `5sfjctlQMOFuvm2KUXxP`
- ctwa_clid: `lr9AYYbE3MKxcbMqGOew` (ya existía)
- fbclid: `1Cz1rZn3TCW33fqqBraX`
- **Workflow ID:** `e1c8709e-a55a-4aee-ad18-e1c86376ce35` — PUBLISHED v3

### Bucaramanga (`s40Wa8mXYBxlFCieKohO`)
- utm_source: `nPJRTlPWxcVrKVKki0sF` (creado 2026-06-27)
- utm_medium: `8vZkuEdu6n6yZYI7xn5V` (creado 2026-06-27)
- utm_campaign: `YFaOUsGEEZVT5fFSTjJf` (creado 2026-06-27)
- utm_content: `vPllZizKTgC0gCef9p6H` (creado 2026-06-27)
- ctwa_clid: `UHB4VHlBQ2XnnZODeGRK` (ya existía)
- fbclid: `oWCS5H4uG9OcoNvOfzdz`
- **Workflow ID:** `d10dcfdc-5d04-4485-b10b-991450141203` — PUBLISHED v3

### Panamá (`45SKYgIDgr4Eh6a6JcFz`)
- utm_source: `hgwZIIgLsNOrkBYbHXKq`
- utm_medium: `tb4eGy7QDPj1Dql87zjp`
- utm_campaign: `MMl9tbuRuLbkfOfjqVvc`
- utm_content: `vdAmS14XgkvqbTqgqTyr`
- ctwa_clid: `Ckdb2494518FRWLHLb7n` (ya existía)
- fbclid: `z05PZy9bRVBJKRjEyBRH`
- **Workflow ID:** `5722994e-4a17-416b-bec4-fa12283d2f48` — PUBLISHED v3

---

## ⏳ Paso 4 — Verificar con prueba E2E (pendiente)

Enviar mensaje WA de prueba a cada número de WhatsApp Business:
1. Desde un anuncio Click-to-WA activo → verificar tag `fuente_whatsapp_ads` + utm_source=facebook
2. Desde botón WA en landing (con UTMs en URL) → verificar tag `fuente_whatsapp_landing`
3. Número directo sin anuncio → verificar tag `fuente_whatsapp_directo` + utm_source=directo

---

## Workflows existentes — NO tocar
- `3. Recibir msj IG` (ID: `da35ea2a-...`) — NO MODIFICAR
- `2. Recibir msj FB` (ID: `9cae02ee-...`) — NO MODIFICAR
- `0.1 SMS GPT` — NO MODIFICAR

---

## Referencias
- [[utm-tracking-avance-general]] — Estado de todas las fuentes
- [[feedback-cuentas-meta-no-son-sedes]] — REGLA: nombres de cuenta ≠ sedes
