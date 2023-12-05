#!/bin/bash

file="$1"
gs -dSAFER -dBATCH \
    -dNOPAUSE -dNOCACHE -sDEVICE=pdfwrite \
    -sColorConversionStrategy=CMYK \
    -dProcessColorModel=/DeviceCMYK \
    -sOutputFile="${file%.pdf}_cmyk.pdf" \
    "$file"
