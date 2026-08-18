# Biblioteca Tesis BSF-GEI

Infraestructura bibliográfica y de consulta para la tesis doctoral:

> **Sistema Inteligente para el Modelado y Predicción de Emisiones de GEI en la Bioconversión de Residuos con *Hermetia illucens***
> (medición de CO₂/CH₄, gemelo digital, batch controlado, dashboard de visualización)

**Autor**: J. J. Leal (GitHub: `asoleal`) · **Máquina de trabajo**: Arch Linux (EndeavourOS), usuario `jjlealg`
**Estado**: operativo al 2026-08-18 · **163 referencias** · 152 con PDF · 92 citadas en la tesis

---

## 1. Qué es esto

Este repo es la **fuente única de verdad** de la bibliografía de la tesis. Todo referencia que entra por Zotero termina aquí automáticamente convertida en:

- **163 notas Markdown** (`vault/<tema>/<citekey>.md`) con frontmatter YAML — una por referencia.
- **`vault/vault_index.json`** — índice de metadatos de todas las notas (lo consume la webapp).
- **`vault/vault_textos.json`** — texto completo extraído de 146 PDF (búsqueda profunda; ~9.5 MB).

Sobre el repo viven dos consumidores:

1. **Webapp** (plataforma Kimi): biblioteca navegable, buscador transversal, consulta por artículo, estadísticas y grafo — lee este repo **en vivo** vía backend con token.
2. **CLI local**: `buscar.py` / comando `tesis`, para búsquedas desde terminal o desde Kimi CLI.

⚠️ **El repo es PRIVADO a propósito**: `vault_textos.json` contiene texto extraído de artículos con copyright. No hacer público.

---

## 2. Arquitectura

```
Zotero 7 (grupo "Tesis_profesor_leal")
   │  Better BibTeX exporta con "Mantener actualizado" ✓
   ▼
~/Zotero/Tesis_profesor_leal.bib        ← .bib MAESTRO (153 BBT + 10 manuales = 163)
   │  cambio en el archivo dispara el watcher systemd
   ▼
~/actualizar_biblioteca.sh              ← cadena 1/4 → 4/4:
   ├─ ~/completar_bib.py                (añade 10 entradas manuales, idempotente)
   ├─ ~/generar_vault.py                (regenera las 163 notas .md desde Zotero + .bib)
   ├─ ~/generar_index_json.py           (vault_index.json)
   ├─ ~/generar_textos_json.py          (pdftotext → vault_textos.json, caché en ~/.cache/tesis-textos)
   └─ git add/commit/push               (solo si hay cambios)
   ▼
GitHub: asoleal/biblioteca-tesis  (PRIVADO, rama main)
   ▼
Webapp Kimi (backend lee con GITHUB_TOKEN, caché 5 min)
   ├─ Pestaña Biblioteca / Estadísticas / Grafo  → vault_index.json + notas .md
   └─ Pestaña Consulta IA                        → índice + textos completos
```

**Repos hermanos de redacción** (reciben el .bib maestro sincronizado):
- `~/proyecto-tesis`
- `/mnt/Compartida/Descargas_HDD/tesis-doctorado/tesis-BSF`

---

## 3. Componentes locales (máquina `jjlealg`)

### 3.1 `.bib` maestro — `~/Zotero/Tesis_profesor_leal.bib`
- 153 entradas exportadas por **Better BibTeX** (auto-export activado: *click derecho sobre la colección → Exportar → Mantener actualizado*). Si esa casilla se desmarca, la automatización muere silenciosamente.
- 10 entradas manuales (libros/normas/reportes sin ítem Zotero): `noaa2024ch4`, `jcgmEvaluationMeasurementData2008`, `ipccGuidelinesNationalGreenhouse2006`, `ideam2021inventario`, `atkinsPhysicalChemistry2014`, `roels1980`, `jucker2017` (VERIFICAR), `hutchinsonMethodsSoilAnalysis1992` (VERIFICAR), `allanSummaryPolicymakers2023`, `shulerbioprocess2017`.
- **Nunca editar a mano**: las manuales se gestionan con `completar_bib.py`.

### 3.2 Scripts (todos en `~`, copia de respaldo en `herramientas/` de este repo)

