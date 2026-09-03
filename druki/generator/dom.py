# -*- coding: utf-8 -*-
"""Minimalny parser HTML -> drzewo Node."""
from html.parser import HTMLParser

VOID = {'br','img','input','hr','meta','link','col','source'}

class Node:
    __slots__ = ('tag','attrs','children','parent','text')
    def __init__(self, tag, attrs=None, text=None, parent=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []
        self.parent = parent
        self.text = text
    # -- pomocnicze --
    @property
    def cls(self):
        return self.attrs.get('class','').split()
    def has(self, c):
        return c in self.cls
    @property
    def style(self):
        return parse_style(self.attrs.get('style',''))
    def find_all(self, tag=None, cls=None):
        out = []
        for ch in self.children:
            if ch.tag == '#text':
                continue
            if (tag is None or ch.tag == tag) and (cls is None or ch.has(cls)):
                out.append(ch)
            out.extend(ch.find_all(tag, cls))
        return out
    def all_text(self):
        if self.tag == '#text':
            return self.text
        return ''.join(c.all_text() for c in self.children)
    def __repr__(self):
        if self.tag == '#text':
            return '#text(%r)' % (self.text[:30],)
        return '<%s class=%r kids=%d>' % (self.tag, self.attrs.get('class',''), len(self.children))


def parse_style(s):
    d = {}
    for part in s.split(';'):
        if ':' in part:
            k, v = part.split(':', 1)
            d[k.strip().lower()] = v.strip()
    return d


class _P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root')
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        n = Node(tag, dict(attrs), parent=self.stack[-1])
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)
    def handle_startendtag(self, tag, attrs):
        n = Node(tag, dict(attrs), parent=self.stack[-1])
        self.stack[-1].children.append(n)
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
    def handle_data(self, data):
        if data.strip() == '' and '\n' in data:
            data = ' ' if data else ''
            if not data.strip():
                # zachowaj pojedynczą spację tylko jeśli nie jest to wcięcie
                self.stack[-1].children.append(Node('#text', text=' ', parent=self.stack[-1]))
                return
        self.stack[-1].children.append(Node('#text', text=data, parent=self.stack[-1]))


def parse_html(html):
    p = _P()
    p.feed(html)
    return p.root
