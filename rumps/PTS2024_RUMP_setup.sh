#!/bin/bash

# Drop rumps pdfs then run this script to get quick pdf-console-resenter shortcuts

for f in *pdf; do
  if ! [ -e "${f%.pdf}.sh" ]; then
    ln -s PTS2024_RUMP.sh "${f%.pdf}.sh"
  fi
done
