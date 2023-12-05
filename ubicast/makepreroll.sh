#!/bin/bash


PREROLL=preroll_pts2023_16x9
libreoffice --headless --convert-to pdf "${PREROLL}.odp"
convert -density 300 "${PREROLL}.pdf" -resize 1280x720 "${PREROLL}.jpg"
TRANSITION=smoothleft
rm "${PREROLL}.mp4"
ffmpeg \
-loop 1 -t 4 -i "${PREROLL}-0.jpg" \
-loop 1 -t 4 -i "${PREROLL}-1.jpg" \
-loop 1 -t 4 -i "${PREROLL}-2.jpg" \
-filter_complex \
"[0][1]xfade=transition=$TRANSITION:duration=1:offset=3[f0]; \
[f0][2]xfade=transition=$TRANSITION:duration=1:offset=6[f1]" \
-map "[f1]" -r 25 -pix_fmt yuv420p -vcodec libx264 "${PREROLL}.mp4"
rm "${PREROLL}.pdf" "${PREROLL}"-*.jpg
