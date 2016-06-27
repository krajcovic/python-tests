#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
tree = etree.parse('feed.xml')
root = tree.getroot()
# print(help(root))
print(root)
print(root.tag)
print(len(root))
for child in root:
    print(child, child.attrib)

root.findall('{http://www.w3.org/2005/Atom}entry')

