---
name: skill-ver-videos
description: Habilidad propia que permite a Claude "ver" videos (locales, Drive por ID, o URL) — fotogramas + transcripción. Clave para absorber material de VIDEO al cerebro de marca. Creada 2026-06-20.
metadata:
  type: reference
---

# 👁️ Skill `ver-videos` — Claude "ve" videos

Habilidad en `~/.claude/skills/ver-videos/` (SKILL.md + `analizar_video.sh`). Quita la limitación de no procesar video: extrae **fotogramas (ffmpeg)** + **transcribe audio (whisper)** y luego Claude los analiza.

## Uso rápido
```bash
~/.claude/skills/ver-videos/analizar_video.sh "<entrada>" [num_frames=10] [modelo=base|tiny|small|none]
```
- `<entrada>`: ruta local · **ID de Google Drive** · URL (yt-dlp).
- Drive: descarga por ID con `rclone backend copyid gdrive:` (remote ya autenticado).
- `none` en modelo = solo fotogramas (rápido). `tiny` = transcripción veloz. Default `base`.
- Output en `/tmp/ver-videos/<slug>/`: `frame_*.jpg` + `transcript.txt`. Luego: Read de los frames + del transcript → sintetizar qué muestra/dice.

## Verificado
2026-06-20: probado con `4.mp4` de Innovart (reel nostalgia fútbol Colombia vs Inglaterra 1995, Higuita). Descarga + 8 fotogramas + manejo de reel sin voz: OK.

## Para absorber al cerebro
Tras entender el video, destilar en [[adn-comunicacion-innovart]] y registrar cobertura en [[material-grafico-drive-mapa]]. Nunca mezclar marcas: Churra→cerebro Churra, Ritual→cerebro Ritual. Requisitos (instalados): ffmpeg, rclone(`gdrive:`), whisper, yt-dlp.
