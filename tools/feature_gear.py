# -*- coding: utf-8 -*-
"""Swap article image to the real gear photo and make the gear article the
featured post in each language's blog index (old tolerances becomes a row)."""
import os, re

BASE = r'C:\Users\druzh\bibparts'
SLUG = 'custom-gear-manufacturing'
OLD_IMG = '/assets/images/powder-metal-1.webp'
NEW_IMG = '/assets/images/custom-gear-manufacturing.webp'
TOL = 'cnc-machining-tolerances'
LANGS = ['en', 'de', 'es', 'fr', 'pl']

# 1) swap cover/og image in the 5 article files
for l in LANGS:
    p = os.path.join(BASE, l, 'blog', SLUG, 'index.html')
    s = open(p, encoding='utf-8').read()
    s = s.replace(OLD_IMG, NEW_IMG)
    open(p, 'w', encoding='utf-8').write(s)

# 2) blog index: make gear featured, demote tolerances to a row
for l in LANGS:
    p = os.path.join(BASE, l, 'blog', 'index.html')
    s = open(p, encoding='utf-8').read()

    # --- capture current featured (tolerances) ---
    feat = re.search(r'<a href="/' + l + r'/blog/' + TOL + r'/" class="post-featured".*?</a>', s, re.S).group(0)
    tol_cat = re.search(r'class="post-featured" data-cat="([^"]*)"', feat).group(1)
    tol_img = re.search(r'<img[^>]*>', feat, re.S).group(0)
    tol_catlbl = re.search(r'<span class="post-cat">(.*?)</span>', feat, re.S).group(1).strip()
    tol_date = re.search(r'<span class="post-date">(.*?)</span>', feat, re.S).group(1).strip()
    tol_title = re.search(r'<div class="post-title">(.*?)</div>', feat, re.S).group(1).strip()
    tol_excerpt = re.search(r'<div class="post-excerpt">(.*?)</div>', feat, re.S).group(1).strip()
    badge = re.search(r'<span class="featured-badge">(.*?)</span>', feat, re.S).group(1).strip()
    readmore = re.search(r'<span class="post-read-more">(.*?)</span>', feat, re.S).group(1).strip()

    # --- capture the gear post-row we inserted earlier ---
    gear_row = re.search(r'[ \t]*<!-- POST: ' + SLUG + r' -->.*?</a>', s, re.S).group(0)
    g_cat = re.search(r'class="post-row" data-cat="([^"]*)"', gear_row).group(1)
    g_catlbl = re.search(r'<span class="post-cat">(.*?)</span>', gear_row, re.S).group(1).strip()
    g_date = re.search(r'<span class="post-date">(.*?)</span>', gear_row, re.S).group(1).strip()
    g_title = re.search(r'<div class="post-row-title">(.*?)</div>', gear_row, re.S).group(1).strip()
    g_excerpt = re.search(r'<div class="post-row-excerpt">(.*?)</div>', gear_row, re.S).group(1).strip()
    g_alt = re.search(r'<img[^>]*alt="([^"]*)"', gear_row).group(1)

    # remove the gear post-row from its current spot
    s = re.sub(r'[ \t]*<!-- POST: ' + SLUG + r' -->.*?</a>\n*', '', s, count=1, flags=re.S)

    # build new gear FEATURED block (uses the real photo)
    gear_feat = (
        '<a href="/' + l + '/blog/' + SLUG + '/" class="post-featured" data-cat="' + g_cat + '">\n'
        '        <div class="post-featured-img">\n'
        '          <img loading="lazy" src="' + NEW_IMG + '" alt="' + g_alt + '">\n'
        '        </div>\n'
        '        <div class="post-featured-body">\n'
        '          <span class="featured-badge">' + badge + '</span>\n'
        '          <div class="post-meta">\n'
        '            <span class="post-cat">' + g_catlbl + '</span>\n'
        '            <span class="post-sep">&middot;</span>\n'
        '            <span class="post-date">' + g_date + '</span>\n'
        '          </div>\n'
        '          <div class="post-title">' + g_title + '</div>\n'
        '          <div class="post-excerpt">' + g_excerpt + '</div>\n'
        '          <span class="post-read-more">' + readmore + '</span>\n'
        '        </div>\n'
        '      </a>')

    # build tolerances as a ROW (keeps its own image/title/excerpt)
    tol_row = (
        '<a href="/' + l + '/blog/' + TOL + '/" class="post-row" data-cat="' + tol_cat + '">\n'
        '        <div class="post-row-img">\n'
        '          ' + tol_img + '\n'
        '        </div>\n'
        '        <div class="post-row-body">\n'
        '          <div class="post-meta">\n'
        '            <span class="post-cat">' + tol_catlbl + '</span>\n'
        '            <span class="post-sep">&middot;</span>\n'
        '            <span class="post-date">' + tol_date + '</span>\n'
        '          </div>\n'
        '          <div class="post-row-title">' + tol_title + '</div>\n'
        '          <div class="post-row-excerpt">' + tol_excerpt + '</div>\n'
        '        </div>\n'
        '      </a>')

    s = s.replace(feat, gear_feat + '\n\n      ' + tol_row)
    open(p, 'w', encoding='utf-8').write(s)
    print('featured swapped', l)
print('done')
