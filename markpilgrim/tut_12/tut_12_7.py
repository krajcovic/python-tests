#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree

import lxml.etree

new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
                         attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print(etree.tostring(new_feed))

NSMAP = {None: 'http://www.w3.org/2005/Atom'}
new_feed = lxml.etree.Element('feed', nsmap=NSMAP)
print(lxml.etree.tounicode(new_feed))
new_feed.set('{http://www.w3.org/XML/1998/namespace}lang', 'en')
print(lxml.etree.tounicode(new_feed))
