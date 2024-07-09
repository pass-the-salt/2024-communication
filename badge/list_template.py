#!/usr/bin/env python3

import sys
import os

YEAR=2024
START_DATE="20240101-000000"
#START_DATE="20240622-235959"
ERASE_LAST=True
# Badges per template
N=8
TEMPLATE=f"templates/badge_{YEAR}_{sys.argv[0].replace('./list_', '').replace('.py', '')}.svg"
SEPARATOR='~'

src=f"{START_DATE}_{sys.argv[0].replace('./list_', '').replace('.py', '')}.txt"
basename=os.path.basename(src)
with open(src) as f:
    l=[[lll.rstrip() for lll in ll.split(SEPARATOR)] for ll in f.readlines()]

for p in range((len(l)+N-1)//N):
    pl=l[p*N:(p+1)*N]
    for x in pl:
        if len(x)!=4:
            print("Error on this line, expected 4 elements, got:", x)
    with open(TEMPLATE) as f:
        t=f.read()
    for on,fn,ln,tn in pl:
        t=t.replace("xxxxxxxx01", fn.strip().replace("&", "&amp;"), 1)
        t=t.replace("xxxxxxxx02", ln.strip().replace("&", "&amp;"), 1)
        t=t.replace("xxxxxxxx03", tn.strip().replace("&", "&amp;"), 1)
        t=t.replace("xxx04", on.strip(), 1)
    if ERASE_LAST:
        t=t.replace("xxxxxxxx01", "")
        t=t.replace("xxxxxxxx02", "")
        t=t.replace("xxxxxxxx03", "")
        t=t.replace("xxx04", "")
    with open(basename.replace('.txt', '_') + "%02i.svg" % p, "w") as f:
        f.write(t)
#    subprocess.run(["inkscape", basename + "%02i.svg" % p, "--export-plain-svg=" + basename + "%02i_flatten.svg" % p, "--export-text-to-path"])
