---
tipo: prompt-template
tema: crm
trigger: leads aging, priorizar leads, leads fríos, recuperar leads, leads perdidos
---

# Priorizar Leads con Aging

## Cuándo usar
Al inicio de la semana para que el equipo comercial sepa en quién enfocarse primero.

## Variables que tenés que reemplazar
- `<CIUDAD>`: ej. "Bogotá", "todas las sedes"
- `<ASESOR>`: ej. "Karla", "todo el equipo"
- `<DIAS_MINIMO>`: días mínimos sin contacto para considerar aging (ej. "7")

## Prompt
Generá un listado priorizado de leads con aging para <ASESOR> en <CIUDAD>.

Criterio de aging: sin actividad hace más de <DIAS_MINIMO> días.

Usando GHL CRM, extraé leads con las siguientes condiciones:
- Etapa: Primer contacto, Tibio, o Agenda Valoración (NO Perdido, NO Ganado)
- Sin nota o mensaje registrado en los últimos <DIAS_MINIMO> días
- Ordenados por: (1) etapa más avanzada primero, (2) más días sin contacto

Para cada lead mostrá:
| Lead | Ciudad | Etapa | Días sin contacto | Última acción | Asesor | Señal de compra |

Después del listado, generá:
1. Top 5 leads "calientes rescatables" — los que tienen más señales de cierre aunque tengan aging
2. Top 5 leads para depurar — los que probablemente nunca van a avanzar (identificar patrón)
3. Acción recomendada para cada uno (mensaje, llamada, o archivar)

## Output esperado
Tabla de leads + top 5 calientes + top 5 a depurar + acción recomendada por lead.

## Ejemplo de uso real
"Listame los leads de Bogotá sin contacto hace más de 7 días de Karla y decime en quién enfocarse"
