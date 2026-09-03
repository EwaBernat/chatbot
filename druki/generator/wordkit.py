# -*- coding: utf-8 -*-
"""Niskopoziomowe narzędzia OOXML dla python-docx (ramki, cieniowanie, tabele)."""
from docx.shared import Pt, Twips, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH

PX = 15.0  # 1 px CSS = 0.75 pt = 15 twips

def px2tw(px):
    return int(round(px * PX))

def px2pt(px):
    return px * 0.75


# ---------- kolejność elementów wg schematu OOXML ----------
ORDER = {
 'pPr': ['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr',
         'suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap',
         'overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd',
         'snapToGrid','spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc',
         'textDirection','textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr',
         'sectPr','pPrChange'],
 'rPr': ['rStyle','rFonts','b','bCs','i','iCs','caps','smallCaps','strike','dstrike','outline',
         'shadow','emboss','imprint','noProof','snapToGrid','vanish','webHidden','color','spacing',
         'w','kern','position','sz','szCs','highlight','u','effect','bdr','shd','fitText',
         'vertAlign','rtl','cs','em','lang','eastAsianLayout','specVanish','oMath'],
 'tblPr': ['tblStyle','tblpPr','tblOverlap','bidiVisual','tblStyleRowBandSize','tblStyleColBandSize',
           'tblW','jc','tblCellSpacing','tblInd','tblBorders','shd','tblLayout','tblCellMar',
           'tblLook','tblCaption','tblDescription','tblPrChange'],
 'tcPr': ['cnfStyle','tcW','gridSpan','hMerge','vMerge','tcBorders','shd','noWrap','tcMar',
          'textDirection','tcFitText','vAlign','hideMark','tcPrChange'],
 'trPr': ['cnfStyle','divId','gridBefore','gridAfter','wBefore','wAfter','cantSplit','trHeight',
          'tblHeader','tblCellSpacing','jc','hidden','ins','del','trPrChange'],
}

def _local(tag):
    return tag.split('}')[-1]

def insert_ordered(pr, child):
    """Wstawia element w miejscu zgodnym ze schematem OOXML."""
    seq = ORDER.get(_local(pr.tag))
    if not seq:
        pr.append(child)
        return child
    name = _local(child.tag)
    try:
        idx = seq.index(name)
    except ValueError:
        pr.append(child)
        return child
    for existing in pr:
        ename = _local(existing.tag)
        try:
            eidx = seq.index(ename)
        except ValueError:
            continue
        if eidx > idx:
            existing.addprevious(child)
            return child
    pr.append(child)
    return child

def drop(pr, name):
    for e in pr.findall(qn('w:' + name)):
        pr.remove(e)

def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn('w:' + k), str(v))
    return e

# ---------- cieniowanie ----------

def shade(pr, fill):
    drop(pr, 'shd')
    insert_ordered(pr, _el('w:shd', val='clear', color='auto', fill=fill))

def run_shade(run, fill):
    shade(run._element.get_or_add_rPr(), fill)

def par_shade(par, fill):
    shade(par._p.get_or_add_pPr(), fill)

def cell_shade(cell, fill):
    shade(cell._tc.get_or_add_tcPr(), fill)

# ---------- ramki ----------

def _borders_el(pr, tagname, spec, order):
    drop(pr, tagname.split(':')[1])
    b = OxmlElement(tagname)
    for side in order:
        if side not in spec:
            continue
        s = spec[side]
        e = OxmlElement('w:' + side)
        if s is None:
            e.set(qn('w:val'), 'nil')
        else:
            if len(s) == 3:
                sz, color, style = s
            else:
                (sz, color), style = s, 'single'
            e.set(qn('w:val'), style)
            e.set(qn('w:sz'), str(sz))
            e.set(qn('w:space'), '0')
            e.set(qn('w:color'), color)
        b.append(e)
    insert_ordered(pr, b)

def par_borders(par, **spec):
    """spec: top/left/bottom/right = (sz, 'RRGGBB') albo None"""
    _borders_el(par._p.get_or_add_pPr(), 'w:pBdr',
                spec, ['top', 'left', 'bottom', 'right'])

def cell_borders(cell, **spec):
    _borders_el(cell._tc.get_or_add_tcPr(), 'w:tcBorders',
                spec, ['top', 'left', 'bottom', 'right'])

def table_borders(table, **spec):
    _borders_el(table._tbl.tblPr, 'w:tblBorders', spec,
                ['top', 'left', 'bottom', 'right', 'insideH', 'insideV'])

