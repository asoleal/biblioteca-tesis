# AGENTS.md — Biblioteca de tesis (BSF × GEI)

Biblioteca Markdown de 163 notas (una por referencia de Zotero, grupo
"Tesis_profesor_leal"). Tesis: modelado y predicción de emisiones de
CO2/CH4 en bioconversión de residuos con Hermetia illucens.

## Herramienta principal: `tesis`
Usa SIEMPRE el comando `tesis` (está en PATH). No uses grep/ripgrep sobre
vault/: pierde el ranking por sinónimos ES→EN y la extracción de PDF.

- `tesis buscar <términos>` — transversal, texto completo de los PDF
- `tesis nota <citekey> <términos>` — dentro de un solo artículo
- `tesis citekey <frag>` / `tesis ficha <frag>` — resolver y ver metadatos
- `tesis temas` / `tesis stats` / `tesis actualizar`

## Reglas
- Cita como [citekey]; el citekey es el nombre del archivo .md.
- Frontmatter de cada nota: title, authors, year, doi, tema, tags, pdf, citado.
- Tras agregar referencias en Zotero: `tesis actualizar` (regenera y empuja a git).
- Responde en español, en párrafos con citas, estilo de tesis doctoral.
