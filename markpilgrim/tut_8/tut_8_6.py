#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools

perms = itertools.permutations(set(range(3)), 2)
perms = itertools.permutations('ABC', 3)
print(list(itertools.permutations('ABC', 3)))
#perms = itertools.permutations([1, 2, 3], 2)
print(perms)
try:
    while True:
        print(next(perms))
except StopIteration:
    pass
finally:
    del perms

print(list(itertools.product('ABC', '123')))
print(list(itertools.permutations(['Zlin', 'Ostrava', 'Brno', 'Vyskov'], 2)))

