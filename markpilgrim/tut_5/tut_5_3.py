#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
pattern = '^M?M?M?$'
result = re.search(pattern, 'M')
print(result)

print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, 'MMMM'))
print(re.search(pattern, ''))

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC'))
print(re.search(pattern, ''))

pattern = '^M{0,3}$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, 'MMMM'))
print(re.search(pattern, ''))

pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern, 'MCMXL'))
print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MCML'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MCMLX'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'MCMLXXX'))
print(re.search(pattern, 'I'))
print(re.search(pattern, 'MCMLXXXX'))
print(re.search(pattern, ''))

pattern = '''
^                       # zacatek retezce
M{0,3}                  # tisice - 0 az 3 M
(CM|CD|D?C{0,3})        # stovky
(XC|XL|L?X{0,3})        # desitky
(IX,IV|V?I{0,3})        # jednotky
$                       # konec retezce
'''
print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))

