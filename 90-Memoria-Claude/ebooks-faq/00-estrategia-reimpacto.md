# Estrategia de Reimpacto — Reactivación de Leads Fríos y Tibios con los 8 Ebooks

**Innovart Medical IPS · Lifecycle/CRM · v1 · 2026-06-19**

Premisa: el ebook es **excusa de valor**, no oferta de venta. Reactivamos las ~160K+ oportunidades dormidas del CRM con educación → generamos micro-compromiso (clic/respuesta) → elevamos score → handoff humano (Sofia) → valoración. El "won status roto" del CRM (solo 2 won de 25K en Bogotá) significa que **NO confiamos en el stage del pipeline para medir cierre**; medimos reactivación por señales propias (respuesta, clic, agenda).

---

## 1) Segmentación de la base: FRÍO vs TIBIO

### Definición operativa

| Eje | FRÍO | TIBIO |
|---|---|---|
| **Etapa pipeline** | Frío, Primer contacto (sin avanzar), Perdido temprano | Tibio, Agenda Valoración (no completó), Val Virtual no-show, "Cancelado-Reagendamiento pendiente" |
| **Última interacción** | > 60 días sin respuesta, o nunca respondió | 15-90 días, respondió al menos 1 vez |
| **Lead score** | Bajo (`{{score < 30}}`) | Medio (`{{30 <= score < 70}}`) |
| **Señal de intención** | Solo dio datos / clic en ad, nunca preguntó nada concreto | Preguntó precio, técnica, candidatura, o agendó y no fue |
| **Permiso de canal** | Incierto → **requiere re-permiso** | Conversación previa existente → permiso vivo |

### Sub-segmentos accionables (los que mueven la aguja)

**TIBIO (alta prioridad — atacan show rate <40% y "casi-clientes"):**
- **T1 No-show / Val Virtual no asistió** — agendó, no llegó. Recuperable inmediato.
- **T2 Casi-cliente / "Consultar con esposa(o)"** — decisión en pareja, freno emocional/social.
- **T3 Consultó precio / MeddiPay** — freno económico, necesita financiación.
- **T4 Cancelado-Reagendamiento pendiente** — canceló explícito pero abierto.
- **T5 "A la espera de vacaciones"** — freno de timing/recuperación laboral.

**FRÍO:**
- **F1 Curioso TOFU** — descargó/clic en ebook o ad, nunca avanzó.
- **F2 Lead viejo dormido** — dio datos hace > 60-90 días, silencio total.
- **F3 Dudas de candidatura** — mujer, alopecia avanzada, edad, caso especial (auto-excluido por miedo).

### Reglas de filtrado en GHL (tags + smart lists)

Crear **smart lists por sede** (6 subcuentas). Tags de control sugeridos (crear en cada location):

```
Estado de reimpacto:
  reimp_frio  reimp_tibio
  reimp_T1_noshow  reimp_T2_pareja  reimp_T3_precio  reimp_T4_cancelado  reimp_T5_vacaciones
  reimp_F1_curioso  reimp_F2_dormido  reimp_F3_candidatura
Control de cadencia / permiso:
  reimp_repermiso_pedido  reimp_repermiso_si  reimp_optout
  reimp_ola_1 ... reimp_ola_N  reimp_pausa  reimp_reactivado  reimp_agendado
```

Filtros (mapear a IDs reales de stage/customField):
- **FRÍO:** `stage IN [Frío, Primer contacto]` **OR** `Perdido` con `dias_sin_actividad > 60` **AND** `tag NOT reimp_optout` **AND** `score < 30`.
- **TIBIO:** `stage IN [Tibio, Agenda Valoración, Val Virtual]` **OR** `lost_reason IN [Reagendamiento pendiente, Consultar con esposa, MeddiPay, Vacaciones]` **AND** `tag NOT reimp_optout`.
- **T1 No-show:** appointment con `status = no-show/cancelled` **AND** sin appointment futura.
- **T3 Precio/MeddiPay:** `lost_reason = MeddiPay` OR `tag precio_consultado`.

> ⚠️ Como el "won" está roto, **excluir clientes ya operados** cruzando contra el pipeline **"Operaciones"** antes de cualquier envío. No reimpactar a quien ya se operó.

---

## 2) Mapa ebook → segmento

**Fríos = educación/curiosidad/desmontar miedo** (E01, E04, E06, E08). **Tibios = decisión/objeciones** (E02, E03, E05, E07). Se entrega **1 ebook por toque** (no saturar).

| Segmento | Ebook ancla | Por qué | Secuencia |
|---|---|---|---|
| **F1 Curioso TOFU** | E01 (duele) | Miedo #1 universal, baja barrera | E01 → E06 → E04 → (si responde) E05 |
| **F2 Dormido** | E01 (duele) | Re-enganche con el ángulo más magnético | E01 → E06 → E02 |
| **F3 Candidatura** | E06 (soy candidato) | Responde directo su auto-exclusión | E06 → E03 → E05 |
| **T1 No-show** | E05 (resultados) | Reconecta con el "para qué": el resultado real | E05 → E07 → CTA reagendar |
| **T2 Pareja** | E04 (día a día) | Material para decidir EN pareja, baja ansiedad del acompañante | E04 → E08 → E05 |
| **T3 Precio** | E07 (costo/financiación) | Ataca el freno directo: financiación hasta 90% | E07 → E03 → CTA valoración |
| **T4 Cancelado** | E02 (FUE vs DHI) | Reabre con valor técnico neutro, sin presión | E02 → E05 → CTA reagendar |
| **T5 Vacaciones** | E04 (día a día) | Ayuda a planear el calendario de recuperación | E04 → E08 → CTA fecha futura |

