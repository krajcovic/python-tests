#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
    from lxml import etree
except ImportError:
    pass
    # import xml.etree.ElementTree as etree

tree = etree.parse('feed.xml')
print(tree.findall('.//{http://www.w3.org/2005/Atom}*[@href]'))
print(tree.findall("//{http://www.w3.org/2005/Atom}*[@href='http://diveintomark.org/']"))

NS = '{http://www.w3.org/2005/Atom}'
print(tree.findall('//{NS}author[{NS}uri]'.format(NS=NS)))

NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}
entries = tree.xpath("//atom:category[@term='accessibility']/..", namespaces=NSMAP)
print(entries)
entry = entries[0]
print(entry)
print(entry.xpath('./atom:title/text()', namespaces=NSMAP))

