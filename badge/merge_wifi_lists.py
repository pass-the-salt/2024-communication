#!/usr/bin/env python3
from unidecode import unidecode

START_DATE="20240101-000000"

with open(f"{START_DATE}_ppl1.txt") as f:
    bigl = [ll.rstrip().split(" ", 1) for ll in f.readlines()]
    l = [(unidecode(n.replace('-', ' ').replace('_', ' ')),c) for c,n in bigl]
bigd = dict(l)

with open(f"{START_DATE}_ppl_wifi_codes.csv") as f:
    bigl = [ll.rstrip().split(":", 1) for ll in f.readlines()]
    l = [(n.replace('.', ' ').replace('-', ' ').rstrip('1').rstrip('2').rstrip('3').rstrip(),w) for n,w in bigl]
bigd2 = dict(l)

bigl=[]
for k,v in bigd2.items():
    try:
        bigl.append(f"{bigd[k]}: {k:30} {v}")
    except:
        print(k, "FAIL")

with open(f"{START_DATE}_ppl_wifi_merged.txt", "w") as f:
    f.write('\n'.join(sorted(bigl)))