# ---------- tabele ----------

def cell_margins(table, top=0, left=0, bottom=0, right=0):
    pr = table._tbl.tblPr
    drop(pr, 'tblCellMar')
    m = OxmlElement('w:tblCellMar')
    for name, val in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement('w:' + name)
        e.set(qn('w:w'), str(int(val)))
        e.set(qn('w:type'), 'dxa')
        m.append(e)
    insert_ordered(pr, m)

def table_indent(table, tw):
    pr = table._tbl.tblPr
    drop(pr, 'tblInd')
    e = OxmlElement('w:tblInd')
    e.set(qn('w:w'), str(int(tw)))
    e.set(qn('w:type'), 'dxa')
    insert_ordered(pr, e)

def fixed_layout(table):
    pr = table._tbl.tblPr
    drop(pr, 'tblLayout')
    e = OxmlElement('w:tblLayout')
    e.set(qn('w:type'), 'fixed')
    insert_ordered(pr, e)

def set_widths(table, widths_tw):
    fixed_layout(table)
    table.autofit = False
    widths_tw = [int(w) for w in widths_tw]
    # tblW = suma kolumn (inaczej LibreOffice/Word skalują tabelę)
    pr = table._tbl.tblPr
    drop(pr, 'tblW')
    w = OxmlElement('w:tblW')
    w.set(qn('w:w'), str(sum(widths_tw)))
    w.set(qn('w:type'), 'dxa')
    insert_ordered(pr, w)
    # tblGrid decyduje o realnej szerokości kolumn
    grid = table._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        cols = grid.findall(qn('w:gridCol'))
        for i, gc in enumerate(cols):
            if i < len(widths_tw):
                gc.set(qn('w:w'), str(widths_tw[i]))
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths_tw):
                cell.width = Twips(widths_tw[i])

def row_height(row, pt, exact=True):
    row.height = Pt(pt)
    row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY if exact else WD_ROW_HEIGHT_RULE.AT_LEAST

def keep_together(par):
    pPr = par._p.get_or_add_pPr()
    for tag in ('w:keepNext', 'w:keepLines'):
        if pPr.find(qn(tag)) is None:
            insert_ordered(pPr, OxmlElement(tag))

def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn('w:cantSplit')) is None:
        insert_ordered(trPr, OxmlElement('w:cantSplit'))

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    insert_ordered(trPr, OxmlElement('w:tblHeader'))

def vmerge(cell, val):
    e = OxmlElement('w:vMerge')
    e.set(qn('w:val'), val)
    insert_ordered(cell._tc.get_or_add_tcPr(), e)

def valign(cell, v='center'):
    pr = cell._tc.get_or_add_tcPr()
    drop(pr, 'vAlign')
    e = OxmlElement('w:vAlign')
    e.set(qn('w:val'), v)
    insert_ordered(pr, e)

# ---------- akapity ----------

def tune(par, before=0, after=0, line=None, exact=False, align=None,
         left=0, right=0, first=None, keep=False):
    pf = par.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if line is not None:
        pf.line_spacing = Pt(line) if exact else line
    if align is not None:
        par.alignment = align
    pf.left_indent = Twips(int(left))
    pf.right_indent = Twips(int(right))
    if first is not None:
        pf.first_line_indent = Twips(int(first))
    if keep:
        keep_together(par)
    return par

def run(par, text, size=9, bold=False, italic=False, color=None, font=None,
        caps=False, underline=None, spacing=None, fill=None):
    r = par.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    r.font.name = font or 'Segoe UI'
    rPr = r._element.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts')
        rPr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rf.set(qn(a), r.font.name)
    if caps:
        insert_ordered(rPr, OxmlElement('w:caps'))
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), underline)
        insert_ordered(rPr, u)
    if spacing is not None:
        sp = OxmlElement('w:spacing')
        sp.set(qn('w:val'), str(int(spacing)))
        insert_ordered(rPr, sp)
    if fill:
        run_shade(r, fill)
    return r

def tabstop(par, pos_tw, align='right', leader=None):
    pPr = par._p.get_or_add_pPr()
    tabs = pPr.find(qn('w:tabs'))
    if tabs is None:
        tabs = OxmlElement('w:tabs')
        insert_ordered(pPr, tabs)
    t = OxmlElement('w:tab')
    t.set(qn('w:val'), align)
    t.set(qn('w:pos'), str(int(pos_tw)))
    if leader:
        t.set(qn('w:leader'), leader)
    tabs.append(t)
