#!/bin/bash

API=TODO
# Available top slugs:
# wget -q -O - "https://passthesalt.ubicast.tv/api/v2/channels/content/?api_key=$API"|json_pp|awk -F'"' '/slug/{print $4}'
#TOPSLUG=2018
TOPSLUG=2024
echo "TOPSLUG=$TOPSLUG"
n=1
# 0 because of hidden rumps video
rn=0
for OID in $(wget -q -O - "https://passthesalt.ubicast.tv/api/v2/channels/content/?api_key=$API&parent_slug=$TOPSLUG&content=v"|json_pp|egrep "\"oid\""|grep -o "v[[:alnum:]]*"|tac); do
    echo "OID=$OID"

    SLUG=$(wget -q -O - "https://passthesalt.ubicast.tv/api/v2/medias/get/?api_key=$API&oid=$OID&full=yes"|json_pp|grep "^      \"slug"|sed 's/.*slug" : "\(.*\)".*/\1/')
    echo "SLUG=$SLUG"

    MP4=$(wget -q -O - "https://passthesalt.ubicast.tv/videos/$SLUG" |grep download-mp4|sed 's/.*href=.//;s/".*//')
    if [[ "$SLUG" =~ rump ]]; then
        wget -c -O "PTS${TOPSLUG}-Rump-$(printf %02i $rn)-${SLUG/202?-rump-/}.mp4" "https://passthesalt.ubicast.tv$MP4"
        rn=$((rn+1))
    else
        wget -c -O "PTS${TOPSLUG}-Talk-$(printf %02i $n)-${SLUG/202?-/}.mp4" "https://passthesalt.ubicast.tv$MP4"
        n=$((n+1))
    fi
done
