"""Porządkuje kolejność krawędzi w <w:pBdr> zgodnie ze schematem OOXML (top, left, bottom, right)."""
import re, shutil, sys, zipfile

ORDER = ['top', 'left', 'bottom', 'right', 'between', 'bar']

def fix_xml(xml: str) -> str:
    def repl(m):
        inner = m.group(1)
        parts = re.findall(r'<w:(top|left|bottom|right|between|bar)\b[^>]*/>', inner)
        elems = re.findall(r'<w:(?:top|left|bottom|right|between|bar)\b[^>]*/>', inner)
        pairs = sorted(zip(parts, elems), key=lambda p: ORDER.index(p[0]))
        return '<w:pBdr>' + ''.join(e for _, e in pairs) + '</w:pBdr>'
    return re.sub(r'<w:pBdr>(.*?)</w:pBdr>', repl, xml, flags=re.S)

src = sys.argv[1]
tmp = src + '.tmp'
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename.endswith('.xml') and b'<w:pBdr>' in data:
            data = fix_xml(data.decode('utf-8')).encode('utf-8')
        zout.writestr(item, data)
shutil.move(tmp, src)
print('pBdr uporządkowane:', src)
