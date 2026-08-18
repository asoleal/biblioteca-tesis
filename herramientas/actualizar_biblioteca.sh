#!/usr/bin/env bash
# actualizar_biblioteca.sh — Zotero → bib → vault → JSON → GitHub
# Uso:  bash ~/actualizar_biblioteca.sh ["mensaje"] [--repos]
set -e
BIB=~/Zotero/Tesis_profesor_leal.bib
echo "1/4 .bib: entradas manuales"
python3 ~/completar_bib.py
echo "2/4 vault .md"
python3 ~/generar_vault.py ~/biblioteca-tesis
echo "3/4 índice JSON"
python3 ~/generar_index_json.py ~/biblioteca-tesis
echo "4/4 git"
cd ~/biblioteca-tesis
git add -A
if git diff --cached --quiet; then echo "Sin cambios que subir"; else
  git commit -m "${1:-Actualiza biblioteca}" && git push
fi
if [[ "$*" == *--repos* ]]; then
  for R in ~/proyecto-tesis /mnt/Compartida/Descargas_HDD/tesis-doctorado/tesis-BSF; do
    [ -d "$R" ] && find "$R" -name '*.bib' -not -path '*/.git/*' -exec cp "$BIB" {} \; && echo "bib → $R"
  done
fi
echo "Listo — la webapp se actualiza sola en ~5 min"
