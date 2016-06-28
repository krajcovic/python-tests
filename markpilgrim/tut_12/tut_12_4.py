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

print(root.findall('{http://www.w3.org/2005/Atom}entry'))
print(root.findall('entry'))
print(root.tag)

print(root.findall('{http://www.w3.org/2005/Atom}feed'))
print(root.findall('{http://www.w3.org/2005/Atom}author'))
entries = tree.findall('{http://www.w3.org/2005/Atom}entry')
print(len(entries))

for entry in entries:
    title_element = entry.find('{http://www.w3.org/2005/Atom}title')
    print(title_element, title_element.text)
    foo_element = entry.find('{http://www.w3.org/2005/Atom}foo')
    print(foo_element, type(foo_element))

all_links = tree.findall('.//{http://www.w3.org/2005/Atom}link')
for link in all_links:
    print(link.attrib)


