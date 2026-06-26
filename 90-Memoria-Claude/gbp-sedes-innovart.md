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

### BOGOTÁ ✅ La mejor configurada
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical Ips \| Implante Capilar | ⚠️ "Ips" minúscula, sin ciudad |
| Categoría | Clínica de trasplante capilar | ✅ Correcto |
| Rating | 4.3 ⭐ / 103 reseñas | ⚠️ 17 reseñas de 1★ |
| Dirección | Sector Usaquén, Cl. 119 #7-94, Bogotá | ✅ |
| Horarios | L-V 8am-5pm, Sáb 8am-1pm, Dom Cerrado | ✅ |
| Teléfono | 312 4565014 | ✅ |
| Website | innovartmedical.com | ✅ |
| Fotos | Sí (vídeos, exterior, propietario) | ✅ |
| Post propietario | Sí (26 feb 2026) | ✅ |
| Accesibilidad | Accesible con silla de ruedas | ✅ |
| Landing URL | No verificada | ⬜ |

### BARRANQUILLA ❌ Categoría incorrecta
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical Ips _ Implante capilar Barranquilla | ❌ Usa "_", "capilar" minúscula |
| **Categoría** | **Médico de medicina general** | ❌ CRÍTICO — cambiar |
| Rating | 4.8 ⭐ / 37 reseñas | ✅ |
| Accesibilidad | Accesible con silla de ruedas | ✅ |
| Post propietario | Sí | ✅ |
| Dirección/Tel/Web | No verificados (necesita revisión) | ⬜ |

### MEDELLÍN ❌ Categoría incorrecta
| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Innovart Medical Ips \| Implante Capilar Medellín | ⚠️ "Ips" minúscula |
| **Categoría** | **Servicio de tratamiento del cabello** | ❌ CRÍTICO — cambiar |
| Rating | 5.0 ⭐ / 25 reseñas | ✅ |
| Accesibilidad | No visible | ⬜ |
| Post propietario | Sí | ✅ |
| Dirección/Tel/Web | No verificados (necesita revisión) | ⬜ |

### PANAMÁ ❌ Categoría incorrecta + información faltante
| Campo | Valor | Estado |
|-------|-------|--------|
| **Nombre** | **Innovart Medical Implante capilar Panamá** | ❌ Sin "IPS" |
| **Categoría** | **Centro de salud y bienestar** | ❌ CRÍTICO — cambiar |
| Rating | 4.9 ⭐ / 20 reseñas | ✅ |
| **Info faltante** | **Google dice "Añadir la información que falta"** | ❌ URGENTE |
| Post propietario | Sí | ✅ |
| Dirección/Tel/Web | No verificados (necesita revisión) | ⬜ |

---

## 🔴 Prioridades de corrección (impacto AEO)

### P0 — Esta semana (máximo impacto Knowledge Graph)
1. ❌ **Categoría Barranquilla** → cambiar a "Clínica de trasplante capilar"
2. ❌ **Categoría Medellín** → cambiar a "Clínica de trasplante capilar"
3. ❌ **Categoría Panamá** → cambiar a "Clínica de trasplante capilar"
4. ❌ **Información faltante Panamá** → completar todo lo que Google pida
5. ❌ **Nombre Panamá** → agregar "IPS": "Innovart Medical IPS | Implante Capilar Panamá"

### P1 — Esta semana
6. ⬜ Nombre Barranquilla → cambiar "_" por "|" y "capilar" → "Capilar"
7. ⬜ Agregar URL de landing en cada GBP (apuntar a landing de ciudad)
8. ⬜ Verificar dirección/teléfono/web de Barranquilla, Medellín y Panamá
9. ⬜ Crear GBP Bucaramanga → "Innovart Medical IPS | Implante Capilar Bucaramanga"

### P2 — Semana 2
10. ⬜ Estrategia para reducir 17 reseñas 1★ de Bogotá (responder, pedir más 5★)
11. ⬜ Subir fotos en Barranquilla, Medellín y Panamá (mínimo 10 por sede)
12. ⬜ Atributos de salud en Medellín y Panamá

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
