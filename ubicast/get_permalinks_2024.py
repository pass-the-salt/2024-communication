#!/usr/bin/env python3

import json
import requests

API=TODO
TOPSLUG="2024"
url = f"https://passthesalt.ubicast.tv/api/v2/channels/content/?api_key={API}&parent_slug={TOPSLUG}&content=v"

data = requests.get(url).json()

output = []

for video in data['videos']:
    video_info = {
        'title': video['title'],
        'slug': video['slug'],
        'video': f"https://passthesalt.ubicast.tv/permalink/{video['oid']}",
        'thumbnail': f"https://passthesalt.ubicast.tv/thumb/{video['oid']}/play/"
    }
    output.append(video_info)

output_json = json.dumps(output, indent=4)
print(output_json)
