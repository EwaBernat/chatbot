#!/usr/bin/env python3
"""Kontrola układu druków: szerokości tabel i komórek względem szerokości kolumny tekstu."""
import sys, zipfile, glob, os
from lxml import etree

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
CONTENT_W = 11906 - 1080 - 1080  # 9746 DXA

def sprawdz(path):
    bledy = []
    with zipfile.ZipFile(path) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    for i, tbl in enumerate(root.iter(f"{{{NS['w']}}}tbl"), 1):
        grid = [int(c.get(f"{{{NS['w']}}}w")) for c in tbl.iter(f"{{{NS['w']}}}gridCol")]
        suma = sum(grid)
        if suma > CONTENT_W:
            bledy.append(f"tabela {i}: siatka {suma} DXA > {CONTENT_W} (wyjdzie poza margines)")
        tblw = tbl.find(f"{{{NS['w']}}}tblPr/{{{NS['w']}}}tblW")
        if tblw is not None and tblw.get(f"{{{NS['w']}}}type") == "dxa":
            dekl = int(tblw.get(f"{{{NS['w']}}}w"))
            if dekl != suma:
                bledy.append(f"tabela {i}: tblW={dekl} != suma kolumn {suma}")
        for r, tr in enumerate(tbl.findall(f"{{{NS['w']}}}tr"), 1):
            szer, span = 0, 0
            for tc in tr.findall(f"{{{NS['w']}}}tc"):
                tcw = tc.find(f"{{{NS['w']}}}tcPr/{{{NS['w']}}}tcW")
                gs = tc.find(f"{{{NS['w']}}}tcPr/{{{NS['w']}}}gridSpan")
                span += int(gs.get(f"{{{NS['w']}}}val")) if gs is not None else 1
                if tcw is not None and tcw.get(f"{{{NS['w']}}}type") == "dxa":
                    szer += int(tcw.get(f"{{{NS['w']}}}w"))
            if span != len(grid):
                bledy.append(f"tabela {i}, wiersz {r}: {span} kolumn wobec {len(grid)} w siatce")
            elif abs(szer - suma) > 2:
                bledy.append(f"tabela {i}, wiersz {r}: komórki {szer} DXA wobec siatki {suma}")
    return bledy

pliki = sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__), "out", "*.docx")))
zle = 0
for p in pliki:
    b = sprawdz(p)
    zle += len(b)
    print(f"{'✗' if b else '✓'} {os.path.basename(p)}")
    for x in b[:12]:
        print(f"    {x}")
print(f"\nProblemów: {zle}")
sys.exit(1 if zle else 0)
