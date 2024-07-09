#!/bin/bash


PREROLL=Intro_Video_PTS24
convert -density 300 "${PREROLL}.pdf" -resize 1920x1080 "${PREROLL}.jpg"

# had to fix manually the jpg here: 1919x1080 => 1920x1080

TRANSITION=smoothleft
rm "${PREROLL}.mp4"
ffmpeg \
-loop 1 -t 4 -i "${PREROLL}-0.jpg" \
-loop 1 -t 4 -i "${PREROLL}-1.jpg" \
-filter_complex \
"[0][1]xfade=transition=$TRANSITION:duration=1:offset=3[f0]" \
-map "[f0]" -r 25 -pix_fmt yuv420p -vcodec libx264 "${PREROLL}.mp4"
#rm "${PREROLL}"-*.jpg