| Script | Qué hace exactamente |
|---|---|
| `completar_bib.py` | Añade las 10 entradas manuales al .bib si no están (`if '{'+k+',' not in txt`). Idempotente. |
| `export_biblio.py` | Copia la sqlite de Zotero a `/tmp/zq` (truco para evitar *database locked*), exporta catálogo del grupo → `~/biblioteca.csv` (itemID, key, title, abstractNote, DOI, authors, tags, collections, **pdf_path relativo a `~/Zotero/storage/`**). |
| `generar_vault.py` | Lee sqlite-copia + .bib + escanea citas `\cite{}` en ambos repos de tesis. **Borra y regenera** `vault/`: notas con frontmatter, clasificadas en 10 carpetas temáticas por palabras clave; empareja ítem↔citekey por DOI/título normalizados; tiene tabla ALIAS para excepciones. Regex de campos BBT con doble anidación de llaves. |
| `generar_index_json.py` | Frontmatter de cada .md → `vault/vault_index.json` (citekey, title, authors, year, type, doi, url, tema, tags, pdf, citado, verificar, abstract, citado_en, path). |
| `generar_textos_json.py` | Refresca `biblioteca.csv`, empareja pdf_path→citekey, `pdftotext` con caché en `~/.cache/tesis-textos/<citekey>.txt`, corta la sección References (rfind en el último 45%), tope 200k chars → `vault_textos.json`. |
| `buscar.py` | Buscador CLI de texto completo. Modos: transversal (grupos de sinónimos ES→EN, ranking todos-los-grupos primero, luego parciales) y `--nota <citekey|apellido> <términos>` (dentro de un artículo). `--n N` resultados. |
| `~/.local/bin/tesis` | Wrapper para terminal/Kimi CLI: `buscar`, `nota`, `ficha`, `citekey`, `temas`, `stats`, `actualizar`. |
| `actualizar_biblioteca.sh` | La cadena completa + git push. Flag `--repos` también copia el .bib a los repos de redacción. |

### 3.3 Automatización (systemd --user)
- `~/.config/systemd/user/actualizar-biblioteca.path` → `PathChanged=%h/Zotero/Tesis_profesor_leal.bib`
- `~/.config/systemd/user/actualizar-biblioteca.service` → `Type=oneshot`, `ExecStartPre=sleep 20` (debounce), `GIT_SSH_COMMAND=ssh -o BatchMode=yes`
- Estado: **habilitado**. Verificar: `systemctl --user status actualizar-biblioteca.path` y `journalctl --user -u actualizar-biblioteca.service -f`.

**Flujo automático**: agregas una referencia en Zotero → BBT reexporta el .bib → watcher espera 20 s → corre la cadena → push → webapp actualizada en ~5 min.

---

## 4. El vault

- 10 carpetas temáticas: `01-bsf-gei` (17), `02-bsf-modelado` (34), `03-bsf-general` (22), `04-gei-clima` (21), `05-iot-sensores` (20), `06-ml-ia` (14), `07-residuos-compostaje` (17), `08-acv` (3), `09-deb-bioenergetica` (6), `00-otros` (9).
- El **nombre del archivo ES el citekey** (Better BibTeX). Así se citan en LaTeX: `\cite{ermolaevGreenhouseGasEmissions2019}`.
- Frontmatter de cada nota: `citekey, title, authors, year, type, doi, url, tema, tags, pdf, citado, verificar, abstract, citado_en`.
- `citado: true` = aparece citada en algún .tex de los repos de redacción (92 de 163).
- `verificar: true` = entrada provisional que requiere revisión manual.

---

## 5. La webapp (plataforma Kimi)

**Stack**: React 19 + TS + Vite + Tailwind + shadcn/ui (frontend) · Hono + tRPC 11 + Drizzle (backend, feature `db`) · despliegue por versiones (actual: `2875d7a`, tipo *dynamic*).

### Pestañas
1. **Biblioteca** — tabla/filtros de las 163 notas, ficha con Markdown renderizado y visor de PDF.
2. **Consulta IA** — dos sub-pestañas:
   - *Por tema*: pregunta en lenguaje natural → grupos de sinónimos ES→EN (diccionario EXP) → ranking sobre título+resumen+tags (peso ×3) + texto completo (tope) → degradación progresiva de grupos (como `buscar.py`) → síntesis en párrafos con citas `[citekey]` + tarjetas clicables.
   - *Por artículo*: selector con autocompletado (apellido/año/título) + pregunta opcional → extrae los 3 pasajes más relevantes del texto completo (ventanas de 1400 chars centradas en el primer hit) o resumen general si la pregunta va vacía.
3. **Estadísticas** — distribución por tema/año/tipo.
4. **Grafo** — red de notas por tema.

### Backend (`api/`)
- `consulta.preguntar` `{pregunta, maxArticulos}` — transversal; detecta autor+año y enfoca si hay evidencia fuerte.
- `consulta.porArticulo` `{citekey, pregunta}` — modo artículo explícito (sin detección).
- `biblioteca.indice` / `biblioteca.nota {path}` — **proxy al repo privado** (el navegador no puede llamar a GitHub con token; todo pasa por el backend).
- Cachés en memoria de 5 min para índice y textos.
- **Síntesis IA (LLM)**: llama agent-gw OpenAI-compatible con `DEFAULT_AI_*`; si falla (en sandbox da 403 `api_key_path_forbidden`), degrada a **síntesis extractiva** con fragmentos/resúmenes — la insignia bajo cada respuesta indica el modo (`IA` vs `extractiva (sin IA)`).