Reglas: frío **siempre** abre con re-permiso. Tibio recibe ebook directo (permiso vivo). E08 **nunca** a fríos puros (asume decisión tomada; reservarlo a tibios avanzados o post-valoración).

---

## 3) Cadencia de reimpacto

**Canal (applevel):** Enviar por acción WhatsApp (`send_whatsapp_message`, `from` = WABA sede). Escuchar respuestas con `message.type == 2` (SMS), **nunca 19**. Email de respaldo. Horarios COL/PAN: **martes a sábado, 10:00-12:00 y 15:00-18:00**; evitar lunes AM y domingos.

**Re-permiso limpio (solo FRÍOS):** el toque 1 no entrega ebook, pide opt-in ("responde SÍ"). `SÍ` → tag `reimp_repermiso_si` → secuencia. `NO/stop` → `reimp_optout`. Sin respuesta 48h → 1 recordatorio email, luego pausa.

**FRÍOS (re-permiso primero):** D0 re-permiso (WA) · D2 email recordatorio · D5 ebook ancla (WA, solo si dijo SÍ) · D9 2º ebook · D14 3er ebook + CTA suave · D21 sin señal → pausa 90d. Máx **3 toques de contenido** tras el SÍ.

**TIBIOS (permiso vivo, más ágil):** D0 ebook ancla · D3 2º ebook + pregunta abierta · D7 3er ebook + CTA fuerte · D12 CTA directo valoración (Sofia) · D18 sin respuesta → nurture mensual, score −10.

**Salud WABA:** olas de **500-1000 contactos/día/sede**, nunca blast. Orden de calidad: **tibios primero**, luego fríos con re-permiso, luego dormidos. Plantillas aprobadas como WhatsApp templates (skill `whatsapp-templates-ghl`). Respetar ventana 24h. Alerta dura si optout+bloqueos > 2-3%.

---

## 4) Mecánica GHL por API

**Workflow-first:** `WF-REIMP-FRIO-[sede]` y `WF-REIMP-TIBIO-[sede]` por subcuenta. Enrolamiento por smart list + tag (`add_contact_to_workflow` / `bulk_add_to_workflow` en olas controladas). Acciones de envío dentro del WF (WhatsApp + Email + waits). `send_message` directo solo para pruebas 1-a-1.

**Trigger links (medibles):** cada ebook se entrega como trigger link (`{{ebook_link_e01}}`…`{{ebook_link_e08}}`, crear con `create_trigger_link` por sede). Clic → tag `ebook_eNN_click` + score + avanza secuencia. Separa "abrió WhatsApp" de "abrió ebook" de "leyó y volvió".

**Scoring + handoff:** trigger `customer_reply` (Reply channel = SMS, `message.type==2`, filtro contains). Respuesta +15, clic ebook +10, clic agenda +25. Al cruzar `score >= 70` o intención clara → **handoff a Sofia**: tag `ai_parar`, asignar/notificar, mover stage. Tag `reimp_reactivado` + salir del workflow (evita doble contacto).

**CAPI:** agenda → evento **Schedule** (webhook, con fbclid/ctwa_clid). Cirugía (pipeline Operaciones) → **Purchase** (validado 2026-06-14). Las reactivaciones también nutren audiencias/lookalike del plan TOFU-Ebook.

**Pre-requisito bloqueante:** UTMs/trigger links desde el día 1 (hoy 0% UTMs en 176 ads). Sin medición de clic, el reimpacto vuela a ciegas.

---

## 5) KPIs y regla de parar/insistir

| Métrica | Definición | Meta inicial (calibrar) |
|---|---|---|
| Tasa de re-permiso (fríos) | `SÍ` / enviados toque 1 | ≥ 8-12% |
| Tasa de respuesta | responden (type==2) / enviados | Tibios ≥ 15-20%; Fríos ≥ 5-8% |
| Clic a ebook (CTR trigger link) | clics / entregados | ≥ 10-15% |
| Lectura → CTA | clic agenda / clic ebook | ≥ 20% |
| % a valoración | citas / contactos reimpactados | ≥ 3-5% |
| **Reactivaciones** | tag `reimp_reactivado` / total | **KPI norte** |
| Show rate de reactivados | asistió / agendados (cruce Operaciones) | subir vs base <40% |
| Salud WABA | optout+bloqueos / enviados | < 2-3% (alerta) |

Reportar por **cohorte de ola**, juzgar a +30/+45 días (ciclo largo; no medir cierre por stage, won roto).

**Parar (contacto):** optout / NO / 3 toques sin señal → pausa 90d. **Parar (ola):** salud WABA > 3% → detener esa sede, revisar copy/horario/lista. **Insistir:** respuesta+clic sobre meta y optout <2% → subir +20%/día (tibios > fríos re-permiso > dormidos). **Handoff:** ante intención de compra → `ai_parar` + Sofia.

---

## Placeholders a resolver con IDs reales
- `location_id` x6 · `workflow_id` WF-REIMP-FRIO/TIBIO por sede.
- `pipeline_id_ventas` + stage IDs · `pipeline_id_operaciones` (exclusión de operados).
- `from_phone_number` WABA por sede · `conversationProviderId` = `628f88b07cf43a7641c58089`.
- `{{ebook_link_e01..e08}}` trigger links por sede (pendiente hospedar los ebooks).
- Custom fields: `lead_score`, `dias_sin_actividad`, `lost_reason`, `precio_consultado`.
- Umbrales de score (30/70) y deltas (+15/+10/+25) — calibrar con datos reales.
- Templates WhatsApp aprobados (re-permiso + 8 ebooks) vía skill `whatsapp-templates-ghl`.

**Quick win inmediato:** arrancar con **T1 no-show + T2 casi-cliente** usando E05 y E07 sobre las ~160K opps dormidas — mayor retorno y ataca el show rate directamente.
