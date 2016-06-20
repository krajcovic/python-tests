#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

pattern = r'\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$'
phonePattern = re.compile(pattern)
print(phonePattern.search('work 1 -(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('(800)5551212 x1234').groups())

phonePattern = re.compile(r'''
# nevázat se na začátek řetězce, číslo může začít kdekoliv
(\d{3}) # číslo oblasti má 3 číslice (např. '800')
\D* # nepovinný oddělovač - libovolný počet nenumerických znaků
(\d{3}) # číslo hlavní linky má 3 číslice (např. '555')
\D* # nepovinný oddělovač
(\d{4}) # zbytek čísla má 4 číslice (např. '1212')
\D* # nepovinný oddělovač
(\d*) # nepovinná klapka - libovolný počet číslic
$ # konec řetězce
''', re.VERBOSE)

print(phonePattern.search('work 1 -(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('(800)5551212 x1234').groups())
