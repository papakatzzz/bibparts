# -*- coding: utf-8 -*-
"""Replace em-dash (U+2014) with ' - ' across all HTML files, collapsing
surrounding spaces/tabs (not newlines). Leaves en-dash (U+2013) untouched."""
import os, re

BASE = r'C:\Users\druzh\bibparts'
pat = re.compile(r'[ \t]*—[ \t]*')

changed = 0
total = 0
for root, dirs, files in os.walk(BASE):
    if '.git' in root:
        continue
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(root, fn)
        s = open(p, encoding='utf-8').read()
        n = s.count('—')
        if n:
            s = pat.sub(' - ', s)
            open(p, 'w', encoding='utf-8').write(s)
            changed += 1
            total += n
            print(os.path.relpath(p, BASE), n)
print('files changed:', changed, 'em-dashes replaced:', total)
