#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
pattern = '^M?M?M?$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, 'MMMM'))
print(re.search(pattern, ''))