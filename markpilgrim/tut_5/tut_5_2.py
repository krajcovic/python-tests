#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

s = '100 NORTH MAIN ROAD'
s = '100 NORTH BROAD ROAD'

print(re.sub('ROAD$', 'RD.', s))

s = '100 BROAD'
print(re.sub('\\bROAD$', 'RD.', s))
print(re.sub(r'\bROAD$', 'RD.', s))

s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD\b', 'RD.', s))