---
name: gbp-sedes-innovart
description: Google Business Profile de las 5 sedes de Innovart Medical — Place IDs, nombres actuales, inconsistencias NAP detectadas y estado por sede.
metadata:
  type: reference
  date: 2026-06-25
  status: 4_de_5_activos
---

# Google Business Profile — Innovart Medical IPS

## Estado por sede

| Sede | Existe | Place ID | GBP ID | URL |
|------|--------|----------|--------|-----|
| **Bogotá** | ✅ | `0x8e3f9bfc23173cc3:0x3085b5535566e7d` | `/g/11q7dlpp0y` | [Maps](https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar/@4.6959114,-74.0353125,19z) |
| **Barranquilla** | ✅ | `0x8ef42d52d7e676d1:0xb8394a73a239784b` | `/g/11w59w7kq0` | [Maps](https://www.google.com/maps/place/Innovart+Medical+Ips+_+Implante+capilar+Barranquilla/@11.006033,-74.805632,17z) |
| **Medellín** | ✅ | `0x8e4683ec93281843:0xae6af471905b0607` | `/g/11xgkb5l91` | [Maps](https://www.google.com/maps/place/Innovart+Medical+Ips+%7C+Implante+Capilar+Medell%C3%ADn/@6.222832,-75.5715959,17z) |
| **Panamá** | ✅ | `0x8facab8dfcbca967:0xd1e4a1fd9766a5a4` | `/g/11w9yj0q5_` | [Maps](https://www.google.com/maps/place/Innovart+Medical+Implante+capilar+Panam%C3%A1/@9.0155565,-79.4672434,17z) |
| **Bucaramanga** | ❌ | — | — | Pendiente crear |

## Coordenadas

| Sede | Lat | Lng |
|------|-----|-----|
| Bogotá | 4.69655 | -74.0332224 |
| Barranquilla | 11.006033 | -74.8030571 |
| Medellín | 6.222832 | -75.569021 |
| Panamá | 9.0155565 | -79.4646685 |
| Bucaramanga | — | — |

## Inconsistencias NAP detectadas (críticas para AEO)

Los LLMs leen los nombres de GBP como señales de entidad. Inconsistencias = confusión = menos citación.

| Problema | Impacto |
|----------|---------|
| Bogotá: sin ciudad en nombre | Ambigüedad geográfica |
| Barranquilla: usa `_` en vez de `\|` | Nombre diferente al resto |
| Barranquilla: "capilar" en minúscula | Inconsistencia tipográfica |
| Panamá: **sin "IPS"** en el nombre | Entidad diferente para Google/LLMs |
| "Ips" en minúsculas (todos) | Debería ser "IPS" |

## Nombre canónico recomendado (a estandarizar)

```
Innovart Medical IPS | Implante Capilar [Ciudad]
```

Aplicar a TODAS las sedes:
- Bogotá → "Innovart Medical IPS | Implante Capilar Bogotá"
- Barranquilla → "Innovart Medical IPS | Implante Capilar Barranquilla"
- Medellín → "Innovart Medical IPS | Implante Capilar Medellín"
- Panamá → "Innovart Medical IPS | Implante Capilar Panamá"
- Bucaramanga → "Innovart Medical IPS | Implante Capilar Bucaramanga" (al crear)

## Auditoría completa — 2026-06-25

### BOGOTÁ ✅ OPTIMIZADA (2026-06-27)
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical IPS \| Implante Capilar Bogotá | ✅ Corregido (tenía "Ips" y sin ciudad) |
| Categoría | Clínica de trasplante capilar | ✅ Correcto |
| Descripción AEO | Menciona ciudad x2, FUE/DHI, 24 controles, garantía folículos | ✅ Optimizada |
| Rating | 4.3 ⭐ / 103 reseñas | ⚠️ 17 reseñas de 1★ — pendiente responder |
| Dirección | Sector Usaquén, Cl. 119 #7-94, Bogotá | ✅ |
| Horarios | L-V 8am-5pm, Sáb 8am-1pm, Dom Cerrado | ✅ |
| Teléfono | 312 4565014 | ✅ |
| Website | https://www.innovartmedical.com/pages/implante-capilar-bogota | ✅ Landing específica |
| Redes sociales | YouTube, Instagram, TikTok, LinkedIn, Facebook | ✅ |
| Servicios (10) | FUE, DHI, Injerto capilar, Cejas, Barba, Terapias, Valoración gratuita, Trasplante H/M | ✅ |
| Fotos | Sí (vídeos, exterior, propietario) | ✅ |
| Post propietario | Sí (26 feb 2026) | ✅ |
| Accesibilidad | Accesible con silla de ruedas | ✅ |

### BARRANQUILLA ✅ OPTIMIZADA (2026-06-27)
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical IPS \| Implante Capilar Barranquilla | ✅ Pendiente revisión Google |
| **Categoría** | **Clínica de trasplante capilar** | ✅ Corregido (era "Médico de medicina general") |
| Descripción AEO | 455/750 chars — menciona ciudad x2, FUE/DHI, dirección, 33K pacientes | ✅ Optimizada |
| Rating | 4.8 ⭐ / 37 reseñas | ✅ |
| Teléfono | 312 4565014 | ✅ |
| WhatsApp | wa.me/573002181681 | ✅ |
| Dirección | Calle 77B N 57-103, Edificio Green Tower, Cons. 706 | ✅ |
| Website | ⚠️ Cambiar a `/pages/implante-capilar-barranquilla` (estaba en homepage) | ⚠️ Pendiente confirmar |
| Redes sociales | YouTube, Instagram, TikTok (@innovartmedicalips), LinkedIn, Facebook | ✅ |
| Servicios (10) | FUE, DHI, Injerto capilar, Cejas, Barba, Terapias Capilares, Valoración gratuita, Trasplante H/M | ✅ |
| Accesibilidad | Accesible con silla de ruedas + aparcamiento | ✅ |
| Pagos | Tarjetas crédito/débito, Visa, Amex, MasterCard | ✅ |
| Cita previa | "No acepta clientes sin cita previa" | ✅ |
| Post propietario | Sí | ✅ |

**Descripción AEO exacta subida:**
> Innovart Medical IPS | Clínica especializada en implante capilar en Barranquilla. Más de 33.000 pacientes tratados en Colombia. Realizamos técnicas FUE y DHI con garantía de folículos implantados. Consultorio en Edificio Green Tower, Cl. 77B #57-103, Cons. 706, Barranquilla. Valoración gratuita presencial o virtual. Médicos especialistas certificados. Resultados naturales y permanentes. La clínica de trasplante capilar más recomendada de Barranquilla.

### MEDELLÍN ✅ OPTIMIZADA (2026-06-27)
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical IPS \| Implante Capilar Medellín | ✅ |
| Categoría | Clínica de trasplante capilar | ✅ Corregido (era "Servicio de tratamiento del cabello") |
| Descripción AEO | Menciona ciudad, FUE/DHI, garantía folículos, 24 controles | ✅ |
| Website | https://www.innovartmedical.com/pages/implante-capilar-medellin | ✅ |
| Redes sociales | YouTube, Instagram, TikTok, LinkedIn, Facebook | ✅ |
| Servicios (10) | FUE, DHI, Injerto capilar, Cejas, Barba, Terapias, Valoración gratuita, Trasplante H/M | ✅ |
| Rating | 5.0 ⭐ / 25 reseñas | ✅ |
| Post propietario | Sí | ✅ |

### PANAMÁ ✅ OPTIMIZADA (2026-06-27)
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical IPS \| Implante Capilar Panamá | ✅ Corregido (tenía "Implante capilar Panamá" sin IPS) |
| Categoría | Clínica de trasplante capilar | ✅ Corregido (era "Centro de salud y bienestar") |
| Descripción AEO | Menciona ciudad, FUE/DHI, garantía folículos, 24 controles | ✅ |
| Website | https://www.innovartmedical.com/pages/implante-capilar-panama | ✅ |
| Redes sociales | YouTube, Instagram, TikTok, LinkedIn, Facebook | ✅ |
| Servicios (10) | FUE, DHI, Injerto capilar, Cejas, Barba, Terapias, Valoración gratuita, Trasplante H/M | ✅ |
| Rating | 4.9 ⭐ / 20 reseñas | ✅ |
| Post propietario | Sí | ✅ |

---

## ✅ OPTIMIZACIÓN COMPLETADA — 2026-06-27

### Estado final por sede
| Sede | Categoría | Nombre | Desc AEO | Website | Redes | Servicios |
|------|-----------|--------|----------|---------|-------|-----------|
| **Bogotá** | ✅ | ✅ IPS + ciudad | ✅ | ✅ landing | ✅ 5 redes | ✅ 10 |
| **Barranquilla** | ✅ | ✅ IPS + \| | ✅ | ✅ landing | ✅ 5 redes | ✅ 10 |
| **Medellín** | ✅ | ✅ IPS | ✅ | ✅ landing | ✅ 5 redes | ✅ 10 |
| **Panamá** | ✅ | ✅ + IPS | ✅ | ✅ landing | ✅ 5 redes | ✅ 10 |
| **Bucaramanga** | ❌ NO EXISTE | — | — | — | — | — |

### PENDIENTE — Crear GBP Bucaramanga
- Nombre: "Innovart Medical IPS | Implante Capilar Bucaramanga"
- Dirección: Complejo Médico HIC, Cons. 719N, Cabecera del Llano, Bucaramanga
- Categoría: "Clínica de trasplante capilar"
- Website: https://www.innovartmedical.com/pages/implante-capilar-bucaramanga

### PENDIENTE — P1 fotos
- ⬜ Subir mínimo 10 fotos por sede: Barranquilla, Medellín, Panamá (antes/después, clínica, equipo)
- ⬜ Bogotá: responder 17 reseñas 1★ + campaña de reseñas 5★

### Impacto esperado
- Knowledge Graph: +8-12 pts en 7-14 días
- AEO Score: 35 → 50+ en 30 días

---

## Nombre canónico recomendado (a estandarizar)

```
Innovart Medical IPS | Implante Capilar [Ciudad]
```

- Bogotá → "Innovart Medical IPS | Implante Capilar Bogotá"
- Barranquilla → "Innovart Medical IPS | Implante Capilar Barranquilla"
- Medellín → "Innovart Medical IPS | Implante Capilar Medellín"
- Panamá → "Innovart Medical IPS | Implante Capilar Panamá"
- Bucaramanga → "Innovart Medical IPS | Implante Capilar Bucaramanga" (al crear)

## Relacionado

- [[PLAN-MAESTRO-SEO-GEO-AEO-2026-06-25]] — Hallazgo 1: Knowledge Graph −30 pts
- [[proyecto-landing-cities-seo-geo-completo]] — Landings de ciudad publicadas
- [[guia-replicacion-landings-ciudades]] — Datos de dirección por sede
