---
name: medicion-leads-blog-whatsapp
description: Sistema GHL para medir leads que llegan por WhatsApp desde el blog de Innovart (tags + workflow)
metadata:
  type: project
---

Sistema de **medición de leads del blog por WhatsApp** montado el 2026-06-18 en la cuenta GHL **principal** `Innovart Medical IPS` (`NPhQTmLOHd6FbDtqLPnG`). Solo ahí (no en TVD ni en las otras sedes).

**Convención del blog:** todo mensaje de WhatsApp desde el blog incluye el texto fijo `vengo del blog de Innovart` + un código por artículo `(Ref: CODIGO)`.

**Workflow:** `Leads del Blog (WhatsApp)` — ID `ddc39bd2-37fd-4db1-85e9-3dde52da613c`, **publicado/activo**.
- Disparador: Customer Replied con `message.type == 2` (canal SMS = WhatsApp applevel, ver [[feedback-whatsapp-applevel-sms]]) **y** `message.body` contains `vengo del blog de Innovart`.
- 1ª acción: agrega tag `lead del blog`.
- 13 ramas If/Else anidadas (cada NO encadena al siguiente check) por `message.body` contains `(Ref: ...)`; la rama SÍ agrega su tag y termina. Orden: FUE-DHI → FUE → DHI → Candidato → Recuperacion → Resultados → Barba → Alopecia-Mujeres → FAQ → Clinica → Dr-Carreno → Dra-Morales → Info-IA. Se matchea el token completo con paréntesis de cierre `(Ref: FUE)` para evitar solapes.

**14 tags creados** (GHL los guarda en minúsculas): `lead del blog` + `lead del blog <codigo>` por artículo.

**Continuidad (decisión de Javier, modo AUTO):** el workflow del blog SOLO etiqueta. La maquinaria de oportunidad + asignación de comercial + IA es `0.1 SMS GPT` (`428a4568-c93e-4667-bd19-531e563d9601`), que dispara con el MISMO inbound (customer_reply type 2, sin filtro de texto) → los leads del blog ya entran ahí automáticamente. **No** se hizo Add to workflow (con `allowMultiple:true` en 0.1 duplicaría la IA) ni se tocó 0.1.

**Técnico reutilizable:** if/else por cuerpo de mensaje en GHL = `conditionType:"contact_reply"`, `conditionSubType:"message.body"`, `conditionOperator:"contains"`, `conditionValue:"..."`. El disparador `customer_reply` admite condiciones sobre `message.type`, `message.body` (contains) y `contact.tags`. Relacionado con [[academia-capilar-ecosistema]] y [[blog-salud-capilar-drive]].

**Prueba E2E ✅ (2026-06-18):** WhatsApp real `vengo del blog de Innovart (Ref: FUE-DHI)` desde +573002181681 → contacto nuevo quedó con `lead del blog` + `lead del blog fue-dhi` (sin solape con `fue`), y 0.1 SMS GPT lo metió a `oportunidad ventas frio`, lo asignó a comercial y puso `ai_activado`. Disparador type 2 confirmado en producción. Mensaje de prueba inyectado por API NO se pudo (provider applevel `628f88...` da 401 a mi token); la validación válida es por WhatsApp real.

**Botones del blog: YA HECHOS ✅ (verificado 2026-06-19).** Los 13 artículos del blog Shopify "Artículos Médicos" (`www.innovartmedical.com/blogs/articulos-medicos`) YA tienen el CTA verde "Escríbenos por WhatsApp" apuntando a **`wa.me/573124565014`** (número 312 principal) con su `(Ref: <CODIGO>)` correcto 1:1 por tema y la frase "vengo del blog de Innovart". Los blogs se generaron con el CTA incluido — NO agregar más (duplicaría). Sistema completo de punta a punta: botón blog → workflow `Leads del Blog (WhatsApp)` → tags + `0.1 SMS GPT`. (El E2E confirmó que el WhatsApp entrante cae en la cuenta principal.) Si alguna vez entrara como type 19 (nativo), añadir trigger gemelo.

Editar artículos del blog: Shopify Admin GraphQL `articleUpdate(id, article:{body})`; campo de contenido = `body` (HTML). 13 artículos con IDs `gid://shopify/Article/6834...`.