### `.env` (solo servidor, nunca llega al navegador)
- `GITHUB_TOKEN` — fine-grained PAT, repo `biblioteca-tesis`, permiso **Contents: Read-only**. **Vence en 1 año**; síntoma de expiración: la webapp vuelve a decir "copia local". Renovar en https://github.com/settings/personal-access-tokens y actualizar el `.env`.
- `DEFAULT_AI_API_KEY / DEFAULT_AI_BASE_URL / DEFAULT_AI_MODEL` — credenciales IA del portal.
- `APP_ID/APP_SECRET/DATABASE_URL` — provistos por la plataforma (no tocar).

---

## 6. Cómo se usa (flujos)

**Agregar referencias**: entrar por Zotero al grupo `Tesis_profesor_leal` (con PDF si hay). No hay que hacer nada más: el watcher propaga. Forzar manual: `tesis actualizar`.

**Buscar desde terminal / Kimi CLI** (Kimi CLI lee `AGENTS.md` y usa estos comandos):
```bash
tesis buscar co2 ch4 sensores            # transversal, texto completo
tesis nota ermolaev 2019 metano camara   # dentro de un artículo
tesis citekey ermolaev                   # resolver citekey exacto
tesis ficha ermolaev2019                 # metadatos
tesis temas && tesis stats               # panorama
```

**Buscar desde la webapp**: pestaña Consulta IA → *Por tema* o *Por artículo*. Las tarjetas abren la ficha; la insignia indica fuente (GitHub en vivo / copia local) y modo de síntesis.

**Citar en la tesis**: usar los citekeys tal cual (son nombres de archivo del vault). Los repos de redacción reciben el .bib con `bash ~/actualizar_biblioteca.sh --repos`.

---

## 7. Reglas para agentes de IA que trabajen aquí

1. **El .bib no se edita a mano** (BBT lo reexporta y pisa todo). Entradas sin ítem Zotero → añadir en `completar_bib.py`.
2. **El vault no se edita a mano**: se regenera con `generar_vault.py` (borra todo). Cambios de contenido → en Zotero.
3. Los PDF **nunca** se suben al repo (copyright). Solo texto extraído, repo privado.
4. Si Zotero está abierto, la sqlite se copia primero (`cp ~/Zotero/zotero.sqlite* /tmp/zq/`).
5. Citekeys "feos" tipo `nacionesUnidas…` son *pinned keys* de BBT: no renombrar a mano (se hace con *Better BibTeX → pin key* si acaso).
6. Compilación de la tesis: **xelatex** (no pdflatex).
7. Comandos para el usuario: rutas absolutas sin placeholders, heredocs `cat << 'EOF'`, de a 1-2 comandos por turno.

---

## 8. Estado y pendientes conocidos

- [ ] **6 PDF sin texto** en `vault_textos.json` (146/152): no emparejaron título/DOI entre Zotero y .bib. Diagnóstico: comparar stems del vault `pdf: true` contra claves del JSON.
- [ ] Síntesis IA: desde el sandbox de desarrollo el endpoint da 403; en el runtime de plataforma debería activar. Si la insignia dice siempre "extractiva", revisar credenciales `DEFAULT_AI_*`.
- [ ] `chenEffectMoistureContent2019` — artículo **retractado**: eliminar su cita de `tesis/Capitulos/discusion_capitulo2.tex` (repo tesis-BSF).
- [ ] Placeholders `ref4, ref54, ref56, ref59, ref64` en borradores de tesis-BSF: resolver a citekeys reales.
- [ ] `macavei2020`, `minciencias2020guia`: citas posiblemente fantasma en tesis-BSF.
- [ ] Biblioteca personal de Zotero: 28 ítems, 100% duplicados verificados del grupo (16 por DOI + 12 por título) → vaciarla es seguro (opcional).
- [ ] `.bak` de la sincronización de citekeys en repos de redacción: limpiar.

---

## 9. Historial de decisiones (por qué es así)

1. **Zotero grupo + BBT auto-export** como única entrada de datos: elimina sincronización manual.
2. **Repo privado + token read-only**: permite tener texto completo sin violar copyright; el navegador nunca ve el token (proxy backend).
3. **Ranking por grupos de sinónimos ES→EN**: las consultas son en español, el corpus en inglés; cada palabra de la consulta es un grupo y los documentos deben tocar todos (con degradación a parciales).
4. **Degradación elegante de la IA**: si el LLM no responde, síntesis extractiva con citas — la herramienta nunca falla en vacío.
5. **Citekey = nombre de archivo**: un identificador para Zotero, LaTeX, vault, CLI y webapp.
6. **systemd watcher en vez de cron**: actualización disparada por el evento real (cambio del .bib), con debounce de 20 s para no correr a mitad de export.
